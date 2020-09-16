# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from os import path, remove
from azure.identity import InteractiveBrowserCredential, AuthenticationRecord

from msgraph.cli.core.constants import AUTH_RECORD_LOCATION, CLIENT_ID
from msgraph.cli.core.exceptions import CLIException


class Authentication:
    def login(self, scopes: [str]) -> bool:
        auth_record = self.get_credential(login=True).authenticate(scopes=scopes)

        if not auth_record:
            return False

        self._save_auth_record(auth_record)
        return True

    def logout(self):
        # By deleting the authentication record, we logout the user
        self._delete_auth_record()

    def get_credential(self, login=False) -> InteractiveBrowserCredential:
        auth_record = self._get_auth_record(login)

        return InteractiveBrowserCredential(
            client_id=CLIENT_ID,
            enable_persistent_cache=True,
            authentication_record=auth_record,
        )

    def _save_auth_record(self, auth_record: AuthenticationRecord):
        record = auth_record.serialize()

        try:
            with open(AUTH_RECORD_LOCATION, 'w') as file:
                file.write(record)
        except IOError as ex:
            raise CLIException('Authentication session not saved, you\'ll be prompted \
                to login when running a command') from ex

    def _get_auth_record(self, login) -> AuthenticationRecord:
        result = None

        # If we are logging in, return with None since we don't need
        # AuthenticationRecord object.
        if login:
            return result

        try:
            with open(AUTH_RECORD_LOCATION, 'r') as file:
                result = file.read()
            return AuthenticationRecord.deserialize(result)
        except IOError as ex:
            raise CLIException('Login to run this command') from ex

    def _delete_auth_record(self):
        if path.isfile(AUTH_RECORD_LOCATION):
            try:
                remove(AUTH_RECORD_LOCATION)
                print('Logged out successfully')
            except IOError as ex:
                print('Logout failed')
                raise CLIException(ex)
        else:
            print('You\'re already logged out')
