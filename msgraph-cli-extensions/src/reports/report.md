# Azure CLI Module Creation Report

### reports create-application-sign-in-detailed-summary

create-application-sign-in-detailed-summary a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-application-sign-in-detailed-summary|CreateApplicationSignInDetailedSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--app-id**|string||app_id|appId|
|**--app-display-name**|string||app_display_name|appDisplayName|
|**--sign-in-count**|integer||sign_in_count|signInCount|
|**--aggregated-event-date-time**|date-time||aggregated_event_date_time|aggregatedEventDateTime|
|**--status-error-code**|integer|Provides the 5-6digit error code that's generated during a sign-in failure. Check out the list of error codes and messages.|error_code|errorCode|
|**--status-failure-reason**|string|Provides the error message or the reason for failure for the corresponding sign-in activity. Check out the list of error codes and messages.|failure_reason|failureReason|
|**--status-additional-details**|string|Provides additional details on the sign-in activity|additional_details|additionalDetails|

### reports create-credential-user-registration-detail

create-credential-user-registration-detail a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-credential-user-registration-detail|CreateCredentialUserRegistrationDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--auth-methods**|array||auth_methods|authMethods|
|**--is-registered**|boolean||is_registered|isRegistered|
|**--is-enabled**|boolean||is_enabled|isEnabled|
|**--is-capable**|boolean||is_capable|isCapable|
|**--is-mfa-registered**|boolean||is_mfa_registered|isMfaRegistered|

### reports create-daily-print-usage-summary-by-printer

create-daily-print-usage-summary-by-printer a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-daily-print-usage-summary-by-printer|CreateDailyPrintUsageSummariesByPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--printer-id**|string||printer_id|printerId|
|**--usage-date**|date||usage_date|usageDate|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|

### reports create-daily-print-usage-summary-by-user

create-daily-print-usage-summary-by-user a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-daily-print-usage-summary-by-user|CreateDailyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--usage-date**|date||usage_date|usageDate|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|

### reports create-monthly-print-usage-summary-by-printer

create-monthly-print-usage-summary-by-printer a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-monthly-print-usage-summary-by-printer|CreateMonthlyPrintUsageSummariesByPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--printer-id**|string||printer_id|printerId|
|**--usage-date**|date||usage_date|usageDate|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|

### reports create-monthly-print-usage-summary-by-user

create-monthly-print-usage-summary-by-user a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-monthly-print-usage-summary-by-user|CreateMonthlyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--usage-date**|date||usage_date|usageDate|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|

### reports create-user-credential-usage-detail

create-user-credential-usage-detail a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-user-credential-usage-detail|CreateUserCredentialUsageDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--feature**|choice||feature|feature|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--is-success**|boolean||is_success|isSuccess|
|**--auth-method**|choice||auth_method|authMethod|
|**--failure-reason**|string||failure_reason|failureReason|
|**--event-date-time**|date-time||event_date_time|eventDateTime|

### reports device-configuration-device-activity

device-configuration-device-activity a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|device-configuration-device-activity|deviceConfigurationDeviceActivity|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports device-configuration-user-activity

device-configuration-user-activity a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|device-configuration-user-activity|deviceConfigurationUserActivity|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports get-application-sign-in-detailed-summary

get-application-sign-in-detailed-summary a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-application-sign-in-detailed-summary|GetApplicationSignInDetailedSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-sign-in-detailed-summary-id**|string|key: applicationSignInDetailedSummary-id of applicationSignInDetailedSummary|application_sign_in_detailed_summary_id|applicationSignInDetailedSummary-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports get-azure-ad-application-sign-in-summary

get-azure-ad-application-sign-in-summary a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-azure-ad-application-sign-in-summary|getAzureADApplicationSignInSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-azure-ad-feature-usage

get-azure-ad-feature-usage a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-azure-ad-feature-usage|getAzureADFeatureUsage|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-azure-ad-license-usage

get-azure-ad-license-usage a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-azure-ad-license-usage|getAzureADLicenseUsage|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-azure-ad-user-feature-usage

