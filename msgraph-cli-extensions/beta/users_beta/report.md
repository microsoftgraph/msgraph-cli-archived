# Azure CLI Module Creation Report

### users user create

create a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New entity|body|body|

### users user create-extension

create-extension a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

### users user create-license-detail

create-license-detail a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user create-notification

create-notification a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-notification|CreateNotifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--display-time-to-live**|integer||display_time_to_live|displayTimeToLive|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--group-name**|string||group_name|groupName|
|**--priority**|choice||priority|priority|
|**--target-host-name**|string||target_host_name|targetHostName|
|**--target-policy**|object|targetPolicyEndpoints|target_policy|targetPolicy|
|**--payload-raw-content**|string||raw_content|rawContent|
|**--payload-visual-content**|object|visualProperties|visual_content|visualContent|

### users user create-photo

create-photo a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user create-ref-created-object

create-ref-created-object a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-created-object|CreateRefCreatedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users user create-ref-direct-report

create-ref-direct-report a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-direct-report|CreateRefDirectReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users user create-ref-member-of

create-ref-member-of a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-member-of|CreateRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users user create-ref-owned-device

create-ref-owned-device a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-owned-device|CreateRefOwnedDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users user create-ref-owned-object

create-ref-owned-object a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-owned-object|CreateRefOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users user create-ref-registered-device

create-ref-registered-device a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-registered-device|CreateRefRegisteredDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users user create-ref-transitive-member-of

create-ref-transitive-member-of a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-transitive-member-of|CreateRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### users user delete

delete a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteExtensions|
|delete|DeleteLicenseDetails|
|delete|DeleteNotifications|
|delete|DeletePhotos|
|delete|DeleteRefManager|
|delete|DeleteOutlook|
|delete|DeletePhoto|
|delete|DeleteSettings|
|delete|DeleteTodo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--license-details-id**|string|key: id of licenseDetails|license_details_id|licenseDetails-id|
|**--notification-id**|string|key: id of notification|notification_id|notification-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user get

get a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--consistency-level**|string|Indicates the requested consistency level.|consistency_level|ConsistencyLevel|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user get-extension

get-extension a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user get-license-detail

get-license-detail a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user get-manager

get-manager a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user get-notification

get-notification a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-notification|GetNotifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notification-id**|string|key: id of notification|notification_id|notification-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user get-outlook

get-outlook a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user get-photo

get-photo a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user get-photo-content

get-photo-content a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-photo-content|GetPhotosContent|
|get-photo-content|GetPhotoContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|

### users user get-ref-manager

get-ref-manager a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-manager|GetRefManager|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|

### users user get-setting

get-setting a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user get-todo

get-todo a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-todo|GetTodo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user list

list a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--consistency-level**|string|Indicates the requested consistency level.|consistency_level|ConsistencyLevel|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user list-created-object

list-created-object a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user list-direct-report

list-direct-report a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user list-extension

list-extension a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user list-license-detail

list-license-detail a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user list-member-of

list-member-of a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user list-notification

list-notification a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-notification|ListNotifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user list-owned-device

list-owned-device a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user list-owned-object

list-owned-object a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user list-photo

list-photo a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user list-ref-created-object

list-ref-created-object a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-created-object|ListRefCreatedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users user list-ref-direct-report

list-ref-direct-report a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-direct-report|ListRefDirectReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users user list-ref-member-of

list-ref-member-of a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-member-of|ListRefMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users user list-ref-owned-device

list-ref-owned-device a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-owned-device|ListRefOwnedDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users user list-ref-owned-object

list-ref-owned-object a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-owned-object|ListRefOwnedObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users user list-ref-registered-device

list-ref-registered-device a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-registered-device|ListRefRegisteredDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users user list-ref-transitive-member-of

list-ref-transitive-member-of a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-transitive-member-of|ListRefTransitiveMemberOf|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### users user list-registered-device

list-registered-device a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user list-transitive-member-of

list-transitive-member-of a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user set-photo-content

set-photo-content a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-photo-content|SetPhotosContent|
|set-photo-content|SetPhotoContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|
|**--data**|binary|New media content.|data|data|

### users user set-ref-manager

set-ref-manager a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-manager|SetRefManager|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### users user update

update a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users.user|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|object|New property values|body|body|

### users user update-extension

update-extension a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user update-license-detail

update-license-detail a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user update-notification

