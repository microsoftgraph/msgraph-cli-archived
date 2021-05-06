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
# pylint: disable=bad-continuation
# pylint: disable=line-too-long

from msgraph.cli.core.commands import CliCommandType
from azext_security_beta.generated._client_factory import (
    cf_security_security,
    cf_security,
    cf_security_alert,
    cf_security_security_action,
    cf_security_tiindicator,
)


security_beta_security_security = CliCommandType(
    operations_tmpl='azext_security_beta.vendored_sdks.security.operations._security_security_operations#SecuritySecurityOperations.{}',
    client_factory=cf_security_security,
)


security_beta_security = CliCommandType(
    operations_tmpl='azext_security_beta.vendored_sdks.security.operations._security_operations#SecurityOperations.{}',
    client_factory=cf_security,
)


security_beta_security_alert = CliCommandType(
    operations_tmpl=(
        'azext_security_beta.vendored_sdks.security.operations._security_alerts_operations#SecurityAlertsOperations.{}'
    ),
    client_factory=cf_security_alert,
)


security_beta_security_security_action = CliCommandType(
    operations_tmpl='azext_security_beta.vendored_sdks.security.operations._security_security_actions_operations#SecuritySecurityActionsOperations.{}',
    client_factory=cf_security_security_action,
)


security_beta_security_tiindicator = CliCommandType(
    operations_tmpl='azext_security_beta.vendored_sdks.security.operations._security_ti_indicators_operations#SecurityTiIndicatorsOperations.{}',
    client_factory=cf_security_tiindicator,
)


def load_command_table(self, _):

    with self.command_group(
        'security security', security_beta_security_security, client_factory=cf_security_security
    ) as g:
        g.custom_command('create', 'security_security_create')
        g.custom_command('create-action', 'security_security_create_action', client_factory=cf_security)
        g.custom_command('list-action', 'security_security_list_action', client_factory=cf_security)
        g.custom_command('show-security', 'security_security_show_security')

    with self.command_group('security security', security_beta_security, client_factory=cf_security) as g:
        g.custom_command('create-alert', 'security_security_create_alert')
        g.custom_command('create-cloud-app-security-profile', 'security_security_create_cloud_app_security_profile')
        g.custom_command('create-domain-security-profile', 'security_security_create_domain_security_profile')
        g.custom_command('create-file-security-profile', 'security_security_create_file_security_profile')
        g.custom_command('create-host-security-profile', 'security_security_create_host_security_profile')
        g.custom_command('create-ip-security-profile', 'security_security_create_ip_security_profile')
        g.custom_command('create-provider-tenant-setting', 'security_security_create_provider_tenant_setting')
        g.custom_command('create-secure-score', 'security_security_create_secure_score')
        g.custom_command('create-secure-score-control-profile', 'security_security_create_secure_score_control_profile')
        g.custom_command('create-ti-indicator', 'security_security_create_ti_indicator')
        g.custom_command('create-user-security-profile', 'security_security_create_user_security_profile')
        g.custom_command('delete-alert', 'security_security_delete_alert')
        g.custom_command('delete-cloud-app-security-profile', 'security_security_delete_cloud_app_security_profile')
        g.custom_command('delete-domain-security-profile', 'security_security_delete_domain_security_profile')
        g.custom_command('delete-file-security-profile', 'security_security_delete_file_security_profile')
        g.custom_command('delete-host-security-profile', 'security_security_delete_host_security_profile')
        g.custom_command('delete-ip-security-profile', 'security_security_delete_ip_security_profile')
        g.custom_command('delete-provider-tenant-setting', 'security_security_delete_provider_tenant_setting')
        g.custom_command('delete-secure-score', 'security_security_delete_secure_score')
        g.custom_command('delete-secure-score-control-profile', 'security_security_delete_secure_score_control_profile')
        g.custom_command('delete-security-action', 'security_security_delete_security_action')
        g.custom_command('delete-ti-indicator', 'security_security_delete_ti_indicator')
        g.custom_command('delete-user-security-profile', 'security_security_delete_user_security_profile')
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
        g.custom_command('show-alert', 'security_security_show_alert')
        g.custom_command('show-cloud-app-security-profile', 'security_security_show_cloud_app_security_profile')
        g.custom_command('show-domain-security-profile', 'security_security_show_domain_security_profile')
        g.custom_command('show-file-security-profile', 'security_security_show_file_security_profile')
        g.custom_command('show-host-security-profile', 'security_security_show_host_security_profile')
        g.custom_command('show-ip-security-profile', 'security_security_show_ip_security_profile')
        g.custom_command('show-provider-tenant-setting', 'security_security_show_provider_tenant_setting')
        g.custom_command('show-secure-score', 'security_security_show_secure_score')
        g.custom_command('show-secure-score-control-profile', 'security_security_show_secure_score_control_profile')
        g.custom_command('show-security-action', 'security_security_show_security_action')
        g.custom_command('show-ti-indicator', 'security_security_show_ti_indicator')
        g.custom_command('show-user-security-profile', 'security_security_show_user_security_profile')
        g.custom_command('update-alert', 'security_security_update_alert')
        g.custom_command('update-cloud-app-security-profile', 'security_security_update_cloud_app_security_profile')
        g.custom_command('update-domain-security-profile', 'security_security_update_domain_security_profile')
        g.custom_command('update-file-security-profile', 'security_security_update_file_security_profile')
        g.custom_command('update-host-security-profile', 'security_security_update_host_security_profile')
        g.custom_command('update-ip-security-profile', 'security_security_update_ip_security_profile')
        g.custom_command('update-provider-tenant-setting', 'security_security_update_provider_tenant_setting')
        g.custom_command('update-secure-score', 'security_security_update_secure_score')
        g.custom_command('update-secure-score-control-profile', 'security_security_update_secure_score_control_profile')
        g.custom_command('update-ti-indicator', 'security_security_update_ti_indicator')
        g.custom_command('update-user-security-profile', 'security_security_update_user_security_profile')

    with self.command_group(
        'security security-alert', security_beta_security_alert, client_factory=cf_security_alert
    ) as g:
        g.custom_command('update-alert', 'security_security_alert_update_alert')

    with self.command_group(
        'security security-action', security_beta_security_security_action, client_factory=cf_security_security_action
    ) as g:
        g.custom_command('cancel-security-action', 'security_security_action_cancel_security_action')

    with self.command_group(
        'security security-ti-indicator', security_beta_security_tiindicator, client_factory=cf_security_tiindicator
    ) as g:
        g.custom_command('delete-ti-indicator', 'security_security_ti_indicator_delete_ti_indicator')
        g.custom_command(
            'delete-ti-indicator-by-external-id', 'security_security_ti_indicator_delete_ti_indicator_by_external_id'
        )
        g.custom_command('submit-ti-indicator', 'security_security_ti_indicator_submit_ti_indicator')
        g.custom_command('update-ti-indicator', 'security_security_ti_indicator_update_ti_indicator')

    with self.command_group('security_beta', is_experimental=True):
        pass