get-azure-ad-user-feature-usage a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-azure-ad-user-feature-usage|getAzureADUserFeatureUsage|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports get-credential-usage-summary

get-credential-usage-summary a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-credential-usage-summary|getCredentialUsageSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-credential-user-registration-count

get-credential-user-registration-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-credential-user-registration-count|getCredentialUserRegistrationCount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports get-credential-user-registration-detail

get-credential-user-registration-detail a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-credential-user-registration-detail|GetCredentialUserRegistrationDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--credential-user-registration-details-id**|string|key: credentialUserRegistrationDetails-id of credentialUserRegistrationDetails|credential_user_registration_details_id|credentialUserRegistrationDetails-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports get-daily-print-usage-summary-by-printer

get-daily-print-usage-summary-by-printer a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-daily-print-usage-summary-by-printer|GetDailyPrintUsageSummariesByPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-printer-id**|string|key: PrintUsageSummaryByPrinter-id of PrintUsageSummaryByPrinter|print_usage_summary_by_printer_id|PrintUsageSummaryByPrinter-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports get-daily-print-usage-summary-by-user

get-daily-print-usage-summary-by-user a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-daily-print-usage-summary-by-user|GetDailyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-user-id**|string|key: PrintUsageSummaryByUser-id of PrintUsageSummaryByUser|print_usage_summary_by_user_id|PrintUsageSummaryByUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports get-email-activity-count

get-email-activity-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-activity-count|getEmailActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-email-activity-user-count

get-email-activity-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-activity-user-count|getEmailActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-email-activity-user-detail-ddb2

get-email-activity-user-detail-ddb2 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-activity-user-detail-ddb2|getEmailActivityUserDetail-ddb2|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-email-activity-user-detail-fe32

get-email-activity-user-detail-fe32 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-activity-user-detail-fe32|getEmailActivityUserDetail-fe32|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports get-email-app-usage-app-user-count

get-email-app-usage-app-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-app-usage-app-user-count|getEmailAppUsageAppsUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-email-app-usage-user-count

get-email-app-usage-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-app-usage-user-count|getEmailAppUsageUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-email-app-usage-user-detail546-b

get-email-app-usage-user-detail546-b a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-app-usage-user-detail546-b|getEmailAppUsageUserDetail-546b|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-email-app-usage-user-detail62-ec

get-email-app-usage-user-detail62-ec a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-app-usage-user-detail62-ec|getEmailAppUsageUserDetail-62ec|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports get-email-app-usage-version-user-count

get-email-app-usage-version-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-email-app-usage-version-user-count|getEmailAppUsageVersionsUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-mailbox-usage-detail

get-mailbox-usage-detail a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mailbox-usage-detail|getMailboxUsageDetail|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-mailbox-usage-mailbox-count

get-mailbox-usage-mailbox-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mailbox-usage-mailbox-count|getMailboxUsageMailboxCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-mailbox-usage-quota-status-mailbox-count

get-mailbox-usage-quota-status-mailbox-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mailbox-usage-quota-status-mailbox-count|getMailboxUsageQuotaStatusMailboxCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-mailbox-usage-storage

get-mailbox-usage-storage a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mailbox-usage-storage|getMailboxUsageStorage|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-monthly-print-usage-summary-by-printer

get-monthly-print-usage-summary-by-printer a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-monthly-print-usage-summary-by-printer|GetMonthlyPrintUsageSummariesByPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-printer-id**|string|key: PrintUsageSummaryByPrinter-id of PrintUsageSummaryByPrinter|print_usage_summary_by_printer_id|PrintUsageSummaryByPrinter-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports get-monthly-print-usage-summary-by-user

get-monthly-print-usage-summary-by-user a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-monthly-print-usage-summary-by-user|GetMonthlyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-user-id**|string|key: PrintUsageSummaryByUser-id of PrintUsageSummaryByUser|print_usage_summary_by_user_id|PrintUsageSummaryByUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports get-office365-activation-count

get-office365-activation-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-activation-count|getOffice365ActivationCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports get-office365-activation-user-count

