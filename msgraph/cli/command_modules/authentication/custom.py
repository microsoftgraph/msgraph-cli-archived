from msgraph.cli.core.msal import CustomBrowserCredential


def login(cmd):
    credential = CustomBrowserCredential()
    scopes = ['user.read']
    result = credential.get_token(*scopes)
    print(result)