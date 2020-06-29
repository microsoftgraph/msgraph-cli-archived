from azure.identity import InteractiveBrowserCredential
from knack.cli import logger
from knack.util import CLIError
# from msgraphcore import GraphSession


def resolve_client_arg_name(operation, kwargs):
    if not isinstance(operation, str):
        raise CLIError(
            "operation should be type 'str'. Got '{}'".format(type(operation)))
    if 'client_arg_name' in kwargs:
        logger.info(
            "Keyword 'client_arg_name' is deprecated and should be removed.")
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


def get_mgmt_service_client(cli_ctx,
                            client_type,
                            subscription_bound=True,
                            subscription_id=None,
                            api_version=None,
                            base_url_bound=True,
                            resource='https://graph.microsoft.com',
                            sdk_profile=None,
                            aux_subscriptions=None,
                            aux_tenants=None,
                            **kwargs):
    # browser_credential = InteractiveBrowserCredential(
    #     client_id='f7218512-c727-4138-9fb9-a0fe2500650c')
    # graph_session = GraphSession(browser_credential)
    client = client_type({})
    return client
