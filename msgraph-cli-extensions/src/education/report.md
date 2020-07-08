# Azure CLI Module Creation Report

### education education create-class

create-class a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-class|CreateClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|Name of the class.|display_name|displayName|
|**--mail-nickname**|string|Mail name for sending email to all members, if this is enabled.|mail_nickname|mailNickname|
|**--description**|string|Description of the class.|description|description|
|**--class-code**|string|Class code used by the school to identify the class.|class_code|classCode|
|**--external-name**|string|Name of the class in the syncing system.|external_name|externalName|
|**--external-id**|string|ID of the class from the syncing system.|external_id|externalId|
|**--external-source**|choice|educationExternalSource|external_source|externalSource|
|**--grade**|string||grade|grade|
|**--term**|object|educationTerm|term|term|
|**--course**|object|educationCourse|course|course|
|**--assignments**|array||assignments|assignments|
|**--assignment-categories**|array||assignment_categories|assignmentCategories|
|**--members**|array|All users in the class. Nullable.|members|members|
|**--teachers**|array|All teachers in the class. Nullable.|teachers|teachers|
|**--schools**|array|All schools that this class is associated with. Nullable.|schools|schools|
|**--group**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|group|group|
|**--created-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|

### education education create-school

create-school a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-school|CreateSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|Organization display name.|display_name|displayName|
|**--description**|string|Organization description.|description|description|
|**--external-source**|choice|educationExternalSource|external_source|externalSource|
|**--principal-email**|string|Email address of the principal.|principal_email|principalEmail|
|**--principal-name**|string|Name of the principal.|principal_name|principalName|
|**--external-principal-id**|string|ID of principal in syncing system.|external_principal_id|externalPrincipalId|
|**--lowest-grade**|string|Lowest grade taught.|lowest_grade|lowestGrade|
|**--highest-grade**|string|Highest grade taught.|highest_grade|highestGrade|
|**--school-number**|string|School Number.|school_number|schoolNumber|
|**--external-id**|string|ID of school in syncing system.|external_id|externalId|
|**--phone**|string|Phone number of school.|phone|phone|
|**--fax**|string||fax|fax|
|**--address**|object|physicalAddress|address|address|
|**--classes**|array|Classes taught at the school. Nullable.|classes|classes|
|**--users**|array|Users in the school. Nullable.|users|users|
|**--administrative-unit-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--administrative-unit-deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--administrative-unit-display-name**|string||microsoft_graph_administrative_unit_display_name|displayName|
|**--administrative-unit-description**|string||microsoft_graph_administrative_unit_description|description|
|**--administrative-unit-visibility**|string||visibility|visibility|
|**--administrative-unit-members**|array||members|members|
|**--administrative-unit-scoped-role-members**|array||scoped_role_members|scopedRoleMembers|
|**--administrative-unit-extensions**|array||extensions|extensions|
|**--created-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|

### education education create-synchronization-profile

create-synchronization-profile a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-synchronization-profile|CreateSynchronizationProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--data-provider**|any|Any object|data_provider|dataProvider|
|**--identity-synchronization-configuration**|any|Any object|identity_synchronization_configuration|identitySynchronizationConfiguration|
|**--licenses-to-assign**|array||licenses_to_assign|licensesToAssign|
|**--state**|choice|educationSynchronizationProfileState|state|state|
|**--handle-special-character-constraint**|boolean||handle_special_character_constraint|handleSpecialCharacterConstraint|
|**--errors**|array||errors|errors|
|**--profile-status**|object|educationSynchronizationProfileStatus|profile_status|profileStatus|

### education education create-user

create-user a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-user|CreateUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New navigation property|body|body|

### education education get-class

get-class a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-class|GetClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education get-me

get-me a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-me|GetMe|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education get-school

get-school a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-school|GetSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: educationSchool-id of educationSchool|education_school_id|educationSchool-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education get-synchronization-profile

get-synchronization-profile a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-synchronization-profile|GetSynchronizationProfiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: educationSynchronizationProfile-id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education get-user

get-user a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user|GetUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education list-class

list-class a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-class|ListClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education list-school

list-school a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-school|ListSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education list-synchronization-profile

list-synchronization-profile a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

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

### education education list-user

list-user a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-user|ListUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education update

