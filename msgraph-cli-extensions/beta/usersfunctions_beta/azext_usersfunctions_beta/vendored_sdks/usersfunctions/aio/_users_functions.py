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

from ._configuration import UsersFunctionsConfiguration
from .operations import UserActivityOperations
from .operations import UserCalendarCalendarViewCalendarOperations
from .operations import UserCalendarCalendarViewExceptionOccurrenceOperations
from .operations import UserCalendarCalendarViewInstanceOperations
from .operations import UserCalendarCalendarViewOperations
from .operations import UserCalendarEventCalendarOperations
from .operations import UserCalendarEventExceptionOccurrenceOperations
from .operations import UserCalendarEventInstanceOperations
from .operations import UserCalendarEventOperations
from .operations import UserCalendarOperations
from .operations import UserCalendarGroupCalendarCalendarViewCalendarOperations
from .operations import UserCalendarGroupCalendarCalendarViewExceptionOccurrenceOperations
from .operations import UserCalendarGroupCalendarCalendarViewInstanceOperations
from .operations import UserCalendarGroupCalendarCalendarViewOperations
from .operations import UserCalendarGroupCalendarEventCalendarOperations
from .operations import UserCalendarGroupCalendarEventExceptionOccurrenceOperations
from .operations import UserCalendarGroupCalendarEventInstanceOperations
from .operations import UserCalendarGroupCalendarEventOperations
from .operations import UserCalendarGroupCalendarOperations
from .operations import UserCalendarCalendarViewCalendarOperations
from .operations import UserCalendarCalendarViewExceptionOccurrenceOperations
from .operations import UserCalendarCalendarViewInstanceOperations
from .operations import UserCalendarCalendarViewOperations
from .operations import UserCalendarEventCalendarOperations
from .operations import UserCalendarEventExceptionOccurrenceOperations
from .operations import UserCalendarEventInstanceOperations
from .operations import UserCalendarEventOperations
from .operations import UserCalendarOperations
from .operations import UserCalendarViewCalendarCalendarViewOperations
from .operations import UserCalendarViewCalendarEventOperations
from .operations import UserCalendarViewCalendarOperations
from .operations import UserCalendarViewExceptionOccurrenceOperations
from .operations import UserCalendarViewInstanceOperations
from .operations import UserCalendarViewOperations
from .operations import UserContactFolderChildFolderOperations
from .operations import UserContactFolderContactOperations
from .operations import UserContactFolderOperations
from .operations import UserContactOperations
from .operations import UserEventCalendarCalendarViewOperations
from .operations import UserEventCalendarEventOperations
from .operations import UserEventCalendarOperations
from .operations import UserEventExceptionOccurrenceOperations
from .operations import UserEventInstanceOperations
from .operations import UserEventOperations
from .operations import UserMailFolderChildFolderOperations
from .operations import UserMailFolderMessageOperations
from .operations import UserMailFolderOperations
from .operations import UserManagedAppRegistrationOperations
from .operations import UserManagedDeviceOperations
from .operations import UserMessageOperations
from .operations import UserOperations
from .operations import UserOnenoteNotebookSectionGroupSectionPageOperations
from .operations import UserOnenoteNotebookSectionPageOperations
from .operations import UserOnenoteNotebookOperations
from .operations import UserOnenotePageOperations
from .operations import UserOnenotePageParentNotebookSectionGroupSectionPageOperations
from .operations import UserOnenotePageParentNotebookSectionPageOperations
from .operations import UserOnenotePageParentSectionPageOperations
from .operations import UserOnenoteSectionGroupParentNotebookSectionPageOperations
from .operations import UserOnenoteSectionGroupSectionPageOperations
from .operations import UserOnenoteSectionPageOperations
from .operations import UserOutlookOperations
from .operations import UserPlannerAllOperations
from .operations import UserTodoListTaskOperations
from .operations import UserTodoListOperations
from .. import models


