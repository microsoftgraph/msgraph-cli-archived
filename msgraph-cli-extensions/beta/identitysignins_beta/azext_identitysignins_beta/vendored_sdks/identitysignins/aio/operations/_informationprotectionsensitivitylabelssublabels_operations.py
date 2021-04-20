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

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class informationprotectionsensitivitylabelssublabelsOperations:
    """informationprotectionsensitivitylabelssublabelsOperations async operations.

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

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def evaluate(
        self,
        sensitivity_label_id: str,
        body: "models.pathsk62xddinformationprotectionsensitivitylabelssensitivitylabelidsublabelsmicrosoftgraphevaluatepostrequestbodycontentapplicationjsonschema",
        **kwargs
    ) -> "models.microsoftgraphevaluatelabeljobresponse":
        """Invoke action evaluate.

        Invoke action evaluate.

        :param sensitivity_label_id: key: id of sensitivityLabel.
        :type sensitivity_label_id: str
        :param body: Action parameters.
        :type body: ~identity_sign_ins.models.pathsk62xddinformationprotectionsensitivitylabelssensitivitylabelidsublabelsmicrosoftgraphevaluatepostrequestbodycontentapplicationjsonschema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: microsoftgraphevaluatelabeljobresponse, or the result of cls(response)
        :rtype: ~identity_sign_ins.models.microsoftgraphevaluatelabeljobresponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.microsoftgraphevaluatelabeljobresponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.evaluate.metadata['url']  # type: ignore
        path_format_arguments = {
            'sensitivityLabel-id': self._serialize.url("sensitivity_label_id", sensitivity_label_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'pathsk62xddinformationprotectionsensitivitylabelssensitivitylabelidsublabelsmicrosoftgraphevaluatepostrequestbodycontentapplicationjsonschema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.odataerror, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('microsoftgraphevaluatelabeljobresponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    evaluate.metadata = {'url': '/informationProtection/sensitivityLabels/{sensitivityLabel-id}/sublabels/microsoft.graph.evaluate'}  # type: ignore
