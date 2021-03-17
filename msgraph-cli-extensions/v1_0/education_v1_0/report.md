# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az education_v1_0|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az education_v1_0` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az education education-root|education.educationRoot|[commands](#CommandsIneducation.educationRoot)|
|az education education|education|[commands](#CommandsIneducation)|
|az education education-class|education.classes|[commands](#CommandsIneducation.classes)|
|az education education-me|education.me|[commands](#CommandsIneducation.me)|
|az education education-school|education.schools|[commands](#CommandsIneducation.schools)|
|az education education-user|education.users|[commands](#CommandsIneducation.users)|

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

### <a name="CommandsIneducation.classes">Commands in `az education education-class` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-class create-ref-member](#education.classesCreateRefMembers)|CreateRefMembers|[Parameters](#Parameterseducation.classesCreateRefMembers)|Not Found|
|[az education education-class create-ref-school](#education.classesCreateRefSchools)|CreateRefSchools|[Parameters](#Parameterseducation.classesCreateRefSchools)|Not Found|
|[az education education-class create-ref-teacher](#education.classesCreateRefTeachers)|CreateRefTeachers|[Parameters](#Parameterseducation.classesCreateRefTeachers)|Not Found|
|[az education education-class delete-ref-group](#education.classesDeleteRefGroup)|DeleteRefGroup|[Parameters](#Parameterseducation.classesDeleteRefGroup)|Not Found|
|[az education education-class list-member](#education.classesListMembers)|ListMembers|[Parameters](#Parameterseducation.classesListMembers)|Not Found|
|[az education education-class list-ref-member](#education.classesListRefMembers)|ListRefMembers|[Parameters](#Parameterseducation.classesListRefMembers)|Not Found|
|[az education education-class list-ref-school](#education.classesListRefSchools)|ListRefSchools|[Parameters](#Parameterseducation.classesListRefSchools)|Not Found|
|[az education education-class list-ref-teacher](#education.classesListRefTeachers)|ListRefTeachers|[Parameters](#Parameterseducation.classesListRefTeachers)|Not Found|
|[az education education-class list-school](#education.classesListSchools)|ListSchools|[Parameters](#Parameterseducation.classesListSchools)|Not Found|
|[az education education-class list-teacher](#education.classesListTeachers)|ListTeachers|[Parameters](#Parameterseducation.classesListTeachers)|Not Found|
|[az education education-class set-ref-group](#education.classesSetRefGroup)|SetRefGroup|[Parameters](#Parameterseducation.classesSetRefGroup)|Not Found|
|[az education education-class show-group](#education.classesGetGroup)|GetGroup|[Parameters](#Parameterseducation.classesGetGroup)|Not Found|
|[az education education-class show-ref-group](#education.classesGetRefGroup)|GetRefGroup|[Parameters](#Parameterseducation.classesGetRefGroup)|Not Found|

### <a name="CommandsIneducation.me">Commands in `az education education-me` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-me create-ref-class](#education.meCreateRefClasses)|CreateRefClasses|[Parameters](#Parameterseducation.meCreateRefClasses)|Not Found|
|[az education education-me create-ref-school](#education.meCreateRefSchools)|CreateRefSchools|[Parameters](#Parameterseducation.meCreateRefSchools)|Not Found|
|[az education education-me delete-ref-user](#education.meDeleteRefUser)|DeleteRefUser|[Parameters](#Parameterseducation.meDeleteRefUser)|Not Found|
|[az education education-me list-class](#education.meListClasses)|ListClasses|[Parameters](#Parameterseducation.meListClasses)|Not Found|
|[az education education-me list-ref-class](#education.meListRefClasses)|ListRefClasses|[Parameters](#Parameterseducation.meListRefClasses)|Not Found|
|[az education education-me list-ref-school](#education.meListRefSchools)|ListRefSchools|[Parameters](#Parameterseducation.meListRefSchools)|Not Found|
|[az education education-me list-school](#education.meListSchools)|ListSchools|[Parameters](#Parameterseducation.meListSchools)|Not Found|
|[az education education-me set-ref-user](#education.meSetRefUser)|SetRefUser|[Parameters](#Parameterseducation.meSetRefUser)|Not Found|
|[az education education-me show-ref-user](#education.meGetRefUser)|GetRefUser|[Parameters](#Parameterseducation.meGetRefUser)|Not Found|
|[az education education-me show-user](#education.meGetUser)|GetUser|[Parameters](#Parameterseducation.meGetUser)|Not Found|

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
|[az education education-school list-class](#education.schoolsListClasses)|ListClasses|[Parameters](#Parameterseducation.schoolsListClasses)|Not Found|
|[az education education-school list-ref-class](#education.schoolsListRefClasses)|ListRefClasses|[Parameters](#Parameterseducation.schoolsListRefClasses)|Not Found|
|[az education education-school list-ref-user](#education.schoolsListRefUsers)|ListRefUsers|[Parameters](#Parameterseducation.schoolsListRefUsers)|Not Found|
|[az education education-school list-user](#education.schoolsListUsers)|ListUsers|[Parameters](#Parameterseducation.schoolsListUsers)|Not Found|

### <a name="CommandsIneducation.users">Commands in `az education education-user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az education education-user create-ref-class](#education.usersCreateRefClasses)|CreateRefClasses|[Parameters](#Parameterseducation.usersCreateRefClasses)|Not Found|
|[az education education-user create-ref-school](#education.usersCreateRefSchools)|CreateRefSchools|[Parameters](#Parameterseducation.usersCreateRefSchools)|Not Found|
|[az education education-user delete-ref-user](#education.usersDeleteRefUser)|DeleteRefUser|[Parameters](#Parameterseducation.usersDeleteRefUser)|Not Found|
|[az education education-user list-class](#education.usersListClasses)|ListClasses|[Parameters](#Parameterseducation.usersListClasses)|Not Found|
|[az education education-user list-ref-class](#education.usersListRefClasses)|ListRefClasses|[Parameters](#Parameterseducation.usersListRefClasses)|Not Found|
|[az education education-user list-ref-school](#education.usersListRefSchools)|ListRefSchools|[Parameters](#Parameterseducation.usersListRefSchools)|Not Found|
|[az education education-user list-school](#education.usersListSchools)|ListSchools|[Parameters](#Parameterseducation.usersListSchools)|Not Found|
|[az education education-user set-ref-user](#education.usersSetRefUser)|SetRefUser|[Parameters](#Parameterseducation.usersSetRefUser)|Not Found|
|[az education education-user show-ref-user](#education.usersGetRefUser)|GetRefUser|[Parameters](#Parameterseducation.usersGetRefUser)|Not Found|
|[az education education-user show-user](#education.usersGetUser)|GetUser|[Parameters](#Parameterseducation.usersGetUser)|Not Found|


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
|**--id**|string|Read-only.|id|id|
|**--account-enabled**|boolean|True if the account is enabled; otherwise, false. This property is required when a user is created. Supports $filter.|account_enabled|accountEnabled|
|**--assigned-licenses**|array|The licenses that are assigned to the user. Not nullable.|assigned_licenses|assignedLicenses|
|**--assigned-plans**|array|The plans that are assigned to the user. Read-only. Not nullable.|assigned_plans|assignedPlans|
|**--business-phones**|array|The telephone numbers for the user. Note: Although this is a string collection, only one number can be set for this property.|business_phones|businessPhones|
|**--department**|string|The name for the department in which the user works. Supports $filter.|department|department|
|**--display-name**|string|The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates. Supports $filter and $orderby.|display_name|displayName|
|**--external-source**|choice||external_source|externalSource|
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
|**--classes**|array|Classes to which the user belongs. Nullable.|classes|classes|
|**--schools**|array|Schools to which the user belongs. Nullable.|schools|schools|
|**--user**|object|Represents an Azure Active Directory user object.|user|user|
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
|**--id**|string|Read-only.|id|id|
|**--account-enabled**|boolean|True if the account is enabled; otherwise, false. This property is required when a user is created. Supports $filter.|account_enabled|accountEnabled|
|**--assigned-licenses**|array|The licenses that are assigned to the user. Not nullable.|assigned_licenses|assignedLicenses|
|**--assigned-plans**|array|The plans that are assigned to the user. Read-only. Not nullable.|assigned_plans|assignedPlans|
|**--business-phones**|array|The telephone numbers for the user. Note: Although this is a string collection, only one number can be set for this property.|business_phones|businessPhones|
|**--department**|string|The name for the department in which the user works. Supports $filter.|department|department|
|**--display-name**|string|The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates. Supports $filter and $orderby.|display_name|displayName|
|**--external-source**|choice||external_source|externalSource|
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
|**--classes**|array|Classes to which the user belongs. Nullable.|classes|classes|
|**--schools**|array|Schools to which the user belongs. Nullable.|schools|schools|
|**--user**|object|Represents an Azure Active Directory user object.|user|user|
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
|**--id**|string|Read-only.|id|id|
|**--account-enabled**|boolean|True if the account is enabled; otherwise, false. This property is required when a user is created. Supports $filter.|account_enabled|accountEnabled|
|**--assigned-licenses**|array|The licenses that are assigned to the user. Not nullable.|assigned_licenses|assignedLicenses|
|**--assigned-plans**|array|The plans that are assigned to the user. Read-only. Not nullable.|assigned_plans|assignedPlans|
|**--business-phones**|array|The telephone numbers for the user. Note: Although this is a string collection, only one number can be set for this property.|business_phones|businessPhones|
|**--department**|string|The name for the department in which the user works. Supports $filter.|department|department|
|**--display-name**|string|The name displayed in the address book for the user. This is usually the combination of the user's first name, middle initial, and last name. This property is required when a user is created and it cannot be cleared during updates. Supports $filter and $orderby.|display_name|displayName|
|**--external-source**|choice||external_source|externalSource|
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
|**--classes**|array|Classes to which the user belongs. Nullable.|classes|classes|
|**--schools**|array|Schools to which the user belongs. Nullable.|schools|schools|
|**--user**|object|Represents an Azure Active Directory user object.|user|user|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|

### group `az education education-class`
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

#### <a name="education.classesDeleteRefGroup">Command `az education education-class delete-ref-group`</a>

##### <a name="Parameterseducation.classesDeleteRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--if-match**|string|ETag|if_match|If-Match|

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

### group `az education education-me`
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

#### <a name="education.meDeleteRefUser">Command `az education education-me delete-ref-user`</a>

##### <a name="Parameterseducation.meDeleteRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

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

#### <a name="education.meListSchools">Command `az education education-me list-school`</a>

##### <a name="Parameterseducation.meListSchools">Parameters</a> 
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

#### <a name="education.meGetRefUser">Command `az education education-me show-ref-user`</a>

##### <a name="Parameterseducation.meGetRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="education.meGetUser">Command `az education education-me show-user`</a>

##### <a name="Parameterseducation.meGetUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

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

### group `az education education-user`
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

#### <a name="education.usersDeleteRefUser">Command `az education education-user delete-ref-user`</a>

##### <a name="Parameterseducation.usersDeleteRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--if-match**|string|ETag|if_match|If-Match|

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

#### <a name="education.usersListSchools">Command `az education education-user list-school`</a>

##### <a name="Parameterseducation.usersListSchools">Parameters</a> 
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

#### <a name="education.usersGetRefUser">Command `az education education-user show-ref-user`</a>

##### <a name="Parameterseducation.usersGetRefUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|

#### <a name="education.usersGetUser">Command `az education education-user show-user`</a>

##### <a name="Parameterseducation.usersGetUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|
