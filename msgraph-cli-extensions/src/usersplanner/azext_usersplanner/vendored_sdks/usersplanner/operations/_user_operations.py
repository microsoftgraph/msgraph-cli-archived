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
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class UserOperations(object):
    """UserOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users_planner.models
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

    def get_planner(
        self,
        user_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Get1ItemsItem"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Get2ItemsItem"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPlannerUser"
        """Get planner from users.

        Get planner from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~users_planner.models.Get1ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str or ~users_planner.models.Get2ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPlannerUser, or the result of cls(response)
        :rtype: ~users_planner.models.MicrosoftGraphPlannerUser
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPlannerUser"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_planner.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPlannerUser', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_planner.metadata = {'url': '/users/{user-id}/planner'}  # type: ignore

    def update_planner(
        self,
        user_id,  # type: str
        id=None,  # type: Optional[str]
        favorite_plan_references=None,  # type: Optional[object]
        recent_plan_references=None,  # type: Optional[object]
        tasks=None,  # type: Optional[List["models.MicrosoftGraphPlannerTask"]]
        plans=None,  # type: Optional[List["models.MicrosoftGraphPlannerPlan"]]
        favorite_plans=None,  # type: Optional[List["models.MicrosoftGraphPlannerPlan"]]
        recent_plans=None,  # type: Optional[List["models.MicrosoftGraphPlannerPlan"]]
        all=None,  # type: Optional[List["models.MicrosoftGraphEntity"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property planner in users.

        Update the navigation property planner in users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param id: Read-only.
        :type id: str
        :param favorite_plan_references: Any object.
        :type favorite_plan_references: object
        :param recent_plan_references: Any object.
        :type recent_plan_references: object
        :param tasks: Read-only. Nullable. Returns the plannerPlans shared with the user.
        :type tasks: list[~users_planner.models.MicrosoftGraphPlannerTask]
        :param plans: Read-only. Nullable. Returns the plannerTasks assigned to the user.
        :type plans: list[~users_planner.models.MicrosoftGraphPlannerPlan]
        :param favorite_plans:
        :type favorite_plans: list[~users_planner.models.MicrosoftGraphPlannerPlan]
        :param recent_plans:
        :type recent_plans: list[~users_planner.models.MicrosoftGraphPlannerPlan]
        :param all:
        :type all: list[~users_planner.models.MicrosoftGraphEntity]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPlannerUser(id=id, favorite_plan_references=favorite_plan_references, recent_plan_references=recent_plan_references, tasks=tasks, plans=plans, favorite_plans=favorite_plans, recent_plans=recent_plans, all=all)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_planner.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPlannerUser')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_planner.metadata = {'url': '/users/{user-id}/planner'}  # type: ignore