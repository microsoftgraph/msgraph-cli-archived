# Azure CLI Module Creation Report

### identitydirmgt contact check-member-group

check-member-group a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-group|checkMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--group-ids**|array||group_ids|groupIds|

### identitydirmgt contact check-member-object

check-member-object a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-object|checkMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--ids**|array||ids|ids|

### identitydirmgt contact create-ref-direct-report

create-ref-direct-report a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-direct-report|CreateRefDirectReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirmgt contact create-ref-member-of

create-ref-member-of a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-member-of|CreateRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirmgt contact create-ref-transitive-member-of

create-ref-transitive-member-of a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-transitive-member-of|CreateRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirmgt contact delete

delete a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRefManager|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt contact delta

delta a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### identitydirmgt contact get-available-extension-property

get-available-extension-property a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-available-extension-property|getAvailableExtensionProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

### identitydirmgt contact get-by-id

get-by-id a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-id|getByIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

### identitydirmgt contact get-manager

get-manager a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-manager|GetManager|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt contact get-member-group

get-member-group a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-group|getMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### identitydirmgt contact get-member-object

get-member-object a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-object|getMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### identitydirmgt contact get-ref-manager

get-ref-manager a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-manager|GetRefManager|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|

### identitydirmgt contact list-direct-report

list-direct-report a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-direct-report|ListDirectReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt contact list-member-of

list-member-of a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member-of|ListMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt contact list-ref-direct-report

list-ref-direct-report a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-direct-report|ListRefDirectReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirmgt contact list-ref-member-of

list-ref-member-of a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-member-of|ListRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirmgt contact list-ref-transitive-member-of

list-ref-transitive-member-of a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-transitive-member-of|ListRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirmgt contact list-transitive-member-of

list-transitive-member-of a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-transitive-member-of|ListTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt contact restore

restore a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore|restore|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|

### identitydirmgt contact set-ref-manager

set-ref-manager a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-manager|SetRefManager|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### identitydirmgt contact validate-property

validate-property a identitydirmgt contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact|contacts|

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

### identitydirmgt contact-org-contact create-org-contact

create-org-contact a identitydirmgt contact-org-contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact-org-contact|contacts.orgContact|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-org-contact|CreateOrgContact|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--addresses**|array||addresses|addresses|
|**--company-name**|string||company_name|companyName|
|**--department**|string||department|department|
|**--display-name**|string||display_name|displayName|
|**--given-name**|string||given_name|givenName|
|**--job-title**|string||job_title|jobTitle|
|**--mail**|string||mail|mail|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-premises-last-sync-date-time**|date-time||on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-provisioning-errors**|array||on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--on-premises-sync-enabled**|boolean||on_premises_sync_enabled|onPremisesSyncEnabled|
|**--phones**|array||phones|phones|
|**--proxy-addresses**|array||proxy_addresses|proxyAddresses|
|**--surname**|string||surname|surname|
|**--direct-reports**|array||direct_reports|directReports|
|**--manager**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|manager|manager|
|**--member-of**|array||member_of|memberOf|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|

### identitydirmgt contact-org-contact delete

delete a identitydirmgt contact-org-contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact-org-contact|contacts.orgContact|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteOrgContact|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt contact-org-contact get-org-contact

get-org-contact a identitydirmgt contact-org-contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact-org-contact|contacts.orgContact|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-org-contact|GetOrgContact|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt contact-org-contact list-org-contact

list-org-contact a identitydirmgt contact-org-contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact-org-contact|contacts.orgContact|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-org-contact|ListOrgContact|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt contact-org-contact update-org-contact

update-org-contact a identitydirmgt contact-org-contact.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contact-org-contact|contacts.orgContact|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-org-contact|UpdateOrgContact|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--addresses**|array||addresses|addresses|
|**--company-name**|string||company_name|companyName|
|**--department**|string||department|department|
|**--display-name**|string||display_name|displayName|
|**--given-name**|string||given_name|givenName|
|**--job-title**|string||job_title|jobTitle|
|**--mail**|string||mail|mail|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-premises-last-sync-date-time**|date-time||on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-provisioning-errors**|array||on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--on-premises-sync-enabled**|boolean||on_premises_sync_enabled|onPremisesSyncEnabled|
|**--phones**|array||phones|phones|
|**--proxy-addresses**|array||proxy_addresses|proxyAddresses|
|**--surname**|string||surname|surname|
|**--direct-reports**|array||direct_reports|directReports|
|**--manager**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|manager|manager|
|**--member-of**|array||member_of|memberOf|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|

### identitydirmgt contract check-member-group

check-member-group a identitydirmgt contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contract|contracts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-group|checkMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--group-ids**|array||group_ids|groupIds|

### identitydirmgt contract check-member-object

check-member-object a identitydirmgt contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contract|contracts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-object|checkMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--ids**|array||ids|ids|

### identitydirmgt contract get-available-extension-property

get-available-extension-property a identitydirmgt contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contract|contracts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-available-extension-property|getAvailableExtensionProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

### identitydirmgt contract get-by-id

get-by-id a identitydirmgt contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contract|contracts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-id|getByIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

### identitydirmgt contract get-member-group

get-member-group a identitydirmgt contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contract|contracts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-group|getMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### identitydirmgt contract get-member-object

get-member-object a identitydirmgt contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contract|contracts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-object|getMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### identitydirmgt contract restore

restore a identitydirmgt contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contract|contracts|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore|restore|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|

### identitydirmgt contract validate-property

validate-property a identitydirmgt contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contract|contracts|

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

### identitydirmgt contract-contract create-contract

create-contract a identitydirmgt contract-contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contract-contract|contracts.contract|

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

### identitydirmgt contract-contract delete

delete a identitydirmgt contract-contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contract-contract|contracts.contract|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteContract|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt contract-contract get-contract

get-contract a identitydirmgt contract-contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contract-contract|contracts.contract|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-contract|GetContract|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt contract-contract list-contract

list-contract a identitydirmgt contract-contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contract-contract|contracts.contract|

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

### identitydirmgt contract-contract update-contract

