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

from ._configuration import CrossDeviceExperiencesConfiguration
from .operations import UsersOperations
from .operations import UsersActivitiesOperations
from .operations import UsersActivitiesHistoryItemsOperations
from . import models


class CrossDeviceExperiences(object):
    """CrossDeviceExperiences.

    :ivar users: UsersOperations operations
    :vartype users: cross_device_experiences.operations.UsersOperations
    :ivar users_activities: UsersActivitiesOperations operations
    :vartype users_activities: cross_device_experiences.operations.UsersActivitiesOperations
    :ivar users_activities_history_items: UsersActivitiesHistoryItemsOperations operations
    :vartype users_activities_history_items: cross_device_experiences.operations.UsersActivitiesHistoryItemsOperations
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
        self._config = CrossDeviceExperiencesConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.users = UsersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_activities = UsersActivitiesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_activities_history_items = UsersActivitiesHistoryItemsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> CrossDeviceExperiences
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)