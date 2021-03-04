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

    from azext_schemaextensions_beta.generated._client_factory import cf_schema_extension_schema_extension

    schemaextensions_beta_schema_extension_schema_extension = CliCommandType(
        operations_tmpl='azext_schemaextensions_beta.vendored_sdks.schemaextensions.operations._schema_extension_schema_extension_operations#SchemaExtensionSchemaExtensionOperations.{}',
        client_factory=cf_schema_extension_schema_extension,
    )
    with self.command_group(
        'schemaextensions schema-extension-schema-extension',
        schemaextensions_beta_schema_extension_schema_extension,
        client_factory=cf_schema_extension_schema_extension,
    ) as g:
        g.custom_command('delete', 'schemaextensions_schema_extension_schema_extension_delete', confirmation=True)
        g.custom_command(
            'create-schema-extension', 'schemaextensions_schema_extension_schema_extension_create_schema_extension'
        )
        g.custom_command(
            'list-schema-extension', 'schemaextensions_schema_extension_schema_extension_list_schema_extension'
        )
        g.custom_command(
            'show-schema-extension', 'schemaextensions_schema_extension_schema_extension_show_schema_extension'
        )
        g.custom_command(
            'update-schema-extension', 'schemaextensions_schema_extension_schema_extension_update_schema_extension'
        )

    with self.command_group('schemaextensions_beta', is_experimental=True):
        pass