#### Get required permissions
```shell
mgc login --scopes 'application.read.all,policy.read.all,policy.readwrite.conditionalaccess'
```

#### Minimum required parameters to create a conditional access policy
```shell
mgc  identitysignins identity-conditional-access create-policy --display-name 'MinimumRequiredParams' --grant-controls built-in-controls=mfa operator=OR --state disabled  --applications include-applications=none  --users include-users=none
```