update-notification a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-notification|UpdateNotifications|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--notification-id**|string|key: id of notification|notification_id|notification-id|
|**--id**|string|Read-only.|id|id|
|**--display-time-to-live**|integer||display_time_to_live|displayTimeToLive|
|**--expiration-date-time**|date-time||expiration_date_time|expirationDateTime|
|**--group-name**|string||group_name|groupName|
|**--priority**|choice||priority|priority|
|**--target-host-name**|string||target_host_name|targetHostName|
|**--target-policy**|object|targetPolicyEndpoints|target_policy|targetPolicy|
|**--payload-raw-content**|string||raw_content|rawContent|
|**--payload-visual-content**|object|visualProperties|visual_content|visualContent|

### users user update-outlook

update-outlook a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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
|**--task-folders**|array||task_folders|taskFolders|
|**--task-groups**|array||task_groups|taskGroups|
|**--tasks**|array||tasks|tasks|

### users user update-photo

update-photo a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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

### users user update-setting

update-setting a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

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
|**--shift-preferences-created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--shift-preferences-created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--shift-preferences-created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--shift-preferences-availability**|array|Availability of the user to be scheduled for work and its recurrence pattern.|availability|availability|
|**--regional-and-language-settings-id**|string|Read-only.|id1|id|
|**--regional-and-language-settings-authoring-languages**|array||authoring_languages|authoringLanguages|
|**--regional-and-language-settings-default-display-language**|object|localeInfo|default_display_language|defaultDisplayLanguage|
|**--regional-and-language-settings-default-regional-format**|object|localeInfo|default_regional_format|defaultRegionalFormat|
|**--regional-and-language-settings-default-speech-input-language**|object|localeInfo|default_speech_input_language|defaultSpeechInputLanguage|
|**--regional-and-language-settings-default-translation-language**|object|localeInfo|default_translation_language|defaultTranslationLanguage|
|**--regional-and-language-settings-regional-format-overrides**|object|regionalFormatOverrides|regional_format_overrides|regionalFormatOverrides|

### users user update-todo

update-todo a users user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-todo|UpdateTodo|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--lists**|array||lists|lists|

### users user-outlook create-master-category

create-master-category a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

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

### users user-outlook create-task

create-task a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice||status|status|
|**--subject**|string||subject|subject|
|**--attachments**|array||attachments|attachments|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-outlook create-task-folder

create-task-folder a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task-folder|CreateTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--is-default-folder**|boolean||is_default_folder|isDefaultFolder|
|**--name**|string||name|name|
|**--parent-group-key**|uuid||parent_group_key|parentGroupKey|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--tasks**|array||tasks|tasks|

### users user-outlook create-task-group

create-task-group a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task-group|CreateTaskGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--group-key**|uuid||group_key|groupKey|
|**--is-default-group**|boolean||is_default_group|isDefaultGroup|
|**--name**|string||name|name|
|**--task-folders**|array||task_folders|taskFolders|

### users user-outlook delete

delete a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteMasterCategories|
|delete|DeleteTaskFolders|
|delete|DeleteTaskGroups|
|delete|DeleteTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-category-id**|string|key: id of outlookCategory|outlook_category_id|outlookCategory-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-outlook get-master-category

get-master-category a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

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

### users user-outlook get-task

get-task a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook get-task-folder

get-task-folder a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task-folder|GetTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook get-task-group

get-task-group a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task-group|GetTaskGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook list-master-category

list-master-category a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

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

### users user-outlook list-task

list-task a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook list-task-folder

list-task-folder a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task-folder|ListTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook list-task-group

list-task-group a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task-group|ListTaskGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook update-master-category

update-master-category a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

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

### users user-outlook update-task

update-task a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice||status|status|
|**--subject**|string||subject|subject|
|**--attachments**|array||attachments|attachments|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-outlook update-task-folder

update-task-folder a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task-folder|UpdateTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--is-default-folder**|boolean||is_default_folder|isDefaultFolder|
|**--name**|string||name|name|
|**--parent-group-key**|uuid||parent_group_key|parentGroupKey|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--tasks**|array||tasks|tasks|

### users user-outlook update-task-group

update-task-group a users user-outlook.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook|users.outlook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task-group|UpdateTaskGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--group-key**|uuid||group_key|groupKey|
|**--is-default-group**|boolean||is_default_group|isDefaultGroup|
|**--name**|string||name|name|
|**--task-folders**|array||task_folders|taskFolders|

### users user-outlook-task create-attachment

