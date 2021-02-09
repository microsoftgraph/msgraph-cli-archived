# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class UserOperations:
    """UserOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~people.models
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

    async def get_insight(
        self,
        user_id: str,
        select: Optional[List[Union[str, "models.Get1ItemsItem"]]] = None,
        expand: Optional[List[Union[str, "models.Get2ItemsItem"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphOfficeGraphInsights":
        """Get insights from users.

        Get insights from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~people.models.Get1ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str or ~people.models.Get2ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOfficeGraphInsights, or the result of cls(response)
        :rtype: ~people.models.MicrosoftGraphOfficeGraphInsights
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOfficeGraphInsights"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_insight.metadata['url']  # type: ignore
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
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphOfficeGraphInsights', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_insight.metadata = {'url': '/users/{user-id}/insights'}  # type: ignore

    async def update_insight(
        self,
        user_id: str,
        id: Optional[str] = None,
        shared: Optional[List["models.MicrosoftGraphSharedInsight"]] = None,
        trending: Optional[List["models.MicrosoftGraphTrending"]] = None,
        used: Optional[List["models.MicrosoftGraphUsedInsight"]] = None,
        **kwargs
    ) -> None:
        """Update the navigation property insights in users.

        Update the navigation property insights in users.

        :param user_id: key: id of user.
        :type user_id: str
        :param id: Read-only.
        :type id: str
        :param shared: Calculated relationship identifying documents shared with or by the user. This
         includes URLs, file attachments, and reference attachments to OneDrive for Business and
         SharePoint files found in Outlook messages and meetings. This also includes URLs and reference
         attachments to Teams conversations. Ordered by recency of share.
        :type shared: list[~people.models.MicrosoftGraphSharedInsight]
        :param trending: Calculated relationship identifying documents trending around a user. Trending
         documents are calculated based on activity of the user's closest network of people and include
         files stored in OneDrive for Business and SharePoint. Trending insights help the user to
         discover potentially useful content that the user has access to, but has never viewed before.
        :type trending: list[~people.models.MicrosoftGraphTrending]
        :param used: Calculated relationship identifying the latest documents viewed or modified by a
         user, including OneDrive for Business and SharePoint documents, ranked by recency of use.
        :type used: list[~people.models.MicrosoftGraphUsedInsight]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphOfficeGraphInsights(id=id, shared=shared, trending=trending, used=used)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_insight.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphOfficeGraphInsights')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_insight.metadata = {'url': '/users/{user-id}/insights'}  # type: ignore

    async def delete_insight(
        self,
        user_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property insights for users.

        Delete navigation property insights for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param if_match: ETag.
        :type if_match: str
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
        url = self.delete_insight.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_insight.metadata = {'url': '/users/{user-id}/insights'}  # type: ignore

    def list_person(
        self,
        user_id: str,
        orderby: Optional[List[Union[str, "models.Enum17"]]] = None,
        select: Optional[List[Union[str, "models.Enum18"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> AsyncIterable["models.CollectionOfPerson"]:
        """Get people from users.

        Get people from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~people.models.Enum17]
        :param select: Select properties to be returned.
        :type select: list[str or ~people.models.Enum18]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfPerson or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~people.models.CollectionOfPerson]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfPerson"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_person.metadata['url']  # type: ignore
                path_format_arguments = {
                    'user-id': self._serialize.url("user_id", user_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if self._config.top is not None:
                    query_parameters['$top'] = self._serialize.query("self._config.top", self._config.top, 'int', minimum=0)
                if self._config.skip is not None:
                    query_parameters['$skip'] = self._serialize.query("self._config.skip", self._config.skip, 'int', minimum=0)
                if self._config.search is not None:
                    query_parameters['$search'] = self._serialize.query("self._config.search", self._config.search, 'str')
                if self._config.filter is not None:
                    query_parameters['$filter'] = self._serialize.query("self._config.filter", self._config.filter, 'str')
                if self._config.count is not None:
                    query_parameters['$count'] = self._serialize.query("self._config.count", self._config.count, 'bool')
                if orderby is not None:
                    query_parameters['$orderby'] = self._serialize.query("orderby", orderby, '[str]', div=',')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('CollectionOfPerson', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.OdataError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_person.metadata = {'url': '/users/{user-id}/people'}  # type: ignore

    async def create_person(
        self,
        user_id: str,
        id: Optional[str] = None,
        birthday: Optional[str] = None,
        company_name: Optional[str] = None,
        department: Optional[str] = None,
        display_name: Optional[str] = None,
        given_name: Optional[str] = None,
        im_address: Optional[str] = None,
        is_favorite: Optional[bool] = None,
        job_title: Optional[str] = None,
        office_location: Optional[str] = None,
        person_notes: Optional[str] = None,
        person_type: Optional["models.MicrosoftGraphPersonType"] = None,
        phones: Optional[List["models.MicrosoftGraphPhone"]] = None,
        postal_addresses: Optional[List["models.MicrosoftGraphLocation"]] = None,
        profession: Optional[str] = None,
        scored_email_addresses: Optional[List["models.MicrosoftGraphScoredEmailAddress"]] = None,
        surname: Optional[str] = None,
        user_principal_name: Optional[str] = None,
        websites: Optional[List["models.MicrosoftGraphWebsite"]] = None,
        yomi_company: Optional[str] = None,
        **kwargs
    ) -> "models.MicrosoftGraphPerson":
        """Create new navigation property to people for users.

        Create new navigation property to people for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param id: Read-only.
        :type id: str
        :param birthday: The person's birthday.
        :type birthday: str
        :param company_name: The name of the person's company.
        :type company_name: str
        :param department: The person's department.
        :type department: str
        :param display_name: The person's display name.
        :type display_name: str
        :param given_name: The person's given name.
        :type given_name: str
        :param im_address: The instant message voice over IP (VOIP) session initiation protocol (SIP)
         address for the user. Read-only.
        :type im_address: str
        :param is_favorite: true if the user has flagged this person as a favorite.
        :type is_favorite: bool
        :param job_title: The person's job title.
        :type job_title: str
        :param office_location: The location of the person's office.
        :type office_location: str
        :param person_notes: Free-form notes that the user has taken about this person.
        :type person_notes: str
        :param person_type: personType.
        :type person_type: ~people.models.MicrosoftGraphPersonType
        :param phones: The person's phone numbers.
        :type phones: list[~people.models.MicrosoftGraphPhone]
        :param postal_addresses: The person's addresses.
        :type postal_addresses: list[~people.models.MicrosoftGraphLocation]
        :param profession: The person's profession.
        :type profession: str
        :param scored_email_addresses: The person's email addresses.
        :type scored_email_addresses: list[~people.models.MicrosoftGraphScoredEmailAddress]
        :param surname: The person's surname.
        :type surname: str
        :param user_principal_name: The user principal name (UPN) of the person. The UPN is an
         Internet-style login name for the person based on the Internet standard RFC 822. By convention,
         this should map to the person's email name. The general format is alias@domain.
        :type user_principal_name: str
        :param websites: The person's websites.
        :type websites: list[~people.models.MicrosoftGraphWebsite]
        :param yomi_company: The phonetic Japanese name of the person's company.
        :type yomi_company: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPerson, or the result of cls(response)
        :rtype: ~people.models.MicrosoftGraphPerson
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPerson"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPerson(id=id, birthday=birthday, company_name=company_name, department=department, display_name=display_name, given_name=given_name, im_address=im_address, is_favorite=is_favorite, job_title=job_title, office_location=office_location, person_notes=person_notes, person_type=person_type, phones=phones, postal_addresses=postal_addresses, profession=profession, scored_email_addresses=scored_email_addresses, surname=surname, user_principal_name=user_principal_name, websites=websites, yomi_company=yomi_company)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_person.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPerson')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPerson', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_person.metadata = {'url': '/users/{user-id}/people'}  # type: ignore

    async def get_person(
        self,
        user_id: str,
        person_id: str,
        select: Optional[List[Union[str, "models.Enum24"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphPerson":
        """Get people from users.

        Get people from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param person_id: key: id of person.
        :type person_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~people.models.Enum24]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPerson, or the result of cls(response)
        :rtype: ~people.models.MicrosoftGraphPerson
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPerson"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_person.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'person-id': self._serialize.url("person_id", person_id, 'str'),
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
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPerson', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_person.metadata = {'url': '/users/{user-id}/people/{person-id}'}  # type: ignore

    async def update_person(
        self,
        user_id: str,
        person_id: str,
        id: Optional[str] = None,
        birthday: Optional[str] = None,
        company_name: Optional[str] = None,
        department: Optional[str] = None,
        display_name: Optional[str] = None,
        given_name: Optional[str] = None,
        im_address: Optional[str] = None,
        is_favorite: Optional[bool] = None,
        job_title: Optional[str] = None,
        office_location: Optional[str] = None,
        person_notes: Optional[str] = None,
        person_type: Optional["models.MicrosoftGraphPersonType"] = None,
        phones: Optional[List["models.MicrosoftGraphPhone"]] = None,
        postal_addresses: Optional[List["models.MicrosoftGraphLocation"]] = None,
        profession: Optional[str] = None,
        scored_email_addresses: Optional[List["models.MicrosoftGraphScoredEmailAddress"]] = None,
        surname: Optional[str] = None,
        user_principal_name: Optional[str] = None,
        websites: Optional[List["models.MicrosoftGraphWebsite"]] = None,
        yomi_company: Optional[str] = None,
        **kwargs
    ) -> None:
        """Update the navigation property people in users.

        Update the navigation property people in users.

        :param user_id: key: id of user.
        :type user_id: str
        :param person_id: key: id of person.
        :type person_id: str
        :param id: Read-only.
        :type id: str
        :param birthday: The person's birthday.
        :type birthday: str
        :param company_name: The name of the person's company.
        :type company_name: str
        :param department: The person's department.
        :type department: str
        :param display_name: The person's display name.
        :type display_name: str
        :param given_name: The person's given name.
        :type given_name: str
        :param im_address: The instant message voice over IP (VOIP) session initiation protocol (SIP)
         address for the user. Read-only.
        :type im_address: str
        :param is_favorite: true if the user has flagged this person as a favorite.
        :type is_favorite: bool
        :param job_title: The person's job title.
        :type job_title: str
        :param office_location: The location of the person's office.
        :type office_location: str
        :param person_notes: Free-form notes that the user has taken about this person.
        :type person_notes: str
        :param person_type: personType.
        :type person_type: ~people.models.MicrosoftGraphPersonType
        :param phones: The person's phone numbers.
        :type phones: list[~people.models.MicrosoftGraphPhone]
        :param postal_addresses: The person's addresses.
        :type postal_addresses: list[~people.models.MicrosoftGraphLocation]
        :param profession: The person's profession.
        :type profession: str
        :param scored_email_addresses: The person's email addresses.
        :type scored_email_addresses: list[~people.models.MicrosoftGraphScoredEmailAddress]
        :param surname: The person's surname.
        :type surname: str
        :param user_principal_name: The user principal name (UPN) of the person. The UPN is an
         Internet-style login name for the person based on the Internet standard RFC 822. By convention,
         this should map to the person's email name. The general format is alias@domain.
        :type user_principal_name: str
        :param websites: The person's websites.
        :type websites: list[~people.models.MicrosoftGraphWebsite]
        :param yomi_company: The phonetic Japanese name of the person's company.
        :type yomi_company: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPerson(id=id, birthday=birthday, company_name=company_name, department=department, display_name=display_name, given_name=given_name, im_address=im_address, is_favorite=is_favorite, job_title=job_title, office_location=office_location, person_notes=person_notes, person_type=person_type, phones=phones, postal_addresses=postal_addresses, profession=profession, scored_email_addresses=scored_email_addresses, surname=surname, user_principal_name=user_principal_name, websites=websites, yomi_company=yomi_company)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_person.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'person-id': self._serialize.url("person_id", person_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPerson')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_person.metadata = {'url': '/users/{user-id}/people/{person-id}'}  # type: ignore

    async def delete_person(
        self,
        user_id: str,
        person_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property people for users.

        Delete navigation property people for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param person_id: key: id of person.
        :type person_id: str
        :param if_match: ETag.
        :type if_match: str
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
        url = self.delete_person.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'person-id': self._serialize.url("person_id", person_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_person.metadata = {'url': '/users/{user-id}/people/{person-id}'}  # type: ignore