get-office365-activation-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-activation-user-count|getOffice365ActivationsUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports get-office365-activation-user-detail

get-office365-activation-user-detail a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-activation-user-detail|getOffice365ActivationsUserDetail|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports get-office365-active-user-count

get-office365-active-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-active-user-count|getOffice365ActiveUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-office365-active-user-detail-d389

get-office365-active-user-detail-d389 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-active-user-detail-d389|getOffice365ActiveUserDetail-d389|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports get-office365-active-user-detail68-ad

get-office365-active-user-detail68-ad a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-active-user-detail68-ad|getOffice365ActiveUserDetail-68ad|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-office365-group-activity-count

get-office365-group-activity-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-group-activity-count|getOffice365GroupsActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-office365-group-activity-detail38-f6

get-office365-group-activity-detail38-f6 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-group-activity-detail38-f6|getOffice365GroupsActivityDetail-38f6|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-office365-group-activity-detail81-cc

get-office365-group-activity-detail81-cc a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-group-activity-detail81-cc|getOffice365GroupsActivityDetail-81cc|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports get-office365-group-activity-file-count

get-office365-group-activity-file-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-group-activity-file-count|getOffice365GroupsActivityFileCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-office365-group-activity-group-count

get-office365-group-activity-group-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-group-activity-group-count|getOffice365GroupsActivityGroupCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-office365-group-activity-storage

get-office365-group-activity-storage a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-group-activity-storage|getOffice365GroupsActivityStorage|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-office365-service-user-count

get-office365-service-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-office365-service-user-count|getOffice365ServicesUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-one-drive-activity-file-count

get-one-drive-activity-file-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-activity-file-count|getOneDriveActivityFileCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-one-drive-activity-user-count

get-one-drive-activity-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-activity-user-count|getOneDriveActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-one-drive-activity-user-detail-c424

get-one-drive-activity-user-detail-c424 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-activity-user-detail-c424|getOneDriveActivityUserDetail-c424|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-one-drive-activity-user-detail05-f1

get-one-drive-activity-user-detail05-f1 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-activity-user-detail05-f1|getOneDriveActivityUserDetail-05f1|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports get-one-drive-usage-account-count

get-one-drive-usage-account-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-usage-account-count|getOneDriveUsageAccountCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-one-drive-usage-account-detail-dd7-f

get-one-drive-usage-account-detail-dd7-f a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-usage-account-detail-dd7-f|getOneDriveUsageAccountDetail-dd7f|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-one-drive-usage-account-detail-e827

get-one-drive-usage-account-detail-e827 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-usage-account-detail-e827|getOneDriveUsageAccountDetail-e827|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports get-one-drive-usage-file-count

get-one-drive-usage-file-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-usage-file-count|getOneDriveUsageFileCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-one-drive-usage-storage

get-one-drive-usage-storage a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-one-drive-usage-storage|getOneDriveUsageStorage|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-relying-party-detailed-summary

get-relying-party-detailed-summary a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-relying-party-detailed-summary|getRelyingPartyDetailedSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-report-root

get-report-root a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports.reportRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-report-root|GetReportRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports get-share-point-activity-file-count

get-share-point-activity-file-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-activity-file-count|getSharePointActivityFileCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-share-point-activity-page

get-share-point-activity-page a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-activity-page|getSharePointActivityPages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-share-point-activity-user-count

get-share-point-activity-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-activity-user-count|getSharePointActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-share-point-activity-user-detail-b778

get-share-point-activity-user-detail-b778 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-activity-user-detail-b778|getSharePointActivityUserDetail-b778|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-share-point-activity-user-detail-f3-be

get-share-point-activity-user-detail-f3-be a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-activity-user-detail-f3-be|getSharePointActivityUserDetail-f3be|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports get-share-point-site-usage-detail-d27-a

get-share-point-site-usage-detail-d27-a a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-site-usage-detail-d27-a|getSharePointSiteUsageDetail-d27a|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports get-share-point-site-usage-detail204-b

