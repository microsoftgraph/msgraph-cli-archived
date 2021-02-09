# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az people_beta|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az people_beta` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az people user|users|[commands](#CommandsInusers)|
|az people user-analytic|users.analytics|[commands](#CommandsInusers.analytics)|
|az people user-profile|users.profile|[commands](#CommandsInusers.profile)|

## COMMANDS
### <a name="CommandsInusers">Commands in `az people user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az people user delete](#usersDeletePeople)|DeletePeople|[Parameters](#ParametersusersDeletePeople)|Not Found|
|[az people user delete](#usersDeleteAnalytics)|DeleteAnalytics|[Parameters](#ParametersusersDeleteAnalytics)|Not Found|
|[az people user delete](#usersDeleteProfile)|DeleteProfile|[Parameters](#ParametersusersDeleteProfile)|Not Found|
|[az people user create-person](#usersCreatePeople)|CreatePeople|[Parameters](#ParametersusersCreatePeople)|Not Found|
|[az people user list-person](#usersListPeople)|ListPeople|[Parameters](#ParametersusersListPeople)|Not Found|
|[az people user show-analytic](#usersGetAnalytics)|GetAnalytics|[Parameters](#ParametersusersGetAnalytics)|Not Found|
|[az people user show-person](#usersGetPeople)|GetPeople|[Parameters](#ParametersusersGetPeople)|Not Found|
|[az people user show-profile](#usersGetProfile)|GetProfile|[Parameters](#ParametersusersGetProfile)|Not Found|
|[az people user update-analytic](#usersUpdateAnalytics)|UpdateAnalytics|[Parameters](#ParametersusersUpdateAnalytics)|Not Found|
|[az people user update-person](#usersUpdatePeople)|UpdatePeople|[Parameters](#ParametersusersUpdatePeople)|Not Found|
|[az people user update-profile](#usersUpdateProfile)|UpdateProfile|[Parameters](#ParametersusersUpdateProfile)|Not Found|

### <a name="CommandsInusers.analytics">Commands in `az people user-analytic` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az people user-analytic delete](#users.analyticsDeleteActivityStatistics)|DeleteActivityStatistics|[Parameters](#Parametersusers.analyticsDeleteActivityStatistics)|Not Found|
|[az people user-analytic create-activity-statistics](#users.analyticsCreateActivityStatistics)|CreateActivityStatistics|[Parameters](#Parametersusers.analyticsCreateActivityStatistics)|Not Found|
|[az people user-analytic list-activity-statistics](#users.analyticsListActivityStatistics)|ListActivityStatistics|[Parameters](#Parametersusers.analyticsListActivityStatistics)|Not Found|
|[az people user-analytic show-activity-statistics](#users.analyticsGetActivityStatistics)|GetActivityStatistics|[Parameters](#Parametersusers.analyticsGetActivityStatistics)|Not Found|
|[az people user-analytic update-activity-statistics](#users.analyticsUpdateActivityStatistics)|UpdateActivityStatistics|[Parameters](#Parametersusers.analyticsUpdateActivityStatistics)|Not Found|

### <a name="CommandsInusers.profile">Commands in `az people user-profile` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az people user-profile delete](#users.profileDeleteAccount)|DeleteAccount|[Parameters](#Parametersusers.profileDeleteAccount)|Not Found|
|[az people user-profile delete](#users.profileDeleteAddresses)|DeleteAddresses|[Parameters](#Parametersusers.profileDeleteAddresses)|Not Found|
|[az people user-profile delete](#users.profileDeleteAnniversaries)|DeleteAnniversaries|[Parameters](#Parametersusers.profileDeleteAnniversaries)|Not Found|
|[az people user-profile delete](#users.profileDeleteAwards)|DeleteAwards|[Parameters](#Parametersusers.profileDeleteAwards)|Not Found|
|[az people user-profile delete](#users.profileDeleteCertifications)|DeleteCertifications|[Parameters](#Parametersusers.profileDeleteCertifications)|Not Found|
|[az people user-profile delete](#users.profileDeleteEducationalActivities)|DeleteEducationalActivities|[Parameters](#Parametersusers.profileDeleteEducationalActivities)|Not Found|
|[az people user-profile delete](#users.profileDeleteEmails)|DeleteEmails|[Parameters](#Parametersusers.profileDeleteEmails)|Not Found|
|[az people user-profile delete](#users.profileDeleteInterests)|DeleteInterests|[Parameters](#Parametersusers.profileDeleteInterests)|Not Found|
|[az people user-profile delete](#users.profileDeleteLanguages)|DeleteLanguages|[Parameters](#Parametersusers.profileDeleteLanguages)|Not Found|
|[az people user-profile delete](#users.profileDeleteNames)|DeleteNames|[Parameters](#Parametersusers.profileDeleteNames)|Not Found|
|[az people user-profile delete](#users.profileDeleteNotes)|DeleteNotes|[Parameters](#Parametersusers.profileDeleteNotes)|Not Found|
|[az people user-profile delete](#users.profileDeletePatents)|DeletePatents|[Parameters](#Parametersusers.profileDeletePatents)|Not Found|
|[az people user-profile delete](#users.profileDeletePhones)|DeletePhones|[Parameters](#Parametersusers.profileDeletePhones)|Not Found|
|[az people user-profile delete](#users.profileDeletePositions)|DeletePositions|[Parameters](#Parametersusers.profileDeletePositions)|Not Found|
|[az people user-profile delete](#users.profileDeleteProjects)|DeleteProjects|[Parameters](#Parametersusers.profileDeleteProjects)|Not Found|
|[az people user-profile delete](#users.profileDeletePublications)|DeletePublications|[Parameters](#Parametersusers.profileDeletePublications)|Not Found|
|[az people user-profile delete](#users.profileDeleteSkills)|DeleteSkills|[Parameters](#Parametersusers.profileDeleteSkills)|Not Found|
|[az people user-profile delete](#users.profileDeleteWebAccounts)|DeleteWebAccounts|[Parameters](#Parametersusers.profileDeleteWebAccounts)|Not Found|
|[az people user-profile delete](#users.profileDeleteWebsites)|DeleteWebsites|[Parameters](#Parametersusers.profileDeleteWebsites)|Not Found|
|[az people user-profile create-account](#users.profileCreateAccount)|CreateAccount|[Parameters](#Parametersusers.profileCreateAccount)|Not Found|
|[az people user-profile create-address](#users.profileCreateAddresses)|CreateAddresses|[Parameters](#Parametersusers.profileCreateAddresses)|Not Found|
|[az people user-profile create-anniversary](#users.profileCreateAnniversaries)|CreateAnniversaries|[Parameters](#Parametersusers.profileCreateAnniversaries)|Not Found|
|[az people user-profile create-award](#users.profileCreateAwards)|CreateAwards|[Parameters](#Parametersusers.profileCreateAwards)|Not Found|
|[az people user-profile create-certification](#users.profileCreateCertifications)|CreateCertifications|[Parameters](#Parametersusers.profileCreateCertifications)|Not Found|
|[az people user-profile create-educational-activity](#users.profileCreateEducationalActivities)|CreateEducationalActivities|[Parameters](#Parametersusers.profileCreateEducationalActivities)|Not Found|
|[az people user-profile create-email](#users.profileCreateEmails)|CreateEmails|[Parameters](#Parametersusers.profileCreateEmails)|Not Found|
|[az people user-profile create-interest](#users.profileCreateInterests)|CreateInterests|[Parameters](#Parametersusers.profileCreateInterests)|Not Found|
|[az people user-profile create-language](#users.profileCreateLanguages)|CreateLanguages|[Parameters](#Parametersusers.profileCreateLanguages)|Not Found|
|[az people user-profile create-name](#users.profileCreateNames)|CreateNames|[Parameters](#Parametersusers.profileCreateNames)|Not Found|
|[az people user-profile create-note](#users.profileCreateNotes)|CreateNotes|[Parameters](#Parametersusers.profileCreateNotes)|Not Found|
|[az people user-profile create-patent](#users.profileCreatePatents)|CreatePatents|[Parameters](#Parametersusers.profileCreatePatents)|Not Found|
|[az people user-profile create-phone](#users.profileCreatePhones)|CreatePhones|[Parameters](#Parametersusers.profileCreatePhones)|Not Found|
|[az people user-profile create-position](#users.profileCreatePositions)|CreatePositions|[Parameters](#Parametersusers.profileCreatePositions)|Not Found|
|[az people user-profile create-project](#users.profileCreateProjects)|CreateProjects|[Parameters](#Parametersusers.profileCreateProjects)|Not Found|
|[az people user-profile create-publication](#users.profileCreatePublications)|CreatePublications|[Parameters](#Parametersusers.profileCreatePublications)|Not Found|
|[az people user-profile create-skill](#users.profileCreateSkills)|CreateSkills|[Parameters](#Parametersusers.profileCreateSkills)|Not Found|
|[az people user-profile create-web-account](#users.profileCreateWebAccounts)|CreateWebAccounts|[Parameters](#Parametersusers.profileCreateWebAccounts)|Not Found|
|[az people user-profile create-website](#users.profileCreateWebsites)|CreateWebsites|[Parameters](#Parametersusers.profileCreateWebsites)|Not Found|
|[az people user-profile list-account](#users.profileListAccount)|ListAccount|[Parameters](#Parametersusers.profileListAccount)|Not Found|
|[az people user-profile list-address](#users.profileListAddresses)|ListAddresses|[Parameters](#Parametersusers.profileListAddresses)|Not Found|
|[az people user-profile list-anniversary](#users.profileListAnniversaries)|ListAnniversaries|[Parameters](#Parametersusers.profileListAnniversaries)|Not Found|
|[az people user-profile list-award](#users.profileListAwards)|ListAwards|[Parameters](#Parametersusers.profileListAwards)|Not Found|
|[az people user-profile list-certification](#users.profileListCertifications)|ListCertifications|[Parameters](#Parametersusers.profileListCertifications)|Not Found|
|[az people user-profile list-educational-activity](#users.profileListEducationalActivities)|ListEducationalActivities|[Parameters](#Parametersusers.profileListEducationalActivities)|Not Found|
|[az people user-profile list-email](#users.profileListEmails)|ListEmails|[Parameters](#Parametersusers.profileListEmails)|Not Found|
|[az people user-profile list-interest](#users.profileListInterests)|ListInterests|[Parameters](#Parametersusers.profileListInterests)|Not Found|
|[az people user-profile list-language](#users.profileListLanguages)|ListLanguages|[Parameters](#Parametersusers.profileListLanguages)|Not Found|
|[az people user-profile list-name](#users.profileListNames)|ListNames|[Parameters](#Parametersusers.profileListNames)|Not Found|
|[az people user-profile list-note](#users.profileListNotes)|ListNotes|[Parameters](#Parametersusers.profileListNotes)|Not Found|
|[az people user-profile list-patent](#users.profileListPatents)|ListPatents|[Parameters](#Parametersusers.profileListPatents)|Not Found|
|[az people user-profile list-phone](#users.profileListPhones)|ListPhones|[Parameters](#Parametersusers.profileListPhones)|Not Found|
|[az people user-profile list-position](#users.profileListPositions)|ListPositions|[Parameters](#Parametersusers.profileListPositions)|Not Found|
|[az people user-profile list-project](#users.profileListProjects)|ListProjects|[Parameters](#Parametersusers.profileListProjects)|Not Found|
|[az people user-profile list-publication](#users.profileListPublications)|ListPublications|[Parameters](#Parametersusers.profileListPublications)|Not Found|
|[az people user-profile list-skill](#users.profileListSkills)|ListSkills|[Parameters](#Parametersusers.profileListSkills)|Not Found|
|[az people user-profile list-web-account](#users.profileListWebAccounts)|ListWebAccounts|[Parameters](#Parametersusers.profileListWebAccounts)|Not Found|
|[az people user-profile list-website](#users.profileListWebsites)|ListWebsites|[Parameters](#Parametersusers.profileListWebsites)|Not Found|
|[az people user-profile show-account](#users.profileGetAccount)|GetAccount|[Parameters](#Parametersusers.profileGetAccount)|Not Found|
|[az people user-profile show-address](#users.profileGetAddresses)|GetAddresses|[Parameters](#Parametersusers.profileGetAddresses)|Not Found|
|[az people user-profile show-anniversary](#users.profileGetAnniversaries)|GetAnniversaries|[Parameters](#Parametersusers.profileGetAnniversaries)|Not Found|
|[az people user-profile show-award](#users.profileGetAwards)|GetAwards|[Parameters](#Parametersusers.profileGetAwards)|Not Found|
|[az people user-profile show-certification](#users.profileGetCertifications)|GetCertifications|[Parameters](#Parametersusers.profileGetCertifications)|Not Found|
|[az people user-profile show-educational-activity](#users.profileGetEducationalActivities)|GetEducationalActivities|[Parameters](#Parametersusers.profileGetEducationalActivities)|Not Found|
|[az people user-profile show-email](#users.profileGetEmails)|GetEmails|[Parameters](#Parametersusers.profileGetEmails)|Not Found|
|[az people user-profile show-interest](#users.profileGetInterests)|GetInterests|[Parameters](#Parametersusers.profileGetInterests)|Not Found|
|[az people user-profile show-language](#users.profileGetLanguages)|GetLanguages|[Parameters](#Parametersusers.profileGetLanguages)|Not Found|
|[az people user-profile show-name](#users.profileGetNames)|GetNames|[Parameters](#Parametersusers.profileGetNames)|Not Found|
|[az people user-profile show-note](#users.profileGetNotes)|GetNotes|[Parameters](#Parametersusers.profileGetNotes)|Not Found|
|[az people user-profile show-patent](#users.profileGetPatents)|GetPatents|[Parameters](#Parametersusers.profileGetPatents)|Not Found|
|[az people user-profile show-phone](#users.profileGetPhones)|GetPhones|[Parameters](#Parametersusers.profileGetPhones)|Not Found|
|[az people user-profile show-position](#users.profileGetPositions)|GetPositions|[Parameters](#Parametersusers.profileGetPositions)|Not Found|
|[az people user-profile show-project](#users.profileGetProjects)|GetProjects|[Parameters](#Parametersusers.profileGetProjects)|Not Found|
|[az people user-profile show-publication](#users.profileGetPublications)|GetPublications|[Parameters](#Parametersusers.profileGetPublications)|Not Found|
|[az people user-profile show-skill](#users.profileGetSkills)|GetSkills|[Parameters](#Parametersusers.profileGetSkills)|Not Found|
|[az people user-profile show-web-account](#users.profileGetWebAccounts)|GetWebAccounts|[Parameters](#Parametersusers.profileGetWebAccounts)|Not Found|
|[az people user-profile show-website](#users.profileGetWebsites)|GetWebsites|[Parameters](#Parametersusers.profileGetWebsites)|Not Found|
|[az people user-profile update-account](#users.profileUpdateAccount)|UpdateAccount|[Parameters](#Parametersusers.profileUpdateAccount)|Not Found|
|[az people user-profile update-address](#users.profileUpdateAddresses)|UpdateAddresses|[Parameters](#Parametersusers.profileUpdateAddresses)|Not Found|
|[az people user-profile update-anniversary](#users.profileUpdateAnniversaries)|UpdateAnniversaries|[Parameters](#Parametersusers.profileUpdateAnniversaries)|Not Found|
|[az people user-profile update-award](#users.profileUpdateAwards)|UpdateAwards|[Parameters](#Parametersusers.profileUpdateAwards)|Not Found|
|[az people user-profile update-certification](#users.profileUpdateCertifications)|UpdateCertifications|[Parameters](#Parametersusers.profileUpdateCertifications)|Not Found|
|[az people user-profile update-educational-activity](#users.profileUpdateEducationalActivities)|UpdateEducationalActivities|[Parameters](#Parametersusers.profileUpdateEducationalActivities)|Not Found|
|[az people user-profile update-email](#users.profileUpdateEmails)|UpdateEmails|[Parameters](#Parametersusers.profileUpdateEmails)|Not Found|
|[az people user-profile update-interest](#users.profileUpdateInterests)|UpdateInterests|[Parameters](#Parametersusers.profileUpdateInterests)|Not Found|
|[az people user-profile update-language](#users.profileUpdateLanguages)|UpdateLanguages|[Parameters](#Parametersusers.profileUpdateLanguages)|Not Found|
|[az people user-profile update-name](#users.profileUpdateNames)|UpdateNames|[Parameters](#Parametersusers.profileUpdateNames)|Not Found|
|[az people user-profile update-note](#users.profileUpdateNotes)|UpdateNotes|[Parameters](#Parametersusers.profileUpdateNotes)|Not Found|
|[az people user-profile update-patent](#users.profileUpdatePatents)|UpdatePatents|[Parameters](#Parametersusers.profileUpdatePatents)|Not Found|
|[az people user-profile update-phone](#users.profileUpdatePhones)|UpdatePhones|[Parameters](#Parametersusers.profileUpdatePhones)|Not Found|
|[az people user-profile update-position](#users.profileUpdatePositions)|UpdatePositions|[Parameters](#Parametersusers.profileUpdatePositions)|Not Found|
|[az people user-profile update-project](#users.profileUpdateProjects)|UpdateProjects|[Parameters](#Parametersusers.profileUpdateProjects)|Not Found|
|[az people user-profile update-publication](#users.profileUpdatePublications)|UpdatePublications|[Parameters](#Parametersusers.profileUpdatePublications)|Not Found|
|[az people user-profile update-skill](#users.profileUpdateSkills)|UpdateSkills|[Parameters](#Parametersusers.profileUpdateSkills)|Not Found|
|[az people user-profile update-web-account](#users.profileUpdateWebAccounts)|UpdateWebAccounts|[Parameters](#Parametersusers.profileUpdateWebAccounts)|Not Found|
|[az people user-profile update-website](#users.profileUpdateWebsites)|UpdateWebsites|[Parameters](#Parametersusers.profileUpdateWebsites)|Not Found|


## COMMAND DETAILS

### group `az people user`
#### <a name="usersDeletePeople">Command `az people user delete`</a>

##### <a name="ParametersusersDeletePeople">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-id**|string|key: id of person|person_id|person-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteAnalytics">Command `az people user delete`</a>

##### <a name="ParametersusersDeleteAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="usersDeleteProfile">Command `az people user delete`</a>

##### <a name="ParametersusersDeleteProfile">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="usersCreatePeople">Command `az people user create-person`</a>

##### <a name="ParametersusersCreatePeople">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--birthday**|string|The person's birthday.|birthday|birthday|
|**--company-name**|string|The name of the person's company.|company_name|companyName|
|**--department**|string|The person's department.|department|department|
|**--display-name**|string|The person's display name.|display_name|displayName|
|**--email-addresses**|array||email_addresses|emailAddresses|
|**--given-name**|string|The person's given name.|given_name|givenName|
|**--is-favorite**|boolean|true if the user has flagged this person as a favorite.|is_favorite|isFavorite|
|**--mailbox-type**|string||mailbox_type|mailboxType|
|**--office-location**|string|The location of the person's office.|office_location|officeLocation|
|**--person-notes**|string|Free-form notes that the user has taken about this person.|person_notes|personNotes|
|**--person-type**|string|The type of person.|person_type|personType|
|**--phones**|array|The person's phone numbers.|phones|phones|
|**--postal-addresses**|array|The person's addresses.|postal_addresses|postalAddresses|
|**--profession**|string|The person's profession.|profession|profession|
|**--sources**|array||sources|sources|
|**--surname**|string|The person's surname.|surname|surname|
|**--title**|string||title|title|
|**--user-principal-name**|string|The user principal name (UPN) of the person. The UPN is an Internet-style login name for the person based on the Internet standard RFC 822. By convention, this should map to the person's email name. The general format is alias@domain.|user_principal_name|userPrincipalName|
|**--websites**|array|The person's websites.|websites|websites|
|**--yomi-company**|string|The phonetic Japanese name of the person's company.|yomi_company|yomiCompany|

#### <a name="usersListPeople">Command `az people user list-person`</a>

##### <a name="ParametersusersListPeople">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetAnalytics">Command `az people user show-analytic`</a>

##### <a name="ParametersusersGetAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetPeople">Command `az people user show-person`</a>

##### <a name="ParametersusersGetPeople">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-id**|string|key: id of person|person_id|person-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetProfile">Command `az people user show-profile`</a>

##### <a name="ParametersusersGetProfile">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateAnalytics">Command `az people user update-analytic`</a>

##### <a name="ParametersusersUpdateAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--settings**|object|settings|settings|settings|
|**--activity-statistics**|array||activity_statistics|activityStatistics|

#### <a name="usersUpdatePeople">Command `az people user update-person`</a>

##### <a name="ParametersusersUpdatePeople">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-id**|string|key: id of person|person_id|person-id|
|**--id**|string|Read-only.|id|id|
|**--birthday**|string|The person's birthday.|birthday|birthday|
|**--company-name**|string|The name of the person's company.|company_name|companyName|
|**--department**|string|The person's department.|department|department|
|**--display-name**|string|The person's display name.|display_name|displayName|
|**--email-addresses**|array||email_addresses|emailAddresses|
|**--given-name**|string|The person's given name.|given_name|givenName|
|**--is-favorite**|boolean|true if the user has flagged this person as a favorite.|is_favorite|isFavorite|
|**--mailbox-type**|string||mailbox_type|mailboxType|
|**--office-location**|string|The location of the person's office.|office_location|officeLocation|
|**--person-notes**|string|Free-form notes that the user has taken about this person.|person_notes|personNotes|
|**--person-type**|string|The type of person.|person_type|personType|
|**--phones**|array|The person's phone numbers.|phones|phones|
|**--postal-addresses**|array|The person's addresses.|postal_addresses|postalAddresses|
|**--profession**|string|The person's profession.|profession|profession|
|**--sources**|array||sources|sources|
|**--surname**|string|The person's surname.|surname|surname|
|**--title**|string||title|title|
|**--user-principal-name**|string|The user principal name (UPN) of the person. The UPN is an Internet-style login name for the person based on the Internet standard RFC 822. By convention, this should map to the person's email name. The general format is alias@domain.|user_principal_name|userPrincipalName|
|**--websites**|array|The person's websites.|websites|websites|
|**--yomi-company**|string|The phonetic Japanese name of the person's company.|yomi_company|yomiCompany|

#### <a name="usersUpdateProfile">Command `az people user update-profile`</a>

##### <a name="ParametersusersUpdateProfile">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--account**|array||account|account|
|**--addresses**|array||addresses|addresses|
|**--anniversaries**|array||anniversaries|anniversaries|
|**--awards**|array||awards|awards|
|**--certifications**|array||certifications|certifications|
|**--educational-activities**|array||educational_activities|educationalActivities|
|**--emails**|array||emails|emails|
|**--interests**|array||interests|interests|
|**--languages**|array||languages|languages|
|**--names**|array||names|names|
|**--notes**|array||notes|notes|
|**--patents**|array||patents|patents|
|**--phones**|array||phones|phones|
|**--positions**|array||positions|positions|
|**--projects**|array||projects|projects|
|**--publications**|array||publications|publications|
|**--skills**|array||skills|skills|
|**--web-accounts**|array||web_accounts|webAccounts|
|**--websites**|array||websites|websites|

### group `az people user-analytic`
#### <a name="users.analyticsDeleteActivityStatistics">Command `az people user-analytic delete`</a>

##### <a name="Parametersusers.analyticsDeleteActivityStatistics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--activity-statistics-id**|string|key: id of activityStatistics|activity_statistics_id|activityStatistics-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.analyticsCreateActivityStatistics">Command `az people user-analytic create-activity-statistics`</a>

##### <a name="Parametersusers.analyticsCreateActivityStatistics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--activity**|choice||activity|activity|
|**--duration**|duration||duration|duration|
|**--end-date**|date||end_date|endDate|
|**--start-date**|date||start_date|startDate|
|**--time-zone-used**|string||time_zone_used|timeZoneUsed|

#### <a name="users.analyticsListActivityStatistics">Command `az people user-analytic list-activity-statistics`</a>

##### <a name="Parametersusers.analyticsListActivityStatistics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.analyticsGetActivityStatistics">Command `az people user-analytic show-activity-statistics`</a>

##### <a name="Parametersusers.analyticsGetActivityStatistics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--activity-statistics-id**|string|key: id of activityStatistics|activity_statistics_id|activityStatistics-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.analyticsUpdateActivityStatistics">Command `az people user-analytic update-activity-statistics`</a>

##### <a name="Parametersusers.analyticsUpdateActivityStatistics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--activity-statistics-id**|string|key: id of activityStatistics|activity_statistics_id|activityStatistics-id|
|**--id**|string|Read-only.|id|id|
|**--activity**|choice||activity|activity|
|**--duration**|duration||duration|duration|
|**--end-date**|date||end_date|endDate|
|**--start-date**|date||start_date|startDate|
|**--time-zone-used**|string||time_zone_used|timeZoneUsed|

### group `az people user-profile`
#### <a name="users.profileDeleteAccount">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeleteAccount">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-account-information-id**|string|key: id of userAccountInformation|user_account_information_id|userAccountInformation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.profileDeleteAddresses">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeleteAddresses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--item-address-id**|string|key: id of itemAddress|item_address_id|itemAddress-id|

#### <a name="users.profileDeleteAnniversaries">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeleteAnniversaries">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--person-anniversary-id**|string|key: id of personAnniversary|person_anniversary_id|personAnniversary-id|

#### <a name="users.profileDeleteAwards">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeleteAwards">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--person-award-id**|string|key: id of personAward|person_award_id|personAward-id|

#### <a name="users.profileDeleteCertifications">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeleteCertifications">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--person-certification-id**|string|key: id of personCertification|person_certification_id|personCertification-id|

#### <a name="users.profileDeleteEducationalActivities">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeleteEducationalActivities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--educational-activity-id**|string|key: id of educationalActivity|educational_activity_id|educationalActivity-id|

#### <a name="users.profileDeleteEmails">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeleteEmails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--item-email-id**|string|key: id of itemEmail|item_email_id|itemEmail-id|

#### <a name="users.profileDeleteInterests">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeleteInterests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--person-interest-id**|string|key: id of personInterest|person_interest_id|personInterest-id|

#### <a name="users.profileDeleteLanguages">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeleteLanguages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--language-proficiency-id**|string|key: id of languageProficiency|language_proficiency_id|languageProficiency-id|

#### <a name="users.profileDeleteNames">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeleteNames">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--person-name-id**|string|key: id of personName|person_name_id|personName-id|

#### <a name="users.profileDeleteNotes">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeleteNotes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--person-annotation-id**|string|key: id of personAnnotation|person_annotation_id|personAnnotation-id|

#### <a name="users.profileDeletePatents">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeletePatents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--item-patent-id**|string|key: id of itemPatent|item_patent_id|itemPatent-id|

#### <a name="users.profileDeletePhones">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeletePhones">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--item-phone-id**|string|key: id of itemPhone|item_phone_id|itemPhone-id|

#### <a name="users.profileDeletePositions">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeletePositions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--work-position-id**|string|key: id of workPosition|work_position_id|workPosition-id|

#### <a name="users.profileDeleteProjects">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeleteProjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--project-participation-id**|string|key: id of projectParticipation|project_participation_id|projectParticipation-id|

#### <a name="users.profileDeletePublications">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeletePublications">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--item-publication-id**|string|key: id of itemPublication|item_publication_id|itemPublication-id|

#### <a name="users.profileDeleteSkills">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeleteSkills">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--skill-proficiency-id**|string|key: id of skillProficiency|skill_proficiency_id|skillProficiency-id|

#### <a name="users.profileDeleteWebAccounts">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeleteWebAccounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--web-account-id**|string|key: id of webAccount|web_account_id|webAccount-id|

#### <a name="users.profileDeleteWebsites">Command `az people user-profile delete`</a>

##### <a name="Parametersusers.profileDeleteWebsites">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--person-website-id**|string|key: id of personWebsite|person_website_id|personWebsite-id|

#### <a name="users.profileCreateAccount">Command `az people user-profile create-account`</a>

##### <a name="Parametersusers.profileCreateAccount">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--age-group**|string||age_group|ageGroup|
|**--country-code**|string||country_code|countryCode|
|**--preferred-language-tag**|object|localeInfo|preferred_language_tag|preferredLanguageTag|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

#### <a name="users.profileCreateAddresses">Command `az people user-profile create-address`</a>

##### <a name="Parametersusers.profileCreateAddresses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--detail**|object|physicalAddress|detail|detail|
|**--display-name**|string||display_name|displayName|
|**--geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|

#### <a name="users.profileCreateAnniversaries">Command `az people user-profile create-anniversary`</a>

##### <a name="Parametersusers.profileCreateAnniversaries">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--date**|date||date|date|
|**--type**|choice||type|type|

#### <a name="users.profileCreateAwards">Command `az people user-profile create-award`</a>

##### <a name="Parametersusers.profileCreateAwards">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--issued-date**|date||issued_date|issuedDate|
|**--issuing-authority**|string||issuing_authority|issuingAuthority|
|**--thumbnail-url**|string||thumbnail_url|thumbnailUrl|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileCreateCertifications">Command `az people user-profile create-certification`</a>

##### <a name="Parametersusers.profileCreateCertifications">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--certification-id**|string||certification_id|certificationId|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--end-date**|date||end_date|endDate|
|**--issued-date**|date||issued_date|issuedDate|
|**--issuing-authority**|string||issuing_authority|issuingAuthority|
|**--issuing-company**|string||issuing_company|issuingCompany|
|**--start-date**|date||start_date|startDate|
|**--thumbnail-url**|string||thumbnail_url|thumbnailUrl|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileCreateEducationalActivities">Command `az people user-profile create-educational-activity`</a>

##### <a name="Parametersusers.profileCreateEducationalActivities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.profileCreateEmails">Command `az people user-profile create-email`</a>

##### <a name="Parametersusers.profileCreateEmails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--address**|string||address|address|
|**--display-name**|string||display_name|displayName|
|**--type**|choice||type|type|

#### <a name="users.profileCreateInterests">Command `az people user-profile create-interest`</a>

##### <a name="Parametersusers.profileCreateInterests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--collaboration-tags**|array||collaboration_tags|collaborationTags|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileCreateLanguages">Command `az people user-profile create-language`</a>

##### <a name="Parametersusers.profileCreateLanguages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string||display_name|displayName|
|**--proficiency**|choice||proficiency|proficiency|
|**--reading**|choice||reading|reading|
|**--spoken**|choice||spoken|spoken|
|**--tag**|string||tag|tag|
|**--written**|choice||written|written|

#### <a name="users.profileCreateNames">Command `az people user-profile create-name`</a>

##### <a name="Parametersusers.profileCreateNames">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string||display_name|displayName|
|**--first**|string||first|first|
|**--initials**|string||initials|initials|
|**--language-tag**|string||language_tag|languageTag|
|**--last**|string||last|last|
|**--maiden**|string||maiden|maiden|
|**--middle**|string||middle|middle|
|**--nickname**|string||nickname|nickname|
|**--pronunciation**|object|yomiPersonName|pronunciation|pronunciation|
|**--suffix**|string||suffix|suffix|
|**--title**|string||title|title|

#### <a name="users.profileCreateNotes">Command `az people user-profile create-note`</a>

##### <a name="Parametersusers.profileCreateNotes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--detail**|object|itemBody|detail|detail|
|**--display-name**|string||display_name|displayName|

#### <a name="users.profileCreatePatents">Command `az people user-profile create-patent`</a>

##### <a name="Parametersusers.profileCreatePatents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--is-pending**|boolean||is_pending|isPending|
|**--issued-date**|date||issued_date|issuedDate|
|**--issuing-authority**|string||issuing_authority|issuingAuthority|
|**--number**|string||number|number|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileCreatePhones">Command `az people user-profile create-phone`</a>

##### <a name="Parametersusers.profileCreatePhones">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string||display_name|displayName|
|**--number**|string||number|number|
|**--type**|choice||type|type|

#### <a name="users.profileCreatePositions">Command `az people user-profile create-position`</a>

##### <a name="Parametersusers.profileCreatePositions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--colleagues**|array||colleagues|colleagues|
|**--is-current**|boolean||is_current|isCurrent|
|**--manager**|object|relatedPerson|manager|manager|
|**--company**|object|companyDetail|company|company|
|**--description**|string||description|description|
|**--end-month-year**|date||end_month_year|endMonthYear|
|**--job-title**|string||job_title|jobTitle|
|**--role**|string||role|role|
|**--start-month-year**|date||start_month_year|startMonthYear|
|**--summary**|string||summary|summary|

#### <a name="users.profileCreateProjects">Command `az people user-profile create-project`</a>

##### <a name="Parametersusers.profileCreateProjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--collaboration-tags**|array||collaboration_tags|collaborationTags|
|**--colleagues**|array||colleagues|colleagues|
|**--display-name**|string||display_name|displayName|
|**--sponsors**|array||sponsors|sponsors|
|**--company**|object|companyDetail|company|company|
|**--description**|string||description|description|
|**--end-month-year**|date||end_month_year|endMonthYear|
|**--job-title**|string||job_title|jobTitle|
|**--role**|string||role|role|
|**--start-month-year**|date||start_month_year|startMonthYear|
|**--summary**|string||summary|summary|
|**--address**|object|physicalAddress|address|address|
|**--department**|string||department|department|
|**--microsoft-graph-company-detail-display-name**|string||microsoft_graph_company_detail_display_name|displayName|
|**--office-location**|string||office_location|officeLocation|
|**--pronunciation**|string||pronunciation|pronunciation|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileCreatePublications">Command `az people user-profile create-publication`</a>

##### <a name="Parametersusers.profileCreatePublications">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--published-date**|date||published_date|publishedDate|
|**--publisher**|string||publisher|publisher|
|**--thumbnail-url**|string||thumbnail_url|thumbnailUrl|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileCreateSkills">Command `az people user-profile create-skill`</a>

##### <a name="Parametersusers.profileCreateSkills">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--collaboration-tags**|array||collaboration_tags|collaborationTags|
|**--display-name**|string||display_name|displayName|
|**--proficiency**|choice||proficiency|proficiency|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileCreateWebAccounts">Command `az people user-profile create-web-account`</a>

##### <a name="Parametersusers.profileCreateWebAccounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--service**|object|serviceInformation|service|service|
|**--status-message**|string||status_message|statusMessage|
|**--microsoft-graph-web-account-user-id**|string||microsoft_graph_web_account_user_id|userId|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileCreateWebsites">Command `az people user-profile create-website`</a>

##### <a name="Parametersusers.profileCreateWebsites">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileListAccount">Command `az people user-profile list-account`</a>

##### <a name="Parametersusers.profileListAccount">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListAddresses">Command `az people user-profile list-address`</a>

##### <a name="Parametersusers.profileListAddresses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListAnniversaries">Command `az people user-profile list-anniversary`</a>

##### <a name="Parametersusers.profileListAnniversaries">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListAwards">Command `az people user-profile list-award`</a>

##### <a name="Parametersusers.profileListAwards">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListCertifications">Command `az people user-profile list-certification`</a>

##### <a name="Parametersusers.profileListCertifications">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListEducationalActivities">Command `az people user-profile list-educational-activity`</a>

##### <a name="Parametersusers.profileListEducationalActivities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListEmails">Command `az people user-profile list-email`</a>

##### <a name="Parametersusers.profileListEmails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListInterests">Command `az people user-profile list-interest`</a>

##### <a name="Parametersusers.profileListInterests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListLanguages">Command `az people user-profile list-language`</a>

##### <a name="Parametersusers.profileListLanguages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListNames">Command `az people user-profile list-name`</a>

##### <a name="Parametersusers.profileListNames">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListNotes">Command `az people user-profile list-note`</a>

##### <a name="Parametersusers.profileListNotes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListPatents">Command `az people user-profile list-patent`</a>

##### <a name="Parametersusers.profileListPatents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListPhones">Command `az people user-profile list-phone`</a>

##### <a name="Parametersusers.profileListPhones">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListPositions">Command `az people user-profile list-position`</a>

##### <a name="Parametersusers.profileListPositions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListProjects">Command `az people user-profile list-project`</a>

##### <a name="Parametersusers.profileListProjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListPublications">Command `az people user-profile list-publication`</a>

##### <a name="Parametersusers.profileListPublications">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListSkills">Command `az people user-profile list-skill`</a>

##### <a name="Parametersusers.profileListSkills">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListWebAccounts">Command `az people user-profile list-web-account`</a>

##### <a name="Parametersusers.profileListWebAccounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileListWebsites">Command `az people user-profile list-website`</a>

##### <a name="Parametersusers.profileListWebsites">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetAccount">Command `az people user-profile show-account`</a>

##### <a name="Parametersusers.profileGetAccount">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-account-information-id**|string|key: id of userAccountInformation|user_account_information_id|userAccountInformation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetAddresses">Command `az people user-profile show-address`</a>

##### <a name="Parametersusers.profileGetAddresses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-address-id**|string|key: id of itemAddress|item_address_id|itemAddress-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetAnniversaries">Command `az people user-profile show-anniversary`</a>

##### <a name="Parametersusers.profileGetAnniversaries">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-anniversary-id**|string|key: id of personAnniversary|person_anniversary_id|personAnniversary-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetAwards">Command `az people user-profile show-award`</a>

##### <a name="Parametersusers.profileGetAwards">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-award-id**|string|key: id of personAward|person_award_id|personAward-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetCertifications">Command `az people user-profile show-certification`</a>

##### <a name="Parametersusers.profileGetCertifications">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-certification-id**|string|key: id of personCertification|person_certification_id|personCertification-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetEducationalActivities">Command `az people user-profile show-educational-activity`</a>

##### <a name="Parametersusers.profileGetEducationalActivities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--educational-activity-id**|string|key: id of educationalActivity|educational_activity_id|educationalActivity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetEmails">Command `az people user-profile show-email`</a>

##### <a name="Parametersusers.profileGetEmails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-email-id**|string|key: id of itemEmail|item_email_id|itemEmail-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetInterests">Command `az people user-profile show-interest`</a>

##### <a name="Parametersusers.profileGetInterests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-interest-id**|string|key: id of personInterest|person_interest_id|personInterest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetLanguages">Command `az people user-profile show-language`</a>

##### <a name="Parametersusers.profileGetLanguages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--language-proficiency-id**|string|key: id of languageProficiency|language_proficiency_id|languageProficiency-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetNames">Command `az people user-profile show-name`</a>

##### <a name="Parametersusers.profileGetNames">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-name-id**|string|key: id of personName|person_name_id|personName-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetNotes">Command `az people user-profile show-note`</a>

##### <a name="Parametersusers.profileGetNotes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-annotation-id**|string|key: id of personAnnotation|person_annotation_id|personAnnotation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetPatents">Command `az people user-profile show-patent`</a>

##### <a name="Parametersusers.profileGetPatents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-patent-id**|string|key: id of itemPatent|item_patent_id|itemPatent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetPhones">Command `az people user-profile show-phone`</a>

##### <a name="Parametersusers.profileGetPhones">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-phone-id**|string|key: id of itemPhone|item_phone_id|itemPhone-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetPositions">Command `az people user-profile show-position`</a>

##### <a name="Parametersusers.profileGetPositions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--work-position-id**|string|key: id of workPosition|work_position_id|workPosition-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetProjects">Command `az people user-profile show-project`</a>

##### <a name="Parametersusers.profileGetProjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--project-participation-id**|string|key: id of projectParticipation|project_participation_id|projectParticipation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetPublications">Command `az people user-profile show-publication`</a>

##### <a name="Parametersusers.profileGetPublications">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-publication-id**|string|key: id of itemPublication|item_publication_id|itemPublication-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetSkills">Command `az people user-profile show-skill`</a>

##### <a name="Parametersusers.profileGetSkills">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--skill-proficiency-id**|string|key: id of skillProficiency|skill_proficiency_id|skillProficiency-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetWebAccounts">Command `az people user-profile show-web-account`</a>

##### <a name="Parametersusers.profileGetWebAccounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--web-account-id**|string|key: id of webAccount|web_account_id|webAccount-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileGetWebsites">Command `az people user-profile show-website`</a>

##### <a name="Parametersusers.profileGetWebsites">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-website-id**|string|key: id of personWebsite|person_website_id|personWebsite-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.profileUpdateAccount">Command `az people user-profile update-account`</a>

##### <a name="Parametersusers.profileUpdateAccount">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-account-information-id**|string|key: id of userAccountInformation|user_account_information_id|userAccountInformation-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--age-group**|string||age_group|ageGroup|
|**--country-code**|string||country_code|countryCode|
|**--preferred-language-tag**|object|localeInfo|preferred_language_tag|preferredLanguageTag|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

#### <a name="users.profileUpdateAddresses">Command `az people user-profile update-address`</a>

##### <a name="Parametersusers.profileUpdateAddresses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-address-id**|string|key: id of itemAddress|item_address_id|itemAddress-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--detail**|object|physicalAddress|detail|detail|
|**--display-name**|string||display_name|displayName|
|**--geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|

#### <a name="users.profileUpdateAnniversaries">Command `az people user-profile update-anniversary`</a>

##### <a name="Parametersusers.profileUpdateAnniversaries">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-anniversary-id**|string|key: id of personAnniversary|person_anniversary_id|personAnniversary-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--date**|date||date|date|
|**--type**|choice||type|type|

#### <a name="users.profileUpdateAwards">Command `az people user-profile update-award`</a>

##### <a name="Parametersusers.profileUpdateAwards">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-award-id**|string|key: id of personAward|person_award_id|personAward-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--issued-date**|date||issued_date|issuedDate|
|**--issuing-authority**|string||issuing_authority|issuingAuthority|
|**--thumbnail-url**|string||thumbnail_url|thumbnailUrl|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileUpdateCertifications">Command `az people user-profile update-certification`</a>

##### <a name="Parametersusers.profileUpdateCertifications">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-certification-id**|string|key: id of personCertification|person_certification_id|personCertification-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--certification-id**|string||certification_id|certificationId|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--end-date**|date||end_date|endDate|
|**--issued-date**|date||issued_date|issuedDate|
|**--issuing-authority**|string||issuing_authority|issuingAuthority|
|**--issuing-company**|string||issuing_company|issuingCompany|
|**--start-date**|date||start_date|startDate|
|**--thumbnail-url**|string||thumbnail_url|thumbnailUrl|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileUpdateEducationalActivities">Command `az people user-profile update-educational-activity`</a>

##### <a name="Parametersusers.profileUpdateEducationalActivities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--educational-activity-id**|string|key: id of educationalActivity|educational_activity_id|educationalActivity-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.profileUpdateEmails">Command `az people user-profile update-email`</a>

##### <a name="Parametersusers.profileUpdateEmails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-email-id**|string|key: id of itemEmail|item_email_id|itemEmail-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--address**|string||address|address|
|**--display-name**|string||display_name|displayName|
|**--type**|choice||type|type|

#### <a name="users.profileUpdateInterests">Command `az people user-profile update-interest`</a>

##### <a name="Parametersusers.profileUpdateInterests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-interest-id**|string|key: id of personInterest|person_interest_id|personInterest-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--collaboration-tags**|array||collaboration_tags|collaborationTags|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileUpdateLanguages">Command `az people user-profile update-language`</a>

##### <a name="Parametersusers.profileUpdateLanguages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--language-proficiency-id**|string|key: id of languageProficiency|language_proficiency_id|languageProficiency-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string||display_name|displayName|
|**--proficiency**|choice||proficiency|proficiency|
|**--reading**|choice||reading|reading|
|**--spoken**|choice||spoken|spoken|
|**--tag**|string||tag|tag|
|**--written**|choice||written|written|

#### <a name="users.profileUpdateNames">Command `az people user-profile update-name`</a>

##### <a name="Parametersusers.profileUpdateNames">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-name-id**|string|key: id of personName|person_name_id|personName-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string||display_name|displayName|
|**--first**|string||first|first|
|**--initials**|string||initials|initials|
|**--language-tag**|string||language_tag|languageTag|
|**--last**|string||last|last|
|**--maiden**|string||maiden|maiden|
|**--middle**|string||middle|middle|
|**--nickname**|string||nickname|nickname|
|**--pronunciation**|object|yomiPersonName|pronunciation|pronunciation|
|**--suffix**|string||suffix|suffix|
|**--title**|string||title|title|

#### <a name="users.profileUpdateNotes">Command `az people user-profile update-note`</a>

##### <a name="Parametersusers.profileUpdateNotes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-annotation-id**|string|key: id of personAnnotation|person_annotation_id|personAnnotation-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--detail**|object|itemBody|detail|detail|
|**--display-name**|string||display_name|displayName|

#### <a name="users.profileUpdatePatents">Command `az people user-profile update-patent`</a>

##### <a name="Parametersusers.profileUpdatePatents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-patent-id**|string|key: id of itemPatent|item_patent_id|itemPatent-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--is-pending**|boolean||is_pending|isPending|
|**--issued-date**|date||issued_date|issuedDate|
|**--issuing-authority**|string||issuing_authority|issuingAuthority|
|**--number**|string||number|number|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileUpdatePhones">Command `az people user-profile update-phone`</a>

##### <a name="Parametersusers.profileUpdatePhones">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-phone-id**|string|key: id of itemPhone|item_phone_id|itemPhone-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string||display_name|displayName|
|**--number**|string||number|number|
|**--type**|choice||type|type|

#### <a name="users.profileUpdatePositions">Command `az people user-profile update-position`</a>

##### <a name="Parametersusers.profileUpdatePositions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--work-position-id**|string|key: id of workPosition|work_position_id|workPosition-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--colleagues**|array||colleagues|colleagues|
|**--is-current**|boolean||is_current|isCurrent|
|**--manager**|object|relatedPerson|manager|manager|
|**--company**|object|companyDetail|company|company|
|**--description**|string||description|description|
|**--end-month-year**|date||end_month_year|endMonthYear|
|**--job-title**|string||job_title|jobTitle|
|**--role**|string||role|role|
|**--start-month-year**|date||start_month_year|startMonthYear|
|**--summary**|string||summary|summary|

#### <a name="users.profileUpdateProjects">Command `az people user-profile update-project`</a>

##### <a name="Parametersusers.profileUpdateProjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--project-participation-id**|string|key: id of projectParticipation|project_participation_id|projectParticipation-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--collaboration-tags**|array||collaboration_tags|collaborationTags|
|**--colleagues**|array||colleagues|colleagues|
|**--display-name**|string||display_name|displayName|
|**--sponsors**|array||sponsors|sponsors|
|**--company**|object|companyDetail|company|company|
|**--description**|string||description|description|
|**--end-month-year**|date||end_month_year|endMonthYear|
|**--job-title**|string||job_title|jobTitle|
|**--role**|string||role|role|
|**--start-month-year**|date||start_month_year|startMonthYear|
|**--summary**|string||summary|summary|
|**--address**|object|physicalAddress|address|address|
|**--department**|string||department|department|
|**--microsoft-graph-company-detail-display-name**|string||microsoft_graph_company_detail_display_name|displayName|
|**--office-location**|string||office_location|officeLocation|
|**--pronunciation**|string||pronunciation|pronunciation|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileUpdatePublications">Command `az people user-profile update-publication`</a>

##### <a name="Parametersusers.profileUpdatePublications">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--item-publication-id**|string|key: id of itemPublication|item_publication_id|itemPublication-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--published-date**|date||published_date|publishedDate|
|**--publisher**|string||publisher|publisher|
|**--thumbnail-url**|string||thumbnail_url|thumbnailUrl|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileUpdateSkills">Command `az people user-profile update-skill`</a>

##### <a name="Parametersusers.profileUpdateSkills">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--skill-proficiency-id**|string|key: id of skillProficiency|skill_proficiency_id|skillProficiency-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--collaboration-tags**|array||collaboration_tags|collaborationTags|
|**--display-name**|string||display_name|displayName|
|**--proficiency**|choice||proficiency|proficiency|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileUpdateWebAccounts">Command `az people user-profile update-web-account`</a>

##### <a name="Parametersusers.profileUpdateWebAccounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--web-account-id**|string|key: id of webAccount|web_account_id|webAccount-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--description**|string||description|description|
|**--service**|object|serviceInformation|service|service|
|**--status-message**|string||status_message|statusMessage|
|**--microsoft-graph-web-account-user-id**|string||microsoft_graph_web_account_user_id|userId|
|**--web-url**|string||web_url|webUrl|

#### <a name="users.profileUpdateWebsites">Command `az people user-profile update-website`</a>

##### <a name="Parametersusers.profileUpdateWebsites">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--person-website-id**|string|key: id of personWebsite|person_website_id|personWebsite-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-audiences**|choice||allowed_audiences|allowedAudiences|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--inference**|object|inferenceData|inference|inference|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--source**|object|personDataSources|source|source|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--categories**|array||categories|categories|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--web-url**|string||web_url|webUrl|