class UsersFunctions(object):
    """UsersFunctions.

    :ivar user_activity: UserActivityOperations operations
    :vartype user_activity: users_functions.aio.operations.UserActivityOperations
    :ivar user_calendar_calendar_view_calendar: UserCalendarCalendarViewCalendarOperations operations
    :vartype user_calendar_calendar_view_calendar: users_functions.aio.operations.UserCalendarCalendarViewCalendarOperations
    :ivar user_calendar_calendar_view_exception_occurrence: UserCalendarCalendarViewExceptionOccurrenceOperations operations
    :vartype user_calendar_calendar_view_exception_occurrence: users_functions.aio.operations.UserCalendarCalendarViewExceptionOccurrenceOperations
    :ivar user_calendar_calendar_view_instance: UserCalendarCalendarViewInstanceOperations operations
    :vartype user_calendar_calendar_view_instance: users_functions.aio.operations.UserCalendarCalendarViewInstanceOperations
    :ivar user_calendar_calendar_view: UserCalendarCalendarViewOperations operations
    :vartype user_calendar_calendar_view: users_functions.aio.operations.UserCalendarCalendarViewOperations
    :ivar user_calendar_event_calendar: UserCalendarEventCalendarOperations operations
    :vartype user_calendar_event_calendar: users_functions.aio.operations.UserCalendarEventCalendarOperations
    :ivar user_calendar_event_exception_occurrence: UserCalendarEventExceptionOccurrenceOperations operations
    :vartype user_calendar_event_exception_occurrence: users_functions.aio.operations.UserCalendarEventExceptionOccurrenceOperations
    :ivar user_calendar_event_instance: UserCalendarEventInstanceOperations operations
    :vartype user_calendar_event_instance: users_functions.aio.operations.UserCalendarEventInstanceOperations
    :ivar user_calendar_event: UserCalendarEventOperations operations
    :vartype user_calendar_event: users_functions.aio.operations.UserCalendarEventOperations
    :ivar user_calendar: UserCalendarOperations operations
    :vartype user_calendar: users_functions.aio.operations.UserCalendarOperations
    :ivar user_calendar_group_calendar_calendar_view_calendar: UserCalendarGroupCalendarCalendarViewCalendarOperations operations
    :vartype user_calendar_group_calendar_calendar_view_calendar: users_functions.aio.operations.UserCalendarGroupCalendarCalendarViewCalendarOperations
    :ivar user_calendar_group_calendar_calendar_view_exception_occurrence: UserCalendarGroupCalendarCalendarViewExceptionOccurrenceOperations operations
    :vartype user_calendar_group_calendar_calendar_view_exception_occurrence: users_functions.aio.operations.UserCalendarGroupCalendarCalendarViewExceptionOccurrenceOperations
    :ivar user_calendar_group_calendar_calendar_view_instance: UserCalendarGroupCalendarCalendarViewInstanceOperations operations
    :vartype user_calendar_group_calendar_calendar_view_instance: users_functions.aio.operations.UserCalendarGroupCalendarCalendarViewInstanceOperations
    :ivar user_calendar_group_calendar_calendar_view: UserCalendarGroupCalendarCalendarViewOperations operations
    :vartype user_calendar_group_calendar_calendar_view: users_functions.aio.operations.UserCalendarGroupCalendarCalendarViewOperations
    :ivar user_calendar_group_calendar_event_calendar: UserCalendarGroupCalendarEventCalendarOperations operations
    :vartype user_calendar_group_calendar_event_calendar: users_functions.aio.operations.UserCalendarGroupCalendarEventCalendarOperations
    :ivar user_calendar_group_calendar_event_exception_occurrence: UserCalendarGroupCalendarEventExceptionOccurrenceOperations operations
    :vartype user_calendar_group_calendar_event_exception_occurrence: users_functions.aio.operations.UserCalendarGroupCalendarEventExceptionOccurrenceOperations
    :ivar user_calendar_group_calendar_event_instance: UserCalendarGroupCalendarEventInstanceOperations operations
    :vartype user_calendar_group_calendar_event_instance: users_functions.aio.operations.UserCalendarGroupCalendarEventInstanceOperations
    :ivar user_calendar_group_calendar_event: UserCalendarGroupCalendarEventOperations operations
    :vartype user_calendar_group_calendar_event: users_functions.aio.operations.UserCalendarGroupCalendarEventOperations
    :ivar user_calendar_group_calendar: UserCalendarGroupCalendarOperations operations
    :vartype user_calendar_group_calendar: users_functions.aio.operations.UserCalendarGroupCalendarOperations
    :ivar user_calendar_calendar_view_calendar: UserCalendarCalendarViewCalendarOperations operations
    :vartype user_calendar_calendar_view_calendar: users_functions.aio.operations.UserCalendarCalendarViewCalendarOperations
    :ivar user_calendar_calendar_view_exception_occurrence: UserCalendarCalendarViewExceptionOccurrenceOperations operations
    :vartype user_calendar_calendar_view_exception_occurrence: users_functions.aio.operations.UserCalendarCalendarViewExceptionOccurrenceOperations
    :ivar user_calendar_calendar_view_instance: UserCalendarCalendarViewInstanceOperations operations
    :vartype user_calendar_calendar_view_instance: users_functions.aio.operations.UserCalendarCalendarViewInstanceOperations
    :ivar user_calendar_calendar_view: UserCalendarCalendarViewOperations operations
    :vartype user_calendar_calendar_view: users_functions.aio.operations.UserCalendarCalendarViewOperations
    :ivar user_calendar_event_calendar: UserCalendarEventCalendarOperations operations
    :vartype user_calendar_event_calendar: users_functions.aio.operations.UserCalendarEventCalendarOperations
    :ivar user_calendar_event_exception_occurrence: UserCalendarEventExceptionOccurrenceOperations operations
    :vartype user_calendar_event_exception_occurrence: users_functions.aio.operations.UserCalendarEventExceptionOccurrenceOperations
    :ivar user_calendar_event_instance: UserCalendarEventInstanceOperations operations
    :vartype user_calendar_event_instance: users_functions.aio.operations.UserCalendarEventInstanceOperations
    :ivar user_calendar_event: UserCalendarEventOperations operations
    :vartype user_calendar_event: users_functions.aio.operations.UserCalendarEventOperations
    :ivar user_calendar: UserCalendarOperations operations
    :vartype user_calendar: users_functions.aio.operations.UserCalendarOperations
    :ivar user_calendar_view_calendar_calendar_view: UserCalendarViewCalendarCalendarViewOperations operations
    :vartype user_calendar_view_calendar_calendar_view: users_functions.aio.operations.UserCalendarViewCalendarCalendarViewOperations
    :ivar user_calendar_view_calendar_event: UserCalendarViewCalendarEventOperations operations
    :vartype user_calendar_view_calendar_event: users_functions.aio.operations.UserCalendarViewCalendarEventOperations
    :ivar user_calendar_view_calendar: UserCalendarViewCalendarOperations operations
    :vartype user_calendar_view_calendar: users_functions.aio.operations.UserCalendarViewCalendarOperations
    :ivar user_calendar_view_exception_occurrence: UserCalendarViewExceptionOccurrenceOperations operations
    :vartype user_calendar_view_exception_occurrence: users_functions.aio.operations.UserCalendarViewExceptionOccurrenceOperations
    :ivar user_calendar_view_instance: UserCalendarViewInstanceOperations operations
    :vartype user_calendar_view_instance: users_functions.aio.operations.UserCalendarViewInstanceOperations
    :ivar user_calendar_view: UserCalendarViewOperations operations
    :vartype user_calendar_view: users_functions.aio.operations.UserCalendarViewOperations
    :ivar user_contact_folder_child_folder: UserContactFolderChildFolderOperations operations
    :vartype user_contact_folder_child_folder: users_functions.aio.operations.UserContactFolderChildFolderOperations
    :ivar user_contact_folder_contact: UserContactFolderContactOperations operations
    :vartype user_contact_folder_contact: users_functions.aio.operations.UserContactFolderContactOperations
    :ivar user_contact_folder: UserContactFolderOperations operations
    :vartype user_contact_folder: users_functions.aio.operations.UserContactFolderOperations
    :ivar user_contact: UserContactOperations operations
    :vartype user_contact: users_functions.aio.operations.UserContactOperations
    :ivar user_event_calendar_calendar_view: UserEventCalendarCalendarViewOperations operations
    :vartype user_event_calendar_calendar_view: users_functions.aio.operations.UserEventCalendarCalendarViewOperations
    :ivar user_event_calendar_event: UserEventCalendarEventOperations operations
    :vartype user_event_calendar_event: users_functions.aio.operations.UserEventCalendarEventOperations
    :ivar user_event_calendar: UserEventCalendarOperations operations
    :vartype user_event_calendar: users_functions.aio.operations.UserEventCalendarOperations
    :ivar user_event_exception_occurrence: UserEventExceptionOccurrenceOperations operations
    :vartype user_event_exception_occurrence: users_functions.aio.operations.UserEventExceptionOccurrenceOperations
    :ivar user_event_instance: UserEventInstanceOperations operations
    :vartype user_event_instance: users_functions.aio.operations.UserEventInstanceOperations
    :ivar user_event: UserEventOperations operations
    :vartype user_event: users_functions.aio.operations.UserEventOperations
    :ivar user_mail_folder_child_folder: UserMailFolderChildFolderOperations operations
    :vartype user_mail_folder_child_folder: users_functions.aio.operations.UserMailFolderChildFolderOperations
    :ivar user_mail_folder_message: UserMailFolderMessageOperations operations
    :vartype user_mail_folder_message: users_functions.aio.operations.UserMailFolderMessageOperations
    :ivar user_mail_folder: UserMailFolderOperations operations
    :vartype user_mail_folder: users_functions.aio.operations.UserMailFolderOperations
    :ivar user_managed_app_registration: UserManagedAppRegistrationOperations operations
    :vartype user_managed_app_registration: users_functions.aio.operations.UserManagedAppRegistrationOperations
    :ivar user_managed_device: UserManagedDeviceOperations operations
    :vartype user_managed_device: users_functions.aio.operations.UserManagedDeviceOperations
    :ivar user_message: UserMessageOperations operations
    :vartype user_message: users_functions.aio.operations.UserMessageOperations
    :ivar user: UserOperations operations
    :vartype user: users_functions.aio.operations.UserOperations
    :ivar user_onenote_notebook_section_group_section_page: UserOnenoteNotebookSectionGroupSectionPageOperations operations
    :vartype user_onenote_notebook_section_group_section_page: users_functions.aio.operations.UserOnenoteNotebookSectionGroupSectionPageOperations
    :ivar user_onenote_notebook_section_page: UserOnenoteNotebookSectionPageOperations operations
    :vartype user_onenote_notebook_section_page: users_functions.aio.operations.UserOnenoteNotebookSectionPageOperations
    :ivar user_onenote_notebook: UserOnenoteNotebookOperations operations
    :vartype user_onenote_notebook: users_functions.aio.operations.UserOnenoteNotebookOperations
    :ivar user_onenote_page: UserOnenotePageOperations operations
    :vartype user_onenote_page: users_functions.aio.operations.UserOnenotePageOperations
    :ivar user_onenote_page_parent_notebook_section_group_section_page: UserOnenotePageParentNotebookSectionGroupSectionPageOperations operations
    :vartype user_onenote_page_parent_notebook_section_group_section_page: users_functions.aio.operations.UserOnenotePageParentNotebookSectionGroupSectionPageOperations
    :ivar user_onenote_page_parent_notebook_section_page: UserOnenotePageParentNotebookSectionPageOperations operations
    :vartype user_onenote_page_parent_notebook_section_page: users_functions.aio.operations.UserOnenotePageParentNotebookSectionPageOperations
    :ivar user_onenote_page_parent_section_page: UserOnenotePageParentSectionPageOperations operations
    :vartype user_onenote_page_parent_section_page: users_functions.aio.operations.UserOnenotePageParentSectionPageOperations
    :ivar user_onenote_section_group_parent_notebook_section_page: UserOnenoteSectionGroupParentNotebookSectionPageOperations operations
    :vartype user_onenote_section_group_parent_notebook_section_page: users_functions.aio.operations.UserOnenoteSectionGroupParentNotebookSectionPageOperations
    :ivar user_onenote_section_group_section_page: UserOnenoteSectionGroupSectionPageOperations operations
    :vartype user_onenote_section_group_section_page: users_functions.aio.operations.UserOnenoteSectionGroupSectionPageOperations
    :ivar user_onenote_section_page: UserOnenoteSectionPageOperations operations
    :vartype user_onenote_section_page: users_functions.aio.operations.UserOnenoteSectionPageOperations
    :ivar user_outlook: UserOutlookOperations operations
    :vartype user_outlook: users_functions.aio.operations.UserOutlookOperations
    :ivar user_planner_all: UserPlannerAllOperations operations
    :vartype user_planner_all: users_functions.aio.operations.UserPlannerAllOperations
    :ivar user_todo_list_task: UserTodoListTaskOperations operations
    :vartype user_todo_list_task: users_functions.aio.operations.UserTodoListTaskOperations
    :ivar user_todo_list: UserTodoListOperations operations
    :vartype user_todo_list: users_functions.aio.operations.UserTodoListOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://graph.microsoft.com/beta'
        self._config = UsersFunctionsConfiguration(credential, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.user_activity = UserActivityOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view_calendar = UserCalendarCalendarViewCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view_exception_occurrence = UserCalendarCalendarViewExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view_instance = UserCalendarCalendarViewInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view = UserCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event_calendar = UserCalendarEventCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event_exception_occurrence = UserCalendarEventExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event_instance = UserCalendarEventInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event = UserCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar = UserCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_calendar_view_calendar = UserCalendarGroupCalendarCalendarViewCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_calendar_view_exception_occurrence = UserCalendarGroupCalendarCalendarViewExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_calendar_view_instance = UserCalendarGroupCalendarCalendarViewInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_calendar_view = UserCalendarGroupCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_event_calendar = UserCalendarGroupCalendarEventCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_event_exception_occurrence = UserCalendarGroupCalendarEventExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_event_instance = UserCalendarGroupCalendarEventInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar_event = UserCalendarGroupCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_group_calendar = UserCalendarGroupCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view_calendar = UserCalendarCalendarViewCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view_exception_occurrence = UserCalendarCalendarViewExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view_instance = UserCalendarCalendarViewInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_calendar_view = UserCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event_calendar = UserCalendarEventCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event_exception_occurrence = UserCalendarEventExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event_instance = UserCalendarEventInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_event = UserCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar = UserCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view_calendar_calendar_view = UserCalendarViewCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view_calendar_event = UserCalendarViewCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view_calendar = UserCalendarViewCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view_exception_occurrence = UserCalendarViewExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view_instance = UserCalendarViewInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_calendar_view = UserCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_contact_folder_child_folder = UserContactFolderChildFolderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_contact_folder_contact = UserContactFolderContactOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_contact_folder = UserContactFolderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_contact = UserContactOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event_calendar_calendar_view = UserEventCalendarCalendarViewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event_calendar_event = UserEventCalendarEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event_calendar = UserEventCalendarOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event_exception_occurrence = UserEventExceptionOccurrenceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event_instance = UserEventInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_event = UserEventOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_mail_folder_child_folder = UserMailFolderChildFolderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_mail_folder_message = UserMailFolderMessageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_mail_folder = UserMailFolderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_managed_app_registration = UserManagedAppRegistrationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_managed_device = UserManagedDeviceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_message = UserMessageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user = UserOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_notebook_section_group_section_page = UserOnenoteNotebookSectionGroupSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_notebook_section_page = UserOnenoteNotebookSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_notebook = UserOnenoteNotebookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page = UserOnenotePageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_notebook_section_group_section_page = UserOnenotePageParentNotebookSectionGroupSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_notebook_section_page = UserOnenotePageParentNotebookSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_page_parent_section_page = UserOnenotePageParentSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_group_parent_notebook_section_page = UserOnenoteSectionGroupParentNotebookSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_group_section_page = UserOnenoteSectionGroupSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_onenote_section_page = UserOnenoteSectionPageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_outlook = UserOutlookOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_planner_all = UserPlannerAllOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_todo_list_task = UserTodoListTaskOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_todo_list = UserTodoListOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "UsersFunctions":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)