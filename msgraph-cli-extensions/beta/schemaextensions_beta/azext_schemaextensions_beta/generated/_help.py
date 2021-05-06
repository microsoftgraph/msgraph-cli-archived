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


helps['schemaextensions_beta'] = '''
    type: group
    short-summary: Manage Schema Extensions
'''

helps['schemaextensions schema-extension-schema-extension'] = """
    type: group
    short-summary: Manage schema extension schema extension with schemaextensions_beta
"""

helps['schemaextensions schema-extension-schema-extension create-schema-extension'] = """
    type: command
    short-summary: "Add new entity to schemaExtensions."
    parameters:
      - name: --properties
        short-summary: "The collection of property names and types that make up the schema extension definition."
        long-summary: |
            Usage: --properties name=XX type=XX

            name: The name of the strongly-typed property defined as part of a schema extension.
            type: The type of the property that is defined as part of a schema extension.  Allowed values are Binary, \
Boolean, DateTime, Integer or String.  See the table below for more details.

            Multiple actions can be specified by using more than one --properties argument.
"""

helps['schemaextensions schema-extension-schema-extension delete-schema-extension'] = """
    type: command
    short-summary: "Delete entity from schemaExtensions."
"""

helps['schemaextensions schema-extension-schema-extension list-schema-extension'] = """
    type: command
    short-summary: "Get entities from schemaExtensions."
"""

helps['schemaextensions schema-extension-schema-extension show-schema-extension'] = """
    type: command
    short-summary: "Get entity from schemaExtensions by key."
"""

helps['schemaextensions schema-extension-schema-extension update-schema-extension'] = """
    type: command
    short-summary: "Update entity in schemaExtensions."
    parameters:
      - name: --properties
        short-summary: "The collection of property names and types that make up the schema extension definition."
        long-summary: |
            Usage: --properties name=XX type=XX

            name: The name of the strongly-typed property defined as part of a schema extension.
            type: The type of the property that is defined as part of a schema extension.  Allowed values are Binary, \
Boolean, DateTime, Integer or String.  See the table below for more details.

            Multiple actions can be specified by using more than one --properties argument.
"""
