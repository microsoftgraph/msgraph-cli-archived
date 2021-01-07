# Azure CLI Module Creation Report

### users create-extension

create-extension a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

### users create-license-detail

create-license-detail a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-license-detail|CreateLicenseDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--service-plans**|array|Information about the service plans assigned with the license. Read-only, Not nullable|service_plans|servicePlans|
|**--sku-id**|uuid|Unique identifier (GUID) for the service SKU. Equal to the skuId property on the related SubscribedSku object. Read-only|sku_id|skuId|
|**--sku-part-number**|string|Unique SKU display name. Equal to the skuPartNumber on the related SubscribedSku object; for example: 'AAD_Premium'. Read-only|sku_part_number|skuPartNumber|

### users create-master-category

create-master-category a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-master-category|CreateMasterCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--color**|choice||color|color|
|**--display-name**|string|A unique name that identifies a category in the user's mailbox. After a category is created, the name cannot be changed. Read-only.|display_name|displayName|

### users create-photo

create-photo a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-photo|CreatePhotos|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--height**|integer|The height of the photo. Read-only.|height|height|
|**--width**|integer|The width of the photo. Read-only.|width|width|

### users create-ref-created-object

create-ref-created-object a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-created-object|CreateRefCreatedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users create-ref-direct-report

create-ref-direct-report a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-direct-report|CreateRefDirectReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users create-ref-member-of

create-ref-member-of a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-member-of|CreateRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users create-ref-oauth2-permission-grant

create-ref-oauth2-permission-grant a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-oauth2-permission-grant|CreateRefOauth2PermissionGrants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users create-ref-owned-device

create-ref-owned-device a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-owned-device|CreateRefOwnedDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users create-ref-owned-object

create-ref-owned-object a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-owned-object|CreateRefOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users create-ref-registered-device

create-ref-registered-device a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-registered-device|CreateRefRegisteredDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users create-ref-transitive-member-of

create-ref-transitive-member-of a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-transitive-member-of|CreateRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users create-user

create-user a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-user|CreateUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New entity|body|body|

### users delete

delete a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteShiftPreferences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users get-extension

get-extension a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users get-license-detail

get-license-detail a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-license-detail|GetLicenseDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--license-details-id**|string|key: id of licenseDetails|license_details_id|licenseDetails-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users get-manager

get-manager a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-manager|GetManager|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users get-master-category

get-master-category a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-master-category|GetMasterCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-category-id**|string|key: id of outlookCategory|outlook_category_id|outlookCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users get-outlook

get-outlook a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-outlook|GetOutlook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users get-photo

get-photo a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-photo|GetPhotos|
|get-photo|GetPhoto|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users get-ref-manager

get-ref-manager a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-manager|GetRefManager|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|

### users get-setting

get-setting a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-setting|GetSettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users get-shift-preference

get-shift-preference a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shift-preference|GetShiftPreferences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users get-user

get-user a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user|GetUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users list-created-object

list-created-object a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-created-object|ListCreatedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users list-direct-report

list-direct-report a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-direct-report|ListDirectReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users list-extension

list-extension a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users list-license-detail

list-license-detail a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-license-detail|ListLicenseDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users list-master-category

list-master-category a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-master-category|ListMasterCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users list-member-of

list-member-of a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member-of|ListMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users list-oauth2-permission-grant

list-oauth2-permission-grant a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-oauth2-permission-grant|ListOauth2PermissionGrants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users list-owned-device

list-owned-device a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-owned-device|ListOwnedDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users list-owned-object

list-owned-object a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-owned-object|ListOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users list-photo

list-photo a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-photo|ListPhotos|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users list-ref-created-object

list-ref-created-object a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-created-object|ListRefCreatedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users list-ref-direct-report

list-ref-direct-report a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-direct-report|ListRefDirectReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users list-ref-member-of

list-ref-member-of a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-member-of|ListRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users list-ref-oauth2-permission-grant

list-ref-oauth2-permission-grant a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-oauth2-permission-grant|ListRefOauth2PermissionGrants|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users list-ref-owned-device

list-ref-owned-device a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-owned-device|ListRefOwnedDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users list-ref-owned-object

list-ref-owned-object a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-owned-object|ListRefOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users list-ref-registered-device

list-ref-registered-device a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-registered-device|ListRefRegisteredDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users list-ref-transitive-member-of

list-ref-transitive-member-of a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-transitive-member-of|ListRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users list-registered-device

list-registered-device a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-registered-device|ListRegisteredDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users list-transitive-member-of

list-transitive-member-of a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-transitive-member-of|ListTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users list-user

list-user a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-user|ListUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users set-ref-manager

set-ref-manager a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-manager|SetRefManager|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### users update-extension

update-extension a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### users update-license-detail

update-license-detail a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-license-detail|UpdateLicenseDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--license-details-id**|string|key: id of licenseDetails|license_details_id|licenseDetails-id|
|**--id**|string|Read-only.|id|id|
|**--service-plans**|array|Information about the service plans assigned with the license. Read-only, Not nullable|service_plans|servicePlans|
|**--sku-id**|uuid|Unique identifier (GUID) for the service SKU. Equal to the skuId property on the related SubscribedSku object. Read-only|sku_id|skuId|
|**--sku-part-number**|string|Unique SKU display name. Equal to the skuPartNumber on the related SubscribedSku object; for example: 'AAD_Premium'. Read-only|sku_part_number|skuPartNumber|

### users update-master-category

update-master-category a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-master-category|UpdateMasterCategories|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-category-id**|string|key: id of outlookCategory|outlook_category_id|outlookCategory-id|
|**--id**|string|Read-only.|id|id|
|**--color**|choice||color|color|
|**--display-name**|string|A unique name that identifies a category in the user's mailbox. After a category is created, the name cannot be changed. Read-only.|display_name|displayName|

### users update-outlook

update-outlook a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-outlook|UpdateOutlook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--master-categories**|array|A list of categories defined for the user.|master_categories|masterCategories|

### users update-photo

update-photo a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-photo|UpdatePhotos|
|update-photo|UpdatePhoto|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|
|**--id**|string|Read-only.|id|id|
|**--height**|integer|The height of the photo. Read-only.|height|height|
|**--width**|integer|The width of the photo. Read-only.|width|width|

### users update-setting

update-setting a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-setting|UpdateSettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--contribution-to-content-discovery-as-organization-disabled**|boolean||contribution_to_content_discovery_as_organization_disabled|contributionToContentDiscoveryAsOrganizationDisabled|
|**--contribution-to-content-discovery-disabled**|boolean||contribution_to_content_discovery_disabled|contributionToContentDiscoveryDisabled|
|**--shift-preferences-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--shift-preferences-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--shift-preferences-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--shift-preferences-last-modified-by-application**|object|identity|application|application|
|**--shift-preferences-last-modified-by-device**|object|identity|device|device|
|**--shift-preferences-last-modified-by-user**|object|identity|user|user|
|**--shift-preferences-availability**|array|Availability of the user to be scheduled for work and its recurrence pattern.|availability|availability|

### users update-shift-preference

update-shift-preference a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shift-preference|UpdateShiftPreferences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-application**|object|identity|application|application|
|**--last-modified-by-device**|object|identity|device|device|
|**--last-modified-by-user**|object|identity|user|user|
|**--availability**|array|Availability of the user to be scheduled for work and its recurrence pattern.|availability|availability|

### users update-user

update-user a users.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-user|UpdateUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|object|New property values|body|body|