get-share-point-site-usage-detail204-b a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-site-usage-detail204-b|getSharePointSiteUsageDetail-204b|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-share-point-site-usage-file-count

get-share-point-site-usage-file-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-site-usage-file-count|getSharePointSiteUsageFileCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-share-point-site-usage-page

get-share-point-site-usage-page a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-site-usage-page|getSharePointSiteUsagePages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-share-point-site-usage-site-count

get-share-point-site-usage-site-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-site-usage-site-count|getSharePointSiteUsageSiteCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-share-point-site-usage-storage

get-share-point-site-usage-storage a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share-point-site-usage-storage|getSharePointSiteUsageStorage|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-skype-for-business-activity-count

get-skype-for-business-activity-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-activity-count|getSkypeForBusinessActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-skype-for-business-activity-user-count

get-skype-for-business-activity-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-activity-user-count|getSkypeForBusinessActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-skype-for-business-activity-user-detail-e4-c9

get-skype-for-business-activity-user-detail-e4-c9 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-activity-user-detail-e4-c9|getSkypeForBusinessActivityUserDetail-e4c9|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports get-skype-for-business-activity-user-detail744-e

get-skype-for-business-activity-user-detail744-e a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-activity-user-detail744-e|getSkypeForBusinessActivityUserDetail-744e|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-skype-for-business-device-usage-distribution-user-count

get-skype-for-business-device-usage-distribution-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-device-usage-distribution-user-count|getSkypeForBusinessDeviceUsageDistributionUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-skype-for-business-device-usage-user-count

get-skype-for-business-device-usage-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-device-usage-user-count|getSkypeForBusinessDeviceUsageUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-skype-for-business-device-usage-user-detail-a692

get-skype-for-business-device-usage-user-detail-a692 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-device-usage-user-detail-a692|getSkypeForBusinessDeviceUsageUserDetail-a692|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports get-skype-for-business-device-usage-user-detail-e753

get-skype-for-business-device-usage-user-detail-e753 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-device-usage-user-detail-e753|getSkypeForBusinessDeviceUsageUserDetail-e753|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-skype-for-business-organizer-activity-count

get-skype-for-business-organizer-activity-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-organizer-activity-count|getSkypeForBusinessOrganizerActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-skype-for-business-organizer-activity-minute-count

get-skype-for-business-organizer-activity-minute-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-organizer-activity-minute-count|getSkypeForBusinessOrganizerActivityMinuteCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-skype-for-business-organizer-activity-user-count

get-skype-for-business-organizer-activity-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-organizer-activity-user-count|getSkypeForBusinessOrganizerActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-skype-for-business-participant-activity-count

get-skype-for-business-participant-activity-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-participant-activity-count|getSkypeForBusinessParticipantActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-skype-for-business-participant-activity-minute-count

get-skype-for-business-participant-activity-minute-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-participant-activity-minute-count|getSkypeForBusinessParticipantActivityMinuteCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-skype-for-business-participant-activity-user-count

get-skype-for-business-participant-activity-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-participant-activity-user-count|getSkypeForBusinessParticipantActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-skype-for-business-peer-to-peer-activity-count

get-skype-for-business-peer-to-peer-activity-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-peer-to-peer-activity-count|getSkypeForBusinessPeerToPeerActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-skype-for-business-peer-to-peer-activity-minute-count

get-skype-for-business-peer-to-peer-activity-minute-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-peer-to-peer-activity-minute-count|getSkypeForBusinessPeerToPeerActivityMinuteCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-skype-for-business-peer-to-peer-activity-user-count

get-skype-for-business-peer-to-peer-activity-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-skype-for-business-peer-to-peer-activity-user-count|getSkypeForBusinessPeerToPeerActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-team-device-usage-distribution-user-count

get-team-device-usage-distribution-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-device-usage-distribution-user-count|getTeamsDeviceUsageDistributionUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-team-device-usage-user-count

get-team-device-usage-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-device-usage-user-count|getTeamsDeviceUsageUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-team-device-usage-user-detail7148

