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

from ._configuration_async import TeamsChatsConfiguration
from .operations_async import ChatChatOperations
from .operations_async import ChatOperations
from .operations_async import ChatInstalledAppOperations
from .operations_async import ChatMessageOperations
from .operations_async import ChatMessageReplyOperations
from .operations_async import UserOperations
from .. import models


class TeamsChats(object):
    """TeamsChats.

    :ivar chat_chat: ChatChatOperations operations
    :vartype chat_chat: teams_chats.aio.operations_async.ChatChatOperations
    :ivar chat: ChatOperations operations
    :vartype chat: teams_chats.aio.operations_async.ChatOperations
    :ivar chat_installed_app: ChatInstalledAppOperations operations
    :vartype chat_installed_app: teams_chats.aio.operations_async.ChatInstalledAppOperations
    :ivar chat_message: ChatMessageOperations operations
    :vartype chat_message: teams_chats.aio.operations_async.ChatMessageOperations
    :ivar chat_message_reply: ChatMessageReplyOperations operations
    :vartype chat_message_reply: teams_chats.aio.operations_async.ChatMessageReplyOperations
    :ivar user: UserOperations operations
    :vartype user: teams_chats.aio.operations_async.UserOperations
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
            base_url = 'https://graph.microsoft.com/beta'
        self._config = TeamsChatsConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.chat_chat = ChatChatOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.chat = ChatOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.chat_installed_app = ChatInstalledAppOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.chat_message = ChatMessageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.chat_message_reply = ChatMessageReplyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "TeamsChats":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)