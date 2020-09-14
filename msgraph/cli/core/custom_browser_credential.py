# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.identity import InteractiveBrowserCredential, AuthenticationRecord

from msgraph.cli.core.constants import CACHE_LOCATION, CLIENT_ID
from msgraph.cli.core.exceptions import CLIException


def get_credential() -> InteractiveBrowserCredential:
    auth_record = _get_auth_record()

    return InteractiveBrowserCredential(
        client_id=CLIENT_ID,
        enable_persistent_cache=True,
        authentication_record=auth_record,
    )


def _get_auth_record() -> AuthenticationRecord:
    result = None

    try:
        with open(CACHE_LOCATION, 'r') as file:
            result = file.read()

        return AuthenticationRecord.deserialize(result)
    except IOError:
        raise CLIException('Login to run this command')
