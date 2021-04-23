# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az education_beta|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az education_beta` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az education education-root|education.educationRoot|[commands](#CommandsIneducation.educationRoot)|
|az education education|education|[commands](#CommandsIneducation)|
|az education education-class|education.classes|[commands](#CommandsIneducation.classes)|
|az education education-class-assignment|education.classes.assignments|[commands](#CommandsIneducation.classes.assignments)|
|az education education-class-assignment-submission|education.classes.assignments.submissions|[commands](#CommandsIneducation.classes.assignments.submissions)|
|az education education-class-member|education.classes.members|[commands](#CommandsIneducation.classes.members)|
|az education education-class-school|education.classes.schools|[commands](#CommandsIneducation.classes.schools)|
|az education education-class-teacher|education.classes.teachers|[commands](#CommandsIneducation.classes.teachers)|
|az education education-me|education.me|[commands](#CommandsIneducation.me)|
|az education education-me-assignment|education.me.assignments|[commands](#CommandsIneducation.me.assignments)|
|az education education-me-assignment-submission|education.me.assignments.submissions|[commands](#CommandsIneducation.me.assignments.submissions)|
|az education education-me-class|education.me.classes|[commands](#CommandsIneducation.me.classes)|
|az education education-me-school|education.me.schools|[commands](#CommandsIneducation.me.schools)|
|az education education-me-taught-class|education.me.taughtClasses|[commands](#CommandsIneducation.me.taughtClasses)|
|az education education-school|education.schools|[commands](#CommandsIneducation.schools)|
|az education education-school-class|education.schools.classes|[commands](#CommandsIneducation.schools.classes)|
|az education education-school-user|education.schools.users|[commands](#CommandsIneducation.schools.users)|
|az education education-synchronization-profile|education.synchronizationProfiles|[commands](#CommandsIneducation.synchronizationProfiles)|
|az education education-user|education.users|[commands](#CommandsIneducation.users)|
|az education education-user-assignment|education.users.assignments|[commands](#CommandsIneducation.users.assignments)|
|az education education-user-assignment-submission|education.users.assignments.submissions|[commands](#CommandsIneducation.users.assignments.submissions)|
|az education education-user-class|education.users.classes|[commands](#CommandsIneducation.users.classes)|
|az education education-user-school|education.users.schools|[commands](#CommandsIneducation.users.schools)|
|az education education-user-taught-class|education.users.taughtClasses|[commands](#CommandsIneducation.users.taughtClasses)|

## COMMANDS
### <a name="CommandsIneducation">Commands in `az education education` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education create-class](#educationCreateClasses)|CreateClasses|[Parameters](#ParameterseducationCreateClasses)|Not Found|
|[az education education create-school](#educationCreateSchools)|CreateSchools|[Parameters](#ParameterseducationCreateSchools)|Not Found|
|[az education education create-synchronization-profile](#educationCreateSynchronizationProfiles)|CreateSynchronizationProfiles|[Parameters](#ParameterseducationCreateSynchronizationProfiles)|Not Found|
|[az education education create-user](#educationCreateUsers)|CreateUsers|[Parameters](#ParameterseducationCreateUsers)|Not Found|
|[az education education delete-class](#educationDeleteClasses)|DeleteClasses|[Parameters](#ParameterseducationDeleteClasses)|Not Found|
|[az education education delete-me](#educationDeleteMe)|DeleteMe|[Parameters](#ParameterseducationDeleteMe)|Not Found|
|[az education education delete-school](#educationDeleteSchools)|DeleteSchools|[Parameters](#ParameterseducationDeleteSchools)|Not Found|
|[az education education delete-synchronization-profile](#educationDeleteSynchronizationProfiles)|DeleteSynchronizationProfiles|[Parameters](#ParameterseducationDeleteSynchronizationProfiles)|Not Found|
|[az education education delete-user](#educationDeleteUsers)|DeleteUsers|[Parameters](#ParameterseducationDeleteUsers)|Not Found|
|[az education education list-class](#educationListClasses)|ListClasses|[Parameters](#ParameterseducationListClasses)|Not Found|
|[az education education list-school](#educationListSchools)|ListSchools|[Parameters](#ParameterseducationListSchools)|Not Found|
|[az education education list-synchronization-profile](#educationListSynchronizationProfiles)|ListSynchronizationProfiles|[Parameters](#ParameterseducationListSynchronizationProfiles)|Not Found|
|[az education education list-user](#educationListUsers)|ListUsers|[Parameters](#ParameterseducationListUsers)|Not Found|
|[az education education show-class](#educationGetClasses)|GetClasses|[Parameters](#ParameterseducationGetClasses)|Not Found|
|[az education education show-me](#educationGetMe)|GetMe|[Parameters](#ParameterseducationGetMe)|Not Found|
|[az education education show-school](#educationGetSchools)|GetSchools|[Parameters](#ParameterseducationGetSchools)|Not Found|
|[az education education show-synchronization-profile](#educationGetSynchronizationProfiles)|GetSynchronizationProfiles|[Parameters](#ParameterseducationGetSynchronizationProfiles)|Not Found|
|[az education education show-user](#educationGetUsers)|GetUsers|[Parameters](#ParameterseducationGetUsers)|Not Found|
|[az education education update-class](#educationUpdateClasses)|UpdateClasses|[Parameters](#ParameterseducationUpdateClasses)|Not Found|
|[az education education update-me](#educationUpdateMe)|UpdateMe|[Parameters](#ParameterseducationUpdateMe)|Not Found|
|[az education education update-school](#educationUpdateSchools)|UpdateSchools|[Parameters](#ParameterseducationUpdateSchools)|Not Found|
|[az education education update-synchronization-profile](#educationUpdateSynchronizationProfiles)|UpdateSynchronizationProfiles|[Parameters](#ParameterseducationUpdateSynchronizationProfiles)|Not Found|
|[az education education update-user](#educationUpdateUsers)|UpdateUsers|[Parameters](#ParameterseducationUpdateUsers)|Not Found|

### <a name="CommandsIneducation.classes">Commands in `az education education-class` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-class create-assignment](#education.classesCreateAssignments)|CreateAssignments|[Parameters](#Parameterseducation.classesCreateAssignments)|Not Found|
|[az education education-class create-assignment-category](#education.classesCreateAssignmentCategories)|CreateAssignmentCategories|[Parameters](#Parameterseducation.classesCreateAssignmentCategories)|Not Found|
|[az education education-class create-ref-member](#education.classesCreateRefMembers)|CreateRefMembers|[Parameters](#Parameterseducation.classesCreateRefMembers)|Not Found|
|[az education education-class create-ref-school](#education.classesCreateRefSchools)|CreateRefSchools|[Parameters](#Parameterseducation.classesCreateRefSchools)|Not Found|
|[az education education-class create-ref-teacher](#education.classesCreateRefTeachers)|CreateRefTeachers|[Parameters](#Parameterseducation.classesCreateRefTeachers)|Not Found|
|[az education education-class delete-assignment](#education.classesDeleteAssignments)|DeleteAssignments|[Parameters](#Parameterseducation.classesDeleteAssignments)|Not Found|
|[az education education-class delete-assignment-category](#education.classesDeleteAssignmentCategories)|DeleteAssignmentCategories|[Parameters](#Parameterseducation.classesDeleteAssignmentCategories)|Not Found|
|[az education education-class delete-ref-group](#education.classesDeleteRefGroup)|DeleteRefGroup|[Parameters](#Parameterseducation.classesDeleteRefGroup)|Not Found|
|[az education education-class delta](#education.classesdelta)|delta|[Parameters](#Parameterseducation.classesdelta)|Not Found|
|[az education education-class list-assignment](#education.classesListAssignments)|ListAssignments|[Parameters](#Parameterseducation.classesListAssignments)|Not Found|
|[az education education-class list-assignment-category](#education.classesListAssignmentCategories)|ListAssignmentCategories|[Parameters](#Parameterseducation.classesListAssignmentCategories)|Not Found|
|[az education education-class list-member](#education.classesListMembers)|ListMembers|[Parameters](#Parameterseducation.classesListMembers)|Not Found|
|[az education education-class list-ref-member](#education.classesListRefMembers)|ListRefMembers|[Parameters](#Parameterseducation.classesListRefMembers)|Not Found|
|[az education education-class list-ref-school](#education.classesListRefSchools)|ListRefSchools|[Parameters](#Parameterseducation.classesListRefSchools)|Not Found|
|[az education education-class list-ref-teacher](#education.classesListRefTeachers)|ListRefTeachers|[Parameters](#Parameterseducation.classesListRefTeachers)|Not Found|
|[az education education-class list-school](#education.classesListSchools)|ListSchools|[Parameters](#Parameterseducation.classesListSchools)|Not Found|
|[az education education-class list-teacher](#education.classesListTeachers)|ListTeachers|[Parameters](#Parameterseducation.classesListTeachers)|Not Found|
|[az education education-class set-ref-group](#education.classesSetRefGroup)|SetRefGroup|[Parameters](#Parameterseducation.classesSetRefGroup)|Not Found|
|[az education education-class show-assignment](#education.classesGetAssignments)|GetAssignments|[Parameters](#Parameterseducation.classesGetAssignments)|Not Found|
|[az education education-class show-assignment-category](#education.classesGetAssignmentCategories)|GetAssignmentCategories|[Parameters](#Parameterseducation.classesGetAssignmentCategories)|Not Found|
|[az education education-class show-group](#education.classesGetGroup)|GetGroup|[Parameters](#Parameterseducation.classesGetGroup)|Not Found|
|[az education education-class show-ref-group](#education.classesGetRefGroup)|GetRefGroup|[Parameters](#Parameterseducation.classesGetRefGroup)|Not Found|
|[az education education-class update-assignment](#education.classesUpdateAssignments)|UpdateAssignments|[Parameters](#Parameterseducation.classesUpdateAssignments)|Not Found|
|[az education education-class update-assignment-category](#education.classesUpdateAssignmentCategories)|UpdateAssignmentCategories|[Parameters](#Parameterseducation.classesUpdateAssignmentCategories)|Not Found|

### <a name="CommandsIneducation.classes.assignments">Commands in `az education education-class-assignment` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-class-assignment create-category](#education.classes.assignmentsCreateCategories)|CreateCategories|[Parameters](#Parameterseducation.classes.assignmentsCreateCategories)|Not Found|
|[az education education-class-assignment create-resource](#education.classes.assignmentsCreateResources)|CreateResources|[Parameters](#Parameterseducation.classes.assignmentsCreateResources)|Not Found|
|[az education education-class-assignment create-submission](#education.classes.assignmentsCreateSubmissions)|CreateSubmissions|[Parameters](#Parameterseducation.classes.assignmentsCreateSubmissions)|Not Found|
|[az education education-class-assignment delete-category](#education.classes.assignmentsDeleteCategories)|DeleteCategories|[Parameters](#Parameterseducation.classes.assignmentsDeleteCategories)|Not Found|
|[az education education-class-assignment delete-resource](#education.classes.assignmentsDeleteResources)|DeleteResources|[Parameters](#Parameterseducation.classes.assignmentsDeleteResources)|Not Found|
|[az education education-class-assignment delete-rubric](#education.classes.assignmentsDeleteRubric)|DeleteRubric|[Parameters](#Parameterseducation.classes.assignmentsDeleteRubric)|Not Found|
|[az education education-class-assignment delete-submission](#education.classes.assignmentsDeleteSubmissions)|DeleteSubmissions|[Parameters](#Parameterseducation.classes.assignmentsDeleteSubmissions)|Not Found|
|[az education education-class-assignment list-category](#education.classes.assignmentsListCategories)|ListCategories|[Parameters](#Parameterseducation.classes.assignmentsListCategories)|Not Found|
|[az education education-class-assignment list-resource](#education.classes.assignmentsListResources)|ListResources|[Parameters](#Parameterseducation.classes.assignmentsListResources)|Not Found|
|[az education education-class-assignment list-submission](#education.classes.assignmentsListSubmissions)|ListSubmissions|[Parameters](#Parameterseducation.classes.assignmentsListSubmissions)|Not Found|
|[az education education-class-assignment publish](#education.classes.assignmentspublish)|publish|[Parameters](#Parameterseducation.classes.assignmentspublish)|Not Found|
|[az education education-class-assignment show-category](#education.classes.assignmentsGetCategories)|GetCategories|[Parameters](#Parameterseducation.classes.assignmentsGetCategories)|Not Found|
|[az education education-class-assignment show-resource](#education.classes.assignmentsGetResources)|GetResources|[Parameters](#Parameterseducation.classes.assignmentsGetResources)|Not Found|
|[az education education-class-assignment show-resource-folder-url](#education.classes.assignmentsgetResourcesFolderUrl)|getResourcesFolderUrl|[Parameters](#Parameterseducation.classes.assignmentsgetResourcesFolderUrl)|Not Found|
|[az education education-class-assignment show-rubric](#education.classes.assignmentsGetRubric)|GetRubric|[Parameters](#Parameterseducation.classes.assignmentsGetRubric)|Not Found|
|[az education education-class-assignment show-submission](#education.classes.assignmentsGetSubmissions)|GetSubmissions|[Parameters](#Parameterseducation.classes.assignmentsGetSubmissions)|Not Found|
|[az education education-class-assignment update-category](#education.classes.assignmentsUpdateCategories)|UpdateCategories|[Parameters](#Parameterseducation.classes.assignmentsUpdateCategories)|Not Found|
|[az education education-class-assignment update-resource](#education.classes.assignmentsUpdateResources)|UpdateResources|[Parameters](#Parameterseducation.classes.assignmentsUpdateResources)|Not Found|
|[az education education-class-assignment update-rubric](#education.classes.assignmentsUpdateRubric)|UpdateRubric|[Parameters](#Parameterseducation.classes.assignmentsUpdateRubric)|Not Found|
|[az education education-class-assignment update-submission](#education.classes.assignmentsUpdateSubmissions)|UpdateSubmissions|[Parameters](#Parameterseducation.classes.assignmentsUpdateSubmissions)|Not Found|

### <a name="CommandsIneducation.classes.assignments.submissions">Commands in `az education education-class-assignment-submission` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-class-assignment-submission create-outcome](#education.classes.assignments.submissionsCreateOutcomes)|CreateOutcomes|[Parameters](#Parameterseducation.classes.assignments.submissionsCreateOutcomes)|Not Found|
|[az education education-class-assignment-submission create-resource](#education.classes.assignments.submissionsCreateResources)|CreateResources|[Parameters](#Parameterseducation.classes.assignments.submissionsCreateResources)|Not Found|
|[az education education-class-assignment-submission create-submitted-resource](#education.classes.assignments.submissionsCreateSubmittedResources)|CreateSubmittedResources|[Parameters](#Parameterseducation.classes.assignments.submissionsCreateSubmittedResources)|Not Found|
|[az education education-class-assignment-submission delete-outcome](#education.classes.assignments.submissionsDeleteOutcomes)|DeleteOutcomes|[Parameters](#Parameterseducation.classes.assignments.submissionsDeleteOutcomes)|Not Found|
|[az education education-class-assignment-submission delete-resource](#education.classes.assignments.submissionsDeleteResources)|DeleteResources|[Parameters](#Parameterseducation.classes.assignments.submissionsDeleteResources)|Not Found|
|[az education education-class-assignment-submission delete-submitted-resource](#education.classes.assignments.submissionsDeleteSubmittedResources)|DeleteSubmittedResources|[Parameters](#Parameterseducation.classes.assignments.submissionsDeleteSubmittedResources)|Not Found|
|[az education education-class-assignment-submission list-outcome](#education.classes.assignments.submissionsListOutcomes)|ListOutcomes|[Parameters](#Parameterseducation.classes.assignments.submissionsListOutcomes)|Not Found|
|[az education education-class-assignment-submission list-resource](#education.classes.assignments.submissionsListResources)|ListResources|[Parameters](#Parameterseducation.classes.assignments.submissionsListResources)|Not Found|
|[az education education-class-assignment-submission list-submitted-resource](#education.classes.assignments.submissionsListSubmittedResources)|ListSubmittedResources|[Parameters](#Parameterseducation.classes.assignments.submissionsListSubmittedResources)|Not Found|
|[az education education-class-assignment-submission return](#education.classes.assignments.submissionsreturn)|return|[Parameters](#Parameterseducation.classes.assignments.submissionsreturn)|Not Found|
|[az education education-class-assignment-submission show-outcome](#education.classes.assignments.submissionsGetOutcomes)|GetOutcomes|[Parameters](#Parameterseducation.classes.assignments.submissionsGetOutcomes)|Not Found|
|[az education education-class-assignment-submission show-resource](#education.classes.assignments.submissionsGetResources)|GetResources|[Parameters](#Parameterseducation.classes.assignments.submissionsGetResources)|Not Found|
|[az education education-class-assignment-submission show-submitted-resource](#education.classes.assignments.submissionsGetSubmittedResources)|GetSubmittedResources|[Parameters](#Parameterseducation.classes.assignments.submissionsGetSubmittedResources)|Not Found|
|[az education education-class-assignment-submission submit](#education.classes.assignments.submissionssubmit)|submit|[Parameters](#Parameterseducation.classes.assignments.submissionssubmit)|Not Found|
|[az education education-class-assignment-submission unsubmit](#education.classes.assignments.submissionsunsubmit)|unsubmit|[Parameters](#Parameterseducation.classes.assignments.submissionsunsubmit)|Not Found|
|[az education education-class-assignment-submission update-outcome](#education.classes.assignments.submissionsUpdateOutcomes)|UpdateOutcomes|[Parameters](#Parameterseducation.classes.assignments.submissionsUpdateOutcomes)|Not Found|
|[az education education-class-assignment-submission update-resource](#education.classes.assignments.submissionsUpdateResources)|UpdateResources|[Parameters](#Parameterseducation.classes.assignments.submissionsUpdateResources)|Not Found|
|[az education education-class-assignment-submission update-submitted-resource](#education.classes.assignments.submissionsUpdateSubmittedResources)|UpdateSubmittedResources|[Parameters](#Parameterseducation.classes.assignments.submissionsUpdateSubmittedResources)|Not Found|

### <a name="CommandsIneducation.classes.members">Commands in `az education education-class-member` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-class-member delta](#education.classes.membersdelta)|delta|[Parameters](#Parameterseducation.classes.membersdelta)|Not Found|

### <a name="CommandsIneducation.classes.schools">Commands in `az education education-class-school` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-class-school delta](#education.classes.schoolsdelta)|delta|[Parameters](#Parameterseducation.classes.schoolsdelta)|Not Found|

### <a name="CommandsIneducation.classes.teachers">Commands in `az education education-class-teacher` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-class-teacher delta](#education.classes.teachersdelta)|delta|[Parameters](#Parameterseducation.classes.teachersdelta)|Not Found|

### <a name="CommandsIneducation.me">Commands in `az education education-me` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-me create-assignment](#education.meCreateAssignments)|CreateAssignments|[Parameters](#Parameterseducation.meCreateAssignments)|Not Found|
|[az education education-me create-ref-class](#education.meCreateRefClasses)|CreateRefClasses|[Parameters](#Parameterseducation.meCreateRefClasses)|Not Found|
|[az education education-me create-ref-school](#education.meCreateRefSchools)|CreateRefSchools|[Parameters](#Parameterseducation.meCreateRefSchools)|Not Found|
|[az education education-me create-ref-taught-class](#education.meCreateRefTaughtClasses)|CreateRefTaughtClasses|[Parameters](#Parameterseducation.meCreateRefTaughtClasses)|Not Found|
|[az education education-me create-rubric](#education.meCreateRubrics)|CreateRubrics|[Parameters](#Parameterseducation.meCreateRubrics)|Not Found|
|[az education education-me delete-assignment](#education.meDeleteAssignments)|DeleteAssignments|[Parameters](#Parameterseducation.meDeleteAssignments)|Not Found|
|[az education education-me delete-ref-user](#education.meDeleteRefUser)|DeleteRefUser|[Parameters](#Parameterseducation.meDeleteRefUser)|Not Found|
|[az education education-me delete-rubric](#education.meDeleteRubrics)|DeleteRubrics|[Parameters](#Parameterseducation.meDeleteRubrics)|Not Found|
|[az education education-me list-assignment](#education.meListAssignments)|ListAssignments|[Parameters](#Parameterseducation.meListAssignments)|Not Found|
|[az education education-me list-class](#education.meListClasses)|ListClasses|[Parameters](#Parameterseducation.meListClasses)|Not Found|
|[az education education-me list-ref-class](#education.meListRefClasses)|ListRefClasses|[Parameters](#Parameterseducation.meListRefClasses)|Not Found|
|[az education education-me list-ref-school](#education.meListRefSchools)|ListRefSchools|[Parameters](#Parameterseducation.meListRefSchools)|Not Found|
|[az education education-me list-ref-taught-class](#education.meListRefTaughtClasses)|ListRefTaughtClasses|[Parameters](#Parameterseducation.meListRefTaughtClasses)|Not Found|
|[az education education-me list-rubric](#education.meListRubrics)|ListRubrics|[Parameters](#Parameterseducation.meListRubrics)|Not Found|
|[az education education-me list-school](#education.meListSchools)|ListSchools|[Parameters](#Parameterseducation.meListSchools)|Not Found|
|[az education education-me list-taught-class](#education.meListTaughtClasses)|ListTaughtClasses|[Parameters](#Parameterseducation.meListTaughtClasses)|Not Found|
|[az education education-me set-ref-user](#education.meSetRefUser)|SetRefUser|[Parameters](#Parameterseducation.meSetRefUser)|Not Found|
|[az education education-me show-assignment](#education.meGetAssignments)|GetAssignments|[Parameters](#Parameterseducation.meGetAssignments)|Not Found|
|[az education education-me show-ref-user](#education.meGetRefUser)|GetRefUser|[Parameters](#Parameterseducation.meGetRefUser)|Not Found|
|[az education education-me show-rubric](#education.meGetRubrics)|GetRubrics|[Parameters](#Parameterseducation.meGetRubrics)|Not Found|
|[az education education-me show-user](#education.meGetUser)|GetUser|[Parameters](#Parameterseducation.meGetUser)|Not Found|
|[az education education-me update-assignment](#education.meUpdateAssignments)|UpdateAssignments|[Parameters](#Parameterseducation.meUpdateAssignments)|Not Found|
|[az education education-me update-rubric](#education.meUpdateRubrics)|UpdateRubrics|[Parameters](#Parameterseducation.meUpdateRubrics)|Not Found|

### <a name="CommandsIneducation.me.assignments">Commands in `az education education-me-assignment` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-me-assignment create-category](#education.me.assignmentsCreateCategories)|CreateCategories|[Parameters](#Parameterseducation.me.assignmentsCreateCategories)|Not Found|
|[az education education-me-assignment create-resource](#education.me.assignmentsCreateResources)|CreateResources|[Parameters](#Parameterseducation.me.assignmentsCreateResources)|Not Found|
|[az education education-me-assignment create-submission](#education.me.assignmentsCreateSubmissions)|CreateSubmissions|[Parameters](#Parameterseducation.me.assignmentsCreateSubmissions)|Not Found|
|[az education education-me-assignment delete-category](#education.me.assignmentsDeleteCategories)|DeleteCategories|[Parameters](#Parameterseducation.me.assignmentsDeleteCategories)|Not Found|
|[az education education-me-assignment delete-resource](#education.me.assignmentsDeleteResources)|DeleteResources|[Parameters](#Parameterseducation.me.assignmentsDeleteResources)|Not Found|
|[az education education-me-assignment delete-rubric](#education.me.assignmentsDeleteRubric)|DeleteRubric|[Parameters](#Parameterseducation.me.assignmentsDeleteRubric)|Not Found|
|[az education education-me-assignment delete-submission](#education.me.assignmentsDeleteSubmissions)|DeleteSubmissions|[Parameters](#Parameterseducation.me.assignmentsDeleteSubmissions)|Not Found|
|[az education education-me-assignment list-category](#education.me.assignmentsListCategories)|ListCategories|[Parameters](#Parameterseducation.me.assignmentsListCategories)|Not Found|
|[az education education-me-assignment list-resource](#education.me.assignmentsListResources)|ListResources|[Parameters](#Parameterseducation.me.assignmentsListResources)|Not Found|
|[az education education-me-assignment list-submission](#education.me.assignmentsListSubmissions)|ListSubmissions|[Parameters](#Parameterseducation.me.assignmentsListSubmissions)|Not Found|
|[az education education-me-assignment publish](#education.me.assignmentspublish)|publish|[Parameters](#Parameterseducation.me.assignmentspublish)|Not Found|
|[az education education-me-assignment show-category](#education.me.assignmentsGetCategories)|GetCategories|[Parameters](#Parameterseducation.me.assignmentsGetCategories)|Not Found|
|[az education education-me-assignment show-resource](#education.me.assignmentsGetResources)|GetResources|[Parameters](#Parameterseducation.me.assignmentsGetResources)|Not Found|
|[az education education-me-assignment show-resource-folder-url](#education.me.assignmentsgetResourcesFolderUrl)|getResourcesFolderUrl|[Parameters](#Parameterseducation.me.assignmentsgetResourcesFolderUrl)|Not Found|
|[az education education-me-assignment show-rubric](#education.me.assignmentsGetRubric)|GetRubric|[Parameters](#Parameterseducation.me.assignmentsGetRubric)|Not Found|
|[az education education-me-assignment show-submission](#education.me.assignmentsGetSubmissions)|GetSubmissions|[Parameters](#Parameterseducation.me.assignmentsGetSubmissions)|Not Found|
|[az education education-me-assignment update-category](#education.me.assignmentsUpdateCategories)|UpdateCategories|[Parameters](#Parameterseducation.me.assignmentsUpdateCategories)|Not Found|
|[az education education-me-assignment update-resource](#education.me.assignmentsUpdateResources)|UpdateResources|[Parameters](#Parameterseducation.me.assignmentsUpdateResources)|Not Found|
|[az education education-me-assignment update-rubric](#education.me.assignmentsUpdateRubric)|UpdateRubric|[Parameters](#Parameterseducation.me.assignmentsUpdateRubric)|Not Found|
|[az education education-me-assignment update-submission](#education.me.assignmentsUpdateSubmissions)|UpdateSubmissions|[Parameters](#Parameterseducation.me.assignmentsUpdateSubmissions)|Not Found|

### <a name="CommandsIneducation.me.assignments.submissions">Commands in `az education education-me-assignment-submission` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-me-assignment-submission create-outcome](#education.me.assignments.submissionsCreateOutcomes)|CreateOutcomes|[Parameters](#Parameterseducation.me.assignments.submissionsCreateOutcomes)|Not Found|
|[az education education-me-assignment-submission create-resource](#education.me.assignments.submissionsCreateResources)|CreateResources|[Parameters](#Parameterseducation.me.assignments.submissionsCreateResources)|Not Found|
|[az education education-me-assignment-submission create-submitted-resource](#education.me.assignments.submissionsCreateSubmittedResources)|CreateSubmittedResources|[Parameters](#Parameterseducation.me.assignments.submissionsCreateSubmittedResources)|Not Found|
|[az education education-me-assignment-submission delete-outcome](#education.me.assignments.submissionsDeleteOutcomes)|DeleteOutcomes|[Parameters](#Parameterseducation.me.assignments.submissionsDeleteOutcomes)|Not Found|
|[az education education-me-assignment-submission delete-resource](#education.me.assignments.submissionsDeleteResources)|DeleteResources|[Parameters](#Parameterseducation.me.assignments.submissionsDeleteResources)|Not Found|
|[az education education-me-assignment-submission delete-submitted-resource](#education.me.assignments.submissionsDeleteSubmittedResources)|DeleteSubmittedResources|[Parameters](#Parameterseducation.me.assignments.submissionsDeleteSubmittedResources)|Not Found|
|[az education education-me-assignment-submission list-outcome](#education.me.assignments.submissionsListOutcomes)|ListOutcomes|[Parameters](#Parameterseducation.me.assignments.submissionsListOutcomes)|Not Found|
|[az education education-me-assignment-submission list-resource](#education.me.assignments.submissionsListResources)|ListResources|[Parameters](#Parameterseducation.me.assignments.submissionsListResources)|Not Found|
|[az education education-me-assignment-submission list-submitted-resource](#education.me.assignments.submissionsListSubmittedResources)|ListSubmittedResources|[Parameters](#Parameterseducation.me.assignments.submissionsListSubmittedResources)|Not Found|
|[az education education-me-assignment-submission return](#education.me.assignments.submissionsreturn)|return|[Parameters](#Parameterseducation.me.assignments.submissionsreturn)|Not Found|
|[az education education-me-assignment-submission show-outcome](#education.me.assignments.submissionsGetOutcomes)|GetOutcomes|[Parameters](#Parameterseducation.me.assignments.submissionsGetOutcomes)|Not Found|
|[az education education-me-assignment-submission show-resource](#education.me.assignments.submissionsGetResources)|GetResources|[Parameters](#Parameterseducation.me.assignments.submissionsGetResources)|Not Found|
|[az education education-me-assignment-submission show-submitted-resource](#education.me.assignments.submissionsGetSubmittedResources)|GetSubmittedResources|[Parameters](#Parameterseducation.me.assignments.submissionsGetSubmittedResources)|Not Found|
|[az education education-me-assignment-submission submit](#education.me.assignments.submissionssubmit)|submit|[Parameters](#Parameterseducation.me.assignments.submissionssubmit)|Not Found|
|[az education education-me-assignment-submission unsubmit](#education.me.assignments.submissionsunsubmit)|unsubmit|[Parameters](#Parameterseducation.me.assignments.submissionsunsubmit)|Not Found|
|[az education education-me-assignment-submission update-outcome](#education.me.assignments.submissionsUpdateOutcomes)|UpdateOutcomes|[Parameters](#Parameterseducation.me.assignments.submissionsUpdateOutcomes)|Not Found|
|[az education education-me-assignment-submission update-resource](#education.me.assignments.submissionsUpdateResources)|UpdateResources|[Parameters](#Parameterseducation.me.assignments.submissionsUpdateResources)|Not Found|
|[az education education-me-assignment-submission update-submitted-resource](#education.me.assignments.submissionsUpdateSubmittedResources)|UpdateSubmittedResources|[Parameters](#Parameterseducation.me.assignments.submissionsUpdateSubmittedResources)|Not Found|

### <a name="CommandsIneducation.me.classes">Commands in `az education education-me-class` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-me-class delta](#education.me.classesdelta)|delta|[Parameters](#Parameterseducation.me.classesdelta)|Not Found|

### <a name="CommandsIneducation.me.schools">Commands in `az education education-me-school` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-me-school delta](#education.me.schoolsdelta)|delta|[Parameters](#Parameterseducation.me.schoolsdelta)|Not Found|

### <a name="CommandsIneducation.me.taughtClasses">Commands in `az education education-me-taught-class` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-me-taught-class delta](#education.me.taughtClassesdelta)|delta|[Parameters](#Parameterseducation.me.taughtClassesdelta)|Not Found|

### <a name="CommandsIneducation.educationRoot">Commands in `az education education-root` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-root show-education-root](#education.educationRootGetEducationRoot)|GetEducationRoot|[Parameters](#Parameterseducation.educationRootGetEducationRoot)|Not Found|
|[az education education-root update-education-root](#education.educationRootUpdateEducationRoot)|UpdateEducationRoot|[Parameters](#Parameterseducation.educationRootUpdateEducationRoot)|Not Found|

### <a name="CommandsIneducation.schools">Commands in `az education education-school` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-school create-ref-class](#education.schoolsCreateRefClasses)|CreateRefClasses|[Parameters](#Parameterseducation.schoolsCreateRefClasses)|Not Found|
|[az education education-school create-ref-user](#education.schoolsCreateRefUsers)|CreateRefUsers|[Parameters](#Parameterseducation.schoolsCreateRefUsers)|Not Found|
|[az education education-school delete-ref-administrative-unit](#education.schoolsDeleteRefAdministrativeUnit)|DeleteRefAdministrativeUnit|[Parameters](#Parameterseducation.schoolsDeleteRefAdministrativeUnit)|Not Found|
|[az education education-school delta](#education.schoolsdelta)|delta|[Parameters](#Parameterseducation.schoolsdelta)|Not Found|
|[az education education-school list-class](#education.schoolsListClasses)|ListClasses|[Parameters](#Parameterseducation.schoolsListClasses)|Not Found|
|[az education education-school list-ref-class](#education.schoolsListRefClasses)|ListRefClasses|[Parameters](#Parameterseducation.schoolsListRefClasses)|Not Found|
|[az education education-school list-ref-user](#education.schoolsListRefUsers)|ListRefUsers|[Parameters](#Parameterseducation.schoolsListRefUsers)|Not Found|
|[az education education-school list-user](#education.schoolsListUsers)|ListUsers|[Parameters](#Parameterseducation.schoolsListUsers)|Not Found|
|[az education education-school set-ref-administrative-unit](#education.schoolsSetRefAdministrativeUnit)|SetRefAdministrativeUnit|[Parameters](#Parameterseducation.schoolsSetRefAdministrativeUnit)|Not Found|
|[az education education-school show-administrative-unit](#education.schoolsGetAdministrativeUnit)|GetAdministrativeUnit|[Parameters](#Parameterseducation.schoolsGetAdministrativeUnit)|Not Found|
|[az education education-school show-ref-administrative-unit](#education.schoolsGetRefAdministrativeUnit)|GetRefAdministrativeUnit|[Parameters](#Parameterseducation.schoolsGetRefAdministrativeUnit)|Not Found|

### <a name="CommandsIneducation.schools.classes">Commands in `az education education-school-class` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-school-class delta](#education.schools.classesdelta)|delta|[Parameters](#Parameterseducation.schools.classesdelta)|Not Found|

### <a name="CommandsIneducation.schools.users">Commands in `az education education-school-user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-school-user delta](#education.schools.usersdelta)|delta|[Parameters](#Parameterseducation.schools.usersdelta)|Not Found|

### <a name="CommandsIneducation.synchronizationProfiles">Commands in `az education education-synchronization-profile` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-synchronization-profile create-error](#education.synchronizationProfilesCreateErrors)|CreateErrors|[Parameters](#Parameterseducation.synchronizationProfilesCreateErrors)|Not Found|
|[az education education-synchronization-profile delete-error](#education.synchronizationProfilesDeleteErrors)|DeleteErrors|[Parameters](#Parameterseducation.synchronizationProfilesDeleteErrors)|Not Found|
|[az education education-synchronization-profile delete-profile-status](#education.synchronizationProfilesDeleteProfileStatus)|DeleteProfileStatus|[Parameters](#Parameterseducation.synchronizationProfilesDeleteProfileStatus)|Not Found|
|[az education education-synchronization-profile list-error](#education.synchronizationProfilesListErrors)|ListErrors|[Parameters](#Parameterseducation.synchronizationProfilesListErrors)|Not Found|
|[az education education-synchronization-profile pause](#education.synchronizationProfilespause)|pause|[Parameters](#Parameterseducation.synchronizationProfilespause)|Not Found|
|[az education education-synchronization-profile reset](#education.synchronizationProfilesreset)|reset|[Parameters](#Parameterseducation.synchronizationProfilesreset)|Not Found|
|[az education education-synchronization-profile resume](#education.synchronizationProfilesresume)|resume|[Parameters](#Parameterseducation.synchronizationProfilesresume)|Not Found|
|[az education education-synchronization-profile show-error](#education.synchronizationProfilesGetErrors)|GetErrors|[Parameters](#Parameterseducation.synchronizationProfilesGetErrors)|Not Found|
|[az education education-synchronization-profile show-profile-status](#education.synchronizationProfilesGetProfileStatus)|GetProfileStatus|[Parameters](#Parameterseducation.synchronizationProfilesGetProfileStatus)|Not Found|
|[az education education-synchronization-profile start](#education.synchronizationProfilesstart)|start|[Parameters](#Parameterseducation.synchronizationProfilesstart)|Not Found|
|[az education education-synchronization-profile update-error](#education.synchronizationProfilesUpdateErrors)|UpdateErrors|[Parameters](#Parameterseducation.synchronizationProfilesUpdateErrors)|Not Found|
|[az education education-synchronization-profile update-profile-status](#education.synchronizationProfilesUpdateProfileStatus)|UpdateProfileStatus|[Parameters](#Parameterseducation.synchronizationProfilesUpdateProfileStatus)|Not Found|
|[az education education-synchronization-profile upload-url](#education.synchronizationProfilesuploadUrl)|uploadUrl|[Parameters](#Parameterseducation.synchronizationProfilesuploadUrl)|Not Found|

### <a name="CommandsIneducation.users">Commands in `az education education-user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-user create-assignment](#education.usersCreateAssignments)|CreateAssignments|[Parameters](#Parameterseducation.usersCreateAssignments)|Not Found|
|[az education education-user create-ref-class](#education.usersCreateRefClasses)|CreateRefClasses|[Parameters](#Parameterseducation.usersCreateRefClasses)|Not Found|
|[az education education-user create-ref-school](#education.usersCreateRefSchools)|CreateRefSchools|[Parameters](#Parameterseducation.usersCreateRefSchools)|Not Found|
|[az education education-user create-ref-taught-class](#education.usersCreateRefTaughtClasses)|CreateRefTaughtClasses|[Parameters](#Parameterseducation.usersCreateRefTaughtClasses)|Not Found|
|[az education education-user create-rubric](#education.usersCreateRubrics)|CreateRubrics|[Parameters](#Parameterseducation.usersCreateRubrics)|Not Found|
|[az education education-user delete-assignment](#education.usersDeleteAssignments)|DeleteAssignments|[Parameters](#Parameterseducation.usersDeleteAssignments)|Not Found|
|[az education education-user delete-ref-user](#education.usersDeleteRefUser)|DeleteRefUser|[Parameters](#Parameterseducation.usersDeleteRefUser)|Not Found|
|[az education education-user delete-rubric](#education.usersDeleteRubrics)|DeleteRubrics|[Parameters](#Parameterseducation.usersDeleteRubrics)|Not Found|
|[az education education-user delta](#education.usersdelta)|delta|[Parameters](#Parameterseducation.usersdelta)|Not Found|
|[az education education-user list-assignment](#education.usersListAssignments)|ListAssignments|[Parameters](#Parameterseducation.usersListAssignments)|Not Found|
|[az education education-user list-class](#education.usersListClasses)|ListClasses|[Parameters](#Parameterseducation.usersListClasses)|Not Found|
|[az education education-user list-ref-class](#education.usersListRefClasses)|ListRefClasses|[Parameters](#Parameterseducation.usersListRefClasses)|Not Found|
|[az education education-user list-ref-school](#education.usersListRefSchools)|ListRefSchools|[Parameters](#Parameterseducation.usersListRefSchools)|Not Found|
|[az education education-user list-ref-taught-class](#education.usersListRefTaughtClasses)|ListRefTaughtClasses|[Parameters](#Parameterseducation.usersListRefTaughtClasses)|Not Found|
|[az education education-user list-rubric](#education.usersListRubrics)|ListRubrics|[Parameters](#Parameterseducation.usersListRubrics)|Not Found|
|[az education education-user list-school](#education.usersListSchools)|ListSchools|[Parameters](#Parameterseducation.usersListSchools)|Not Found|
|[az education education-user list-taught-class](#education.usersListTaughtClasses)|ListTaughtClasses|[Parameters](#Parameterseducation.usersListTaughtClasses)|Not Found|
|[az education education-user set-ref-user](#education.usersSetRefUser)|SetRefUser|[Parameters](#Parameterseducation.usersSetRefUser)|Not Found|
|[az education education-user show-assignment](#education.usersGetAssignments)|GetAssignments|[Parameters](#Parameterseducation.usersGetAssignments)|Not Found|
|[az education education-user show-ref-user](#education.usersGetRefUser)|GetRefUser|[Parameters](#Parameterseducation.usersGetRefUser)|Not Found|
|[az education education-user show-rubric](#education.usersGetRubrics)|GetRubrics|[Parameters](#Parameterseducation.usersGetRubrics)|Not Found|
|[az education education-user show-user](#education.usersGetUser)|GetUser|[Parameters](#Parameterseducation.usersGetUser)|Not Found|
|[az education education-user update-assignment](#education.usersUpdateAssignments)|UpdateAssignments|[Parameters](#Parameterseducation.usersUpdateAssignments)|Not Found|
|[az education education-user update-rubric](#education.usersUpdateRubrics)|UpdateRubrics|[Parameters](#Parameterseducation.usersUpdateRubrics)|Not Found|

### <a name="CommandsIneducation.users.assignments">Commands in `az education education-user-assignment` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-user-assignment create-category](#education.users.assignmentsCreateCategories)|CreateCategories|[Parameters](#Parameterseducation.users.assignmentsCreateCategories)|Not Found|
|[az education education-user-assignment create-resource](#education.users.assignmentsCreateResources)|CreateResources|[Parameters](#Parameterseducation.users.assignmentsCreateResources)|Not Found|
|[az education education-user-assignment create-submission](#education.users.assignmentsCreateSubmissions)|CreateSubmissions|[Parameters](#Parameterseducation.users.assignmentsCreateSubmissions)|Not Found|
|[az education education-user-assignment delete-category](#education.users.assignmentsDeleteCategories)|DeleteCategories|[Parameters](#Parameterseducation.users.assignmentsDeleteCategories)|Not Found|
|[az education education-user-assignment delete-resource](#education.users.assignmentsDeleteResources)|DeleteResources|[Parameters](#Parameterseducation.users.assignmentsDeleteResources)|Not Found|
|[az education education-user-assignment delete-rubric](#education.users.assignmentsDeleteRubric)|DeleteRubric|[Parameters](#Parameterseducation.users.assignmentsDeleteRubric)|Not Found|
|[az education education-user-assignment delete-submission](#education.users.assignmentsDeleteSubmissions)|DeleteSubmissions|[Parameters](#Parameterseducation.users.assignmentsDeleteSubmissions)|Not Found|
|[az education education-user-assignment list-category](#education.users.assignmentsListCategories)|ListCategories|[Parameters](#Parameterseducation.users.assignmentsListCategories)|Not Found|
|[az education education-user-assignment list-resource](#education.users.assignmentsListResources)|ListResources|[Parameters](#Parameterseducation.users.assignmentsListResources)|Not Found|
|[az education education-user-assignment list-submission](#education.users.assignmentsListSubmissions)|ListSubmissions|[Parameters](#Parameterseducation.users.assignmentsListSubmissions)|Not Found|
|[az education education-user-assignment publish](#education.users.assignmentspublish)|publish|[Parameters](#Parameterseducation.users.assignmentspublish)|Not Found|
|[az education education-user-assignment show-category](#education.users.assignmentsGetCategories)|GetCategories|[Parameters](#Parameterseducation.users.assignmentsGetCategories)|Not Found|
|[az education education-user-assignment show-resource](#education.users.assignmentsGetResources)|GetResources|[Parameters](#Parameterseducation.users.assignmentsGetResources)|Not Found|
|[az education education-user-assignment show-resource-folder-url](#education.users.assignmentsgetResourcesFolderUrl)|getResourcesFolderUrl|[Parameters](#Parameterseducation.users.assignmentsgetResourcesFolderUrl)|Not Found|
|[az education education-user-assignment show-rubric](#education.users.assignmentsGetRubric)|GetRubric|[Parameters](#Parameterseducation.users.assignmentsGetRubric)|Not Found|
|[az education education-user-assignment show-submission](#education.users.assignmentsGetSubmissions)|GetSubmissions|[Parameters](#Parameterseducation.users.assignmentsGetSubmissions)|Not Found|
|[az education education-user-assignment update-category](#education.users.assignmentsUpdateCategories)|UpdateCategories|[Parameters](#Parameterseducation.users.assignmentsUpdateCategories)|Not Found|
|[az education education-user-assignment update-resource](#education.users.assignmentsUpdateResources)|UpdateResources|[Parameters](#Parameterseducation.users.assignmentsUpdateResources)|Not Found|
|[az education education-user-assignment update-rubric](#education.users.assignmentsUpdateRubric)|UpdateRubric|[Parameters](#Parameterseducation.users.assignmentsUpdateRubric)|Not Found|
|[az education education-user-assignment update-submission](#education.users.assignmentsUpdateSubmissions)|UpdateSubmissions|[Parameters](#Parameterseducation.users.assignmentsUpdateSubmissions)|Not Found|

### <a name="CommandsIneducation.users.assignments.submissions">Commands in `az education education-user-assignment-submission` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-user-assignment-submission create-outcome](#education.users.assignments.submissionsCreateOutcomes)|CreateOutcomes|[Parameters](#Parameterseducation.users.assignments.submissionsCreateOutcomes)|Not Found|
|[az education education-user-assignment-submission create-resource](#education.users.assignments.submissionsCreateResources)|CreateResources|[Parameters](#Parameterseducation.users.assignments.submissionsCreateResources)|Not Found|
|[az education education-user-assignment-submission create-submitted-resource](#education.users.assignments.submissionsCreateSubmittedResources)|CreateSubmittedResources|[Parameters](#Parameterseducation.users.assignments.submissionsCreateSubmittedResources)|Not Found|
|[az education education-user-assignment-submission delete-outcome](#education.users.assignments.submissionsDeleteOutcomes)|DeleteOutcomes|[Parameters](#Parameterseducation.users.assignments.submissionsDeleteOutcomes)|Not Found|
|[az education education-user-assignment-submission delete-resource](#education.users.assignments.submissionsDeleteResources)|DeleteResources|[Parameters](#Parameterseducation.users.assignments.submissionsDeleteResources)|Not Found|
|[az education education-user-assignment-submission delete-submitted-resource](#education.users.assignments.submissionsDeleteSubmittedResources)|DeleteSubmittedResources|[Parameters](#Parameterseducation.users.assignments.submissionsDeleteSubmittedResources)|Not Found|
|[az education education-user-assignment-submission list-outcome](#education.users.assignments.submissionsListOutcomes)|ListOutcomes|[Parameters](#Parameterseducation.users.assignments.submissionsListOutcomes)|Not Found|
|[az education education-user-assignment-submission list-resource](#education.users.assignments.submissionsListResources)|ListResources|[Parameters](#Parameterseducation.users.assignments.submissionsListResources)|Not Found|
|[az education education-user-assignment-submission list-submitted-resource](#education.users.assignments.submissionsListSubmittedResources)|ListSubmittedResources|[Parameters](#Parameterseducation.users.assignments.submissionsListSubmittedResources)|Not Found|
|[az education education-user-assignment-submission return](#education.users.assignments.submissionsreturn)|return|[Parameters](#Parameterseducation.users.assignments.submissionsreturn)|Not Found|
|[az education education-user-assignment-submission show-outcome](#education.users.assignments.submissionsGetOutcomes)|GetOutcomes|[Parameters](#Parameterseducation.users.assignments.submissionsGetOutcomes)|Not Found|
|[az education education-user-assignment-submission show-resource](#education.users.assignments.submissionsGetResources)|GetResources|[Parameters](#Parameterseducation.users.assignments.submissionsGetResources)|Not Found|
|[az education education-user-assignment-submission show-submitted-resource](#education.users.assignments.submissionsGetSubmittedResources)|GetSubmittedResources|[Parameters](#Parameterseducation.users.assignments.submissionsGetSubmittedResources)|Not Found|
|[az education education-user-assignment-submission submit](#education.users.assignments.submissionssubmit)|submit|[Parameters](#Parameterseducation.users.assignments.submissionssubmit)|Not Found|
|[az education education-user-assignment-submission unsubmit](#education.users.assignments.submissionsunsubmit)|unsubmit|[Parameters](#Parameterseducation.users.assignments.submissionsunsubmit)|Not Found|
|[az education education-user-assignment-submission update-outcome](#education.users.assignments.submissionsUpdateOutcomes)|UpdateOutcomes|[Parameters](#Parameterseducation.users.assignments.submissionsUpdateOutcomes)|Not Found|
|[az education education-user-assignment-submission update-resource](#education.users.assignments.submissionsUpdateResources)|UpdateResources|[Parameters](#Parameterseducation.users.assignments.submissionsUpdateResources)|Not Found|
|[az education education-user-assignment-submission update-submitted-resource](#education.users.assignments.submissionsUpdateSubmittedResources)|UpdateSubmittedResources|[Parameters](#Parameterseducation.users.assignments.submissionsUpdateSubmittedResources)|Not Found|

### <a name="CommandsIneducation.users.classes">Commands in `az education education-user-class` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-user-class delta](#education.users.classesdelta)|delta|[Parameters](#Parameterseducation.users.classesdelta)|Not Found|

### <a name="CommandsIneducation.users.schools">Commands in `az education education-user-school` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-user-school delta](#education.users.schoolsdelta)|delta|[Parameters](#Parameterseducation.users.schoolsdelta)|Not Found|

### <a name="CommandsIneducation.users.taughtClasses">Commands in `az education education-user-taught-class` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-user-taught-class delta](#education.users.taughtClassesdelta)|delta|[Parameters](#Parameterseducation.users.taughtClassesdelta)|Not Found|


## COMMAND DETAILS

### group `az education education`
#### <a name="educationCreateClasses">Command `az education education create-class`</a>

##### <a name="ParameterseducationCreateClasses">Parameters</a> 
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
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="educationCreateSchools">Command `az education education create-school`</a>

##### <a name="ParameterseducationCreateSchools">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--microsoft-graph-administrative-unit-description**|string|An optional description for the administrative unit.|microsoft_graph_administrative_unit_description|description|
|**--microsoft-graph-administrative-unit-display-name**|string|Display name for the administrative unit.|microsoft_graph_administrative_unit_display_name|displayName|
|**--visibility**|string|Controls whether the administrative unit and its members are hidden or public. Can be set to HiddenMembership or Public. If not set, default behavior is Public. When set to HiddenMembership, only members of the administrative unit can list other members of the adminstrative unit.|visibility|visibility|
|**--members**|array|Users and groups that are members of this Adminsitrative Unit. HTTP Methods: GET (list members), POST (add members), DELETE (remove members).|members|members|
|**--scoped-role-members**|array|Scoped-role members of this Administrative Unit.  HTTP Methods: GET (list scopedRoleMemberships), POST (add scopedRoleMembership), DELETE (remove scopedRoleMembership).|scoped_role_members|scopedRoleMembers|
|**--extensions**|array||extensions|extensions|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="educationCreateSynchronizationProfiles">Command `az education education create-synchronization-profile`</a>

##### <a name="ParameterseducationCreateSynchronizationProfiles">Parameters</a> 
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

#### <a name="educationCreateUsers">Command `az education education create-user`</a>

##### <a name="ParameterseducationCreateUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--related-contacts**|array|Set of contacts related to the user.  This optional property must be specified in a $select clause and can only be retrieved for an individual user.|related_contacts|relatedContacts|
|**--account-enabled**|boolean|True if the account is enabled; otherwise, false. This property is required when a user is created. Supports $filter.|account_enabled|accountEnabled|
|**--assigned-licenses**|array|The licenses that are assigned to the user. Not nullable.|assigned_licenses|assignedLicenses|
|**--assigned-plans**|array|The plans that are assigned to the user. Read-only. Not nullable.|assigned_plans|assignedPlans|
|**--business-phones**|array|The telephone numbers for the user. Note: Although this is a string collection, only one number can be set for this property.|business_phones|businessPhones|
|**--department**|string|The name for the department in which the user works. Supports $filter.|department|department|
|**--display-name**|string|The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates. Supports $filter and $orderby.|display_name|displayName|
|**--external-source**|choice||external_source|externalSource|
|**--external-source-detail**|string||external_source_detail|externalSourceDetail|
|**--given-name**|string|The given name (first name) of the user. Supports $filter.|given_name|givenName|
|**--mail**|string|The SMTP address for the user; for example, 'jeff@contoso.onmicrosoft.com'. Read-Only. Supports $filter.|mail|mail|
|**--mailing-address**|object|physicalAddress|mailing_address|mailingAddress|
|**--mail-nickname**|string|The mail alias for the user. This property must be specified when a user is created. Supports $filter.|mail_nickname|mailNickname|
|**--middle-name**|string|The middle name of user.|middle_name|middleName|
|**--mobile-phone**|string|The primary cellular telephone number for the user.|mobile_phone|mobilePhone|
|**--office-location**|string||office_location|officeLocation|
|**--password-policies**|string|Specifies password policies for the user. This value is an enumeration with one possible value being 'DisableStrongPassword', which allows weaker passwords than the default policy to be specified. 'DisablePasswordExpiration' can also be specified. The two can be specified together; for example: 'DisablePasswordExpiration, DisableStrongPassword'.|password_policies|passwordPolicies|
|**--password-profile**|object|passwordProfile|password_profile|passwordProfile|
|**--preferred-language**|string|The preferred language for the user. Should follow ISO 639-1 Code; for example, 'en-US'.|preferred_language|preferredLanguage|
|**--primary-role**|choice||primary_role|primaryRole|
|**--provisioned-plans**|array|The plans that are provisioned for the user. Read-only. Not nullable.|provisioned_plans|provisionedPlans|
|**--refresh-tokens-valid-from-date-time**|date-time||refresh_tokens_valid_from_date_time|refreshTokensValidFromDateTime|
|**--residence-address**|object|physicalAddress|residence_address|residenceAddress|
|**--show-in-address-list**|boolean||show_in_address_list|showInAddressList|
|**--student**|object|educationStudent|student|student|
|**--surname**|string|The user's surname (family name or last name). Supports $filter.|surname|surname|
|**--teacher**|object|educationTeacher|teacher|teacher|
|**--usage-location**|string|A two-letter country code (ISO standard 3166). Required for users who will be assigned licenses due to a legal requirement to check for availability of services in countries or regions. Examples include: 'US', 'JP', and 'GB'. Not nullable. Supports $filter.|usage_location|usageLocation|
|**--user-principal-name**|string|The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of organization. Supports $filter and $orderby.|user_principal_name|userPrincipalName|
|**--user-type**|string|A string value that can be used to classify user types in your directory, such as 'Member' and 'Guest'. Supports $filter.|user_type|userType|
|**--assignments**|array|List of assignments for the user. Nullable.|assignments|assignments|
|**--rubrics**|array||rubrics|rubrics|
|**--classes**|array|Classes to which the user belongs. Nullable.|classes|classes|
|**--schools**|array|Schools to which the user belongs. Nullable.|schools|schools|
|**--taught-classes**|array||taught_classes|taughtClasses|
|**--user**|object|Represents an Azure Active Directory user object.|user|user|
|**--immutable-id**|string||immutable_id|immutableId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="educationDeleteClasses">Command `az education education delete-class`</a>

##### <a name="ParameterseducationDeleteClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="educationDeleteMe">Command `az education education delete-me`</a>

##### <a name="ParameterseducationDeleteMe">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="educationDeleteSchools">Command `az education education delete-school`</a>

##### <a name="ParameterseducationDeleteSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="educationDeleteSynchronizationProfiles">Command `az education education delete-synchronization-profile`</a>

##### <a name="ParameterseducationDeleteSynchronizationProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="educationDeleteUsers">Command `az education education delete-user`</a>

##### <a name="ParameterseducationDeleteUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="educationListClasses">Command `az education education list-class`</a>

##### <a name="ParameterseducationListClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="educationListSchools">Command `az education education list-school`</a>

##### <a name="ParameterseducationListSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="educationListSynchronizationProfiles">Command `az education education list-synchronization-profile`</a>

##### <a name="ParameterseducationListSynchronizationProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="educationListUsers">Command `az education education list-user`</a>

##### <a name="ParameterseducationListUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="educationGetClasses">Command `az education education show-class`</a>

##### <a name="ParameterseducationGetClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="educationGetMe">Command `az education education show-me`</a>

##### <a name="ParameterseducationGetMe">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="educationGetSchools">Command `az education education show-school`</a>

##### <a name="ParameterseducationGetSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="educationGetSynchronizationProfiles">Command `az education education show-synchronization-profile`</a>

##### <a name="ParameterseducationGetSynchronizationProfiles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="educationGetUsers">Command `az education education show-user`</a>

##### <a name="ParameterseducationGetUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="educationUpdateClasses">Command `az education education update-class`</a>

##### <a name="ParameterseducationUpdateClasses">Parameters</a> 
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
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="educationUpdateMe">Command `az education education update-me`</a>

##### <a name="ParameterseducationUpdateMe">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--related-contacts**|array|Set of contacts related to the user.  This optional property must be specified in a $select clause and can only be retrieved for an individual user.|related_contacts|relatedContacts|
|**--account-enabled**|boolean|True if the account is enabled; otherwise, false. This property is required when a user is created. Supports $filter.|account_enabled|accountEnabled|
|**--assigned-licenses**|array|The licenses that are assigned to the user. Not nullable.|assigned_licenses|assignedLicenses|
|**--assigned-plans**|array|The plans that are assigned to the user. Read-only. Not nullable.|assigned_plans|assignedPlans|
|**--business-phones**|array|The telephone numbers for the user. Note: Although this is a string collection, only one number can be set for this property.|business_phones|businessPhones|
|**--department**|string|The name for the department in which the user works. Supports $filter.|department|department|
|**--display-name**|string|The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates. Supports $filter and $orderby.|display_name|displayName|
|**--external-source**|choice||external_source|externalSource|
|**--external-source-detail**|string||external_source_detail|externalSourceDetail|
|**--given-name**|string|The given name (first name) of the user. Supports $filter.|given_name|givenName|
|**--mail**|string|The SMTP address for the user; for example, 'jeff@contoso.onmicrosoft.com'. Read-Only. Supports $filter.|mail|mail|
|**--mailing-address**|object|physicalAddress|mailing_address|mailingAddress|
|**--mail-nickname**|string|The mail alias for the user. This property must be specified when a user is created. Supports $filter.|mail_nickname|mailNickname|
|**--middle-name**|string|The middle name of user.|middle_name|middleName|
|**--mobile-phone**|string|The primary cellular telephone number for the user.|mobile_phone|mobilePhone|
|**--office-location**|string||office_location|officeLocation|
|**--password-policies**|string|Specifies password policies for the user. This value is an enumeration with one possible value being 'DisableStrongPassword', which allows weaker passwords than the default policy to be specified. 'DisablePasswordExpiration' can also be specified. The two can be specified together; for example: 'DisablePasswordExpiration, DisableStrongPassword'.|password_policies|passwordPolicies|
|**--password-profile**|object|passwordProfile|password_profile|passwordProfile|
|**--preferred-language**|string|The preferred language for the user. Should follow ISO 639-1 Code; for example, 'en-US'.|preferred_language|preferredLanguage|
|**--primary-role**|choice||primary_role|primaryRole|
|**--provisioned-plans**|array|The plans that are provisioned for the user. Read-only. Not nullable.|provisioned_plans|provisionedPlans|
|**--refresh-tokens-valid-from-date-time**|date-time||refresh_tokens_valid_from_date_time|refreshTokensValidFromDateTime|
|**--residence-address**|object|physicalAddress|residence_address|residenceAddress|
|**--show-in-address-list**|boolean||show_in_address_list|showInAddressList|
|**--student**|object|educationStudent|student|student|
|**--surname**|string|The user's surname (family name or last name). Supports $filter.|surname|surname|
|**--teacher**|object|educationTeacher|teacher|teacher|
|**--usage-location**|string|A two-letter country code (ISO standard 3166). Required for users who will be assigned licenses due to a legal requirement to check for availability of services in countries or regions. Examples include: 'US', 'JP', and 'GB'. Not nullable. Supports $filter.|usage_location|usageLocation|
|**--user-principal-name**|string|The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of organization. Supports $filter and $orderby.|user_principal_name|userPrincipalName|
|**--user-type**|string|A string value that can be used to classify user types in your directory, such as 'Member' and 'Guest'. Supports $filter.|user_type|userType|
|**--assignments**|array|List of assignments for the user. Nullable.|assignments|assignments|
|**--rubrics**|array||rubrics|rubrics|
|**--classes**|array|Classes to which the user belongs. Nullable.|classes|classes|
|**--schools**|array|Schools to which the user belongs. Nullable.|schools|schools|
|**--taught-classes**|array||taught_classes|taughtClasses|
|**--user**|object|Represents an Azure Active Directory user object.|user|user|
|**--immutable-id**|string||immutable_id|immutableId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="educationUpdateSchools">Command `az education education update-school`</a>

##### <a name="ParameterseducationUpdateSchools">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--microsoft-graph-administrative-unit-description**|string|An optional description for the administrative unit.|microsoft_graph_administrative_unit_description|description|
|**--microsoft-graph-administrative-unit-display-name**|string|Display name for the administrative unit.|microsoft_graph_administrative_unit_display_name|displayName|
|**--visibility**|string|Controls whether the administrative unit and its members are hidden or public. Can be set to HiddenMembership or Public. If not set, default behavior is Public. When set to HiddenMembership, only members of the administrative unit can list other members of the adminstrative unit.|visibility|visibility|
|**--members**|array|Users and groups that are members of this Adminsitrative Unit. HTTP Methods: GET (list members), POST (add members), DELETE (remove members).|members|members|
|**--scoped-role-members**|array|Scoped-role members of this Administrative Unit.  HTTP Methods: GET (list scopedRoleMemberships), POST (add scopedRoleMembership), DELETE (remove scopedRoleMembership).|scoped_role_members|scopedRoleMembers|
|**--extensions**|array||extensions|extensions|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="educationUpdateSynchronizationProfiles">Command `az education education update-synchronization-profile`</a>

##### <a name="ParameterseducationUpdateSynchronizationProfiles">Parameters</a> 
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

#### <a name="educationUpdateUsers">Command `az education education update-user`</a>

##### <a name="ParameterseducationUpdateUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--id**|string|Read-only.|id|id|
|**--related-contacts**|array|Set of contacts related to the user.  This optional property must be specified in a $select clause and can only be retrieved for an individual user.|related_contacts|relatedContacts|
|**--account-enabled**|boolean|True if the account is enabled; otherwise, false. This property is required when a user is created. Supports $filter.|account_enabled|accountEnabled|
|**--assigned-licenses**|array|The licenses that are assigned to the user. Not nullable.|assigned_licenses|assignedLicenses|
|**--assigned-plans**|array|The plans that are assigned to the user. Read-only. Not nullable.|assigned_plans|assignedPlans|
|**--business-phones**|array|The telephone numbers for the user. Note: Although this is a string collection, only one number can be set for this property.|business_phones|businessPhones|
|**--department**|string|The name for the department in which the user works. Supports $filter.|department|department|
|**--display-name**|string|The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates. Supports $filter and $orderby.|display_name|displayName|
|**--external-source**|choice||external_source|externalSource|
|**--external-source-detail**|string||external_source_detail|externalSourceDetail|
|**--given-name**|string|The given name (first name) of the user. Supports $filter.|given_name|givenName|
|**--mail**|string|The SMTP address for the user; for example, 'jeff@contoso.onmicrosoft.com'. Read-Only. Supports $filter.|mail|mail|
|**--mailing-address**|object|physicalAddress|mailing_address|mailingAddress|
|**--mail-nickname**|string|The mail alias for the user. This property must be specified when a user is created. Supports $filter.|mail_nickname|mailNickname|
|**--middle-name**|string|The middle name of user.|middle_name|middleName|
|**--mobile-phone**|string|The primary cellular telephone number for the user.|mobile_phone|mobilePhone|
|**--office-location**|string||office_location|officeLocation|
|**--password-policies**|string|Specifies password policies for the user. This value is an enumeration with one possible value being 'DisableStrongPassword', which allows weaker passwords than the default policy to be specified. 'DisablePasswordExpiration' can also be specified. The two can be specified together; for example: 'DisablePasswordExpiration, DisableStrongPassword'.|password_policies|passwordPolicies|
|**--password-profile**|object|passwordProfile|password_profile|passwordProfile|
|**--preferred-language**|string|The preferred language for the user. Should follow ISO 639-1 Code; for example, 'en-US'.|preferred_language|preferredLanguage|
|**--primary-role**|choice||primary_role|primaryRole|
|**--provisioned-plans**|array|The plans that are provisioned for the user. Read-only. Not nullable.|provisioned_plans|provisionedPlans|
|**--refresh-tokens-valid-from-date-time**|date-time||refresh_tokens_valid_from_date_time|refreshTokensValidFromDateTime|
|**--residence-address**|object|physicalAddress|residence_address|residenceAddress|
|**--show-in-address-list**|boolean||show_in_address_list|showInAddressList|
|**--student**|object|educationStudent|student|student|
|**--surname**|string|The user's surname (family name or last name). Supports $filter.|surname|surname|
|**--teacher**|object|educationTeacher|teacher|teacher|
|**--usage-location**|string|A two-letter country code (ISO standard 3166). Required for users who will be assigned licenses due to a legal requirement to check for availability of services in countries or regions. Examples include: 'US', 'JP', and 'GB'. Not nullable. Supports $filter.|usage_location|usageLocation|
|**--user-principal-name**|string|The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of organization. Supports $filter and $orderby.|user_principal_name|userPrincipalName|
|**--user-type**|string|A string value that can be used to classify user types in your directory, such as 'Member' and 'Guest'. Supports $filter.|user_type|userType|
|**--assignments**|array|List of assignments for the user. Nullable.|assignments|assignments|
|**--rubrics**|array||rubrics|rubrics|
|**--classes**|array|Classes to which the user belongs. Nullable.|classes|classes|
|**--schools**|array|Schools to which the user belongs. Nullable.|schools|schools|
|**--taught-classes**|array||taught_classes|taughtClasses|
|**--user**|object|Represents an Azure Active Directory user object.|user|user|
|**--immutable-id**|string||immutable_id|immutableId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

### group `az education education-class`
#### <a name="education.classesCreateAssignments">Command `az education education-class create-assignment`</a>

##### <a name="Parameterseducation.classesCreateAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-education-rubric-created-date-time-created-date-time**|date-time||microsoft_graph_education_rubric_created_date_time_created_date_time|createdDateTime|
|**--description**|object|educationItemBody|description|description|
|**--microsoft-graph-education-rubric-display-name**|string||microsoft_graph_education_rubric_display_name|displayName|
|**--microsoft-graph-education-assignment-grade-type-grading**|dictionary|educationAssignmentGradeType|microsoft_graph_education_assignment_grade_type_grading|grading|
|**--microsoft-graph-education-rubric-last-modified-date-time-last-modified-date-time**|date-time||microsoft_graph_education_rubric_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--levels**|array||levels|levels|
|**--qualities**|array||qualities|qualities|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|

#### <a name="education.classesCreateAssignmentCategories">Command `az education education-class create-assignment-category`</a>

##### <a name="Parameterseducation.classesCreateAssignmentCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

#### <a name="education.classesCreateRefMembers">Command `az education education-class create-ref-member`</a>

##### <a name="Parameterseducation.classesCreateRefMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.classesCreateRefSchools">Command `az education education-class create-ref-school`</a>

##### <a name="Parameterseducation.classesCreateRefSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.classesCreateRefTeachers">Command `az education education-class create-ref-teacher`</a>

##### <a name="Parameterseducation.classesCreateRefTeachers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.classesDeleteAssignments">Command `az education education-class delete-assignment`</a>

##### <a name="Parameterseducation.classesDeleteAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.classesDeleteAssignmentCategories">Command `az education education-class delete-assignment-category`</a>

##### <a name="Parameterseducation.classesDeleteAssignmentCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.classesDeleteRefGroup">Command `az education education-class delete-ref-group`</a>

##### <a name="Parameterseducation.classesDeleteRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.classesdelta">Command `az education education-class delta`</a>

##### <a name="Parameterseducation.classesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="education.classesListAssignments">Command `az education education-class list-assignment`</a>

##### <a name="Parameterseducation.classesListAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classesListAssignmentCategories">Command `az education education-class list-assignment-category`</a>

##### <a name="Parameterseducation.classesListAssignmentCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classesListMembers">Command `az education education-class list-member`</a>

##### <a name="Parameterseducation.classesListMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classesListRefMembers">Command `az education education-class list-ref-member`</a>

##### <a name="Parameterseducation.classesListRefMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.classesListRefSchools">Command `az education education-class list-ref-school`</a>

##### <a name="Parameterseducation.classesListRefSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.classesListRefTeachers">Command `az education education-class list-ref-teacher`</a>

##### <a name="Parameterseducation.classesListRefTeachers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.classesListSchools">Command `az education education-class list-school`</a>

##### <a name="Parameterseducation.classesListSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classesListTeachers">Command `az education education-class list-teacher`</a>

##### <a name="Parameterseducation.classesListTeachers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classesSetRefGroup">Command `az education education-class set-ref-group`</a>

##### <a name="Parameterseducation.classesSetRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="education.classesGetAssignments">Command `az education education-class show-assignment`</a>

##### <a name="Parameterseducation.classesGetAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classesGetAssignmentCategories">Command `az education education-class show-assignment-category`</a>

##### <a name="Parameterseducation.classesGetAssignmentCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classesGetGroup">Command `az education education-class show-group`</a>

##### <a name="Parameterseducation.classesGetGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classesGetRefGroup">Command `az education education-class show-ref-group`</a>

##### <a name="Parameterseducation.classesGetRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|

#### <a name="education.classesUpdateAssignments">Command `az education education-class update-assignment`</a>

##### <a name="Parameterseducation.classesUpdateAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-education-rubric-created-date-time-created-date-time**|date-time||microsoft_graph_education_rubric_created_date_time_created_date_time|createdDateTime|
|**--description**|object|educationItemBody|description|description|
|**--microsoft-graph-education-rubric-display-name**|string||microsoft_graph_education_rubric_display_name|displayName|
|**--microsoft-graph-education-assignment-grade-type-grading**|dictionary|educationAssignmentGradeType|microsoft_graph_education_assignment_grade_type_grading|grading|
|**--microsoft-graph-education-rubric-last-modified-date-time-last-modified-date-time**|date-time||microsoft_graph_education_rubric_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--levels**|array||levels|levels|
|**--qualities**|array||qualities|qualities|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|

#### <a name="education.classesUpdateAssignmentCategories">Command `az education education-class update-assignment-category`</a>

##### <a name="Parameterseducation.classesUpdateAssignmentCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### group `az education education-class-assignment`
#### <a name="education.classes.assignmentsCreateCategories">Command `az education education-class-assignment create-category`</a>

##### <a name="Parameterseducation.classes.assignmentsCreateCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

#### <a name="education.classes.assignmentsCreateResources">Command `az education education-class-assignment create-resource`</a>

##### <a name="Parameterseducation.classes.assignmentsCreateResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

#### <a name="education.classes.assignmentsCreateSubmissions">Command `az education education-class-assignment create-submission`</a>

##### <a name="Parameterseducation.classes.assignmentsCreateSubmissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
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
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|

#### <a name="education.classes.assignmentsDeleteCategories">Command `az education education-class-assignment delete-category`</a>

##### <a name="Parameterseducation.classes.assignmentsDeleteCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.classes.assignmentsDeleteResources">Command `az education education-class-assignment delete-resource`</a>

##### <a name="Parameterseducation.classes.assignmentsDeleteResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.classes.assignmentsDeleteRubric">Command `az education education-class-assignment delete-rubric`</a>

##### <a name="Parameterseducation.classes.assignmentsDeleteRubric">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.classes.assignmentsDeleteSubmissions">Command `az education education-class-assignment delete-submission`</a>

##### <a name="Parameterseducation.classes.assignmentsDeleteSubmissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.classes.assignmentsListCategories">Command `az education education-class-assignment list-category`</a>

##### <a name="Parameterseducation.classes.assignmentsListCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classes.assignmentsListResources">Command `az education education-class-assignment list-resource`</a>

##### <a name="Parameterseducation.classes.assignmentsListResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classes.assignmentsListSubmissions">Command `az education education-class-assignment list-submission`</a>

##### <a name="Parameterseducation.classes.assignmentsListSubmissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classes.assignmentspublish">Command `az education education-class-assignment publish`</a>

##### <a name="Parameterseducation.classes.assignmentspublish">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|

#### <a name="education.classes.assignmentsGetCategories">Command `az education education-class-assignment show-category`</a>

##### <a name="Parameterseducation.classes.assignmentsGetCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classes.assignmentsGetResources">Command `az education education-class-assignment show-resource`</a>

##### <a name="Parameterseducation.classes.assignmentsGetResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classes.assignmentsgetResourcesFolderUrl">Command `az education education-class-assignment show-resource-folder-url`</a>

##### <a name="Parameterseducation.classes.assignmentsgetResourcesFolderUrl">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|

#### <a name="education.classes.assignmentsGetRubric">Command `az education education-class-assignment show-rubric`</a>

##### <a name="Parameterseducation.classes.assignmentsGetRubric">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classes.assignmentsGetSubmissions">Command `az education education-class-assignment show-submission`</a>

##### <a name="Parameterseducation.classes.assignmentsGetSubmissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classes.assignmentsUpdateCategories">Command `az education education-class-assignment update-category`</a>

##### <a name="Parameterseducation.classes.assignmentsUpdateCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

#### <a name="education.classes.assignmentsUpdateResources">Command `az education education-class-assignment update-resource`</a>

##### <a name="Parameterseducation.classes.assignmentsUpdateResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--id**|string|Read-only.|id|id|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

#### <a name="education.classes.assignmentsUpdateRubric">Command `az education education-class-assignment update-rubric`</a>

##### <a name="Parameterseducation.classes.assignmentsUpdateRubric">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--description**|object|educationItemBody|description|description|
|**--display-name**|string||display_name|displayName|
|**--grading**|dictionary|educationAssignmentGradeType|grading|grading|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--levels**|array||levels|levels|
|**--qualities**|array||qualities|qualities|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="education.classes.assignmentsUpdateSubmissions">Command `az education education-class-assignment update-submission`</a>

##### <a name="Parameterseducation.classes.assignmentsUpdateSubmissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
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
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|

### group `az education education-class-assignment-submission`
#### <a name="education.classes.assignments.submissionsCreateOutcomes">Command `az education education-class-assignment-submission create-outcome`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsCreateOutcomes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="education.classes.assignments.submissionsCreateResources">Command `az education education-class-assignment-submission create-resource`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsCreateResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

#### <a name="education.classes.assignments.submissionsCreateSubmittedResources">Command `az education education-class-assignment-submission create-submitted-resource`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsCreateSubmittedResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

#### <a name="education.classes.assignments.submissionsDeleteOutcomes">Command `az education education-class-assignment-submission delete-outcome`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsDeleteOutcomes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.classes.assignments.submissionsDeleteResources">Command `az education education-class-assignment-submission delete-resource`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsDeleteResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.classes.assignments.submissionsDeleteSubmittedResources">Command `az education education-class-assignment-submission delete-submitted-resource`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsDeleteSubmittedResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.classes.assignments.submissionsListOutcomes">Command `az education education-class-assignment-submission list-outcome`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsListOutcomes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classes.assignments.submissionsListResources">Command `az education education-class-assignment-submission list-resource`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsListResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classes.assignments.submissionsListSubmittedResources">Command `az education education-class-assignment-submission list-submitted-resource`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsListSubmittedResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classes.assignments.submissionsreturn">Command `az education education-class-assignment-submission return`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsreturn">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

#### <a name="education.classes.assignments.submissionsGetOutcomes">Command `az education education-class-assignment-submission show-outcome`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsGetOutcomes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classes.assignments.submissionsGetResources">Command `az education education-class-assignment-submission show-resource`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsGetResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classes.assignments.submissionsGetSubmittedResources">Command `az education education-class-assignment-submission show-submitted-resource`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsGetSubmittedResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classes.assignments.submissionssubmit">Command `az education education-class-assignment-submission submit`</a>

##### <a name="Parameterseducation.classes.assignments.submissionssubmit">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

#### <a name="education.classes.assignments.submissionsunsubmit">Command `az education education-class-assignment-submission unsubmit`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsunsubmit">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

#### <a name="education.classes.assignments.submissionsUpdateOutcomes">Command `az education education-class-assignment-submission update-outcome`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsUpdateOutcomes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="education.classes.assignments.submissionsUpdateResources">Command `az education education-class-assignment-submission update-resource`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsUpdateResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

#### <a name="education.classes.assignments.submissionsUpdateSubmittedResources">Command `az education education-class-assignment-submission update-submitted-resource`</a>

##### <a name="Parameterseducation.classes.assignments.submissionsUpdateSubmittedResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### group `az education education-class-member`
#### <a name="education.classes.membersdelta">Command `az education education-class-member delta`</a>

##### <a name="Parameterseducation.classes.membersdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|

### group `az education education-class-school`
#### <a name="education.classes.schoolsdelta">Command `az education education-class-school delta`</a>

##### <a name="Parameterseducation.classes.schoolsdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|

### group `az education education-class-teacher`
#### <a name="education.classes.teachersdelta">Command `az education education-class-teacher delta`</a>

##### <a name="Parameterseducation.classes.teachersdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|

### group `az education education-me`
#### <a name="education.meCreateAssignments">Command `az education education-me create-assignment`</a>

##### <a name="Parameterseducation.meCreateAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-education-rubric-created-date-time-created-date-time**|date-time||microsoft_graph_education_rubric_created_date_time_created_date_time|createdDateTime|
|**--description**|object|educationItemBody|description|description|
|**--microsoft-graph-education-rubric-display-name**|string||microsoft_graph_education_rubric_display_name|displayName|
|**--microsoft-graph-education-assignment-grade-type-grading**|dictionary|educationAssignmentGradeType|microsoft_graph_education_assignment_grade_type_grading|grading|
|**--microsoft-graph-education-rubric-last-modified-date-time-last-modified-date-time**|date-time||microsoft_graph_education_rubric_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--levels**|array||levels|levels|
|**--qualities**|array||qualities|qualities|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|

#### <a name="education.meCreateRefClasses">Command `az education education-me create-ref-class`</a>

##### <a name="Parameterseducation.meCreateRefClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.meCreateRefSchools">Command `az education education-me create-ref-school`</a>

##### <a name="Parameterseducation.meCreateRefSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.meCreateRefTaughtClasses">Command `az education education-me create-ref-taught-class`</a>

##### <a name="Parameterseducation.meCreateRefTaughtClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.meCreateRubrics">Command `az education education-me create-rubric`</a>

##### <a name="Parameterseducation.meCreateRubrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--description**|object|educationItemBody|description|description|
|**--display-name**|string||display_name|displayName|
|**--grading**|dictionary|educationAssignmentGradeType|grading|grading|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--levels**|array||levels|levels|
|**--qualities**|array||qualities|qualities|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="education.meDeleteAssignments">Command `az education education-me delete-assignment`</a>

##### <a name="Parameterseducation.meDeleteAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.meDeleteRefUser">Command `az education education-me delete-ref-user`</a>

##### <a name="Parameterseducation.meDeleteRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.meDeleteRubrics">Command `az education education-me delete-rubric`</a>

##### <a name="Parameterseducation.meDeleteRubrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-rubric-id**|string|key: id of educationRubric|education_rubric_id|educationRubric-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.meListAssignments">Command `az education education-me list-assignment`</a>

##### <a name="Parameterseducation.meListAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.meListClasses">Command `az education education-me list-class`</a>

##### <a name="Parameterseducation.meListClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.meListRefClasses">Command `az education education-me list-ref-class`</a>

##### <a name="Parameterseducation.meListRefClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.meListRefSchools">Command `az education education-me list-ref-school`</a>

##### <a name="Parameterseducation.meListRefSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.meListRefTaughtClasses">Command `az education education-me list-ref-taught-class`</a>

##### <a name="Parameterseducation.meListRefTaughtClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.meListRubrics">Command `az education education-me list-rubric`</a>

##### <a name="Parameterseducation.meListRubrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.meListSchools">Command `az education education-me list-school`</a>

##### <a name="Parameterseducation.meListSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.meListTaughtClasses">Command `az education education-me list-taught-class`</a>

##### <a name="Parameterseducation.meListTaughtClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.meSetRefUser">Command `az education education-me set-ref-user`</a>

##### <a name="Parameterseducation.meSetRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="education.meGetAssignments">Command `az education education-me show-assignment`</a>

##### <a name="Parameterseducation.meGetAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.meGetRefUser">Command `az education education-me show-ref-user`</a>

##### <a name="Parameterseducation.meGetRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="education.meGetRubrics">Command `az education education-me show-rubric`</a>

##### <a name="Parameterseducation.meGetRubrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-rubric-id**|string|key: id of educationRubric|education_rubric_id|educationRubric-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.meGetUser">Command `az education education-me show-user`</a>

##### <a name="Parameterseducation.meGetUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.meUpdateAssignments">Command `az education education-me update-assignment`</a>

##### <a name="Parameterseducation.meUpdateAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-education-rubric-created-date-time-created-date-time**|date-time||microsoft_graph_education_rubric_created_date_time_created_date_time|createdDateTime|
|**--description**|object|educationItemBody|description|description|
|**--microsoft-graph-education-rubric-display-name**|string||microsoft_graph_education_rubric_display_name|displayName|
|**--microsoft-graph-education-assignment-grade-type-grading**|dictionary|educationAssignmentGradeType|microsoft_graph_education_assignment_grade_type_grading|grading|
|**--microsoft-graph-education-rubric-last-modified-date-time-last-modified-date-time**|date-time||microsoft_graph_education_rubric_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--levels**|array||levels|levels|
|**--qualities**|array||qualities|qualities|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|

#### <a name="education.meUpdateRubrics">Command `az education education-me update-rubric`</a>

##### <a name="Parameterseducation.meUpdateRubrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-rubric-id**|string|key: id of educationRubric|education_rubric_id|educationRubric-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--description**|object|educationItemBody|description|description|
|**--display-name**|string||display_name|displayName|
|**--grading**|dictionary|educationAssignmentGradeType|grading|grading|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--levels**|array||levels|levels|
|**--qualities**|array||qualities|qualities|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

### group `az education education-me-assignment`
#### <a name="education.me.assignmentsCreateCategories">Command `az education education-me-assignment create-category`</a>

##### <a name="Parameterseducation.me.assignmentsCreateCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

#### <a name="education.me.assignmentsCreateResources">Command `az education education-me-assignment create-resource`</a>

##### <a name="Parameterseducation.me.assignmentsCreateResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

#### <a name="education.me.assignmentsCreateSubmissions">Command `az education education-me-assignment create-submission`</a>

##### <a name="Parameterseducation.me.assignmentsCreateSubmissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
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
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|

#### <a name="education.me.assignmentsDeleteCategories">Command `az education education-me-assignment delete-category`</a>

##### <a name="Parameterseducation.me.assignmentsDeleteCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.me.assignmentsDeleteResources">Command `az education education-me-assignment delete-resource`</a>

##### <a name="Parameterseducation.me.assignmentsDeleteResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.me.assignmentsDeleteRubric">Command `az education education-me-assignment delete-rubric`</a>

##### <a name="Parameterseducation.me.assignmentsDeleteRubric">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.me.assignmentsDeleteSubmissions">Command `az education education-me-assignment delete-submission`</a>

##### <a name="Parameterseducation.me.assignmentsDeleteSubmissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.me.assignmentsListCategories">Command `az education education-me-assignment list-category`</a>

##### <a name="Parameterseducation.me.assignmentsListCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.me.assignmentsListResources">Command `az education education-me-assignment list-resource`</a>

##### <a name="Parameterseducation.me.assignmentsListResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.me.assignmentsListSubmissions">Command `az education education-me-assignment list-submission`</a>

##### <a name="Parameterseducation.me.assignmentsListSubmissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.me.assignmentspublish">Command `az education education-me-assignment publish`</a>

##### <a name="Parameterseducation.me.assignmentspublish">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|

#### <a name="education.me.assignmentsGetCategories">Command `az education education-me-assignment show-category`</a>

##### <a name="Parameterseducation.me.assignmentsGetCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.me.assignmentsGetResources">Command `az education education-me-assignment show-resource`</a>

##### <a name="Parameterseducation.me.assignmentsGetResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.me.assignmentsgetResourcesFolderUrl">Command `az education education-me-assignment show-resource-folder-url`</a>

##### <a name="Parameterseducation.me.assignmentsgetResourcesFolderUrl">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|

#### <a name="education.me.assignmentsGetRubric">Command `az education education-me-assignment show-rubric`</a>

##### <a name="Parameterseducation.me.assignmentsGetRubric">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.me.assignmentsGetSubmissions">Command `az education education-me-assignment show-submission`</a>

##### <a name="Parameterseducation.me.assignmentsGetSubmissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.me.assignmentsUpdateCategories">Command `az education education-me-assignment update-category`</a>

##### <a name="Parameterseducation.me.assignmentsUpdateCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

#### <a name="education.me.assignmentsUpdateResources">Command `az education education-me-assignment update-resource`</a>

##### <a name="Parameterseducation.me.assignmentsUpdateResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--id**|string|Read-only.|id|id|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

#### <a name="education.me.assignmentsUpdateRubric">Command `az education education-me-assignment update-rubric`</a>

##### <a name="Parameterseducation.me.assignmentsUpdateRubric">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--description**|object|educationItemBody|description|description|
|**--display-name**|string||display_name|displayName|
|**--grading**|dictionary|educationAssignmentGradeType|grading|grading|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--levels**|array||levels|levels|
|**--qualities**|array||qualities|qualities|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="education.me.assignmentsUpdateSubmissions">Command `az education education-me-assignment update-submission`</a>

##### <a name="Parameterseducation.me.assignmentsUpdateSubmissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
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
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|

### group `az education education-me-assignment-submission`
#### <a name="education.me.assignments.submissionsCreateOutcomes">Command `az education education-me-assignment-submission create-outcome`</a>

##### <a name="Parameterseducation.me.assignments.submissionsCreateOutcomes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="education.me.assignments.submissionsCreateResources">Command `az education education-me-assignment-submission create-resource`</a>

##### <a name="Parameterseducation.me.assignments.submissionsCreateResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

#### <a name="education.me.assignments.submissionsCreateSubmittedResources">Command `az education education-me-assignment-submission create-submitted-resource`</a>

##### <a name="Parameterseducation.me.assignments.submissionsCreateSubmittedResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

#### <a name="education.me.assignments.submissionsDeleteOutcomes">Command `az education education-me-assignment-submission delete-outcome`</a>

##### <a name="Parameterseducation.me.assignments.submissionsDeleteOutcomes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.me.assignments.submissionsDeleteResources">Command `az education education-me-assignment-submission delete-resource`</a>

##### <a name="Parameterseducation.me.assignments.submissionsDeleteResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.me.assignments.submissionsDeleteSubmittedResources">Command `az education education-me-assignment-submission delete-submitted-resource`</a>

##### <a name="Parameterseducation.me.assignments.submissionsDeleteSubmittedResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.me.assignments.submissionsListOutcomes">Command `az education education-me-assignment-submission list-outcome`</a>

##### <a name="Parameterseducation.me.assignments.submissionsListOutcomes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.me.assignments.submissionsListResources">Command `az education education-me-assignment-submission list-resource`</a>

##### <a name="Parameterseducation.me.assignments.submissionsListResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.me.assignments.submissionsListSubmittedResources">Command `az education education-me-assignment-submission list-submitted-resource`</a>

##### <a name="Parameterseducation.me.assignments.submissionsListSubmittedResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.me.assignments.submissionsreturn">Command `az education education-me-assignment-submission return`</a>

##### <a name="Parameterseducation.me.assignments.submissionsreturn">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

#### <a name="education.me.assignments.submissionsGetOutcomes">Command `az education education-me-assignment-submission show-outcome`</a>

##### <a name="Parameterseducation.me.assignments.submissionsGetOutcomes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.me.assignments.submissionsGetResources">Command `az education education-me-assignment-submission show-resource`</a>

##### <a name="Parameterseducation.me.assignments.submissionsGetResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.me.assignments.submissionsGetSubmittedResources">Command `az education education-me-assignment-submission show-submitted-resource`</a>

##### <a name="Parameterseducation.me.assignments.submissionsGetSubmittedResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.me.assignments.submissionssubmit">Command `az education education-me-assignment-submission submit`</a>

##### <a name="Parameterseducation.me.assignments.submissionssubmit">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

#### <a name="education.me.assignments.submissionsunsubmit">Command `az education education-me-assignment-submission unsubmit`</a>

##### <a name="Parameterseducation.me.assignments.submissionsunsubmit">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

#### <a name="education.me.assignments.submissionsUpdateOutcomes">Command `az education education-me-assignment-submission update-outcome`</a>

##### <a name="Parameterseducation.me.assignments.submissionsUpdateOutcomes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="education.me.assignments.submissionsUpdateResources">Command `az education education-me-assignment-submission update-resource`</a>

##### <a name="Parameterseducation.me.assignments.submissionsUpdateResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

#### <a name="education.me.assignments.submissionsUpdateSubmittedResources">Command `az education education-me-assignment-submission update-submitted-resource`</a>

##### <a name="Parameterseducation.me.assignments.submissionsUpdateSubmittedResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### group `az education education-me-class`
#### <a name="education.me.classesdelta">Command `az education education-me-class delta`</a>

##### <a name="Parameterseducation.me.classesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
### group `az education education-me-school`
#### <a name="education.me.schoolsdelta">Command `az education education-me-school delta`</a>

##### <a name="Parameterseducation.me.schoolsdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
### group `az education education-me-taught-class`
#### <a name="education.me.taughtClassesdelta">Command `az education education-me-taught-class delta`</a>

##### <a name="Parameterseducation.me.taughtClassesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
### group `az education education-root`
#### <a name="education.educationRootGetEducationRoot">Command `az education education-root show-education-root`</a>

##### <a name="Parameterseducation.educationRootGetEducationRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.educationRootUpdateEducationRoot">Command `az education education-root update-education-root`</a>

##### <a name="Parameterseducation.educationRootUpdateEducationRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--synchronization-profiles**|array||synchronization_profiles|synchronizationProfiles|
|**--classes**|array|Read-only. Nullable.|classes|classes|
|**--me**|object|educationUser|me|me|
|**--schools**|array|Read-only. Nullable.|schools|schools|
|**--users**|array|Read-only. Nullable.|users|users|

### group `az education education-school`
#### <a name="education.schoolsCreateRefClasses">Command `az education education-school create-ref-class`</a>

##### <a name="Parameterseducation.schoolsCreateRefClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.schoolsCreateRefUsers">Command `az education education-school create-ref-user`</a>

##### <a name="Parameterseducation.schoolsCreateRefUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.schoolsDeleteRefAdministrativeUnit">Command `az education education-school delete-ref-administrative-unit`</a>

##### <a name="Parameterseducation.schoolsDeleteRefAdministrativeUnit">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.schoolsdelta">Command `az education education-school delta`</a>

##### <a name="Parameterseducation.schoolsdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="education.schoolsListClasses">Command `az education education-school list-class`</a>

##### <a name="Parameterseducation.schoolsListClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.schoolsListRefClasses">Command `az education education-school list-ref-class`</a>

##### <a name="Parameterseducation.schoolsListRefClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.schoolsListRefUsers">Command `az education education-school list-ref-user`</a>

##### <a name="Parameterseducation.schoolsListRefUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.schoolsListUsers">Command `az education education-school list-user`</a>

##### <a name="Parameterseducation.schoolsListUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.schoolsSetRefAdministrativeUnit">Command `az education education-school set-ref-administrative-unit`</a>

##### <a name="Parameterseducation.schoolsSetRefAdministrativeUnit">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="education.schoolsGetAdministrativeUnit">Command `az education education-school show-administrative-unit`</a>

##### <a name="Parameterseducation.schoolsGetAdministrativeUnit">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.schoolsGetRefAdministrativeUnit">Command `az education education-school show-ref-administrative-unit`</a>

##### <a name="Parameterseducation.schoolsGetRefAdministrativeUnit">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|

### group `az education education-school-class`
#### <a name="education.schools.classesdelta">Command `az education education-school-class delta`</a>

##### <a name="Parameterseducation.schools.classesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|

### group `az education education-school-user`
#### <a name="education.schools.usersdelta">Command `az education education-school-user delta`</a>

##### <a name="Parameterseducation.schools.usersdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|

### group `az education education-synchronization-profile`
#### <a name="education.synchronizationProfilesCreateErrors">Command `az education education-synchronization-profile create-error`</a>

##### <a name="Parameterseducation.synchronizationProfilesCreateErrors">Parameters</a> 
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

#### <a name="education.synchronizationProfilesDeleteErrors">Command `az education education-synchronization-profile delete-error`</a>

##### <a name="Parameterseducation.synchronizationProfilesDeleteErrors">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--education-synchronization-error-id**|string|key: id of educationSynchronizationError|education_synchronization_error_id|educationSynchronizationError-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.synchronizationProfilesDeleteProfileStatus">Command `az education education-synchronization-profile delete-profile-status`</a>

##### <a name="Parameterseducation.synchronizationProfilesDeleteProfileStatus">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.synchronizationProfilesListErrors">Command `az education education-synchronization-profile list-error`</a>

##### <a name="Parameterseducation.synchronizationProfilesListErrors">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.synchronizationProfilespause">Command `az education education-synchronization-profile pause`</a>

##### <a name="Parameterseducation.synchronizationProfilespause">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

#### <a name="education.synchronizationProfilesreset">Command `az education education-synchronization-profile reset`</a>

##### <a name="Parameterseducation.synchronizationProfilesreset">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

#### <a name="education.synchronizationProfilesresume">Command `az education education-synchronization-profile resume`</a>

##### <a name="Parameterseducation.synchronizationProfilesresume">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

#### <a name="education.synchronizationProfilesGetErrors">Command `az education education-synchronization-profile show-error`</a>

##### <a name="Parameterseducation.synchronizationProfilesGetErrors">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--education-synchronization-error-id**|string|key: id of educationSynchronizationError|education_synchronization_error_id|educationSynchronizationError-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.synchronizationProfilesGetProfileStatus">Command `az education education-synchronization-profile show-profile-status`</a>

##### <a name="Parameterseducation.synchronizationProfilesGetProfileStatus">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.synchronizationProfilesstart">Command `az education education-synchronization-profile start`</a>

##### <a name="Parameterseducation.synchronizationProfilesstart">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

#### <a name="education.synchronizationProfilesUpdateErrors">Command `az education education-synchronization-profile update-error`</a>

##### <a name="Parameterseducation.synchronizationProfilesUpdateErrors">Parameters</a> 
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

#### <a name="education.synchronizationProfilesUpdateProfileStatus">Command `az education education-synchronization-profile update-profile-status`</a>

##### <a name="Parameterseducation.synchronizationProfilesUpdateProfileStatus">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--id**|string|Read-only.|id|id|
|**--last-synchronization-date-time**|date-time||last_synchronization_date_time|lastSynchronizationDateTime|
|**--status**|choice||status|status|

#### <a name="education.synchronizationProfilesuploadUrl">Command `az education education-synchronization-profile upload-url`</a>

##### <a name="Parameterseducation.synchronizationProfilesuploadUrl">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

### group `az education education-user`
#### <a name="education.usersCreateAssignments">Command `az education education-user create-assignment`</a>

##### <a name="Parameterseducation.usersCreateAssignments">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-education-rubric-created-date-time-created-date-time**|date-time||microsoft_graph_education_rubric_created_date_time_created_date_time|createdDateTime|
|**--description**|object|educationItemBody|description|description|
|**--microsoft-graph-education-rubric-display-name**|string||microsoft_graph_education_rubric_display_name|displayName|
|**--microsoft-graph-education-assignment-grade-type-grading**|dictionary|educationAssignmentGradeType|microsoft_graph_education_assignment_grade_type_grading|grading|
|**--microsoft-graph-education-rubric-last-modified-date-time-last-modified-date-time**|date-time||microsoft_graph_education_rubric_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--levels**|array||levels|levels|
|**--qualities**|array||qualities|qualities|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|

#### <a name="education.usersCreateRefClasses">Command `az education education-user create-ref-class`</a>

##### <a name="Parameterseducation.usersCreateRefClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.usersCreateRefSchools">Command `az education education-user create-ref-school`</a>

##### <a name="Parameterseducation.usersCreateRefSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.usersCreateRefTaughtClasses">Command `az education education-user create-ref-taught-class`</a>

##### <a name="Parameterseducation.usersCreateRefTaughtClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.usersCreateRubrics">Command `az education education-user create-rubric`</a>

##### <a name="Parameterseducation.usersCreateRubrics">Parameters</a> 
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
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="education.usersDeleteAssignments">Command `az education education-user delete-assignment`</a>

##### <a name="Parameterseducation.usersDeleteAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.usersDeleteRefUser">Command `az education education-user delete-ref-user`</a>

##### <a name="Parameterseducation.usersDeleteRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.usersDeleteRubrics">Command `az education education-user delete-rubric`</a>

##### <a name="Parameterseducation.usersDeleteRubrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-rubric-id**|string|key: id of educationRubric|education_rubric_id|educationRubric-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.usersdelta">Command `az education education-user delta`</a>

##### <a name="Parameterseducation.usersdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="education.usersListAssignments">Command `az education education-user list-assignment`</a>

##### <a name="Parameterseducation.usersListAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.usersListClasses">Command `az education education-user list-class`</a>

##### <a name="Parameterseducation.usersListClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.usersListRefClasses">Command `az education education-user list-ref-class`</a>

##### <a name="Parameterseducation.usersListRefClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.usersListRefSchools">Command `az education education-user list-ref-school`</a>

##### <a name="Parameterseducation.usersListRefSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.usersListRefTaughtClasses">Command `az education education-user list-ref-taught-class`</a>

##### <a name="Parameterseducation.usersListRefTaughtClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.usersListRubrics">Command `az education education-user list-rubric`</a>

##### <a name="Parameterseducation.usersListRubrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.usersListSchools">Command `az education education-user list-school`</a>

##### <a name="Parameterseducation.usersListSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.usersListTaughtClasses">Command `az education education-user list-taught-class`</a>

##### <a name="Parameterseducation.usersListTaughtClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.usersSetRefUser">Command `az education education-user set-ref-user`</a>

##### <a name="Parameterseducation.usersSetRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="education.usersGetAssignments">Command `az education education-user show-assignment`</a>

##### <a name="Parameterseducation.usersGetAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.usersGetRefUser">Command `az education education-user show-ref-user`</a>

##### <a name="Parameterseducation.usersGetRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|

#### <a name="education.usersGetRubrics">Command `az education education-user show-rubric`</a>

##### <a name="Parameterseducation.usersGetRubrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-rubric-id**|string|key: id of educationRubric|education_rubric_id|educationRubric-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.usersGetUser">Command `az education education-user show-user`</a>

##### <a name="Parameterseducation.usersGetUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.usersUpdateAssignments">Command `az education education-user update-assignment`</a>

##### <a name="Parameterseducation.usersUpdateAssignments">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-education-rubric-created-date-time-created-date-time**|date-time||microsoft_graph_education_rubric_created_date_time_created_date_time|createdDateTime|
|**--description**|object|educationItemBody|description|description|
|**--microsoft-graph-education-rubric-display-name**|string||microsoft_graph_education_rubric_display_name|displayName|
|**--microsoft-graph-education-assignment-grade-type-grading**|dictionary|educationAssignmentGradeType|microsoft_graph_education_assignment_grade_type_grading|grading|
|**--microsoft-graph-education-rubric-last-modified-date-time-last-modified-date-time**|date-time||microsoft_graph_education_rubric_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--levels**|array||levels|levels|
|**--qualities**|array||qualities|qualities|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|

#### <a name="education.usersUpdateRubrics">Command `az education education-user update-rubric`</a>

##### <a name="Parameterseducation.usersUpdateRubrics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-rubric-id**|string|key: id of educationRubric|education_rubric_id|educationRubric-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--description**|object|educationItemBody|description|description|
|**--display-name**|string||display_name|displayName|
|**--grading**|dictionary|educationAssignmentGradeType|grading|grading|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--levels**|array||levels|levels|
|**--qualities**|array||qualities|qualities|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

### group `az education education-user-assignment`
#### <a name="education.users.assignmentsCreateCategories">Command `az education education-user-assignment create-category`</a>

##### <a name="Parameterseducation.users.assignmentsCreateCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

#### <a name="education.users.assignmentsCreateResources">Command `az education education-user-assignment create-resource`</a>

##### <a name="Parameterseducation.users.assignmentsCreateResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

#### <a name="education.users.assignmentsCreateSubmissions">Command `az education education-user-assignment create-submission`</a>

##### <a name="Parameterseducation.users.assignmentsCreateSubmissions">Parameters</a> 
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
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|

#### <a name="education.users.assignmentsDeleteCategories">Command `az education education-user-assignment delete-category`</a>

##### <a name="Parameterseducation.users.assignmentsDeleteCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.users.assignmentsDeleteResources">Command `az education education-user-assignment delete-resource`</a>

##### <a name="Parameterseducation.users.assignmentsDeleteResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.users.assignmentsDeleteRubric">Command `az education education-user-assignment delete-rubric`</a>

##### <a name="Parameterseducation.users.assignmentsDeleteRubric">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.users.assignmentsDeleteSubmissions">Command `az education education-user-assignment delete-submission`</a>

##### <a name="Parameterseducation.users.assignmentsDeleteSubmissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.users.assignmentsListCategories">Command `az education education-user-assignment list-category`</a>

##### <a name="Parameterseducation.users.assignmentsListCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.users.assignmentsListResources">Command `az education education-user-assignment list-resource`</a>

##### <a name="Parameterseducation.users.assignmentsListResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.users.assignmentsListSubmissions">Command `az education education-user-assignment list-submission`</a>

##### <a name="Parameterseducation.users.assignmentsListSubmissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.users.assignmentspublish">Command `az education education-user-assignment publish`</a>

##### <a name="Parameterseducation.users.assignmentspublish">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|

#### <a name="education.users.assignmentsGetCategories">Command `az education education-user-assignment show-category`</a>

##### <a name="Parameterseducation.users.assignmentsGetCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.users.assignmentsGetResources">Command `az education education-user-assignment show-resource`</a>

##### <a name="Parameterseducation.users.assignmentsGetResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.users.assignmentsgetResourcesFolderUrl">Command `az education education-user-assignment show-resource-folder-url`</a>

##### <a name="Parameterseducation.users.assignmentsgetResourcesFolderUrl">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|

#### <a name="education.users.assignmentsGetRubric">Command `az education education-user-assignment show-rubric`</a>

##### <a name="Parameterseducation.users.assignmentsGetRubric">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.users.assignmentsGetSubmissions">Command `az education education-user-assignment show-submission`</a>

##### <a name="Parameterseducation.users.assignmentsGetSubmissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.users.assignmentsUpdateCategories">Command `az education education-user-assignment update-category`</a>

##### <a name="Parameterseducation.users.assignmentsUpdateCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

#### <a name="education.users.assignmentsUpdateResources">Command `az education education-user-assignment update-resource`</a>

##### <a name="Parameterseducation.users.assignmentsUpdateResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--id**|string|Read-only.|id|id|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

#### <a name="education.users.assignmentsUpdateRubric">Command `az education education-user-assignment update-rubric`</a>

##### <a name="Parameterseducation.users.assignmentsUpdateRubric">Parameters</a> 
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
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

#### <a name="education.users.assignmentsUpdateSubmissions">Command `az education education-user-assignment update-submission`</a>

##### <a name="Parameterseducation.users.assignmentsUpdateSubmissions">Parameters</a> 
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
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|

### group `az education education-user-assignment-submission`
#### <a name="education.users.assignments.submissionsCreateOutcomes">Command `az education education-user-assignment-submission create-outcome`</a>

##### <a name="Parameterseducation.users.assignments.submissionsCreateOutcomes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="education.users.assignments.submissionsCreateResources">Command `az education education-user-assignment-submission create-resource`</a>

##### <a name="Parameterseducation.users.assignments.submissionsCreateResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

#### <a name="education.users.assignments.submissionsCreateSubmittedResources">Command `az education education-user-assignment-submission create-submitted-resource`</a>

##### <a name="Parameterseducation.users.assignments.submissionsCreateSubmittedResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

#### <a name="education.users.assignments.submissionsDeleteOutcomes">Command `az education education-user-assignment-submission delete-outcome`</a>

##### <a name="Parameterseducation.users.assignments.submissionsDeleteOutcomes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.users.assignments.submissionsDeleteResources">Command `az education education-user-assignment-submission delete-resource`</a>

##### <a name="Parameterseducation.users.assignments.submissionsDeleteResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.users.assignments.submissionsDeleteSubmittedResources">Command `az education education-user-assignment-submission delete-submitted-resource`</a>

##### <a name="Parameterseducation.users.assignments.submissionsDeleteSubmittedResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.users.assignments.submissionsListOutcomes">Command `az education education-user-assignment-submission list-outcome`</a>

##### <a name="Parameterseducation.users.assignments.submissionsListOutcomes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.users.assignments.submissionsListResources">Command `az education education-user-assignment-submission list-resource`</a>

##### <a name="Parameterseducation.users.assignments.submissionsListResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.users.assignments.submissionsListSubmittedResources">Command `az education education-user-assignment-submission list-submitted-resource`</a>

##### <a name="Parameterseducation.users.assignments.submissionsListSubmittedResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.users.assignments.submissionsreturn">Command `az education education-user-assignment-submission return`</a>

##### <a name="Parameterseducation.users.assignments.submissionsreturn">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

#### <a name="education.users.assignments.submissionsGetOutcomes">Command `az education education-user-assignment-submission show-outcome`</a>

##### <a name="Parameterseducation.users.assignments.submissionsGetOutcomes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.users.assignments.submissionsGetResources">Command `az education education-user-assignment-submission show-resource`</a>

##### <a name="Parameterseducation.users.assignments.submissionsGetResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.users.assignments.submissionsGetSubmittedResources">Command `az education education-user-assignment-submission show-submitted-resource`</a>

##### <a name="Parameterseducation.users.assignments.submissionsGetSubmittedResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.users.assignments.submissionssubmit">Command `az education education-user-assignment-submission submit`</a>

##### <a name="Parameterseducation.users.assignments.submissionssubmit">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

#### <a name="education.users.assignments.submissionsunsubmit">Command `az education education-user-assignment-submission unsubmit`</a>

##### <a name="Parameterseducation.users.assignments.submissionsunsubmit">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

#### <a name="education.users.assignments.submissionsUpdateOutcomes">Command `az education education-user-assignment-submission update-outcome`</a>

##### <a name="Parameterseducation.users.assignments.submissionsUpdateOutcomes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="education.users.assignments.submissionsUpdateResources">Command `az education education-user-assignment-submission update-resource`</a>

##### <a name="Parameterseducation.users.assignments.submissionsUpdateResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

#### <a name="education.users.assignments.submissionsUpdateSubmittedResources">Command `az education education-user-assignment-submission update-submitted-resource`</a>

##### <a name="Parameterseducation.users.assignments.submissionsUpdateSubmittedResources">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--created-by**|object|identitySet|created_by|createdBy|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--display-name**|string||display_name|displayName|
|**--last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### group `az education education-user-class`
#### <a name="education.users.classesdelta">Command `az education education-user-class delta`</a>

##### <a name="Parameterseducation.users.classesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|

### group `az education education-user-school`
#### <a name="education.users.schoolsdelta">Command `az education education-user-school delta`</a>

##### <a name="Parameterseducation.users.schoolsdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|

### group `az education education-user-taught-class`
#### <a name="education.users.taughtClassesdelta">Command `az education education-user-taught-class delta`</a>

##### <a name="Parameterseducation.users.taughtClassesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
