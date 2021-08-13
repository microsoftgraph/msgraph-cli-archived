#### Microsoft Graph Users and Groups

# Login with scopes to access all user operations
```shell
mgc login --scopes user.readwrite.all
```

# List all users in json format
```shell
mgc users user list
```

# List all users in table format
```shell
mgc users user list -o table
```

#### List first 10 users and use JMESPath query to get specific properties
```shell
mgc users user list --query "[:10].{Id:id,Name:displayName,Office:officeLocation,BusinessPhones:businessPhones[0]}" -o table
```

# Get number of users in the tenant
```shell
mgc users user list --query "[] | length(@)"
```

# Filter for a specific user using JMSEPath query
```shell
mgc users user list --query "[?displayName=='Lynne Robbins'].{Id:id, Name:displayName}" -o table
```

#### Update user's location
```shell
$newLocation = 'Minneapolis'
$userId = mgc users user list --query "[?displayName=='Lynne Robbins'].id | [0]"
$userId = $id.Trim('"')
mgc users user update --user-id $userId --office-location $newLocation
```