update a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateClasses|
|update|UpdateSchools|
|update|UpdateSynchronizationProfiles|
|update|UpdateUsers|
|update|UpdateMe|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-school-id**|string|key: educationSchool-id of educationSchool|education_school_id|educationSchool-id|
|**--education-synchronization-profile-id**|string|key: educationSynchronizationProfile-id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--body**|object|New navigation property values|body|body|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|Name of the class.|display_name|displayName|
|**--mail-nickname**|string|Mail name for sending email to all members, if this is enabled.|mail_nickname|mailNickname|
|**--description**|string|Description of the class.|description|description|
|**--class-code**|string|Class code used by the school to identify the class.|class_code|classCode|
|**--external-name**|string|Name of the class in the syncing system.|external_name|externalName|
|**--external-id**|string|ID of the class from the syncing system.|external_id|externalId|
|**--external-source**|choice|educationExternalSource|external_source|externalSource|
|**--grade**|string||grade|grade|
|**--term**|object|educationTerm|term|term|
|**--course**|object|educationCourse|course|course|
|**--assignments**|array||assignments|assignments|
|**--assignment-categories**|array||assignment_categories|assignmentCategories|
|**--members**|array|All users in the class. Nullable.|members|members|
|**--teachers**|array|All teachers in the class. Nullable.|teachers|teachers|
|**--schools**|array|All schools that this class is associated with. Nullable.|schools|schools|
|**--group**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|group|group|
|**--created-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--principal-email**|string|Email address of the principal.|principal_email|principalEmail|
|**--principal-name**|string|Name of the principal.|principal_name|principalName|
|**--external-principal-id**|string|ID of principal in syncing system.|external_principal_id|externalPrincipalId|
|**--lowest-grade**|string|Lowest grade taught.|lowest_grade|lowestGrade|
|**--highest-grade**|string|Highest grade taught.|highest_grade|highestGrade|
|**--school-number**|string|School Number.|school_number|schoolNumber|
|**--phone**|string|Phone number of school.|phone|phone|
|**--fax**|string||fax|fax|
|**--address**|object|physicalAddress|address|address|
|**--classes**|array|Classes taught at the school. Nullable.|classes|classes|
|**--users**|array|Users in the school. Nullable.|users|users|
|**--administrative-unit-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--administrative-unit-deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--administrative-unit-display-name**|string||microsoft_graph_administrative_unit_display_name|displayName|
|**--administrative-unit-description**|string||microsoft_graph_administrative_unit_description|description|
|**--administrative-unit-visibility**|string||visibility|visibility|
|**--administrative-unit-members**|array||members|members|
|**--administrative-unit-scoped-role-members**|array||scoped_role_members|scopedRoleMembers|
|**--administrative-unit-extensions**|array||extensions|extensions|
|**--data-provider**|any|Any object|data_provider|dataProvider|
|**--identity-synchronization-configuration**|any|Any object|identity_synchronization_configuration|identitySynchronizationConfiguration|
|**--licenses-to-assign**|array||licenses_to_assign|licensesToAssign|
|**--state**|choice|educationSynchronizationProfileState|state|state|
|**--handle-special-character-constraint**|boolean||handle_special_character_constraint|handleSpecialCharacterConstraint|
|**--errors**|array||errors|errors|
|**--profile-status**|object|educationSynchronizationProfileStatus|profile_status|profileStatus|

### education education-class create-assignment

create-assignment a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-assignment|CreateAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--id**|string|Read-only.|id|id|
|**--class-id**|string||class_id|classId|
|**--display-name**|string||display_name|displayName|
|**--instructions**|object|educationItemBody|instructions|instructions|
|**--close-date-time**|date-time||close_date_time|closeDateTime|
|**--due-date-time**|date-time||due_date_time|dueDateTime|
|**--assign-date-time**|date-time||assign_date_time|assignDateTime|
|**--assigned-date-time**|date-time||assigned_date_time|assignedDateTime|
|**--grading**|any|Any object|grading|grading|
|**--assign-to**|any|Any object|assign_to|assignTo|
|**--allow-late-submissions**|boolean||allow_late_submissions|allowLateSubmissions|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--allow-students-to-add-resources-to-submission**|boolean||allow_students_to_add_resources_to_submission|allowStudentsToAddResourcesToSubmission|
|**--status**|choice|educationAssignmentStatus|status|status|
|**--resources**|array||resources|resources|
|**--submissions**|array||submissions|submissions|
|**--categories**|array||categories|categories|
|**--rubric-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--rubric-display-name**|string||microsoft_graph_education_rubric_display_name|displayName|
|**--rubric-description**|object|educationItemBody|description|description|
|**--rubric-qualities**|array||qualities|qualities|
|**--rubric-levels**|array||levels|levels|
|**--rubric-grading**|any|Any object|any_grading|grading|
|**--rubric-created-date-time**|date-time||microsoft_graph_education_rubric_created_date_time_created_date_time|createdDateTime|
|**--rubric-last-modified-date-time**|date-time||microsoft_graph_education_rubric_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--rubric-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--rubric-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--rubric-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--rubric-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--rubric-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--rubric-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--rubric-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--rubric-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--rubric-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--rubric-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--rubric-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--rubric-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id11|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name11|displayName|

### education education-class create-assignment-category

create-assignment-category a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-assignment-category|CreateAssignmentCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### education education-class delta

delta a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### education education-class get-assignment

get-assignment a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assignment|GetAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class get-assignment-category

get-assignment-category a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assignment-category|GetAssignmentCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-category-id**|string|key: educationCategory-id of educationCategory|education_category_id|educationCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class get-group

get-group a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-group|GetGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class get-member

get-member a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member|GetMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class get-school

get-school a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-school|GetSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-school-id**|string|key: educationSchool-id of educationSchool|education_school_id|educationSchool-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class get-teacher

get-teacher a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-teacher|GetTeachers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class list-assignment

list-assignment a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-assignment|ListAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class list-assignment-category

list-assignment-category a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-assignment-category|ListAssignmentCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class list-member

list-member a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member|ListMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class list-school

list-school a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-school|ListSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class list-teacher

list-teacher a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-teacher|ListTeachers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class update

