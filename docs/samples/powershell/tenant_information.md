#### Get permissions to access application operations for the tenant
 ```sh
 mgc login --scopes "application.readwrite.all"
 ```

#### List application registrations in the tenant
```shell
mgc applications application list --query '[:10].{Name:displayName,Id:appId,SignInAudience:signInAudience}'
```

#### List service principals in the tenant
```shell
mgc applications  service-principal-service-principal  list-service-principal --query '[].{Id:id,Name:appDisplayName}' -o table
```