update-contract a identitydirmgt contract-contract.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt contract-contract|contracts.contract|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-contract|UpdateContract|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--contract-type**|string|Type of contract.Possible values are: SyndicationPartner - Partner that exclusively resells and manages O365 and Intune for this customer. They resell and support their customers. BreadthPartner - Partner has the ability to provide administrative support for this customer. However, the partner is not allowed to resell to the customer.ResellerPartner - Partner that is similar to a syndication partner, except that the partner doesn’t have exclusive access to a tenant. In the syndication case, the customer cannot buy additional direct subscriptions from Microsoft or from other partners.|contract_type|contractType|
|**--customer-id**|uuid|The unique identifier for the customer tenant referenced by this partnership. Corresponds to the id property of the customer tenant's organization resource.|customer_id|customerId|
|**--default-domain-name**|string|A copy of the customer tenant's default domain name. The copy is made when the partnership with the customer is established. It is not automatically updated if the customer tenant's default domain name changes.|default_domain_name|defaultDomainName|
|**--display-name**|string|A copy of the customer tenant's display name. The copy is made when the partnership with the customer is established. It is not automatically updated if the customer tenant's display name changes.|display_name|displayName|

### identitydirmgt device check-member-group

check-member-group a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-group|checkMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--group-ids**|array||group_ids|groupIds|

### identitydirmgt device check-member-object

check-member-object a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-object|checkMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--ids**|array||ids|ids|

### identitydirmgt device create-extension

create-extension a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--id**|string|Read-only.|id|id|

### identitydirmgt device create-ref-member-of

create-ref-member-of a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-member-of|CreateRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirmgt device create-ref-registered-owner

create-ref-registered-owner a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-registered-owner|CreateRefRegisteredOwners|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirmgt device create-ref-registered-user

create-ref-registered-user a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-registered-user|CreateRefRegisteredUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirmgt device create-ref-transitive-member-of

create-ref-transitive-member-of a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-transitive-member-of|CreateRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirmgt device delete

delete a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt device get-available-extension-property

get-available-extension-property a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-available-extension-property|getAvailableExtensionProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

### identitydirmgt device get-by-id

get-by-id a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-id|getByIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

### identitydirmgt device get-extension

get-extension a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt device get-member-group

get-member-group a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-group|getMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### identitydirmgt device get-member-object

get-member-object a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-object|getMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### identitydirmgt device list-extension

list-extension a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt device list-member-of

list-member-of a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member-of|ListMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt device list-ref-member-of

list-ref-member-of a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-member-of|ListRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirmgt device list-ref-registered-owner

list-ref-registered-owner a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-registered-owner|ListRefRegisteredOwners|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirmgt device list-ref-registered-user

list-ref-registered-user a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-registered-user|ListRefRegisteredUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirmgt device list-ref-transitive-member-of

list-ref-transitive-member-of a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-transitive-member-of|ListRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirmgt device list-registered-owner

list-registered-owner a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-registered-owner|ListRegisteredOwners|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt device list-registered-user

list-registered-user a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-registered-user|ListRegisteredUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt device list-transitive-member-of

list-transitive-member-of a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-transitive-member-of|ListTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt device restore

restore a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore|restore|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|

### identitydirmgt device update-extension

update-extension a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### identitydirmgt device validate-property

validate-property a identitydirmgt device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device|devices|

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

### identitydirmgt device-device create-device

create-device a identitydirmgt device-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device-device|devices.device|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-device|CreateDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--account-enabled**|boolean|true if the account is enabled; otherwise, false. Required.|account_enabled|accountEnabled|
|**--alternative-security-ids**|array|For internal use only. Not nullable.|alternative_security_ids|alternativeSecurityIds|
|**--approximate-last-sign-in-date-time**|date-time|The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|approximate_last_sign_in_date_time|approximateLastSignInDateTime|
|**--compliance-expiration-date-time**|date-time|The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|compliance_expiration_date_time|complianceExpirationDateTime|
|**--device-id**|string|Unique identifier set by Azure Device Registration Service at the time of registration.|device_id|deviceId|
|**--device-metadata**|string|For interal use only. Set to null.|device_metadata|deviceMetadata|
|**--device-version**|integer|For interal use only.|device_version|deviceVersion|
|**--display-name**|string|The display name for the device. Required.|display_name|displayName|
|**--is-compliant**|boolean|true if the device complies with Mobile Device Management (MDM) policies; otherwise, false. Read-only. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices.|is_compliant|isCompliant|
|**--is-managed**|boolean|true if the device is managed by a Mobile Device Management (MDM) app; otherwise, false. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices.|is_managed|isManaged|
|**--mdm-app-id**|string|Application identifier used to register device into MDM. Read-only. Supports $filter.|mdm_app_id|mdmAppId|
|**--on-premises-last-sync-date-time**|date-time|The last time at which the object was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z' Read-only.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-sync-enabled**|boolean|true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--operating-system**|string|The type of operating system on the device. Required.|operating_system|operatingSystem|
|**--operating-system-version**|string|The version of the operating system on the device. Required.|operating_system_version|operatingSystemVersion|
|**--physical-ids**|array|For interal use only. Not nullable.|physical_ids|physicalIds|
|**--profile-type**|string|The profile type of the device. Possible values:RegisteredDevice (default)SecureVMPrinterSharedIoT|profile_type|profileType|
|**--system-labels**|array|List of labels applied to the device by the system.|system_labels|systemLabels|
|**--trust-type**|string|Type of trust for the joined device. Read-only. Possible values: Workplace - indicates bring your own personal devicesAzureAd - Cloud only joined devicesServerAd - on-premises domain joined devices joined to Azure AD. For more details, see Introduction to device management in Azure Active Directory|trust_type|trustType|
|**--member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--registered-owners**|array|The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Currently, there can be only one owner. Read-only. Nullable.|registered_owners|registeredOwners|
|**--registered-users**|array|Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable.|registered_users|registeredUsers|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--extensions**|array|The collection of open extensions defined for the device. Read-only. Nullable.|extensions|extensions|

### identitydirmgt device-device delete

delete a identitydirmgt device-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device-device|devices.device|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt device-device get-device

