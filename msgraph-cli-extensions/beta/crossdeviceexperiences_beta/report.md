# Azure CLI Module Creation Report

### crossdeviceexperiences user create-activity

create-activity a crossdeviceexperiences user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-activity|CreateActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--activation-url**|string|Required. URL used to launch the activity in the best native experience represented by the appId. Might launch a web-based app if no native app exists.|activation_url|activationUrl|
|**--activity-source-host**|string|Required. URL for the domain representing the cross-platform identity mapping for the app. Mapping is stored either as a JSON file hosted on the domain or configurable via Windows Dev Center. The JSON file is named cross-platform-app-identifiers and is hosted at root of your HTTPS domain, either at the top level domain or include a sub domain. For example: https://contoso.com or https://myapp.contoso.com but NOT https://myapp.contoso.com/somepath. You must have a unique file and domain (or sub domain) per cross-platform app identity. For example, a separate file and domain is needed for Word vs. PowerPoint.|activity_source_host|activitySourceHost|
|**--app-activity-id**|string|Required. The unique activity ID in the context of the app - supplied by caller and immutable thereafter.|app_activity_id|appActivityId|
|**--app-display-name**|string|Optional. Short text description of the app used to generate the activity for use in cases when the app is not installed on the user’s local device.|app_display_name|appDisplayName|
|**--content-info**|dictionary|Json|content_info|contentInfo|
|**--content-url**|string|Optional. Used in the event the content can be rendered outside of a native or web-based app experience (for example, a pointer to an item in an RSS feed).|content_url|contentUrl|
|**--created-date-time**|date-time|Set by the server. DateTime in UTC when the object was created on the server.|created_date_time|createdDateTime|
|**--expiration-date-time**|date-time|Set by the server. DateTime in UTC when the object expired on the server.|expiration_date_time|expirationDateTime|
|**--fallback-url**|string|Optional. URL used to launch the activity in a web-based app, if available.|fallback_url|fallbackUrl|
|**--last-modified-date-time**|date-time|Set by the server. DateTime in UTC when the object was modified on the server.|last_modified_date_time|lastModifiedDateTime|
|**--status**|choice||status|status|
|**--user-timezone**|string|Optional. The timezone in which the user's device used to generate the activity was located at activity creation time; values supplied as Olson IDs in order to support cross-platform representation.|user_timezone|userTimezone|
|**--history-items**|array|Optional. NavigationProperty/Containment; navigation property to the activity's historyItems.|history_items|historyItems|
|**--visual-elements-attribution**|object|imageInfo|attribution|attribution|
|**--visual-elements-background-color**|string|Optional. Background color used to render the activity in the UI - brand color for the application source of the activity. Must be a valid hex color|background_color|backgroundColor|
|**--visual-elements-content**|dictionary|Json|content|content|
|**--visual-elements-description**|string|Optional. Longer text description of the user's unique activity (example: document name, first sentence, and/or metadata)|description|description|
|**--visual-elements-display-text**|string|Required. Short text description of the user's unique activity (for example, document name in cases where an activity refers to document creation)|display_text|displayText|

### crossdeviceexperiences user create-device

