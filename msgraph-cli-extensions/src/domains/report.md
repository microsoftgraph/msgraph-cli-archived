# Azure CLI Module Creation Report

### domains domain create-service-configuration-record

create-service-configuration-record a domains domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-service-configuration-record|CreateServiceConfigurationRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: domain-id of domain|domain_id|domain-id|
|**--id**|string|Read-only.|id|id|
|**--is-optional**|boolean|If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.|is_optional|isOptional|
|**--label**|string|Value used when configuring the name of the DNS record at the DNS host.|label|label|
|**--record-type**|string|Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, TxtKey|record_type|recordType|
|**--supported-service**|string|Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune|supported_service|supportedService|
|**--ttl**|integer|Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable|ttl|ttl|

### domains domain create-verification-dns-record

create-verification-dns-record a domains domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-verification-dns-record|CreateVerificationDnsRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: domain-id of domain|domain_id|domain-id|
|**--id**|string|Read-only.|id|id|
|**--is-optional**|boolean|If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.|is_optional|isOptional|
|**--label**|string|Value used when configuring the name of the DNS record at the DNS host.|label|label|
|**--record-type**|string|Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, TxtKey|record_type|recordType|
|**--supported-service**|string|Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune|supported_service|supportedService|
|**--ttl**|integer|Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable|ttl|ttl|

### domains domain force-delete

force-delete a domains domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|force-delete|forceDelete|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: domain-id of domain|domain_id|domain-id|
|**--disable-user-accounts**|boolean||disable_user_accounts|disableUserAccounts|

### domains domain get-domain-name-reference

get-domain-name-reference a domains domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-domain-name-reference|GetDomainNameReferences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: domain-id of domain|domain_id|domain-id|
|**--directory-object-id**|string|key: directoryObject-id of directoryObject|directory_object_id|directoryObject-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### domains domain get-service-configuration-record

get-service-configuration-record a domains domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-service-configuration-record|GetServiceConfigurationRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: domain-id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: domainDnsRecord-id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### domains domain get-verification-dns-record

get-verification-dns-record a domains domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-verification-dns-record|GetVerificationDnsRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: domain-id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: domainDnsRecord-id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### domains domain list-domain-name-reference

list-domain-name-reference a domains domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-domain-name-reference|ListDomainNameReferences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: domain-id of domain|domain_id|domain-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### domains domain list-service-configuration-record

list-service-configuration-record a domains domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-service-configuration-record|ListServiceConfigurationRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: domain-id of domain|domain_id|domain-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### domains domain list-verification-dns-record

list-verification-dns-record a domains domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-verification-dns-record|ListVerificationDnsRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: domain-id of domain|domain_id|domain-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### domains domain update

update a domains domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateServiceConfigurationRecords|
|update|UpdateVerificationDnsRecords|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: domain-id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: domainDnsRecord-id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--id**|string|Read-only.|id|id|
|**--is-optional**|boolean|If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.|is_optional|isOptional|
|**--label**|string|Value used when configuring the name of the DNS record at the DNS host.|label|label|
|**--record-type**|string|Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, TxtKey|record_type|recordType|
|**--supported-service**|string|Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune|supported_service|supportedService|
|**--ttl**|integer|Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable|ttl|ttl|

### domains domain verify

verify a domains domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain|domains|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|verify|verify|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: domain-id of domain|domain_id|domain-id|

### domains domain-domain create-domain