get-device a identitydirmgt device-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device-device|devices.device|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-device|GetDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt device-device list-device

list-device a identitydirmgt device-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device-device|devices.device|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-device|ListDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt device-device update-device

update-device a identitydirmgt device-device.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt device-device|devices.device|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-device|UpdateDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--account-enabled**|boolean|true if the account is enabled; otherwise, false. Required.|account_enabled|accountEnabled|
|**--alternative-security-ids**|array|For internal use only. Not nullable.|alternative_security_ids|alternativeSecurityIds|
|**--approximate-last-sign-in-date-time**|date-time|The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|approximate_last_sign_in_date_time|approximateLastSignInDateTime|
|**--compliance-expiration-date-time**|date-time|The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|compliance_expiration_date_time|complianceExpirationDateTime|
|**--microsoft-graph-device-id**|string|Unique identifier set by Azure Device Registration Service at the time of registration.|microsoft_graph_device_id|deviceId|
|**--device-metadata**|string|For interal use only. Set to null.|device_metadata|deviceMetadata|
|**--device-version**|integer|For interal use only.|device_version|deviceVersion|
|**--display-name**|string|The display name for the device. Required.|display_name|displayName|
|**--is-compliant**|boolean|true if the device complies with Mobile Device Management (MDM) policies; otherwise, false. Read-only. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices.|is_compliant|isCompliant|
|**--is-managed**|boolean|true if the device is managed by a Mobile Device Management (MDM) app; otherwise, false. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices.|is_managed|isManaged|
|**--mdm-app-id**|string|Application identifier used to register device into MDM. Read-only. Supports $filter.|mdm_app_id|mdmAppId|
|**--on-premises-last-sync-date-time**|date-time|The last time at which the object was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z' Read-only.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-sync-enabled**|boolean|true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--operating-system**|string|The type of operating system on the device. Required.|operating_system|operatingSystem|
|**--operating-system-version**|string|The version of the operating system on the device. Required.|operating_system_version|operatingSystemVersion|
|**--physical-ids**|array|For interal use only. Not nullable.|physical_ids|physicalIds|
|**--profile-type**|string|The profile type of the device. Possible values:RegisteredDevice (default)SecureVMPrinterSharedIoT|profile_type|profileType|
|**--system-labels**|array|List of labels applied to the device by the system.|system_labels|systemLabels|
|**--trust-type**|string|Type of trust for the joined device. Read-only. Possible values: Workplace - indicates bring your own personal devicesAzureAd - Cloud only joined devicesServerAd - on-premises domain joined devices joined to Azure AD. For more details, see Introduction to device management in Azure Active Directory|trust_type|trustType|
|**--member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--registered-owners**|array|The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Currently, there can be only one owner. Read-only. Nullable.|registered_owners|registeredOwners|
|**--registered-users**|array|Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable.|registered_users|registeredUsers|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--extensions**|array|The collection of open extensions defined for the device. Read-only. Nullable.|extensions|extensions|

### identitydirmgt directory create-administrative-unit

create-administrative-unit a identitydirmgt directory.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-administrative-unit|CreateAdministrativeUnits|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|An optional description for the administrative unit.|description|description|
|**--display-name**|string|Display name for the administrative unit.|display_name|displayName|
|**--visibility**|string|Controls whether the adminstrative unit and its members are hidden or public. Can be set to HiddenMembership or Public. If not set, default behavior is Public. When set to HiddenMembership, only members of the administrative unit can list other members of the adminstrative unit.|visibility|visibility|
|**--members**|array|Users and groups that are members of this Adminsitrative Unit. HTTP Methods: GET (list members), POST (add members), DELETE (remove members).|members|members|
|**--scoped-role-members**|array|Scoped-role members of this Administrative Unit.  HTTP Methods: GET (list scopedRoleMemberships), POST (add scopedRoleMembership), DELETE (remove scopedRoleMembership).|scoped_role_members|scopedRoleMembers|
|**--extensions**|array||extensions|extensions|

### identitydirmgt directory create-deleted-item

create-deleted-item a identitydirmgt directory.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-deleted-item|CreateDeletedItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|

### identitydirmgt directory delete

delete a identitydirmgt directory.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAdministrativeUnits|
|delete|DeleteDeletedItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt directory get-administrative-unit

get-administrative-unit a identitydirmgt directory.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-administrative-unit|GetAdministrativeUnits|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory get-deleted-item

get-deleted-item a identitydirmgt directory.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-deleted-item|GetDeletedItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory list-administrative-unit

list-administrative-unit a identitydirmgt directory.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-administrative-unit|ListAdministrativeUnits|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory list-deleted-item

list-deleted-item a identitydirmgt directory.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-deleted-item|ListDeletedItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory update-administrative-unit

update-administrative-unit a identitydirmgt directory.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-administrative-unit|UpdateAdministrativeUnits|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|An optional description for the administrative unit.|description|description|
|**--display-name**|string|Display name for the administrative unit.|display_name|displayName|
|**--visibility**|string|Controls whether the adminstrative unit and its members are hidden or public. Can be set to HiddenMembership or Public. If not set, default behavior is Public. When set to HiddenMembership, only members of the administrative unit can list other members of the adminstrative unit.|visibility|visibility|
|**--members**|array|Users and groups that are members of this Adminsitrative Unit. HTTP Methods: GET (list members), POST (add members), DELETE (remove members).|members|members|
|**--scoped-role-members**|array|Scoped-role members of this Administrative Unit.  HTTP Methods: GET (list scopedRoleMemberships), POST (add scopedRoleMembership), DELETE (remove scopedRoleMembership).|scoped_role_members|scopedRoleMembers|
|**--extensions**|array||extensions|extensions|

### identitydirmgt directory update-deleted-item

update-deleted-item a identitydirmgt directory.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory|directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-deleted-item|UpdateDeletedItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|

### identitydirmgt directory-administrative-unit create-extension

create-extension a identitydirmgt directory-administrative-unit.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-administrative-unit|directory.administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--id**|string|Read-only.|id|id|