create-device a crossdeviceexperiences user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-device|CreateDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--account-enabled**|boolean|true if the account is enabled; otherwise, false. Required.|account_enabled|accountEnabled|
|**--alternative-security-ids**|array|For internal use only. Not nullable.|alternative_security_ids|alternativeSecurityIds|
|**--approximate-last-sign-in-date-time**|date-time|The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|approximate_last_sign_in_date_time|approximateLastSignInDateTime|
|**--compliance-expiration-date-time**|date-time|The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|compliance_expiration_date_time|complianceExpirationDateTime|
|**--device-category**|string||device_category|deviceCategory|
|**--device-id**|string|Unique identifier set by Azure Device Registration Service at the time of registration.|device_id|deviceId|
|**--device-metadata**|string|For internal use only. Set to null.|device_metadata|deviceMetadata|
|**--device-ownership**|string||device_ownership|deviceOwnership|
|**--device-version**|integer|For internal use only.|device_version|deviceVersion|
|**--display-name**|string|The display name for the device. Required.|display_name|displayName|
|**--domain-name**|string||domain_name|domainName|
|**--enrollment-profile-name**|string||enrollment_profile_name|enrollmentProfileName|
|**--enrollment-type**|string||enrollment_type|enrollmentType|
|**--extension-attributes**|object|onPremisesExtensionAttributes|extension_attributes|extensionAttributes|
|**--is-compliant**|boolean|true if the device complies with Mobile Device Management (MDM) policies; otherwise, false. Read-only. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices.|is_compliant|isCompliant|
|**--is-managed**|boolean|true if the device is managed by a Mobile Device Management (MDM) app; otherwise, false. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices.|is_managed|isManaged|
|**--is-rooted**|boolean||is_rooted|isRooted|
|**--management-type**|string||management_type|managementType|
|**--on-premises-last-sync-date-time**|date-time|The last time at which the object was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z' Read-only.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-sync-enabled**|boolean|true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--operating-system**|string|The type of operating system on the device. Required.|operating_system|operatingSystem|
|**--operating-system-version**|string|The version of the operating system on the device. Required.|operating_system_version|operatingSystemVersion|
|**--physical-ids**|array|For internal use only. Not nullable.|physical_ids|physicalIds|
|**--profile-type**|string|The profile type of the device. Possible values:RegisteredDevice (default)SecureVMPrinterSharedIoT|profile_type|profileType|
|**--registration-date-time**|date-time||registration_date_time|registrationDateTime|
|**--system-labels**|array|List of labels applied to the device by the system.|system_labels|systemLabels|
|**--trust-type**|string|Type of trust for the joined device. Read-only. Possible values: Workplace - indicates bring your own personal devicesAzureAd - Cloud only joined devicesServerAd - on-premises domain joined devices joined to Azure AD. For more details, see Introduction to device management in Azure Active Directory|trust_type|trustType|
|**--kind**|string||kind|kind|
|**--manufacturer**|string|Manufacturer of the device. Read-only.|manufacturer|manufacturer|
|**--model**|string|Model of the device. Read-only.|model|model|
|**--name**|string||name|name|
|**--platform**|string||platform|platform|
|**--status**|string||status|status|
|**--member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--registered-owners**|array|The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Currently, there can be only one owner. Read-only. Nullable.|registered_owners|registeredOwners|
|**--registered-users**|array|Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable.|registered_users|registeredUsers|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--extensions**|array|The collection of open extensions defined for the device. Read-only. Nullable.|extensions|extensions|
|**--commands**|array||commands|commands|

### crossdeviceexperiences user delete

delete a crossdeviceexperiences user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteActivities|
|delete|DeleteDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--if-match**|string|ETag|if_match|If-Match|

### crossdeviceexperiences user get-activity

get-activity a crossdeviceexperiences user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity|GetActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### crossdeviceexperiences user get-device

get-device a crossdeviceexperiences user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-device|GetDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### crossdeviceexperiences user list-activity

list-activity a crossdeviceexperiences user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-activity|ListActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### crossdeviceexperiences user list-device

list-device a crossdeviceexperiences user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-device|ListDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### crossdeviceexperiences user update-activity

update-activity a crossdeviceexperiences user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-activity|UpdateActivities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--id**|string|Read-only.|id|id|
|**--activation-url**|string|Required. URL used to launch the activity in the best native experience represented by the appId. Might launch a web-based app if no native app exists.|activation_url|activationUrl|
|**--activity-source-host**|string|Required. URL for the domain representing the cross-platform identity mapping for the app. Mapping is stored either as a JSON file hosted on the domain or configurable via Windows Dev Center. The JSON file is named cross-platform-app-identifiers and is hosted at root of your HTTPS domain, either at the top level domain or include a sub domain. For example: https://contoso.com or https://myapp.contoso.com but NOT https://myapp.contoso.com/somepath. You must have a unique file and domain (or sub domain) per cross-platform app identity. For example, a separate file and domain is needed for Word vs. PowerPoint.|activity_source_host|activitySourceHost|
|**--app-activity-id**|string|Required. The unique activity ID in the context of the app - supplied by caller and immutable thereafter.|app_activity_id|appActivityId|
|**--app-display-name**|string|Optional. Short text description of the app used to generate the activity for use in cases when the app is not installed on the user’s local device.|app_display_name|appDisplayName|
|**--content-info**|dictionary|Json|content_info|contentInfo|
|**--content-url**|string|Optional. Used in the event the content can be rendered outside of a native or web-based app experience (for example, a pointer to an item in an RSS feed).|content_url|contentUrl|
|**--created-date-time**|date-time|Set by the server. DateTime in UTC when the object was created on the server.|created_date_time|createdDateTime|
|**--expiration-date-time**|date-time|Set by the server. DateTime in UTC when the object expired on the server.|expiration_date_time|expirationDateTime|
|**--fallback-url**|string|Optional. URL used to launch the activity in a web-based app, if available.|fallback_url|fallbackUrl|
|**--last-modified-date-time**|date-time|Set by the server. DateTime in UTC when the object was modified on the server.|last_modified_date_time|lastModifiedDateTime|
|**--status**|choice||status|status|
|**--user-timezone**|string|Optional. The timezone in which the user's device used to generate the activity was located at activity creation time; values supplied as Olson IDs in order to support cross-platform representation.|user_timezone|userTimezone|
|**--history-items**|array|Optional. NavigationProperty/Containment; navigation property to the activity's historyItems.|history_items|historyItems|
|**--visual-elements-attribution**|object|imageInfo|attribution|attribution|
|**--visual-elements-background-color**|string|Optional. Background color used to render the activity in the UI - brand color for the application source of the activity. Must be a valid hex color|background_color|backgroundColor|
|**--visual-elements-content**|dictionary|Json|content|content|
|**--visual-elements-description**|string|Optional. Longer text description of the user's unique activity (example: document name, first sentence, and/or metadata)|description|description|
|**--visual-elements-display-text**|string|Required. Short text description of the user's unique activity (for example, document name in cases where an activity refers to document creation)|display_text|displayText|

