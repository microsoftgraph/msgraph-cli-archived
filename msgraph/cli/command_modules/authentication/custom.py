# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from os import path, remove
from knack.cli import CLIError

from msgraph.cli.core.custom_browser_credential import CustomBrowserCredential
from msgraph.cli.core.constants import CACHE_LOCATION


def login(scopes):
    # Stripping whitespaces so that users don't have to worry about how
    # they enter scopes. ie "user.read, mail.read" or "user.read,mail.read"
    login_scopes = [scope.strip() for scope in scopes.split(',')]
    credential = CustomBrowserCredential()
    result = credential.login(login_scopes)

    if not result:
        raise CLIError('Login failed')
    else:
        print('Logged in successfully')


def logout():
    # By deleting the token cache, we logout the user since the access token
    # will be deleted as well.
    _delete_token_cache()


def _delete_token_cache():
    if path.isfile(CACHE_LOCATION):
        remove(CACHE_LOCATION)
        print('Logged out successfully')
    else:
        print('You\'re already logged out')
