# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from knack.cli import CLIError

from msgraph.cli.core.authentication import Authentication

authentication = Authentication()


def login(scopes: str, client_id=None):
    # Stripping whitespaces so that users don't have to worry about how
    # they enter scopes. ie "user.read, mail.read" or "user.read,mail.read"
    scopes = [scope.strip() for scope in scopes.split(',')]
    logged_in = authentication.login(scopes, client_id)

    if not logged_in:
        raise CLIError('Login failed')

    print('Logged in successfully')


def logout():
    authentication.logout()
