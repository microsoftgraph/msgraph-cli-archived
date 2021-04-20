# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['compliance_beta'] = '''
    type: group
    short-summary: Manage Compliance
'''

helps['compliance compliance'] = """
    type: group
    short-summary: Manage compliance with compliance_beta
"""

helps['compliance compliance show-compliance'] = """
    type: command
    short-summary: "Get compliance."
"""

helps['compliance compliance update-compliance'] = """
    type: command
    short-summary: "Update compliance."
"""

helps['compliance compliance'] = """
    type: group
    short-summary: Manage compliance with compliance_beta
"""

helps['compliance compliance delete-ediscovery'] = """
    type: command
    short-summary: "Delete navigation property ediscovery for compliance."
"""

helps['compliance compliance show-ediscovery'] = """
    type: command
    short-summary: "Get ediscovery from compliance."
"""

helps['compliance compliance update-ediscovery'] = """
    type: command
    short-summary: "Update the navigation property ediscovery in compliance."
"""

helps['compliance complianceediscovery'] = """
    type: group
    short-summary: Manage complianceediscovery with compliance_beta
"""

helps['compliance complianceediscovery create-case'] = """
    type: command
    short-summary: "Create new navigation property to cases for compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-application
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-device
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-user
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance complianceediscovery delete-case'] = """
    type: command
    short-summary: "Delete navigation property cases for compliance."
"""

helps['compliance complianceediscovery list-case'] = """
    type: command
    short-summary: "Get cases from compliance."
"""

helps['compliance complianceediscovery show-case'] = """
    type: command
    short-summary: "Get cases from compliance."
"""

helps['compliance complianceediscovery update-case'] = """
    type: command
    short-summary: "Update the navigation property cases in compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-application
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-device
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-user
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance complianceediscoverycase'] = """
    type: group
    short-summary: Manage complianceediscoverycase with compliance_beta
"""

helps['compliance complianceediscoverycase close'] = """
    type: command
    short-summary: "Invoke action close."
"""

helps['compliance complianceediscoverycase create-custodian'] = """
    type: command
    short-summary: "Create new navigation property to custodians for compliance."
    parameters:
      - name: --last-index-operation
        short-summary: "caseIndexOperation"
        long-summary: |
            Usage: --last-index-operation action=XX completed-date-time=XX created-date-time=XX display-name=XX \
percent-progress=XX status=XX id=XX

            id: Read-only.
      - name: --user-sources
        long-summary: |
            Usage: --user-sources email=XX included-sources=XX created-date-time=XX display-name=XX application=XX \
device=XX user=XX id=XX

            application: identity
            device: identity
            user: identity
            id: Read-only.

            Multiple actions can be specified by using more than one --user-sources argument.
"""

helps['compliance complianceediscoverycase create-review-set'] = """
    type: command
    short-summary: "Create new navigation property to reviewSets for compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance complianceediscoverycase delete-custodian'] = """
    type: command
    short-summary: "Delete navigation property custodians for compliance."
"""

helps['compliance complianceediscoverycase delete-review-set'] = """
    type: command
    short-summary: "Delete navigation property reviewSets for compliance."
"""

helps['compliance complianceediscoverycase list-custodian'] = """
    type: command
    short-summary: "Get custodians from compliance."
"""

helps['compliance complianceediscoverycase list-review-set'] = """
    type: command
    short-summary: "Get reviewSets from compliance."
"""

helps['compliance complianceediscoverycase reopen'] = """
    type: command
    short-summary: "Invoke action reopen."
"""

helps['compliance complianceediscoverycase show-custodian'] = """
    type: command
    short-summary: "Get custodians from compliance."
"""

helps['compliance complianceediscoverycase show-review-set'] = """
    type: command
    short-summary: "Get reviewSets from compliance."
"""

helps['compliance complianceediscoverycase update-custodian'] = """
    type: command
    short-summary: "Update the navigation property custodians in compliance."
    parameters:
      - name: --last-index-operation
        short-summary: "caseIndexOperation"
        long-summary: |
            Usage: --last-index-operation action=XX completed-date-time=XX created-date-time=XX display-name=XX \
percent-progress=XX status=XX id=XX

            id: Read-only.
      - name: --user-sources
        long-summary: |
            Usage: --user-sources email=XX included-sources=XX created-date-time=XX display-name=XX application=XX \
device=XX user=XX id=XX

            application: identity
            device: identity
            user: identity
            id: Read-only.

            Multiple actions can be specified by using more than one --user-sources argument.
"""

helps['compliance complianceediscoverycase update-review-set'] = """
    type: command
    short-summary: "Update the navigation property reviewSets in compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance complianceediscoverycasescustodian'] = """
    type: group
    short-summary: Manage complianceediscoverycasescustodian with compliance_beta
"""

helps['compliance complianceediscoverycasescustodian activate'] = """
    type: command
    short-summary: "Invoke action activate."
"""

helps['compliance complianceediscoverycasescustodian create-site-source'] = """
    type: command
    short-summary: "Create new navigation property to siteSources for compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance complianceediscoverycasescustodian create-unified-group-source'] = """
    type: command
    short-summary: "Create new navigation property to unifiedGroupSources for compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance complianceediscoverycasescustodian create-user-source'] = """
    type: command
    short-summary: "Create new navigation property to userSources for compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance complianceediscoverycasescustodian delete-ref-last-index-operation'] = """
    type: command
    short-summary: "Delete ref of navigation property lastIndexOperation for compliance."
"""

helps['compliance complianceediscoverycasescustodian delete-site-source'] = """
    type: command
    short-summary: "Delete navigation property siteSources for compliance."
"""

helps['compliance complianceediscoverycasescustodian delete-unified-group-source'] = """
    type: command
    short-summary: "Delete navigation property unifiedGroupSources for compliance."
"""

helps['compliance complianceediscoverycasescustodian delete-user-source'] = """
    type: command
    short-summary: "Delete navigation property userSources for compliance."
"""

helps['compliance complianceediscoverycasescustodian list-site-source'] = """
    type: command
    short-summary: "Get siteSources from compliance."
"""

helps['compliance complianceediscoverycasescustodian list-unified-group-source'] = """
    type: command
    short-summary: "Get unifiedGroupSources from compliance."
"""

helps['compliance complianceediscoverycasescustodian list-user-source'] = """
    type: command
    short-summary: "Get userSources from compliance."
"""

helps['compliance complianceediscoverycasescustodian release'] = """
    type: command
    short-summary: "Invoke action release."
"""

helps['compliance complianceediscoverycasescustodian set-ref-last-index-operation'] = """
    type: command
    short-summary: "Update the ref of navigation property lastIndexOperation in compliance."
"""

helps['compliance complianceediscoverycasescustodian show-last-index-operation'] = """
    type: command
    short-summary: "Get lastIndexOperation from compliance."
"""

helps['compliance complianceediscoverycasescustodian show-ref-last-index-operation'] = """
    type: command
    short-summary: "Get ref of lastIndexOperation from compliance."
"""

helps['compliance complianceediscoverycasescustodian show-site-source'] = """
    type: command
    short-summary: "Get siteSources from compliance."
"""

helps['compliance complianceediscoverycasescustodian show-unified-group-source'] = """
    type: command
    short-summary: "Get unifiedGroupSources from compliance."
"""

helps['compliance complianceediscoverycasescustodian show-user-source'] = """
    type: command
    short-summary: "Get userSources from compliance."
"""

helps['compliance complianceediscoverycasescustodian update-index'] = """
    type: command
    short-summary: "Invoke action updateIndex."
"""

helps['compliance complianceediscoverycasescustodian update-site-source'] = """
    type: command
    short-summary: "Update the navigation property siteSources in compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance complianceediscoverycasescustodian update-unified-group-source'] = """
    type: command
    short-summary: "Update the navigation property unifiedGroupSources in compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance complianceediscoverycasescustodian update-user-source'] = """
    type: command
    short-summary: "Update the navigation property userSources in compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance complianceediscoverycasescustodianssitesource'] = """
    type: group
    short-summary: Manage complianceediscoverycasescustodianssitesource with compliance_beta
"""

helps['compliance complianceediscoverycasescustodianssitesource delete-ref-site'] = """
    type: command
    short-summary: "Delete ref of navigation property site for compliance."
"""

helps['compliance complianceediscoverycasescustodianssitesource set-ref-site'] = """
    type: command
    short-summary: "Update the ref of navigation property site in compliance."
"""

helps['compliance complianceediscoverycasescustodianssitesource show-ref-site'] = """
    type: command
    short-summary: "Get ref of site from compliance."
"""

helps['compliance complianceediscoverycasescustodianssitesource show-site'] = """
    type: command
    short-summary: "Get site from compliance."
"""

helps['compliance complianceediscoverycasescustodiansunifiedgroupsource'] = """
    type: group
    short-summary: Manage complianceediscoverycasescustodiansunifiedgroupsource with compliance_beta
"""

helps['compliance complianceediscoverycasescustodiansunifiedgroupsource delete-ref-group'] = """
    type: command
    short-summary: "Delete ref of navigation property group for compliance."
"""

helps['compliance complianceediscoverycasescustodiansunifiedgroupsource set-ref-group'] = """
    type: command
    short-summary: "Update the ref of navigation property group in compliance."
"""

helps['compliance complianceediscoverycasescustodiansunifiedgroupsource show-group'] = """
    type: command
    short-summary: "Get group from compliance."
"""

helps['compliance complianceediscoverycasescustodiansunifiedgroupsource show-ref-group'] = """
    type: command
    short-summary: "Get ref of group from compliance."
"""

helps['compliance complianceediscoverycasesreviewset'] = """
    type: group
    short-summary: Manage complianceediscoverycasesreviewset with compliance_beta
"""

helps['compliance complianceediscoverycasesreviewset create-query'] = """
    type: command
    short-summary: "Create new navigation property to queries for compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-application
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-device
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-user
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""

helps['compliance complianceediscoverycasesreviewset delete-query'] = """
    type: command
    short-summary: "Delete navigation property queries for compliance."
"""

helps['compliance complianceediscoverycasesreviewset list-query'] = """
    type: command
    short-summary: "Get queries from compliance."
"""

helps['compliance complianceediscoverycasesreviewset show-query'] = """
    type: command
    short-summary: "Get queries from compliance."
"""

helps['compliance complianceediscoverycasesreviewset update-query'] = """
    type: command
    short-summary: "Update the navigation property queries in compliance."
    parameters:
      - name: --application
        short-summary: "identity"
        long-summary: |
            Usage: --application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --device
        short-summary: "identity"
        long-summary: |
            Usage: --device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --user
        short-summary: "identity"
        long-summary: |
            Usage: --user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-application
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-application display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-device
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-device display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
      - name: --microsoft-graph-identity-user
        short-summary: "identity"
        long-summary: |
            Usage: --microsoft-graph-identity-user display-name=XX id=XX

            display-name: The identity's display name. Note that this may not always be available or up to date. For \
example, if a user changes their display name, the API may show the new value in a future response, but the items \
associated with the user won't show up as having changed when using delta.
            id: Unique identifier for the identity.
"""
