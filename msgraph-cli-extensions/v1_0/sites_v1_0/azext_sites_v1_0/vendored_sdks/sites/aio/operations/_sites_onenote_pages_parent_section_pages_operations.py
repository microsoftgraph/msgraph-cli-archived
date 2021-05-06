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

class SitesOnenotePagesParentSectionPagesOperations:
    """SitesOnenotePagesParentSectionPagesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~sites.models
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

    async def copy_to_section(
        self,
        site_id: str,
        onenote_page_id: str,
        onenote_page_id1: str,
        body: "models.PathsGk640QSitesSiteIdOnenotePagesOnenotepageIdParentsectionPagesOnenotepageId1MicrosoftGraphCopytosectionPostRequestbodyContentApplicationJsonSchema",
        **kwargs
    ) -> "models.MicrosoftGraphOnenoteOperation":
        """Invoke action copyToSection.

        Invoke action copyToSection.

        :param site_id: key: id of site.
        :type site_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param onenote_page_id1: key: id of onenotePage.
        :type onenote_page_id1: str
        :param body: Action parameters.
        :type body: ~sites.models.PathsGk640QSitesSiteIdOnenotePagesOnenotepageIdParentsectionPagesOnenotepageId1MicrosoftGraphCopytosectionPostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOnenoteOperation, or the result of cls(response)
        :rtype: ~sites.models.MicrosoftGraphOnenoteOperation
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
        url = self.copy_to_section.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
            'onenotePage-id1': self._serialize.url("onenote_page_id1", onenote_page_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PathsGk640QSitesSiteIdOnenotePagesOnenotepageIdParentsectionPagesOnenotepageId1MicrosoftGraphCopytosectionPostRequestbodyContentApplicationJsonSchema')
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
    copy_to_section.metadata = {'url': '/sites/{site-id}/onenote/pages/{onenotePage-id}/parentSection/pages/{onenotePage-id1}/microsoft.graph.copyToSection'}  # type: ignore

    async def onenote_patch_content(
        self,
        site_id: str,
        onenote_page_id: str,
        onenote_page_id1: str,
        body: "models.PathsV7Bq3TSitesSiteIdOnenotePagesOnenotepageIdParentsectionPagesOnenotepageId1MicrosoftGraphOnenotepatchcontentPostRequestbodyContentApplicationJsonSchema",
        **kwargs
    ) -> None:
        """Invoke action onenotePatchContent.

        Invoke action onenotePatchContent.

        :param site_id: key: id of site.
        :type site_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param onenote_page_id1: key: id of onenotePage.
        :type onenote_page_id1: str
        :param body: Action parameters.
        :type body: ~sites.models.PathsV7Bq3TSitesSiteIdOnenotePagesOnenotepageIdParentsectionPagesOnenotepageId1MicrosoftGraphOnenotepatchcontentPostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.onenote_patch_content.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
            'onenotePage-id1': self._serialize.url("onenote_page_id1", onenote_page_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PathsV7Bq3TSitesSiteIdOnenotePagesOnenotepageIdParentsectionPagesOnenotepageId1MicrosoftGraphOnenotepatchcontentPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    onenote_patch_content.metadata = {'url': '/sites/{site-id}/onenote/pages/{onenotePage-id}/parentSection/pages/{onenotePage-id1}/microsoft.graph.onenotePatchContent'}  # type: ignore

    async def preview(
        self,
        site_id: str,
        onenote_page_id: str,
        onenote_page_id1: str,
        **kwargs
    ) -> "models.MicrosoftGraphOnenotePagePreview":
        """Invoke function preview.

        Invoke function preview.

        :param site_id: key: id of site.
        :type site_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param onenote_page_id1: key: id of onenotePage.
        :type onenote_page_id1: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOnenotePagePreview, or the result of cls(response)
        :rtype: ~sites.models.MicrosoftGraphOnenotePagePreview
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOnenotePagePreview"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.preview.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
            'onenotePage-id1': self._serialize.url("onenote_page_id1", onenote_page_id1, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphOnenotePagePreview', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    preview.metadata = {'url': '/sites/{site-id}/onenote/pages/{onenotePage-id}/parentSection/pages/{onenotePage-id1}/microsoft.graph.preview()'}  # type: ignore
