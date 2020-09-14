# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from os import path, remove
from knack.cli import CLIError
from azure.identity import AuthenticationRecord

from msgraph.cli.core.custom_browser_credential import get_credential
from msgraph.cli.core.constants import CACHE_LOCATION


def login(scopes):
    # Stripping whitespaces so that users don't have to worry about how
    # they enter scopes. ie "user.read, mail.read" or "user.read,mail.read"
    login_scopes = [scope.strip() for scope in scopes.split(',')]
    credential = get_credential()

    auth_record = credential.authenticate(scopes=login_scopes)
    _save_auth_record(auth_record)

    if not auth_record:
        raise CLIError('Login failed')

    print('Logged in successfully')


def _save_auth_record(auth_record: AuthenticationRecord):
    record = auth_record.serialize()

    with open(CACHE_LOCATION, 'w') as file:
        file.write(record)


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
