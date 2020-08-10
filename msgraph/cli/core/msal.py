import json
import logging

from msal import PublicClientApplication
from msal_extensions import *

CACHE_LOCATION = 'mg.bin'


class PublicClient:
    def __init__(self):
        persistence = self._build_persistence(CACHE_LOCATION, fallback_to_plaintext=True)
        self.app = PublicClientApplication(
            client_id='14d82eec-204b-4c2f-b7e8-296a70dab67e',
            token_cache=PersistedTokenCache(persistence)
        )

    def login(self, client_id=None, scopes='user.read'):
        flow = self.app.initiate_device_flow(['user.read.all'])
        # TODO: Raise CLI error instead
        if "user_code" not in flow:
            raise ValueError(
                "Fail to create device flow. Err: %s" % json.dumps(flow, indent=4))

        print(flow["message"])
        sys.stdout.flush()

        result = self.app.acquire_token_by_device_flow(flow)

        if 'access_token' in result:
            return print('Logged in successfuly')
        else:
            return print('Login failed')

    def get_token(self):
        result = {}
        # TODO: Allows users to pick a login account
        accounts = self.app.get_accounts()

        if accounts:
            selected_account = accounts[0]
            result = self.app.acquire_token_silent(scopes=['user.read'], account=selected_account)

        if not result:
            raise Exception('Login in to make requests')

        access_token = result.get('access_token')
        return [access_token]

    def _build_persistence(self, location, fallback_to_plaintext=False):
        """Build persistence instance based on current OS"""
        if sys.platform.startswith('win'):
            return FilePersistenceWithDataProtection(location)
        if sys.platform.startswith('darwin'):
            return KeychainPersistence(location, "mg", "mg")
        if sys.platform.startswith('linux'):
            try:
                return LibsecretPersistence(
                    location,
                    schema_name="mg",
                    attributes={"my_attr1": "foo", "my_attr2": "bar"},
                )
            except:  # pylint: disable=bare-except
                if not fallback_to_plaintext:
                    raise
                logging.warning("Encryption unavailable. Opting in to plain text.")
        return FilePersistence(location)