### identitydirmgt directory-administrative-unit create-ref-member

create-ref-member a identitydirmgt directory-administrative-unit.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-administrative-unit|directory.administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-member|CreateRefMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirmgt directory-administrative-unit create-scoped-role-member

create-scoped-role-member a identitydirmgt directory-administrative-unit.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-administrative-unit|directory.administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-scoped-role-member|CreateScopedRoleMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--id**|string|Read-only.|id|id|
|**--microsoft-graph-scoped-role-membership-administrative-unit-id-administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|microsoft_graph_scoped_role_membership_administrative_unit_id_administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--role-member-info-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|

### identitydirmgt directory-administrative-unit delete

delete a identitydirmgt directory-administrative-unit.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-administrative-unit|directory.administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteExtensions|
|delete|DeleteScopedRoleMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt directory-administrative-unit delta

delta a identitydirmgt directory-administrative-unit.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-administrative-unit|directory.administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### identitydirmgt directory-administrative-unit get-extension

get-extension a identitydirmgt directory-administrative-unit.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-administrative-unit|directory.administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory-administrative-unit get-scoped-role-member

get-scoped-role-member a identitydirmgt directory-administrative-unit.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-administrative-unit|directory.administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-scoped-role-member|GetScopedRoleMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory-administrative-unit list-extension

list-extension a identitydirmgt directory-administrative-unit.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-administrative-unit|directory.administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory-administrative-unit list-member

list-member a identitydirmgt directory-administrative-unit.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-administrative-unit|directory.administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member|ListMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory-administrative-unit list-ref-member

list-ref-member a identitydirmgt directory-administrative-unit.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-administrative-unit|directory.administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-member|ListRefMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirmgt directory-administrative-unit list-scoped-role-member

list-scoped-role-member a identitydirmgt directory-administrative-unit.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-administrative-unit|directory.administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-scoped-role-member|ListScopedRoleMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory-administrative-unit update-extension

update-extension a identitydirmgt directory-administrative-unit.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-administrative-unit|directory.administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### identitydirmgt directory-administrative-unit update-scoped-role-member

update-scoped-role-member a identitydirmgt directory-administrative-unit.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-administrative-unit|directory.administrativeUnits|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-scoped-role-member|UpdateScopedRoleMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--id**|string|Read-only.|id|id|
|**--microsoft-graph-scoped-role-membership-administrative-unit-id-administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|microsoft_graph_scoped_role_membership_administrative_unit_id_administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--role-member-info-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|

### identitydirmgt directory-directory get-directory

get-directory a identitydirmgt directory-directory.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-directory|directory.directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-directory|GetDirectory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory-directory update-directory

update-directory a identitydirmgt directory-directory.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-directory|directory.directory|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-directory|UpdateDirectory|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--administrative-units**|array||administrative_units|administrativeUnits|
|**--deleted-items**|array|Recently deleted items. Read-only. Nullable.|deleted_items|deletedItems|

### identitydirmgt directory-role check-member-group

check-member-group a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-group|checkMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--group-ids**|array||group_ids|groupIds|

### identitydirmgt directory-role check-member-object

check-member-object a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-object|checkMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--ids**|array||ids|ids|

### identitydirmgt directory-role create-ref-member

create-ref-member a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-member|CreateRefMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirmgt directory-role create-scoped-member

create-scoped-member a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-scoped-member|CreateScopedMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--id**|string|Read-only.|id|id|
|**--administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--role-member-info-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|

### identitydirmgt directory-role delete

delete a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteScopedMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt directory-role delta

delta a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delta|delta|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### identitydirmgt directory-role get-available-extension-property

get-available-extension-property a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-available-extension-property|getAvailableExtensionProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

### identitydirmgt directory-role get-by-id

get-by-id a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-id|getByIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

### identitydirmgt directory-role get-member-group

get-member-group a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-group|getMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### identitydirmgt directory-role get-member-object

get-member-object a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-object|getMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### identitydirmgt directory-role get-scoped-member

get-scoped-member a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-scoped-member|GetScopedMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory-role list-member

list-member a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member|ListMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory-role list-ref-member

list-ref-member a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-member|ListRefMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirmgt directory-role list-scoped-member

list-scoped-member a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-scoped-member|ListScopedMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory-role restore

restore a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore|restore|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|

### identitydirmgt directory-role update-scoped-member

update-scoped-member a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-scoped-member|UpdateScopedMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--id**|string|Read-only.|id|id|
|**--administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--role-member-info-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|

### identitydirmgt directory-role validate-property

validate-property a identitydirmgt directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role|directoryRoles|

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

### identitydirmgt directory-role-directory-role create-directory-role

create-directory-role a identitydirmgt directory-role-directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-directory-role|directoryRoles.directoryRole|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-directory-role|CreateDirectoryRole|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|The description for the directory role. Read-only.|description|description|
|**--display-name**|string|The display name for the directory role. Read-only.|display_name|displayName|
|**--role-template-id**|string|The id of the directoryRoleTemplate that this role is based on. The property must be specified when activating a directory role in a tenant with a POST operation. After the directory role has been activated, the property is read only.|role_template_id|roleTemplateId|
|**--members**|array|Users that are members of this directory role. HTTP Methods: GET, POST, DELETE. Read-only. Nullable.|members|members|
|**--scoped-members**|array||scoped_members|scopedMembers|

### identitydirmgt directory-role-directory-role delete

delete a identitydirmgt directory-role-directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-directory-role|directoryRoles.directoryRole|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteDirectoryRole|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt directory-role-directory-role get-directory-role

get-directory-role a identitydirmgt directory-role-directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-directory-role|directoryRoles.directoryRole|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-directory-role|GetDirectoryRole|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory-role-directory-role list-directory-role

list-directory-role a identitydirmgt directory-role-directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-directory-role|directoryRoles.directoryRole|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-directory-role|ListDirectoryRole|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory-role-directory-role update-directory-role

