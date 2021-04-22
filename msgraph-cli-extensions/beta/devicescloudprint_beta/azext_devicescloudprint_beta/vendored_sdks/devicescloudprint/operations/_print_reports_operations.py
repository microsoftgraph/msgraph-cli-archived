# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class PrintReportsOperations(object):
    """PrintReportsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~devices_cloud_print.models
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

    def get_group_archived_print_jobs(
        self,
        group_id,  # type: str
        period_start,  # type: datetime.datetime
        period_end,  # type: datetime.datetime
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphArchivedPrintJob"]
        """Invoke function getGroupArchivedPrintJobs.

        Invoke function getGroupArchivedPrintJobs.

        :param group_id:
        :type group_id: str
        :param period_start:
        :type period_start: ~datetime.datetime
        :param period_end:
        :type period_end: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphArchivedPrintJob, or the result of cls(response)
        :rtype: list[~devices_cloud_print.models.MicrosoftGraphArchivedPrintJob]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphArchivedPrintJob"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_group_archived_print_jobs.metadata['url']  # type: ignore
        path_format_arguments = {
            'groupId': self._serialize.url("group_id", group_id, 'str'),
            'periodStart': self._serialize.url("period_start", period_start, 'iso-8601'),
            'periodEnd': self._serialize.url("period_end", period_end, 'iso-8601'),
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

        deserialized = self._deserialize('[MicrosoftGraphArchivedPrintJob]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_group_archived_print_jobs.metadata = {'url': '/print/reports/microsoft.graph.getGroupArchivedPrintJobs(groupId=\'{groupId}\',periodStart={periodStart},periodEnd={periodEnd})'}  # type: ignore

    def get_group_print_usage_summary(
        self,
        group_id,  # type: str
        period_start,  # type: datetime.datetime
        period_end,  # type: datetime.datetime
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphGroupPrintUsageSummary"
        """Invoke function getGroupPrintUsageSummary.

        Invoke function getGroupPrintUsageSummary.

        :param group_id:
        :type group_id: str
        :param period_start:
        :type period_start: ~datetime.datetime
        :param period_end:
        :type period_end: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphGroupPrintUsageSummary, or the result of cls(response)
        :rtype: ~devices_cloud_print.models.MicrosoftGraphGroupPrintUsageSummary
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphGroupPrintUsageSummary"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_group_print_usage_summary.metadata['url']  # type: ignore
        path_format_arguments = {
            'groupId': self._serialize.url("group_id", group_id, 'str'),
            'periodStart': self._serialize.url("period_start", period_start, 'iso-8601'),
            'periodEnd': self._serialize.url("period_end", period_end, 'iso-8601'),
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

        deserialized = self._deserialize('MicrosoftGraphGroupPrintUsageSummary', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_group_print_usage_summary.metadata = {'url': '/print/reports/microsoft.graph.getGroupPrintUsageSummary(groupId=\'{groupId}\',periodStart={periodStart},periodEnd={periodEnd})'}  # type: ignore

    def get_overall_print_usage_summary(
        self,
        period_start,  # type: datetime.datetime
        period_end,  # type: datetime.datetime
        top_lists_size,  # type: int
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphOverallPrintUsageSummary"]
        """Invoke function getOverallPrintUsageSummary.

        Invoke function getOverallPrintUsageSummary.

        :param period_start:
        :type period_start: ~datetime.datetime
        :param period_end:
        :type period_end: ~datetime.datetime
        :param top_lists_size:
        :type top_lists_size: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphOverallPrintUsageSummary, or the result of cls(response)
        :rtype: list[~devices_cloud_print.models.MicrosoftGraphOverallPrintUsageSummary]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphOverallPrintUsageSummary"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_overall_print_usage_summary.metadata['url']  # type: ignore
        path_format_arguments = {
            'periodStart': self._serialize.url("period_start", period_start, 'iso-8601'),
            'periodEnd': self._serialize.url("period_end", period_end, 'iso-8601'),
            'topListsSize': self._serialize.url("top_lists_size", top_lists_size, 'int', maximum=2147483647, minimum=-2147483648),
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

        deserialized = self._deserialize('[MicrosoftGraphOverallPrintUsageSummary]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_overall_print_usage_summary.metadata = {'url': '/print/reports/microsoft.graph.getOverallPrintUsageSummary(periodStart={periodStart},periodEnd={periodEnd},topListsSize={topListsSize})'}  # type: ignore

    def get_printer_archived_print_jobs(
        self,
        printer_id,  # type: str
        period_start,  # type: datetime.datetime
        period_end,  # type: datetime.datetime
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphArchivedPrintJob"]
        """Invoke function getPrinterArchivedPrintJobs.

        Invoke function getPrinterArchivedPrintJobs.

        :param printer_id:
        :type printer_id: str
        :param period_start:
        :type period_start: ~datetime.datetime
        :param period_end:
        :type period_end: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphArchivedPrintJob, or the result of cls(response)
        :rtype: list[~devices_cloud_print.models.MicrosoftGraphArchivedPrintJob]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphArchivedPrintJob"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_printer_archived_print_jobs.metadata['url']  # type: ignore
        path_format_arguments = {
            'printerId': self._serialize.url("printer_id", printer_id, 'str'),
            'periodStart': self._serialize.url("period_start", period_start, 'iso-8601'),
            'periodEnd': self._serialize.url("period_end", period_end, 'iso-8601'),
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

        deserialized = self._deserialize('[MicrosoftGraphArchivedPrintJob]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_printer_archived_print_jobs.metadata = {'url': '/print/reports/microsoft.graph.getPrinterArchivedPrintJobs(printerId=\'{printerId}\',periodStart={periodStart},periodEnd={periodEnd})'}  # type: ignore

    def get_printer_usage_summary(
        self,
        printer_id,  # type: str
        period_start,  # type: datetime.datetime
        period_end,  # type: datetime.datetime
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPrinterUsageSummary"
        """Invoke function getPrinterUsageSummary.

        Invoke function getPrinterUsageSummary.

        :param printer_id:
        :type printer_id: str
        :param period_start:
        :type period_start: ~datetime.datetime
        :param period_end:
        :type period_end: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPrinterUsageSummary, or the result of cls(response)
        :rtype: ~devices_cloud_print.models.MicrosoftGraphPrinterUsageSummary
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPrinterUsageSummary"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_printer_usage_summary.metadata['url']  # type: ignore
        path_format_arguments = {
            'printerId': self._serialize.url("printer_id", printer_id, 'str'),
            'periodStart': self._serialize.url("period_start", period_start, 'iso-8601'),
            'periodEnd': self._serialize.url("period_end", period_end, 'iso-8601'),
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

        deserialized = self._deserialize('MicrosoftGraphPrinterUsageSummary', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_printer_usage_summary.metadata = {'url': '/print/reports/microsoft.graph.getPrinterUsageSummary(printerId=\'{printerId}\',periodStart={periodStart},periodEnd={periodEnd})'}  # type: ignore

    def get_print_usage_summaries_by_group(
        self,
        period_start,  # type: datetime.datetime
        period_end,  # type: datetime.datetime
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphGroupPrintUsageSummary"]
        """Invoke function getPrintUsageSummariesByGroup.

        Invoke function getPrintUsageSummariesByGroup.

        :param period_start:
        :type period_start: ~datetime.datetime
        :param period_end:
        :type period_end: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphGroupPrintUsageSummary, or the result of cls(response)
        :rtype: list[~devices_cloud_print.models.MicrosoftGraphGroupPrintUsageSummary]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphGroupPrintUsageSummary"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_print_usage_summaries_by_group.metadata['url']  # type: ignore
        path_format_arguments = {
            'periodStart': self._serialize.url("period_start", period_start, 'iso-8601'),
            'periodEnd': self._serialize.url("period_end", period_end, 'iso-8601'),
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

        deserialized = self._deserialize('[MicrosoftGraphGroupPrintUsageSummary]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_print_usage_summaries_by_group.metadata = {'url': '/print/reports/microsoft.graph.getPrintUsageSummariesByGroup(periodStart={periodStart},periodEnd={periodEnd})'}  # type: ignore

    def get_print_usage_summaries_by_printer(
        self,
        period_start,  # type: datetime.datetime
        period_end,  # type: datetime.datetime
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphPrinterUsageSummary"]
        """Invoke function getPrintUsageSummariesByPrinter.

        Invoke function getPrintUsageSummariesByPrinter.

        :param period_start:
        :type period_start: ~datetime.datetime
        :param period_end:
        :type period_end: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphPrinterUsageSummary, or the result of cls(response)
        :rtype: list[~devices_cloud_print.models.MicrosoftGraphPrinterUsageSummary]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphPrinterUsageSummary"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_print_usage_summaries_by_printer.metadata['url']  # type: ignore
        path_format_arguments = {
            'periodStart': self._serialize.url("period_start", period_start, 'iso-8601'),
            'periodEnd': self._serialize.url("period_end", period_end, 'iso-8601'),
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

        deserialized = self._deserialize('[MicrosoftGraphPrinterUsageSummary]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_print_usage_summaries_by_printer.metadata = {'url': '/print/reports/microsoft.graph.getPrintUsageSummariesByPrinter(periodStart={periodStart},periodEnd={periodEnd})'}  # type: ignore

    def get_print_usage_summaries_by_time_span(
        self,
        period_start,  # type: datetime.datetime
        period_end,  # type: datetime.datetime
        time_span_in_minutes,  # type: int
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphPrintUsageSummary"]
        """Invoke function getPrintUsageSummariesByTimeSpan.

        Invoke function getPrintUsageSummariesByTimeSpan.

        :param period_start:
        :type period_start: ~datetime.datetime
        :param period_end:
        :type period_end: ~datetime.datetime
        :param time_span_in_minutes:
        :type time_span_in_minutes: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphPrintUsageSummary, or the result of cls(response)
        :rtype: list[~devices_cloud_print.models.MicrosoftGraphPrintUsageSummary]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphPrintUsageSummary"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_print_usage_summaries_by_time_span.metadata['url']  # type: ignore
        path_format_arguments = {
            'periodStart': self._serialize.url("period_start", period_start, 'iso-8601'),
            'periodEnd': self._serialize.url("period_end", period_end, 'iso-8601'),
            'timeSpanInMinutes': self._serialize.url("time_span_in_minutes", time_span_in_minutes, 'int', maximum=2147483647, minimum=-2147483648),
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

        deserialized = self._deserialize('[MicrosoftGraphPrintUsageSummary]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_print_usage_summaries_by_time_span.metadata = {'url': '/print/reports/microsoft.graph.getPrintUsageSummariesByTimeSpan(periodStart={periodStart},periodEnd={periodEnd},timeSpanInMinutes={timeSpanInMinutes})'}  # type: ignore

    def get_print_usage_summaries_by_user(
        self,
        period_start,  # type: datetime.datetime
        period_end,  # type: datetime.datetime
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphUserPrintUsageSummary"]
        """Invoke function getPrintUsageSummariesByUser.

        Invoke function getPrintUsageSummariesByUser.

        :param period_start:
        :type period_start: ~datetime.datetime
        :param period_end:
        :type period_end: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphUserPrintUsageSummary, or the result of cls(response)
        :rtype: list[~devices_cloud_print.models.MicrosoftGraphUserPrintUsageSummary]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphUserPrintUsageSummary"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_print_usage_summaries_by_user.metadata['url']  # type: ignore
        path_format_arguments = {
            'periodStart': self._serialize.url("period_start", period_start, 'iso-8601'),
            'periodEnd': self._serialize.url("period_end", period_end, 'iso-8601'),
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

        deserialized = self._deserialize('[MicrosoftGraphUserPrintUsageSummary]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_print_usage_summaries_by_user.metadata = {'url': '/print/reports/microsoft.graph.getPrintUsageSummariesByUser(periodStart={periodStart},periodEnd={periodEnd})'}  # type: ignore

    def get_user_archived_print_jobs(
        self,
        user_id,  # type: str
        period_start,  # type: datetime.datetime
        period_end,  # type: datetime.datetime
        **kwargs  # type: Any
    ):
        # type: (...) -> List["models.MicrosoftGraphArchivedPrintJob"]
        """Invoke function getUserArchivedPrintJobs.

        Invoke function getUserArchivedPrintJobs.

        :param user_id:
        :type user_id: str
        :param period_start:
        :type period_start: ~datetime.datetime
        :param period_end:
        :type period_end: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphArchivedPrintJob, or the result of cls(response)
        :rtype: list[~devices_cloud_print.models.MicrosoftGraphArchivedPrintJob]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphArchivedPrintJob"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_user_archived_print_jobs.metadata['url']  # type: ignore
        path_format_arguments = {
            'userId': self._serialize.url("user_id", user_id, 'str'),
            'periodStart': self._serialize.url("period_start", period_start, 'iso-8601'),
            'periodEnd': self._serialize.url("period_end", period_end, 'iso-8601'),
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

        deserialized = self._deserialize('[MicrosoftGraphArchivedPrintJob]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_user_archived_print_jobs.metadata = {'url': '/print/reports/microsoft.graph.getUserArchivedPrintJobs(userId=\'{userId}\',periodStart={periodStart},periodEnd={periodEnd})'}  # type: ignore

    def get_user_print_usage_summary(
        self,
        user_id,  # type: str
        period_start,  # type: datetime.datetime
        period_end,  # type: datetime.datetime
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphUserPrintUsageSummary"
        """Invoke function getUserPrintUsageSummary.

        Invoke function getUserPrintUsageSummary.

        :param user_id:
        :type user_id: str
        :param period_start:
        :type period_start: ~datetime.datetime
        :param period_end:
        :type period_end: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphUserPrintUsageSummary, or the result of cls(response)
        :rtype: ~devices_cloud_print.models.MicrosoftGraphUserPrintUsageSummary
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphUserPrintUsageSummary"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_user_print_usage_summary.metadata['url']  # type: ignore
        path_format_arguments = {
            'userId': self._serialize.url("user_id", user_id, 'str'),
            'periodStart': self._serialize.url("period_start", period_start, 'iso-8601'),
            'periodEnd': self._serialize.url("period_end", period_end, 'iso-8601'),
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

        deserialized = self._deserialize('MicrosoftGraphUserPrintUsageSummary', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_user_print_usage_summary.metadata = {'url': '/print/reports/microsoft.graph.getUserPrintUsageSummary(userId=\'{userId}\',periodStart={periodStart},periodEnd={periodEnd})'}  # type: ignore
