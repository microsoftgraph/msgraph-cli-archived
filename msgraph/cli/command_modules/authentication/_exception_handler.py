# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError, ClientAuthenticationError
from knack.cli import CLIError
import sys


def auth_exception_handler(ex):
    if isinstance(ex, HttpResponseError):
        if ex.status_code == 403:
            handle_403()
            sys.exit(1)
    if isinstance(ex, ClientAuthenticationError):
        handle_auth_error(ex)
        sys.exit(1)


def handle_403():
    raise CLIError(
        'You have insufficient privileges to complete the operation, login with required scopes')


def handle_auth_error(ex):
    raise CLIError(ex.message)
