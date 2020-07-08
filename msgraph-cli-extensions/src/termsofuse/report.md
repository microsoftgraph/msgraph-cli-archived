# Azure CLI Module Creation Report

### termsofuse agreement create-file

create-file a termsofuse agreement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse agreement|agreements|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-file|CreateFiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--agreement-id**|string|key: agreement-id of agreement|agreement_id|agreement-id|
|**--id**|string|Read-only.|id|id|
|**--language**|string||language|language|
|**--file-name**|string||file_name|fileName|
|**--is-default**|boolean||is_default|isDefault|
|**--file-data-data**|byte-array||data|data|

### termsofuse agreement get-file

get-file a termsofuse agreement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse agreement|agreements|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-file|GetFiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--agreement-id**|string|key: agreement-id of agreement|agreement_id|agreement-id|
|**--agreement-file-id**|string|key: agreementFile-id of agreementFile|agreement_file_id|agreementFile-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### termsofuse agreement list-file

list-file a termsofuse agreement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse agreement|agreements|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-file|ListFiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--agreement-id**|string|key: agreement-id of agreement|agreement_id|agreement-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### termsofuse agreement update

update a termsofuse agreement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse agreement|agreements|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateFiles|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--agreement-id**|string|key: agreement-id of agreement|agreement_id|agreement-id|
|**--agreement-file-id**|string|key: agreementFile-id of agreementFile|agreement_file_id|agreementFile-id|
|**--id**|string|Read-only.|id|id|
|**--language**|string||language|language|
|**--file-name**|string||file_name|fileName|
|**--is-default**|boolean||is_default|isDefault|
|**--file-data-data**|byte-array||data|data|

### termsofuse agreement-acceptance-agreement-acceptance create-agreement-acceptance

create-agreement-acceptance a termsofuse agreement-acceptance-agreement-acceptance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse agreement-acceptance-agreement-acceptance|agreementAcceptances.agreementAcceptance|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-agreement-acceptance|CreateAgreementAcceptance|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--agreement-id**|string||agreement_id|agreementId|
|**--user-id**|string||user_id|userId|
|**--agreement-file-id**|string||agreement_file_id|agreementFileId|
|**--recorded-date-time**|date-time||recorded_date_time|recordedDateTime|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--user-email**|string||user_email|userEmail|
|**--state**|choice|agreementAcceptanceState|state|state|

### termsofuse agreement-acceptance-agreement-acceptance delete

delete a termsofuse agreement-acceptance-agreement-acceptance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse agreement-acceptance-agreement-acceptance|agreementAcceptances.agreementAcceptance|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAgreementAcceptance|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--agreement-acceptance-id**|string|key: agreementAcceptance-id of agreementAcceptance|agreement_acceptance_id|agreementAcceptance-id|
|**--if-match**|string|ETag|if_match|If-Match|

### termsofuse agreement-acceptance-agreement-acceptance get-agreement-acceptance

get-agreement-acceptance a termsofuse agreement-acceptance-agreement-acceptance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse agreement-acceptance-agreement-acceptance|agreementAcceptances.agreementAcceptance|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-agreement-acceptance|GetAgreementAcceptance|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--agreement-acceptance-id**|string|key: agreementAcceptance-id of agreementAcceptance|agreement_acceptance_id|agreementAcceptance-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### termsofuse agreement-acceptance-agreement-acceptance list-agreement-acceptance

list-agreement-acceptance a termsofuse agreement-acceptance-agreement-acceptance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse agreement-acceptance-agreement-acceptance|agreementAcceptances.agreementAcceptance|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-agreement-acceptance|ListAgreementAcceptance|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### termsofuse agreement-acceptance-agreement-acceptance update

update a termsofuse agreement-acceptance-agreement-acceptance.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse agreement-acceptance-agreement-acceptance|agreementAcceptances.agreementAcceptance|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateAgreementAcceptance|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--agreement-acceptance-id**|string|key: agreementAcceptance-id of agreementAcceptance|agreement_acceptance_id|agreementAcceptance-id|
|**--id**|string|Read-only.|id|id|
|**--agreement-id**|string||agreement_id|agreementId|
|**--user-id**|string||user_id|userId|
|**--agreement-file-id**|string||agreement_file_id|agreementFileId|
|**--recorded-date-time**|date-time||recorded_date_time|recordedDateTime|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--user-email**|string||user_email|userEmail|
|**--state**|choice|agreementAcceptanceState|state|state|

### termsofuse agreement-agreement create-agreement

create-agreement a termsofuse agreement-agreement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse agreement-agreement|agreements.agreement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-agreement|CreateAgreement|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--is-viewing-before-acceptance-required**|boolean||is_viewing_before_acceptance_required|isViewingBeforeAcceptanceRequired|
|**--files**|array||files|files|

### termsofuse agreement-agreement delete

delete a termsofuse agreement-agreement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse agreement-agreement|agreements.agreement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAgreement|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--agreement-id**|string|key: agreement-id of agreement|agreement_id|agreement-id|
|**--if-match**|string|ETag|if_match|If-Match|

### termsofuse agreement-agreement get-agreement

get-agreement a termsofuse agreement-agreement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse agreement-agreement|agreements.agreement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-agreement|GetAgreement|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--agreement-id**|string|key: agreement-id of agreement|agreement_id|agreement-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### termsofuse agreement-agreement list-agreement

list-agreement a termsofuse agreement-agreement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse agreement-agreement|agreements.agreement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-agreement|ListAgreement|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### termsofuse agreement-agreement update

update a termsofuse agreement-agreement.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse agreement-agreement|agreements.agreement|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateAgreement|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--agreement-id**|string|key: agreement-id of agreement|agreement_id|agreement-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--is-viewing-before-acceptance-required**|boolean||is_viewing_before_acceptance_required|isViewingBeforeAcceptanceRequired|
|**--files**|array||files|files|

### termsofuse user get-agreement-acceptance

get-agreement-acceptance a termsofuse user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-agreement-acceptance|GetAgreementAcceptances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--agreement-acceptance-id**|string|key: agreementAcceptance-id of agreementAcceptance|agreement_acceptance_id|agreementAcceptance-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### termsofuse user list-agreement-acceptance

list-agreement-acceptance a termsofuse user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|termsofuse user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-agreement-acceptance|ListAgreementAcceptances|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|
