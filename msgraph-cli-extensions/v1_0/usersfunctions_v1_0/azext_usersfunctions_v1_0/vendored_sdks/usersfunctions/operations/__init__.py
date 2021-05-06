# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._users_activities_operations import UsersActivitiesOperations
from ._users_calendar_calendar_view_calendar_operations import UsersCalendarCalendarViewCalendarOperations
from ._users_calendar_calendar_view_instances_operations import UsersCalendarCalendarViewInstancesOperations
from ._users_calendar_calendar_view_operations import UsersCalendarCalendarViewOperations
from ._users_calendar_events_calendar_operations import UsersCalendarEventsCalendarOperations
from ._users_calendar_events_instances_operations import UsersCalendarEventsInstancesOperations
from ._users_calendar_events_operations import UsersCalendarEventsOperations
from ._users_calendar_operations import UsersCalendarOperations
from ._users_calendar_groups_calendars_calendar_view_calendar_operations import UsersCalendarGroupsCalendarsCalendarViewCalendarOperations
from ._users_calendar_groups_calendars_calendar_view_instances_operations import UsersCalendarGroupsCalendarsCalendarViewInstancesOperations
from ._users_calendar_groups_calendars_calendar_view_operations import UsersCalendarGroupsCalendarsCalendarViewOperations
from ._users_calendar_groups_calendars_events_calendar_operations import UsersCalendarGroupsCalendarsEventsCalendarOperations
from ._users_calendar_groups_calendars_events_instances_operations import UsersCalendarGroupsCalendarsEventsInstancesOperations
from ._users_calendar_groups_calendars_events_operations import UsersCalendarGroupsCalendarsEventsOperations
from ._users_calendar_groups_calendars_operations import UsersCalendarGroupsCalendarsOperations
from ._users_calendars_calendar_view_calendar_operations import UsersCalendarsCalendarViewCalendarOperations
from ._users_calendars_calendar_view_instances_operations import UsersCalendarsCalendarViewInstancesOperations
from ._users_calendars_calendar_view_operations import UsersCalendarsCalendarViewOperations
from ._users_calendars_events_calendar_operations import UsersCalendarsEventsCalendarOperations
from ._users_calendars_events_instances_operations import UsersCalendarsEventsInstancesOperations
from ._users_calendars_events_operations import UsersCalendarsEventsOperations
from ._users_calendars_operations import UsersCalendarsOperations
from ._users_calendar_view_calendar_calendar_view_operations import UsersCalendarViewCalendarCalendarViewOperations
from ._users_calendar_view_calendar_events_operations import UsersCalendarViewCalendarEventsOperations
from ._users_calendar_view_calendar_operations import UsersCalendarViewCalendarOperations
from ._users_calendar_view_instances_operations import UsersCalendarViewInstancesOperations
from ._users_calendar_view_operations import UsersCalendarViewOperations
from ._users_contact_folders_child_folders_operations import UsersContactFoldersChildFoldersOperations
from ._users_contact_folders_contacts_operations import UsersContactFoldersContactsOperations
from ._users_contact_folders_operations import UsersContactFoldersOperations
from ._users_contacts_operations import UsersContactsOperations
from ._users_events_calendar_calendar_view_operations import UsersEventsCalendarCalendarViewOperations
from ._users_events_calendar_events_operations import UsersEventsCalendarEventsOperations
from ._users_events_calendar_operations import UsersEventsCalendarOperations
from ._users_events_instances_operations import UsersEventsInstancesOperations
from ._users_events_operations import UsersEventsOperations
from ._users_mail_folders_child_folders_operations import UsersMailFoldersChildFoldersOperations
from ._users_mail_folders_messages_operations import UsersMailFoldersMessagesOperations
from ._users_mail_folders_operations import UsersMailFoldersOperations
from ._users_managed_app_registrations_operations import UsersManagedAppRegistrationsOperations
from ._users_messages_operations import UsersMessagesOperations
from ._users_operations import UsersOperations
from ._users_onenote_notebooks_section_groups_sections_pages_operations import UsersOnenoteNotebooksSectionGroupsSectionsPagesOperations
from ._users_onenote_notebooks_sections_pages_operations import UsersOnenoteNotebooksSectionsPagesOperations
from ._users_onenote_notebooks_operations import UsersOnenoteNotebooksOperations
from ._users_onenote_pages_operations import UsersOnenotePagesOperations
from ._users_onenote_pages_parent_notebook_section_groups_sections_pages_operations import UsersOnenotePagesParentNotebookSectionGroupsSectionsPagesOperations
from ._users_onenote_pages_parent_notebook_sections_pages_operations import UsersOnenotePagesParentNotebookSectionsPagesOperations
from ._users_onenote_pages_parent_section_pages_operations import UsersOnenotePagesParentSectionPagesOperations
from ._users_onenote_section_groups_parent_notebook_sections_pages_operations import UsersOnenoteSectionGroupsParentNotebookSectionsPagesOperations
from ._users_onenote_section_groups_sections_pages_operations import UsersOnenoteSectionGroupsSectionsPagesOperations
from ._users_onenote_sections_pages_operations import UsersOnenoteSectionsPagesOperations
from ._users_outlook_operations import UsersOutlookOperations