create-attachment a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### users user-outlook-task create-multi-value-extended-property

create-multi-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task create-single-value-extended-property

create-single-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task delete

delete a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-outlook-task get-attachment

get-attachment a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task get-multi-value-extended-property

get-multi-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task get-single-value-extended-property

get-single-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task list-attachment

list-attachment a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task list-multi-value-extended-property

list-multi-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task list-single-value-extended-property

list-single-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task update-attachment

update-attachment a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-attachment|UpdateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### users user-outlook-task update-multi-value-extended-property

update-multi-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task update-single-value-extended-property

update-single-value-extended-property a users user-outlook-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task|users.outlook.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-folder create-multi-value-extended-property

create-multi-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-folder create-single-value-extended-property

create-single-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-folder create-task

create-task a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice||status|status|
|**--subject**|string||subject|subject|
|**--attachments**|array||attachments|attachments|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-outlook-task-folder delete

delete a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|
|delete|DeleteTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-outlook-task-folder get-multi-value-extended-property

get-multi-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder get-single-value-extended-property

get-single-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder get-task

get-task a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder list-multi-value-extended-property

list-multi-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder list-single-value-extended-property

list-single-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder list-task

list-task a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder update-multi-value-extended-property

update-multi-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-folder update-single-value-extended-property

update-single-value-extended-property a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-folder update-task

update-task a users user-outlook-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder|users.outlook.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice||status|status|
|**--subject**|string||subject|subject|
|**--attachments**|array||attachments|attachments|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-outlook-task-folder-task create-attachment

create-attachment a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### users user-outlook-task-folder-task create-multi-value-extended-property

create-multi-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-folder-task create-single-value-extended-property

create-single-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-folder-task delete

delete a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-outlook-task-folder-task get-attachment

get-attachment a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder-task get-multi-value-extended-property

get-multi-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder-task get-single-value-extended-property

get-single-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder-task list-attachment

list-attachment a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder-task list-multi-value-extended-property

list-multi-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder-task list-single-value-extended-property

list-single-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-folder-task update-attachment

update-attachment a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-attachment|UpdateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### users user-outlook-task-folder-task update-multi-value-extended-property

update-multi-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-folder-task update-single-value-extended-property

update-single-value-extended-property a users user-outlook-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-folder-task|users.outlook.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-group create-task-folder

create-task-folder a users user-outlook-task-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group|users.outlook.taskGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task-folder|CreateTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--is-default-folder**|boolean||is_default_folder|isDefaultFolder|
|**--name**|string||name|name|
|**--parent-group-key**|uuid||parent_group_key|parentGroupKey|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--tasks**|array||tasks|tasks|

### users user-outlook-task-group delete

delete a users user-outlook-task-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group|users.outlook.taskGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-outlook-task-group get-task-folder

get-task-folder a users user-outlook-task-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group|users.outlook.taskGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task-folder|GetTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group list-task-folder

list-task-folder a users user-outlook-task-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group|users.outlook.taskGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task-folder|ListTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group update-task-folder

update-task-folder a users user-outlook-task-group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group|users.outlook.taskGroups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task-folder|UpdateTaskFolders|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string||change_key|changeKey|
|**--is-default-folder**|boolean||is_default_folder|isDefaultFolder|
|**--name**|string||name|name|
|**--parent-group-key**|uuid||parent_group_key|parentGroupKey|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--tasks**|array||tasks|tasks|

### users user-outlook-task-group-task-folder create-multi-value-extended-property

create-multi-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-group-task-folder create-single-value-extended-property

create-single-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-group-task-folder create-task

create-task a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice||status|status|
|**--subject**|string||subject|subject|
|**--attachments**|array||attachments|attachments|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-outlook-task-group-task-folder delete

delete a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|
|delete|DeleteTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-outlook-task-group-task-folder get-multi-value-extended-property

get-multi-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder get-single-value-extended-property

get-single-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder get-task

get-task a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder list-multi-value-extended-property

list-multi-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder list-single-value-extended-property

list-single-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder list-task

list-task a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder update-multi-value-extended-property

update-multi-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-group-task-folder update-single-value-extended-property

update-single-value-extended-property a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-group-task-folder update-task

