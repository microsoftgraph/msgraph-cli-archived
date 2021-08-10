#### Microsoft Graph Users and Groups

# Get number of users
```shell
mgc users user list --query 'length([])'
```

#### List users
```shell
mgc users user list --query '[:10].{Id:id,Name:displayName,Office:officeLocation,BusinessPhones:businessPhones[0]}' -o table
```

#### Update user's location
```shell
mgc users user update --user-id $userId --office-location $newLocation
```
