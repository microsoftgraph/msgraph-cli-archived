# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from msgraph.cli.core.commands.parameters import (
    get_three_state_flag,
    get_enum_type
)
from msgraph.cli.core.commands.validators import validate_file_or_dict
from azext_compliance_beta.action import (
    AddApplication,
    AddLastIndexOperation,
    AddUserSources
)


def load_arguments(self, _):

    with self.argument_context('compliance compliance create') as c:
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.', arg_group='Ediscovery')
        c.argument('cases', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.',
                   arg_group='Ediscovery')

    with self.argument_context('compliance compliance show-compliance') as c:
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance delete-ediscovery') as c:
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('compliance compliance show-ediscovery') as c:
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance update-ediscovery') as c:
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('cases', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')

    with self.argument_context('compliance compliance-ediscovery create-case') as c:
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('closed_date_time', help='')
        c.argument('created_date_time', help='')
        c.argument('description', type=str, help='')
        c.argument('display_name', type=str, help='')
        c.argument('external_id', type=str, help='')
        c.argument('last_modified_date_time', help='')
        c.argument('status', arg_type=get_enum_type(['unknown', 'active', 'pendingDelete', 'closing', 'closed',
                                                     'closedWithError']), help='')
        c.argument('custodians', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('review_sets', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('application', action=AddApplication, nargs='+', help='identity', arg_group='Last Modified By')
        c.argument('device', action=AddApplication, nargs='+', help='identity', arg_group='Last Modified By')
        c.argument('user', action=AddApplication, nargs='+', help='identity', arg_group='Last Modified By')
        c.argument('microsoft_graph_identity_application', action=AddApplication, nargs='+', help='identity',
                   arg_group='Closed By')
        c.argument('microsoft_graph_identity_device', action=AddApplication, nargs='+', help='identity',
                   arg_group='Closed By')
        c.argument('microsoft_graph_identity_user', action=AddApplication, nargs='+', help='identity',
                   arg_group='Closed By')

    with self.argument_context('compliance compliance-ediscovery delete-case') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('compliance compliance-ediscovery list-case') as c:
        c.argument('orderby', nargs='+', help='Order items by property values')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery show-case') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery update-case') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('closed_date_time', help='')
        c.argument('created_date_time', help='')
        c.argument('description', type=str, help='')
        c.argument('display_name', type=str, help='')
        c.argument('external_id', type=str, help='')
        c.argument('last_modified_date_time', help='')
        c.argument('status', arg_type=get_enum_type(['unknown', 'active', 'pendingDelete', 'closing', 'closed',
                                                     'closedWithError']), help='')
        c.argument('custodians', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('review_sets', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('application', action=AddApplication, nargs='+', help='identity', arg_group='Last Modified By')
        c.argument('device', action=AddApplication, nargs='+', help='identity', arg_group='Last Modified By')
        c.argument('user', action=AddApplication, nargs='+', help='identity', arg_group='Last Modified By')
        c.argument('microsoft_graph_identity_application', action=AddApplication, nargs='+', help='identity',
                   arg_group='Closed By')
        c.argument('microsoft_graph_identity_device', action=AddApplication, nargs='+', help='identity',
                   arg_group='Closed By')
        c.argument('microsoft_graph_identity_user', action=AddApplication, nargs='+', help='identity',
                   arg_group='Closed By')

    with self.argument_context('compliance compliance-ediscovery-case close') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')

    with self.argument_context('compliance compliance-ediscovery-case create-custodian') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('acknowledged_date_time', help='')
        c.argument('apply_hold_to_sources', arg_type=get_three_state_flag(), help='')
        c.argument('created_date_time', help='')
        c.argument('display_name', type=str, help='')
        c.argument('email', type=str, help='')
        c.argument('last_modified_date_time', help='')
        c.argument('released_date_time', help='')
        c.argument('status', arg_type=get_enum_type(['active', 'released']), help='')
        c.argument('last_index_operation', action=AddLastIndexOperation, nargs='+', help='caseIndexOperation')
        c.argument('site_sources', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('unified_group_sources', type=validate_file_or_dict,
                   help=' Expected value: json-string/@json-file.')
        c.argument('user_sources', action=AddUserSources, nargs='+', help='')

    with self.argument_context('compliance compliance-ediscovery-case create-review-set') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('created_date_time', help='')
        c.argument('display_name', type=str, help='')
        c.argument('queries', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('application', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('device', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('user', action=AddApplication, nargs='+', help='identity', arg_group='Created By')

    with self.argument_context('compliance compliance-ediscovery-case delete-custodian') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('compliance compliance-ediscovery-case delete-review-set') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('review_set_id', type=str, help='key: id of reviewSet')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('compliance compliance-ediscovery-case list-custodian') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('orderby', nargs='+', help='Order items by property values')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery-case list-review-set') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('orderby', nargs='+', help='Order items by property values')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery-case reopen') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')

    with self.argument_context('compliance compliance-ediscovery-case show-custodian') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery-case show-review-set') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('review_set_id', type=str, help='key: id of reviewSet')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery-case update-custodian') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('acknowledged_date_time', help='')
        c.argument('apply_hold_to_sources', arg_type=get_three_state_flag(), help='')
        c.argument('created_date_time', help='')
        c.argument('display_name', type=str, help='')
        c.argument('email', type=str, help='')
        c.argument('last_modified_date_time', help='')
        c.argument('released_date_time', help='')
        c.argument('status', arg_type=get_enum_type(['active', 'released']), help='')
        c.argument('last_index_operation', action=AddLastIndexOperation, nargs='+', help='caseIndexOperation')
        c.argument('site_sources', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('unified_group_sources', type=validate_file_or_dict,
                   help=' Expected value: json-string/@json-file.')
        c.argument('user_sources', action=AddUserSources, nargs='+', help='')

    with self.argument_context('compliance compliance-ediscovery-case update-review-set') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('review_set_id', type=str, help='key: id of reviewSet')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('created_date_time', help='')
        c.argument('display_name', type=str, help='')
        c.argument('queries', type=validate_file_or_dict, help=' Expected value: json-string/@json-file.')
        c.argument('application', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('device', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('user', action=AddApplication, nargs='+', help='identity', arg_group='Created By')

    with self.argument_context('compliance compliance-ediscovery-case-custodian activate') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')

    with self.argument_context('compliance compliance-ediscovery-case-custodian create-site-source') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('created_date_time', help='')
        c.argument('display_name', type=str, help='')
        c.argument('application', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('device', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('user', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('site', type=validate_file_or_dict, help='site Expected value: json-string/@json-file.')

    with self.argument_context('compliance compliance-ediscovery-case-custodian create-unified-group-source') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('created_date_time', help='')
        c.argument('display_name', type=str, help='')
        c.argument('application', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('device', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('user', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('included_sources', arg_type=get_enum_type(['mailbox', 'site']), help='')
        c.argument('group', type=validate_file_or_dict, help='Represents an Azure Active Directory object. The '
                   'directoryObject type is the base type for many other directory entity types. Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('compliance compliance-ediscovery-case-custodian create-user-source') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('created_date_time', help='')
        c.argument('display_name', type=str, help='')
        c.argument('application', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('device', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('user', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('email', type=str, help='')
        c.argument('included_sources', arg_type=get_enum_type(['mailbox', 'site']), help='')

    with self.argument_context('compliance compliance-ediscovery-case-custodian delete-ref-last-index-operation') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('compliance compliance-ediscovery-case-custodian delete-site-source') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('site_source_id', type=str, help='key: id of siteSource')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('compliance compliance-ediscovery-case-custodian delete-unified-group-source') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('unified_group_source_id', type=str, help='key: id of unifiedGroupSource')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('compliance compliance-ediscovery-case-custodian delete-user-source') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('user_source_id', type=str, help='key: id of userSource')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('compliance compliance-ediscovery-case-custodian list-site-source') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('orderby', nargs='+', help='Order items by property values')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery-case-custodian list-unified-group-source') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('orderby', nargs='+', help='Order items by property values')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery-case-custodian list-user-source') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('orderby', nargs='+', help='Order items by property values')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery-case-custodian release') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')

    with self.argument_context('compliance compliance-ediscovery-case-custodian set-ref-last-index-operation') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref values Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('compliance compliance-ediscovery-case-custodian show-last-index-operation') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery-case-custodian show-ref-last-index-operation') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')

    with self.argument_context('compliance compliance-ediscovery-case-custodian show-site-source') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('site_source_id', type=str, help='key: id of siteSource')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery-case-custodian show-unified-group-source') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('unified_group_source_id', type=str, help='key: id of unifiedGroupSource')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery-case-custodian show-user-source') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('user_source_id', type=str, help='key: id of userSource')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery-case-custodian update-index') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')

    with self.argument_context('compliance compliance-ediscovery-case-custodian update-site-source') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('site_source_id', type=str, help='key: id of siteSource')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('created_date_time', help='')
        c.argument('display_name', type=str, help='')
        c.argument('application', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('device', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('user', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('site', type=validate_file_or_dict, help='site Expected value: json-string/@json-file.')

    with self.argument_context('compliance compliance-ediscovery-case-custodian update-unified-group-source') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('unified_group_source_id', type=str, help='key: id of unifiedGroupSource')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('created_date_time', help='')
        c.argument('display_name', type=str, help='')
        c.argument('application', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('device', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('user', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('included_sources', arg_type=get_enum_type(['mailbox', 'site']), help='')
        c.argument('group', type=validate_file_or_dict, help='Represents an Azure Active Directory object. The '
                   'directoryObject type is the base type for many other directory entity types. Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('compliance compliance-ediscovery-case-custodian update-user-source') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('user_source_id', type=str, help='key: id of userSource')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('created_date_time', help='')
        c.argument('display_name', type=str, help='')
        c.argument('application', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('device', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('user', action=AddApplication, nargs='+', help='identity', arg_group='Created By')
        c.argument('email', type=str, help='')
        c.argument('included_sources', arg_type=get_enum_type(['mailbox', 'site']), help='')

    with self.argument_context('compliance compliance-ediscovery-case-custodian-site-source delete-ref-site') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('site_source_id', type=str, help='key: id of siteSource')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('compliance compliance-ediscovery-case-custodian-site-source set-ref-site') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('site_source_id', type=str, help='key: id of siteSource')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref values Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('compliance compliance-ediscovery-case-custodian-site-source show-ref-site') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('site_source_id', type=str, help='key: id of siteSource')

    with self.argument_context('compliance compliance-ediscovery-case-custodian-site-source show-site') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('site_source_id', type=str, help='key: id of siteSource')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery-case-custodian-unified-group-source delete-ref-group') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('unified_group_source_id', type=str, help='key: id of unifiedGroupSource')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('compliance compliance-ediscovery-case-custodian-unified-group-source set-ref-group') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('unified_group_source_id', type=str, help='key: id of unifiedGroupSource')
        c.argument('body', type=validate_file_or_dict, help='New navigation property ref values Expected value: '
                   'json-string/@json-file.')

    with self.argument_context('compliance compliance-ediscovery-case-custodian-unified-group-source show-group') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('unified_group_source_id', type=str, help='key: id of unifiedGroupSource')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery-case-custodian-unified-group-source show-ref-group') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('custodian_id', type=str, help='key: id of custodian')
        c.argument('unified_group_source_id', type=str, help='key: id of unifiedGroupSource')

    with self.argument_context('compliance compliance-ediscovery-case-review-set create-query') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('review_set_id', type=str, help='key: id of reviewSet')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('created_date_time', help='')
        c.argument('display_name', type=str, help='')
        c.argument('last_modified_date_time', help='')
        c.argument('query', type=str, help='')
        c.argument('application', action=AddApplication, nargs='+', help='identity', arg_group='Last Modified By')
        c.argument('device', action=AddApplication, nargs='+', help='identity', arg_group='Last Modified By')
        c.argument('user', action=AddApplication, nargs='+', help='identity', arg_group='Last Modified By')
        c.argument('microsoft_graph_identity_application', action=AddApplication, nargs='+', help='identity',
                   arg_group='Created By')
        c.argument('microsoft_graph_identity_device', action=AddApplication, nargs='+', help='identity',
                   arg_group='Created By')
        c.argument('microsoft_graph_identity_user', action=AddApplication, nargs='+', help='identity',
                   arg_group='Created By')

    with self.argument_context('compliance compliance-ediscovery-case-review-set delete-query') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('review_set_id', type=str, help='key: id of reviewSet')
        c.argument('review_set_query_id', type=str, help='key: id of reviewSetQuery')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('compliance compliance-ediscovery-case-review-set list-query') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('review_set_id', type=str, help='key: id of reviewSet')
        c.argument('orderby', nargs='+', help='Order items by property values')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery-case-review-set show-query') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('review_set_id', type=str, help='key: id of reviewSet')
        c.argument('review_set_query_id', type=str, help='key: id of reviewSetQuery')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('compliance compliance-ediscovery-case-review-set update-query') as c:
        c.argument('ediscovery_case_id', type=str, help='key: id of ediscoveryCase')
        c.argument('review_set_id', type=str, help='key: id of reviewSet')
        c.argument('review_set_query_id', type=str, help='key: id of reviewSetQuery')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('created_date_time', help='')
        c.argument('display_name', type=str, help='')
        c.argument('last_modified_date_time', help='')
        c.argument('query', type=str, help='')
        c.argument('application', action=AddApplication, nargs='+', help='identity', arg_group='Last Modified By')
        c.argument('device', action=AddApplication, nargs='+', help='identity', arg_group='Last Modified By')
        c.argument('user', action=AddApplication, nargs='+', help='identity', arg_group='Last Modified By')
        c.argument('microsoft_graph_identity_application', action=AddApplication, nargs='+', help='identity',
                   arg_group='Created By')
        c.argument('microsoft_graph_identity_device', action=AddApplication, nargs='+', help='identity',
                   arg_group='Created By')
        c.argument('microsoft_graph_identity_user', action=AddApplication, nargs='+', help='identity',
                   arg_group='Created By')