from msgraph.cli.core.msal import CustomBrowserCredential


def login(cmd, scopes):
    login_scopes = scopes.split(',')

    credential = CustomBrowserCredential()
    result = credential.get_token(*login_scopes)

    if result:
        print('Logged in successfully')
    else:
        print('Login failed')