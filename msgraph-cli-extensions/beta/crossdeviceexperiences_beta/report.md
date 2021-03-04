# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az crossdeviceexperiences_beta|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az crossdeviceexperiences_beta` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az crossdeviceexperiences user|users|[commands](#CommandsInusers)|
|az crossdeviceexperiences user-activity|users.activities|[commands](#CommandsInusers.activities)|
|az crossdeviceexperiences user-activity-history-item|users.activities.historyItems|[commands](#CommandsInusers.activities.historyItems)|

## COMMANDS
### <a name="CommandsInusers">Commands in `az crossdeviceexperiences user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az crossdeviceexperiences user delete](#usersDeleteActivities)|DeleteActivities|[Parameters](#ParametersusersDeleteActivities)|Not Found|
|[az crossdeviceexperiences user delete](#usersDeleteDevices)|DeleteDevices|[Parameters](#ParametersusersDeleteDevices)|Not Found|
|[az crossdeviceexperiences user create-activity](#usersCreateActivities)|CreateActivities|[Parameters](#ParametersusersCreateActivities)|Not Found|
|[az crossdeviceexperiences user create-device](#usersCreateDevices)|CreateDevices|[Parameters](#ParametersusersCreateDevices)|Not Found|
|[az crossdeviceexperiences user list-activity](#usersListActivities)|ListActivities|[Parameters](#ParametersusersListActivities)|Not Found|
|[az crossdeviceexperiences user list-device](#usersListDevices)|ListDevices|[Parameters](#ParametersusersListDevices)|Not Found|
|[az crossdeviceexperiences user show-activity](#usersGetActivities)|GetActivities|[Parameters](#ParametersusersGetActivities)|Not Found|
|[az crossdeviceexperiences user show-device](#usersGetDevices)|GetDevices|[Parameters](#ParametersusersGetDevices)|Not Found|
|[az crossdeviceexperiences user update-activity](#usersUpdateActivities)|UpdateActivities|[Parameters](#ParametersusersUpdateActivities)|Not Found|
|[az crossdeviceexperiences user update-device](#usersUpdateDevices)|UpdateDevices|[Parameters](#ParametersusersUpdateDevices)|Not Found|

### <a name="CommandsInusers.activities">Commands in `az crossdeviceexperiences user-activity` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az crossdeviceexperiences user-activity delete](#users.activitiesDeleteHistoryItems)|DeleteHistoryItems|[Parameters](#Parametersusers.activitiesDeleteHistoryItems)|Not Found|
|[az crossdeviceexperiences user-activity create-history-item](#users.activitiesCreateHistoryItems)|CreateHistoryItems|[Parameters](#Parametersusers.activitiesCreateHistoryItems)|Not Found|
|[az crossdeviceexperiences user-activity list-history-item](#users.activitiesListHistoryItems)|ListHistoryItems|[Parameters](#Parametersusers.activitiesListHistoryItems)|Not Found|
|[az crossdeviceexperiences user-activity show-history-item](#users.activitiesGetHistoryItems)|GetHistoryItems|[Parameters](#Parametersusers.activitiesGetHistoryItems)|Not Found|
|[az crossdeviceexperiences user-activity update-history-item](#users.activitiesUpdateHistoryItems)|UpdateHistoryItems|[Parameters](#Parametersusers.activitiesUpdateHistoryItems)|Not Found|

### <a name="CommandsInusers.activities.historyItems">Commands in `az crossdeviceexperiences user-activity-history-item` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az crossdeviceexperiences user-activity-history-item delete](#users.activities.historyItemsDeleteRefActivity)|DeleteRefActivity|[Parameters](#Parametersusers.activities.historyItemsDeleteRefActivity)|Not Found|
|[az crossdeviceexperiences user-activity-history-item set-ref-activity](#users.activities.historyItemsSetRefActivity)|SetRefActivity|[Parameters](#Parametersusers.activities.historyItemsSetRefActivity)|Not Found|
|[az crossdeviceexperiences user-activity-history-item show-activity](#users.activities.historyItemsGetActivity)|GetActivity|[Parameters](#Parametersusers.activities.historyItemsGetActivity)|Not Found|
|[az crossdeviceexperiences user-activity-history-item show-ref-activity](#users.activities.historyItemsGetRefActivity)|GetRefActivity|[Parameters](#Parametersusers.activities.historyItemsGetRefActivity)|Not Found|


## COMMAND DETAILS

### group `az crossdeviceexperiences user`
#### <a name="usersDeleteActivities">Command `az crossdeviceexperiences user delete`</a>

##### <a name="ParametersusersDeleteActivities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteDevices">Command `az crossdeviceexperiences user delete`</a>

##### <a name="ParametersusersDeleteDevices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|

#### <a name="usersCreateActivities">Command `az crossdeviceexperiences user create-activity`</a>

##### <a name="ParametersusersCreateActivities">Parameters</a> 
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
|**--attribution**|object|imageInfo|attribution|attribution|
|**--background-color**|string|Optional. Background color used to render the activity in the UI - brand color for the application source of the activity. Must be a valid hex color|background_color|backgroundColor|
|**--content**|dictionary|Json|content|content|
|**--description**|string|Optional. Longer text description of the user's unique activity (example: document name, first sentence, and/or metadata)|description|description|
|**--display-text**|string|Required. Short text description of the user's unique activity (for example, document name in cases where an activity refers to document creation)|display_text|displayText|

#### <a name="usersCreateDevices">Command `az crossdeviceexperiences user create-device`</a>

##### <a name="ParametersusersCreateDevices">Parameters</a> 
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

#### <a name="usersListActivities">Command `az crossdeviceexperiences user list-activity`</a>

##### <a name="ParametersusersListActivities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListDevices">Command `az crossdeviceexperiences user list-device`</a>

##### <a name="ParametersusersListDevices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetActivities">Command `az crossdeviceexperiences user show-activity`</a>

##### <a name="ParametersusersGetActivities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetDevices">Command `az crossdeviceexperiences user show-device`</a>

##### <a name="ParametersusersGetDevices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateActivities">Command `az crossdeviceexperiences user update-activity`</a>

##### <a name="ParametersusersUpdateActivities">Parameters</a> 
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
|**--attribution**|object|imageInfo|attribution|attribution|
|**--background-color**|string|Optional. Background color used to render the activity in the UI - brand color for the application source of the activity. Must be a valid hex color|background_color|backgroundColor|
|**--content**|dictionary|Json|content|content|
|**--description**|string|Optional. Longer text description of the user's unique activity (example: document name, first sentence, and/or metadata)|description|description|
|**--display-text**|string|Required. Short text description of the user's unique activity (for example, document name in cases where an activity refers to document creation)|display_text|displayText|

#### <a name="usersUpdateDevices">Command `az crossdeviceexperiences user update-device`</a>

##### <a name="ParametersusersUpdateDevices">Parameters</a> 
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

### group `az crossdeviceexperiences user-activity`
#### <a name="users.activitiesDeleteHistoryItems">Command `az crossdeviceexperiences user-activity delete`</a>

##### <a name="Parametersusers.activitiesDeleteHistoryItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.activitiesCreateHistoryItems">Command `az crossdeviceexperiences user-activity create-history-item`</a>

##### <a name="Parametersusers.activitiesCreateHistoryItems">Parameters</a> 
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

#### <a name="users.activitiesListHistoryItems">Command `az crossdeviceexperiences user-activity list-history-item`</a>

##### <a name="Parametersusers.activitiesListHistoryItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.activitiesGetHistoryItems">Command `az crossdeviceexperiences user-activity show-history-item`</a>

##### <a name="Parametersusers.activitiesGetHistoryItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.activitiesUpdateHistoryItems">Command `az crossdeviceexperiences user-activity update-history-item`</a>

##### <a name="Parametersusers.activitiesUpdateHistoryItems">Parameters</a> 
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

### group `az crossdeviceexperiences user-activity-history-item`
#### <a name="users.activities.historyItemsDeleteRefActivity">Command `az crossdeviceexperiences user-activity-history-item delete`</a>

##### <a name="Parametersusers.activities.historyItemsDeleteRefActivity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.activities.historyItemsSetRefActivity">Command `az crossdeviceexperiences user-activity-history-item set-ref-activity`</a>

##### <a name="Parametersusers.activities.historyItemsSetRefActivity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="users.activities.historyItemsGetActivity">Command `az crossdeviceexperiences user-activity-history-item show-activity`</a>

##### <a name="Parametersusers.activities.historyItemsGetActivity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.activities.historyItemsGetRefActivity">Command `az crossdeviceexperiences user-activity-history-item show-ref-activity`</a>

##### <a name="Parametersusers.activities.historyItemsGetRefActivity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--user-activity-id**|string|key: id of userActivity|user_activity_id|userActivity-id|
|**--activity-history-item-id**|string|key: id of activityHistoryItem|activity_history_item_id|activityHistoryItem-id|
