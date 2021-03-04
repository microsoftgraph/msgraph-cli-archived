# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SecuritySecurityOperations(object):
    """SecuritySecurityOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~security.models
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

    def get_security(
        self,
        select=None,  # type: Optional[List[Union[str, "models.Get0ItemsItem"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Get1ItemsItem"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphSecurity"
        """Get Security.

        Get Security.

        :param select: Select properties to be returned.
        :type select: list[str or ~security.models.Get0ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str or ~security.models.Get1ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphSecurity, or the result of cls(response)
        :rtype: ~security.models.MicrosoftGraphSecurity
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphSecurity"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_security.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphSecurity', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_security.metadata = {'url': '/Security'}  # type: ignore

    def update_security(
        self,
        id=None,  # type: Optional[str]
        provider_status=None,  # type: Optional[List["models.MicrosoftGraphSecurityProviderStatus"]]
        alerts=None,  # type: Optional[List["models.MicrosoftGraphAlert"]]
        cloud_app_security_profiles=None,  # type: Optional[List["models.MicrosoftGraphCloudAppSecurityProfile"]]
        domain_security_profiles=None,  # type: Optional[List["models.MicrosoftGraphDomainSecurityProfile"]]
        file_security_profiles=None,  # type: Optional[List["models.MicrosoftGraphFileSecurityProfile"]]
        host_security_profiles=None,  # type: Optional[List["models.MicrosoftGraphHostSecurityProfile"]]
        ip_security_profiles=None,  # type: Optional[List["models.MicrosoftGraphIpSecurityProfile"]]
        provider_tenant_settings=None,  # type: Optional[List["models.MicrosoftGraphProviderTenantSetting"]]
        secure_score_control_profiles=None,  # type: Optional[List["models.MicrosoftGraphSecureScoreControlProfile"]]
        secure_scores=None,  # type: Optional[List["models.MicrosoftGraphSecureScore"]]
        security_actions=None,  # type: Optional[List["models.MicrosoftGraphSecurityAction"]]
        ti_indicators=None,  # type: Optional[List["models.MicrosoftGraphTIIndicator"]]
        user_security_profiles=None,  # type: Optional[List["models.MicrosoftGraphUserSecurityProfile"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update Security.

        Update Security.

        :param id: Read-only.
        :type id: str
        :param provider_status:
        :type provider_status: list[~security.models.MicrosoftGraphSecurityProviderStatus]
        :param alerts: Read-only. Nullable.
        :type alerts: list[~security.models.MicrosoftGraphAlert]
        :param cloud_app_security_profiles:
        :type cloud_app_security_profiles: list[~security.models.MicrosoftGraphCloudAppSecurityProfile]
        :param domain_security_profiles:
        :type domain_security_profiles: list[~security.models.MicrosoftGraphDomainSecurityProfile]
        :param file_security_profiles:
        :type file_security_profiles: list[~security.models.MicrosoftGraphFileSecurityProfile]
        :param host_security_profiles:
        :type host_security_profiles: list[~security.models.MicrosoftGraphHostSecurityProfile]
        :param ip_security_profiles:
        :type ip_security_profiles: list[~security.models.MicrosoftGraphIpSecurityProfile]
        :param provider_tenant_settings:
        :type provider_tenant_settings: list[~security.models.MicrosoftGraphProviderTenantSetting]
        :param secure_score_control_profiles:
        :type secure_score_control_profiles: list[~security.models.MicrosoftGraphSecureScoreControlProfile]
        :param secure_scores:
        :type secure_scores: list[~security.models.MicrosoftGraphSecureScore]
        :param security_actions:
        :type security_actions: list[~security.models.MicrosoftGraphSecurityAction]
        :param ti_indicators:
        :type ti_indicators: list[~security.models.MicrosoftGraphTIIndicator]
        :param user_security_profiles:
        :type user_security_profiles: list[~security.models.MicrosoftGraphUserSecurityProfile]
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

        body = models.MicrosoftGraphSecurity(id=id, provider_status=provider_status, alerts=alerts, cloud_app_security_profiles=cloud_app_security_profiles, domain_security_profiles=domain_security_profiles, file_security_profiles=file_security_profiles, host_security_profiles=host_security_profiles, ip_security_profiles=ip_security_profiles, provider_tenant_settings=provider_tenant_settings, secure_score_control_profiles=secure_score_control_profiles, secure_scores=secure_scores, security_actions=security_actions, ti_indicators=ti_indicators, user_security_profiles=user_security_profiles)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_security.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphSecurity')
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

    update_security.metadata = {'url': '/Security'}  # type: ignore
