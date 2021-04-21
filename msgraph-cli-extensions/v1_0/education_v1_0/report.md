# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az education_v1_0|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az education_v1_0` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az education educationroot|education.educationRoot|[commands](#CommandsIneducation.educationRoot)|
|az education education|education|[commands](#CommandsIneducation)|
|az education educationclass|education.classes|[commands](#CommandsIneducation.classes)|
|az education educationme|education.me|[commands](#CommandsIneducation.me)|
|az education educationschool|education.schools|[commands](#CommandsIneducation.schools)|
|az education educationuser|education.users|[commands](#CommandsIneducation.users)|

## COMMANDS
### <a name="CommandsIneducation">Commands in `az education education` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education create-class](#educationCreateClasses)|CreateClasses|[Parameters](#ParameterseducationCreateClasses)|Not Found|
|[az education education create-school](#educationCreateSchools)|CreateSchools|[Parameters](#ParameterseducationCreateSchools)|Not Found|
|[az education education create-user](#educationCreateUsers)|CreateUsers|[Parameters](#ParameterseducationCreateUsers)|Not Found|
|[az education education delete-class](#educationDeleteClasses)|DeleteClasses|[Parameters](#ParameterseducationDeleteClasses)|Not Found|
|[az education education delete-me](#educationDeleteMe)|DeleteMe|[Parameters](#ParameterseducationDeleteMe)|Not Found|
|[az education education delete-school](#educationDeleteSchools)|DeleteSchools|[Parameters](#ParameterseducationDeleteSchools)|Not Found|
|[az education education delete-user](#educationDeleteUsers)|DeleteUsers|[Parameters](#ParameterseducationDeleteUsers)|Not Found|
|[az education education list-class](#educationListClasses)|ListClasses|[Parameters](#ParameterseducationListClasses)|Not Found|
|[az education education list-school](#educationListSchools)|ListSchools|[Parameters](#ParameterseducationListSchools)|Not Found|
|[az education education list-user](#educationListUsers)|ListUsers|[Parameters](#ParameterseducationListUsers)|Not Found|
|[az education education show-class](#educationGetClasses)|GetClasses|[Parameters](#ParameterseducationGetClasses)|Not Found|
|[az education education show-me](#educationGetMe)|GetMe|[Parameters](#ParameterseducationGetMe)|Not Found|
|[az education education show-school](#educationGetSchools)|GetSchools|[Parameters](#ParameterseducationGetSchools)|Not Found|
|[az education education show-user](#educationGetUsers)|GetUsers|[Parameters](#ParameterseducationGetUsers)|Not Found|
|[az education education update-class](#educationUpdateClasses)|UpdateClasses|[Parameters](#ParameterseducationUpdateClasses)|Not Found|
|[az education education update-me](#educationUpdateMe)|UpdateMe|[Parameters](#ParameterseducationUpdateMe)|Not Found|
|[az education education update-school](#educationUpdateSchools)|UpdateSchools|[Parameters](#ParameterseducationUpdateSchools)|Not Found|
|[az education education update-user](#educationUpdateUsers)|UpdateUsers|[Parameters](#ParameterseducationUpdateUsers)|Not Found|

### <a name="CommandsIneducation.classes">Commands in `az education educationclass` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education educationclass create-ref-member](#education.classesCreateRefMembers)|CreateRefMembers|[Parameters](#Parameterseducation.classesCreateRefMembers)|Not Found|
|[az education educationclass create-ref-school](#education.classesCreateRefSchools)|CreateRefSchools|[Parameters](#Parameterseducation.classesCreateRefSchools)|Not Found|
|[az education educationclass create-ref-teacher](#education.classesCreateRefTeachers)|CreateRefTeachers|[Parameters](#Parameterseducation.classesCreateRefTeachers)|Not Found|
|[az education educationclass delete-ref-group](#education.classesDeleteRefGroup)|DeleteRefGroup|[Parameters](#Parameterseducation.classesDeleteRefGroup)|Not Found|
|[az education educationclass list-member](#education.classesListMembers)|ListMembers|[Parameters](#Parameterseducation.classesListMembers)|Not Found|
|[az education educationclass list-ref-member](#education.classesListRefMembers)|ListRefMembers|[Parameters](#Parameterseducation.classesListRefMembers)|Not Found|
|[az education educationclass list-ref-school](#education.classesListRefSchools)|ListRefSchools|[Parameters](#Parameterseducation.classesListRefSchools)|Not Found|
|[az education educationclass list-ref-teacher](#education.classesListRefTeachers)|ListRefTeachers|[Parameters](#Parameterseducation.classesListRefTeachers)|Not Found|
|[az education educationclass list-school](#education.classesListSchools)|ListSchools|[Parameters](#Parameterseducation.classesListSchools)|Not Found|
|[az education educationclass list-teacher](#education.classesListTeachers)|ListTeachers|[Parameters](#Parameterseducation.classesListTeachers)|Not Found|
|[az education educationclass set-ref-group](#education.classesSetRefGroup)|SetRefGroup|[Parameters](#Parameterseducation.classesSetRefGroup)|Not Found|
|[az education educationclass show-group](#education.classesGetGroup)|GetGroup|[Parameters](#Parameterseducation.classesGetGroup)|Not Found|
|[az education educationclass show-ref-group](#education.classesGetRefGroup)|GetRefGroup|[Parameters](#Parameterseducation.classesGetRefGroup)|Not Found|

### <a name="CommandsIneducation.me">Commands in `az education educationme` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education educationme create-ref-class](#education.meCreateRefClasses)|CreateRefClasses|[Parameters](#Parameterseducation.meCreateRefClasses)|Not Found|
|[az education educationme create-ref-school](#education.meCreateRefSchools)|CreateRefSchools|[Parameters](#Parameterseducation.meCreateRefSchools)|Not Found|
|[az education educationme delete-ref-user](#education.meDeleteRefUser)|DeleteRefUser|[Parameters](#Parameterseducation.meDeleteRefUser)|Not Found|
|[az education educationme list-class](#education.meListClasses)|ListClasses|[Parameters](#Parameterseducation.meListClasses)|Not Found|
|[az education educationme list-ref-class](#education.meListRefClasses)|ListRefClasses|[Parameters](#Parameterseducation.meListRefClasses)|Not Found|
|[az education educationme list-ref-school](#education.meListRefSchools)|ListRefSchools|[Parameters](#Parameterseducation.meListRefSchools)|Not Found|
|[az education educationme list-school](#education.meListSchools)|ListSchools|[Parameters](#Parameterseducation.meListSchools)|Not Found|
|[az education educationme set-ref-user](#education.meSetRefUser)|SetRefUser|[Parameters](#Parameterseducation.meSetRefUser)|Not Found|
|[az education educationme show-ref-user](#education.meGetRefUser)|GetRefUser|[Parameters](#Parameterseducation.meGetRefUser)|Not Found|
|[az education educationme show-user](#education.meGetUser)|GetUser|[Parameters](#Parameterseducation.meGetUser)|Not Found|

### <a name="CommandsIneducation.educationRoot">Commands in `az education educationroot` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education educationroot show-education-root](#education.educationRootGetEducationRoot)|GetEducationRoot|[Parameters](#Parameterseducation.educationRootGetEducationRoot)|Not Found|
|[az education educationroot update-education-root](#education.educationRootUpdateEducationRoot)|UpdateEducationRoot|[Parameters](#Parameterseducation.educationRootUpdateEducationRoot)|Not Found|

### <a name="CommandsIneducation.schools">Commands in `az education educationschool` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education educationschool create-ref-class](#education.schoolsCreateRefClasses)|CreateRefClasses|[Parameters](#Parameterseducation.schoolsCreateRefClasses)|Not Found|
|[az education educationschool create-ref-user](#education.schoolsCreateRefUsers)|CreateRefUsers|[Parameters](#Parameterseducation.schoolsCreateRefUsers)|Not Found|
|[az education educationschool list-class](#education.schoolsListClasses)|ListClasses|[Parameters](#Parameterseducation.schoolsListClasses)|Not Found|
|[az education educationschool list-ref-class](#education.schoolsListRefClasses)|ListRefClasses|[Parameters](#Parameterseducation.schoolsListRefClasses)|Not Found|
|[az education educationschool list-ref-user](#education.schoolsListRefUsers)|ListRefUsers|[Parameters](#Parameterseducation.schoolsListRefUsers)|Not Found|
|[az education educationschool list-user](#education.schoolsListUsers)|ListUsers|[Parameters](#Parameterseducation.schoolsListUsers)|Not Found|

### <a name="CommandsIneducation.users">Commands in `az education educationuser` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education educationuser create-ref-class](#education.usersCreateRefClasses)|CreateRefClasses|[Parameters](#Parameterseducation.usersCreateRefClasses)|Not Found|
|[az education educationuser create-ref-school](#education.usersCreateRefSchools)|CreateRefSchools|[Parameters](#Parameterseducation.usersCreateRefSchools)|Not Found|
|[az education educationuser delete-ref-user](#education.usersDeleteRefUser)|DeleteRefUser|[Parameters](#Parameterseducation.usersDeleteRefUser)|Not Found|
|[az education educationuser list-class](#education.usersListClasses)|ListClasses|[Parameters](#Parameterseducation.usersListClasses)|Not Found|
|[az education educationuser list-ref-class](#education.usersListRefClasses)|ListRefClasses|[Parameters](#Parameterseducation.usersListRefClasses)|Not Found|
|[az education educationuser list-ref-school](#education.usersListRefSchools)|ListRefSchools|[Parameters](#Parameterseducation.usersListRefSchools)|Not Found|
|[az education educationuser list-school](#education.usersListSchools)|ListSchools|[Parameters](#Parameterseducation.usersListSchools)|Not Found|
|[az education educationuser set-ref-user](#education.usersSetRefUser)|SetRefUser|[Parameters](#Parameterseducation.usersSetRefUser)|Not Found|
|[az education educationuser show-ref-user](#education.usersGetRefUser)|GetRefUser|[Parameters](#Parameterseducation.usersGetRefUser)|Not Found|
|[az education educationuser show-user](#education.usersGetUser)|GetUser|[Parameters](#Parameterseducation.usersGetUser)|Not Found|


## COMMAND DETAILS

### group `az education education`
#### <a name="educationCreateClasses">Command `az education education create-class`</a>

##### <a name="ParameterseducationCreateClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--class-code**|string|Class code used by the school to identify the class.|class_code|classCode|
|**--description**|string|Description of the class.|description|description|
|**--display-name**|string|Name of the class.|display_name|displayName|
|**--external-id**|string|ID of the class from the syncing system.|external_id|externalId|
|**--external-name**|string|Name of the class in the syncing system.|external_name|externalName|
|**--external-source**|choice||external_source|externalSource|
|**--mail-nickname**|string|Mail name for sending email to all members, if this is enabled.|mail_nickname|mailNickname|
|**--term**|object|educationTerm|term|term|
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
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="educationCreateUsers">Command `az education education create-user`</a>

##### <a name="ParameterseducationCreateUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New navigation property|body|body|

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
|**--description**|string|Description of the class.|description|description|
|**--display-name**|string|Name of the class.|display_name|displayName|
|**--external-id**|string|ID of the class from the syncing system.|external_id|externalId|
|**--external-name**|string|Name of the class in the syncing system.|external_name|externalName|
|**--external-source**|choice||external_source|externalSource|
|**--mail-nickname**|string|Mail name for sending email to all members, if this is enabled.|mail_nickname|mailNickname|
|**--term**|object|educationTerm|term|term|
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
|**--body**|object|New navigation property values|body|body|

#### <a name="educationUpdateSchools">Command `az education education update-school`</a>

##### <a name="ParameterseducationUpdateSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string|Organization description.|description|description|
|**--display-name**|string|Organization display name.|display_name|displayName|
|**--external-source**|choice||external_source|externalSource|
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
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="educationUpdateUsers">Command `az education education update-user`</a>

##### <a name="ParameterseducationUpdateUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|object|New navigation property values|body|body|

### group `az education educationclass`
#### <a name="education.classesCreateRefMembers">Command `az education educationclass create-ref-member`</a>

##### <a name="Parameterseducation.classesCreateRefMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.classesCreateRefSchools">Command `az education educationclass create-ref-school`</a>

##### <a name="Parameterseducation.classesCreateRefSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.classesCreateRefTeachers">Command `az education educationclass create-ref-teacher`</a>

##### <a name="Parameterseducation.classesCreateRefTeachers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.classesDeleteRefGroup">Command `az education educationclass delete-ref-group`</a>

##### <a name="Parameterseducation.classesDeleteRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.classesListMembers">Command `az education educationclass list-member`</a>

##### <a name="Parameterseducation.classesListMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classesListRefMembers">Command `az education educationclass list-ref-member`</a>

##### <a name="Parameterseducation.classesListRefMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.classesListRefSchools">Command `az education educationclass list-ref-school`</a>

##### <a name="Parameterseducation.classesListRefSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.classesListRefTeachers">Command `az education educationclass list-ref-teacher`</a>

##### <a name="Parameterseducation.classesListRefTeachers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.classesListSchools">Command `az education educationclass list-school`</a>

##### <a name="Parameterseducation.classesListSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classesListTeachers">Command `az education educationclass list-teacher`</a>

##### <a name="Parameterseducation.classesListTeachers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classesSetRefGroup">Command `az education educationclass set-ref-group`</a>

##### <a name="Parameterseducation.classesSetRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="education.classesGetGroup">Command `az education educationclass show-group`</a>

##### <a name="Parameterseducation.classesGetGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.classesGetRefGroup">Command `az education educationclass show-ref-group`</a>

##### <a name="Parameterseducation.classesGetRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|

### group `az education educationme`
#### <a name="education.meCreateRefClasses">Command `az education educationme create-ref-class`</a>

##### <a name="Parameterseducation.meCreateRefClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.meCreateRefSchools">Command `az education educationme create-ref-school`</a>

##### <a name="Parameterseducation.meCreateRefSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.meDeleteRefUser">Command `az education educationme delete-ref-user`</a>

##### <a name="Parameterseducation.meDeleteRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.meListClasses">Command `az education educationme list-class`</a>

##### <a name="Parameterseducation.meListClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.meListRefClasses">Command `az education educationme list-ref-class`</a>

##### <a name="Parameterseducation.meListRefClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.meListRefSchools">Command `az education educationme list-ref-school`</a>

##### <a name="Parameterseducation.meListRefSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.meListSchools">Command `az education educationme list-school`</a>

##### <a name="Parameterseducation.meListSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.meSetRefUser">Command `az education educationme set-ref-user`</a>

##### <a name="Parameterseducation.meSetRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="education.meGetRefUser">Command `az education educationme show-ref-user`</a>

##### <a name="Parameterseducation.meGetRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="education.meGetUser">Command `az education educationme show-user`</a>

##### <a name="Parameterseducation.meGetUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### group `az education educationroot`
#### <a name="education.educationRootGetEducationRoot">Command `az education educationroot show-education-root`</a>

##### <a name="Parameterseducation.educationRootGetEducationRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.educationRootUpdateEducationRoot">Command `az education educationroot update-education-root`</a>

##### <a name="Parameterseducation.educationRootUpdateEducationRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--classes**|array|Read-only. Nullable.|classes|classes|
|**--me**|object|educationUser|me|me|
|**--schools**|array|Read-only. Nullable.|schools|schools|
|**--users**|array|Read-only. Nullable.|users|users|

### group `az education educationschool`
#### <a name="education.schoolsCreateRefClasses">Command `az education educationschool create-ref-class`</a>

##### <a name="Parameterseducation.schoolsCreateRefClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.schoolsCreateRefUsers">Command `az education educationschool create-ref-user`</a>

##### <a name="Parameterseducation.schoolsCreateRefUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.schoolsListClasses">Command `az education educationschool list-class`</a>

##### <a name="Parameterseducation.schoolsListClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.schoolsListRefClasses">Command `az education educationschool list-ref-class`</a>

##### <a name="Parameterseducation.schoolsListRefClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.schoolsListRefUsers">Command `az education educationschool list-ref-user`</a>

##### <a name="Parameterseducation.schoolsListRefUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.schoolsListUsers">Command `az education educationschool list-user`</a>

##### <a name="Parameterseducation.schoolsListUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### group `az education educationuser`
#### <a name="education.usersCreateRefClasses">Command `az education educationuser create-ref-class`</a>

##### <a name="Parameterseducation.usersCreateRefClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.usersCreateRefSchools">Command `az education educationuser create-ref-school`</a>

##### <a name="Parameterseducation.usersCreateRefSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="education.usersDeleteRefUser">Command `az education educationuser delete-ref-user`</a>

##### <a name="Parameterseducation.usersDeleteRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="education.usersListClasses">Command `az education educationuser list-class`</a>

##### <a name="Parameterseducation.usersListClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.usersListRefClasses">Command `az education educationuser list-ref-class`</a>

##### <a name="Parameterseducation.usersListRefClasses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.usersListRefSchools">Command `az education educationuser list-ref-school`</a>

##### <a name="Parameterseducation.usersListRefSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="education.usersListSchools">Command `az education educationuser list-school`</a>

##### <a name="Parameterseducation.usersListSchools">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="education.usersSetRefUser">Command `az education educationuser set-ref-user`</a>

##### <a name="Parameterseducation.usersSetRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="education.usersGetRefUser">Command `az education educationuser show-ref-user`</a>

##### <a name="Parameterseducation.usersGetRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|

#### <a name="education.usersGetUser">Command `az education educationuser show-user`</a>

##### <a name="Parameterseducation.usersGetUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|