### crossdeviceexperiences user update-device

update-device a crossdeviceexperiences user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-device|UpdateDevices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--account-enabled**|boolean|true if the account is enabled; otherwise, false. Required.|account_enabled|accountEnabled|
|**--alternative-security-ids**|array|For internal use only. Not nullable.|alternative_security_ids|alternativeSecurityIds|
|**--approximate-last-sign-in-date-time**|date-time|The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|approximate_last_sign_in_date_time|approximateLastSignInDateTime|
|**--compliance-expiration-date-time**|date-time|The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|compliance_expiration_date_time|complianceExpirationDateTime|
|**--device-category**|string||device_category|deviceCategory|
|**--microsoft-graph-device-id**|string|Unique identifier set by Azure Device Registration Service at the time of registration.|microsoft_graph_device_id|deviceId|
|**--device-metadata**|string|For internal use only. Set to null.|device_metadata|deviceMetadata|
|**--device-ownership**|string||device_ownership|deviceOwnership|
|**--device-version**|integer|For internal use only.|device_version|deviceVersion|
|**--display-name**|string|The display name for the device. Required.|display_name|displayName|
|**--domain-name**|string||domain_name|domainName|
|**--enrollment-profile-name**|string||enrollment_profile_name|enrollmentProfileName|
|**--enrollment-type**|string||enrollment_type|enrollmentType|
|**--extension-attributes**|object|onPremisesExtensionAttributes|extension_attributes|extensionAttributes|
|**--is-compliant**|boolean|true if the device complies with Mobile Device Management (MDM) policies; otherwise, false. Read-only. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices.|is_compliant|isCompliant|
|**--is-managed**|boolean|true if the device is managed by a Mobile Device Management (MDM) app; otherwise, false. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices.|is_managed|isManaged|
|**--is-rooted**|boolean||is_rooted|isRooted|
|**--management-type**|string||management_type|managementType|
|**--on-premises-last-sync-date-time**|date-time|The last time at which the object was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z' Read-only.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-sync-enabled**|boolean|true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--operating-system**|string|The type of operating system on the device. Required.|operating_system|operatingSystem|
|**--operating-system-version**|string|The version of the operating system on the device. Required.|operating_system_version|operatingSystemVersion|
|**--physical-ids**|array|For internal use only. Not nullable.|physical_ids|physicalIds|
|**--profile-type**|string|The profile type of the device. Possible values:RegisteredDevice (default)SecureVMPrinterSharedIoT|profile_type|profileType|
|**--registration-date-time**|date-time||registration_date_time|registrationDateTime|
|**--system-labels**|array|List of labels applied to the device by the system.|system_labels|systemLabels|
|**--trust-type**|string|Type of trust for the joined device. Read-only. Possible values: Workplace - indicates bring your own personal devicesAzureAd - Cloud only joined devicesServerAd - on-premises domain joined devices joined to Azure AD. For more details, see Introduction to device management in Azure Active Directory|trust_type|trustType|
|**--kind**|string||kind|kind|
|**--manufacturer**|string|Manufacturer of the device. Read-only.|manufacturer|manufacturer|
|**--model**|string|Model of the device. Read-only.|model|model|
|**--name**|string||name|name|
|**--platform**|string||platform|platform|
|**--status**|string||status|status|
|**--member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--registered-owners**|array|The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Currently, there can be only one owner. Read-only. Nullable.|registered_owners|registeredOwners|
|**--registered-users**|array|Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable.|registered_users|registeredUsers|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--extensions**|array|The collection of open extensions defined for the device. Read-only. Nullable.|extensions|extensions|
|**--commands**|array||commands|commands|

