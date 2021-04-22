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
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class TrustFrameworkKeySetsOperations(object):
    """TrustFrameworkKeySetsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~identity_sign_ins.models
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

    def generate_key(
        self,
        trust_framework_key_set_id,  # type: str
        body,  # type: "models.Paths1IaopbhTrustframeworkKeysetsTrustframeworkkeysetIdMicrosoftGraphGeneratekeyPostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphTrustFrameworkKey"
        """Invoke action generateKey.

        Invoke action generateKey.

        :param trust_framework_key_set_id: key: id of trustFrameworkKeySet.
        :type trust_framework_key_set_id: str
        :param body: Action parameters.
        :type body: ~identity_sign_ins.models.Paths1IaopbhTrustframeworkKeysetsTrustframeworkkeysetIdMicrosoftGraphGeneratekeyPostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphTrustFrameworkKey, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.MicrosoftGraphTrustFrameworkKey
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphTrustFrameworkKey"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.generate_key.metadata['url']  # type: ignore
        path_format_arguments = {
            'trustFrameworkKeySet-id': self._serialize.url("trust_framework_key_set_id", trust_framework_key_set_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths1IaopbhTrustframeworkKeysetsTrustframeworkkeysetIdMicrosoftGraphGeneratekeyPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphTrustFrameworkKey', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    generate_key.metadata = {'url': '/trustFramework/keySets/{trustFrameworkKeySet-id}/microsoft.graph.generateKey'}  # type: ignore

    def get_active_key(
        self,
        trust_framework_key_set_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphTrustFrameworkKey"
        """Invoke function getActiveKey.

        Invoke function getActiveKey.

        :param trust_framework_key_set_id: key: id of trustFrameworkKeySet.
        :type trust_framework_key_set_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphTrustFrameworkKey, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.MicrosoftGraphTrustFrameworkKey
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphTrustFrameworkKey"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_active_key.metadata['url']  # type: ignore
        path_format_arguments = {
            'trustFrameworkKeySet-id': self._serialize.url("trust_framework_key_set_id", trust_framework_key_set_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

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

        deserialized = self._deserialize('MicrosoftGraphTrustFrameworkKey', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_active_key.metadata = {'url': '/trustFramework/keySets/{trustFrameworkKeySet-id}/microsoft.graph.getActiveKey()'}  # type: ignore

    def upload_certificate(
        self,
        trust_framework_key_set_id,  # type: str
        body,  # type: "models.Paths19SkfwzTrustframeworkKeysetsTrustframeworkkeysetIdMicrosoftGraphUploadcertificatePostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphTrustFrameworkKey"
        """Invoke action uploadCertificate.

        Invoke action uploadCertificate.

        :param trust_framework_key_set_id: key: id of trustFrameworkKeySet.
        :type trust_framework_key_set_id: str
        :param body: Action parameters.
        :type body: ~identity_sign_ins.models.Paths19SkfwzTrustframeworkKeysetsTrustframeworkkeysetIdMicrosoftGraphUploadcertificatePostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphTrustFrameworkKey, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.MicrosoftGraphTrustFrameworkKey
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphTrustFrameworkKey"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.upload_certificate.metadata['url']  # type: ignore
        path_format_arguments = {
            'trustFrameworkKeySet-id': self._serialize.url("trust_framework_key_set_id", trust_framework_key_set_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths19SkfwzTrustframeworkKeysetsTrustframeworkkeysetIdMicrosoftGraphUploadcertificatePostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphTrustFrameworkKey', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    upload_certificate.metadata = {'url': '/trustFramework/keySets/{trustFrameworkKeySet-id}/microsoft.graph.uploadCertificate'}  # type: ignore

    def upload_pkcs12(
        self,
        trust_framework_key_set_id,  # type: str
        body,  # type: "models.Paths11Ap814TrustframeworkKeysetsTrustframeworkkeysetIdMicrosoftGraphUploadpkcs12PostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphTrustFrameworkKey"
        """Invoke action uploadPkcs12.

        Invoke action uploadPkcs12.

        :param trust_framework_key_set_id: key: id of trustFrameworkKeySet.
        :type trust_framework_key_set_id: str
        :param body: Action parameters.
        :type body: ~identity_sign_ins.models.Paths11Ap814TrustframeworkKeysetsTrustframeworkkeysetIdMicrosoftGraphUploadpkcs12PostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphTrustFrameworkKey, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.MicrosoftGraphTrustFrameworkKey
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphTrustFrameworkKey"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.upload_pkcs12.metadata['url']  # type: ignore
        path_format_arguments = {
            'trustFrameworkKeySet-id': self._serialize.url("trust_framework_key_set_id", trust_framework_key_set_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'Paths11Ap814TrustframeworkKeysetsTrustframeworkkeysetIdMicrosoftGraphUploadpkcs12PostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphTrustFrameworkKey', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    upload_pkcs12.metadata = {'url': '/trustFramework/keySets/{trustFrameworkKeySet-id}/microsoft.graph.uploadPkcs12'}  # type: ignore

    def upload_secret(
        self,
        trust_framework_key_set_id,  # type: str
        body,  # type: "models.PathsDmvqaiTrustframeworkKeysetsTrustframeworkkeysetIdMicrosoftGraphUploadsecretPostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphTrustFrameworkKey"
        """Invoke action uploadSecret.

        Invoke action uploadSecret.

        :param trust_framework_key_set_id: key: id of trustFrameworkKeySet.
        :type trust_framework_key_set_id: str
        :param body: Action parameters.
        :type body: ~identity_sign_ins.models.PathsDmvqaiTrustframeworkKeysetsTrustframeworkkeysetIdMicrosoftGraphUploadsecretPostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphTrustFrameworkKey, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.MicrosoftGraphTrustFrameworkKey
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphTrustFrameworkKey"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.upload_secret.metadata['url']  # type: ignore
        path_format_arguments = {
            'trustFrameworkKeySet-id': self._serialize.url("trust_framework_key_set_id", trust_framework_key_set_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PathsDmvqaiTrustframeworkKeysetsTrustframeworkkeysetIdMicrosoftGraphUploadsecretPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphTrustFrameworkKey', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    upload_secret.metadata = {'url': '/trustFramework/keySets/{trustFrameworkKeySet-id}/microsoft.graph.uploadSecret'}  # type: ignore
