import logging
import time

from azure.core.credentials import AccessToken
from msal import PublicClientApplication
from msal_extensions import *

CACHE_LOCATION = 'mg.bin'
CLIENT_ID = 'f7218512-c727-4138-9fb9-a0fe2500650c'

from azure.identity import InteractiveBrowserCredential


class CustomBrowserCredential(InteractiveBrowserCredential):
    def __init__(self, **kwargs):
        super(CustomBrowserCredential, self).__init__(**kwargs)

    def _get_token_from_cache(self, scopes, **kwargs):
        """if the user has already signed in, we can redeem a refresh token for a new access token"""
        scopes = ['user.read']

        app = self._get_app()
        accounts = app.get_accounts()
        if accounts:  # => user has already authenticated
            # MSAL asserts scopes is a list
            scopes = list(scopes)  # type: ignore
            now = int(time.time())
            token = app.acquire_token_silent(scopes, account=accounts[0], **kwargs)
            print(token)
            if token and "access_token" in token and "expires_in" in token:
                return AccessToken(token["access_token"], now + int(token["expires_in"]))
        return None

    def _get_app(self):
        # type: () -> msal.PublicClientApplication
        if not self._msal_app:
            self._msal_app = self._create_app(PublicClientApplication)
        return self._msal_app

    def _create_app(self, cls):
        # type: (Type[msal.ClientApplication]) -> msal.ClientApplication
        persistence = self._build_persistence(CACHE_LOCATION, fallback_to_plaintext=True)
        persisted_cached = PersistedTokenCache(persistence)
        return cls(client_id=CLIENT_ID, token_cache=persisted_cached)

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
