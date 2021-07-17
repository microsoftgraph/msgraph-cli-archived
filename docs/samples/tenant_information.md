#### List application registrations in the tenant
```shell
mg applications application list --query '[:10].{Name:displayName,Id:appId,SignInAudience:signInAudience}'
```

#### List service principals in the tenant
```shell
mg applications  service-principal-service-principal  list-service-principal --query '[].{Id:id,Name:appDisplayName}' -o table
```