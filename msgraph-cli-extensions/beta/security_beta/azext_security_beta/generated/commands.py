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

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_security_beta.generated._client_factory import cf_security_security
    security_beta_security_security = CliCommandType(
        operations_tmpl='azext_security_beta.vendored_sdks.security.operations._security_security_operations#SecuritySe'
        'curityOperations.{}',
        client_factory=cf_security_security)
    with self.command_group('security security', security_beta_security_security, client_factory=cf_security_security,
                            is_experimental=True) as g:
        g.custom_command('update', 'security_security_update')
        g.custom_command('get', 'security_security_get')

    from azext_security_beta.generated._client_factory import cf_security
    security_beta_security = CliCommandType(
        operations_tmpl='azext_security_beta.vendored_sdks.security.operations._security_operations#SecurityOperations.'
        '{}',
        client_factory=cf_security)
    with self.command_group('security security', security_beta_security, client_factory=cf_security,
                            is_experimental=True) as g:
        g.custom_command('delete', 'security_security_delete', confirmation=True)
        g.custom_command('create-action', 'security_security_create_action')
        g.custom_command('create-alert', 'security_security_create_alert')
        g.custom_command('create-cloud-app-security-profile', 'security_security_create_cloud_app_security_profile')
        g.custom_command('create-domain-security-profile', 'security_security_create_domain_security_profile')
        g.custom_command('create-file-security-profile', 'security_security_create_file_security_profile')
        g.custom_command('create-host-security-profile', 'security_security_create_host_security_profile')
        g.custom_command('create-ip-security-profile', 'security_security_create_ip_security_profile')
        g.custom_command('create-provider-tenant-setting', 'security_security_create_provider_tenant_setting')
        g.custom_command('create-secure-score', 'security_security_create_secure_score')
        g.custom_command('create-secure-score-control-profile',
                         'security_security_create_secure_score_control_profile')
        g.custom_command('create-ti-indicator', 'security_security_create_ti_indicator')
        g.custom_command('create-user-security-profile', 'security_security_create_user_security_profile')
        g.custom_command('get-action', 'security_security_get_action')
        g.custom_command('get-alert', 'security_security_get_alert')
        g.custom_command('get-cloud-app-security-profile', 'security_security_get_cloud_app_security_profile')
        g.custom_command('get-domain-security-profile', 'security_security_get_domain_security_profile')
        g.custom_command('get-file-security-profile', 'security_security_get_file_security_profile')
        g.custom_command('get-host-security-profile', 'security_security_get_host_security_profile')
        g.custom_command('get-ip-security-profile', 'security_security_get_ip_security_profile')
        g.custom_command('get-provider-tenant-setting', 'security_security_get_provider_tenant_setting')
        g.custom_command('get-secure-score', 'security_security_get_secure_score')
        g.custom_command('get-secure-score-control-profile', 'security_security_get_secure_score_control_profile')
        g.custom_command('get-ti-indicator', 'security_security_get_ti_indicator')
        g.custom_command('get-user-security-profile', 'security_security_get_user_security_profile')
        g.custom_command('list-action', 'security_security_list_action')
        g.custom_command('list-alert', 'security_security_list_alert')
        g.custom_command('list-cloud-app-security-profile', 'security_security_list_cloud_app_security_profile')
        g.custom_command('list-domain-security-profile', 'security_security_list_domain_security_profile')
        g.custom_command('list-file-security-profile', 'security_security_list_file_security_profile')
        g.custom_command('list-host-security-profile', 'security_security_list_host_security_profile')
        g.custom_command('list-ip-security-profile', 'security_security_list_ip_security_profile')
        g.custom_command('list-provider-tenant-setting', 'security_security_list_provider_tenant_setting')
        g.custom_command('list-secure-score', 'security_security_list_secure_score')
        g.custom_command('list-secure-score-control-profile', 'security_security_list_secure_score_control_profile')
        g.custom_command('list-ti-indicator', 'security_security_list_ti_indicator')
        g.custom_command('list-user-security-profile', 'security_security_list_user_security_profile')
        g.custom_command('update-action', 'security_security_update_action')
        g.custom_command('update-alert', 'security_security_update_alert')
        g.custom_command('update-cloud-app-security-profile', 'security_security_update_cloud_app_security_profile')
        g.custom_command('update-domain-security-profile', 'security_security_update_domain_security_profile')
        g.custom_command('update-file-security-profile', 'security_security_update_file_security_profile')
        g.custom_command('update-host-security-profile', 'security_security_update_host_security_profile')
        g.custom_command('update-ip-security-profile', 'security_security_update_ip_security_profile')
        g.custom_command('update-provider-tenant-setting', 'security_security_update_provider_tenant_setting')
        g.custom_command('update-secure-score', 'security_security_update_secure_score')
        g.custom_command('update-secure-score-control-profile',
                         'security_security_update_secure_score_control_profile')
        g.custom_command('update-ti-indicator', 'security_security_update_ti_indicator')
        g.custom_command('update-user-security-profile', 'security_security_update_user_security_profile')

    from azext_security_beta.generated._client_factory import cf_security_alert
    security_beta_security_alert = CliCommandType(
        operations_tmpl='azext_security_beta.vendored_sdks.security.operations._security_alert_operations#SecurityAlert'
        'Operations.{}',
        client_factory=cf_security_alert)
    with self.command_group('security security-alert', security_beta_security_alert, client_factory=cf_security_alert,
                            is_experimental=True) as g:
        g.custom_command('update-alert', 'security_security_alert_update_alert')

    from azext_security_beta.generated._client_factory import cf_security_security_action
    security_beta_security_security_action = CliCommandType(
        operations_tmpl='azext_security_beta.vendored_sdks.security.operations._security_security_action_operations#Sec'
        'uritySecurityActionOperations.{}',
        client_factory=cf_security_security_action)
    with self.command_group('security security-action', security_beta_security_security_action,
                            client_factory=cf_security_security_action, is_experimental=True) as g:
        g.custom_command('cancel-security-action', 'security_security_action_cancel_security_action')

    from azext_security_beta.generated._client_factory import cf_security_tiindicator
    security_beta_security_tiindicator = CliCommandType(
        operations_tmpl='azext_security_beta.vendored_sdks.security.operations._security_ti_indicator_operations#Securi'
        'tyTIIndicatorOperations.{}',
        client_factory=cf_security_tiindicator)
    with self.command_group('security security-ti-indicator', security_beta_security_tiindicator,
                            client_factory=cf_security_tiindicator, is_experimental=True) as g:
        g.custom_command('delete-ti-indicator', 'security_security_ti_indicator_delete_ti_indicator')
        g.custom_command('delete-ti-indicator-by-external-id', 'security_security_ti_indicator_delete_ti_indicator_by_e'
                         'xternal_id')
        g.custom_command('submit-ti-indicator', 'security_security_ti_indicator_submit_ti_indicator')
        g.custom_command('update-ti-indicator', 'security_security_ti_indicator_update_ti_indicator')