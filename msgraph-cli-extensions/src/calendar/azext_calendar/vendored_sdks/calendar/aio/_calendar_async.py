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

from ._configuration_async import CalendarConfiguration
from .operations_async import GroupOperations
from .operations_async import GroupCalendarOperations
from .operations_async import GroupCalendarCalendarViewOperations
from .operations_async import GroupCalendarEventOperations
from .operations_async import GroupCalendarViewOperations
from .operations_async import GroupCalendarViewCalendarOperations
from .operations_async import GroupEventOperations
from .operations_async import GroupEventCalendarOperations
from .operations_async import PlacePlaceOperations
from .operations_async import UserOperations
from .operations_async import UserCalendarOperations
from .operations_async import UserCalendarCalendarViewOperations
from .operations_async import UserCalendarEventOperations
from .operations_async import UserCalendarGroupOperations
from .operations_async import UserCalendarGroupCalendarOperations
from .operations_async import UserCalendarGroupCalendarCalendarViewOperations
from .operations_async import UserCalendarGroupCalendarEventOperations
from .operations_async import UserCalendarOperations
from .operations_async import UserCalendarCalendarViewOperations
from .operations_async import UserCalendarEventOperations
from .operations_async import UserCalendarViewOperations
from .operations_async import UserCalendarViewCalendarOperations
from .operations_async import UserEventOperations
from .operations_async import UserEventCalendarOperations
from .. import models


class Calendar(object):
    """Calendar.

    :ivar group: GroupOperations operations
    :vartype group: calendar.aio.operations_async.GroupOperations
    :ivar group_calendar: GroupCalendarOperations operations
    :vartype group_calendar: calendar.aio.operations_async.GroupCalendarOperations
    :ivar group_calendar_calendar_view: GroupCalendarCalendarViewOperations operations
    :vartype group_calendar_calendar_view: calendar.aio.operations_async.GroupCalendarCalendarViewOperations
    :ivar group_calendar_event: GroupCalendarEventOperations operations
    :vartype group_calendar_event: calendar.aio.operations_async.GroupCalendarEventOperations
    :ivar group_calendar_view: GroupCalendarViewOperations operations
    :vartype group_calendar_view: calendar.aio.operations_async.GroupCalendarViewOperations
    :ivar group_calendar_view_calendar: GroupCalendarViewCalendarOperations operations
    :vartype group_calendar_view_calendar: calendar.aio.operations_async.GroupCalendarViewCalendarOperations
    :ivar group_event: GroupEventOperations operations
    :vartype group_event: calendar.aio.operations_async.GroupEventOperations
    :ivar group_event_calendar: GroupEventCalendarOperations operations
    :vartype group_event_calendar: calendar.aio.operations_async.GroupEventCalendarOperations
    :ivar place_place: PlacePlaceOperations operations
    :vartype place_place: calendar.aio.operations_async.PlacePlaceOperations
    :ivar user: UserOperations operations
    :vartype user: calendar.aio.operations_async.UserOperations
    :ivar user_calendar: UserCalendarOperations operations
    :vartype user_calendar: calendar.aio.operations_async.UserCalendarOperations
    :ivar user_calendar_calendar_view: UserCalendarCalendarViewOperations operations
    :vartype user_calendar_calendar_view: calendar.aio.operations_async.UserCalendarCalendarViewOperations
    :ivar user_calendar_event: UserCalendarEventOperations operations
    :vartype user_calendar_event: calendar.aio.operations_async.UserCalendarEventOperations
    :ivar user_calendar_group: UserCalendarGroupOperations operations
    :vartype user_calendar_group: calendar.aio.operations_async.UserCalendarGroupOperations
    :ivar user_calendar_group_calendar: UserCalendarGroupCalendarOperations operations
    :vartype user_calendar_group_calendar: calendar.aio.operations_async.UserCalendarGroupCalendarOperations
    :ivar user_calendar_group_calendar_calendar_view: UserCalendarGroupCalendarCalendarViewOperations operations
    :vartype user_calendar_group_calendar_calendar_view: calendar.aio.operations_async.UserCalendarGroupCalendarCalendarViewOperations
    :ivar user_calendar_group_calendar_event: UserCalendarGroupCalendarEventOperations operations
    :vartype user_calendar_group_calendar_event: calendar.aio.operations_async.UserCalendarGroupCalendarEventOperations
    :ivar user_calendar: UserCalendarOperations operations
    :vartype user_calendar: calendar.aio.operations_async.UserCalendarOperations
    :ivar user_calendar_calendar_view: UserCalendarCalendarViewOperations operations
    :vartype user_calendar_calendar_view: calendar.aio.operations_async.UserCalendarCalendarViewOperations
    :ivar user_calendar_event: UserCalendarEventOperations operations
    :vartype user_calendar_event: calendar.aio.operations_async.UserCalendarEventOperations
    :ivar user_calendar_view: UserCalendarViewOperations operations
    :vartype user_calendar_view: calendar.aio.operations_async.UserCalendarViewOperations
    :ivar user_calendar_view_calendar: UserCalendarViewCalendarOperations operations
    :vartype user_calendar_view_calendar: calendar.aio.operations_async.UserCalendarViewCalendarOperations
    :ivar user_event: UserEventOperations operations
    :vartype user_event: calendar.aio.operations_async.UserEventOperations
    :ivar user_event_calendar: UserEventCalendarOperations operations
    :vartype user_event_calendar: calendar.aio.operations_async.UserEventCalendarOperations
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
        self._config = CalendarConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.group = GroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_calendar = GroupCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_calendar_calendar_view = GroupCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_calendar_event = GroupCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_calendar_view = GroupCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_calendar_view_calendar = GroupCalendarViewCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_event = GroupEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.group_event_calendar = GroupEventCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.place_place = PlacePlaceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar = UserCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view = UserCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event = UserCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group = UserCalendarGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar = UserCalendarGroupCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_calendar_view = UserCalendarGroupCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_event = UserCalendarGroupCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar = UserCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view = UserCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event = UserCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view = UserCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view_calendar = UserCalendarViewCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event = UserEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event_calendar = UserEventCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "Calendar":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
