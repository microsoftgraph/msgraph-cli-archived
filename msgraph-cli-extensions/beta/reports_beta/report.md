# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az reports_beta|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az reports_beta` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az reports audit-log-audit-log-root|auditLogs.auditLogRoot|[commands](#CommandsInauditLogs.auditLogRoot)|
|az reports audit-log|auditLogs|[commands](#CommandsInauditLogs)|
|az reports report-report-root|reports.reportRoot|[commands](#CommandsInreports.reportRoot)|
|az reports report|reports|[commands](#CommandsInreports)|

## COMMANDS
### <a name="CommandsInauditLogs">Commands in `az reports audit-log` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az reports audit-log delete](#auditLogsDeleteDirectoryAudits)|DeleteDirectoryAudits|[Parameters](#ParametersauditLogsDeleteDirectoryAudits)|Not Found|
|[az reports audit-log delete](#auditLogsDeleteDirectoryProvisioning)|DeleteDirectoryProvisioning|[Parameters](#ParametersauditLogsDeleteDirectoryProvisioning)|Not Found|
|[az reports audit-log delete](#auditLogsDeleteProvisioning)|DeleteProvisioning|[Parameters](#ParametersauditLogsDeleteProvisioning)|Not Found|
|[az reports audit-log delete](#auditLogsDeleteRestrictedSignIns)|DeleteRestrictedSignIns|[Parameters](#ParametersauditLogsDeleteRestrictedSignIns)|Not Found|
|[az reports audit-log delete](#auditLogsDeleteSignIns)|DeleteSignIns|[Parameters](#ParametersauditLogsDeleteSignIns)|Not Found|
|[az reports audit-log create-directory-audit](#auditLogsCreateDirectoryAudits)|CreateDirectoryAudits|[Parameters](#ParametersauditLogsCreateDirectoryAudits)|Not Found|
|[az reports audit-log create-directory-provisioning](#auditLogsCreateDirectoryProvisioning)|CreateDirectoryProvisioning|[Parameters](#ParametersauditLogsCreateDirectoryProvisioning)|Not Found|
|[az reports audit-log create-provisioning](#auditLogsCreateProvisioning)|CreateProvisioning|[Parameters](#ParametersauditLogsCreateProvisioning)|Not Found|
|[az reports audit-log create-restricted-sign-in](#auditLogsCreateRestrictedSignIns)|CreateRestrictedSignIns|[Parameters](#ParametersauditLogsCreateRestrictedSignIns)|Not Found|
|[az reports audit-log create-sign-in](#auditLogsCreateSignIns)|CreateSignIns|[Parameters](#ParametersauditLogsCreateSignIns)|Not Found|
|[az reports audit-log list-directory-audit](#auditLogsListDirectoryAudits)|ListDirectoryAudits|[Parameters](#ParametersauditLogsListDirectoryAudits)|Not Found|
|[az reports audit-log list-directory-provisioning](#auditLogsListDirectoryProvisioning)|ListDirectoryProvisioning|[Parameters](#ParametersauditLogsListDirectoryProvisioning)|Not Found|
|[az reports audit-log list-provisioning](#auditLogsListProvisioning)|ListProvisioning|[Parameters](#ParametersauditLogsListProvisioning)|Not Found|
|[az reports audit-log list-restricted-sign-in](#auditLogsListRestrictedSignIns)|ListRestrictedSignIns|[Parameters](#ParametersauditLogsListRestrictedSignIns)|Not Found|
|[az reports audit-log list-sign-in](#auditLogsListSignIns)|ListSignIns|[Parameters](#ParametersauditLogsListSignIns)|Not Found|
|[az reports audit-log show-directory-audit](#auditLogsGetDirectoryAudits)|GetDirectoryAudits|[Parameters](#ParametersauditLogsGetDirectoryAudits)|Not Found|
|[az reports audit-log show-directory-provisioning](#auditLogsGetDirectoryProvisioning)|GetDirectoryProvisioning|[Parameters](#ParametersauditLogsGetDirectoryProvisioning)|Not Found|
|[az reports audit-log show-provisioning](#auditLogsGetProvisioning)|GetProvisioning|[Parameters](#ParametersauditLogsGetProvisioning)|Not Found|
|[az reports audit-log show-restricted-sign-in](#auditLogsGetRestrictedSignIns)|GetRestrictedSignIns|[Parameters](#ParametersauditLogsGetRestrictedSignIns)|Not Found|
|[az reports audit-log show-sign-in](#auditLogsGetSignIns)|GetSignIns|[Parameters](#ParametersauditLogsGetSignIns)|Not Found|
|[az reports audit-log update-directory-audit](#auditLogsUpdateDirectoryAudits)|UpdateDirectoryAudits|[Parameters](#ParametersauditLogsUpdateDirectoryAudits)|Not Found|
|[az reports audit-log update-directory-provisioning](#auditLogsUpdateDirectoryProvisioning)|UpdateDirectoryProvisioning|[Parameters](#ParametersauditLogsUpdateDirectoryProvisioning)|Not Found|
|[az reports audit-log update-provisioning](#auditLogsUpdateProvisioning)|UpdateProvisioning|[Parameters](#ParametersauditLogsUpdateProvisioning)|Not Found|
|[az reports audit-log update-restricted-sign-in](#auditLogsUpdateRestrictedSignIns)|UpdateRestrictedSignIns|[Parameters](#ParametersauditLogsUpdateRestrictedSignIns)|Not Found|
|[az reports audit-log update-sign-in](#auditLogsUpdateSignIns)|UpdateSignIns|[Parameters](#ParametersauditLogsUpdateSignIns)|Not Found|

### <a name="CommandsInauditLogs.auditLogRoot">Commands in `az reports audit-log-audit-log-root` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az reports audit-log-audit-log-root show-audit-log-root](#auditLogs.auditLogRootGetAuditLogRoot)|GetAuditLogRoot|[Parameters](#ParametersauditLogs.auditLogRootGetAuditLogRoot)|Not Found|
|[az reports audit-log-audit-log-root update-audit-log-root](#auditLogs.auditLogRootUpdateAuditLogRoot)|UpdateAuditLogRoot|[Parameters](#ParametersauditLogs.auditLogRootUpdateAuditLogRoot)|Not Found|

### <a name="CommandsInreports">Commands in `az reports report` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az reports report delete](#reportsDeleteApplicationSignInDetailedSummary)|DeleteApplicationSignInDetailedSummary|[Parameters](#ParametersreportsDeleteApplicationSignInDetailedSummary)|Not Found|
|[az reports report delete](#reportsDeleteCredentialUserRegistrationDetails)|DeleteCredentialUserRegistrationDetails|[Parameters](#ParametersreportsDeleteCredentialUserRegistrationDetails)|Not Found|
|[az reports report delete](#reportsDeleteDailyPrintUsageSummariesByPrinter)|DeleteDailyPrintUsageSummariesByPrinter|[Parameters](#ParametersreportsDeleteDailyPrintUsageSummariesByPrinter)|Not Found|
|[az reports report delete](#reportsDeleteDailyPrintUsageSummariesByUser)|DeleteDailyPrintUsageSummariesByUser|[Parameters](#ParametersreportsDeleteDailyPrintUsageSummariesByUser)|Not Found|
|[az reports report delete](#reportsDeleteMonthlyPrintUsageSummariesByPrinter)|DeleteMonthlyPrintUsageSummariesByPrinter|[Parameters](#ParametersreportsDeleteMonthlyPrintUsageSummariesByPrinter)|Not Found|
|[az reports report delete](#reportsDeleteMonthlyPrintUsageSummariesByUser)|DeleteMonthlyPrintUsageSummariesByUser|[Parameters](#ParametersreportsDeleteMonthlyPrintUsageSummariesByUser)|Not Found|
|[az reports report delete](#reportsDeleteUserCredentialUsageDetails)|DeleteUserCredentialUsageDetails|[Parameters](#ParametersreportsDeleteUserCredentialUsageDetails)|Not Found|
|[az reports report create-application-sign-in-detailed-summary](#reportsCreateApplicationSignInDetailedSummary)|CreateApplicationSignInDetailedSummary|[Parameters](#ParametersreportsCreateApplicationSignInDetailedSummary)|Not Found|
|[az reports report create-credential-user-registration-detail](#reportsCreateCredentialUserRegistrationDetails)|CreateCredentialUserRegistrationDetails|[Parameters](#ParametersreportsCreateCredentialUserRegistrationDetails)|Not Found|
|[az reports report create-daily-print-usage-summary-by-printer](#reportsCreateDailyPrintUsageSummariesByPrinter)|CreateDailyPrintUsageSummariesByPrinter|[Parameters](#ParametersreportsCreateDailyPrintUsageSummariesByPrinter)|Not Found|
|[az reports report create-daily-print-usage-summary-by-user](#reportsCreateDailyPrintUsageSummariesByUser)|CreateDailyPrintUsageSummariesByUser|[Parameters](#ParametersreportsCreateDailyPrintUsageSummariesByUser)|Not Found|
|[az reports report create-monthly-print-usage-summary-by-printer](#reportsCreateMonthlyPrintUsageSummariesByPrinter)|CreateMonthlyPrintUsageSummariesByPrinter|[Parameters](#ParametersreportsCreateMonthlyPrintUsageSummariesByPrinter)|Not Found|
|[az reports report create-monthly-print-usage-summary-by-user](#reportsCreateMonthlyPrintUsageSummariesByUser)|CreateMonthlyPrintUsageSummariesByUser|[Parameters](#ParametersreportsCreateMonthlyPrintUsageSummariesByUser)|Not Found|
|[az reports report create-user-credential-usage-detail](#reportsCreateUserCredentialUsageDetails)|CreateUserCredentialUsageDetails|[Parameters](#ParametersreportsCreateUserCredentialUsageDetails)|Not Found|
|[az reports report device-configuration-device-activity](#reportsdeviceConfigurationDeviceActivity)|deviceConfigurationDeviceActivity|[Parameters](#ParametersreportsdeviceConfigurationDeviceActivity)|Not Found|
|[az reports report device-configuration-user-activity](#reportsdeviceConfigurationUserActivity)|deviceConfigurationUserActivity|[Parameters](#ParametersreportsdeviceConfigurationUserActivity)|Not Found|
|[az reports report list-application-sign-in-detailed-summary](#reportsListApplicationSignInDetailedSummary)|ListApplicationSignInDetailedSummary|[Parameters](#ParametersreportsListApplicationSignInDetailedSummary)|Not Found|
|[az reports report list-credential-user-registration-detail](#reportsListCredentialUserRegistrationDetails)|ListCredentialUserRegistrationDetails|[Parameters](#ParametersreportsListCredentialUserRegistrationDetails)|Not Found|
|[az reports report list-daily-print-usage-summary](#reportsListDailyPrintUsageSummariesByPrinter)|ListDailyPrintUsageSummariesByPrinter|[Parameters](#ParametersreportsListDailyPrintUsageSummariesByPrinter)|Not Found|
|[az reports report list-daily-print-usage-summary](#reportsListDailyPrintUsageSummariesByUser)|ListDailyPrintUsageSummariesByUser|[Parameters](#ParametersreportsListDailyPrintUsageSummariesByUser)|Not Found|
|[az reports report list-monthly-print-usage-summary](#reportsListMonthlyPrintUsageSummariesByPrinter)|ListMonthlyPrintUsageSummariesByPrinter|[Parameters](#ParametersreportsListMonthlyPrintUsageSummariesByPrinter)|Not Found|
|[az reports report list-monthly-print-usage-summary](#reportsListMonthlyPrintUsageSummariesByUser)|ListMonthlyPrintUsageSummariesByUser|[Parameters](#ParametersreportsListMonthlyPrintUsageSummariesByUser)|Not Found|
|[az reports report list-user-credential-usage-detail](#reportsListUserCredentialUsageDetails)|ListUserCredentialUsageDetails|[Parameters](#ParametersreportsListUserCredentialUsageDetails)|Not Found|
|[az reports report managed-device-enrollment-abandonment-detail](#reportsmanagedDeviceEnrollmentAbandonmentDetails)|managedDeviceEnrollmentAbandonmentDetails|[Parameters](#ParametersreportsmanagedDeviceEnrollmentAbandonmentDetails)|Not Found|
|[az reports report managed-device-enrollment-abandonment-summary](#reportsmanagedDeviceEnrollmentAbandonmentSummary)|managedDeviceEnrollmentAbandonmentSummary|[Parameters](#ParametersreportsmanagedDeviceEnrollmentAbandonmentSummary)|Not Found|
|[az reports report managed-device-enrollment-failure-details027-e](#reportsmanagedDeviceEnrollmentFailureDetails-027e)|managedDeviceEnrollmentFailureDetails-027e|[Parameters](#ParametersreportsmanagedDeviceEnrollmentFailureDetails-027e)|Not Found|
|[az reports report managed-device-enrollment-failure-details2-b3-d](#reportsmanagedDeviceEnrollmentFailureDetails-2b3d)|managedDeviceEnrollmentFailureDetails-2b3d|[Parameters](#ParametersreportsmanagedDeviceEnrollmentFailureDetails-2b3d)|Not Found|
|[az reports report managed-device-enrollment-failure-trend](#reportsmanagedDeviceEnrollmentFailureTrends)|managedDeviceEnrollmentFailureTrends|[Parameters](#ParametersreportsmanagedDeviceEnrollmentFailureTrends)|Not Found|
|[az reports report managed-device-enrollment-top-failure-afd1](#reportsmanagedDeviceEnrollmentTopFailures-afd1)|managedDeviceEnrollmentTopFailures-afd1|[Parameters](#ParametersreportsmanagedDeviceEnrollmentTopFailures-afd1)|Not Found|
|[az reports report managed-device-enrollment-top-failures4669](#reportsmanagedDeviceEnrollmentTopFailures-4669)|managedDeviceEnrollmentTopFailures-4669|[Parameters](#ParametersreportsmanagedDeviceEnrollmentTopFailures-4669)|Not Found|
|[az reports report show-application-sign-in-detailed-summary](#reportsGetApplicationSignInDetailedSummary)|GetApplicationSignInDetailedSummary|[Parameters](#ParametersreportsGetApplicationSignInDetailedSummary)|Not Found|
|[az reports report show-azure-ad-application-sign-in-summary](#reportsgetAzureADApplicationSignInSummary)|getAzureADApplicationSignInSummary|[Parameters](#ParametersreportsgetAzureADApplicationSignInSummary)|Not Found|
|[az reports report show-azure-ad-feature-usage](#reportsgetAzureADFeatureUsage)|getAzureADFeatureUsage|[Parameters](#ParametersreportsgetAzureADFeatureUsage)|Not Found|
|[az reports report show-azure-ad-license-usage](#reportsgetAzureADLicenseUsage)|getAzureADLicenseUsage|[Parameters](#ParametersreportsgetAzureADLicenseUsage)|Not Found|
|[az reports report show-azure-ad-user-feature-usage](#reportsgetAzureADUserFeatureUsage)|getAzureADUserFeatureUsage|[Parameters](#ParametersreportsgetAzureADUserFeatureUsage)|Not Found|
|[az reports report show-credential-usage-summary](#reportsgetCredentialUsageSummary)|getCredentialUsageSummary|[Parameters](#ParametersreportsgetCredentialUsageSummary)|Not Found|
|[az reports report show-credential-user-registration-count](#reportsgetCredentialUserRegistrationCount)|getCredentialUserRegistrationCount|[Parameters](#ParametersreportsgetCredentialUserRegistrationCount)|Not Found|
|[az reports report show-credential-user-registration-detail](#reportsGetCredentialUserRegistrationDetails)|GetCredentialUserRegistrationDetails|[Parameters](#ParametersreportsGetCredentialUserRegistrationDetails)|Not Found|
|[az reports report show-daily-print-usage-summary](#reportsGetDailyPrintUsageSummariesByPrinter)|GetDailyPrintUsageSummariesByPrinter|[Parameters](#ParametersreportsGetDailyPrintUsageSummariesByPrinter)|Not Found|
|[az reports report show-daily-print-usage-summary](#reportsGetDailyPrintUsageSummariesByUser)|GetDailyPrintUsageSummariesByUser|[Parameters](#ParametersreportsGetDailyPrintUsageSummariesByUser)|Not Found|
|[az reports report show-email-activity-count](#reportsgetEmailActivityCounts)|getEmailActivityCounts|[Parameters](#ParametersreportsgetEmailActivityCounts)|Not Found|
|[az reports report show-email-activity-user-count](#reportsgetEmailActivityUserCounts)|getEmailActivityUserCounts|[Parameters](#ParametersreportsgetEmailActivityUserCounts)|Not Found|
|[az reports report show-email-activity-user-detail-ddb2](#reportsgetEmailActivityUserDetail-ddb2)|getEmailActivityUserDetail-ddb2|[Parameters](#ParametersreportsgetEmailActivityUserDetail-ddb2)|Not Found|
|[az reports report show-email-activity-user-detail-fe32](#reportsgetEmailActivityUserDetail-fe32)|getEmailActivityUserDetail-fe32|[Parameters](#ParametersreportsgetEmailActivityUserDetail-fe32)|Not Found|
|[az reports report show-email-app-usage-app-user-count](#reportsgetEmailAppUsageAppsUserCounts)|getEmailAppUsageAppsUserCounts|[Parameters](#ParametersreportsgetEmailAppUsageAppsUserCounts)|Not Found|
|[az reports report show-email-app-usage-user-count](#reportsgetEmailAppUsageUserCounts)|getEmailAppUsageUserCounts|[Parameters](#ParametersreportsgetEmailAppUsageUserCounts)|Not Found|
|[az reports report show-email-app-usage-user-detail546-b](#reportsgetEmailAppUsageUserDetail-546b)|getEmailAppUsageUserDetail-546b|[Parameters](#ParametersreportsgetEmailAppUsageUserDetail-546b)|Not Found|
|[az reports report show-email-app-usage-user-detail62-ec](#reportsgetEmailAppUsageUserDetail-62ec)|getEmailAppUsageUserDetail-62ec|[Parameters](#ParametersreportsgetEmailAppUsageUserDetail-62ec)|Not Found|
|[az reports report show-email-app-usage-version-user-count](#reportsgetEmailAppUsageVersionsUserCounts)|getEmailAppUsageVersionsUserCounts|[Parameters](#ParametersreportsgetEmailAppUsageVersionsUserCounts)|Not Found|
|[az reports report show-m365-app-platform-user-count](#reportsgetM365AppPlatformUserCounts)|getM365AppPlatformUserCounts|[Parameters](#ParametersreportsgetM365AppPlatformUserCounts)|Not Found|
|[az reports report show-m365-app-user-count](#reportsgetM365AppUserCounts)|getM365AppUserCounts|[Parameters](#ParametersreportsgetM365AppUserCounts)|Not Found|
|[az reports report show-m365-app-user-detail-c8-df](#reportsgetM365AppUserDetail-c8df)|getM365AppUserDetail-c8df|[Parameters](#ParametersreportsgetM365AppUserDetail-c8df)|Not Found|
|[az reports report show-m365-app-user-detail2-b20](#reportsgetM365AppUserDetail-2b20)|getM365AppUserDetail-2b20|[Parameters](#ParametersreportsgetM365AppUserDetail-2b20)|Not Found|
|[az reports report show-mailbox-usage-detail](#reportsgetMailboxUsageDetail)|getMailboxUsageDetail|[Parameters](#ParametersreportsgetMailboxUsageDetail)|Not Found|
|[az reports report show-mailbox-usage-mailbox-count](#reportsgetMailboxUsageMailboxCounts)|getMailboxUsageMailboxCounts|[Parameters](#ParametersreportsgetMailboxUsageMailboxCounts)|Not Found|
|[az reports report show-mailbox-usage-quota-status-mailbox-count](#reportsgetMailboxUsageQuotaStatusMailboxCounts)|getMailboxUsageQuotaStatusMailboxCounts|[Parameters](#ParametersreportsgetMailboxUsageQuotaStatusMailboxCounts)|Not Found|
|[az reports report show-mailbox-usage-storage](#reportsgetMailboxUsageStorage)|getMailboxUsageStorage|[Parameters](#ParametersreportsgetMailboxUsageStorage)|Not Found|
|[az reports report show-monthly-print-usage-summary](#reportsGetMonthlyPrintUsageSummariesByPrinter)|GetMonthlyPrintUsageSummariesByPrinter|[Parameters](#ParametersreportsGetMonthlyPrintUsageSummariesByPrinter)|Not Found|
|[az reports report show-monthly-print-usage-summary](#reportsGetMonthlyPrintUsageSummariesByUser)|GetMonthlyPrintUsageSummariesByUser|[Parameters](#ParametersreportsGetMonthlyPrintUsageSummariesByUser)|Not Found|
|[az reports report show-office365-activation-count](#reportsgetOffice365ActivationCounts)|getOffice365ActivationCounts|[Parameters](#ParametersreportsgetOffice365ActivationCounts)|Not Found|
|[az reports report show-office365-activation-user-count](#reportsgetOffice365ActivationsUserCounts)|getOffice365ActivationsUserCounts|[Parameters](#ParametersreportsgetOffice365ActivationsUserCounts)|Not Found|
|[az reports report show-office365-activation-user-detail](#reportsgetOffice365ActivationsUserDetail)|getOffice365ActivationsUserDetail|[Parameters](#ParametersreportsgetOffice365ActivationsUserDetail)|Not Found|
|[az reports report show-office365-active-user-count](#reportsgetOffice365ActiveUserCounts)|getOffice365ActiveUserCounts|[Parameters](#ParametersreportsgetOffice365ActiveUserCounts)|Not Found|
|[az reports report show-office365-active-user-detail-d389](#reportsgetOffice365ActiveUserDetail-d389)|getOffice365ActiveUserDetail-d389|[Parameters](#ParametersreportsgetOffice365ActiveUserDetail-d389)|Not Found|
|[az reports report show-office365-active-user-detail68-ad](#reportsgetOffice365ActiveUserDetail-68ad)|getOffice365ActiveUserDetail-68ad|[Parameters](#ParametersreportsgetOffice365ActiveUserDetail-68ad)|Not Found|
|[az reports report show-office365-group-activity-count](#reportsgetOffice365GroupsActivityCounts)|getOffice365GroupsActivityCounts|[Parameters](#ParametersreportsgetOffice365GroupsActivityCounts)|Not Found|
|[az reports report show-office365-group-activity-detail38-f6](#reportsgetOffice365GroupsActivityDetail-38f6)|getOffice365GroupsActivityDetail-38f6|[Parameters](#ParametersreportsgetOffice365GroupsActivityDetail-38f6)|Not Found|
|[az reports report show-office365-group-activity-detail81-cc](#reportsgetOffice365GroupsActivityDetail-81cc)|getOffice365GroupsActivityDetail-81cc|[Parameters](#ParametersreportsgetOffice365GroupsActivityDetail-81cc)|Not Found|
|[az reports report show-office365-group-activity-file-count](#reportsgetOffice365GroupsActivityFileCounts)|getOffice365GroupsActivityFileCounts|[Parameters](#ParametersreportsgetOffice365GroupsActivityFileCounts)|Not Found|
|[az reports report show-office365-group-activity-group-count](#reportsgetOffice365GroupsActivityGroupCounts)|getOffice365GroupsActivityGroupCounts|[Parameters](#ParametersreportsgetOffice365GroupsActivityGroupCounts)|Not Found|
|[az reports report show-office365-group-activity-storage](#reportsgetOffice365GroupsActivityStorage)|getOffice365GroupsActivityStorage|[Parameters](#ParametersreportsgetOffice365GroupsActivityStorage)|Not Found|
|[az reports report show-office365-service-user-count](#reportsgetOffice365ServicesUserCounts)|getOffice365ServicesUserCounts|[Parameters](#ParametersreportsgetOffice365ServicesUserCounts)|Not Found|
|[az reports report show-one-drive-activity-file-count](#reportsgetOneDriveActivityFileCounts)|getOneDriveActivityFileCounts|[Parameters](#ParametersreportsgetOneDriveActivityFileCounts)|Not Found|
|[az reports report show-one-drive-activity-user-count](#reportsgetOneDriveActivityUserCounts)|getOneDriveActivityUserCounts|[Parameters](#ParametersreportsgetOneDriveActivityUserCounts)|Not Found|
|[az reports report show-one-drive-activity-user-detail-c424](#reportsgetOneDriveActivityUserDetail-c424)|getOneDriveActivityUserDetail-c424|[Parameters](#ParametersreportsgetOneDriveActivityUserDetail-c424)|Not Found|
|[az reports report show-one-drive-activity-user-detail05-f1](#reportsgetOneDriveActivityUserDetail-05f1)|getOneDriveActivityUserDetail-05f1|[Parameters](#ParametersreportsgetOneDriveActivityUserDetail-05f1)|Not Found|
|[az reports report show-one-drive-usage-account-count](#reportsgetOneDriveUsageAccountCounts)|getOneDriveUsageAccountCounts|[Parameters](#ParametersreportsgetOneDriveUsageAccountCounts)|Not Found|
|[az reports report show-one-drive-usage-account-detail-dd7-f](#reportsgetOneDriveUsageAccountDetail-dd7f)|getOneDriveUsageAccountDetail-dd7f|[Parameters](#ParametersreportsgetOneDriveUsageAccountDetail-dd7f)|Not Found|
|[az reports report show-one-drive-usage-account-detail-e827](#reportsgetOneDriveUsageAccountDetail-e827)|getOneDriveUsageAccountDetail-e827|[Parameters](#ParametersreportsgetOneDriveUsageAccountDetail-e827)|Not Found|
|[az reports report show-one-drive-usage-file-count](#reportsgetOneDriveUsageFileCounts)|getOneDriveUsageFileCounts|[Parameters](#ParametersreportsgetOneDriveUsageFileCounts)|Not Found|
|[az reports report show-one-drive-usage-storage](#reportsgetOneDriveUsageStorage)|getOneDriveUsageStorage|[Parameters](#ParametersreportsgetOneDriveUsageStorage)|Not Found|
|[az reports report show-relying-party-detailed-summary](#reportsgetRelyingPartyDetailedSummary)|getRelyingPartyDetailedSummary|[Parameters](#ParametersreportsgetRelyingPartyDetailedSummary)|Not Found|
|[az reports report show-share-point-activity-file-count](#reportsgetSharePointActivityFileCounts)|getSharePointActivityFileCounts|[Parameters](#ParametersreportsgetSharePointActivityFileCounts)|Not Found|
|[az reports report show-share-point-activity-page](#reportsgetSharePointActivityPages)|getSharePointActivityPages|[Parameters](#ParametersreportsgetSharePointActivityPages)|Not Found|
|[az reports report show-share-point-activity-user-count](#reportsgetSharePointActivityUserCounts)|getSharePointActivityUserCounts|[Parameters](#ParametersreportsgetSharePointActivityUserCounts)|Not Found|
|[az reports report show-share-point-activity-user-detail-b778](#reportsgetSharePointActivityUserDetail-b778)|getSharePointActivityUserDetail-b778|[Parameters](#ParametersreportsgetSharePointActivityUserDetail-b778)|Not Found|
|[az reports report show-share-point-activity-user-detail-f3-be](#reportsgetSharePointActivityUserDetail-f3be)|getSharePointActivityUserDetail-f3be|[Parameters](#ParametersreportsgetSharePointActivityUserDetail-f3be)|Not Found|
|[az reports report show-share-point-site-usage-detail-d27-a](#reportsgetSharePointSiteUsageDetail-d27a)|getSharePointSiteUsageDetail-d27a|[Parameters](#ParametersreportsgetSharePointSiteUsageDetail-d27a)|Not Found|
|[az reports report show-share-point-site-usage-detail204-b](#reportsgetSharePointSiteUsageDetail-204b)|getSharePointSiteUsageDetail-204b|[Parameters](#ParametersreportsgetSharePointSiteUsageDetail-204b)|Not Found|
|[az reports report show-share-point-site-usage-file-count](#reportsgetSharePointSiteUsageFileCounts)|getSharePointSiteUsageFileCounts|[Parameters](#ParametersreportsgetSharePointSiteUsageFileCounts)|Not Found|
|[az reports report show-share-point-site-usage-page](#reportsgetSharePointSiteUsagePages)|getSharePointSiteUsagePages|[Parameters](#ParametersreportsgetSharePointSiteUsagePages)|Not Found|
|[az reports report show-share-point-site-usage-site-count](#reportsgetSharePointSiteUsageSiteCounts)|getSharePointSiteUsageSiteCounts|[Parameters](#ParametersreportsgetSharePointSiteUsageSiteCounts)|Not Found|
|[az reports report show-share-point-site-usage-storage](#reportsgetSharePointSiteUsageStorage)|getSharePointSiteUsageStorage|[Parameters](#ParametersreportsgetSharePointSiteUsageStorage)|Not Found|
|[az reports report show-skype-for-business-activity-count](#reportsgetSkypeForBusinessActivityCounts)|getSkypeForBusinessActivityCounts|[Parameters](#ParametersreportsgetSkypeForBusinessActivityCounts)|Not Found|
|[az reports report show-skype-for-business-activity-user-count](#reportsgetSkypeForBusinessActivityUserCounts)|getSkypeForBusinessActivityUserCounts|[Parameters](#ParametersreportsgetSkypeForBusinessActivityUserCounts)|Not Found|
|[az reports report show-skype-for-business-activity-user-detail-e4-c9](#reportsgetSkypeForBusinessActivityUserDetail-e4c9)|getSkypeForBusinessActivityUserDetail-e4c9|[Parameters](#ParametersreportsgetSkypeForBusinessActivityUserDetail-e4c9)|Not Found|
|[az reports report show-skype-for-business-activity-user-detail744-e](#reportsgetSkypeForBusinessActivityUserDetail-744e)|getSkypeForBusinessActivityUserDetail-744e|[Parameters](#ParametersreportsgetSkypeForBusinessActivityUserDetail-744e)|Not Found|
|[az reports report show-skype-for-business-device-usage-distribution-user-count](#reportsgetSkypeForBusinessDeviceUsageDistributionUserCounts)|getSkypeForBusinessDeviceUsageDistributionUserCounts|[Parameters](#ParametersreportsgetSkypeForBusinessDeviceUsageDistributionUserCounts)|Not Found|
|[az reports report show-skype-for-business-device-usage-user-count](#reportsgetSkypeForBusinessDeviceUsageUserCounts)|getSkypeForBusinessDeviceUsageUserCounts|[Parameters](#ParametersreportsgetSkypeForBusinessDeviceUsageUserCounts)|Not Found|
|[az reports report show-skype-for-business-device-usage-user-detail-a692](#reportsgetSkypeForBusinessDeviceUsageUserDetail-a692)|getSkypeForBusinessDeviceUsageUserDetail-a692|[Parameters](#ParametersreportsgetSkypeForBusinessDeviceUsageUserDetail-a692)|Not Found|
|[az reports report show-skype-for-business-device-usage-user-detail-e753](#reportsgetSkypeForBusinessDeviceUsageUserDetail-e753)|getSkypeForBusinessDeviceUsageUserDetail-e753|[Parameters](#ParametersreportsgetSkypeForBusinessDeviceUsageUserDetail-e753)|Not Found|
|[az reports report show-skype-for-business-organizer-activity-count](#reportsgetSkypeForBusinessOrganizerActivityCounts)|getSkypeForBusinessOrganizerActivityCounts|[Parameters](#ParametersreportsgetSkypeForBusinessOrganizerActivityCounts)|Not Found|
|[az reports report show-skype-for-business-organizer-activity-minute-count](#reportsgetSkypeForBusinessOrganizerActivityMinuteCounts)|getSkypeForBusinessOrganizerActivityMinuteCounts|[Parameters](#ParametersreportsgetSkypeForBusinessOrganizerActivityMinuteCounts)|Not Found|
|[az reports report show-skype-for-business-organizer-activity-user-count](#reportsgetSkypeForBusinessOrganizerActivityUserCounts)|getSkypeForBusinessOrganizerActivityUserCounts|[Parameters](#ParametersreportsgetSkypeForBusinessOrganizerActivityUserCounts)|Not Found|
|[az reports report show-skype-for-business-participant-activity-count](#reportsgetSkypeForBusinessParticipantActivityCounts)|getSkypeForBusinessParticipantActivityCounts|[Parameters](#ParametersreportsgetSkypeForBusinessParticipantActivityCounts)|Not Found|
|[az reports report show-skype-for-business-participant-activity-minute-count](#reportsgetSkypeForBusinessParticipantActivityMinuteCounts)|getSkypeForBusinessParticipantActivityMinuteCounts|[Parameters](#ParametersreportsgetSkypeForBusinessParticipantActivityMinuteCounts)|Not Found|
|[az reports report show-skype-for-business-participant-activity-user-count](#reportsgetSkypeForBusinessParticipantActivityUserCounts)|getSkypeForBusinessParticipantActivityUserCounts|[Parameters](#ParametersreportsgetSkypeForBusinessParticipantActivityUserCounts)|Not Found|
|[az reports report show-skype-for-business-peer-to-peer-activity-count](#reportsgetSkypeForBusinessPeerToPeerActivityCounts)|getSkypeForBusinessPeerToPeerActivityCounts|[Parameters](#ParametersreportsgetSkypeForBusinessPeerToPeerActivityCounts)|Not Found|
|[az reports report show-skype-for-business-peer-to-peer-activity-minute-count](#reportsgetSkypeForBusinessPeerToPeerActivityMinuteCounts)|getSkypeForBusinessPeerToPeerActivityMinuteCounts|[Parameters](#ParametersreportsgetSkypeForBusinessPeerToPeerActivityMinuteCounts)|Not Found|
|[az reports report show-skype-for-business-peer-to-peer-activity-user-count](#reportsgetSkypeForBusinessPeerToPeerActivityUserCounts)|getSkypeForBusinessPeerToPeerActivityUserCounts|[Parameters](#ParametersreportsgetSkypeForBusinessPeerToPeerActivityUserCounts)|Not Found|
|[az reports report show-team-device-usage-distribution-user-count](#reportsgetTeamsDeviceUsageDistributionUserCounts)|getTeamsDeviceUsageDistributionUserCounts|[Parameters](#ParametersreportsgetTeamsDeviceUsageDistributionUserCounts)|Not Found|
|[az reports report show-team-device-usage-user-count](#reportsgetTeamsDeviceUsageUserCounts)|getTeamsDeviceUsageUserCounts|[Parameters](#ParametersreportsgetTeamsDeviceUsageUserCounts)|Not Found|
|[az reports report show-team-device-usage-user-detail7148](#reportsgetTeamsDeviceUsageUserDetail-7148)|getTeamsDeviceUsageUserDetail-7148|[Parameters](#ParametersreportsgetTeamsDeviceUsageUserDetail-7148)|Not Found|
|[az reports report show-team-device-usage-user-detail7565](#reportsgetTeamsDeviceUsageUserDetail-7565)|getTeamsDeviceUsageUserDetail-7565|[Parameters](#ParametersreportsgetTeamsDeviceUsageUserDetail-7565)|Not Found|
|[az reports report show-team-user-activity-count](#reportsgetTeamsUserActivityCounts)|getTeamsUserActivityCounts|[Parameters](#ParametersreportsgetTeamsUserActivityCounts)|Not Found|
|[az reports report show-team-user-activity-user-count](#reportsgetTeamsUserActivityUserCounts)|getTeamsUserActivityUserCounts|[Parameters](#ParametersreportsgetTeamsUserActivityUserCounts)|Not Found|
|[az reports report show-team-user-activity-user-detail-a3-f1](#reportsgetTeamsUserActivityUserDetail-a3f1)|getTeamsUserActivityUserDetail-a3f1|[Parameters](#ParametersreportsgetTeamsUserActivityUserDetail-a3f1)|Not Found|
|[az reports report show-team-user-activity-user-detail-eb13](#reportsgetTeamsUserActivityUserDetail-eb13)|getTeamsUserActivityUserDetail-eb13|[Parameters](#ParametersreportsgetTeamsUserActivityUserDetail-eb13)|Not Found|
|[az reports report show-tenant-secure-score](#reportsgetTenantSecureScores)|getTenantSecureScores|[Parameters](#ParametersreportsgetTenantSecureScores)|Not Found|
|[az reports report show-user-credential-usage-detail](#reportsGetUserCredentialUsageDetails)|GetUserCredentialUsageDetails|[Parameters](#ParametersreportsGetUserCredentialUsageDetails)|Not Found|
|[az reports report show-yammer-activity-count](#reportsgetYammerActivityCounts)|getYammerActivityCounts|[Parameters](#ParametersreportsgetYammerActivityCounts)|Not Found|
|[az reports report show-yammer-activity-user-count](#reportsgetYammerActivityUserCounts)|getYammerActivityUserCounts|[Parameters](#ParametersreportsgetYammerActivityUserCounts)|Not Found|
|[az reports report show-yammer-activity-user-detail-ac30](#reportsgetYammerActivityUserDetail-ac30)|getYammerActivityUserDetail-ac30|[Parameters](#ParametersreportsgetYammerActivityUserDetail-ac30)|Not Found|
|[az reports report show-yammer-activity-user-detail15-a5](#reportsgetYammerActivityUserDetail-15a5)|getYammerActivityUserDetail-15a5|[Parameters](#ParametersreportsgetYammerActivityUserDetail-15a5)|Not Found|
|[az reports report show-yammer-device-usage-distribution-user-count](#reportsgetYammerDeviceUsageDistributionUserCounts)|getYammerDeviceUsageDistributionUserCounts|[Parameters](#ParametersreportsgetYammerDeviceUsageDistributionUserCounts)|Not Found|
|[az reports report show-yammer-device-usage-user-count](#reportsgetYammerDeviceUsageUserCounts)|getYammerDeviceUsageUserCounts|[Parameters](#ParametersreportsgetYammerDeviceUsageUserCounts)|Not Found|
|[az reports report show-yammer-device-usage-user-detail-cfad](#reportsgetYammerDeviceUsageUserDetail-cfad)|getYammerDeviceUsageUserDetail-cfad|[Parameters](#ParametersreportsgetYammerDeviceUsageUserDetail-cfad)|Not Found|
|[az reports report show-yammer-device-usage-user-detail-d0-ac](#reportsgetYammerDeviceUsageUserDetail-d0ac)|getYammerDeviceUsageUserDetail-d0ac|[Parameters](#ParametersreportsgetYammerDeviceUsageUserDetail-d0ac)|Not Found|
|[az reports report show-yammer-group-activity-count](#reportsgetYammerGroupsActivityCounts)|getYammerGroupsActivityCounts|[Parameters](#ParametersreportsgetYammerGroupsActivityCounts)|Not Found|
|[az reports report show-yammer-group-activity-detail-da9-a](#reportsgetYammerGroupsActivityDetail-da9a)|getYammerGroupsActivityDetail-da9a|[Parameters](#ParametersreportsgetYammerGroupsActivityDetail-da9a)|Not Found|
|[az reports report show-yammer-group-activity-detail0-d7-d](#reportsgetYammerGroupsActivityDetail-0d7d)|getYammerGroupsActivityDetail-0d7d|[Parameters](#ParametersreportsgetYammerGroupsActivityDetail-0d7d)|Not Found|
|[az reports report show-yammer-group-activity-group-count](#reportsgetYammerGroupsActivityGroupCounts)|getYammerGroupsActivityGroupCounts|[Parameters](#ParametersreportsgetYammerGroupsActivityGroupCounts)|Not Found|
|[az reports report update-application-sign-in-detailed-summary](#reportsUpdateApplicationSignInDetailedSummary)|UpdateApplicationSignInDetailedSummary|[Parameters](#ParametersreportsUpdateApplicationSignInDetailedSummary)|Not Found|
|[az reports report update-credential-user-registration-detail](#reportsUpdateCredentialUserRegistrationDetails)|UpdateCredentialUserRegistrationDetails|[Parameters](#ParametersreportsUpdateCredentialUserRegistrationDetails)|Not Found|
|[az reports report update-daily-print-usage-summary-by-printer](#reportsUpdateDailyPrintUsageSummariesByPrinter)|UpdateDailyPrintUsageSummariesByPrinter|[Parameters](#ParametersreportsUpdateDailyPrintUsageSummariesByPrinter)|Not Found|
|[az reports report update-daily-print-usage-summary-by-user](#reportsUpdateDailyPrintUsageSummariesByUser)|UpdateDailyPrintUsageSummariesByUser|[Parameters](#ParametersreportsUpdateDailyPrintUsageSummariesByUser)|Not Found|
|[az reports report update-monthly-print-usage-summary-by-printer](#reportsUpdateMonthlyPrintUsageSummariesByPrinter)|UpdateMonthlyPrintUsageSummariesByPrinter|[Parameters](#ParametersreportsUpdateMonthlyPrintUsageSummariesByPrinter)|Not Found|
|[az reports report update-monthly-print-usage-summary-by-user](#reportsUpdateMonthlyPrintUsageSummariesByUser)|UpdateMonthlyPrintUsageSummariesByUser|[Parameters](#ParametersreportsUpdateMonthlyPrintUsageSummariesByUser)|Not Found|
|[az reports report update-user-credential-usage-detail](#reportsUpdateUserCredentialUsageDetails)|UpdateUserCredentialUsageDetails|[Parameters](#ParametersreportsUpdateUserCredentialUsageDetails)|Not Found|

### <a name="CommandsInreports.reportRoot">Commands in `az reports report-report-root` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az reports report-report-root show-report-root](#reports.reportRootGetReportRoot)|GetReportRoot|[Parameters](#Parametersreports.reportRootGetReportRoot)|Not Found|
|[az reports report-report-root update-report-root](#reports.reportRootUpdateReportRoot)|UpdateReportRoot|[Parameters](#Parametersreports.reportRootUpdateReportRoot)|Not Found|


## COMMAND DETAILS

### group `az reports audit-log`
#### <a name="auditLogsDeleteDirectoryAudits">Command `az reports audit-log delete`</a>

##### <a name="ParametersauditLogsDeleteDirectoryAudits">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-audit-id**|string|key: id of directoryAudit|directory_audit_id|directoryAudit-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="auditLogsDeleteDirectoryProvisioning">Command `az reports audit-log delete`</a>

##### <a name="ParametersauditLogsDeleteDirectoryProvisioning">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provisioning-object-summary-id**|string|key: id of provisioningObjectSummary|provisioning_object_summary_id|provisioningObjectSummary-id|

#### <a name="auditLogsDeleteProvisioning">Command `az reports audit-log delete`</a>

##### <a name="ParametersauditLogsDeleteProvisioning">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="auditLogsDeleteRestrictedSignIns">Command `az reports audit-log delete`</a>

##### <a name="ParametersauditLogsDeleteRestrictedSignIns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--restricted-sign-in-id**|string|key: id of restrictedSignIn|restricted_sign_in_id|restrictedSignIn-id|

#### <a name="auditLogsDeleteSignIns">Command `az reports audit-log delete`</a>

##### <a name="ParametersauditLogsDeleteSignIns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sign-in-id**|string|key: id of signIn|sign_in_id|signIn-id|

#### <a name="auditLogsCreateDirectoryAudits">Command `az reports audit-log create-directory-audit`</a>

##### <a name="ParametersauditLogsCreateDirectoryAudits">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--activity-date-time**|date-time|Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|activity_date_time|activityDateTime|
|**--activity-display-name**|string|Indicates the activity name or the operation name (examples: 'Create User' and 'Add member to group'). For full list, see Azure AD activity list.|activity_display_name|activityDisplayName|
|**--additional-details**|array|Indicates additional details on the activity.|additional_details|additionalDetails|
|**--category**|string|Indicates which resource category that's targeted by the activity. (For example: User Management, Group Management etc..)|category|category|
|**--correlation-id**|string|Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services.|correlation_id|correlationId|
|**--logged-by-service**|string|Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management.|logged_by_service|loggedByService|
|**--operation-type**|string||operation_type|operationType|
|**--result**|choice||result|result|
|**--result-reason**|string|Describes cause of 'failure' or 'timeout' results.|result_reason|resultReason|
|**--target-resources**|array|Indicates information on which resource was changed due to the activity. Target Resource Type can be User, Device, Directory, App, Role, Group, Policy or Other.|target_resources|targetResources|
|**--app**|object|appIdentity|app|app|
|**--user**|object|userIdentity|user|user|

#### <a name="auditLogsCreateDirectoryProvisioning">Command `az reports audit-log create-directory-provisioning`</a>

##### <a name="ParametersauditLogsCreateDirectoryProvisioning">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New navigation property|body|body|

#### <a name="auditLogsCreateProvisioning">Command `az reports audit-log create-provisioning`</a>

##### <a name="ParametersauditLogsCreateProvisioning">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New navigation property|body|body|

#### <a name="auditLogsCreateRestrictedSignIns">Command `az reports audit-log create-restricted-sign-in`</a>

##### <a name="ParametersauditLogsCreateRestrictedSignIns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--alternate-sign-in-name**|string||alternate_sign_in_name|alternateSignInName|
|**--app-display-name**|string|App name displayed in the Azure Portal.|app_display_name|appDisplayName|
|**--app-id**|string|Unique GUID representing the app ID in the Azure Active Directory.|app_id|appId|
|**--applied-conditional-access-policies**|array||applied_conditional_access_policies|appliedConditionalAccessPolicies|
|**--authentication-details**|array||authentication_details|authenticationDetails|
|**--authentication-methods-used**|array||authentication_methods_used|authenticationMethodsUsed|
|**--authentication-processing-details**|array||authentication_processing_details|authenticationProcessingDetails|
|**--authentication-requirement**|string||authentication_requirement|authenticationRequirement|
|**--authentication-requirement-policies**|array||authentication_requirement_policies|authenticationRequirementPolicies|
|**--client-app-used**|string|Identifies the legacy client used for sign-in activity.  Includes Browser, Exchange Active Sync, modern clients, IMAP, MAPI, SMTP, and POP.|client_app_used|clientAppUsed|
|**--conditional-access-status**|choice||conditional_access_status|conditionalAccessStatus|
|**--correlation-id**|string|The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity.|correlation_id|correlationId|
|**--created-date-time**|date-time|Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--device-detail**|object|deviceDetail|device_detail|deviceDetail|
|**--ip-address**|string|IP address of the client used to sign in.|ip_address|ipAddress|
|**--is-interactive**|boolean|Indicates if a sign-in is interactive or not.|is_interactive|isInteractive|
|**--mfa-detail**|object|mfaDetail|mfa_detail|mfaDetail|
|**--network-location-details**|array||network_location_details|networkLocationDetails|
|**--original-request-id**|string||original_request_id|originalRequestId|
|**--processing-time-in-milliseconds**|integer||processing_time_in_milliseconds|processingTimeInMilliseconds|
|**--resource-display-name**|string|Name of the resource the user signed into.|resource_display_name|resourceDisplayName|
|**--resource-id**|string|ID of the resource that the user signed into.|resource_id|resourceId|
|**--resource-tenant-id**|string||resource_tenant_id|resourceTenantId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-types**|array|Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue.|risk_event_types|riskEventTypes|
|**--risk-event-types-v2**|array|The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.|risk_event_types_v2|riskEventTypes_v2|
|**--risk-level-aggregated**|choice||risk_level_aggregated|riskLevelAggregated|
|**--risk-level-during-sign-in**|choice||risk_level_during_sign_in|riskLevelDuringSignIn|
|**--risk-state**|choice||risk_state|riskState|
|**--service-principal-id**|string||service_principal_id|servicePrincipalId|
|**--service-principal-name**|string||service_principal_name|servicePrincipalName|
|**--sign-in-event-types**|array||sign_in_event_types|signInEventTypes|
|**--status**|object|signInStatus|status|status|
|**--token-issuer-name**|string||token_issuer_name|tokenIssuerName|
|**--token-issuer-type**|choice||token_issuer_type|tokenIssuerType|
|**--user-agent**|string||user_agent|userAgent|
|**--user-display-name**|string|Display name of the user that initiated the sign-in.|user_display_name|userDisplayName|
|**--user-id**|string|ID of the user that initiated the sign-in.|user_id|userId|
|**--user-principal-name**|string|User principal name of the user that initiated the sign-in.|user_principal_name|userPrincipalName|
|**--city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--target-tenant-id**|uuid||target_tenant_id|targetTenantId|

#### <a name="auditLogsCreateSignIns">Command `az reports audit-log create-sign-in`</a>

##### <a name="ParametersauditLogsCreateSignIns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--alternate-sign-in-name**|string||alternate_sign_in_name|alternateSignInName|
|**--app-display-name**|string|App name displayed in the Azure Portal.|app_display_name|appDisplayName|
|**--app-id**|string|Unique GUID representing the app ID in the Azure Active Directory.|app_id|appId|
|**--applied-conditional-access-policies**|array||applied_conditional_access_policies|appliedConditionalAccessPolicies|
|**--authentication-details**|array||authentication_details|authenticationDetails|
|**--authentication-methods-used**|array||authentication_methods_used|authenticationMethodsUsed|
|**--authentication-processing-details**|array||authentication_processing_details|authenticationProcessingDetails|
|**--authentication-requirement**|string||authentication_requirement|authenticationRequirement|
|**--authentication-requirement-policies**|array||authentication_requirement_policies|authenticationRequirementPolicies|
|**--client-app-used**|string|Identifies the legacy client used for sign-in activity.  Includes Browser, Exchange Active Sync, modern clients, IMAP, MAPI, SMTP, and POP.|client_app_used|clientAppUsed|
|**--conditional-access-status**|choice||conditional_access_status|conditionalAccessStatus|
|**--correlation-id**|string|The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity.|correlation_id|correlationId|
|**--created-date-time**|date-time|Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--device-detail**|object|deviceDetail|device_detail|deviceDetail|
|**--ip-address**|string|IP address of the client used to sign in.|ip_address|ipAddress|
|**--is-interactive**|boolean|Indicates if a sign-in is interactive or not.|is_interactive|isInteractive|
|**--mfa-detail**|object|mfaDetail|mfa_detail|mfaDetail|
|**--network-location-details**|array||network_location_details|networkLocationDetails|
|**--original-request-id**|string||original_request_id|originalRequestId|
|**--processing-time-in-milliseconds**|integer||processing_time_in_milliseconds|processingTimeInMilliseconds|
|**--resource-display-name**|string|Name of the resource the user signed into.|resource_display_name|resourceDisplayName|
|**--resource-id**|string|ID of the resource that the user signed into.|resource_id|resourceId|
|**--resource-tenant-id**|string||resource_tenant_id|resourceTenantId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-types**|array|Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue.|risk_event_types|riskEventTypes|
|**--risk-event-types-v2**|array|The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.|risk_event_types_v2|riskEventTypes_v2|
|**--risk-level-aggregated**|choice||risk_level_aggregated|riskLevelAggregated|
|**--risk-level-during-sign-in**|choice||risk_level_during_sign_in|riskLevelDuringSignIn|
|**--risk-state**|choice||risk_state|riskState|
|**--service-principal-id**|string||service_principal_id|servicePrincipalId|
|**--service-principal-name**|string||service_principal_name|servicePrincipalName|
|**--sign-in-event-types**|array||sign_in_event_types|signInEventTypes|
|**--status**|object|signInStatus|status|status|
|**--token-issuer-name**|string||token_issuer_name|tokenIssuerName|
|**--token-issuer-type**|choice||token_issuer_type|tokenIssuerType|
|**--user-agent**|string||user_agent|userAgent|
|**--user-display-name**|string|Display name of the user that initiated the sign-in.|user_display_name|userDisplayName|
|**--user-id**|string|ID of the user that initiated the sign-in.|user_id|userId|
|**--user-principal-name**|string|User principal name of the user that initiated the sign-in.|user_principal_name|userPrincipalName|
|**--city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|

#### <a name="auditLogsListDirectoryAudits">Command `az reports audit-log list-directory-audit`</a>

##### <a name="ParametersauditLogsListDirectoryAudits">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="auditLogsListDirectoryProvisioning">Command `az reports audit-log list-directory-provisioning`</a>

##### <a name="ParametersauditLogsListDirectoryProvisioning">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="auditLogsListProvisioning">Command `az reports audit-log list-provisioning`</a>

##### <a name="ParametersauditLogsListProvisioning">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="auditLogsListRestrictedSignIns">Command `az reports audit-log list-restricted-sign-in`</a>

##### <a name="ParametersauditLogsListRestrictedSignIns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="auditLogsListSignIns">Command `az reports audit-log list-sign-in`</a>

##### <a name="ParametersauditLogsListSignIns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="auditLogsGetDirectoryAudits">Command `az reports audit-log show-directory-audit`</a>

##### <a name="ParametersauditLogsGetDirectoryAudits">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-audit-id**|string|key: id of directoryAudit|directory_audit_id|directoryAudit-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="auditLogsGetDirectoryProvisioning">Command `az reports audit-log show-directory-provisioning`</a>

##### <a name="ParametersauditLogsGetDirectoryProvisioning">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provisioning-object-summary-id**|string|key: id of provisioningObjectSummary|provisioning_object_summary_id|provisioningObjectSummary-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="auditLogsGetProvisioning">Command `az reports audit-log show-provisioning`</a>

##### <a name="ParametersauditLogsGetProvisioning">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provisioning-object-summary-id**|string|key: id of provisioningObjectSummary|provisioning_object_summary_id|provisioningObjectSummary-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="auditLogsGetRestrictedSignIns">Command `az reports audit-log show-restricted-sign-in`</a>

##### <a name="ParametersauditLogsGetRestrictedSignIns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--restricted-sign-in-id**|string|key: id of restrictedSignIn|restricted_sign_in_id|restrictedSignIn-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="auditLogsGetSignIns">Command `az reports audit-log show-sign-in`</a>

##### <a name="ParametersauditLogsGetSignIns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sign-in-id**|string|key: id of signIn|sign_in_id|signIn-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="auditLogsUpdateDirectoryAudits">Command `az reports audit-log update-directory-audit`</a>

##### <a name="ParametersauditLogsUpdateDirectoryAudits">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-audit-id**|string|key: id of directoryAudit|directory_audit_id|directoryAudit-id|
|**--id**|string|Read-only.|id|id|
|**--activity-date-time**|date-time|Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|activity_date_time|activityDateTime|
|**--activity-display-name**|string|Indicates the activity name or the operation name (examples: 'Create User' and 'Add member to group'). For full list, see Azure AD activity list.|activity_display_name|activityDisplayName|
|**--additional-details**|array|Indicates additional details on the activity.|additional_details|additionalDetails|
|**--category**|string|Indicates which resource category that's targeted by the activity. (For example: User Management, Group Management etc..)|category|category|
|**--correlation-id**|string|Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services.|correlation_id|correlationId|
|**--logged-by-service**|string|Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management.|logged_by_service|loggedByService|
|**--operation-type**|string||operation_type|operationType|
|**--result**|choice||result|result|
|**--result-reason**|string|Describes cause of 'failure' or 'timeout' results.|result_reason|resultReason|
|**--target-resources**|array|Indicates information on which resource was changed due to the activity. Target Resource Type can be User, Device, Directory, App, Role, Group, Policy or Other.|target_resources|targetResources|
|**--app**|object|appIdentity|app|app|
|**--user**|object|userIdentity|user|user|

#### <a name="auditLogsUpdateDirectoryProvisioning">Command `az reports audit-log update-directory-provisioning`</a>

##### <a name="ParametersauditLogsUpdateDirectoryProvisioning">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provisioning-object-summary-id**|string|key: id of provisioningObjectSummary|provisioning_object_summary_id|provisioningObjectSummary-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="auditLogsUpdateProvisioning">Command `az reports audit-log update-provisioning`</a>

##### <a name="ParametersauditLogsUpdateProvisioning">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--provisioning-object-summary-id**|string|key: id of provisioningObjectSummary|provisioning_object_summary_id|provisioningObjectSummary-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="auditLogsUpdateRestrictedSignIns">Command `az reports audit-log update-restricted-sign-in`</a>

##### <a name="ParametersauditLogsUpdateRestrictedSignIns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--restricted-sign-in-id**|string|key: id of restrictedSignIn|restricted_sign_in_id|restrictedSignIn-id|
|**--id**|string|Read-only.|id|id|
|**--alternate-sign-in-name**|string||alternate_sign_in_name|alternateSignInName|
|**--app-display-name**|string|App name displayed in the Azure Portal.|app_display_name|appDisplayName|
|**--app-id**|string|Unique GUID representing the app ID in the Azure Active Directory.|app_id|appId|
|**--applied-conditional-access-policies**|array||applied_conditional_access_policies|appliedConditionalAccessPolicies|
|**--authentication-details**|array||authentication_details|authenticationDetails|
|**--authentication-methods-used**|array||authentication_methods_used|authenticationMethodsUsed|
|**--authentication-processing-details**|array||authentication_processing_details|authenticationProcessingDetails|
|**--authentication-requirement**|string||authentication_requirement|authenticationRequirement|
|**--authentication-requirement-policies**|array||authentication_requirement_policies|authenticationRequirementPolicies|
|**--client-app-used**|string|Identifies the legacy client used for sign-in activity.  Includes Browser, Exchange Active Sync, modern clients, IMAP, MAPI, SMTP, and POP.|client_app_used|clientAppUsed|
|**--conditional-access-status**|choice||conditional_access_status|conditionalAccessStatus|
|**--correlation-id**|string|The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity.|correlation_id|correlationId|
|**--created-date-time**|date-time|Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--device-detail**|object|deviceDetail|device_detail|deviceDetail|
|**--ip-address**|string|IP address of the client used to sign in.|ip_address|ipAddress|
|**--is-interactive**|boolean|Indicates if a sign-in is interactive or not.|is_interactive|isInteractive|
|**--mfa-detail**|object|mfaDetail|mfa_detail|mfaDetail|
|**--network-location-details**|array||network_location_details|networkLocationDetails|
|**--original-request-id**|string||original_request_id|originalRequestId|
|**--processing-time-in-milliseconds**|integer||processing_time_in_milliseconds|processingTimeInMilliseconds|
|**--resource-display-name**|string|Name of the resource the user signed into.|resource_display_name|resourceDisplayName|
|**--resource-id**|string|ID of the resource that the user signed into.|resource_id|resourceId|
|**--resource-tenant-id**|string||resource_tenant_id|resourceTenantId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-types**|array|Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue.|risk_event_types|riskEventTypes|
|**--risk-event-types-v2**|array|The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.|risk_event_types_v2|riskEventTypes_v2|
|**--risk-level-aggregated**|choice||risk_level_aggregated|riskLevelAggregated|
|**--risk-level-during-sign-in**|choice||risk_level_during_sign_in|riskLevelDuringSignIn|
|**--risk-state**|choice||risk_state|riskState|
|**--service-principal-id**|string||service_principal_id|servicePrincipalId|
|**--service-principal-name**|string||service_principal_name|servicePrincipalName|
|**--sign-in-event-types**|array||sign_in_event_types|signInEventTypes|
|**--status**|object|signInStatus|status|status|
|**--token-issuer-name**|string||token_issuer_name|tokenIssuerName|
|**--token-issuer-type**|choice||token_issuer_type|tokenIssuerType|
|**--user-agent**|string||user_agent|userAgent|
|**--user-display-name**|string|Display name of the user that initiated the sign-in.|user_display_name|userDisplayName|
|**--user-id**|string|ID of the user that initiated the sign-in.|user_id|userId|
|**--user-principal-name**|string|User principal name of the user that initiated the sign-in.|user_principal_name|userPrincipalName|
|**--city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|
|**--target-tenant-id**|uuid||target_tenant_id|targetTenantId|

#### <a name="auditLogsUpdateSignIns">Command `az reports audit-log update-sign-in`</a>

##### <a name="ParametersauditLogsUpdateSignIns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sign-in-id**|string|key: id of signIn|sign_in_id|signIn-id|
|**--id**|string|Read-only.|id|id|
|**--alternate-sign-in-name**|string||alternate_sign_in_name|alternateSignInName|
|**--app-display-name**|string|App name displayed in the Azure Portal.|app_display_name|appDisplayName|
|**--app-id**|string|Unique GUID representing the app ID in the Azure Active Directory.|app_id|appId|
|**--applied-conditional-access-policies**|array||applied_conditional_access_policies|appliedConditionalAccessPolicies|
|**--authentication-details**|array||authentication_details|authenticationDetails|
|**--authentication-methods-used**|array||authentication_methods_used|authenticationMethodsUsed|
|**--authentication-processing-details**|array||authentication_processing_details|authenticationProcessingDetails|
|**--authentication-requirement**|string||authentication_requirement|authenticationRequirement|
|**--authentication-requirement-policies**|array||authentication_requirement_policies|authenticationRequirementPolicies|
|**--client-app-used**|string|Identifies the legacy client used for sign-in activity.  Includes Browser, Exchange Active Sync, modern clients, IMAP, MAPI, SMTP, and POP.|client_app_used|clientAppUsed|
|**--conditional-access-status**|choice||conditional_access_status|conditionalAccessStatus|
|**--correlation-id**|string|The request ID sent from the client when the sign-in is initiated; used to troubleshoot sign-in activity.|correlation_id|correlationId|
|**--created-date-time**|date-time|Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is reported as '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--device-detail**|object|deviceDetail|device_detail|deviceDetail|
|**--ip-address**|string|IP address of the client used to sign in.|ip_address|ipAddress|
|**--is-interactive**|boolean|Indicates if a sign-in is interactive or not.|is_interactive|isInteractive|
|**--mfa-detail**|object|mfaDetail|mfa_detail|mfaDetail|
|**--network-location-details**|array||network_location_details|networkLocationDetails|
|**--original-request-id**|string||original_request_id|originalRequestId|
|**--processing-time-in-milliseconds**|integer||processing_time_in_milliseconds|processingTimeInMilliseconds|
|**--resource-display-name**|string|Name of the resource the user signed into.|resource_display_name|resourceDisplayName|
|**--resource-id**|string|ID of the resource that the user signed into.|resource_id|resourceId|
|**--resource-tenant-id**|string||resource_tenant_id|resourceTenantId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-types**|array|Risk event types associated with the sign-in. The possible values are: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue.|risk_event_types|riskEventTypes|
|**--risk-event-types-v2**|array|The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.|risk_event_types_v2|riskEventTypes_v2|
|**--risk-level-aggregated**|choice||risk_level_aggregated|riskLevelAggregated|
|**--risk-level-during-sign-in**|choice||risk_level_during_sign_in|riskLevelDuringSignIn|
|**--risk-state**|choice||risk_state|riskState|
|**--service-principal-id**|string||service_principal_id|servicePrincipalId|
|**--service-principal-name**|string||service_principal_name|servicePrincipalName|
|**--sign-in-event-types**|array||sign_in_event_types|signInEventTypes|
|**--status**|object|signInStatus|status|status|
|**--token-issuer-name**|string||token_issuer_name|tokenIssuerName|
|**--token-issuer-type**|choice||token_issuer_type|tokenIssuerType|
|**--user-agent**|string||user_agent|userAgent|
|**--user-display-name**|string|Display name of the user that initiated the sign-in.|user_display_name|userDisplayName|
|**--user-id**|string|ID of the user that initiated the sign-in.|user_id|userId|
|**--user-principal-name**|string|User principal name of the user that initiated the sign-in.|user_principal_name|userPrincipalName|
|**--city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|

### group `az reports audit-log-audit-log-root`
#### <a name="auditLogs.auditLogRootGetAuditLogRoot">Command `az reports audit-log-audit-log-root show-audit-log-root`</a>

##### <a name="ParametersauditLogs.auditLogRootGetAuditLogRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="auditLogs.auditLogRootUpdateAuditLogRoot">Command `az reports audit-log-audit-log-root update-audit-log-root`</a>

##### <a name="ParametersauditLogs.auditLogRootUpdateAuditLogRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--directory-audits**|array|Read-only. Nullable.|directory_audits|directoryAudits|
|**--directory-provisioning**|array||directory_provisioning|directoryProvisioning|
|**--provisioning**|array||provisioning|provisioning|
|**--restricted-sign-ins**|array||restricted_sign_ins|restrictedSignIns|
|**--sign-ins**|array|Read-only. Nullable.|sign_ins|signIns|

### group `az reports report`
#### <a name="reportsDeleteApplicationSignInDetailedSummary">Command `az reports report delete`</a>

##### <a name="ParametersreportsDeleteApplicationSignInDetailedSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-sign-in-detailed-summary-id**|string|key: id of applicationSignInDetailedSummary|application_sign_in_detailed_summary_id|applicationSignInDetailedSummary-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="reportsDeleteCredentialUserRegistrationDetails">Command `az reports report delete`</a>

##### <a name="ParametersreportsDeleteCredentialUserRegistrationDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--credential-user-registration-details-id**|string|key: id of credentialUserRegistrationDetails|credential_user_registration_details_id|credentialUserRegistrationDetails-id|

#### <a name="reportsDeleteDailyPrintUsageSummariesByPrinter">Command `az reports report delete`</a>

##### <a name="ParametersreportsDeleteDailyPrintUsageSummariesByPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-printer-id**|string|key: id of PrintUsageSummaryByPrinter|print_usage_summary_by_printer_id|PrintUsageSummaryByPrinter-id|

#### <a name="reportsDeleteDailyPrintUsageSummariesByUser">Command `az reports report delete`</a>

##### <a name="ParametersreportsDeleteDailyPrintUsageSummariesByUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-user-id**|string|key: id of PrintUsageSummaryByUser|print_usage_summary_by_user_id|PrintUsageSummaryByUser-id|

#### <a name="reportsDeleteMonthlyPrintUsageSummariesByPrinter">Command `az reports report delete`</a>

##### <a name="ParametersreportsDeleteMonthlyPrintUsageSummariesByPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="reportsDeleteMonthlyPrintUsageSummariesByUser">Command `az reports report delete`</a>

##### <a name="ParametersreportsDeleteMonthlyPrintUsageSummariesByUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="reportsDeleteUserCredentialUsageDetails">Command `az reports report delete`</a>

##### <a name="ParametersreportsDeleteUserCredentialUsageDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-credential-usage-details-id**|string|key: id of userCredentialUsageDetails|user_credential_usage_details_id|userCredentialUsageDetails-id|

#### <a name="reportsCreateApplicationSignInDetailedSummary">Command `az reports report create-application-sign-in-detailed-summary`</a>

##### <a name="ParametersreportsCreateApplicationSignInDetailedSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--aggregated-event-date-time**|date-time||aggregated_event_date_time|aggregatedEventDateTime|
|**--app-display-name**|string||app_display_name|appDisplayName|
|**--app-id**|string||app_id|appId|
|**--sign-in-count**|integer||sign_in_count|signInCount|
|**--status**|object|signInStatus|status|status|

#### <a name="reportsCreateCredentialUserRegistrationDetails">Command `az reports report create-credential-user-registration-detail`</a>

##### <a name="ParametersreportsCreateCredentialUserRegistrationDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--auth-methods**|array||auth_methods|authMethods|
|**--is-capable**|boolean||is_capable|isCapable|
|**--is-enabled**|boolean||is_enabled|isEnabled|
|**--is-mfa-registered**|boolean||is_mfa_registered|isMfaRegistered|
|**--is-registered**|boolean||is_registered|isRegistered|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

#### <a name="reportsCreateDailyPrintUsageSummariesByPrinter">Command `az reports report create-daily-print-usage-summary-by-printer`</a>

##### <a name="ParametersreportsCreateDailyPrintUsageSummariesByPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--printer-id**|string||printer_id|printerId|
|**--usage-date**|date||usage_date|usageDate|

#### <a name="reportsCreateDailyPrintUsageSummariesByUser">Command `az reports report create-daily-print-usage-summary-by-user`</a>

##### <a name="ParametersreportsCreateDailyPrintUsageSummariesByUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--usage-date**|date||usage_date|usageDate|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

#### <a name="reportsCreateMonthlyPrintUsageSummariesByPrinter">Command `az reports report create-monthly-print-usage-summary-by-printer`</a>

##### <a name="ParametersreportsCreateMonthlyPrintUsageSummariesByPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--printer-id**|string||printer_id|printerId|
|**--usage-date**|date||usage_date|usageDate|

#### <a name="reportsCreateMonthlyPrintUsageSummariesByUser">Command `az reports report create-monthly-print-usage-summary-by-user`</a>

##### <a name="ParametersreportsCreateMonthlyPrintUsageSummariesByUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--usage-date**|date||usage_date|usageDate|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

#### <a name="reportsCreateUserCredentialUsageDetails">Command `az reports report create-user-credential-usage-detail`</a>

##### <a name="ParametersreportsCreateUserCredentialUsageDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--auth-method**|choice||auth_method|authMethod|
|**--event-date-time**|date-time||event_date_time|eventDateTime|
|**--failure-reason**|string||failure_reason|failureReason|
|**--feature**|choice||feature|feature|
|**--is-success**|boolean||is_success|isSuccess|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

#### <a name="reportsdeviceConfigurationDeviceActivity">Command `az reports report device-configuration-device-activity`</a>

##### <a name="ParametersreportsdeviceConfigurationDeviceActivity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="reportsdeviceConfigurationUserActivity">Command `az reports report device-configuration-user-activity`</a>

##### <a name="ParametersreportsdeviceConfigurationUserActivity">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="reportsListApplicationSignInDetailedSummary">Command `az reports report list-application-sign-in-detailed-summary`</a>

##### <a name="ParametersreportsListApplicationSignInDetailedSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="reportsListCredentialUserRegistrationDetails">Command `az reports report list-credential-user-registration-detail`</a>

##### <a name="ParametersreportsListCredentialUserRegistrationDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="reportsListDailyPrintUsageSummariesByPrinter">Command `az reports report list-daily-print-usage-summary`</a>

##### <a name="ParametersreportsListDailyPrintUsageSummariesByPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="reportsListDailyPrintUsageSummariesByUser">Command `az reports report list-daily-print-usage-summary`</a>

##### <a name="ParametersreportsListDailyPrintUsageSummariesByUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="reportsListMonthlyPrintUsageSummariesByPrinter">Command `az reports report list-monthly-print-usage-summary`</a>

##### <a name="ParametersreportsListMonthlyPrintUsageSummariesByPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="reportsListMonthlyPrintUsageSummariesByUser">Command `az reports report list-monthly-print-usage-summary`</a>

##### <a name="ParametersreportsListMonthlyPrintUsageSummariesByUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="reportsListUserCredentialUsageDetails">Command `az reports report list-user-credential-usage-detail`</a>

##### <a name="ParametersreportsListUserCredentialUsageDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="reportsmanagedDeviceEnrollmentAbandonmentDetails">Command `az reports report managed-device-enrollment-abandonment-detail`</a>

##### <a name="ParametersreportsmanagedDeviceEnrollmentAbandonmentDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--skip**|integer||skip|skip|
|**--top**|integer||top|top|
|**--filter**|string||filter|filter|
|**--skip-token**|string||skip_token|skipToken|

#### <a name="reportsmanagedDeviceEnrollmentAbandonmentSummary">Command `az reports report managed-device-enrollment-abandonment-summary`</a>

##### <a name="ParametersreportsmanagedDeviceEnrollmentAbandonmentSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--skip**|integer||skip|skip|
|**--top**|integer||top|top|
|**--filter**|string||filter|filter|
|**--skip-token**|string||skip_token|skipToken|

#### <a name="reportsmanagedDeviceEnrollmentFailureDetails-027e">Command `az reports report managed-device-enrollment-failure-details027-e`</a>

##### <a name="ParametersreportsmanagedDeviceEnrollmentFailureDetails-027e">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="reportsmanagedDeviceEnrollmentFailureDetails-2b3d">Command `az reports report managed-device-enrollment-failure-details2-b3-d`</a>

##### <a name="ParametersreportsmanagedDeviceEnrollmentFailureDetails-2b3d">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--skip**|integer||skip|skip|
|**--top**|integer||top|top|
|**--filter**|string||filter|filter|
|**--skip-token**|string||skip_token|skipToken|

#### <a name="reportsmanagedDeviceEnrollmentFailureTrends">Command `az reports report managed-device-enrollment-failure-trend`</a>

##### <a name="ParametersreportsmanagedDeviceEnrollmentFailureTrends">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="reportsmanagedDeviceEnrollmentTopFailures-afd1">Command `az reports report managed-device-enrollment-top-failure-afd1`</a>

##### <a name="ParametersreportsmanagedDeviceEnrollmentTopFailures-afd1">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsmanagedDeviceEnrollmentTopFailures-4669">Command `az reports report managed-device-enrollment-top-failures4669`</a>

##### <a name="ParametersreportsmanagedDeviceEnrollmentTopFailures-4669">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="reportsGetApplicationSignInDetailedSummary">Command `az reports report show-application-sign-in-detailed-summary`</a>

##### <a name="ParametersreportsGetApplicationSignInDetailedSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-sign-in-detailed-summary-id**|string|key: id of applicationSignInDetailedSummary|application_sign_in_detailed_summary_id|applicationSignInDetailedSummary-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="reportsgetAzureADApplicationSignInSummary">Command `az reports report show-azure-ad-application-sign-in-summary`</a>

##### <a name="ParametersreportsgetAzureADApplicationSignInSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetAzureADFeatureUsage">Command `az reports report show-azure-ad-feature-usage`</a>

##### <a name="ParametersreportsgetAzureADFeatureUsage">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetAzureADLicenseUsage">Command `az reports report show-azure-ad-license-usage`</a>

##### <a name="ParametersreportsgetAzureADLicenseUsage">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetAzureADUserFeatureUsage">Command `az reports report show-azure-ad-user-feature-usage`</a>

##### <a name="ParametersreportsgetAzureADUserFeatureUsage">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="reportsgetCredentialUsageSummary">Command `az reports report show-credential-usage-summary`</a>

##### <a name="ParametersreportsgetCredentialUsageSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetCredentialUserRegistrationCount">Command `az reports report show-credential-user-registration-count`</a>

##### <a name="ParametersreportsgetCredentialUserRegistrationCount">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="reportsGetCredentialUserRegistrationDetails">Command `az reports report show-credential-user-registration-detail`</a>

##### <a name="ParametersreportsGetCredentialUserRegistrationDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--credential-user-registration-details-id**|string|key: id of credentialUserRegistrationDetails|credential_user_registration_details_id|credentialUserRegistrationDetails-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="reportsGetDailyPrintUsageSummariesByPrinter">Command `az reports report show-daily-print-usage-summary`</a>

##### <a name="ParametersreportsGetDailyPrintUsageSummariesByPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-printer-id**|string|key: id of PrintUsageSummaryByPrinter|print_usage_summary_by_printer_id|PrintUsageSummaryByPrinter-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="reportsGetDailyPrintUsageSummariesByUser">Command `az reports report show-daily-print-usage-summary`</a>

##### <a name="ParametersreportsGetDailyPrintUsageSummariesByUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-user-id**|string|key: id of PrintUsageSummaryByUser|print_usage_summary_by_user_id|PrintUsageSummaryByUser-id|

#### <a name="reportsgetEmailActivityCounts">Command `az reports report show-email-activity-count`</a>

##### <a name="ParametersreportsgetEmailActivityCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetEmailActivityUserCounts">Command `az reports report show-email-activity-user-count`</a>

##### <a name="ParametersreportsgetEmailActivityUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetEmailActivityUserDetail-ddb2">Command `az reports report show-email-activity-user-detail-ddb2`</a>

##### <a name="ParametersreportsgetEmailActivityUserDetail-ddb2">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetEmailActivityUserDetail-fe32">Command `az reports report show-email-activity-user-detail-fe32`</a>

##### <a name="ParametersreportsgetEmailActivityUserDetail-fe32">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetEmailAppUsageAppsUserCounts">Command `az reports report show-email-app-usage-app-user-count`</a>

##### <a name="ParametersreportsgetEmailAppUsageAppsUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetEmailAppUsageUserCounts">Command `az reports report show-email-app-usage-user-count`</a>

##### <a name="ParametersreportsgetEmailAppUsageUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetEmailAppUsageUserDetail-546b">Command `az reports report show-email-app-usage-user-detail546-b`</a>

##### <a name="ParametersreportsgetEmailAppUsageUserDetail-546b">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetEmailAppUsageUserDetail-62ec">Command `az reports report show-email-app-usage-user-detail62-ec`</a>

##### <a name="ParametersreportsgetEmailAppUsageUserDetail-62ec">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetEmailAppUsageVersionsUserCounts">Command `az reports report show-email-app-usage-version-user-count`</a>

##### <a name="ParametersreportsgetEmailAppUsageVersionsUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetM365AppPlatformUserCounts">Command `az reports report show-m365-app-platform-user-count`</a>

##### <a name="ParametersreportsgetM365AppPlatformUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetM365AppUserCounts">Command `az reports report show-m365-app-user-count`</a>

##### <a name="ParametersreportsgetM365AppUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetM365AppUserDetail-c8df">Command `az reports report show-m365-app-user-detail-c8-df`</a>

##### <a name="ParametersreportsgetM365AppUserDetail-c8df">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetM365AppUserDetail-2b20">Command `az reports report show-m365-app-user-detail2-b20`</a>

##### <a name="ParametersreportsgetM365AppUserDetail-2b20">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetMailboxUsageDetail">Command `az reports report show-mailbox-usage-detail`</a>

##### <a name="ParametersreportsgetMailboxUsageDetail">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetMailboxUsageMailboxCounts">Command `az reports report show-mailbox-usage-mailbox-count`</a>

##### <a name="ParametersreportsgetMailboxUsageMailboxCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetMailboxUsageQuotaStatusMailboxCounts">Command `az reports report show-mailbox-usage-quota-status-mailbox-count`</a>

##### <a name="ParametersreportsgetMailboxUsageQuotaStatusMailboxCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetMailboxUsageStorage">Command `az reports report show-mailbox-usage-storage`</a>

##### <a name="ParametersreportsgetMailboxUsageStorage">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsGetMonthlyPrintUsageSummariesByPrinter">Command `az reports report show-monthly-print-usage-summary`</a>

##### <a name="ParametersreportsGetMonthlyPrintUsageSummariesByPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-printer-id**|string|key: id of PrintUsageSummaryByPrinter|print_usage_summary_by_printer_id|PrintUsageSummaryByPrinter-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="reportsGetMonthlyPrintUsageSummariesByUser">Command `az reports report show-monthly-print-usage-summary`</a>

##### <a name="ParametersreportsGetMonthlyPrintUsageSummariesByUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-user-id**|string|key: id of PrintUsageSummaryByUser|print_usage_summary_by_user_id|PrintUsageSummaryByUser-id|

#### <a name="reportsgetOffice365ActivationCounts">Command `az reports report show-office365-activation-count`</a>

##### <a name="ParametersreportsgetOffice365ActivationCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="reportsgetOffice365ActivationsUserCounts">Command `az reports report show-office365-activation-user-count`</a>

##### <a name="ParametersreportsgetOffice365ActivationsUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="reportsgetOffice365ActivationsUserDetail">Command `az reports report show-office365-activation-user-detail`</a>

##### <a name="ParametersreportsgetOffice365ActivationsUserDetail">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="reportsgetOffice365ActiveUserCounts">Command `az reports report show-office365-active-user-count`</a>

##### <a name="ParametersreportsgetOffice365ActiveUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetOffice365ActiveUserDetail-d389">Command `az reports report show-office365-active-user-detail-d389`</a>

##### <a name="ParametersreportsgetOffice365ActiveUserDetail-d389">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetOffice365ActiveUserDetail-68ad">Command `az reports report show-office365-active-user-detail68-ad`</a>

##### <a name="ParametersreportsgetOffice365ActiveUserDetail-68ad">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetOffice365GroupsActivityCounts">Command `az reports report show-office365-group-activity-count`</a>

##### <a name="ParametersreportsgetOffice365GroupsActivityCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetOffice365GroupsActivityDetail-38f6">Command `az reports report show-office365-group-activity-detail38-f6`</a>

##### <a name="ParametersreportsgetOffice365GroupsActivityDetail-38f6">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetOffice365GroupsActivityDetail-81cc">Command `az reports report show-office365-group-activity-detail81-cc`</a>

##### <a name="ParametersreportsgetOffice365GroupsActivityDetail-81cc">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetOffice365GroupsActivityFileCounts">Command `az reports report show-office365-group-activity-file-count`</a>

##### <a name="ParametersreportsgetOffice365GroupsActivityFileCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetOffice365GroupsActivityGroupCounts">Command `az reports report show-office365-group-activity-group-count`</a>

##### <a name="ParametersreportsgetOffice365GroupsActivityGroupCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetOffice365GroupsActivityStorage">Command `az reports report show-office365-group-activity-storage`</a>

##### <a name="ParametersreportsgetOffice365GroupsActivityStorage">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetOffice365ServicesUserCounts">Command `az reports report show-office365-service-user-count`</a>

##### <a name="ParametersreportsgetOffice365ServicesUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetOneDriveActivityFileCounts">Command `az reports report show-one-drive-activity-file-count`</a>

##### <a name="ParametersreportsgetOneDriveActivityFileCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetOneDriveActivityUserCounts">Command `az reports report show-one-drive-activity-user-count`</a>

##### <a name="ParametersreportsgetOneDriveActivityUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetOneDriveActivityUserDetail-c424">Command `az reports report show-one-drive-activity-user-detail-c424`</a>

##### <a name="ParametersreportsgetOneDriveActivityUserDetail-c424">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetOneDriveActivityUserDetail-05f1">Command `az reports report show-one-drive-activity-user-detail05-f1`</a>

##### <a name="ParametersreportsgetOneDriveActivityUserDetail-05f1">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetOneDriveUsageAccountCounts">Command `az reports report show-one-drive-usage-account-count`</a>

##### <a name="ParametersreportsgetOneDriveUsageAccountCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetOneDriveUsageAccountDetail-dd7f">Command `az reports report show-one-drive-usage-account-detail-dd7-f`</a>

##### <a name="ParametersreportsgetOneDriveUsageAccountDetail-dd7f">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetOneDriveUsageAccountDetail-e827">Command `az reports report show-one-drive-usage-account-detail-e827`</a>

##### <a name="ParametersreportsgetOneDriveUsageAccountDetail-e827">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetOneDriveUsageFileCounts">Command `az reports report show-one-drive-usage-file-count`</a>

##### <a name="ParametersreportsgetOneDriveUsageFileCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetOneDriveUsageStorage">Command `az reports report show-one-drive-usage-storage`</a>

##### <a name="ParametersreportsgetOneDriveUsageStorage">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetRelyingPartyDetailedSummary">Command `az reports report show-relying-party-detailed-summary`</a>

##### <a name="ParametersreportsgetRelyingPartyDetailedSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSharePointActivityFileCounts">Command `az reports report show-share-point-activity-file-count`</a>

##### <a name="ParametersreportsgetSharePointActivityFileCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSharePointActivityPages">Command `az reports report show-share-point-activity-page`</a>

##### <a name="ParametersreportsgetSharePointActivityPages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSharePointActivityUserCounts">Command `az reports report show-share-point-activity-user-count`</a>

##### <a name="ParametersreportsgetSharePointActivityUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSharePointActivityUserDetail-b778">Command `az reports report show-share-point-activity-user-detail-b778`</a>

##### <a name="ParametersreportsgetSharePointActivityUserDetail-b778">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSharePointActivityUserDetail-f3be">Command `az reports report show-share-point-activity-user-detail-f3-be`</a>

##### <a name="ParametersreportsgetSharePointActivityUserDetail-f3be">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetSharePointSiteUsageDetail-d27a">Command `az reports report show-share-point-site-usage-detail-d27-a`</a>

##### <a name="ParametersreportsgetSharePointSiteUsageDetail-d27a">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetSharePointSiteUsageDetail-204b">Command `az reports report show-share-point-site-usage-detail204-b`</a>

##### <a name="ParametersreportsgetSharePointSiteUsageDetail-204b">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSharePointSiteUsageFileCounts">Command `az reports report show-share-point-site-usage-file-count`</a>

##### <a name="ParametersreportsgetSharePointSiteUsageFileCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSharePointSiteUsagePages">Command `az reports report show-share-point-site-usage-page`</a>

##### <a name="ParametersreportsgetSharePointSiteUsagePages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSharePointSiteUsageSiteCounts">Command `az reports report show-share-point-site-usage-site-count`</a>

##### <a name="ParametersreportsgetSharePointSiteUsageSiteCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSharePointSiteUsageStorage">Command `az reports report show-share-point-site-usage-storage`</a>

##### <a name="ParametersreportsgetSharePointSiteUsageStorage">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSkypeForBusinessActivityCounts">Command `az reports report show-skype-for-business-activity-count`</a>

##### <a name="ParametersreportsgetSkypeForBusinessActivityCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSkypeForBusinessActivityUserCounts">Command `az reports report show-skype-for-business-activity-user-count`</a>

##### <a name="ParametersreportsgetSkypeForBusinessActivityUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSkypeForBusinessActivityUserDetail-e4c9">Command `az reports report show-skype-for-business-activity-user-detail-e4-c9`</a>

##### <a name="ParametersreportsgetSkypeForBusinessActivityUserDetail-e4c9">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetSkypeForBusinessActivityUserDetail-744e">Command `az reports report show-skype-for-business-activity-user-detail744-e`</a>

##### <a name="ParametersreportsgetSkypeForBusinessActivityUserDetail-744e">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSkypeForBusinessDeviceUsageDistributionUserCounts">Command `az reports report show-skype-for-business-device-usage-distribution-user-count`</a>

##### <a name="ParametersreportsgetSkypeForBusinessDeviceUsageDistributionUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSkypeForBusinessDeviceUsageUserCounts">Command `az reports report show-skype-for-business-device-usage-user-count`</a>

##### <a name="ParametersreportsgetSkypeForBusinessDeviceUsageUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSkypeForBusinessDeviceUsageUserDetail-a692">Command `az reports report show-skype-for-business-device-usage-user-detail-a692`</a>

##### <a name="ParametersreportsgetSkypeForBusinessDeviceUsageUserDetail-a692">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetSkypeForBusinessDeviceUsageUserDetail-e753">Command `az reports report show-skype-for-business-device-usage-user-detail-e753`</a>

##### <a name="ParametersreportsgetSkypeForBusinessDeviceUsageUserDetail-e753">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSkypeForBusinessOrganizerActivityCounts">Command `az reports report show-skype-for-business-organizer-activity-count`</a>

##### <a name="ParametersreportsgetSkypeForBusinessOrganizerActivityCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSkypeForBusinessOrganizerActivityMinuteCounts">Command `az reports report show-skype-for-business-organizer-activity-minute-count`</a>

##### <a name="ParametersreportsgetSkypeForBusinessOrganizerActivityMinuteCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSkypeForBusinessOrganizerActivityUserCounts">Command `az reports report show-skype-for-business-organizer-activity-user-count`</a>

##### <a name="ParametersreportsgetSkypeForBusinessOrganizerActivityUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSkypeForBusinessParticipantActivityCounts">Command `az reports report show-skype-for-business-participant-activity-count`</a>

##### <a name="ParametersreportsgetSkypeForBusinessParticipantActivityCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSkypeForBusinessParticipantActivityMinuteCounts">Command `az reports report show-skype-for-business-participant-activity-minute-count`</a>

##### <a name="ParametersreportsgetSkypeForBusinessParticipantActivityMinuteCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSkypeForBusinessParticipantActivityUserCounts">Command `az reports report show-skype-for-business-participant-activity-user-count`</a>

##### <a name="ParametersreportsgetSkypeForBusinessParticipantActivityUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSkypeForBusinessPeerToPeerActivityCounts">Command `az reports report show-skype-for-business-peer-to-peer-activity-count`</a>

##### <a name="ParametersreportsgetSkypeForBusinessPeerToPeerActivityCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSkypeForBusinessPeerToPeerActivityMinuteCounts">Command `az reports report show-skype-for-business-peer-to-peer-activity-minute-count`</a>

##### <a name="ParametersreportsgetSkypeForBusinessPeerToPeerActivityMinuteCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetSkypeForBusinessPeerToPeerActivityUserCounts">Command `az reports report show-skype-for-business-peer-to-peer-activity-user-count`</a>

##### <a name="ParametersreportsgetSkypeForBusinessPeerToPeerActivityUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetTeamsDeviceUsageDistributionUserCounts">Command `az reports report show-team-device-usage-distribution-user-count`</a>

##### <a name="ParametersreportsgetTeamsDeviceUsageDistributionUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetTeamsDeviceUsageUserCounts">Command `az reports report show-team-device-usage-user-count`</a>

##### <a name="ParametersreportsgetTeamsDeviceUsageUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetTeamsDeviceUsageUserDetail-7148">Command `az reports report show-team-device-usage-user-detail7148`</a>

##### <a name="ParametersreportsgetTeamsDeviceUsageUserDetail-7148">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetTeamsDeviceUsageUserDetail-7565">Command `az reports report show-team-device-usage-user-detail7565`</a>

##### <a name="ParametersreportsgetTeamsDeviceUsageUserDetail-7565">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetTeamsUserActivityCounts">Command `az reports report show-team-user-activity-count`</a>

##### <a name="ParametersreportsgetTeamsUserActivityCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetTeamsUserActivityUserCounts">Command `az reports report show-team-user-activity-user-count`</a>

##### <a name="ParametersreportsgetTeamsUserActivityUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetTeamsUserActivityUserDetail-a3f1">Command `az reports report show-team-user-activity-user-detail-a3-f1`</a>

##### <a name="ParametersreportsgetTeamsUserActivityUserDetail-a3f1">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetTeamsUserActivityUserDetail-eb13">Command `az reports report show-team-user-activity-user-detail-eb13`</a>

##### <a name="ParametersreportsgetTeamsUserActivityUserDetail-eb13">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetTenantSecureScores">Command `az reports report show-tenant-secure-score`</a>

##### <a name="ParametersreportsgetTenantSecureScores">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|integer||period|period|

#### <a name="reportsGetUserCredentialUsageDetails">Command `az reports report show-user-credential-usage-detail`</a>

##### <a name="ParametersreportsGetUserCredentialUsageDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-credential-usage-details-id**|string|key: id of userCredentialUsageDetails|user_credential_usage_details_id|userCredentialUsageDetails-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="reportsgetYammerActivityCounts">Command `az reports report show-yammer-activity-count`</a>

##### <a name="ParametersreportsgetYammerActivityCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetYammerActivityUserCounts">Command `az reports report show-yammer-activity-user-count`</a>

##### <a name="ParametersreportsgetYammerActivityUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetYammerActivityUserDetail-ac30">Command `az reports report show-yammer-activity-user-detail-ac30`</a>

##### <a name="ParametersreportsgetYammerActivityUserDetail-ac30">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetYammerActivityUserDetail-15a5">Command `az reports report show-yammer-activity-user-detail15-a5`</a>

##### <a name="ParametersreportsgetYammerActivityUserDetail-15a5">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetYammerDeviceUsageDistributionUserCounts">Command `az reports report show-yammer-device-usage-distribution-user-count`</a>

##### <a name="ParametersreportsgetYammerDeviceUsageDistributionUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetYammerDeviceUsageUserCounts">Command `az reports report show-yammer-device-usage-user-count`</a>

##### <a name="ParametersreportsgetYammerDeviceUsageUserCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetYammerDeviceUsageUserDetail-cfad">Command `az reports report show-yammer-device-usage-user-detail-cfad`</a>

##### <a name="ParametersreportsgetYammerDeviceUsageUserDetail-cfad">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetYammerDeviceUsageUserDetail-d0ac">Command `az reports report show-yammer-device-usage-user-detail-d0-ac`</a>

##### <a name="ParametersreportsgetYammerDeviceUsageUserDetail-d0ac">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetYammerGroupsActivityCounts">Command `az reports report show-yammer-group-activity-count`</a>

##### <a name="ParametersreportsgetYammerGroupsActivityCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetYammerGroupsActivityDetail-da9a">Command `az reports report show-yammer-group-activity-detail-da9-a`</a>

##### <a name="ParametersreportsgetYammerGroupsActivityDetail-da9a">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

#### <a name="reportsgetYammerGroupsActivityDetail-0d7d">Command `az reports report show-yammer-group-activity-detail0-d7-d`</a>

##### <a name="ParametersreportsgetYammerGroupsActivityDetail-0d7d">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsgetYammerGroupsActivityGroupCounts">Command `az reports report show-yammer-group-activity-group-count`</a>

##### <a name="ParametersreportsgetYammerGroupsActivityGroupCounts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

#### <a name="reportsUpdateApplicationSignInDetailedSummary">Command `az reports report update-application-sign-in-detailed-summary`</a>

##### <a name="ParametersreportsUpdateApplicationSignInDetailedSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-sign-in-detailed-summary-id**|string|key: id of applicationSignInDetailedSummary|application_sign_in_detailed_summary_id|applicationSignInDetailedSummary-id|
|**--id**|string|Read-only.|id|id|
|**--aggregated-event-date-time**|date-time||aggregated_event_date_time|aggregatedEventDateTime|
|**--app-display-name**|string||app_display_name|appDisplayName|
|**--app-id**|string||app_id|appId|
|**--sign-in-count**|integer||sign_in_count|signInCount|
|**--status**|object|signInStatus|status|status|

#### <a name="reportsUpdateCredentialUserRegistrationDetails">Command `az reports report update-credential-user-registration-detail`</a>

##### <a name="ParametersreportsUpdateCredentialUserRegistrationDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--credential-user-registration-details-id**|string|key: id of credentialUserRegistrationDetails|credential_user_registration_details_id|credentialUserRegistrationDetails-id|
|**--id**|string|Read-only.|id|id|
|**--auth-methods**|array||auth_methods|authMethods|
|**--is-capable**|boolean||is_capable|isCapable|
|**--is-enabled**|boolean||is_enabled|isEnabled|
|**--is-mfa-registered**|boolean||is_mfa_registered|isMfaRegistered|
|**--is-registered**|boolean||is_registered|isRegistered|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

#### <a name="reportsUpdateDailyPrintUsageSummariesByPrinter">Command `az reports report update-daily-print-usage-summary-by-printer`</a>

##### <a name="ParametersreportsUpdateDailyPrintUsageSummariesByPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-printer-id**|string|key: id of PrintUsageSummaryByPrinter|print_usage_summary_by_printer_id|PrintUsageSummaryByPrinter-id|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--printer-id**|string||printer_id|printerId|
|**--usage-date**|date||usage_date|usageDate|

#### <a name="reportsUpdateDailyPrintUsageSummariesByUser">Command `az reports report update-daily-print-usage-summary-by-user`</a>

##### <a name="ParametersreportsUpdateDailyPrintUsageSummariesByUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-user-id**|string|key: id of PrintUsageSummaryByUser|print_usage_summary_by_user_id|PrintUsageSummaryByUser-id|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--usage-date**|date||usage_date|usageDate|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

#### <a name="reportsUpdateMonthlyPrintUsageSummariesByPrinter">Command `az reports report update-monthly-print-usage-summary-by-printer`</a>

##### <a name="ParametersreportsUpdateMonthlyPrintUsageSummariesByPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-printer-id**|string|key: id of PrintUsageSummaryByPrinter|print_usage_summary_by_printer_id|PrintUsageSummaryByPrinter-id|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--printer-id**|string||printer_id|printerId|
|**--usage-date**|date||usage_date|usageDate|

#### <a name="reportsUpdateMonthlyPrintUsageSummariesByUser">Command `az reports report update-monthly-print-usage-summary-by-user`</a>

##### <a name="ParametersreportsUpdateMonthlyPrintUsageSummariesByUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-user-id**|string|key: id of PrintUsageSummaryByUser|print_usage_summary_by_user_id|PrintUsageSummaryByUser-id|
|**--id**|string|Read-only.|id|id|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|
|**--usage-date**|date||usage_date|usageDate|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

#### <a name="reportsUpdateUserCredentialUsageDetails">Command `az reports report update-user-credential-usage-detail`</a>

##### <a name="ParametersreportsUpdateUserCredentialUsageDetails">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-credential-usage-details-id**|string|key: id of userCredentialUsageDetails|user_credential_usage_details_id|userCredentialUsageDetails-id|
|**--id**|string|Read-only.|id|id|
|**--auth-method**|choice||auth_method|authMethod|
|**--event-date-time**|date-time||event_date_time|eventDateTime|
|**--failure-reason**|string||failure_reason|failureReason|
|**--feature**|choice||feature|feature|
|**--is-success**|boolean||is_success|isSuccess|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### group `az reports report-report-root`
#### <a name="reports.reportRootGetReportRoot">Command `az reports report-report-root show-report-root`</a>

##### <a name="Parametersreports.reportRootGetReportRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="reports.reportRootUpdateReportRoot">Command `az reports report-report-root update-report-root`</a>

##### <a name="Parametersreports.reportRootUpdateReportRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--application-sign-in-detailed-summary**|array||application_sign_in_detailed_summary|applicationSignInDetailedSummary|
|**--credential-user-registration-details**|array||credential_user_registration_details|credentialUserRegistrationDetails|
|**--user-credential-usage-details**|array||user_credential_usage_details|userCredentialUsageDetails|
|**--daily-print-usage-summaries-by-printer**|array||daily_print_usage_summaries_by_printer|dailyPrintUsageSummariesByPrinter|
|**--daily-print-usage-summaries-by-user**|array||daily_print_usage_summaries_by_user|dailyPrintUsageSummariesByUser|
|**--monthly-print-usage-summaries-by-printer**|array||monthly_print_usage_summaries_by_printer|monthlyPrintUsageSummariesByPrinter|
|**--monthly-print-usage-summaries-by-user**|array||monthly_print_usage_summaries_by_user|monthlyPrintUsageSummariesByUser|