update-directory-role a identitydirmgt directory-role-directory-role.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-directory-role|directoryRoles.directoryRole|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-directory-role|UpdateDirectoryRole|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|The description for the directory role. Read-only.|description|description|
|**--display-name**|string|The display name for the directory role. Read-only.|display_name|displayName|
|**--role-template-id**|string|The id of the directoryRoleTemplate that this role is based on. The property must be specified when activating a directory role in a tenant with a POST operation. After the directory role has been activated, the property is read only.|role_template_id|roleTemplateId|
|**--members**|array|Users that are members of this directory role. HTTP Methods: GET, POST, DELETE. Read-only. Nullable.|members|members|
|**--scoped-members**|array||scoped_members|scopedMembers|

### identitydirmgt directory-role-template check-member-group

check-member-group a identitydirmgt directory-role-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-template|directoryRoleTemplates|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-group|checkMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--group-ids**|array||group_ids|groupIds|

### identitydirmgt directory-role-template check-member-object

check-member-object a identitydirmgt directory-role-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-template|directoryRoleTemplates|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-object|checkMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--ids**|array||ids|ids|

### identitydirmgt directory-role-template get-available-extension-property

get-available-extension-property a identitydirmgt directory-role-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-template|directoryRoleTemplates|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-available-extension-property|getAvailableExtensionProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

### identitydirmgt directory-role-template get-by-id

get-by-id a identitydirmgt directory-role-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-template|directoryRoleTemplates|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-id|getByIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

### identitydirmgt directory-role-template get-member-group

get-member-group a identitydirmgt directory-role-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-template|directoryRoleTemplates|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-group|getMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### identitydirmgt directory-role-template get-member-object

get-member-object a identitydirmgt directory-role-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-template|directoryRoleTemplates|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-object|getMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### identitydirmgt directory-role-template restore

restore a identitydirmgt directory-role-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-template|directoryRoleTemplates|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore|restore|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|

### identitydirmgt directory-role-template validate-property

validate-property a identitydirmgt directory-role-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-template|directoryRoleTemplates|

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

### identitydirmgt directory-role-template-directory-role-template create-directory-role-template

create-directory-role-template a identitydirmgt directory-role-template-directory-role-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-template-directory-role-template|directoryRoleTemplates.directoryRoleTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-directory-role-template|CreateDirectoryRoleTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|The description to set for the directory role. Read-only.|description|description|
|**--display-name**|string|The display name to set for the directory role. Read-only.|display_name|displayName|

### identitydirmgt directory-role-template-directory-role-template delete

delete a identitydirmgt directory-role-template-directory-role-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-template-directory-role-template|directoryRoleTemplates.directoryRoleTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteDirectoryRoleTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt directory-role-template-directory-role-template get-directory-role-template

get-directory-role-template a identitydirmgt directory-role-template-directory-role-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-template-directory-role-template|directoryRoleTemplates.directoryRoleTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-directory-role-template|GetDirectoryRoleTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory-role-template-directory-role-template list-directory-role-template

list-directory-role-template a identitydirmgt directory-role-template-directory-role-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-template-directory-role-template|directoryRoleTemplates.directoryRoleTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-directory-role-template|ListDirectoryRoleTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt directory-role-template-directory-role-template update-directory-role-template

update-directory-role-template a identitydirmgt directory-role-template-directory-role-template.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt directory-role-template-directory-role-template|directoryRoleTemplates.directoryRoleTemplate|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-directory-role-template|UpdateDirectoryRoleTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|The description to set for the directory role. Read-only.|description|description|
|**--display-name**|string|The display name to set for the directory role. Read-only.|display_name|displayName|

### identitydirmgt domain create-ref-domain-name-reference

create-ref-domain-name-reference a identitydirmgt domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-domain-name-reference|CreateRefDomainNameReferences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### identitydirmgt domain create-service-configuration-record

create-service-configuration-record a identitydirmgt domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-service-configuration-record|CreateServiceConfigurationRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--id**|string|Read-only.|id|id|
|**--is-optional**|boolean|If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.|is_optional|isOptional|
|**--label**|string|Value used when configuring the name of the DNS record at the DNS host.|label|label|
|**--record-type**|string|Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, TxtKey|record_type|recordType|
|**--supported-service**|string|Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune|supported_service|supportedService|
|**--ttl**|integer|Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable|ttl|ttl|

### identitydirmgt domain create-verification-dns-record

create-verification-dns-record a identitydirmgt domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-verification-dns-record|CreateVerificationDnsRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--id**|string|Read-only.|id|id|
|**--is-optional**|boolean|If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.|is_optional|isOptional|
|**--label**|string|Value used when configuring the name of the DNS record at the DNS host.|label|label|
|**--record-type**|string|Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, TxtKey|record_type|recordType|
|**--supported-service**|string|Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune|supported_service|supportedService|
|**--ttl**|integer|Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable|ttl|ttl|

### identitydirmgt domain delete

delete a identitydirmgt domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteServiceConfigurationRecords|
|delete|DeleteVerificationDnsRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt domain force-delete

force-delete a identitydirmgt domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|force-delete|forceDelete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--disable-user-accounts**|boolean||disable_user_accounts|disableUserAccounts|

### identitydirmgt domain get-service-configuration-record

get-service-configuration-record a identitydirmgt domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-service-configuration-record|GetServiceConfigurationRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt domain get-verification-dns-record

get-verification-dns-record a identitydirmgt domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-verification-dns-record|GetVerificationDnsRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt domain list-domain-name-reference

list-domain-name-reference a identitydirmgt domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-domain-name-reference|ListDomainNameReferences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt domain list-ref-domain-name-reference

list-ref-domain-name-reference a identitydirmgt domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-domain-name-reference|ListRefDomainNameReferences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### identitydirmgt domain list-service-configuration-record

list-service-configuration-record a identitydirmgt domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-service-configuration-record|ListServiceConfigurationRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt domain list-verification-dns-record

list-verification-dns-record a identitydirmgt domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-verification-dns-record|ListVerificationDnsRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt domain update-service-configuration-record