### crossdeviceexperiences user-activity create-history-item

create-history-item a crossdeviceexperiences user-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user-activity|users.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-history-item|CreateHistoryItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--id**|string|Read-only.|id|id|
|**--active-duration-seconds**|integer|Optional. The duration of active user engagement. if not supplied, this is calculated from the startedDateTime and lastActiveDateTime.|active_duration_seconds|activeDurationSeconds|
|**--created-date-time**|date-time|Set by the server. DateTime in UTC when the object was created on the server.|created_date_time|createdDateTime|
|**--expiration-date-time**|date-time|Optional. UTC DateTime when the historyItem will undergo hard-delete. Can be set by the client.|expiration_date_time|expirationDateTime|
|**--last-active-date-time**|date-time|Optional. UTC DateTime when the historyItem (activity session) was last understood as active or finished - if null, historyItem status should be Ongoing.|last_active_date_time|lastActiveDateTime|
|**--last-modified-date-time**|date-time|Set by the server. DateTime in UTC when the object was modified on the server.|last_modified_date_time|lastModifiedDateTime|
|**--started-date-time**|date-time|Required. UTC DateTime when the historyItem (activity session) was started. Required for timeline history.|started_date_time|startedDateTime|
|**--status**|choice||status|status|
|**--user-timezone**|string|Optional. The timezone in which the user's device used to generate the activity was located at activity creation time. Values supplied as Olson IDs in order to support cross-platform representation.|user_timezone|userTimezone|
|**--activity**|object|userActivity|activity|activity|

### crossdeviceexperiences user-activity delete

delete a crossdeviceexperiences user-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user-activity|users.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteHistoryItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

### crossdeviceexperiences user-activity get-history-item

get-history-item a crossdeviceexperiences user-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user-activity|users.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-history-item|GetHistoryItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### crossdeviceexperiences user-activity list-history-item

list-history-item a crossdeviceexperiences user-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user-activity|users.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-history-item|ListHistoryItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### crossdeviceexperiences user-activity update-history-item

update-history-item a crossdeviceexperiences user-activity.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user-activity|users.activities|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-history-item|UpdateHistoryItems|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--id**|string|Read-only.|id|id|
|**--active-duration-seconds**|integer|Optional. The duration of active user engagement. if not supplied, this is calculated from the startedDateTime and lastActiveDateTime.|active_duration_seconds|activeDurationSeconds|
|**--created-date-time**|date-time|Set by the server. DateTime in UTC when the object was created on the server.|created_date_time|createdDateTime|
|**--expiration-date-time**|date-time|Optional. UTC DateTime when the historyItem will undergo hard-delete. Can be set by the client.|expiration_date_time|expirationDateTime|
|**--last-active-date-time**|date-time|Optional. UTC DateTime when the historyItem (activity session) was last understood as active or finished - if null, historyItem status should be Ongoing.|last_active_date_time|lastActiveDateTime|
|**--last-modified-date-time**|date-time|Set by the server. DateTime in UTC when the object was modified on the server.|last_modified_date_time|lastModifiedDateTime|
|**--started-date-time**|date-time|Required. UTC DateTime when the historyItem (activity session) was started. Required for timeline history.|started_date_time|startedDateTime|
|**--status**|choice||status|status|
|**--user-timezone**|string|Optional. The timezone in which the user's device used to generate the activity was located at activity creation time. Values supplied as Olson IDs in order to support cross-platform representation.|user_timezone|userTimezone|
|**--activity**|object|userActivity|activity|activity|

### crossdeviceexperiences user-activity-history-item delete

delete a crossdeviceexperiences user-activity-history-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user-activity-history-item|users.activities.historyItems|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRefActivity|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

### crossdeviceexperiences user-activity-history-item get-activity

get-activity a crossdeviceexperiences user-activity-history-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user-activity-history-item|users.activities.historyItems|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-activity|GetActivity|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### crossdeviceexperiences user-activity-history-item get-ref-activity

get-ref-activity a crossdeviceexperiences user-activity-history-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user-activity-history-item|users.activities.historyItems|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-activity|GetRefActivity|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|

### crossdeviceexperiences user-activity-history-item set-ref-activity

set-ref-activity a crossdeviceexperiences user-activity-history-item.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|crossdeviceexperiences user-activity-history-item|users.activities.historyItems|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-activity|SetRefActivity|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--body**|dictionary|New navigation property ref values|body|body|