create-domain a domains domain-domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain-domain|domains.domain|

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
|**--is-admin-managed**|boolean|The value of the property is false if the DNS record management of the domain has been delegated to Office 365. Otherwise, the value is true. Not nullable|is_admin_managed|isAdminManaged|
|**--is-default**|boolean|True if this is the default domain that is used for user creation. There is only one default domain per company. Not nullable|is_default|isDefault|
|**--is-initial**|boolean|True if this is the initial domain created by Microsoft Online Services (companyname.onmicrosoft.com). There is only one initial domain per company. Not nullable|is_initial|isInitial|
|**--is-root**|boolean|True if the domain is a verified root domain. Otherwise, false if the domain is a subdomain or unverified. Not nullable|is_root|isRoot|
|**--is-verified**|boolean|True if the domain has completed domain ownership verification. Not nullable|is_verified|isVerified|
|**--password-notification-window-in-days**|integer|Specifies the number of days before a user receives notification that their password will expire. If the property is not set, a default value of 14 days will be used.|password_notification_window_in_days|passwordNotificationWindowInDays|
|**--password-validity-period-in-days**|integer|Specifies the length of time that a password is valid before it must be changed. If the property is not set, a default value of 90 days will be used.|password_validity_period_in_days|passwordValidityPeriodInDays|
|**--supported-services**|array|The capabilities assigned to the domain.Can include 0, 1 or more of following values: Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune The values which you can add/remove using Graph API include: Email, OfficeCommunicationsOnline, YammerNot nullable|supported_services|supportedServices|
|**--state**|object|domainState|state|state|
|**--service-configuration-records**|array|DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services.Read-only, Nullable|service_configuration_records|serviceConfigurationRecords|
|**--verification-dns-records**|array|DNS records that the customer adds to the DNS zone file of the domain before the customer can complete domain ownership verification with Azure AD.Read-only, Nullable|verification_dns_records|verificationDnsRecords|
|**--domain-name-references**|array|Read-only, Nullable|domain_name_references|domainNameReferences|

### domains domain-domain delete

delete a domains domain-domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain-domain|domains.domain|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteDomain|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: domain-id of domain|domain_id|domain-id|
|**--if-match**|string|ETag|if_match|If-Match|

### domains domain-domain get-domain

get-domain a domains domain-domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain-domain|domains.domain|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-domain|GetDomain|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: domain-id of domain|domain_id|domain-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### domains domain-domain list-domain

list-domain a domains domain-domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain-domain|domains.domain|

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

### domains domain-domain update

update a domains domain-domain.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|domains domain-domain|domains.domain|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateDomain|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: domain-id of domain|domain_id|domain-id|
|**--id**|string|Read-only.|id|id|
|**--authentication-type**|string|Indicates the configured authentication type for the domain. The value is either Managed or Federated. Managed indicates a cloud managed domain where Azure AD performs user authentication.Federated indicates authentication is federated with an identity provider such as the tenant's on-premises Active Directory via Active Directory Federation Services. This property is read-only and is not nullable.|authentication_type|authenticationType|
|**--availability-status**|string|This property is always null except when the verify action is used. When the verify action is used, a domain entity is returned in the response. The availabilityStatus property of the domain entity in the response is either AvailableImmediately or EmailVerifiedDomainTakeoverScheduled.|availability_status|availabilityStatus|
|**--is-admin-managed**|boolean|The value of the property is false if the DNS record management of the domain has been delegated to Office 365. Otherwise, the value is true. Not nullable|is_admin_managed|isAdminManaged|
|**--is-default**|boolean|True if this is the default domain that is used for user creation. There is only one default domain per company. Not nullable|is_default|isDefault|
|**--is-initial**|boolean|True if this is the initial domain created by Microsoft Online Services (companyname.onmicrosoft.com). There is only one initial domain per company. Not nullable|is_initial|isInitial|
|**--is-root**|boolean|True if the domain is a verified root domain. Otherwise, false if the domain is a subdomain or unverified. Not nullable|is_root|isRoot|
|**--is-verified**|boolean|True if the domain has completed domain ownership verification. Not nullable|is_verified|isVerified|
|**--password-notification-window-in-days**|integer|Specifies the number of days before a user receives notification that their password will expire. If the property is not set, a default value of 14 days will be used.|password_notification_window_in_days|passwordNotificationWindowInDays|
|**--password-validity-period-in-days**|integer|Specifies the length of time that a password is valid before it must be changed. If the property is not set, a default value of 90 days will be used.|password_validity_period_in_days|passwordValidityPeriodInDays|
|**--supported-services**|array|The capabilities assigned to the domain.Can include 0, 1 or more of following values: Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune The values which you can add/remove using Graph API include: Email, OfficeCommunicationsOnline, YammerNot nullable|supported_services|supportedServices|
|**--state**|object|domainState|state|state|
|**--service-configuration-records**|array|DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services.Read-only, Nullable|service_configuration_records|serviceConfigurationRecords|
|**--verification-dns-records**|array|DNS records that the customer adds to the DNS zone file of the domain before the customer can complete domain ownership verification with Azure AD.Read-only, Nullable|verification_dns_records|verificationDnsRecords|
|**--domain-name-references**|array|Read-only, Nullable|domain_name_references|domainNameReferences|
