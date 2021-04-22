# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import ComplianceConfiguration
from .operations import ComplianceComplianceOperations
from .operations import ComplianceOperations
from .operations import ComplianceEdiscoveryOperations
from .operations import ComplianceEdiscoveryCasesOperations
from .operations import ComplianceEdiscoveryCasesCustodiansOperations
from .operations import ComplianceEdiscoveryCasesCustodiansSiteSourcesOperations
from .operations import ComplianceEdiscoveryCasesCustodiansUnifiedGroupSourcesOperations
from .operations import ComplianceEdiscoveryCasesReviewSetsOperations
from . import models


class Compliance(object):
    """Compliance.

    :ivar compliance_compliance: ComplianceComplianceOperations operations
    :vartype compliance_compliance: compliance.operations.ComplianceComplianceOperations
    :ivar compliance: ComplianceOperations operations
    :vartype compliance: compliance.operations.ComplianceOperations
    :ivar compliance_ediscovery: ComplianceEdiscoveryOperations operations
    :vartype compliance_ediscovery: compliance.operations.ComplianceEdiscoveryOperations
    :ivar compliance_ediscovery_cases: ComplianceEdiscoveryCasesOperations operations
    :vartype compliance_ediscovery_cases: compliance.operations.ComplianceEdiscoveryCasesOperations
    :ivar compliance_ediscovery_cases_custodians: ComplianceEdiscoveryCasesCustodiansOperations operations
    :vartype compliance_ediscovery_cases_custodians: compliance.operations.ComplianceEdiscoveryCasesCustodiansOperations
    :ivar compliance_ediscovery_cases_custodians_site_sources: ComplianceEdiscoveryCasesCustodiansSiteSourcesOperations operations
    :vartype compliance_ediscovery_cases_custodians_site_sources: compliance.operations.ComplianceEdiscoveryCasesCustodiansSiteSourcesOperations
    :ivar compliance_ediscovery_cases_custodians_unified_group_sources: ComplianceEdiscoveryCasesCustodiansUnifiedGroupSourcesOperations operations
    :vartype compliance_ediscovery_cases_custodians_unified_group_sources: compliance.operations.ComplianceEdiscoveryCasesCustodiansUnifiedGroupSourcesOperations
    :ivar compliance_ediscovery_cases_review_sets: ComplianceEdiscoveryCasesReviewSetsOperations operations
    :vartype compliance_ediscovery_cases_review_sets: compliance.operations.ComplianceEdiscoveryCasesReviewSetsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
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
        credential,  # type: "TokenCredential"
        top=None,  # type: Optional[int]
        skip=None,  # type: Optional[int]
        search=None,  # type: Optional[str]
        filter=None,  # type: Optional[str]
        count=None,  # type: Optional[bool]
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://graph.microsoft.com/beta'
        self._config = ComplianceConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.compliance_compliance = ComplianceComplianceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.compliance = ComplianceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.compliance_ediscovery = ComplianceEdiscoveryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.compliance_ediscovery_cases = ComplianceEdiscoveryCasesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.compliance_ediscovery_cases_custodians = ComplianceEdiscoveryCasesCustodiansOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.compliance_ediscovery_cases_custodians_site_sources = ComplianceEdiscoveryCasesCustodiansSiteSourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.compliance_ediscovery_cases_custodians_unified_group_sources = ComplianceEdiscoveryCasesCustodiansUnifiedGroupSourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.compliance_ediscovery_cases_review_sets = ComplianceEdiscoveryCasesReviewSetsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> Compliance
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
