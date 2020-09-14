# Azure CLI Module Creation Report

### teamsteamwork create-installed-app

create-installed-app a teamsteamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teamsteamwork|users.teamwork|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-installed-app|CreateInstalledApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--teams-app-definition**|object|teamsAppDefinition|teams_app_definition|teamsAppDefinition|
|**--teams-app-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--teams-app-external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--teams-app-name**|string||name|name|
|**--teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|display_name|displayName|
|**--teams-app-distribution-method**|choice||distribution_method|distributionMethod|
|**--teams-app-app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

### teamsteamwork get-installed-app

get-installed-app a teamsteamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teamsteamwork|users.teamwork|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-installed-app|GetInstalledApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--teams-app-installation-id**|string|key: teamsAppInstallation-id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teamsteamwork get-team-app

get-team-app a teamsteamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teamsteamwork|users.teamwork.installedApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-app|GetTeamsApp|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--teams-app-installation-id**|string|key: teamsAppInstallation-id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teamsteamwork get-team-app-definition

get-team-app-definition a teamsteamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teamsteamwork|users.teamwork.installedApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-app-definition|GetTeamsAppDefinition|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--teams-app-installation-id**|string|key: teamsAppInstallation-id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teamsteamwork get-teamwork

get-teamwork a teamsteamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teamsteamwork|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-teamwork|GetTeamwork|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teamsteamwork list-installed-app

list-installed-app a teamsteamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teamsteamwork|users.teamwork|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-installed-app|ListInstalledApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teamsteamwork update-installed-app

update-installed-app a teamsteamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teamsteamwork|users.teamwork|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-installed-app|UpdateInstalledApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--teams-app-installation-id**|string|key: teamsAppInstallation-id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--id**|string|Read-only.|id|id|
|**--teams-app-definition**|object|teamsAppDefinition|teams_app_definition|teamsAppDefinition|
|**--teams-app-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--teams-app-external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--teams-app-name**|string||name|name|
|**--teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|display_name|displayName|
|**--teams-app-distribution-method**|choice||distribution_method|distributionMethod|
|**--teams-app-app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

### teamsteamwork update-teamwork

update-teamwork a teamsteamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teamsteamwork|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-teamwork|UpdateTeamwork|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: user-id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--installed-apps**|array||installed_apps|installedApps|