update a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateAssignmentCategories|
|update|UpdateAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-category-id**|string|key: educationCategory-id of educationCategory|education_category_id|educationCategory-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--class-id**|string||class_id|classId|
|**--instructions**|object|educationItemBody|instructions|instructions|
|**--close-date-time**|date-time||close_date_time|closeDateTime|
|**--due-date-time**|date-time||due_date_time|dueDateTime|
|**--assign-date-time**|date-time||assign_date_time|assignDateTime|
|**--assigned-date-time**|date-time||assigned_date_time|assignedDateTime|
|**--grading**|any|Any object|grading|grading|
|**--assign-to**|any|Any object|assign_to|assignTo|
|**--allow-late-submissions**|boolean||allow_late_submissions|allowLateSubmissions|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--allow-students-to-add-resources-to-submission**|boolean||allow_students_to_add_resources_to_submission|allowStudentsToAddResourcesToSubmission|
|**--status**|choice|educationAssignmentStatus|status|status|
|**--resources**|array||resources|resources|
|**--submissions**|array||submissions|submissions|
|**--categories**|array||categories|categories|
|**--rubric-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--rubric-display-name**|string||microsoft_graph_education_rubric_display_name|displayName|
|**--rubric-description**|object|educationItemBody|description|description|
|**--rubric-qualities**|array||qualities|qualities|
|**--rubric-levels**|array||levels|levels|
|**--rubric-grading**|any|Any object|any_grading|grading|
|**--rubric-created-date-time**|date-time||microsoft_graph_education_rubric_created_date_time_created_date_time|createdDateTime|
|**--rubric-last-modified-date-time**|date-time||microsoft_graph_education_rubric_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--rubric-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--rubric-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--rubric-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--rubric-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--rubric-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--rubric-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--rubric-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--rubric-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--rubric-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--rubric-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--rubric-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--rubric-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id11|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name11|displayName|

### education education-class-assignment create-category

create-category a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-category|CreateCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### education education-class-assignment create-resource

create-resource a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-resource|CreateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-class-assignment create-submission

create-submission a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-submission|CreateSubmissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--recipient**|any|Any object|recipient|recipient|
|**--status**|choice|educationSubmissionStatus|status|status|
|**--submitted-date-time**|date-time||submitted_date_time|submittedDateTime|
|**--unsubmitted-date-time**|date-time||unsubmitted_date_time|unsubmittedDateTime|
|**--released-date-time**|date-time||released_date_time|releasedDateTime|
|**--returned-date-time**|date-time||returned_date_time|returnedDateTime|
|**--resources-folder-url**|string||resources_folder_url|resourcesFolderUrl|
|**--resources**|array||resources|resources|
|**--submitted-resources**|array||submitted_resources|submittedResources|
|**--outcomes**|array||outcomes|outcomes|
|**--returned-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--returned-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--returned-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--returned-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--returned-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--returned-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--released-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--released-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--released-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--released-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--released-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--released-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--unsubmitted-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--unsubmitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--unsubmitted-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--unsubmitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--unsubmitted-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--unsubmitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--submitted-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--submitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--submitted-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--submitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--submitted-by-application-id**|string|Unique identifier for the identity.|id11|id|
|**--submitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|

### education education-class-assignment get-category

get-category a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-category|GetCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: educationCategory-id of educationCategory|education_category_id|educationCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class-assignment get-resource

get-resource a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource|GetResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: educationAssignmentResource-id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class-assignment get-resource-folder-url

get-resource-folder-url a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource-folder-url|getResourcesFolderUrl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|

### education education-class-assignment get-rubric

get-rubric a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-rubric|GetRubric|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class-assignment get-submission

get-submission a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-submission|GetSubmissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class-assignment list-category

list-category a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-category|ListCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class-assignment list-resource

list-resource a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-resource|ListResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class-assignment list-submission

list-submission a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-submission|ListSubmissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class-assignment publish

publish a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|publish|publish|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|

### education education-class-assignment update

update a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateCategories|
|update|UpdateResources|
|update|UpdateSubmissions|
|update|UpdateRubric|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: educationCategory-id of educationCategory|education_category_id|educationCategory-id|
|**--education-assignment-resource-id**|string|key: educationAssignmentResource-id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--recipient**|any|Any object|recipient|recipient|
|**--status**|choice|educationSubmissionStatus|status|status|
|**--submitted-date-time**|date-time||submitted_date_time|submittedDateTime|
|**--unsubmitted-date-time**|date-time||unsubmitted_date_time|unsubmittedDateTime|
|**--released-date-time**|date-time||released_date_time|releasedDateTime|
|**--returned-date-time**|date-time||returned_date_time|returnedDateTime|
|**--resources-folder-url**|string||resources_folder_url|resourcesFolderUrl|
|**--resources**|array||resources|resources|
|**--submitted-resources**|array||submitted_resources|submittedResources|
|**--outcomes**|array||outcomes|outcomes|
|**--returned-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--returned-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--returned-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--returned-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--returned-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--returned-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--released-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--released-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--released-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--released-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--released-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--released-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--unsubmitted-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--unsubmitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--unsubmitted-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--unsubmitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--unsubmitted-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--unsubmitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--submitted-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--submitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--submitted-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--submitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--submitted-by-application-id**|string|Unique identifier for the identity.|id11|id|
|**--submitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|
|**--description**|object|educationItemBody|description|description|
|**--qualities**|array||qualities|qualities|
|**--levels**|array||levels|levels|
|**--grading**|any|Any object|grading|grading|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-class-assignment-submission create-outcome

create-outcome a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-outcome|CreateOutcomes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|

### education education-class-assignment-submission create-resource

create-resource a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-resource|CreateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-class-assignment-submission create-submitted-resource

create-submitted-resource a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-submitted-resource|CreateSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-class-assignment-submission get-outcome

