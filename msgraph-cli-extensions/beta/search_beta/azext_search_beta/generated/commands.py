# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=line-too-long

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_search_beta.generated._client_factory import cf_external_external

    search_beta_external_external = CliCommandType(
        operations_tmpl='azext_search_beta.vendored_sdks.search.operations._external_external_operations#ExternalExternalOperations.{}',
        client_factory=cf_external_external,
    )
    with self.command_group(
        'search external-external', search_beta_external_external, client_factory=cf_external_external
    ) as g:
        g.custom_command('show-external', 'search_external_external_show_external')
        g.custom_command('update-external', 'search_external_external_update_external')

    from azext_search_beta.generated._client_factory import cf_external

    search_beta_external = CliCommandType(
        operations_tmpl='azext_search_beta.vendored_sdks.search.operations._external_operations#ExternalOperations.{}',
        client_factory=cf_external,
    )
    with self.command_group('search external', search_beta_external, client_factory=cf_external) as g:
        g.custom_command('delete', 'search_external_delete', confirmation=True)
        g.custom_command('create-connection', 'search_external_create_connection')
        g.custom_command('list-connection', 'search_external_list_connection')
        g.custom_command('show-connection', 'search_external_show_connection')
        g.custom_command('update-connection', 'search_external_update_connection')

    from azext_search_beta.generated._client_factory import cf_search_search_entity

    search_beta_search_search_entity = CliCommandType(
        operations_tmpl='azext_search_beta.vendored_sdks.search.operations._search_search_entity_operations#SearchSearchEntityOperations.{}',
        client_factory=cf_search_search_entity,
    )
    with self.command_group(
        'search search-entity', search_beta_search_search_entity, client_factory=cf_search_search_entity
    ) as g:
        g.custom_command('show-search-entity', 'search_search_entity_show_search_entity')
        g.custom_command('update-search-entity', 'search_search_entity_update_search_entity')

    from azext_search_beta.generated._client_factory import cf_search

    search_beta_search = CliCommandType(
        operations_tmpl='azext_search_beta.vendored_sdks.search.operations._search_operations#SearchOperations.{}',
        client_factory=cf_search,
    )
    with self.command_group('search search', search_beta_search, client_factory=cf_search) as g:
        g.custom_command('query', 'search_search_query')

    with self.command_group('search_beta', is_experimental=True):
        pass