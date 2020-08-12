import json
import logging
import time

from azure.core.credentials import AccessToken
from msal import PublicClientApplication
from msal_extensions import *

from azure.identity import InteractiveBrowserCredential

from msgraph.cli.core.constants import CACHE_LOCATION, CLIENT_ID


class CustomBrowserCredential(InteractiveBrowserCredential):
    def __init__(self, **kwargs):
        super(CustomBrowserCredential, self).__init__(**kwargs)

    def _get_token_from_cache(self, scopes, **kwargs):
        """if the user has already signed in, we can redeem a refresh token for a new access token"""
        scopes_from_cache = self._get_scopes_from_cache()
        app = self._get_app()
        accounts = app.get_accounts()
        if accounts:  # => user has already authenticated
            # MSAL asserts scopes is a list
            scopes = list(scopes)  # type: ignore
            now = int(time.time())
            token = app.acquire_token_silent(scopes_from_cache, account=accounts[0], **kwargs)
            if token and "access_token" in token and "expires_in" in token:
                return AccessToken(token["access_token"], now + int(token["expires_in"]))
        return None

    def _get_scopes_from_cache(self):
        persistence = self._build_persistence(CACHE_LOCATION, fallback_to_plaintext=True)
        refresh_token = json.loads(persistence.load()).get('RefreshToken')
        refresh_token_as_key = list(dict.keys(refresh_token))[0]
        scopes = refresh_token.get(refresh_token_as_key).get('target')
        return scopes.split(' ')

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
