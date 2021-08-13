#### Get permissions to access mail operations
```shell
mgc login --scopes mail.readwrite
```
#### Create a new mail
```shell
mgc mail user create-message --user-id "sender@domain.org" --subject "Hello" --body content="Here is my message" content-type="application/text" --to-recipient '[{\"emailAddress\":{\"address\":\"garth@contoso.com\"}}]'
```