update-service-configuration-record a identitydirmgt domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-service-configuration-record|UpdateServiceConfigurationRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--id**|string|Read-only.|id|id|
|**--is-optional**|boolean|If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.|is_optional|isOptional|
|**--label**|string|Value used when configuring the name of the DNS record at the DNS host.|label|label|
|**--record-type**|string|Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, TxtKey|record_type|recordType|
|**--supported-service**|string|Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune|supported_service|supportedService|
|**--ttl**|integer|Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable|ttl|ttl|

### identitydirmgt domain update-verification-dns-record

update-verification-dns-record a identitydirmgt domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-verification-dns-record|UpdateVerificationDnsRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--id**|string|Read-only.|id|id|
|**--is-optional**|boolean|If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.|is_optional|isOptional|
|**--label**|string|Value used when configuring the name of the DNS record at the DNS host.|label|label|
|**--record-type**|string|Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, TxtKey|record_type|recordType|
|**--supported-service**|string|Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune|supported_service|supportedService|
|**--ttl**|integer|Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable|ttl|ttl|

### identitydirmgt domain verify

verify a identitydirmgt domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|verify|verify|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|

### identitydirmgt domain-domain create-domain

create-domain a identitydirmgt domain-domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain-domain|domains.domain|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-domain|CreateDomain|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--authentication-type**|string|Indicates the configured authentication type for the domain. The value is either Managed or Federated. Managed indicates a cloud managed domain where Azure AD performs user authentication.Federated indicates authentication is federated with an identity provider such as the tenant's on-premises Active Directory via Active Directory Federation Services. This property is read-only and is not nullable.|authentication_type|authenticationType|
|**--availability-status**|string|This property is always null except when the verify action is used. When the verify action is used, a domain entity is returned in the response. The availabilityStatus property of the domain entity in the response is either AvailableImmediately or EmailVerifiedDomainTakeoverScheduled.|availability_status|availabilityStatus|
|**--is-admin-managed**|boolean|The value of the property is false if the DNS record management of the domain has been delegated to Microsoft 365. Otherwise, the value is true. Not nullable|is_admin_managed|isAdminManaged|
|**--is-default**|boolean|True if this is the default domain that is used for user creation. There is only one default domain per company. Not nullable|is_default|isDefault|
|**--is-initial**|boolean|True if this is the initial domain created by Microsoft Online Services (companyname.onmicrosoft.com). There is only one initial domain per company. Not nullable|is_initial|isInitial|
|**--is-root**|boolean|True if the domain is a verified root domain. Otherwise, false if the domain is a subdomain or unverified. Not nullable|is_root|isRoot|
|**--is-verified**|boolean|True if the domain has completed domain ownership verification. Not nullable|is_verified|isVerified|
|**--manufacturer**|string||manufacturer|manufacturer|
|**--model**|string||model|model|
|**--password-notification-window-in-days**|integer|Specifies the number of days before a user receives notification that their password will expire. If the property is not set, a default value of 14 days will be used.|password_notification_window_in_days|passwordNotificationWindowInDays|
|**--password-validity-period-in-days**|integer|Specifies the length of time that a password is valid before it must be changed. If the property is not set, a default value of 90 days will be used.|password_validity_period_in_days|passwordValidityPeriodInDays|
|**--state**|object|domainState|state|state|
|**--supported-services**|array|The capabilities assigned to the domain.Can include 0, 1 or more of following values: Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune The values which you can add/remove using Graph API include: Email, OfficeCommunicationsOnline, YammerNot nullable|supported_services|supportedServices|
|**--domain-name-references**|array|Read-only, Nullable|domain_name_references|domainNameReferences|
|**--service-configuration-records**|array|DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services.Read-only, Nullable|service_configuration_records|serviceConfigurationRecords|
|**--verification-dns-records**|array|DNS records that the customer adds to the DNS zone file of the domain before the customer can complete domain ownership verification with Azure AD.Read-only, Nullable|verification_dns_records|verificationDnsRecords|

### identitydirmgt domain-domain delete

delete a identitydirmgt domain-domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain-domain|domains.domain|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteDomain|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt domain-domain get-domain

get-domain a identitydirmgt domain-domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain-domain|domains.domain|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-domain|GetDomain|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt domain-domain list-domain

list-domain a identitydirmgt domain-domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain-domain|domains.domain|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-domain|ListDomain|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt domain-domain update-domain

update-domain a identitydirmgt domain-domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt domain-domain|domains.domain|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-domain|UpdateDomain|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--id**|string|Read-only.|id|id|
|**--authentication-type**|string|Indicates the configured authentication type for the domain. The value is either Managed or Federated. Managed indicates a cloud managed domain where Azure AD performs user authentication.Federated indicates authentication is federated with an identity provider such as the tenant's on-premises Active Directory via Active Directory Federation Services. This property is read-only and is not nullable.|authentication_type|authenticationType|
|**--availability-status**|string|This property is always null except when the verify action is used. When the verify action is used, a domain entity is returned in the response. The availabilityStatus property of the domain entity in the response is either AvailableImmediately or EmailVerifiedDomainTakeoverScheduled.|availability_status|availabilityStatus|
|**--is-admin-managed**|boolean|The value of the property is false if the DNS record management of the domain has been delegated to Microsoft 365. Otherwise, the value is true. Not nullable|is_admin_managed|isAdminManaged|
|**--is-default**|boolean|True if this is the default domain that is used for user creation. There is only one default domain per company. Not nullable|is_default|isDefault|
|**--is-initial**|boolean|True if this is the initial domain created by Microsoft Online Services (companyname.onmicrosoft.com). There is only one initial domain per company. Not nullable|is_initial|isInitial|
|**--is-root**|boolean|True if the domain is a verified root domain. Otherwise, false if the domain is a subdomain or unverified. Not nullable|is_root|isRoot|
|**--is-verified**|boolean|True if the domain has completed domain ownership verification. Not nullable|is_verified|isVerified|
|**--manufacturer**|string||manufacturer|manufacturer|
|**--model**|string||model|model|
|**--password-notification-window-in-days**|integer|Specifies the number of days before a user receives notification that their password will expire. If the property is not set, a default value of 14 days will be used.|password_notification_window_in_days|passwordNotificationWindowInDays|
|**--password-validity-period-in-days**|integer|Specifies the length of time that a password is valid before it must be changed. If the property is not set, a default value of 90 days will be used.|password_validity_period_in_days|passwordValidityPeriodInDays|
|**--state**|object|domainState|state|state|
|**--supported-services**|array|The capabilities assigned to the domain.Can include 0, 1 or more of following values: Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune The values which you can add/remove using Graph API include: Email, OfficeCommunicationsOnline, YammerNot nullable|supported_services|supportedServices|
|**--domain-name-references**|array|Read-only, Nullable|domain_name_references|domainNameReferences|
|**--service-configuration-records**|array|DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services.Read-only, Nullable|service_configuration_records|serviceConfigurationRecords|
|**--verification-dns-records**|array|DNS records that the customer adds to the DNS zone file of the domain before the customer can complete domain ownership verification with Azure AD.Read-only, Nullable|verification_dns_records|verificationDnsRecords|

