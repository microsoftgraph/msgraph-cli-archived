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


def schemaextensions_schema_extension_schema_extension_create_schema_extension(client,
                                                                               id_=None,
                                                                               description=None,
                                                                               owner=None,
                                                                               properties=None,
                                                                               status=None,
                                                                               target_types=None):
    body = {}
    body['id'] = id_
    body['description'] = description
    body['owner'] = owner
    body['properties'] = properties
    body['status'] = status
    body['target_types'] = target_types
    return client.create_schema_extension(body=body)


def schemaextensions_schema_extension_schema_extension_delete_schema_extension(client,
                                                                               schema_extension_id,
                                                                               if_match=None):
    return client.delete_schema_extension(schema_extension_id=schema_extension_id,
                                          if_match=if_match)


def schemaextensions_schema_extension_schema_extension_list_schema_extension(client,
                                                                             orderby=None,
                                                                             select=None,
                                                                             expand=None):
    return client.list_schema_extension(orderby=orderby,
                                        select=select,
                                        expand=expand)


def schemaextensions_schema_extension_schema_extension_show_schema_extension(client,
                                                                             schema_extension_id,
                                                                             select=None,
                                                                             expand=None):
    return client.get_schema_extension(schema_extension_id=schema_extension_id,
                                       select=select,
                                       expand=expand)


def schemaextensions_schema_extension_schema_extension_update_schema_extension(client,
                                                                               schema_extension_id,
                                                                               id_=None,
                                                                               description=None,
                                                                               owner=None,
                                                                               properties=None,
                                                                               status=None,
                                                                               target_types=None):
    body = {}
    body['id'] = id_
    body['description'] = description
    body['owner'] = owner
    body['properties'] = properties
    body['status'] = status
    body['target_types'] = target_types
    return client.update_schema_extension(schema_extension_id=schema_extension_id,
                                          body=body)