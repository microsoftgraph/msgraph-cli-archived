# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import IdentitySignInsConfiguration
from .operations import datapolicyoperationsdatapolicyoperationOperations
from .operations import identityOperations
from .operations import identityconditionalaccessOperations
from .operations import identityprovidersidentityproviderOperations
from .operations import informationprotectioninformationprotectionOperations
from .operations import informationprotectionOperations
from .operations import informationprotectionthreatassessmentrequestsOperations
from .operations import invitationsinvitationOperations
from .operations import invitationsOperations
from .operations import oauth2permissiongrantsoauth2permissiongrantOperations
from .operations import oauth2permissiongrantsOperations
from .operations import organizationOperations
from .operations import policiespolicyrootOperations
from .operations import policiesOperations
from .operations import policiespermissiongrantpoliciesOperations
from .. import models


class IdentitySignIns(object):
    """IdentitySignIns.

    :ivar datapolicyoperationsdatapolicyoperation: datapolicyoperationsdatapolicyoperationOperations operations
    :vartype datapolicyoperationsdatapolicyoperation: identity_sign_ins.aio.operations.datapolicyoperationsdatapolicyoperationOperations
    :ivar identity: identityOperations operations
    :vartype identity: identity_sign_ins.aio.operations.identityOperations
    :ivar identityconditionalaccess: identityconditionalaccessOperations operations
    :vartype identityconditionalaccess: identity_sign_ins.aio.operations.identityconditionalaccessOperations
    :ivar identityprovidersidentityprovider: identityprovidersidentityproviderOperations operations
    :vartype identityprovidersidentityprovider: identity_sign_ins.aio.operations.identityprovidersidentityproviderOperations
    :ivar informationprotectioninformationprotection: informationprotectioninformationprotectionOperations operations
    :vartype informationprotectioninformationprotection: identity_sign_ins.aio.operations.informationprotectioninformationprotectionOperations
    :ivar informationprotection: informationprotectionOperations operations
    :vartype informationprotection: identity_sign_ins.aio.operations.informationprotectionOperations
    :ivar informationprotectionthreatassessmentrequests: informationprotectionthreatassessmentrequestsOperations operations
    :vartype informationprotectionthreatassessmentrequests: identity_sign_ins.aio.operations.informationprotectionthreatassessmentrequestsOperations
    :ivar invitationsinvitation: invitationsinvitationOperations operations
    :vartype invitationsinvitation: identity_sign_ins.aio.operations.invitationsinvitationOperations
    :ivar invitations: invitationsOperations operations
    :vartype invitations: identity_sign_ins.aio.operations.invitationsOperations
    :ivar oauth2permissiongrantsoauth2permissiongrant: oauth2permissiongrantsoauth2permissiongrantOperations operations
    :vartype oauth2permissiongrantsoauth2permissiongrant: identity_sign_ins.aio.operations.oauth2permissiongrantsoauth2permissiongrantOperations
    :ivar oauth2permissiongrants: oauth2permissiongrantsOperations operations
    :vartype oauth2permissiongrants: identity_sign_ins.aio.operations.oauth2permissiongrantsOperations
    :ivar organization: organizationOperations operations
    :vartype organization: identity_sign_ins.aio.operations.organizationOperations
    :ivar policiespolicyroot: policiespolicyrootOperations operations
    :vartype policiespolicyroot: identity_sign_ins.aio.operations.policiespolicyrootOperations
    :ivar policies: policiesOperations operations
    :vartype policies: identity_sign_ins.aio.operations.policiesOperations
    :ivar policiespermissiongrantpolicies: policiespermissiongrantpoliciesOperations operations
    :vartype policiespermissiongrantpolicies: identity_sign_ins.aio.operations.policiespermissiongrantpoliciesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param top: Show only the first n items.
    :type top: int
    :param skip: Skip the first n items.
    :type skip: int
    :param search: Search items by search phrases.
    :type search: str
    :param filter: Filter items by property values.
    :type filter: str
    :param count: Include count of items.
    :type count: bool
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://graph.microsoft.com/v1.0'
        self._config = IdentitySignInsConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.datapolicyoperationsdatapolicyoperation = datapolicyoperationsdatapolicyoperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.identity = identityOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.identityconditionalaccess = identityconditionalaccessOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.identityprovidersidentityprovider = identityprovidersidentityproviderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.informationprotectioninformationprotection = informationprotectioninformationprotectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.informationprotection = informationprotectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.informationprotectionthreatassessmentrequests = informationprotectionthreatassessmentrequestsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.invitationsinvitation = invitationsinvitationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.invitations = invitationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.oauth2permissiongrantsoauth2permissiongrant = oauth2permissiongrantsoauth2permissiongrantOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.oauth2permissiongrants = oauth2permissiongrantsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.organization = organizationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.policiespolicyroot = policiespolicyrootOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.policies = policiesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.policiespermissiongrantpolicies = policiespermissiongrantpoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "IdentitySignIns":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)