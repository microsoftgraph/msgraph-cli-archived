# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class GroupsOnenoteSectionsParentSectionGroupParentNotebookSectionsOperations:
    """GroupsOnenoteSectionsParentSectionGroupParentNotebookSectionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~groups.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def copy_to_notebook(
        self,
        group_id: str,
        onenote_section_id: str,
        onenote_section_id1: str,
        body: "models.Paths1Dyy9InGroupsGroupIdOnenoteSectionsOnenotesectionIdParentsectiongroupParentnotebookSectionsOnenotesectionId1MicrosoftGraphCopytonotebookPostRequestbodyContentApplicationJsonSchema",
        **kwargs
    ) -> "models.MicrosoftGraphOnenoteOperation":
        """Invoke action copyToNotebook.

        Invoke action copyToNotebook.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_section_id1: key: id of onenoteSection.
        :type onenote_section_id1: str
        :param body: Action parameters.
        :type body: ~groups.models.Paths1Dyy9InGroupsGroupIdOnenoteSectionsOnenotesectionIdParentsectiongroupParentnotebookSectionsOnenotesectionId1MicrosoftGraphCopytonotebookPostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOnenoteOperation, or the result of cls(response)
        :rtype: ~groups.models.MicrosoftGraphOnenoteOperation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOnenoteOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.copy_to_notebook.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
            'onenoteSection-id1': self._serialize.url("onenote_section_id1", onenote_section_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths1Dyy9InGroupsGroupIdOnenoteSectionsOnenotesectionIdParentsectiongroupParentnotebookSectionsOnenotesectionId1MicrosoftGraphCopytonotebookPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphOnenoteOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    copy_to_notebook.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/parentSectionGroup/parentNotebook/sections/{onenoteSection-id1}/microsoft.graph.copyToNotebook'}  # type: ignore

    async def copy_to_section_group(
        self,
        group_id: str,
        onenote_section_id: str,
        onenote_section_id1: str,
        body: "models.PathsRzkt3FGroupsGroupIdOnenoteSectionsOnenotesectionIdParentsectiongroupParentnotebookSectionsOnenotesectionId1MicrosoftGraphCopytosectiongroupPostRequestbodyContentApplicationJsonSchema",
        **kwargs
    ) -> "models.MicrosoftGraphOnenoteOperation":
        """Invoke action copyToSectionGroup.

        Invoke action copyToSectionGroup.

        :param group_id: key: id of group.
        :type group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_section_id1: key: id of onenoteSection.
        :type onenote_section_id1: str
        :param body: Action parameters.
        :type body: ~groups.models.PathsRzkt3FGroupsGroupIdOnenoteSectionsOnenotesectionIdParentsectiongroupParentnotebookSectionsOnenotesectionId1MicrosoftGraphCopytosectiongroupPostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOnenoteOperation, or the result of cls(response)
        :rtype: ~groups.models.MicrosoftGraphOnenoteOperation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOnenoteOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.copy_to_section_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
            'onenoteSection-id1': self._serialize.url("onenote_section_id1", onenote_section_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PathsRzkt3FGroupsGroupIdOnenoteSectionsOnenotesectionIdParentsectiongroupParentnotebookSectionsOnenotesectionId1MicrosoftGraphCopytosectiongroupPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphOnenoteOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    copy_to_section_group.metadata = {'url': '/groups/{group-id}/onenote/sections/{onenoteSection-id}/parentSectionGroup/parentNotebook/sections/{onenoteSection-id1}/microsoft.graph.copyToSectionGroup'}  # type: ignore
