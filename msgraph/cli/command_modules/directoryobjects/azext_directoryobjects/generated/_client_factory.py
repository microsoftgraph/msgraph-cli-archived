# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_directoryobjects_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_directoryobjects.vendored_sdks.directoryobjects import DirectoryObjects
    return get_mgmt_service_client(cli_ctx,
                                   DirectoryObjects,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_directory_object_directory_object(cli_ctx, *_):
    return cf_directoryobjects_cl(cli_ctx).directory_objects_directory_object


def cf_directory_object(cli_ctx, *_):
    return cf_directoryobjects_cl(cli_ctx).directory_objects
