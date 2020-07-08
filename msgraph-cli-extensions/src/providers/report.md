# Azure CLI Module Creation Report

### providers identity-provider-identity-provider create-identity-provider

create-identity-provider a providers identity-provider-identity-provider.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|providers identity-provider-identity-provider|identityProviders.identityProvider|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-identity-provider|CreateIdentityProvider|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--type**|string||type|type|
|**--name**|string||name|name|
|**--client-id**|string||client_id|clientId|
|**--client-secret**|string||client_secret|clientSecret|

### providers identity-provider-identity-provider delete

delete a providers identity-provider-identity-provider.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|providers identity-provider-identity-provider|identityProviders.identityProvider|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteIdentityProvider|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-provider-id**|string|key: identityProvider-id of identityProvider|identity_provider_id|identityProvider-id|
|**--if-match**|string|ETag|if_match|If-Match|

### providers identity-provider-identity-provider get-identity-provider

get-identity-provider a providers identity-provider-identity-provider.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|providers identity-provider-identity-provider|identityProviders.identityProvider|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-identity-provider|GetIdentityProvider|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-provider-id**|string|key: identityProvider-id of identityProvider|identity_provider_id|identityProvider-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### providers identity-provider-identity-provider list-identity-provider

list-identity-provider a providers identity-provider-identity-provider.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|providers identity-provider-identity-provider|identityProviders.identityProvider|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-identity-provider|ListIdentityProvider|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### providers identity-provider-identity-provider update

update a providers identity-provider-identity-provider.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|providers identity-provider-identity-provider|identityProviders.identityProvider|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateIdentityProvider|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-provider-id**|string|key: identityProvider-id of identityProvider|identity_provider_id|identityProvider-id|
|**--id**|string|Read-only.|id|id|
|**--type**|string||type|type|
|**--name**|string||name|name|
|**--client-id**|string||client_id|clientId|
|**--client-secret**|string||client_secret|clientSecret|
