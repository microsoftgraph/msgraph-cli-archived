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

from ._configuration_async import TeamsConfiguration
from .operations_async import ChatChatOperations
from .operations_async import ChatOperations
from .operations_async import GroupOperations
from .operations_async import TeamTeamOperations
from .operations_async import TeamOperations
from .operations_async import TeamChannelOperations
from .operations_async import TeamChannelMessageOperations
from .operations_async import TeamChannelTabOperations
from .operations_async import TeamInstalledAppOperations
from .operations_async import TeamPrimaryChannelOperations
from .operations_async import TeamPrimaryChannelMessageOperations
from .operations_async import TeamPrimaryChannelTabOperations
from .operations_async import TeamScheduleOperations
from .operations_async import TeamworkTeamworkOperations
from .operations_async import TeamworkOperations
from .operations_async import UserOperations
from .. import models


class Teams(object):
    """Teams.

    :ivar chat_chat: ChatChatOperations operations
    :vartype chat_chat: teams.aio.operations_async.ChatChatOperations
    :ivar chat: ChatOperations operations
    :vartype chat: teams.aio.operations_async.ChatOperations
    :ivar group: GroupOperations operations
    :vartype group: teams.aio.operations_async.GroupOperations
    :ivar team_team: TeamTeamOperations operations
    :vartype team_team: teams.aio.operations_async.TeamTeamOperations
    :ivar team: TeamOperations operations
    :vartype team: teams.aio.operations_async.TeamOperations
    :ivar team_channel: TeamChannelOperations operations
    :vartype team_channel: teams.aio.operations_async.TeamChannelOperations
    :ivar team_channel_message: TeamChannelMessageOperations operations
    :vartype team_channel_message: teams.aio.operations_async.TeamChannelMessageOperations
    :ivar team_channel_tab: TeamChannelTabOperations operations
    :vartype team_channel_tab: teams.aio.operations_async.TeamChannelTabOperations
    :ivar team_installed_app: TeamInstalledAppOperations operations
    :vartype team_installed_app: teams.aio.operations_async.TeamInstalledAppOperations
    :ivar team_primary_channel: TeamPrimaryChannelOperations operations
    :vartype team_primary_channel: teams.aio.operations_async.TeamPrimaryChannelOperations
    :ivar team_primary_channel_message: TeamPrimaryChannelMessageOperations operations
    :vartype team_primary_channel_message: teams.aio.operations_async.TeamPrimaryChannelMessageOperations
    :ivar team_primary_channel_tab: TeamPrimaryChannelTabOperations operations
    :vartype team_primary_channel_tab: teams.aio.operations_async.TeamPrimaryChannelTabOperations
    :ivar team_schedule: TeamScheduleOperations operations
    :vartype team_schedule: teams.aio.operations_async.TeamScheduleOperations
    :ivar teamwork_teamwork: TeamworkTeamworkOperations operations
    :vartype teamwork_teamwork: teams.aio.operations_async.TeamworkTeamworkOperations
    :ivar teamwork: TeamworkOperations operations
    :vartype teamwork: teams.aio.operations_async.TeamworkOperations
    :ivar user: UserOperations operations
    :vartype user: teams.aio.operations_async.UserOperations
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
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
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
        self._config = TeamsConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.chat_chat = ChatChatOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.chat = ChatOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group = GroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_team = TeamTeamOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team = TeamOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_channel = TeamChannelOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_channel_message = TeamChannelMessageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_channel_tab = TeamChannelTabOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_installed_app = TeamInstalledAppOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_primary_channel = TeamPrimaryChannelOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_primary_channel_message = TeamPrimaryChannelMessageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_primary_channel_tab = TeamPrimaryChannelTabOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.team_schedule = TeamScheduleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teamwork_teamwork = TeamworkTeamworkOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teamwork = TeamworkOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "Teams":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
