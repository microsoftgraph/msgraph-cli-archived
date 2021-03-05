 #### Incremental scope consent

 ```sh
 mg login --scopes "application.readwrite.all"
 ```

 #### Create an application for use with DeviceCodeFlow

```sh
mg applications application create --display-name "DeviceCodeFlowApp" --is-fallback-public-client --public-client redirect-uris="https://login.microsoftonline.com/common/oauth2/nativeclient"
```

#### Create an application for use with  Native Client and  interactive sign in

```sh
mg applications application create --display-name "NativeAppInteractiveFlow" --is-fallback-public-client --public-client redirect-uris="http://localhost"
```

#### Create a web app with implicit auth

```sh
mg applications application create --display-name "NativeAppInteractiveFlow" --redirect-uris="http://localhost" --implicit-grant-settings enable-access-token-issuance=true enable-id-token-issuance=true
```

#### Create a registration for ASP.NET Web App

```sh
mg applications application create --display-name "AspNetWebApp" --redirect-uris="https://localhost:5001/signin-oidc" --implicit-grant-settings enable-id-token-issuance=true --required-resource-access resource-app-id="00000003-0000-0000-c000-000000000000" resource-access='{"type":"Scope","id":"e1fe6dd8-ba31-4d61-89e7-88639da4683d"}'
```

## TODO: Create an app that calls Graph API.
#### Create a registration for an ASP.NET Web App that calls Graph

```sh
mg applications application create --display-name "AspNetWebApp" --redirect-uris="https://localhost:5001/signin-oidc" --logout-url "https://localhost:5001/signout-oidc" --implicit-grant-settings enable-id-token-issuance=true --required-resource-access resource-app-id="00000003-0000-0000-c000-000000000000" resource-access='{"type":"Scope","id":"e1fe6dd8-ba31-4d61-89e7-88639da4683d"}'
```