### identitydirmgt organization check-member-group

check-member-group a identitydirmgt organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-group|checkMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--group-ids**|array||group_ids|groupIds|

### identitydirmgt organization check-member-object

check-member-object a identitydirmgt organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-object|checkMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--ids**|array||ids|ids|

### identitydirmgt organization create-extension

create-extension a identitydirmgt organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--id**|string|Read-only.|id|id|

### identitydirmgt organization delete

delete a identitydirmgt organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt organization get-available-extension-property

get-available-extension-property a identitydirmgt organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-available-extension-property|getAvailableExtensionProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

### identitydirmgt organization get-by-id

get-by-id a identitydirmgt organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-id|getByIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

### identitydirmgt organization get-extension

get-extension a identitydirmgt organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt organization get-member-group

get-member-group a identitydirmgt organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-group|getMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### identitydirmgt organization get-member-object

get-member-object a identitydirmgt organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-object|getMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### identitydirmgt organization list-extension

list-extension a identitydirmgt organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt organization restore

restore a identitydirmgt organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore|restore|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|

### identitydirmgt organization set-mobile-device-management-authority

set-mobile-device-management-authority a identitydirmgt organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-mobile-device-management-authority|setMobileDeviceManagementAuthority|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|

### identitydirmgt organization update-extension

update-extension a identitydirmgt organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization|organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### identitydirmgt organization validate-property

validate-property a identitydirmgt organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization|organization|

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

### identitydirmgt organization-organization create-organization

create-organization a identitydirmgt organization-organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization-organization|organization.organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-organization|CreateOrganization|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--assigned-plans**|array|The collection of service plans associated with the tenant. Not nullable.|assigned_plans|assignedPlans|
|**--business-phones**|array|Telephone number for the organization. NOTE: Although this is a string collection, only one number can be set for this property.|business_phones|businessPhones|
|**--city**|string|City name of the address for the organization.|city|city|
|**--country**|string|Country/region name of the address for the organization.|country|country|
|**--country-letter-code**|string|Country/region abbreviation for the organization.|country_letter_code|countryLetterCode|
|**--created-date-time**|date-time|Timestamp of when the organization was created. The value cannot be modified and is automatically populated when the organization is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The display name for the tenant.|display_name|displayName|
|**--marketing-notification-emails**|array|Not nullable.|marketing_notification_emails|marketingNotificationEmails|
|**--on-premises-last-sync-date-time**|date-time|The time and date at which the tenant was last synced with the on-premise directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-sync-enabled**|boolean|true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default).|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--postal-code**|string|Postal code of the address for the organization.|postal_code|postalCode|
|**--preferred-language**|string|The preferred language for the organization. Should follow ISO 639-1 Code; for example 'en'.|preferred_language|preferredLanguage|
|**--privacy-profile**|object|privacyProfile|privacy_profile|privacyProfile|
|**--provisioned-plans**|array|Not nullable.|provisioned_plans|provisionedPlans|
|**--security-compliance-notification-mails**|array||security_compliance_notification_mails|securityComplianceNotificationMails|
|**--security-compliance-notification-phones**|array||security_compliance_notification_phones|securityComplianceNotificationPhones|
|**--state**|string|State name of the address for the organization.|state|state|
|**--street**|string|Street name of the address for organization.|street|street|
|**--technical-notification-mails**|array|Not nullable.|technical_notification_mails|technicalNotificationMails|
|**--tenant-type**|string||tenant_type|tenantType|
|**--verified-domains**|array|The collection of domains associated with this tenant. Not nullable.|verified_domains|verifiedDomains|
|**--mobile-device-management-authority**|choice||mobile_device_management_authority|mobileDeviceManagementAuthority|
|**--certificate-based-auth-configuration**|array|Navigation property to manage certificate-based authentication configuration. Only a single instance of certificateBasedAuthConfiguration can be created in the collection.|certificate_based_auth_configuration|certificateBasedAuthConfiguration|
|**--extensions**|array|The collection of open extensions defined for the organization. Read-only. Nullable.|extensions|extensions|

### identitydirmgt organization-organization delete

delete a identitydirmgt organization-organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization-organization|organization.organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteOrganization|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt organization-organization get-organization

get-organization a identitydirmgt organization-organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization-organization|organization.organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-organization|GetOrganization|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt organization-organization list-organization

list-organization a identitydirmgt organization-organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization-organization|organization.organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-organization|ListOrganization|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt organization-organization update-organization