get-outcome a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-outcome|GetOutcomes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: educationOutcome-id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class-assignment-submission get-resource

get-resource a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource|GetResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: educationSubmissionResource-id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class-assignment-submission get-submitted-resource

get-submitted-resource a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-submitted-resource|GetSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: educationSubmissionResource-id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class-assignment-submission list-outcome

list-outcome a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-outcome|ListOutcomes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class-assignment-submission list-resource

list-resource a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-resource|ListResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class-assignment-submission list-submitted-resource

list-submitted-resource a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-submitted-resource|ListSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class-assignment-submission return

return a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|return|return|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|

### education education-class-assignment-submission submit

submit a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|submit|submit|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|

### education education-class-assignment-submission unsubmit

unsubmit a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|unsubmit|unsubmit|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|

### education education-class-assignment-submission update

update a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateOutcomes|
|update|UpdateResources|
|update|UpdateSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: educationOutcome-id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--education-submission-resource-id**|string|key: educationSubmissionResource-id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-class-member delta

delta a education education-class-member.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-member|education.classes.members|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|

### education education-class-school delta

delta a education education-class-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-school|education.classes.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|

### education education-class-teacher delta

delta a education education-class-teacher.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-teacher|education.classes.teachers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|

### education education-me create-assignment

create-assignment a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-assignment|CreateAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--class-id**|string||class_id|classId|
|**--display-name**|string||display_name|displayName|
|**--instructions**|object|educationItemBody|instructions|instructions|
|**--close-date-time**|date-time||close_date_time|closeDateTime|
|**--due-date-time**|date-time||due_date_time|dueDateTime|
|**--assign-date-time**|date-time||assign_date_time|assignDateTime|
|**--assigned-date-time**|date-time||assigned_date_time|assignedDateTime|
|**--grading**|any|Any object|grading|grading|
|**--assign-to**|any|Any object|assign_to|assignTo|
|**--allow-late-submissions**|boolean||allow_late_submissions|allowLateSubmissions|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--allow-students-to-add-resources-to-submission**|boolean||allow_students_to_add_resources_to_submission|allowStudentsToAddResourcesToSubmission|
|**--status**|choice|educationAssignmentStatus|status|status|
|**--resources**|array||resources|resources|
|**--submissions**|array||submissions|submissions|
|**--categories**|array||categories|categories|
|**--rubric-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--rubric-display-name**|string||microsoft_graph_education_rubric_display_name|displayName|
|**--rubric-description**|object|educationItemBody|description|description|
|**--rubric-qualities**|array||qualities|qualities|
|**--rubric-levels**|array||levels|levels|
|**--rubric-grading**|any|Any object|any_grading|grading|
|**--rubric-created-date-time**|date-time||microsoft_graph_education_rubric_created_date_time_created_date_time|createdDateTime|
|**--rubric-last-modified-date-time**|date-time||microsoft_graph_education_rubric_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--rubric-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--rubric-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--rubric-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--rubric-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--rubric-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--rubric-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--rubric-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--rubric-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--rubric-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--rubric-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--rubric-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--rubric-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id11|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name11|displayName|

### education education-me create-rubric

create-rubric a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-rubric|CreateRubrics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--description**|object|educationItemBody|description|description|
|**--qualities**|array||qualities|qualities|
|**--levels**|array||levels|levels|
|**--grading**|any|Any object|grading|grading|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-me get-assignment

get-assignment a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assignment|GetAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me get-class

get-class a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-class|GetClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me get-rubric

get-rubric a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-rubric|GetRubrics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-rubric-id**|string|key: educationRubric-id of educationRubric|education_rubric_id|educationRubric-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me get-school

get-school a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-school|GetSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: educationSchool-id of educationSchool|education_school_id|educationSchool-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me get-taught-class

get-taught-class a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-taught-class|GetTaughtClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me get-user

get-user a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user|GetUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me list-assignment

list-assignment a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-assignment|ListAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me list-class

list-class a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-class|ListClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me list-rubric

list-rubric a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-rubric|ListRubrics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me list-school

list-school a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-school|ListSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me list-taught-class

list-taught-class a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-taught-class|ListTaughtClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me update

update a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateAssignments|
|update|UpdateRubrics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-rubric-id**|string|key: educationRubric-id of educationRubric|education_rubric_id|educationRubric-id|
|**--id**|string|Read-only.|id|id|
|**--class-id**|string||class_id|classId|
|**--display-name**|string||display_name|displayName|
|**--instructions**|object|educationItemBody|instructions|instructions|
|**--close-date-time**|date-time||close_date_time|closeDateTime|
|**--due-date-time**|date-time||due_date_time|dueDateTime|
|**--assign-date-time**|date-time||assign_date_time|assignDateTime|
|**--assigned-date-time**|date-time||assigned_date_time|assignedDateTime|
|**--grading**|any|Any object|grading|grading|
|**--assign-to**|any|Any object|assign_to|assignTo|
|**--allow-late-submissions**|boolean||allow_late_submissions|allowLateSubmissions|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--allow-students-to-add-resources-to-submission**|boolean||allow_students_to_add_resources_to_submission|allowStudentsToAddResourcesToSubmission|
|**--status**|choice|educationAssignmentStatus|status|status|
|**--resources**|array||resources|resources|
|**--submissions**|array||submissions|submissions|
|**--categories**|array||categories|categories|
|**--rubric-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--rubric-display-name**|string||microsoft_graph_education_rubric_display_name|displayName|
|**--rubric-description**|object|educationItemBody|description|description|
|**--rubric-qualities**|array||qualities|qualities|
|**--rubric-levels**|array||levels|levels|
|**--rubric-grading**|any|Any object|any_grading|grading|
|**--rubric-created-date-time**|date-time||microsoft_graph_education_rubric_created_date_time_created_date_time|createdDateTime|
|**--rubric-last-modified-date-time**|date-time||microsoft_graph_education_rubric_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--rubric-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--rubric-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--rubric-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--rubric-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--rubric-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--rubric-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--rubric-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--rubric-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--rubric-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--rubric-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--rubric-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--rubric-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id11|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name11|displayName|
|**--description**|object|educationItemBody|description|description|
|**--qualities**|array||qualities|qualities|
|**--levels**|array||levels|levels|

