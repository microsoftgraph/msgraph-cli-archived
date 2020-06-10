from azure.identity import InteractiveBrowserCredential
from msgraphcore import GraphSession


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
    browser_credential = InteractiveBrowserCredential(client_id='f7218512-c727-4138-9fb9-a0fe2500650c')
    graph_session = GraphSession(browser_credential)
    client = client_type({}, session=graph_session)
    return client, ''