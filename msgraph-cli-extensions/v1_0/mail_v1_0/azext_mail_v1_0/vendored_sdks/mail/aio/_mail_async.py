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

from ._configuration_async import MailConfiguration
from .operations_async import UserOperations
from .operations_async import UserInferenceClassificationOperations
from .operations_async import UserMailFolderOperations
from .operations_async import UserMailFolderMessageOperations
from .operations_async import UserMessageOperations
from .. import models


class Mail(object):
    """Mail.

    :ivar user: UserOperations operations
    :vartype user: mail.aio.operations_async.UserOperations
    :ivar user_inference_classification: UserInferenceClassificationOperations operations
    :vartype user_inference_classification: mail.aio.operations_async.UserInferenceClassificationOperations
    :ivar user_mail_folder: UserMailFolderOperations operations
    :vartype user_mail_folder: mail.aio.operations_async.UserMailFolderOperations
    :ivar user_mail_folder_message: UserMailFolderMessageOperations operations
    :vartype user_mail_folder_message: mail.aio.operations_async.UserMailFolderMessageOperations
    :ivar user_message: UserMessageOperations operations
    :vartype user_message: mail.aio.operations_async.UserMessageOperations
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
        self._config = MailConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_inference_classification = UserInferenceClassificationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_mail_folder = UserMailFolderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_mail_folder_message = UserMailFolderMessageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_message = UserMessageOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "Mail":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