update-task a users user-outlook-task-group-task-folder.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder|users.outlook.taskGroups.taskFolders|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--assigned-to**|string||assigned_to|assignedTo|
|**--body**|object|itemBody|body|body|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--has-attachments**|boolean||has_attachments|hasAttachments|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--owner**|string||owner|owner|
|**--parent-folder-id**|string||parent_folder_id|parentFolderId|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--sensitivity**|choice||sensitivity|sensitivity|
|**--start-date-time**|object|dateTimeTimeZone|start_date_time|startDateTime|
|**--status**|choice||status|status|
|**--subject**|string||subject|subject|
|**--attachments**|array||attachments|attachments|
|**--multi-value-extended-properties**|array||multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array||single_value_extended_properties|singleValueExtendedProperties|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-outlook-task-group-task-folder-task create-attachment

create-attachment a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-attachment|CreateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### users user-outlook-task-group-task-folder-task create-multi-value-extended-property

create-multi-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-multi-value-extended-property|CreateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-group-task-folder-task create-single-value-extended-property

create-single-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-single-value-extended-property|CreateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-outlook-task-group-task-folder-task delete

delete a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAttachments|
|delete|DeleteMultiValueExtendedProperties|
|delete|DeleteSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-outlook-task-group-task-folder-task get-attachment

get-attachment a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-attachment|GetAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder-task get-multi-value-extended-property

get-multi-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-multi-value-extended-property|GetMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder-task get-single-value-extended-property

get-single-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-single-value-extended-property|GetSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder-task list-attachment

list-attachment a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-attachment|ListAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder-task list-multi-value-extended-property

list-multi-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-multi-value-extended-property|ListMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder-task list-single-value-extended-property

list-single-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-single-value-extended-property|ListSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-outlook-task-group-task-folder-task update-attachment

update-attachment a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-attachment|UpdateAttachments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

### users user-outlook-task-group-task-folder-task update-multi-value-extended-property

update-multi-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-multi-value-extended-property|UpdateMultiValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

### users user-outlook-task-group-task-folder-task update-single-value-extended-property

update-single-value-extended-property a users user-outlook-task-group-task-folder-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-outlook-task-group-task-folder-task|users.outlook.taskGroups.taskFolders.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-single-value-extended-property|UpdateSingleValueExtendedProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--outlook-task-group-id**|string|key: id of outlookTaskGroup|outlook_task_group_id|outlookTaskGroup-id|
|**--outlook-task-folder-id**|string|key: id of outlookTaskFolder|outlook_task_folder_id|outlookTaskFolder-id|
|**--outlook-task-id**|string|key: id of outlookTask|outlook_task_id|outlookTask-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### users user-setting delete

delete a users user-setting.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-setting|users.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRegionalAndLanguageSettings|
|delete|DeleteShiftPreferences|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-setting get-regional-and-language-setting

get-regional-and-language-setting a users user-setting.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-setting|users.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-regional-and-language-setting|GetRegionalAndLanguageSettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-setting get-shift-preference

get-shift-preference a users user-setting.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-setting|users.settings|

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

### users user-setting update-regional-and-language-setting

update-regional-and-language-setting a users user-setting.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-setting|users.settings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-regional-and-language-setting|UpdateRegionalAndLanguageSettings|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--authoring-languages**|array||authoring_languages|authoringLanguages|
|**--default-display-language**|object|localeInfo|default_display_language|defaultDisplayLanguage|
|**--default-regional-format**|object|localeInfo|default_regional_format|defaultRegionalFormat|
|**--default-speech-input-language**|object|localeInfo|default_speech_input_language|defaultSpeechInputLanguage|
|**--default-translation-language**|object|localeInfo|default_translation_language|defaultTranslationLanguage|
|**--regional-format-overrides**|object|regionalFormatOverrides|regional_format_overrides|regionalFormatOverrides|

### users user-setting update-shift-preference

update-shift-preference a users user-setting.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-setting|users.settings|

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
|**--created-by-application**|object|identity|microsoft_graph_identity_application|application|
|**--created-by-device**|object|identity|microsoft_graph_identity_device|device|
|**--created-by-user**|object|identity|microsoft_graph_identity_user|user|
|**--availability**|array|Availability of the user to be scheduled for work and its recurrence pattern.|availability|availability|

### users user-todo create-list

create-list a users user-todo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo|users.todo|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-list|CreateLists|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--is-owner**|boolean||is_owner|isOwner|
|**--is-shared**|boolean||is_shared|isShared|
|**--wellknown-list-name**|choice||wellknown_list_name|wellknownListName|
|**--extensions**|array||extensions|extensions|
|**--tasks**|array||tasks|tasks|