### education education-me-assignment create-category

create-category a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-category|CreateCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### education education-me-assignment create-resource

create-resource a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-resource|CreateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-me-assignment create-submission

create-submission a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-submission|CreateSubmissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--recipient**|any|Any object|recipient|recipient|
|**--status**|choice|educationSubmissionStatus|status|status|
|**--submitted-date-time**|date-time||submitted_date_time|submittedDateTime|
|**--unsubmitted-date-time**|date-time||unsubmitted_date_time|unsubmittedDateTime|
|**--released-date-time**|date-time||released_date_time|releasedDateTime|
|**--returned-date-time**|date-time||returned_date_time|returnedDateTime|
|**--resources-folder-url**|string||resources_folder_url|resourcesFolderUrl|
|**--resources**|array||resources|resources|
|**--submitted-resources**|array||submitted_resources|submittedResources|
|**--outcomes**|array||outcomes|outcomes|
|**--returned-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--returned-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--returned-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--returned-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--returned-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--returned-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--released-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--released-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--released-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--released-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--released-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--released-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--unsubmitted-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--unsubmitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--unsubmitted-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--unsubmitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--unsubmitted-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--unsubmitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--submitted-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--submitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--submitted-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--submitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--submitted-by-application-id**|string|Unique identifier for the identity.|id11|id|
|**--submitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|

### education education-me-assignment get-category

get-category a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-category|GetCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: educationCategory-id of educationCategory|education_category_id|educationCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me-assignment get-resource

get-resource a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource|GetResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: educationAssignmentResource-id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me-assignment get-resource-folder-url

get-resource-folder-url a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource-folder-url|getResourcesFolderUrl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|

### education education-me-assignment get-rubric

get-rubric a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-rubric|GetRubric|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me-assignment get-submission

get-submission a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-submission|GetSubmissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me-assignment list-category

list-category a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-category|ListCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me-assignment list-resource

list-resource a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-resource|ListResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me-assignment list-submission

list-submission a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-submission|ListSubmissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me-assignment publish

publish a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|publish|publish|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|

### education education-me-assignment update

update a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateCategories|
|update|UpdateResources|
|update|UpdateSubmissions|
|update|UpdateRubric|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: educationCategory-id of educationCategory|education_category_id|educationCategory-id|
|**--education-assignment-resource-id**|string|key: educationAssignmentResource-id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--recipient**|any|Any object|recipient|recipient|
|**--status**|choice|educationSubmissionStatus|status|status|
|**--submitted-date-time**|date-time||submitted_date_time|submittedDateTime|
|**--unsubmitted-date-time**|date-time||unsubmitted_date_time|unsubmittedDateTime|
|**--released-date-time**|date-time||released_date_time|releasedDateTime|
|**--returned-date-time**|date-time||returned_date_time|returnedDateTime|
|**--resources-folder-url**|string||resources_folder_url|resourcesFolderUrl|
|**--resources**|array||resources|resources|
|**--submitted-resources**|array||submitted_resources|submittedResources|
|**--outcomes**|array||outcomes|outcomes|
|**--returned-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--returned-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--returned-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--returned-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--returned-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--returned-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--released-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--released-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--released-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--released-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--released-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--released-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--unsubmitted-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--unsubmitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--unsubmitted-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--unsubmitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--unsubmitted-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--unsubmitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--submitted-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--submitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--submitted-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--submitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--submitted-by-application-id**|string|Unique identifier for the identity.|id11|id|
|**--submitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|
|**--description**|object|educationItemBody|description|description|
|**--qualities**|array||qualities|qualities|
|**--levels**|array||levels|levels|
|**--grading**|any|Any object|grading|grading|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-me-assignment-submission create-outcome

create-outcome a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-outcome|CreateOutcomes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|

### education education-me-assignment-submission create-resource

create-resource a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-resource|CreateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-me-assignment-submission create-submitted-resource

create-submitted-resource a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-submitted-resource|CreateSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-me-assignment-submission get-outcome

get-outcome a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-outcome|GetOutcomes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: educationOutcome-id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me-assignment-submission get-resource

get-resource a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource|GetResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: educationSubmissionResource-id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me-assignment-submission get-submitted-resource

get-submitted-resource a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-submitted-resource|GetSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: educationSubmissionResource-id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me-assignment-submission list-outcome

list-outcome a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-outcome|ListOutcomes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me-assignment-submission list-resource

list-resource a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-resource|ListResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me-assignment-submission list-submitted-resource

