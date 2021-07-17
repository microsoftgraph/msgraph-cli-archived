#### Minimum required parameters to create a conditional access policy
```shell
msgraph  identitysignins identity-conditional-access create-policy --display-name 'MinimumRequiredParams' --grant-controls built-in-controls=mfa operator=OR --state disabled  --applications include-applications=none  --users include-users=none
```