__all__ = [
    'UsersActivitiesOperations',
    'UsersCalendarCalendarViewCalendarOperations',
    'UsersCalendarCalendarViewInstancesOperations',
    'UsersCalendarCalendarViewOperations',
    'UsersCalendarEventsCalendarOperations',
    'UsersCalendarEventsInstancesOperations',
    'UsersCalendarEventsOperations',
    'UsersCalendarOperations',
    'UsersCalendarGroupsCalendarsCalendarViewCalendarOperations',
    'UsersCalendarGroupsCalendarsCalendarViewInstancesOperations',
    'UsersCalendarGroupsCalendarsCalendarViewOperations',
    'UsersCalendarGroupsCalendarsEventsCalendarOperations',
    'UsersCalendarGroupsCalendarsEventsInstancesOperations',
    'UsersCalendarGroupsCalendarsEventsOperations',
    'UsersCalendarGroupsCalendarsOperations',
    'UsersCalendarsCalendarViewCalendarOperations',
    'UsersCalendarsCalendarViewInstancesOperations',
    'UsersCalendarsCalendarViewOperations',
    'UsersCalendarsEventsCalendarOperations',
    'UsersCalendarsEventsInstancesOperations',
    'UsersCalendarsEventsOperations',
    'UsersCalendarsOperations',
    'UsersCalendarViewCalendarCalendarViewOperations',
    'UsersCalendarViewCalendarEventsOperations',
    'UsersCalendarViewCalendarOperations',
    'UsersCalendarViewInstancesOperations',
    'UsersCalendarViewOperations',
    'UsersContactFoldersChildFoldersOperations',
    'UsersContactFoldersContactsOperations',
    'UsersContactFoldersOperations',
    'UsersContactsOperations',
    'UsersEventsCalendarCalendarViewOperations',
    'UsersEventsCalendarEventsOperations',
    'UsersEventsCalendarOperations',
    'UsersEventsInstancesOperations',
    'UsersEventsOperations',
    'UsersMailFoldersChildFoldersOperations',
    'UsersMailFoldersMessagesOperations',
    'UsersMailFoldersOperations',
    'UsersManagedAppRegistrationsOperations',
    'UsersMessagesOperations',
    'UsersOperations',
    'UsersOnenoteNotebooksSectionGroupsSectionsPagesOperations',
    'UsersOnenoteNotebooksSectionsPagesOperations',
    'UsersOnenoteNotebooksOperations',
    'UsersOnenotePagesOperations',
    'UsersOnenotePagesParentNotebookSectionGroupsSectionsPagesOperations',
    'UsersOnenotePagesParentNotebookSectionsPagesOperations',
    'UsersOnenotePagesParentSectionPagesOperations',
    'UsersOnenoteSectionGroupsParentNotebookSectionsPagesOperations',
    'UsersOnenoteSectionGroupsSectionsPagesOperations',
    'UsersOnenoteSectionsPagesOperations',
    'UsersOutlookOperations',
]
