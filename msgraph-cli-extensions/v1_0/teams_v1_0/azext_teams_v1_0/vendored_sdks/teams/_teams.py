# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import TeamsConfiguration
from .operations import ChatsChatOperations
from .operations import ChatsOperations
from .operations import GroupsOperations
from .operations import TeamsTeamOperations
from .operations import TeamsOperations
from .operations import TeamsChannelsOperations
from .operations import TeamsChannelsMessagesOperations
from .operations import TeamsChannelsTabsOperations
from .operations import TeamsInstalledAppsOperations
from .operations import TeamsPrimaryChannelOperations
from .operations import TeamsPrimaryChannelMessagesOperations
from .operations import TeamsPrimaryChannelTabsOperations
from .operations import TeamsScheduleOperations
from .operations import TeamworkTeamworkOperations
from .operations import TeamworkOperations
from .operations import UsersOperations
from . import models


class Teams(object):
    """Teams.

    :ivar chats_chat: ChatsChatOperations operations
    :vartype chats_chat: teams.operations.ChatsChatOperations
    :ivar chats: ChatsOperations operations
    :vartype chats: teams.operations.ChatsOperations
    :ivar groups: GroupsOperations operations
    :vartype groups: teams.operations.GroupsOperations
    :ivar teams_team: TeamsTeamOperations operations
    :vartype teams_team: teams.operations.TeamsTeamOperations
    :ivar teams: TeamsOperations operations
    :vartype teams: teams.operations.TeamsOperations
    :ivar teams_channels: TeamsChannelsOperations operations
    :vartype teams_channels: teams.operations.TeamsChannelsOperations
    :ivar teams_channels_messages: TeamsChannelsMessagesOperations operations
    :vartype teams_channels_messages: teams.operations.TeamsChannelsMessagesOperations
    :ivar teams_channels_tabs: TeamsChannelsTabsOperations operations
    :vartype teams_channels_tabs: teams.operations.TeamsChannelsTabsOperations
    :ivar teams_installed_apps: TeamsInstalledAppsOperations operations
    :vartype teams_installed_apps: teams.operations.TeamsInstalledAppsOperations
    :ivar teams_primary_channel: TeamsPrimaryChannelOperations operations
    :vartype teams_primary_channel: teams.operations.TeamsPrimaryChannelOperations
    :ivar teams_primary_channel_messages: TeamsPrimaryChannelMessagesOperations operations
    :vartype teams_primary_channel_messages: teams.operations.TeamsPrimaryChannelMessagesOperations
    :ivar teams_primary_channel_tabs: TeamsPrimaryChannelTabsOperations operations
    :vartype teams_primary_channel_tabs: teams.operations.TeamsPrimaryChannelTabsOperations
    :ivar teams_schedule: TeamsScheduleOperations operations
    :vartype teams_schedule: teams.operations.TeamsScheduleOperations
    :ivar teamwork_teamwork: TeamworkTeamworkOperations operations
    :vartype teamwork_teamwork: teams.operations.TeamworkTeamworkOperations
    :ivar teamwork: TeamworkOperations operations
    :vartype teamwork: teams.operations.TeamworkOperations
    :ivar users: UsersOperations operations
    :vartype users: teams.operations.UsersOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
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
        credential,  # type: "TokenCredential"
        top=None,  # type: Optional[int]
        skip=None,  # type: Optional[int]
        search=None,  # type: Optional[str]
        filter=None,  # type: Optional[str]
        count=None,  # type: Optional[bool]
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://graph.microsoft.com/v1.0'
        self._config = TeamsConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.chats_chat = ChatsChatOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.chats = ChatsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groups = GroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_team = TeamsTeamOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams = TeamsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_channels = TeamsChannelsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_channels_messages = TeamsChannelsMessagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_channels_tabs = TeamsChannelsTabsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_installed_apps = TeamsInstalledAppsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_primary_channel = TeamsPrimaryChannelOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_primary_channel_messages = TeamsPrimaryChannelMessagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_primary_channel_tabs = TeamsPrimaryChannelTabsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teams_schedule = TeamsScheduleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teamwork_teamwork = TeamworkTeamworkOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.teamwork = TeamworkOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users = UsersOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> Teams
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
