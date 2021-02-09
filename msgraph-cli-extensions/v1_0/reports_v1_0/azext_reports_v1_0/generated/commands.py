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

    from azext_reports_v1_0.generated._client_factory import cf_audit_log_audit_log_root
    reports_v1_0_audit_log_audit_log_root = CliCommandType(
        operations_tmpl='azext_reports_v1_0.vendored_sdks.reports.operations._audit_log_audit_log_root_operations#Audit'
        'LogAuditLogRootOperations.{}',
        client_factory=cf_audit_log_audit_log_root)
    with self.command_group('reports audit-log-audit-log-root', reports_v1_0_audit_log_audit_log_root,
                            client_factory=cf_audit_log_audit_log_root, is_experimental=True) as g:
        g.custom_command('get-audit-log-root', 'reports_audit_log_audit_log_root_get_audit_log_root')
        g.custom_command('update-audit-log-root', 'reports_audit_log_audit_log_root_update_audit_log_root')

    from azext_reports_v1_0.generated._client_factory import cf_audit_log
    reports_v1_0_audit_log = CliCommandType(
        operations_tmpl='azext_reports_v1_0.vendored_sdks.reports.operations._audit_log_operations#AuditLogOperations.{'
        '}',
        client_factory=cf_audit_log)
    with self.command_group('reports audit-log', reports_v1_0_audit_log, client_factory=cf_audit_log,
                            is_experimental=True) as g:
        g.custom_command('delete', 'reports_audit_log_delete', confirmation=True)
        g.custom_command('create-directory-audit', 'reports_audit_log_create_directory_audit')
        g.custom_command('create-restricted-sign-in', 'reports_audit_log_create_restricted_sign_in')
        g.custom_command('create-sign-in', 'reports_audit_log_create_sign_in')
        g.custom_command('get-directory-audit', 'reports_audit_log_get_directory_audit')
        g.custom_command('get-restricted-sign-in', 'reports_audit_log_get_restricted_sign_in')
        g.custom_command('get-sign-in', 'reports_audit_log_get_sign_in')
        g.custom_command('list-directory-audit', 'reports_audit_log_list_directory_audit')
        g.custom_command('list-restricted-sign-in', 'reports_audit_log_list_restricted_sign_in')
        g.custom_command('list-sign-in', 'reports_audit_log_list_sign_in')
        g.custom_command('update-directory-audit', 'reports_audit_log_update_directory_audit')
        g.custom_command('update-restricted-sign-in', 'reports_audit_log_update_restricted_sign_in')
        g.custom_command('update-sign-in', 'reports_audit_log_update_sign_in')

    from azext_reports_v1_0.generated._client_factory import cf_report_report_root
    reports_v1_0_report_report_root = CliCommandType(
        operations_tmpl='azext_reports_v1_0.vendored_sdks.reports.operations._report_report_root_operations#ReportRepor'
        'tRootOperations.{}',
        client_factory=cf_report_report_root)
    with self.command_group('reports report-root', reports_v1_0_report_report_root,
                            client_factory=cf_report_report_root, is_experimental=True) as g:
        g.custom_command('get-root', 'reports_report_root_get_root')
        g.custom_command('update-root', 'reports_report_root_update_root')

    from azext_reports_v1_0.generated._client_factory import cf_report
    reports_v1_0_report = CliCommandType(
        operations_tmpl='azext_reports_v1_0.vendored_sdks.reports.operations._report_operations#ReportOperations.{}',
        client_factory=cf_report)
    with self.command_group('reports report', reports_v1_0_report, client_factory=cf_report,
                            is_experimental=True) as g:
        g.custom_command('device-configuration-device-activity',
                         'reports_report_device_configuration_device_activity')
        g.custom_command('device-configuration-user-activity', 'reports_report_device_configuration_user_activity')
        g.custom_command('get-email-activity-count', 'reports_report_get_email_activity_count')
        g.custom_command('get-email-activity-user-count', 'reports_report_get_email_activity_user_count')
        g.custom_command('get-email-activity-user-detail-ddb2', 'reports_report_get_email_activity_user_detail_ddb2')
        g.custom_command('get-email-activity-user-detail-fe32', 'reports_report_get_email_activity_user_detail_fe32')
        g.custom_command('get-email-app-usage-app-user-count', 'reports_report_get_email_app_usage_app_user_count')
        g.custom_command('get-email-app-usage-user-count', 'reports_report_get_email_app_usage_user_count')
        g.custom_command('get-email-app-usage-user-detail546-b',
                         'reports_report_get_email_app_usage_user_detail546_b')
        g.custom_command('get-email-app-usage-user-detail62-ec',
                         'reports_report_get_email_app_usage_user_detail62_ec')
        g.custom_command('get-email-app-usage-version-user-count', 'reports_report_get_email_app_usage_version_user_cou'
                         'nt')
        g.custom_command('get-mailbox-usage-detail', 'reports_report_get_mailbox_usage_detail')
        g.custom_command('get-mailbox-usage-mailbox-count', 'reports_report_get_mailbox_usage_mailbox_count')
        g.custom_command('get-mailbox-usage-quota-status-mailbox-count', 'reports_report_get_mailbox_usage_quota_status'
                         '_mailbox_count')
        g.custom_command('get-mailbox-usage-storage', 'reports_report_get_mailbox_usage_storage')
        g.custom_command('get-office365-activation-count', 'reports_report_get_office365_activation_count')
        g.custom_command('get-office365-activation-user-count', 'reports_report_get_office365_activation_user_count')
        g.custom_command('get-office365-activation-user-detail',
                         'reports_report_get_office365_activation_user_detail')
        g.custom_command('get-office365-active-user-count', 'reports_report_get_office365_active_user_count')
        g.custom_command('get-office365-active-user-detail-d389', 'reports_report_get_office365_active_user_detail_d389'
                         '')
        g.custom_command('get-office365-active-user-detail68-ad', 'reports_report_get_office365_active_user_detail68_ad'
                         '')
        g.custom_command('get-office365-group-activity-count', 'reports_report_get_office365_group_activity_count')
        g.custom_command('get-office365-group-activity-detail38-f6', 'reports_report_get_office365_group_activity_detai'
                         'l38_f6')
        g.custom_command('get-office365-group-activity-detail81-cc', 'reports_report_get_office365_group_activity_detai'
                         'l81_cc')
        g.custom_command('get-office365-group-activity-file-count', 'reports_report_get_office365_group_activity_file_c'
                         'ount')
        g.custom_command('get-office365-group-activity-group-count', 'reports_report_get_office365_group_activity_group'
                         '_count')
        g.custom_command('get-office365-group-activity-storage',
                         'reports_report_get_office365_group_activity_storage')
        g.custom_command('get-office365-service-user-count', 'reports_report_get_office365_service_user_count')
        g.custom_command('get-one-drive-activity-file-count', 'reports_report_get_one_drive_activity_file_count')
        g.custom_command('get-one-drive-activity-user-count', 'reports_report_get_one_drive_activity_user_count')
        g.custom_command('get-one-drive-activity-user-detail-c424', 'reports_report_get_one_drive_activity_user_detail_'
                         'c424')
        g.custom_command('get-one-drive-activity-user-detail05-f1', 'reports_report_get_one_drive_activity_user_detail0'
                         '5_f1')
        g.custom_command('get-one-drive-usage-account-count', 'reports_report_get_one_drive_usage_account_count')
        g.custom_command('get-one-drive-usage-account-detail-dd7-f', 'reports_report_get_one_drive_usage_account_detail'
                         '_dd7_f')
        g.custom_command('get-one-drive-usage-account-detail-e827', 'reports_report_get_one_drive_usage_account_detail_'
                         'e827')
        g.custom_command('get-one-drive-usage-file-count', 'reports_report_get_one_drive_usage_file_count')
        g.custom_command('get-one-drive-usage-storage', 'reports_report_get_one_drive_usage_storage')
        g.custom_command('get-share-point-activity-file-count', 'reports_report_get_share_point_activity_file_count')
        g.custom_command('get-share-point-activity-page', 'reports_report_get_share_point_activity_page')
        g.custom_command('get-share-point-activity-user-count', 'reports_report_get_share_point_activity_user_count')
        g.custom_command('get-share-point-activity-user-detail-b778', 'reports_report_get_share_point_activity_user_det'
                         'ail_b778')
        g.custom_command('get-share-point-activity-user-detail-f3-be', 'reports_report_get_share_point_activity_user_de'
                         'tail_f3_be')
        g.custom_command('get-share-point-site-usage-detail-d27-a', 'reports_report_get_share_point_site_usage_detail_d'
                         '27_a')
        g.custom_command('get-share-point-site-usage-detail204-b', 'reports_report_get_share_point_site_usage_detail204'
                         '_b')
        g.custom_command('get-share-point-site-usage-file-count', 'reports_report_get_share_point_site_usage_file_count'
                         '')
        g.custom_command('get-share-point-site-usage-page', 'reports_report_get_share_point_site_usage_page')
        g.custom_command('get-share-point-site-usage-site-count', 'reports_report_get_share_point_site_usage_site_count'
                         '')
        g.custom_command('get-share-point-site-usage-storage', 'reports_report_get_share_point_site_usage_storage')
        g.custom_command('get-skype-for-business-activity-count', 'reports_report_get_skype_for_business_activity_count'
                         '')
        g.custom_command('get-skype-for-business-activity-user-count', 'reports_report_get_skype_for_business_activity_'
                         'user_count')
        g.custom_command('get-skype-for-business-activity-user-detail-e4-c9', 'reports_report_get_skype_for_business_ac'
                         'tivity_user_detail_e4_c9')
        g.custom_command('get-skype-for-business-activity-user-detail744-e', 'reports_report_get_skype_for_business_act'
                         'ivity_user_detail744_e')
        g.custom_command('get-skype-for-business-device-usage-distribution-user-count', ''
                         'reports_report_get_skype_for_business_device_usage_distribution_user_count')
        g.custom_command('get-skype-for-business-device-usage-user-count', 'reports_report_get_skype_for_business_devic'
                         'e_usage_user_count')
        g.custom_command('get-skype-for-business-device-usage-user-detail-a692', 'reports_report_get_skype_for_business'
                         '_device_usage_user_detail_a692')
        g.custom_command('get-skype-for-business-device-usage-user-detail-e753', 'reports_report_get_skype_for_business'
                         '_device_usage_user_detail_e753')
        g.custom_command('get-skype-for-business-organizer-activity-count', 'reports_report_get_skype_for_business_orga'
                         'nizer_activity_count')
        g.custom_command('get-skype-for-business-organizer-activity-minute-count', 'reports_report_get_skype_for_busine'
                         'ss_organizer_activity_minute_count')
        g.custom_command('get-skype-for-business-organizer-activity-user-count', 'reports_report_get_skype_for_business'
                         '_organizer_activity_user_count')
        g.custom_command('get-skype-for-business-participant-activity-count', 'reports_report_get_skype_for_business_pa'
                         'rticipant_activity_count')
        g.custom_command('get-skype-for-business-participant-activity-minute-count', 'reports_report_get_skype_for_busi'
                         'ness_participant_activity_minute_count')
        g.custom_command('get-skype-for-business-participant-activity-user-count', 'reports_report_get_skype_for_busine'
                         'ss_participant_activity_user_count')
        g.custom_command('get-skype-for-business-peer-to-peer-activity-count', 'reports_report_get_skype_for_business_p'
                         'eer_to_peer_activity_count')
        g.custom_command('get-skype-for-business-peer-to-peer-activity-minute-count', 'reports_report_get_skype_for_bus'
                         'iness_peer_to_peer_activity_minute_count')
        g.custom_command('get-skype-for-business-peer-to-peer-activity-user-count', 'reports_report_get_skype_for_busin'
                         'ess_peer_to_peer_activity_user_count')
        g.custom_command('get-team-device-usage-distribution-user-count', 'reports_report_get_team_device_usage_distrib'
                         'ution_user_count')
        g.custom_command('get-team-device-usage-user-count', 'reports_report_get_team_device_usage_user_count')
        g.custom_command('get-team-device-usage-user-detail7148', 'reports_report_get_team_device_usage_user_detail7148'
                         '')
        g.custom_command('get-team-device-usage-user-detail7565', 'reports_report_get_team_device_usage_user_detail7565'
                         '')
        g.custom_command('get-team-user-activity-count', 'reports_report_get_team_user_activity_count')
        g.custom_command('get-team-user-activity-user-count', 'reports_report_get_team_user_activity_user_count')
        g.custom_command('get-team-user-activity-user-detail-a3-f1', 'reports_report_get_team_user_activity_user_detail'
                         '_a3_f1')
        g.custom_command('get-team-user-activity-user-detail-eb13', 'reports_report_get_team_user_activity_user_detail_'
                         'eb13')
        g.custom_command('get-yammer-activity-count', 'reports_report_get_yammer_activity_count')
        g.custom_command('get-yammer-activity-user-count', 'reports_report_get_yammer_activity_user_count')
        g.custom_command('get-yammer-activity-user-detail-ac30',
                         'reports_report_get_yammer_activity_user_detail_ac30')
        g.custom_command('get-yammer-activity-user-detail15-a5',
                         'reports_report_get_yammer_activity_user_detail15_a5')
        g.custom_command('get-yammer-device-usage-distribution-user-count', 'reports_report_get_yammer_device_usage_dis'
                         'tribution_user_count')
        g.custom_command('get-yammer-device-usage-user-count', 'reports_report_get_yammer_device_usage_user_count')
        g.custom_command('get-yammer-device-usage-user-detail-cfad', 'reports_report_get_yammer_device_usage_user_detai'
                         'l_cfad')
        g.custom_command('get-yammer-device-usage-user-detail-d0-ac', 'reports_report_get_yammer_device_usage_user_deta'
                         'il_d0_ac')
        g.custom_command('get-yammer-group-activity-count', 'reports_report_get_yammer_group_activity_count')
        g.custom_command('get-yammer-group-activity-detail-da9-a', 'reports_report_get_yammer_group_activity_detail_da9'
                         '_a')
        g.custom_command('get-yammer-group-activity-detail0-d7-d', 'reports_report_get_yammer_group_activity_detail0_d7'
                         '_d')
        g.custom_command('get-yammer-group-activity-group-count', 'reports_report_get_yammer_group_activity_group_count'
                         '')
        g.custom_command('managed-device-enrollment-failure-details027-e', 'reports_report_managed_device_enrollment_fa'
                         'ilure_details027_e')
        g.custom_command('managed-device-enrollment-failure-details2-b3-d', 'reports_report_managed_device_enrollment_f'
                         'ailure_details2_b3_d')
        g.custom_command('managed-device-enrollment-top-failure-afd1', 'reports_report_managed_device_enrollment_top_fa'
                         'ilure_afd1')
        g.custom_command('managed-device-enrollment-top-failures4669', 'reports_report_managed_device_enrollment_top_fa'
                         'ilures4669')