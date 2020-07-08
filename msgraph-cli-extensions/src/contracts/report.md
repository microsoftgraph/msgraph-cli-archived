# Azure CLI Module Creation Report

### contracts contract check-member-group

check-member-group a contracts contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|contracts contract|contracts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-group|checkMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: contract-id of contract|contract_id|contract-id|
|**--group-ids**|array||group_ids|groupIds|

### contracts contract check-member-object

check-member-object a contracts contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|contracts contract|contracts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-object|checkMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: contract-id of contract|contract_id|contract-id|
|**--ids**|array||ids|ids|

### contracts contract get-by-id

get-by-id a contracts contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|contracts contract|contracts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-id|getByIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

### contracts contract get-member-group

get-member-group a contracts contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|contracts contract|contracts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-group|getMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: contract-id of contract|contract_id|contract-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### contracts contract get-member-object

get-member-object a contracts contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|contracts contract|contracts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-object|getMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: contract-id of contract|contract_id|contract-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### contracts contract get-user-owned-object

get-user-owned-object a contracts contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|contracts contract|contracts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-owned-object|getUserOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string||user_id|userId|
|**--type**|string||type|type|

### contracts contract restore

restore a contracts contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|contracts contract|contracts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore|restore|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: contract-id of contract|contract_id|contract-id|

### contracts contract validate-property

validate-property a contracts contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|contracts contract|contracts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|validate-property|validateProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--entity-type**|string||entity_type|entityType|
|**--display-name**|string||display_name|displayName|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-behalf-of-user-id**|uuid||on_behalf_of_user_id|onBehalfOfUserId|

### contracts contract-contract create-contract

create-contract a contracts contract-contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|contracts contract-contract|contracts.contract|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-contract|CreateContract|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--contract-type**|string|Type of contract.Possible values are: SyndicationPartner - Partner that exclusively resells and manages O365 and Intune for this customer. They resell and support their customers. BreadthPartner - Partner has the ability to provide administrative support for this customer. However, the partner is not allowed to resell to the customer.ResellerPartner - Partner that is similar to a syndication partner, except that the partner doesn’t have exclusive access to a tenant. In the syndication case, the customer cannot buy additional direct subscriptions from Microsoft or from other partners.|contract_type|contractType|
|**--customer-id**|uuid|The unique identifier for the customer tenant referenced by this partnership. Corresponds to the id property of the customer tenant's organization resource.|customer_id|customerId|
|**--default-domain-name**|string|A copy of the customer tenant's default domain name. The copy is made when the partnership with the customer is established. It is not automatically updated if the customer tenant's default domain name changes.|default_domain_name|defaultDomainName|
|**--display-name**|string|A copy of the customer tenant's display name. The copy is made when the partnership with the customer is established. It is not automatically updated if the customer tenant's display name changes.|display_name|displayName|

### contracts contract-contract delete

delete a contracts contract-contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|contracts contract-contract|contracts.contract|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteContract|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: contract-id of contract|contract_id|contract-id|
|**--if-match**|string|ETag|if_match|If-Match|

### contracts contract-contract get-contract

get-contract a contracts contract-contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|contracts contract-contract|contracts.contract|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-contract|GetContract|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: contract-id of contract|contract_id|contract-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### contracts contract-contract list-contract

list-contract a contracts contract-contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|contracts contract-contract|contracts.contract|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-contract|ListContract|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### contracts contract-contract update

update a contracts contract-contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|contracts contract-contract|contracts.contract|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateContract|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: contract-id of contract|contract_id|contract-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--contract-type**|string|Type of contract.Possible values are: SyndicationPartner - Partner that exclusively resells and manages O365 and Intune for this customer. They resell and support their customers. BreadthPartner - Partner has the ability to provide administrative support for this customer. However, the partner is not allowed to resell to the customer.ResellerPartner - Partner that is similar to a syndication partner, except that the partner doesn’t have exclusive access to a tenant. In the syndication case, the customer cannot buy additional direct subscriptions from Microsoft or from other partners.|contract_type|contractType|
|**--customer-id**|uuid|The unique identifier for the customer tenant referenced by this partnership. Corresponds to the id property of the customer tenant's organization resource.|customer_id|customerId|
|**--default-domain-name**|string|A copy of the customer tenant's default domain name. The copy is made when the partnership with the customer is established. It is not automatically updated if the customer tenant's default domain name changes.|default_domain_name|defaultDomainName|
|**--display-name**|string|A copy of the customer tenant's display name. The copy is made when the partnership with the customer is established. It is not automatically updated if the customer tenant's display name changes.|display_name|displayName|
