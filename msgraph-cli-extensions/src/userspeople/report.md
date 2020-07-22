# Azure CLI Module Creation Report

### userspeople create-person

create-person a userspeople.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userspeople|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-person|CreatePeople|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The person's display name.|display_name|displayName|
|**--given-name**|string|The person's given name.|given_name|givenName|
|**--surname**|string|The person's surname.|surname|surname|
|**--birthday**|string|The person's birthday.|birthday|birthday|
|**--person-notes**|string|Free-form notes that the user has taken about this person.|person_notes|personNotes|
|**--is-favorite**|boolean|true if the user has flagged this person as a favorite.|is_favorite|isFavorite|
|**--email-addresses**|array||email_addresses|emailAddresses|
|**--phones**|array|The person's phone numbers.|phones|phones|
|**--postal-addresses**|array|The person's addresses.|postal_addresses|postalAddresses|
|**--websites**|array|The person's websites.|websites|websites|
|**--title**|string||title|title|
|**--company-name**|string|The name of the person's company.|company_name|companyName|
|**--yomi-company**|string|The phonetic Japanese name of the person's company.|yomi_company|yomiCompany|
|**--department**|string|The person's department.|department|department|
|**--office-location**|string|The location of the person's office.|office_location|officeLocation|
|**--profession**|string|The person's profession.|profession|profession|
|**--sources**|array||sources|sources|
|**--mailbox-type**|string||mailbox_type|mailboxType|
|**--person-type**|string|The type of person.|person_type|personType|
|**--user-principal-name**|string|The user principal name (UPN) of the person. The UPN is an Internet-style login name for the person based on the Internet standard RFC 822. By convention, this should map to the person's email name. The general format is alias@domain.|user_principal_name|userPrincipalName|

### userspeople get-person

get-person a userspeople.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userspeople|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-person|GetPeople|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--person-id**|string|key: person-id of person|person_id|person-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userspeople list-person

list-person a userspeople.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userspeople|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-person|ListPeople|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### userspeople update

update a userspeople.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|userspeople|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdatePeople|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--person-id**|string|key: person-id of person|person_id|person-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The person's display name.|display_name|displayName|
|**--given-name**|string|The person's given name.|given_name|givenName|
|**--surname**|string|The person's surname.|surname|surname|
|**--birthday**|string|The person's birthday.|birthday|birthday|
|**--person-notes**|string|Free-form notes that the user has taken about this person.|person_notes|personNotes|
|**--is-favorite**|boolean|true if the user has flagged this person as a favorite.|is_favorite|isFavorite|
|**--email-addresses**|array||email_addresses|emailAddresses|
|**--phones**|array|The person's phone numbers.|phones|phones|
|**--postal-addresses**|array|The person's addresses.|postal_addresses|postalAddresses|
|**--websites**|array|The person's websites.|websites|websites|
|**--title**|string||title|title|
|**--company-name**|string|The name of the person's company.|company_name|companyName|
|**--yomi-company**|string|The phonetic Japanese name of the person's company.|yomi_company|yomiCompany|
|**--department**|string|The person's department.|department|department|
|**--office-location**|string|The location of the person's office.|office_location|officeLocation|
|**--profession**|string|The person's profession.|profession|profession|
|**--sources**|array||sources|sources|
|**--mailbox-type**|string||mailbox_type|mailboxType|
|**--person-type**|string|The type of person.|person_type|personType|
|**--user-principal-name**|string|The user principal name (UPN) of the person. The UPN is an Internet-style login name for the person based on the Internet standard RFC 822. By convention, this should map to the person's email name. The general format is alias@domain.|user_principal_name|userPrincipalName|
