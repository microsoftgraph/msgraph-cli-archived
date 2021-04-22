# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import PeopleConfiguration
from .operations import UsersOperations
from .operations import UsersInsightsOperations
from .operations import UsersInsightsSharedOperations
from .operations import UsersInsightsTrendingOperations
from .operations import UsersInsightsUsedOperations
from .. import models


class People(object):
    """People.

    :ivar users: UsersOperations operations
    :vartype users: people.aio.operations.UsersOperations
    :ivar users_insights: UsersInsightsOperations operations
    :vartype users_insights: people.aio.operations.UsersInsightsOperations
    :ivar users_insights_shared: UsersInsightsSharedOperations operations
    :vartype users_insights_shared: people.aio.operations.UsersInsightsSharedOperations
    :ivar users_insights_trending: UsersInsightsTrendingOperations operations
    :vartype users_insights_trending: people.aio.operations.UsersInsightsTrendingOperations
    :ivar users_insights_used: UsersInsightsUsedOperations operations
    :vartype users_insights_used: people.aio.operations.UsersInsightsUsedOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param top: Show only the first n items.
    :type top: int
    :param skip: Skip the first n items.
    :type skip: int
    :param search: Search items by search phrases.
    :type search: str
    :param filter: Filter items by property values.
    :type filter: str
    :param count: Include count of items.
    :type count: bool
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://graph.microsoft.com/v1.0'
        self._config = PeopleConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.users = UsersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_insights = UsersInsightsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_insights_shared = UsersInsightsSharedOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_insights_trending = UsersInsightsTrendingOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_insights_used = UsersInsightsUsedOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "People":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
