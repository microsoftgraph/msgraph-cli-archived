# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import json
import logging
import time
from azure.core.credentials import AccessToken
from msal import PublicClientApplication
from msal_extensions import *
from azure.identity import InteractiveBrowserCredential

from msgraph.cli.core.constants import CACHE_LOCATION, CLIENT_ID
from msgraph.cli.core.exceptions import AuthenticationException, CLIException


class CustomBrowserCredential(InteractiveBrowserCredential):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._app = self._get_app()

    def _get_token_from_cache(self, scopes, **kwargs):
        """if the user has already signed in, redeem refresh token for new access token"""
        accounts = self._app.get_accounts()
        has_accounts = len(accounts) > 0

        if has_accounts:  # => user has already authenticated
            # MSAL asserts scopes is a list
            scopes = self._get_scopes_from_cache()  # type: ignore
            now = int(time.time())
            token = self._app.acquire_token_silent(scopes,
                                                   account=accounts[0],
                                                   **kwargs)

            if token and "access_token" in token and "expires_in" in token:
                return AccessToken(token["access_token"],
                                   now + int(token["expires_in"]))
        else:
            raise CLIException('Login to run this command')
        return None

    def login(self, scopes, **kwargs):
        return self._get_token_by_auth_code(scopes, **kwargs)

    def get_token(self, *scopes, **kwargs):
        try:
            return super().get_token(*scopes, **kwargs)
        except Exception as ex:
            raise AuthenticationException(ex) from ex

    def _get_scopes_from_cache(self):
        persistence = self._build_persistence(CACHE_LOCATION,
                                              fallback_to_plaintext=True)
        refresh_token = json.loads(persistence.load()).get('RefreshToken')
        refresh_token_as_key = list(dict.keys(refresh_token))[0]
        scopes = refresh_token.get(refresh_token_as_key).get('target')
        return list(filter(self._get_filtered_scopes, scopes.split(' ')))

    @staticmethod
    def _get_filtered_scopes(scope):
        """Filters out the frozen set of scopes from tokens retrieved from cache

        The authorization endpoint doesn't expect scopes from the "froze_set"
        """
        frozen_set = ['openid', 'profile', 'offline_access']

        if scope not in frozen_set:
            return scope

    def _get_app(self):
        # type: () -> msal.PublicClientApplication
        if not self._msal_app:
            self._msal_app = self._create_app(PublicClientApplication)
        return self._msal_app

    def _create_app(self, cls):
        # type: (Type[msal.ClientApplication]) -> msal.ClientApplication
        persistence = self._build_persistence(CACHE_LOCATION,
                                              fallback_to_plaintext=True)
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
                    attributes={"app_name": "mg"},
                )
            except:  # pylint: disable=bare-except
                if not fallback_to_plaintext:
                    raise
                logging.warning(
                    "Encryption unavailable. Opting in to plain text.")
        return FilePersistence(location)