### users user-todo delete

delete a users user-todo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo|users.todo|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteLists|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-todo get-list

get-list a users user-todo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo|users.todo|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-list|GetLists|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo list-list

list-list a users user-todo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo|users.todo|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-list|ListLists|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo update-list

update-list a users user-todo.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo|users.todo|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-list|UpdateLists|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--is-owner**|boolean||is_owner|isOwner|
|**--is-shared**|boolean||is_shared|isShared|
|**--wellknown-list-name**|choice||wellknown_list_name|wellknownListName|
|**--extensions**|array||extensions|extensions|
|**--tasks**|array||tasks|tasks|

### users user-todo-list create-extension

create-extension a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--id**|string|Read-only.|id|id|

### users user-todo-list create-task

create-task a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--id**|string|Read-only.|id|id|
|**--body**|object|itemBody|body|body|
|**--body-last-modified-date-time**|date-time||body_last_modified_date_time|bodyLastModifiedDateTime|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--status**|choice||status|status|
|**--title**|string||title|title|
|**--extensions**|array||extensions|extensions|
|**--linked-resources**|array||linked_resources|linkedResources|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-todo-list delete

delete a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteExtensions|
|delete|DeleteTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-todo-list get-extension

get-extension a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list get-task

get-task a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list list-extension

list-extension a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list list-task

list-task a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list update-extension

update-extension a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### users user-todo-list update-task

update-task a users user-todo-list.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list|users.todo.lists|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--id**|string|Read-only.|id|id|
|**--body**|object|itemBody|body|body|
|**--body-last-modified-date-time**|date-time||body_last_modified_date_time|bodyLastModifiedDateTime|
|**--completed-date-time**|object|dateTimeTimeZone|completed_date_time|completedDateTime|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--due-date-time**|object|dateTimeTimeZone|due_date_time|dueDateTime|
|**--importance**|choice||importance|importance|
|**--is-reminder-on**|boolean||is_reminder_on|isReminderOn|
|**--last-modified-date-time**|date-time||last_modified_date_time|lastModifiedDateTime|
|**--reminder-date-time**|object|dateTimeTimeZone|reminder_date_time|reminderDateTime|
|**--status**|choice||status|status|
|**--title**|string||title|title|
|**--extensions**|array||extensions|extensions|
|**--linked-resources**|array||linked_resources|linkedResources|
|**--recurrence-pattern**|object|recurrencePattern|pattern|pattern|
|**--recurrence-range**|object|recurrenceRange|range|range|

### users user-todo-list-task create-extension

create-extension a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-extension|CreateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--id**|string|Read-only.|id|id|

### users user-todo-list-task create-linked-resource

create-linked-resource a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-linked-resource|CreateLinkedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--id**|string|Read-only.|id|id|
|**--application-name**|string||application_name|applicationName|
|**--display-name**|string||display_name|displayName|
|**--external-id**|string||external_id|externalId|
|**--web-url**|string||web_url|webUrl|

### users user-todo-list-task delete

delete a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteExtensions|
|delete|DeleteLinkedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--linked-resource-id**|string|key: id of linkedResource|linked_resource_id|linkedResource-id|
|**--if-match**|string|ETag|if_match|If-Match|

### users user-todo-list-task get-extension

get-extension a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-extension|GetExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list-task get-linked-resource

get-linked-resource a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-linked-resource|GetLinkedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--linked-resource-id**|string|key: id of linkedResource|linked_resource_id|linkedResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list-task list-extension

list-extension a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-extension|ListExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list-task list-linked-resource

list-linked-resource a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-linked-resource|ListLinkedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### users user-todo-list-task update-extension

update-extension a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-extension|UpdateExtensions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

### users user-todo-list-task update-linked-resource

update-linked-resource a users user-todo-list-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|users user-todo-list-task|users.todo.lists.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-linked-resource|UpdateLinkedResources|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--todo-task-list-id**|string|key: id of todoTaskList|todo_task_list_id|todoTaskList-id|
|**--todo-task-id**|string|key: id of todoTask|todo_task_id|todoTask-id|
|**--linked-resource-id**|string|key: id of linkedResource|linked_resource_id|linkedResource-id|
|**--id**|string|Read-only.|id|id|
|**--application-name**|string||application_name|applicationName|
|**--display-name**|string||display_name|displayName|
|**--external-id**|string||external_id|externalId|
|**--web-url**|string||web_url|webUrl|
