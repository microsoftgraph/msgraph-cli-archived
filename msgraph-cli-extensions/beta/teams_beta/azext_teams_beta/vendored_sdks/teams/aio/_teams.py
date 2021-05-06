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

from ._configuration import TeamsConfiguration
from .operations import AppCatalogsOperations
from .operations import AppCatalogsTeamsAppsOperations
from .operations import ChatsChatOperations
from .operations import ChatsOperations
from .operations import ChatsInstalledAppsOperations
from .operations import ChatsMembersOperations
from .operations import ChatsMessagesOperations
from .operations import ChatsMessagesRepliesOperations
from .operations import ChatsTabsOperations
from .operations import GroupsOperations
from .operations import TeamsTeamOperations
from .operations import TeamsOperations
from .operations import TeamsChannelsOperations
from .operations import TeamsChannelsMembersOperations
from .operations import TeamsChannelsMessagesOperations
from .operations import TeamsChannelsMessagesRepliesOperations
from .operations import TeamsChannelsTabsOperations
from .operations import TeamsInstalledAppsOperations
from .operations import TeamsMembersOperations
from .operations import TeamsPrimaryChannelOperations
from .operations import TeamsPrimaryChannelMembersOperations
from .operations import TeamsPrimaryChannelMessagesOperations
from .operations import TeamsPrimaryChannelMessagesRepliesOperations
from .operations import TeamsPrimaryChannelTabsOperations
from .operations import TeamsScheduleOperations
from .operations import TeamsScheduleTimeCardsOperations
from .operations import TeamworkTeamworkOperations
from .operations import TeamworkOperations
from .operations import UsersOperations
from .operations import UsersTeamworkOperations
from .operations import UsersTeamworkInstalledAppsOperations
from .. import models


