# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.cli import logger
from knack.util import CLIError

from msgraph.cli.core.authentication import Authentication
from msgraph.cli.core.profile import read_profile
from msgraph.core import GraphSession
from msgraph.cli.core.constants import DEFAULT_BASE_URL


def resolve_client_arg_name(operation, kwargs):
    if not isinstance(operation, str):
        raise CLIError("operation should be type 'str'. Got '{}'".format(type(operation)))
    if 'client_arg_name' in kwargs:
        logger.info("Keyword 'client_arg_name' is deprecated and should be removed.")
        return kwargs['client_arg_name']
    path, op_path = operation.split('#', 1)
    path_comps = path.split('.')
    if path_comps[0] == 'azure':
        # for CLI command modules
        # SDK method: azure.mgmt.foo... or azure.foo...
        # custom method: azure.cli.command_modules.foo...
        client_arg_name = 'client' if path_comps[1] == 'cli' else 'self'
    elif path_comps[0].startswith('azext_'):
        # for CLI extensions
        # SDK method: the operation takes the form '<class name>.<method_name>'
        # custom method: the operation takes the form '<method_name>'
        op_comps = op_path.split('.')
        client_arg_name = 'self' if len(op_comps) > 1 else 'client'
    else:
        raise ValueError('Unrecognized operation: {}'.format(operation))
    return client_arg_name


def get_mgmt_service_client(cli_ctx, client_type, **kwargs):

    auth = Authentication()
    record = auth.get_auth_record()
    credential = auth.get_credential(auth_record=record)
    graph_session = GraphSession(credential=credential)

    base_url = None
    cloud = read_profile().get('cloud', None)

    if cloud:
        base_url = cloud.get('graph_endpoint')
    else:
        base_url = DEFAULT_BASE_URL

    client = client_type({}, session=graph_session, base_url=base_url)
    return client
