#### Microsoft Graph Users and Groups

# Get number of users
```shell
msgraph users user list --query 'length([])'
```

#### List users
```shell
msgraph users user list --query '[:10].{Id:id,Name:displayName,Office:officeLocation,BusinessPhones:businessPhones[0]}' -o table
```

#### Update user's location
```shell
msgraph users user update --user-id $userId --office-location $newLocation
```
