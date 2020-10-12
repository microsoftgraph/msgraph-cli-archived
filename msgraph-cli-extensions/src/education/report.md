# Azure CLI Module Creation Report

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
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|

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
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|

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
|education|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRefUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|

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
|**--classes**|array|Read-only. Nullable.|classes|classes|
|**--me**|object|educationUser|me|me|
|**--schools**|array|Read-only. Nullable.|schools|schools|
|**--users**|array|Read-only. Nullable.|users|users|

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
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|user|user|

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
