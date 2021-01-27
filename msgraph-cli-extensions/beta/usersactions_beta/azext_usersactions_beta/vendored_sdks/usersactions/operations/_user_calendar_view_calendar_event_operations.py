# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class UserCalendarViewCalendarEventOperations(object):
    """UserCalendarViewCalendarEventOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users_actions.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def accept(
        self,
        user_id,  # type: str
        event_id,  # type: str
        event_id1,  # type: str
        comment=None,  # type: Optional[str]
        send_response=False,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action accept.

        Invoke action accept.

        :param user_id: key: id of user.
        :type user_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param event_id1: key: id of event.
        :type event_id1: str
        :param comment:
        :type comment: str
        :param send_response:
        :type send_response: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths1Gv8Qr5UsersUserIdCalendarviewEventIdCalendarEventsEventId1MicrosoftGraphAcceptPostRequestbodyContentApplicationJsonSchema(comment=comment, send_response=send_response)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.accept.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
            'event-id1': self._serialize.url("event_id1", event_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'Paths1Gv8Qr5UsersUserIdCalendarviewEventIdCalendarEventsEventId1MicrosoftGraphAcceptPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    accept.metadata = {'url': '/users/{user-id}/calendarView/{event-id}/calendar/events/{event-id1}/microsoft.graph.accept'}  # type: ignore

    def cancel(
        self,
        user_id,  # type: str
        event_id,  # type: str
        event_id1,  # type: str
        comment=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action cancel.

        Invoke action cancel.

        :param user_id: key: id of user.
        :type user_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param event_id1: key: id of event.
        :type event_id1: str
        :param comment:
        :type comment: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.PathsDrjretUsersUserIdCalendarviewEventIdCalendarEventsEventId1MicrosoftGraphCancelPostRequestbodyContentApplicationJsonSchema(comment=comment)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.cancel.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
            'event-id1': self._serialize.url("event_id1", event_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'PathsDrjretUsersUserIdCalendarviewEventIdCalendarEventsEventId1MicrosoftGraphCancelPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    cancel.metadata = {'url': '/users/{user-id}/calendarView/{event-id}/calendar/events/{event-id1}/microsoft.graph.cancel'}  # type: ignore

    def decline(
        self,
        user_id,  # type: str
        event_id,  # type: str
        event_id1,  # type: str
        comment=None,  # type: Optional[str]
        send_response=False,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action decline.

        Invoke action decline.

        :param user_id: key: id of user.
        :type user_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param event_id1: key: id of event.
        :type event_id1: str
        :param comment:
        :type comment: str
        :param send_response:
        :type send_response: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.PathsIu6EmaUsersUserIdCalendarviewEventIdCalendarEventsEventId1MicrosoftGraphDeclinePostRequestbodyContentApplicationJsonSchema(comment=comment, send_response=send_response)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.decline.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
            'event-id1': self._serialize.url("event_id1", event_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'PathsIu6EmaUsersUserIdCalendarviewEventIdCalendarEventsEventId1MicrosoftGraphDeclinePostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    decline.metadata = {'url': '/users/{user-id}/calendarView/{event-id}/calendar/events/{event-id1}/microsoft.graph.decline'}  # type: ignore

    def dismiss_reminder(
        self,
        user_id,  # type: str
        event_id,  # type: str
        event_id1,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action dismissReminder.

        Invoke action dismissReminder.

        :param user_id: key: id of user.
        :type user_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param event_id1: key: id of event.
        :type event_id1: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.dismiss_reminder.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
            'event-id1': self._serialize.url("event_id1", event_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    dismiss_reminder.metadata = {'url': '/users/{user-id}/calendarView/{event-id}/calendar/events/{event-id1}/microsoft.graph.dismissReminder'}  # type: ignore

    def forward(
        self,
        user_id,  # type: str
        event_id,  # type: str
        event_id1,  # type: str
        to_recipients=None,  # type: Optional[List["models.MicrosoftGraphRecipient"]]
        comment=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action forward.

        Invoke action forward.

        :param user_id: key: id of user.
        :type user_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param event_id1: key: id of event.
        :type event_id1: str
        :param to_recipients:
        :type to_recipients: list[~users_actions.models.MicrosoftGraphRecipient]
        :param comment:
        :type comment: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths1R2ChupUsersUserIdCalendarviewEventIdCalendarEventsEventId1MicrosoftGraphForwardPostRequestbodyContentApplicationJsonSchema(to_recipients=to_recipients, comment=comment)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.forward.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
            'event-id1': self._serialize.url("event_id1", event_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'Paths1R2ChupUsersUserIdCalendarviewEventIdCalendarEventsEventId1MicrosoftGraphForwardPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    forward.metadata = {'url': '/users/{user-id}/calendarView/{event-id}/calendar/events/{event-id1}/microsoft.graph.forward'}  # type: ignore

    def snooze_reminder(
        self,
        user_id,  # type: str
        event_id,  # type: str
        event_id1,  # type: str
        new_reminder_time=None,  # type: Optional["models.MicrosoftGraphDateTimeZone"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action snoozeReminder.

        Invoke action snoozeReminder.

        :param user_id: key: id of user.
        :type user_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param event_id1: key: id of event.
        :type event_id1: str
        :param new_reminder_time: dateTimeTimeZone.
        :type new_reminder_time: ~users_actions.models.MicrosoftGraphDateTimeZone
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.PathsWl7PqtUsersUserIdCalendarviewEventIdCalendarEventsEventId1MicrosoftGraphSnoozereminderPostRequestbodyContentApplicationJsonSchema(new_reminder_time=new_reminder_time)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.snooze_reminder.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
            'event-id1': self._serialize.url("event_id1", event_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'PathsWl7PqtUsersUserIdCalendarviewEventIdCalendarEventsEventId1MicrosoftGraphSnoozereminderPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    snooze_reminder.metadata = {'url': '/users/{user-id}/calendarView/{event-id}/calendar/events/{event-id1}/microsoft.graph.snoozeReminder'}  # type: ignore

    def tentatively_accept(
        self,
        user_id,  # type: str
        event_id,  # type: str
        event_id1,  # type: str
        comment=None,  # type: Optional[str]
        send_response=False,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action tentativelyAccept.

        Invoke action tentativelyAccept.

        :param user_id: key: id of user.
        :type user_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param event_id1: key: id of event.
        :type event_id1: str
        :param comment:
        :type comment: str
        :param send_response:
        :type send_response: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths8Hu9XiUsersUserIdCalendarviewEventIdCalendarEventsEventId1MicrosoftGraphTentativelyacceptPostRequestbodyContentApplicationJsonSchema(comment=comment, send_response=send_response)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.tentatively_accept.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
            'event-id1': self._serialize.url("event_id1", event_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'Paths8Hu9XiUsersUserIdCalendarviewEventIdCalendarEventsEventId1MicrosoftGraphTentativelyacceptPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    tentatively_accept.metadata = {'url': '/users/{user-id}/calendarView/{event-id}/calendar/events/{event-id1}/microsoft.graph.tentativelyAccept'}  # type: ignore
