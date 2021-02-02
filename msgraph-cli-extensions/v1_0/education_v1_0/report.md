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
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|

### education education delete

delete a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteClasses|
|delete|DeleteSchools|
|delete|DeleteUsers|
|delete|DeleteMe|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
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
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
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

### education education update-class

update-class a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

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

### education education update-me

update-me a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-me|UpdateMe|

#### Parameters
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
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|

### education education update-school

update-school a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

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

### education education update-user

update-user a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-user|UpdateUsers|

#### Parameters
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
|**--created-by-application**|object|identity|application|application|
|**--created-by-device**|object|identity|device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|

### education education-class create-ref-member

create-ref-member a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-member|CreateRefMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### education education-class create-ref-school

create-ref-school a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-school|CreateRefSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### education education-class create-ref-teacher

create-ref-teacher a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-teacher|CreateRefTeachers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### education education-class delete

delete a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRefGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class get-ref-group

get-ref-group a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-group|GetRefGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class list-ref-member

list-ref-member a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-member|ListRefMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### education education-class list-ref-school

list-ref-school a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-school|ListRefSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### education education-class list-ref-teacher

list-ref-teacher a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-teacher|ListRefTeachers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-class set-ref-group

set-ref-group a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-group|SetRefGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### education education-education-root get-education-root

get-education-root a education education-education-root.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-education-root|education.educationRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-education-root|GetEducationRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-education-root update-education-root

update-education-root a education education-education-root.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-education-root|education.educationRoot|

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

### education education-me create-ref-class

create-ref-class a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-class|CreateRefClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|dictionary|New navigation property ref value|body|body|

### education education-me create-ref-school

create-ref-school a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-school|CreateRefSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|dictionary|New navigation property ref value|body|body|

### education education-me delete

delete a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRefUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

### education education-me get-ref-user

get-ref-user a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-user|GetRefUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

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

### education education-me list-ref-class

list-ref-class a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-class|ListRefClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### education education-me list-ref-school

list-ref-school a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-school|ListRefSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|

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

### education education-me set-ref-user

set-ref-user a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-user|SetRefUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|dictionary|New navigation property ref values|body|body|

### education education-school create-ref-class

create-ref-class a education education-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-school|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-class|CreateRefClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### education education-school create-ref-user

create-ref-user a education education-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-school|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-user|CreateRefUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--body**|dictionary|New navigation property ref value|body|body|

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
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-school list-ref-class

list-ref-class a education education-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-school|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-class|ListRefClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### education education-school list-ref-user

list-ref-user a education education-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-school|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-user|ListRefUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

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
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user create-ref-class

create-ref-class a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-class|CreateRefClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### education education-user create-ref-school

create-ref-school a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-school|CreateRefSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### education education-user delete

delete a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRefUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--if-match**|string|ETag|if_match|If-Match|

### education education-user get-ref-user

get-ref-user a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-user|GetRefUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|

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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user list-ref-class

list-ref-class a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-class|ListRefClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### education education-user list-ref-school

list-ref-school a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-school|ListRefSchools|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-user set-ref-user

set-ref-user a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-user|SetRefUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|dictionary|New navigation property ref values|body|body|