get-team-device-usage-user-detail7148 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-device-usage-user-detail7148|getTeamsDeviceUsageUserDetail-7148|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports get-team-device-usage-user-detail7565

get-team-device-usage-user-detail7565 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-device-usage-user-detail7565|getTeamsDeviceUsageUserDetail-7565|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-team-user-activity-count

get-team-user-activity-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-user-activity-count|getTeamsUserActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-team-user-activity-user-count

get-team-user-activity-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-user-activity-user-count|getTeamsUserActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-team-user-activity-user-detail-a3-f1

get-team-user-activity-user-detail-a3-f1 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-user-activity-user-detail-a3-f1|getTeamsUserActivityUserDetail-a3f1|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports get-team-user-activity-user-detail-eb13

get-team-user-activity-user-detail-eb13 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-team-user-activity-user-detail-eb13|getTeamsUserActivityUserDetail-eb13|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-tenant-secure-score

get-tenant-secure-score a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-tenant-secure-score|getTenantSecureScores|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|integer||period|period|

### reports get-user-credential-usage-detail

get-user-credential-usage-detail a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-credential-usage-detail|GetUserCredentialUsageDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-credential-usage-details-id**|string|key: userCredentialUsageDetails-id of userCredentialUsageDetails|user_credential_usage_details_id|userCredentialUsageDetails-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports get-yammer-activity-count

get-yammer-activity-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-activity-count|getYammerActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-yammer-activity-user-count

get-yammer-activity-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-activity-user-count|getYammerActivityUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-yammer-activity-user-detail-ac30

get-yammer-activity-user-detail-ac30 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-activity-user-detail-ac30|getYammerActivityUserDetail-ac30|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports get-yammer-activity-user-detail15-a5

get-yammer-activity-user-detail15-a5 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-activity-user-detail15-a5|getYammerActivityUserDetail-15a5|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-yammer-device-usage-distribution-user-count

get-yammer-device-usage-distribution-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-device-usage-distribution-user-count|getYammerDeviceUsageDistributionUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-yammer-device-usage-user-count

get-yammer-device-usage-user-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-device-usage-user-count|getYammerDeviceUsageUserCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-yammer-device-usage-user-detail-cfad

get-yammer-device-usage-user-detail-cfad a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-device-usage-user-detail-cfad|getYammerDeviceUsageUserDetail-cfad|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-yammer-device-usage-user-detail-d0-ac

get-yammer-device-usage-user-detail-d0-ac a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-device-usage-user-detail-d0-ac|getYammerDeviceUsageUserDetail-d0ac|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports get-yammer-group-activity-count

get-yammer-group-activity-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-group-activity-count|getYammerGroupsActivityCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-yammer-group-activity-detail-da9-a

get-yammer-group-activity-detail-da9-a a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-group-activity-detail-da9-a|getYammerGroupsActivityDetail-da9a|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--date**|date||date|date|

### reports get-yammer-group-activity-detail0-d7-d

get-yammer-group-activity-detail0-d7-d a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-group-activity-detail0-d7-d|getYammerGroupsActivityDetail-0d7d|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports get-yammer-group-activity-group-count

get-yammer-group-activity-group-count a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-yammer-group-activity-group-count|getYammerGroupsActivityGroupCounts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports list-application-sign-in-detailed-summary

list-application-sign-in-detailed-summary a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-application-sign-in-detailed-summary|ListApplicationSignInDetailedSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports list-credential-user-registration-detail

list-credential-user-registration-detail a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-credential-user-registration-detail|ListCredentialUserRegistrationDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports list-daily-print-usage-summary

list-daily-print-usage-summary a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-daily-print-usage-summary|ListDailyPrintUsageSummariesByPrinter|
|list-daily-print-usage-summary|ListDailyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports list-monthly-print-usage-summary

list-monthly-print-usage-summary a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-monthly-print-usage-summary|ListMonthlyPrintUsageSummariesByPrinter|
|list-monthly-print-usage-summary|ListMonthlyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports list-user-credential-usage-detail

