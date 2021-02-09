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
|**--data-provider**|dictionary|educationSynchronizationDataProvider|data_provider|dataProvider|
|**--display-name**|string||display_name|displayName|
|**--expiration-date**|date||expiration_date|expirationDate|
|**--handle-special-character-constraint**|boolean||handle_special_character_constraint|handleSpecialCharacterConstraint|
|**--identity-synchronization-configuration**|dictionary|educationIdentitySynchronizationConfiguration|identity_synchronization_configuration|identitySynchronizationConfiguration|
|**--licenses-to-assign**|array||licenses_to_assign|licensesToAssign|
|**--state**|choice||state|state|
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
|**--on-premises-info-immutable-id**|string||immutable_id|immutableId|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id2|id|

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
|delete|DeleteSynchronizationProfiles|
|delete|DeleteUsers|
|delete|DeleteMe|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
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
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
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
|**--on-premises-info-immutable-id**|string||immutable_id|immutableId|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id2|id|

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

### education education update-synchronization-profile

update-synchronization-profile a education education.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education|education|

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
|**--on-premises-info-immutable-id**|string||immutable_id|immutableId|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id2|id|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

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
|delete|DeleteAssignmentCategories|
|delete|DeleteAssignments|
|delete|DeleteRefGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
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

### education education-class update-assignment

update-assignment a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-assignment|UpdateAssignments|

#### Parameters
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

### education education-class update-assignment-category

update-assignment-category a education education-class.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class|education.classes|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

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

### education education-class-assignment delete

delete a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteCategories|
|delete|DeleteResources|
|delete|DeleteSubmissions|
|delete|DeleteRubric|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|

### education education-class-assignment update-category

update-category a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-category|UpdateCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### education education-class-assignment update-resource

update-resource a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-resource|UpdateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--id**|string|Read-only.|id|id|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### education education-class-assignment update-rubric

update-rubric a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-rubric|UpdateRubric|

#### Parameters
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

### education education-class-assignment update-submission

update-submission a education education-class-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment|education.classes.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-submission|UpdateSubmissions|

#### Parameters
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### education education-class-assignment-submission delete

delete a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteOutcomes|
|delete|DeleteResources|
|delete|DeleteSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

### education education-class-assignment-submission update-outcome

update-outcome a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-outcome|UpdateOutcomes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
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

### education education-class-assignment-submission update-resource

update-resource a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-resource|UpdateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### education education-class-assignment-submission update-submitted-resource

update-submitted-resource a education education-class-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-class-assignment-submission|education.classes.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-submitted-resource|UpdateSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|

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
|**--education-class-id**|string|key: id of educationClass|education_class_id|educationClass-id|

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

### education education-me create-ref-taught-class

create-ref-taught-class a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-taught-class|CreateRefTaughtClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|dictionary|New navigation property ref value|body|body|

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

### education education-me delete

delete a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAssignments|
|delete|DeleteRubrics|
|delete|DeleteRefUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-rubric-id**|string|key: id of educationRubric|education_rubric_id|educationRubric-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

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
|**--education-rubric-id**|string|key: id of educationRubric|education_rubric_id|educationRubric-id|
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

### education education-me list-ref-taught-class

list-ref-taught-class a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-taught-class|ListRefTaughtClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|

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

### education education-me update-assignment

update-assignment a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-assignment|UpdateAssignments|

#### Parameters
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

### education education-me update-rubric

update-rubric a education education-me.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me|education.me|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-rubric|UpdateRubrics|

#### Parameters
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

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

### education education-me-assignment delete

delete a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteCategories|
|delete|DeleteResources|
|delete|DeleteSubmissions|
|delete|DeleteRubric|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|

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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|

### education education-me-assignment update-category

update-category a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-category|UpdateCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### education education-me-assignment update-resource

update-resource a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-resource|UpdateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--id**|string|Read-only.|id|id|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### education education-me-assignment update-rubric

update-rubric a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-rubric|UpdateRubric|

#### Parameters
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

### education education-me-assignment update-submission

update-submission a education education-me-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment|education.me.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-submission|UpdateSubmissions|

#### Parameters
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### education education-me-assignment-submission delete

delete a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteOutcomes|
|delete|DeleteResources|
|delete|DeleteSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

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
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

### education education-me-assignment-submission update-outcome

update-outcome a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-outcome|UpdateOutcomes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
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

### education education-me-assignment-submission update-resource

update-resource a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-resource|UpdateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### education education-me-assignment-submission update-submitted-resource

update-submitted-resource a education education-me-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-me-assignment-submission|education.me.assignments.submissions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-submitted-resource|UpdateSubmittedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

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

### education education-root get-root

get-root a education education-root.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-root|education.educationRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-root|GetEducationRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-root update-root

update-root a education education-root.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-root|education.educationRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-root|UpdateEducationRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--synchronization-profiles**|array||synchronization_profiles|synchronizationProfiles|
|**--classes**|array|Read-only. Nullable.|classes|classes|
|**--me**|object|educationUser|me|me|
|**--schools**|array|Read-only. Nullable.|schools|schools|
|**--users**|array|Read-only. Nullable.|users|users|

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

