 #### Login To Default Tenant

 ```sh
 mg login --scopes "application.readwrite.all"
 ```

 #### Login to your own tenant

 ```sh
 mg login --scopes "user.read.all" --client-id YOUR_CLIENT_ID --tenant-id YOUR_TENANT_ID
 ```