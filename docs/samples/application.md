 #### Incremental scope consent

 ```sh
 msgraph login --scopes "application.readwrite.all"
 ```

 #### Create an application for use with DeviceCodeFlow

```sh
msgraph applications application create --display-name "DeviceCodeFlowApp" --is-fallback-public-client --public-client redirect-uris="https://login.microsoftonline.com/common/oauth2/nativeclient"
```

#### Create an application for use with  Native Client and  interactive sign in

```sh
msgraph applications application create --display-name "NativeAppInteractiveFlow" --is-fallback-public-client --public-client redirect-uris="http://localhost"
```

#### Create a web app with implicit auth

```sh
msgraph applications application create --display-name "NativeAppInteractiveFlow" --redirect-uris="http://localhost" --implicit-grant-settings enable-access-token-issuance=true enable-id-token-issuance=true
```

#### Create a registration for ASP.NET Web App

```sh
msgraph applications application create --display-name "AspNetWebApp" --redirect-uris="https://localhost:5001/signin-oidc" --implicit-grant-settings enable-id-token-issuance=true --required-resource-access resource-app-id="00000003-0000-0000-c000-000000000000" resource-access='{"type":"Scope","id":"e1fe6dd8-ba31-4d61-89e7-88639da4683d"}'
```

#### Create a registration for an ASP.NET Web App that calls Graph
```sh
#!/bin/bash

# Create application and get the id property
id=$(msgraph applications application create --display-name AspNetWebApp --redirect-uris=https://localhost:5001/signin-oidc --logout-url https://localhost:5001/signout-oidc --implicit-grant-settings enable-id-token-issuance=true --required-resource-access resource-app-id=00000003-0000-0000-c000-000000000000 resource-access='{"type":"Scope","id":"e1fe6dd8-ba31-4d61-89e7-88639da4683d"}' --query id)

# The id property has quotes "XXX-XXXX-XXXX" these quotes get url encoded when running the add-password command
# resulting in a bad request, therefore, remove the quotes.
id="${id//'"'}"

# Use application id to create password and get secret
secret=$(msgraph applications application add-password --application-id $id)
echo "$secret"
```


#### Create an application for use with Confidential Client flow using a certificate. Get certificate from current user store

```shell
graphResourceId=00000003-0000-0000-c000-000000000000

# Graph permissions constant
userReadAll='{"id":"df021288-bdef-4463-88db-98f22de89214","type":"Role"}'

# Create an application registration
cert=$(cat path_to_your_cert)

msgraph applications application create --display-name "Scripted" --sign-in-audience "AzureADMyOrg" \
      --required-resource-access resource-app-id=$graphResourceId resource-access=$userReadAll \
      --key-credentials key=$(printf %s "$cert" | base64) usage="Verify" type="AsymmetricX509Cert" display-name="scripted"
```

