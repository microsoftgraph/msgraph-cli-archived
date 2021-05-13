#### Microsoft Graph Users and Groups

# Get number of users
```shell
mg users user list --query 'length([])'
```

#### List users
```shell
mg users user list --query '[:10].{Id:id,Name:displayName,Office:officeLocation,BusinessPhones:businessPhones[0]}' -o table
```

#### Update user's location
```shell
mg users user update --user-id $userId --office-location $newLocation
```
