 #### Login To Default Tenant

 ```sh
 mg login --scopes "application.readwrite.all"
 ```

 #### Login to your own tenant
 In your app registration set the redirect uri as `http://localhost:8400/`

 ```sh
 mg login --scopes "user.read.all" --client-id YOUR_CLIENT_ID --tenant-id YOUR_TENANT_ID
 ```
