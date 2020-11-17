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
        try:
            credential = self.get_credential()
            auth_record = credential.authenticate(scopes=scopes)

            if auth_record is None:
                return False

            self._save_auth_record(auth_record)
            return True
        except ValueError:
            warning = '''
            Token can't be stored securely. Install PyGObject to store token securely.

            sudo apt install libgirepository1.0-dev libcairo2-dev python3-dev gir1.2-secret-1
            pip install pygobject
            '''
            print(warning)
            return False

    def logout(self):
        # By deleting the authentication record, we logout the user
        self._delete_auth_record()

    def get_credential(self, auth_record=None) -> InteractiveBrowserCredential:
        '''
        Raises
        ------
        ValueError
            If PyGObject is not installed in the host Linux OS.
        '''
        # TODO: get authority from profile.json
        return InteractiveBrowserCredential(
            client_id=CLIENT_ID,
            enable_persistent_cache=True,
            allow_unencrypted_cache=False,
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

    def get_auth_record(self) -> AuthenticationRecord:
        result = None

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
