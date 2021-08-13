#### Login To Default Tenant Using Previously consented scopes

 ```sh
 mgc login
 ```

 #### Grant more permissions

 ```sh
 mgc login --scopes "user.read,user.readwrite.all,mail.readwrite,directory.read.all,chat.readwrite,people.read,group.read.all,tasks.readwrite,sites.manage.all"
 ```

# Tokens persist across Terminal sessions. You must logout to forget all access tokens
```sh
mgc logout
```
 #### Login to your own tenant
 In your app registration set the redirect uri as `http://localhost:8400/`

 ```sh
 mgc login --scopes "user.read.all" --client-id YOUR_CLIENT_ID --tenant-id YOUR_TENANT_ID
 ```