list-user-credential-usage-detail a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-user-credential-usage-detail|ListUserCredentialUsageDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### reports managed-device-enrollment-abandonment-detail

managed-device-enrollment-abandonment-detail a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|managed-device-enrollment-abandonment-detail|managedDeviceEnrollmentAbandonmentDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--skip**|integer||skip|skip|
|**--top**|integer||top|top|
|**--filter**|string||filter|filter|
|**--skip-token**|string||skip_token|skipToken|

### reports managed-device-enrollment-abandonment-summary

managed-device-enrollment-abandonment-summary a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|managed-device-enrollment-abandonment-summary|managedDeviceEnrollmentAbandonmentSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--skip**|integer||skip|skip|
|**--top**|integer||top|top|
|**--filter**|string||filter|filter|
|**--skip-token**|string||skip_token|skipToken|

### reports managed-device-enrollment-failure-details027-e

managed-device-enrollment-failure-details027-e a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|managed-device-enrollment-failure-details027-e|managedDeviceEnrollmentFailureDetails-027e|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports managed-device-enrollment-failure-details2-b3-d

managed-device-enrollment-failure-details2-b3-d a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|managed-device-enrollment-failure-details2-b3-d|managedDeviceEnrollmentFailureDetails-2b3d|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--skip**|integer||skip|skip|
|**--top**|integer||top|top|
|**--filter**|string||filter|filter|
|**--skip-token**|string||skip_token|skipToken|

### reports managed-device-enrollment-failure-trend

managed-device-enrollment-failure-trend a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|managed-device-enrollment-failure-trend|managedDeviceEnrollmentFailureTrends|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports managed-device-enrollment-top-failure-afd1

managed-device-enrollment-top-failure-afd1 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|managed-device-enrollment-top-failure-afd1|managedDeviceEnrollmentTopFailures-afd1|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period**|string||period|period|

### reports managed-device-enrollment-top-failures4669

managed-device-enrollment-top-failures4669 a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|managed-device-enrollment-top-failures4669|managedDeviceEnrollmentTopFailures-4669|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### reports update-application-sign-in-detailed-summary

update-application-sign-in-detailed-summary a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-application-sign-in-detailed-summary|UpdateApplicationSignInDetailedSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--application-sign-in-detailed-summary-id**|string|key: applicationSignInDetailedSummary-id of applicationSignInDetailedSummary|application_sign_in_detailed_summary_id|applicationSignInDetailedSummary-id|
|**--id**|string|Read-only.|id|id|
|**--app-id**|string||app_id|appId|
|**--app-display-name**|string||app_display_name|appDisplayName|
|**--sign-in-count**|integer||sign_in_count|signInCount|
|**--aggregated-event-date-time**|date-time||aggregated_event_date_time|aggregatedEventDateTime|
|**--status-error-code**|integer|Provides the 5-6digit error code that's generated during a sign-in failure. Check out the list of error codes and messages.|error_code|errorCode|
|**--status-failure-reason**|string|Provides the error message or the reason for failure for the corresponding sign-in activity. Check out the list of error codes and messages.|failure_reason|failureReason|
|**--status-additional-details**|string|Provides additional details on the sign-in activity|additional_details|additionalDetails|

### reports update-credential-user-registration-detail

update-credential-user-registration-detail a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-credential-user-registration-detail|UpdateCredentialUserRegistrationDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--credential-user-registration-details-id**|string|key: credentialUserRegistrationDetails-id of credentialUserRegistrationDetails|credential_user_registration_details_id|credentialUserRegistrationDetails-id|
|**--id**|string|Read-only.|id|id|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--auth-methods**|array||auth_methods|authMethods|
|**--is-registered**|boolean||is_registered|isRegistered|
|**--is-enabled**|boolean||is_enabled|isEnabled|
|**--is-capable**|boolean||is_capable|isCapable|
|**--is-mfa-registered**|boolean||is_mfa_registered|isMfaRegistered|

### reports update-daily-print-usage-summary-by-printer

