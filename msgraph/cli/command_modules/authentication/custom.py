from msgraph.cli.core.msal import PublicClient


def login(cmd):
    client = PublicClient()
    client.login()