list-submitted-resource a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-submitted-resource|ListSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-me-assignment-submission return

return a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|return|return|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|

### education education-me-assignment-submission submit

submit a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|submit|submit|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|

### education education-me-assignment-submission unsubmit

unsubmit a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|unsubmit|unsubmit|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|

### education education-me-assignment-submission update

update a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateOutcomes|
|update|UpdateResources|
|update|UpdateSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: educationOutcome-id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--education-submission-resource-id**|string|key: educationSubmissionResource-id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-me-class delta

delta a education education-me-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-class|education.me.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### education education-me-school delta

delta a education education-me-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-school|education.me.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### education education-me-taught-class delta

delta a education education-me-taught-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-taught-class|education.me.taughtClasses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### education education-root get-education-root

get-education-root a education education-root.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-root|education.educationRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-education-root|GetEducationRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-root update

update a education education-root.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-root|education.educationRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateEducationRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--synchronization-profiles**|array||synchronization_profiles|synchronizationProfiles|
|**--classes**|array|Read-only. Nullable.|classes|classes|
|**--schools**|array|Read-only. Nullable.|schools|schools|
|**--users**|array|Read-only. Nullable.|users|users|
|**--me**|object|educationUser|me|me|

### education education-school delta

delta a education education-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-school|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### education education-school get-administrative-unit

get-administrative-unit a education education-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-school|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-administrative-unit|GetAdministrativeUnit|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: educationSchool-id of educationSchool|education_school_id|educationSchool-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-school get-class

get-class a education education-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-school|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-class|GetClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: educationSchool-id of educationSchool|education_school_id|educationSchool-id|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-school get-user

get-user a education education-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-school|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user|GetUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: educationSchool-id of educationSchool|education_school_id|educationSchool-id|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-school list-class

list-class a education education-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-school|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-class|ListClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: educationSchool-id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-school list-user

list-user a education education-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-school|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-user|ListUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: educationSchool-id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-school-class delta

delta a education education-school-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-school-class|education.schools.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: educationSchool-id of educationSchool|education_school_id|educationSchool-id|

### education education-school-user delta

delta a education education-school-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-school-user|education.schools.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: educationSchool-id of educationSchool|education_school_id|educationSchool-id|

### education education-synchronization-profile create-error

create-error a education education-synchronization-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-synchronization-profile|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-error|CreateErrors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: educationSynchronizationProfile-id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--id**|string|Read-only.|id|id|
|**--entry-type**|string||entry_type|entryType|
|**--error-code**|string||error_code|errorCode|
|**--error-message**|string||error_message|errorMessage|
|**--joining-value**|string||joining_value|joiningValue|
|**--recorded-date-time**|date-time||recorded_date_time|recordedDateTime|
|**--reportable-identifier**|string||reportable_identifier|reportableIdentifier|

### education education-synchronization-profile get-error

get-error a education education-synchronization-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-synchronization-profile|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-error|GetErrors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: educationSynchronizationProfile-id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--education-synchronization-error-id**|string|key: educationSynchronizationError-id of educationSynchronizationError|education_synchronization_error_id|educationSynchronizationError-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-synchronization-profile get-profile-status

get-profile-status a education education-synchronization-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-synchronization-profile|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-profile-status|GetProfileStatus|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: educationSynchronizationProfile-id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-synchronization-profile list-error

list-error a education education-synchronization-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-synchronization-profile|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-error|ListErrors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: educationSynchronizationProfile-id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-synchronization-profile pause

pause a education education-synchronization-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-synchronization-profile|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|pause|pause|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: educationSynchronizationProfile-id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

### education education-synchronization-profile reset

reset a education education-synchronization-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-synchronization-profile|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reset|reset|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: educationSynchronizationProfile-id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

### education education-synchronization-profile resume

resume a education education-synchronization-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-synchronization-profile|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|resume|resume|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: educationSynchronizationProfile-id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

### education education-synchronization-profile start

start a education education-synchronization-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-synchronization-profile|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|start|start|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: educationSynchronizationProfile-id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

### education education-synchronization-profile update

update a education education-synchronization-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-synchronization-profile|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateErrors|
|update|UpdateProfileStatus|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: educationSynchronizationProfile-id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--education-synchronization-error-id**|string|key: educationSynchronizationError-id of educationSynchronizationError|education_synchronization_error_id|educationSynchronizationError-id|
|**--id**|string|Read-only.|id|id|
|**--entry-type**|string||entry_type|entryType|
|**--error-code**|string||error_code|errorCode|
|**--error-message**|string||error_message|errorMessage|
|**--joining-value**|string||joining_value|joiningValue|
|**--recorded-date-time**|date-time||recorded_date_time|recordedDateTime|
|**--reportable-identifier**|string||reportable_identifier|reportableIdentifier|
|**--status**|choice|educationSynchronizationStatus|status|status|
|**--last-synchronization-date-time**|date-time||last_synchronization_date_time|lastSynchronizationDateTime|

### education education-synchronization-profile upload-url

upload-url a education education-synchronization-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-synchronization-profile|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|upload-url|uploadUrl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: educationSynchronizationProfile-id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

### education education-user create-assignment

