# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from msgraph.cli.core.custom_browser_credential import CustomBrowserCredential


def login(cmd, scopes):
    login_scopes = [scope.strip() for scope in scopes.split(',')]
    credential = CustomBrowserCredential()

    try:
        result = credential.get_token(*login_scopes)
        if result:
            print('Logged in successfully')
    except Exception:
        print('Login failed')
