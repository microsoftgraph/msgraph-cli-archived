# Map of Azure CLI to MS Graph CLI

Capturing the differences in experience between MS Graph CLI and Azure CLI. In nearly all scenarios, Microsoft Graph CLI is currently a downgraded experience. Some of the issues are in the actual MS Graph service. Some of them maybe an artifact of expressing the API as CSDL and our transformation.

Also noticed that I can't use my personal account with MS Graph CLI. This needs to be fixed before any announcement.

### Manage applications with AAD Graph

These are cli commands that start with [az ad app](https://docs.microsoft.com/en-us/cli/azure/ad/app?view=azure-cli-latest).

|az cli|mg cli|notes|link
|---|---|---|---|
|az ad app create --display-name "contoso-temp-app2"|mg applications application create --display-name "contoso-temp-app"|Create a web application, web API or native application.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app?view=azure-cli-latest#az_ad_app_create) [mgcli]()|
|az ad app delete --id c4c5ebcb-bcfb-4a24-ae76-ae69b1f29e86 |mg applications application delete-application --application-id 175e99f0-c87d-429f-9124-752dc6bb05f4|Delete an application. Note that MS Graph deletes based on the id property (which is not the appid), AZ CLI uses the appid (but is called id in cli). <br>Also noticed strange perf differences in Azure Portal: MS Graph deletion was delayed in being reflected in the portal while <br>Azure CLI changes were immediate.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app?view=azure-cli-latest#az_ad_app_delete) [mgcli]()|
|az ad app list|mg applications application list|List applications. mg needs scopes: Application.ReadWrite.All. Note that with Azure CLI no scopes needed.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app?view=azure-cli-latest#az_ad_app_list) [mgcli]()|
|az ad app show --id 6881477a-a153-4bf1-973e-60abfad70ad5|mg applications application show-application --application-id 57b496a0-ef24-4cdb-a68d-9791f9a12cc3|Get the details of an application. Same situation as *delete* MS Graph CLI doesn't use appid for deletion.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app?view=azure-cli-latest#az_ad_app_show) [mgcli]()|
|az ad app update --id c729d71b-565b-4963-9825-fe58337ab655 --password password123 |mg applications application add-password --application-id 4f501874-98c4-498b-bd9a-6454b36e0e04|Update an application. In MS Graph CLI, the password is updated differently than in Azure CLI.<br> MG uses an action. Additiionally, we can't set the password like in Azure CLI, this could be a bug scenario in the MG CLI generation. The secret comes back in the response. <br> Default lifetime of secrets are different based on API.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app?view=azure-cli-latest#az_ad_app_update) [mgcli]()|
|az ad app update --id c729d71b-565b-4963-9825-fe58337ab655 --homepage "https://www.contoso.com"|mg applications application update --application-id 4f501874-98c4-498b-bd9a-6454b36e0e04 --description "this is the description"|App update.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/credential?view=azure-cli-latest) [mgcli]()|
|az ad app credential||Manage an application's password or certificate credentials.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/credential?view=azure-cli-latest) [mgcli]()|
|az ad app credential delete||Delete an application's password or certificate credentials.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/credential?view=azure-cli-latest#az_ad_app_credential_delete) [mgcli]()|
|az ad app credential list||List an application's password or certificate credential metadata. (The content of the password or certificate credential is not retrievable.).|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/credential?view=azure-cli-latest#az_ad_app_credential_list) [mgcli]()|
|az ad app credential reset||Append or overwrite an application's password or certificate credentials.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/credential?view=azure-cli-latest#az_ad_app_credential_reset) [mgcli]()|
|az ad app owner||Manage application owners.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/owner?view=azure-cli-latest) [mgcli]()|
|az ad app owner add||Add an application owner.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/owner?view=azure-cli-latest#az_ad_app_owner_add) [mgcli]()|
|az ad app owner list||List application owners.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/owner?view=azure-cli-latest#az_ad_app_owner_list) [mgcli]()|
|az ad app owner remove||Remove an application owner.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/owner?view=azure-cli-latest#az_ad_app_owner_remove) [mgcli]()|
|az ad app permission||Manage an application's OAuth2 permissions.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/permission?view=azure-cli-latest) [mgcli]()|
|az ad app permission add||Add an API permission.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/permission?view=azure-cli-latest#az_ad_app_permission_add) [mgcli]()|
|az ad app permission admin-consent||Grant Application & Delegated permissions through admin-consent.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/permission?view=azure-cli-latest#az_ad_app_permission_admin_consent) [mgcli]()|
|az ad app permission delete||Remove an API permission.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/permission?view=azure-cli-latest#az_ad_app_permission_delete) [mgcli]()|
|az ad app permission grant||Grant the app an API Delegated permissions.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/permission?view=azure-cli-latest#az_ad_app_permission_grant) [mgcli]()|
|az ad app permission list||List API permissions the application has requested.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/permission?view=azure-cli-latest#az_ad_app_permission_list) [mgcli]()|
|az ad app permission list-grants||List Oauth2 permission grants.|[azcli](https://docs.microsoft.com/en-us/cli/azure/ad/app/permission?view=azure-cli-latest#az_ad_app_permission_list_grants) [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|

### Manage Azure Active Directory groups

These are cli commands that start with [az ad group](https://docs.microsoft.com/en-us/cli/azure/ad/group?view=azure-cli-latest).

|az cli|mg cli|notes|link
|---|---|---|---|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|
||||[azcli]() [mgcli]()|

https://docs.microsoft.com/en-us/graph/api/resources/group?view=graph-rest-1.0
https://docs.microsoft.com/en-us/graph/api/resources/directoryobject?view=graph-rest-1.0

### Show graph information about current signed-in user in CLI

These are cli commands that start with [az ad signed-in-user](https://docs.microsoft.com/en-us/cli/azure/ad/signed-in-user?view=azure-cli-latest).

|az cli|mg cli|notes|link
|---|---|---|---|
||||[link]|
|||||
|||||

### Manage Azure Active Directory service principals for automation authentication

These are cli commands that start with [az ad sp](https://docs.microsoft.com/en-us/cli/azure/ad/sp?view=azure-cli-latest).

|az cli|mg cli|notes|link
|---|---|---|---|
||||[link]|
|||||
|||||

### Manage Azure Active Directory users and user authentication

These are cli commands that start with [az ad user](https://docs.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest).

|az cli|mg cli|notes|link
|---|---|---|---|
||||[link]|
|||||
|||||

https://docs.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0
https://docs.microsoft.com/en-us/graph/api/resources/directoryobject?view=graph-rest-1.0

### Manage domain service with azure active directory

These are cli commands that start with [az ad ds](https://docs.microsoft.com/en-us/cli/azure/ad/ds?view=azure-cli-latest). This is not installed by default with the CLI.

|az cli|mg cli|notes|link
|---|---|---|---|
||||[link]|
|||||
|||||

### Managed Service Identities

These are cli commands that start with [az identity](https://docs.microsoft.com/en-us/cli/azure/identity?view=azure-cli-latest).

|az cli|mg cli|notes|link
|---|---|---|---|
||||[link]|
|||||
|||||

### Manage user roles for access control with Azure Active Directory and service principals

These are cli commands that start with [az role](https://docs.microsoft.com/en-us/cli/azure/role?view=azure-cli-latest).

|az cli|mg cli|notes|link
|---|---|---|---|
|az role assignment create --assignee servicePrincipalName --role Reader|||[link]|
|az role assignment delete --assignee userSign-inName --role Contributor||||
|||||

https://docs.microsoft.com/en-us/graph/api/resources/approleassignment?view=graph-rest-1.0

### List Azure Marketplace images allowed for a DevTest Lab.

These are cli commands that start with [az lab gallery-image](https://docs.microsoft.com/en-us/cli/azure/lab/gallery-image?view=azure-cli-latest).

|az cli|mg cli|notes|link
|---|---|---|---|
||||[link]|
|||||
|||||

https://docs.microsoft.com/en-us/graph/api/resources/applicationtemplate?view=graph-rest-1.0