### education education-school delete

delete a education education-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-school|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRefAdministrativeUnit|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### education education-school get-ref-administrative-unit

get-ref-administrative-unit a education education-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-school|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-administrative-unit|GetRefAdministrativeUnit|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|

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

### education education-school set-ref-administrative-unit

set-ref-administrative-unit a education education-school.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-school|education.schools|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-administrative-unit|SetRefAdministrativeUnit|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|
|**--body**|dictionary|New navigation property ref values|body|body|

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
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|

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
|**--education-school-id**|string|key: id of educationSchool|education_school_id|educationSchool-id|

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
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--id**|string|Read-only.|id|id|
|**--entry-type**|string||entry_type|entryType|
|**--error-code**|string||error_code|errorCode|
|**--error-message**|string||error_message|errorMessage|
|**--joining-value**|string||joining_value|joiningValue|
|**--recorded-date-time**|date-time||recorded_date_time|recordedDateTime|
|**--reportable-identifier**|string||reportable_identifier|reportableIdentifier|

### education education-synchronization-profile delete

delete a education education-synchronization-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-synchronization-profile|education.synchronizationProfiles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteErrors|
|delete|DeleteProfileStatus|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--education-synchronization-error-id**|string|key: id of educationSynchronizationError|education_synchronization_error_id|educationSynchronizationError-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
|**--education-synchronization-error-id**|string|key: id of educationSynchronizationError|education_synchronization_error_id|educationSynchronizationError-id|
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
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
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
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|
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
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

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
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

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
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

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
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

### education education-synchronization-profile update-error

update-error a education education-synchronization-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-synchronization-profile|education.synchronizationProfiles|

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

### education education-synchronization-profile update-profile-status

update-profile-status a education education-synchronization-profile.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-synchronization-profile|education.synchronizationProfiles|

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
|**--education-synchronization-profile-id**|string|key: id of educationSynchronizationProfile|education_synchronization_profile_id|educationSynchronizationProfile-id|

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

### education education-user create-ref-taught-class

create-ref-taught-class a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-taught-class|CreateRefTaughtClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--body**|dictionary|New navigation property ref value|body|body|

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

### education education-user delete

delete a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAssignments|
|delete|DeleteRubrics|
|delete|DeleteRefUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-rubric-id**|string|key: id of educationRubric|education_rubric_id|educationRubric-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-rubric-id**|string|key: id of educationRubric|education_rubric_id|educationRubric-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
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

### education education-user list-ref-taught-class

list-ref-taught-class a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-taught-class|ListRefTaughtClasses|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
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

### education education-user update-assignment

update-assignment a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

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

### education education-user update-rubric

update-rubric a education education-user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user|education.users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-rubric|UpdateRubrics|

#### Parameters
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

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

### education education-user-assignment delete

delete a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteCategories|
|delete|DeleteResources|
|delete|DeleteSubmissions|
|delete|DeleteRubric|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--if-match**|string|ETag|if_match|If-Match|

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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-category-id**|string|key: id of educationCategory|education_category_id|educationCategory-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|

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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|

### education education-user-assignment update-category

update-category a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

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

### education education-user-assignment update-resource

update-resource a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-resource|UpdateResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-assignment-resource-id**|string|key: id of educationAssignmentResource|education_assignment_resource_id|educationAssignmentResource-id|
|**--id**|string|Read-only.|id|id|
|**--distribute-for-student-work**|boolean||distribute_for_student_work|distributeForStudentWork|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### education education-user-assignment update-rubric

update-rubric a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

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

### education education-user-assignment update-submission

update-submission a education education-user-assignment.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment|education.users.assignments|

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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--id**|string|Read-only.|id|id|
|**--assignment-resource-url**|string||assignment_resource_url|assignmentResourceUrl|
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### education education-user-assignment-submission delete

delete a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-outcome-id**|string|key: id of educationOutcome|education_outcome_id|educationOutcome-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
|**--education-submission-resource-id**|string|key: id of educationSubmissionResource|education_submission_resource_id|educationSubmissionResource-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|
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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
|**--education-assignment-id**|string|key: id of educationAssignment|education_assignment_id|educationAssignment-id|
|**--education-submission-id**|string|key: id of educationSubmission|education_submission_id|educationSubmission-id|

### education education-user-assignment-submission update-outcome

update-outcome a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

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

### education education-user-assignment-submission update-resource

update-resource a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

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
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

### education education-user-assignment-submission update-submitted-resource

update-submitted-resource a education education-user-assignment-submission.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|education education-user-assignment-submission|education.users.assignments.submissions|

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
|**--resource-created-by**|object|identitySet|created_by|createdBy|
|**--resource-created-date-time**|date-time||created_date_time|createdDateTime|
|**--resource-display-name**|string||display_name|displayName|
|**--resource-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--resource-last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|

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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|

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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|

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
|**--education-user-id**|string|key: id of educationUser|education_user_id|educationUser-id|