update-organization a identitydirmgt organization-organization.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt organization-organization|organization.organization|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-organization|UpdateOrganization|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--assigned-plans**|array|The collection of service plans associated with the tenant. Not nullable.|assigned_plans|assignedPlans|
|**--business-phones**|array|Telephone number for the organization. NOTE: Although this is a string collection, only one number can be set for this property.|business_phones|businessPhones|
|**--city**|string|City name of the address for the organization.|city|city|
|**--country**|string|Country/region name of the address for the organization.|country|country|
|**--country-letter-code**|string|Country/region abbreviation for the organization.|country_letter_code|countryLetterCode|
|**--created-date-time**|date-time|Timestamp of when the organization was created. The value cannot be modified and is automatically populated when the organization is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The display name for the tenant.|display_name|displayName|
|**--marketing-notification-emails**|array|Not nullable.|marketing_notification_emails|marketingNotificationEmails|
|**--on-premises-last-sync-date-time**|date-time|The time and date at which the tenant was last synced with the on-premise directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-sync-enabled**|boolean|true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default).|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--postal-code**|string|Postal code of the address for the organization.|postal_code|postalCode|
|**--preferred-language**|string|The preferred language for the organization. Should follow ISO 639-1 Code; for example 'en'.|preferred_language|preferredLanguage|
|**--privacy-profile**|object|privacyProfile|privacy_profile|privacyProfile|
|**--provisioned-plans**|array|Not nullable.|provisioned_plans|provisionedPlans|
|**--security-compliance-notification-mails**|array||security_compliance_notification_mails|securityComplianceNotificationMails|
|**--security-compliance-notification-phones**|array||security_compliance_notification_phones|securityComplianceNotificationPhones|
|**--state**|string|State name of the address for the organization.|state|state|
|**--street**|string|Street name of the address for organization.|street|street|
|**--technical-notification-mails**|array|Not nullable.|technical_notification_mails|technicalNotificationMails|
|**--tenant-type**|string||tenant_type|tenantType|
|**--verified-domains**|array|The collection of domains associated with this tenant. Not nullable.|verified_domains|verifiedDomains|
|**--mobile-device-management-authority**|choice||mobile_device_management_authority|mobileDeviceManagementAuthority|
|**--certificate-based-auth-configuration**|array|Navigation property to manage certificate-based authentication configuration. Only a single instance of certificateBasedAuthConfiguration can be created in the collection.|certificate_based_auth_configuration|certificateBasedAuthConfiguration|
|**--extensions**|array|The collection of open extensions defined for the organization. Read-only. Nullable.|extensions|extensions|

### identitydirmgt subscribed-sku-subscribed-sku create-subscribed-sku

create-subscribed-sku a identitydirmgt subscribed-sku-subscribed-sku.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt subscribed-sku-subscribed-sku|subscribedSkus.subscribedSku|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-subscribed-sku|CreateSubscribedSku|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--applies-to**|string|For example, 'User' or 'Company'.|applies_to|appliesTo|
|**--capability-status**|string|Possible values are: Enabled, Warning, Suspended, Deleted, LockedOut.|capability_status|capabilityStatus|
|**--consumed-units**|integer|The number of licenses that have been assigned.|consumed_units|consumedUnits|
|**--prepaid-units**|object|licenseUnitsDetail|prepaid_units|prepaidUnits|
|**--service-plans**|array|Information about the service plans that are available with the SKU. Not nullable|service_plans|servicePlans|
|**--sku-id**|uuid|The unique identifier (GUID) for the service SKU.|sku_id|skuId|
|**--sku-part-number**|string|The SKU part number; for example: 'AAD_PREMIUM' or 'RMSBASIC'. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.|sku_part_number|skuPartNumber|

### identitydirmgt subscribed-sku-subscribed-sku delete

delete a identitydirmgt subscribed-sku-subscribed-sku.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt subscribed-sku-subscribed-sku|subscribedSkus.subscribedSku|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteSubscribedSku|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscribed-sku-id**|string|key: id of subscribedSku|subscribed_sku_id|subscribedSku-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt subscribed-sku-subscribed-sku get-subscribed-sku

get-subscribed-sku a identitydirmgt subscribed-sku-subscribed-sku.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt subscribed-sku-subscribed-sku|subscribedSkus.subscribedSku|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-subscribed-sku|GetSubscribedSku|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscribed-sku-id**|string|key: id of subscribedSku|subscribed_sku_id|subscribedSku-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt subscribed-sku-subscribed-sku list-subscribed-sku

list-subscribed-sku a identitydirmgt subscribed-sku-subscribed-sku.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt subscribed-sku-subscribed-sku|subscribedSkus.subscribedSku|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-subscribed-sku|ListSubscribedSku|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt subscribed-sku-subscribed-sku update-subscribed-sku

update-subscribed-sku a identitydirmgt subscribed-sku-subscribed-sku.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt subscribed-sku-subscribed-sku|subscribedSkus.subscribedSku|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-subscribed-sku|UpdateSubscribedSku|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscribed-sku-id**|string|key: id of subscribedSku|subscribed_sku_id|subscribedSku-id|
|**--id**|string|Read-only.|id|id|
|**--applies-to**|string|For example, 'User' or 'Company'.|applies_to|appliesTo|
|**--capability-status**|string|Possible values are: Enabled, Warning, Suspended, Deleted, LockedOut.|capability_status|capabilityStatus|
|**--consumed-units**|integer|The number of licenses that have been assigned.|consumed_units|consumedUnits|
|**--prepaid-units**|object|licenseUnitsDetail|prepaid_units|prepaidUnits|
|**--service-plans**|array|Information about the service plans that are available with the SKU. Not nullable|service_plans|servicePlans|
|**--sku-id**|uuid|The unique identifier (GUID) for the service SKU.|sku_id|skuId|
|**--sku-part-number**|string|The SKU part number; for example: 'AAD_PREMIUM' or 'RMSBASIC'. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.|sku_part_number|skuPartNumber|

### identitydirmgt user create-scoped-role-member-of

create-scoped-role-member-of a identitydirmgt user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-scoped-role-member-of|CreateScopedRoleMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--role-member-info-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|

### identitydirmgt user delete

delete a identitydirmgt user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteScopedRoleMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--if-match**|string|ETag|if_match|If-Match|

### identitydirmgt user get-scoped-role-member-of

get-scoped-role-member-of a identitydirmgt user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-scoped-role-member-of|GetScopedRoleMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt user list-scoped-role-member-of

list-scoped-role-member-of a identitydirmgt user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-scoped-role-member-of|ListScopedRoleMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### identitydirmgt user update-scoped-role-member-of

update-scoped-role-member-of a identitydirmgt user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|identitydirmgt user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-scoped-role-member-of|UpdateScopedRoleMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--id**|string|Read-only.|id|id|
|**--administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--role-member-info-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