class Teams(object):
    """Teams.

    :ivar app_catalogs: AppCatalogsOperations operations
    :vartype app_catalogs: teams.aio.operations.AppCatalogsOperations
    :ivar app_catalogs_teams_apps: AppCatalogsTeamsAppsOperations operations
    :vartype app_catalogs_teams_apps: teams.aio.operations.AppCatalogsTeamsAppsOperations
    :ivar chats_chat: ChatsChatOperations operations
    :vartype chats_chat: teams.aio.operations.ChatsChatOperations
    :ivar chats: ChatsOperations operations
    :vartype chats: teams.aio.operations.ChatsOperations
    :ivar chats_installed_apps: ChatsInstalledAppsOperations operations
    :vartype chats_installed_apps: teams.aio.operations.ChatsInstalledAppsOperations
    :ivar chats_members: ChatsMembersOperations operations
    :vartype chats_members: teams.aio.operations.ChatsMembersOperations
    :ivar chats_messages: ChatsMessagesOperations operations
    :vartype chats_messages: teams.aio.operations.ChatsMessagesOperations
    :ivar chats_messages_replies: ChatsMessagesRepliesOperations operations
    :vartype chats_messages_replies: teams.aio.operations.ChatsMessagesRepliesOperations
    :ivar chats_tabs: ChatsTabsOperations operations
    :vartype chats_tabs: teams.aio.operations.ChatsTabsOperations
    :ivar groups: GroupsOperations operations
    :vartype groups: teams.aio.operations.GroupsOperations
    :ivar teams_team: TeamsTeamOperations operations
    :vartype teams_team: teams.aio.operations.TeamsTeamOperations
    :ivar teams: TeamsOperations operations
    :vartype teams: teams.aio.operations.TeamsOperations
    :ivar teams_channels: TeamsChannelsOperations operations
    :vartype teams_channels: teams.aio.operations.TeamsChannelsOperations
    :ivar teams_channels_members: TeamsChannelsMembersOperations operations
    :vartype teams_channels_members: teams.aio.operations.TeamsChannelsMembersOperations
    :ivar teams_channels_messages: TeamsChannelsMessagesOperations operations
    :vartype teams_channels_messages: teams.aio.operations.TeamsChannelsMessagesOperations
    :ivar teams_channels_messages_replies: TeamsChannelsMessagesRepliesOperations operations
    :vartype teams_channels_messages_replies: teams.aio.operations.TeamsChannelsMessagesRepliesOperations
    :ivar teams_channels_tabs: TeamsChannelsTabsOperations operations
    :vartype teams_channels_tabs: teams.aio.operations.TeamsChannelsTabsOperations
    :ivar teams_installed_apps: TeamsInstalledAppsOperations operations
    :vartype teams_installed_apps: teams.aio.operations.TeamsInstalledAppsOperations
    :ivar teams_members: TeamsMembersOperations operations
    :vartype teams_members: teams.aio.operations.TeamsMembersOperations
    :ivar teams_primary_channel: TeamsPrimaryChannelOperations operations
    :vartype teams_primary_channel: teams.aio.operations.TeamsPrimaryChannelOperations
    :ivar teams_primary_channel_members: TeamsPrimaryChannelMembersOperations operations
    :vartype teams_primary_channel_members: teams.aio.operations.TeamsPrimaryChannelMembersOperations
    :ivar teams_primary_channel_messages: TeamsPrimaryChannelMessagesOperations operations
    :vartype teams_primary_channel_messages: teams.aio.operations.TeamsPrimaryChannelMessagesOperations
    :ivar teams_primary_channel_messages_replies: TeamsPrimaryChannelMessagesRepliesOperations operations
    :vartype teams_primary_channel_messages_replies: teams.aio.operations.TeamsPrimaryChannelMessagesRepliesOperations
    :ivar teams_primary_channel_tabs: TeamsPrimaryChannelTabsOperations operations
    :vartype teams_primary_channel_tabs: teams.aio.operations.TeamsPrimaryChannelTabsOperations
    :ivar teams_schedule: TeamsScheduleOperations operations
    :vartype teams_schedule: teams.aio.operations.TeamsScheduleOperations
    :ivar teams_schedule_time_cards: TeamsScheduleTimeCardsOperations operations
    :vartype teams_schedule_time_cards: teams.aio.operations.TeamsScheduleTimeCardsOperations
    :ivar teamwork_teamwork: TeamworkTeamworkOperations operations
    :vartype teamwork_teamwork: teams.aio.operations.TeamworkTeamworkOperations
    :ivar teamwork: TeamworkOperations operations
    :vartype teamwork: teams.aio.operations.TeamworkOperations
    :ivar users: UsersOperations operations
    :vartype users: teams.aio.operations.UsersOperations
    :ivar users_teamwork: UsersTeamworkOperations operations
    :vartype users_teamwork: teams.aio.operations.UsersTeamworkOperations
    :ivar users_teamwork_installed_apps: UsersTeamworkInstalledAppsOperations operations
    :vartype users_teamwork_installed_apps: teams.aio.operations.UsersTeamworkInstalledAppsOperations
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
            base_url = 'https://graph.microsoft.com/beta'
        self._config = TeamsConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.app_catalogs = AppCatalogsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.app_catalogs_teams_apps = AppCatalogsTeamsAppsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.chats_chat = ChatsChatOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.chats = ChatsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.chats_installed_apps = ChatsInstalledAppsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.chats_members = ChatsMembersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.chats_messages = ChatsMessagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.chats_messages_replies = ChatsMessagesRepliesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.chats_tabs = ChatsTabsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groups = GroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_team = TeamsTeamOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams = TeamsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_channels = TeamsChannelsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_channels_members = TeamsChannelsMembersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_channels_messages = TeamsChannelsMessagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_channels_messages_replies = TeamsChannelsMessagesRepliesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_channels_tabs = TeamsChannelsTabsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_installed_apps = TeamsInstalledAppsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_members = TeamsMembersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_primary_channel = TeamsPrimaryChannelOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_primary_channel_members = TeamsPrimaryChannelMembersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_primary_channel_messages = TeamsPrimaryChannelMessagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_primary_channel_messages_replies = TeamsPrimaryChannelMessagesRepliesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_primary_channel_tabs = TeamsPrimaryChannelTabsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_schedule = TeamsScheduleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_schedule_time_cards = TeamsScheduleTimeCardsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teamwork_teamwork = TeamworkTeamworkOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teamwork = TeamworkOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users = UsersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_teamwork = UsersTeamworkOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_teamwork_installed_apps = UsersTeamworkInstalledAppsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "Teams":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