create-assignment a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-assignment|CreateAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--id**|string|Read-only.|id|id|
|**--class-id**|string||class_id|classId|
|**--display-name**|string||display_name|displayName|
|**--instructions**|object|educationItemBody|instructions|instructions|
|**--close-date-time**|date-time||close_date_time|closeDateTime|
|**--due-date-time**|date-time||due_date_time|dueDateTime|
|**--assign-date-time**|date-time||assign_date_time|assignDateTime|
|**--assigned-date-time**|date-time||assigned_date_time|assignedDateTime|
|**--grading**|any|Any object|grading|grading|
|**--assign-to**|any|Any object|assign_to|assignTo|
|**--allow-late-submissions**|boolean||allow_late_submissions|allowLateSubmissions|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--allow-students-to-add-resources-to-submission**|boolean||allow_students_to_add_resources_to_submission|allowStudentsToAddResourcesToSubmission|
|**--status**|choice|educationAssignmentStatus|status|status|
|**--resources**|array||resources|resources|
|**--submissions**|array||submissions|submissions|
|**--categories**|array||categories|categories|
|**--rubric-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--rubric-display-name**|string||microsoft_graph_education_rubric_display_name|displayName|
|**--rubric-description**|object|educationItemBody|description|description|
|**--rubric-qualities**|array||qualities|qualities|
|**--rubric-levels**|array||levels|levels|
|**--rubric-grading**|any|Any object|any_grading|grading|
|**--rubric-created-date-time**|date-time||microsoft_graph_education_rubric_created_date_time_created_date_time|createdDateTime|
|**--rubric-last-modified-date-time**|date-time||microsoft_graph_education_rubric_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--rubric-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--rubric-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--rubric-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--rubric-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--rubric-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--rubric-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--rubric-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--rubric-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--rubric-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--rubric-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--rubric-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--rubric-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id11|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name11|displayName|

### education education-user create-rubric

create-rubric a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-rubric|CreateRubrics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--description**|object|educationItemBody|description|description|
|**--qualities**|array||qualities|qualities|
|**--levels**|array||levels|levels|
|**--grading**|any|Any object|grading|grading|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-user delta

delta a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### education education-user get-assignment

get-assignment a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-assignment|GetAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user get-class

get-class a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-class|GetClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user get-rubric

get-rubric a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-rubric|GetRubrics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-rubric-id**|string|key: educationRubric-id of educationRubric|education_rubric_id|educationRubric-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user get-school

get-school a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-school|GetSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-school-id**|string|key: educationSchool-id of educationSchool|education_school_id|educationSchool-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user get-taught-class

get-taught-class a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-taught-class|GetTaughtClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-class-id**|string|key: educationClass-id of educationClass|education_class_id|educationClass-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user get-user

get-user a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user|GetUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user list-assignment

list-assignment a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-assignment|ListAssignments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user list-class

list-class a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-class|ListClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user list-rubric

list-rubric a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-rubric|ListRubrics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user list-school

list-school a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-school|ListSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user list-taught-class

list-taught-class a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-taught-class|ListTaughtClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user update

update a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateAssignments|
|update|UpdateRubrics|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-rubric-id**|string|key: educationRubric-id of educationRubric|education_rubric_id|educationRubric-id|
|**--id**|string|Read-only.|id|id|
|**--class-id**|string||class_id|classId|
|**--display-name**|string||display_name|displayName|
|**--instructions**|object|educationItemBody|instructions|instructions|
|**--close-date-time**|date-time||close_date_time|closeDateTime|
|**--due-date-time**|date-time||due_date_time|dueDateTime|
|**--assign-date-time**|date-time||assign_date_time|assignDateTime|
|**--assigned-date-time**|date-time||assigned_date_time|assignedDateTime|
|**--grading**|any|Any object|grading|grading|
|**--assign-to**|any|Any object|assign_to|assignTo|
|**--allow-late-submissions**|boolean||allow_late_submissions|allowLateSubmissions|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--allow-students-to-add-resources-to-submission**|boolean||allow_students_to_add_resources_to_submission|allowStudentsToAddResourcesToSubmission|
|**--status**|choice|educationAssignmentStatus|status|status|
|**--resources**|array||resources|resources|
|**--submissions**|array||submissions|submissions|
|**--categories**|array||categories|categories|
|**--rubric-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--rubric-display-name**|string||microsoft_graph_education_rubric_display_name|displayName|
|**--rubric-description**|object|educationItemBody|description|description|
|**--rubric-qualities**|array||qualities|qualities|
|**--rubric-levels**|array||levels|levels|
|**--rubric-grading**|any|Any object|any_grading|grading|
|**--rubric-created-date-time**|date-time||microsoft_graph_education_rubric_created_date_time_created_date_time|createdDateTime|
|**--rubric-last-modified-date-time**|date-time||microsoft_graph_education_rubric_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--rubric-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--rubric-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--rubric-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--rubric-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--rubric-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--rubric-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--rubric-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--rubric-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--rubric-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--rubric-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--rubric-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--rubric-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id11|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name11|displayName|
|**--description**|object|educationItemBody|description|description|
|**--qualities**|array||qualities|qualities|
|**--levels**|array||levels|levels|

### education education-user-assignment create-category

create-category a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-category|CreateCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### education education-user-assignment create-resource

create-resource a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-resource|CreateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-user-assignment create-submission

