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

from ._configuration import CalendarConfiguration
from .operations import GroupsOperations
from .operations import GroupsCalendarOperations
from .operations import GroupsCalendarCalendarViewOperations
from .operations import GroupsCalendarEventsOperations
from .operations import GroupsCalendarViewOperations
from .operations import GroupsCalendarViewCalendarOperations
from .operations import GroupsEventsOperations
from .operations import GroupsEventsCalendarOperations
from .operations import PlacesPlaceOperations
from .operations import UsersOperations
from .operations import UsersCalendarOperations
from .operations import UsersCalendarCalendarViewOperations
from .operations import UsersCalendarEventsOperations
from .operations import UsersCalendarGroupsOperations
from .operations import UsersCalendarGroupsCalendarsOperations
from .operations import UsersCalendarGroupsCalendarsCalendarViewOperations
from .operations import UsersCalendarGroupsCalendarsEventsOperations
from .operations import UsersCalendarsOperations
from .operations import UsersCalendarsCalendarViewOperations
from .operations import UsersCalendarsEventsOperations
from .operations import UsersCalendarViewOperations
from .operations import UsersCalendarViewCalendarOperations
from .operations import UsersEventsOperations
from .operations import UsersEventsCalendarOperations
from .. import models


class Calendar(object):
    """Calendar.

    :ivar groups: GroupsOperations operations
    :vartype groups: calendar.aio.operations.GroupsOperations
    :ivar groups_calendar: GroupsCalendarOperations operations
    :vartype groups_calendar: calendar.aio.operations.GroupsCalendarOperations
    :ivar groups_calendar_calendar_view: GroupsCalendarCalendarViewOperations operations
    :vartype groups_calendar_calendar_view: calendar.aio.operations.GroupsCalendarCalendarViewOperations
    :ivar groups_calendar_events: GroupsCalendarEventsOperations operations
    :vartype groups_calendar_events: calendar.aio.operations.GroupsCalendarEventsOperations
    :ivar groups_calendar_view: GroupsCalendarViewOperations operations
    :vartype groups_calendar_view: calendar.aio.operations.GroupsCalendarViewOperations
    :ivar groups_calendar_view_calendar: GroupsCalendarViewCalendarOperations operations
    :vartype groups_calendar_view_calendar: calendar.aio.operations.GroupsCalendarViewCalendarOperations
    :ivar groups_events: GroupsEventsOperations operations
    :vartype groups_events: calendar.aio.operations.GroupsEventsOperations
    :ivar groups_events_calendar: GroupsEventsCalendarOperations operations
    :vartype groups_events_calendar: calendar.aio.operations.GroupsEventsCalendarOperations
    :ivar places_place: PlacesPlaceOperations operations
    :vartype places_place: calendar.aio.operations.PlacesPlaceOperations
    :ivar users: UsersOperations operations
    :vartype users: calendar.aio.operations.UsersOperations
    :ivar users_calendar: UsersCalendarOperations operations
    :vartype users_calendar: calendar.aio.operations.UsersCalendarOperations
    :ivar users_calendar_calendar_view: UsersCalendarCalendarViewOperations operations
    :vartype users_calendar_calendar_view: calendar.aio.operations.UsersCalendarCalendarViewOperations
    :ivar users_calendar_events: UsersCalendarEventsOperations operations
    :vartype users_calendar_events: calendar.aio.operations.UsersCalendarEventsOperations
    :ivar users_calendar_groups: UsersCalendarGroupsOperations operations
    :vartype users_calendar_groups: calendar.aio.operations.UsersCalendarGroupsOperations
    :ivar users_calendar_groups_calendars: UsersCalendarGroupsCalendarsOperations operations
    :vartype users_calendar_groups_calendars: calendar.aio.operations.UsersCalendarGroupsCalendarsOperations
    :ivar users_calendar_groups_calendars_calendar_view: UsersCalendarGroupsCalendarsCalendarViewOperations operations
    :vartype users_calendar_groups_calendars_calendar_view: calendar.aio.operations.UsersCalendarGroupsCalendarsCalendarViewOperations
    :ivar users_calendar_groups_calendars_events: UsersCalendarGroupsCalendarsEventsOperations operations
    :vartype users_calendar_groups_calendars_events: calendar.aio.operations.UsersCalendarGroupsCalendarsEventsOperations
    :ivar users_calendars: UsersCalendarsOperations operations
    :vartype users_calendars: calendar.aio.operations.UsersCalendarsOperations
    :ivar users_calendars_calendar_view: UsersCalendarsCalendarViewOperations operations
    :vartype users_calendars_calendar_view: calendar.aio.operations.UsersCalendarsCalendarViewOperations
    :ivar users_calendars_events: UsersCalendarsEventsOperations operations
    :vartype users_calendars_events: calendar.aio.operations.UsersCalendarsEventsOperations
    :ivar users_calendar_view: UsersCalendarViewOperations operations
    :vartype users_calendar_view: calendar.aio.operations.UsersCalendarViewOperations
    :ivar users_calendar_view_calendar: UsersCalendarViewCalendarOperations operations
    :vartype users_calendar_view_calendar: calendar.aio.operations.UsersCalendarViewCalendarOperations
    :ivar users_events: UsersEventsOperations operations
    :vartype users_events: calendar.aio.operations.UsersEventsOperations
    :ivar users_events_calendar: UsersEventsCalendarOperations operations
    :vartype users_events_calendar: calendar.aio.operations.UsersEventsCalendarOperations
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
        self._config = CalendarConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.groups = GroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groups_calendar = GroupsCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groups_calendar_calendar_view = GroupsCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groups_calendar_events = GroupsCalendarEventsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groups_calendar_view = GroupsCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groups_calendar_view_calendar = GroupsCalendarViewCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groups_events = GroupsEventsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groups_events_calendar = GroupsEventsCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.places_place = PlacesPlaceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users = UsersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_calendar = UsersCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_calendar_calendar_view = UsersCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_calendar_events = UsersCalendarEventsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_calendar_groups = UsersCalendarGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_calendar_groups_calendars = UsersCalendarGroupsCalendarsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_calendar_groups_calendars_calendar_view = UsersCalendarGroupsCalendarsCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_calendar_groups_calendars_events = UsersCalendarGroupsCalendarsEventsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_calendars = UsersCalendarsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_calendars_calendar_view = UsersCalendarsCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_calendars_events = UsersCalendarsEventsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_calendar_view = UsersCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_calendar_view_calendar = UsersCalendarViewCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_events = UsersEventsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_events_calendar = UsersEventsCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "Calendar":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