update-daily-print-usage-summary-by-printer a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-daily-print-usage-summary-by-printer|UpdateDailyPrintUsageSummariesByPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-printer-id**|string|key: PrintUsageSummaryByPrinter-id of PrintUsageSummaryByPrinter|print_usage_summary_by_printer_id|PrintUsageSummaryByPrinter-id|
|**--id**|string|Read-only.|id|id|
|**--printer-id**|string||printer_id|printerId|
|**--usage-date**|date||usage_date|usageDate|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|

### reports update-daily-print-usage-summary-by-user

update-daily-print-usage-summary-by-user a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-daily-print-usage-summary-by-user|UpdateDailyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-user-id**|string|key: PrintUsageSummaryByUser-id of PrintUsageSummaryByUser|print_usage_summary_by_user_id|PrintUsageSummaryByUser-id|
|**--id**|string|Read-only.|id|id|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--usage-date**|date||usage_date|usageDate|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|

### reports update-monthly-print-usage-summary-by-printer

update-monthly-print-usage-summary-by-printer a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-monthly-print-usage-summary-by-printer|UpdateMonthlyPrintUsageSummariesByPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-printer-id**|string|key: PrintUsageSummaryByPrinter-id of PrintUsageSummaryByPrinter|print_usage_summary_by_printer_id|PrintUsageSummaryByPrinter-id|
|**--id**|string|Read-only.|id|id|
|**--printer-id**|string||printer_id|printerId|
|**--usage-date**|date||usage_date|usageDate|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|

### reports update-monthly-print-usage-summary-by-user

update-monthly-print-usage-summary-by-user a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-monthly-print-usage-summary-by-user|UpdateMonthlyPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-usage-summary-by-user-id**|string|key: PrintUsageSummaryByUser-id of PrintUsageSummaryByUser|print_usage_summary_by_user_id|PrintUsageSummaryByUser-id|
|**--id**|string|Read-only.|id|id|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--usage-date**|date||usage_date|usageDate|
|**--completed-black-and-white-job-count**|integer||completed_black_and_white_job_count|completedBlackAndWhiteJobCount|
|**--completed-color-job-count**|integer||completed_color_job_count|completedColorJobCount|
|**--incomplete-job-count**|integer||incomplete_job_count|incompleteJobCount|

### reports update-report-root

update-report-root a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports.reportRoot|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-report-root|UpdateReportRoot|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--application-sign-in-detailed-summary**|array||application_sign_in_detailed_summary|applicationSignInDetailedSummary|
|**--credential-user-registration-details**|array||credential_user_registration_details|credentialUserRegistrationDetails|
|**--user-credential-usage-details**|array||user_credential_usage_details|userCredentialUsageDetails|
|**--daily-print-usage-summaries-by-user**|array||daily_print_usage_summaries_by_user|dailyPrintUsageSummariesByUser|
|**--monthly-print-usage-summaries-by-user**|array||monthly_print_usage_summaries_by_user|monthlyPrintUsageSummariesByUser|
|**--daily-print-usage-summaries-by-printer**|array||daily_print_usage_summaries_by_printer|dailyPrintUsageSummariesByPrinter|
|**--monthly-print-usage-summaries-by-printer**|array||monthly_print_usage_summaries_by_printer|monthlyPrintUsageSummariesByPrinter|

### reports update-user-credential-usage-detail

update-user-credential-usage-detail a reports.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|reports|reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-user-credential-usage-detail|UpdateUserCredentialUsageDetails|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-credential-usage-details-id**|string|key: userCredentialUsageDetails-id of userCredentialUsageDetails|user_credential_usage_details_id|userCredentialUsageDetails-id|
|**--id**|string|Read-only.|id|id|
|**--feature**|choice||feature|feature|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|
|**--user-display-name**|string||user_display_name|userDisplayName|
|**--is-success**|boolean||is_success|isSuccess|
|**--auth-method**|choice||auth_method|authMethod|
|**--failure-reason**|string||failure_reason|failureReason|
|**--event-date-time**|date-time||event_date_time|eventDateTime|