create-submission a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-submission|CreateSubmissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--recipient**|any|Any object|recipient|recipient|
|**--status**|choice|educationSubmissionStatus|status|status|
|**--submitted-date-time**|date-time||submitted_date_time|submittedDateTime|
|**--unsubmitted-date-time**|date-time||unsubmitted_date_time|unsubmittedDateTime|
|**--released-date-time**|date-time||released_date_time|releasedDateTime|
|**--returned-date-time**|date-time||returned_date_time|returnedDateTime|
|**--resources-folder-url**|string||resources_folder_url|resourcesFolderUrl|
|**--resources**|array||resources|resources|
|**--submitted-resources**|array||submitted_resources|submittedResources|
|**--outcomes**|array||outcomes|outcomes|
|**--returned-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--returned-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--returned-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--returned-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--returned-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--returned-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--released-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--released-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--released-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--released-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--released-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--released-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--unsubmitted-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--unsubmitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--unsubmitted-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--unsubmitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--unsubmitted-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--unsubmitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--submitted-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--submitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--submitted-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--submitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--submitted-by-application-id**|string|Unique identifier for the identity.|id11|id|
|**--submitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|

### education education-user-assignment get-category

get-category a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-category|GetCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: educationCategory-id of educationCategory|education_category_id|educationCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user-assignment get-resource

get-resource a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource|GetResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: educationAssignmentResource-id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user-assignment get-resource-folder-url

get-resource-folder-url a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource-folder-url|getResourcesFolderUrl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|

### education education-user-assignment get-rubric

get-rubric a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-rubric|GetRubric|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user-assignment get-submission

get-submission a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-submission|GetSubmissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user-assignment list-category

list-category a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-category|ListCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user-assignment list-resource

list-resource a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-resource|ListResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user-assignment list-submission

list-submission a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-submission|ListSubmissions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user-assignment publish

publish a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|publish|publish|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|

### education education-user-assignment update

update a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateCategories|
|update|UpdateResources|
|update|UpdateSubmissions|
|update|UpdateRubric|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: educationCategory-id of educationCategory|education_category_id|educationCategory-id|
|**--education-assignment-resource-id**|string|key: educationAssignmentResource-id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--recipient**|any|Any object|recipient|recipient|
|**--status**|choice|educationSubmissionStatus|status|status|
|**--submitted-date-time**|date-time||submitted_date_time|submittedDateTime|
|**--unsubmitted-date-time**|date-time||unsubmitted_date_time|unsubmittedDateTime|
|**--released-date-time**|date-time||released_date_time|releasedDateTime|
|**--returned-date-time**|date-time||returned_date_time|returnedDateTime|
|**--resources-folder-url**|string||resources_folder_url|resourcesFolderUrl|
|**--resources**|array||resources|resources|
|**--submitted-resources**|array||submitted_resources|submittedResources|
|**--outcomes**|array||outcomes|outcomes|
|**--returned-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--returned-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--returned-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--returned-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--returned-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--returned-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--released-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--released-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--released-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--released-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--released-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--released-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--unsubmitted-by-user-id**|string|Unique identifier for the identity.|id6|id|
|**--unsubmitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--unsubmitted-by-device-id**|string|Unique identifier for the identity.|id7|id|
|**--unsubmitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--unsubmitted-by-application-id**|string|Unique identifier for the identity.|id8|id|
|**--unsubmitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--submitted-by-user-id**|string|Unique identifier for the identity.|id9|id|
|**--submitted-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--submitted-by-device-id**|string|Unique identifier for the identity.|id10|id|
|**--submitted-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--submitted-by-application-id**|string|Unique identifier for the identity.|id11|id|
|**--submitted-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|
|**--description**|object|educationItemBody|description|description|
|**--qualities**|array||qualities|qualities|
|**--levels**|array||levels|levels|
|**--grading**|any|Any object|grading|grading|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-user-assignment-submission create-outcome

create-outcome a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-outcome|CreateOutcomes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|

### education education-user-assignment-submission create-resource

create-resource a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-resource|CreateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-user-assignment-submission create-submitted-resource

create-submitted-resource a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-submitted-resource|CreateSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-user-assignment-submission get-outcome

get-outcome a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-outcome|GetOutcomes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: educationOutcome-id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user-assignment-submission get-resource

get-resource a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-resource|GetResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: educationSubmissionResource-id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user-assignment-submission get-submitted-resource

get-submitted-resource a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-submitted-resource|GetSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: educationSubmissionResource-id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user-assignment-submission list-outcome

list-outcome a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-outcome|ListOutcomes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user-assignment-submission list-resource

list-resource a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-resource|ListResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user-assignment-submission list-submitted-resource

list-submitted-resource a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-submitted-resource|ListSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user-assignment-submission return

return a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|return|return|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|

### education education-user-assignment-submission submit

submit a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|submit|submit|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|

### education education-user-assignment-submission unsubmit

unsubmit a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|unsubmit|unsubmit|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|

### education education-user-assignment-submission update

update a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateOutcomes|
|update|UpdateResources|
|update|UpdateSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: educationAssignment-id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: educationSubmission-id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: educationOutcome-id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--education-submission-resource-id**|string|key: educationSubmissionResource-id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--resource-last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--resource-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--resource-last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--resource-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--resource-last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--resource-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--resource-created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--resource-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--resource-created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--resource-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--resource-created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--resource-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|

### education education-user-class delta

delta a education education-user-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-class|education.users.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|

### education education-user-school delta

delta a education education-user-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-school|education.users.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|

### education education-user-taught-class delta

delta a education education-user-taught-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-taught-class|education.users.taughtClasses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: educationUser-id of educationUser|education_user_id|educationUser-id|
