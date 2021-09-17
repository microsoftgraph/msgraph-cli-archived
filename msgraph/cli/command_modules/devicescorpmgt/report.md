# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az devicescorpmgt|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az devicescorpmgt` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az devicescorpmgt deviceappmanagement|deviceAppManagement|[commands](#CommandsIndeviceAppManagement)|
|az devicescorpmgt deviceappmanagementandroidmanagedappprotection|deviceAppManagement.androidManagedAppProtections|[commands](#CommandsIndeviceAppManagement.androidManagedAppProtections)|
|az devicescorpmgt deviceappmanagementdefaultmanagedappprotection|deviceAppManagement.defaultManagedAppProtections|[commands](#CommandsIndeviceAppManagement.defaultManagedAppProtections)|
|az devicescorpmgt deviceappmanagementdeviceappmanagement|deviceAppManagement.deviceAppManagement|[commands](#CommandsIndeviceAppManagement.deviceAppManagement)|
|az devicescorpmgt deviceappmanagementiosmanagedappprotection|deviceAppManagement.iosManagedAppProtections|[commands](#CommandsIndeviceAppManagement.iosManagedAppProtections)|
|az devicescorpmgt deviceappmanagementmanagedapppolicy|deviceAppManagement.managedAppPolicies|[commands](#CommandsIndeviceAppManagement.managedAppPolicies)|
|az devicescorpmgt deviceappmanagementmanagedappregistration|deviceAppManagement.managedAppRegistrations|[commands](#CommandsIndeviceAppManagement.managedAppRegistrations)|
|az devicescorpmgt deviceappmanagementmanagedappregistrationsappliedpolicy|deviceAppManagement.managedAppRegistrations.appliedPolicies|[commands](#CommandsIndeviceAppManagement.managedAppRegistrations.appliedPolicies)|
|az devicescorpmgt deviceappmanagementmanagedappregistrationsintendedpolicy|deviceAppManagement.managedAppRegistrations.intendedPolicies|[commands](#CommandsIndeviceAppManagement.managedAppRegistrations.intendedPolicies)|
|az devicescorpmgt deviceappmanagementmanagedebook|deviceAppManagement.managedEBooks|[commands](#CommandsIndeviceAppManagement.managedEBooks)|
|az devicescorpmgt deviceappmanagementmanagedebooksuserstatesummary|deviceAppManagement.managedEBooks.userStateSummary|[commands](#CommandsIndeviceAppManagement.managedEBooks.userStateSummary)|
|az devicescorpmgt deviceappmanagementmobileapp|deviceAppManagement.mobileApps|[commands](#CommandsIndeviceAppManagement.mobileApps)|
|az devicescorpmgt deviceappmanagementmobileappconfiguration|deviceAppManagement.mobileAppConfigurations|[commands](#CommandsIndeviceAppManagement.mobileAppConfigurations)|
|az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration|deviceAppManagement.targetedManagedAppConfigurations|[commands](#CommandsIndeviceAppManagement.targetedManagedAppConfigurations)|
|az devicescorpmgt deviceappmanagementvpptoken|deviceAppManagement.vppTokens|[commands](#CommandsIndeviceAppManagement.vppTokens)|
|az devicescorpmgt user|users|[commands](#CommandsInusers)|
|az devicescorpmgt usersmanageddevice|users.managedDevices|[commands](#CommandsInusers.managedDevices)|

## COMMANDS
### <a name="CommandsIndeviceAppManagement">Commands in `az devicescorpmgt deviceappmanagement` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt deviceappmanagement create-android-managed-app-protection](#deviceAppManagementCreateAndroidManagedAppProtections)|CreateAndroidManagedAppProtections|[Parameters](#ParametersdeviceAppManagementCreateAndroidManagedAppProtections)|Not Found|
|[az devicescorpmgt deviceappmanagement create-default-managed-app-protection](#deviceAppManagementCreateDefaultManagedAppProtections)|CreateDefaultManagedAppProtections|[Parameters](#ParametersdeviceAppManagementCreateDefaultManagedAppProtections)|Not Found|
|[az devicescorpmgt deviceappmanagement create-io-managed-app-protection](#deviceAppManagementCreateIosManagedAppProtections)|CreateIosManagedAppProtections|[Parameters](#ParametersdeviceAppManagementCreateIosManagedAppProtections)|Not Found|
|[az devicescorpmgt deviceappmanagement create-managed-app-policy](#deviceAppManagementCreateManagedAppPolicies)|CreateManagedAppPolicies|[Parameters](#ParametersdeviceAppManagementCreateManagedAppPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagement create-managed-app-registration](#deviceAppManagementCreateManagedAppRegistrations)|CreateManagedAppRegistrations|[Parameters](#ParametersdeviceAppManagementCreateManagedAppRegistrations)|Not Found|
|[az devicescorpmgt deviceappmanagement create-managed-app-statuses](#deviceAppManagementCreateManagedAppStatuses)|CreateManagedAppStatuses|[Parameters](#ParametersdeviceAppManagementCreateManagedAppStatuses)|Not Found|
|[az devicescorpmgt deviceappmanagement create-managed-e-book](#deviceAppManagementCreateManagedEBooks)|CreateManagedEBooks|[Parameters](#ParametersdeviceAppManagementCreateManagedEBooks)|Not Found|
|[az devicescorpmgt deviceappmanagement create-mdm-window-information-protection-policy](#deviceAppManagementCreateMdmWindowsInformationProtectionPolicies)|CreateMdmWindowsInformationProtectionPolicies|[Parameters](#ParametersdeviceAppManagementCreateMdmWindowsInformationProtectionPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagement create-mobile-app](#deviceAppManagementCreateMobileApps)|CreateMobileApps|[Parameters](#ParametersdeviceAppManagementCreateMobileApps)|Not Found|
|[az devicescorpmgt deviceappmanagement create-mobile-app-category](#deviceAppManagementCreateMobileAppCategories)|CreateMobileAppCategories|[Parameters](#ParametersdeviceAppManagementCreateMobileAppCategories)|Not Found|
|[az devicescorpmgt deviceappmanagement create-mobile-app-configuration](#deviceAppManagementCreateMobileAppConfigurations)|CreateMobileAppConfigurations|[Parameters](#ParametersdeviceAppManagementCreateMobileAppConfigurations)|Not Found|
|[az devicescorpmgt deviceappmanagement create-targeted-managed-app-configuration](#deviceAppManagementCreateTargetedManagedAppConfigurations)|CreateTargetedManagedAppConfigurations|[Parameters](#ParametersdeviceAppManagementCreateTargetedManagedAppConfigurations)|Not Found|
|[az devicescorpmgt deviceappmanagement create-vpp-token](#deviceAppManagementCreateVppTokens)|CreateVppTokens|[Parameters](#ParametersdeviceAppManagementCreateVppTokens)|Not Found|
|[az devicescorpmgt deviceappmanagement create-window-information-protection-policy](#deviceAppManagementCreateWindowsInformationProtectionPolicies)|CreateWindowsInformationProtectionPolicies|[Parameters](#ParametersdeviceAppManagementCreateWindowsInformationProtectionPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagement delete-android-managed-app-protection](#deviceAppManagementDeleteAndroidManagedAppProtections)|DeleteAndroidManagedAppProtections|[Parameters](#ParametersdeviceAppManagementDeleteAndroidManagedAppProtections)|Not Found|
|[az devicescorpmgt deviceappmanagement delete-default-managed-app-protection](#deviceAppManagementDeleteDefaultManagedAppProtections)|DeleteDefaultManagedAppProtections|[Parameters](#ParametersdeviceAppManagementDeleteDefaultManagedAppProtections)|Not Found|
|[az devicescorpmgt deviceappmanagement delete-io-managed-app-protection](#deviceAppManagementDeleteIosManagedAppProtections)|DeleteIosManagedAppProtections|[Parameters](#ParametersdeviceAppManagementDeleteIosManagedAppProtections)|Not Found|
|[az devicescorpmgt deviceappmanagement delete-managed-app-policy](#deviceAppManagementDeleteManagedAppPolicies)|DeleteManagedAppPolicies|[Parameters](#ParametersdeviceAppManagementDeleteManagedAppPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagement delete-managed-app-registration](#deviceAppManagementDeleteManagedAppRegistrations)|DeleteManagedAppRegistrations|[Parameters](#ParametersdeviceAppManagementDeleteManagedAppRegistrations)|Not Found|
|[az devicescorpmgt deviceappmanagement delete-managed-app-statuses](#deviceAppManagementDeleteManagedAppStatuses)|DeleteManagedAppStatuses|[Parameters](#ParametersdeviceAppManagementDeleteManagedAppStatuses)|Not Found|
|[az devicescorpmgt deviceappmanagement delete-managed-e-book](#deviceAppManagementDeleteManagedEBooks)|DeleteManagedEBooks|[Parameters](#ParametersdeviceAppManagementDeleteManagedEBooks)|Not Found|
|[az devicescorpmgt deviceappmanagement delete-mdm-window-information-protection-policy](#deviceAppManagementDeleteMdmWindowsInformationProtectionPolicies)|DeleteMdmWindowsInformationProtectionPolicies|[Parameters](#ParametersdeviceAppManagementDeleteMdmWindowsInformationProtectionPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagement delete-mobile-app](#deviceAppManagementDeleteMobileApps)|DeleteMobileApps|[Parameters](#ParametersdeviceAppManagementDeleteMobileApps)|Not Found|
|[az devicescorpmgt deviceappmanagement delete-mobile-app-category](#deviceAppManagementDeleteMobileAppCategories)|DeleteMobileAppCategories|[Parameters](#ParametersdeviceAppManagementDeleteMobileAppCategories)|Not Found|
|[az devicescorpmgt deviceappmanagement delete-mobile-app-configuration](#deviceAppManagementDeleteMobileAppConfigurations)|DeleteMobileAppConfigurations|[Parameters](#ParametersdeviceAppManagementDeleteMobileAppConfigurations)|Not Found|
|[az devicescorpmgt deviceappmanagement delete-targeted-managed-app-configuration](#deviceAppManagementDeleteTargetedManagedAppConfigurations)|DeleteTargetedManagedAppConfigurations|[Parameters](#ParametersdeviceAppManagementDeleteTargetedManagedAppConfigurations)|Not Found|
|[az devicescorpmgt deviceappmanagement delete-vpp-token](#deviceAppManagementDeleteVppTokens)|DeleteVppTokens|[Parameters](#ParametersdeviceAppManagementDeleteVppTokens)|Not Found|
|[az devicescorpmgt deviceappmanagement delete-window-information-protection-policy](#deviceAppManagementDeleteWindowsInformationProtectionPolicies)|DeleteWindowsInformationProtectionPolicies|[Parameters](#ParametersdeviceAppManagementDeleteWindowsInformationProtectionPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagement list-android-managed-app-protection](#deviceAppManagementListAndroidManagedAppProtections)|ListAndroidManagedAppProtections|[Parameters](#ParametersdeviceAppManagementListAndroidManagedAppProtections)|Not Found|
|[az devicescorpmgt deviceappmanagement list-default-managed-app-protection](#deviceAppManagementListDefaultManagedAppProtections)|ListDefaultManagedAppProtections|[Parameters](#ParametersdeviceAppManagementListDefaultManagedAppProtections)|Not Found|
|[az devicescorpmgt deviceappmanagement list-io-managed-app-protection](#deviceAppManagementListIosManagedAppProtections)|ListIosManagedAppProtections|[Parameters](#ParametersdeviceAppManagementListIosManagedAppProtections)|Not Found|
|[az devicescorpmgt deviceappmanagement list-managed-app-policy](#deviceAppManagementListManagedAppPolicies)|ListManagedAppPolicies|[Parameters](#ParametersdeviceAppManagementListManagedAppPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagement list-managed-app-registration](#deviceAppManagementListManagedAppRegistrations)|ListManagedAppRegistrations|[Parameters](#ParametersdeviceAppManagementListManagedAppRegistrations)|Not Found|
|[az devicescorpmgt deviceappmanagement list-managed-app-statuses](#deviceAppManagementListManagedAppStatuses)|ListManagedAppStatuses|[Parameters](#ParametersdeviceAppManagementListManagedAppStatuses)|Not Found|
|[az devicescorpmgt deviceappmanagement list-managed-e-book](#deviceAppManagementListManagedEBooks)|ListManagedEBooks|[Parameters](#ParametersdeviceAppManagementListManagedEBooks)|Not Found|
|[az devicescorpmgt deviceappmanagement list-mdm-window-information-protection-policy](#deviceAppManagementListMdmWindowsInformationProtectionPolicies)|ListMdmWindowsInformationProtectionPolicies|[Parameters](#ParametersdeviceAppManagementListMdmWindowsInformationProtectionPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagement list-mobile-app](#deviceAppManagementListMobileApps)|ListMobileApps|[Parameters](#ParametersdeviceAppManagementListMobileApps)|Not Found|
|[az devicescorpmgt deviceappmanagement list-mobile-app-category](#deviceAppManagementListMobileAppCategories)|ListMobileAppCategories|[Parameters](#ParametersdeviceAppManagementListMobileAppCategories)|Not Found|
|[az devicescorpmgt deviceappmanagement list-mobile-app-configuration](#deviceAppManagementListMobileAppConfigurations)|ListMobileAppConfigurations|[Parameters](#ParametersdeviceAppManagementListMobileAppConfigurations)|Not Found|
|[az devicescorpmgt deviceappmanagement list-targeted-managed-app-configuration](#deviceAppManagementListTargetedManagedAppConfigurations)|ListTargetedManagedAppConfigurations|[Parameters](#ParametersdeviceAppManagementListTargetedManagedAppConfigurations)|Not Found|
|[az devicescorpmgt deviceappmanagement list-vpp-token](#deviceAppManagementListVppTokens)|ListVppTokens|[Parameters](#ParametersdeviceAppManagementListVppTokens)|Not Found|
|[az devicescorpmgt deviceappmanagement list-window-information-protection-policy](#deviceAppManagementListWindowsInformationProtectionPolicies)|ListWindowsInformationProtectionPolicies|[Parameters](#ParametersdeviceAppManagementListWindowsInformationProtectionPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagement show-android-managed-app-protection](#deviceAppManagementGetAndroidManagedAppProtections)|GetAndroidManagedAppProtections|[Parameters](#ParametersdeviceAppManagementGetAndroidManagedAppProtections)|Not Found|
|[az devicescorpmgt deviceappmanagement show-default-managed-app-protection](#deviceAppManagementGetDefaultManagedAppProtections)|GetDefaultManagedAppProtections|[Parameters](#ParametersdeviceAppManagementGetDefaultManagedAppProtections)|Not Found|
|[az devicescorpmgt deviceappmanagement show-io-managed-app-protection](#deviceAppManagementGetIosManagedAppProtections)|GetIosManagedAppProtections|[Parameters](#ParametersdeviceAppManagementGetIosManagedAppProtections)|Not Found|
|[az devicescorpmgt deviceappmanagement show-managed-app-policy](#deviceAppManagementGetManagedAppPolicies)|GetManagedAppPolicies|[Parameters](#ParametersdeviceAppManagementGetManagedAppPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagement show-managed-app-registration](#deviceAppManagementGetManagedAppRegistrations)|GetManagedAppRegistrations|[Parameters](#ParametersdeviceAppManagementGetManagedAppRegistrations)|Not Found|
|[az devicescorpmgt deviceappmanagement show-managed-app-statuses](#deviceAppManagementGetManagedAppStatuses)|GetManagedAppStatuses|[Parameters](#ParametersdeviceAppManagementGetManagedAppStatuses)|Not Found|
|[az devicescorpmgt deviceappmanagement show-managed-e-book](#deviceAppManagementGetManagedEBooks)|GetManagedEBooks|[Parameters](#ParametersdeviceAppManagementGetManagedEBooks)|Not Found|
|[az devicescorpmgt deviceappmanagement show-mdm-window-information-protection-policy](#deviceAppManagementGetMdmWindowsInformationProtectionPolicies)|GetMdmWindowsInformationProtectionPolicies|[Parameters](#ParametersdeviceAppManagementGetMdmWindowsInformationProtectionPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagement show-mobile-app](#deviceAppManagementGetMobileApps)|GetMobileApps|[Parameters](#ParametersdeviceAppManagementGetMobileApps)|Not Found|
|[az devicescorpmgt deviceappmanagement show-mobile-app-category](#deviceAppManagementGetMobileAppCategories)|GetMobileAppCategories|[Parameters](#ParametersdeviceAppManagementGetMobileAppCategories)|Not Found|
|[az devicescorpmgt deviceappmanagement show-mobile-app-configuration](#deviceAppManagementGetMobileAppConfigurations)|GetMobileAppConfigurations|[Parameters](#ParametersdeviceAppManagementGetMobileAppConfigurations)|Not Found|
|[az devicescorpmgt deviceappmanagement show-targeted-managed-app-configuration](#deviceAppManagementGetTargetedManagedAppConfigurations)|GetTargetedManagedAppConfigurations|[Parameters](#ParametersdeviceAppManagementGetTargetedManagedAppConfigurations)|Not Found|
|[az devicescorpmgt deviceappmanagement show-vpp-token](#deviceAppManagementGetVppTokens)|GetVppTokens|[Parameters](#ParametersdeviceAppManagementGetVppTokens)|Not Found|
|[az devicescorpmgt deviceappmanagement show-window-information-protection-policy](#deviceAppManagementGetWindowsInformationProtectionPolicies)|GetWindowsInformationProtectionPolicies|[Parameters](#ParametersdeviceAppManagementGetWindowsInformationProtectionPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagement sync-microsoft-store-for-business-app](#deviceAppManagementsyncMicrosoftStoreForBusinessApps)|syncMicrosoftStoreForBusinessApps|[Parameters](#ParametersdeviceAppManagementsyncMicrosoftStoreForBusinessApps)|Not Found|
|[az devicescorpmgt deviceappmanagement update-android-managed-app-protection](#deviceAppManagementUpdateAndroidManagedAppProtections)|UpdateAndroidManagedAppProtections|[Parameters](#ParametersdeviceAppManagementUpdateAndroidManagedAppProtections)|Not Found|
|[az devicescorpmgt deviceappmanagement update-default-managed-app-protection](#deviceAppManagementUpdateDefaultManagedAppProtections)|UpdateDefaultManagedAppProtections|[Parameters](#ParametersdeviceAppManagementUpdateDefaultManagedAppProtections)|Not Found|
|[az devicescorpmgt deviceappmanagement update-io-managed-app-protection](#deviceAppManagementUpdateIosManagedAppProtections)|UpdateIosManagedAppProtections|[Parameters](#ParametersdeviceAppManagementUpdateIosManagedAppProtections)|Not Found|
|[az devicescorpmgt deviceappmanagement update-managed-app-policy](#deviceAppManagementUpdateManagedAppPolicies)|UpdateManagedAppPolicies|[Parameters](#ParametersdeviceAppManagementUpdateManagedAppPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagement update-managed-app-registration](#deviceAppManagementUpdateManagedAppRegistrations)|UpdateManagedAppRegistrations|[Parameters](#ParametersdeviceAppManagementUpdateManagedAppRegistrations)|Not Found|
|[az devicescorpmgt deviceappmanagement update-managed-app-statuses](#deviceAppManagementUpdateManagedAppStatuses)|UpdateManagedAppStatuses|[Parameters](#ParametersdeviceAppManagementUpdateManagedAppStatuses)|Not Found|
|[az devicescorpmgt deviceappmanagement update-managed-e-book](#deviceAppManagementUpdateManagedEBooks)|UpdateManagedEBooks|[Parameters](#ParametersdeviceAppManagementUpdateManagedEBooks)|Not Found|
|[az devicescorpmgt deviceappmanagement update-mdm-window-information-protection-policy](#deviceAppManagementUpdateMdmWindowsInformationProtectionPolicies)|UpdateMdmWindowsInformationProtectionPolicies|[Parameters](#ParametersdeviceAppManagementUpdateMdmWindowsInformationProtectionPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagement update-mobile-app](#deviceAppManagementUpdateMobileApps)|UpdateMobileApps|[Parameters](#ParametersdeviceAppManagementUpdateMobileApps)|Not Found|
|[az devicescorpmgt deviceappmanagement update-mobile-app-category](#deviceAppManagementUpdateMobileAppCategories)|UpdateMobileAppCategories|[Parameters](#ParametersdeviceAppManagementUpdateMobileAppCategories)|Not Found|
|[az devicescorpmgt deviceappmanagement update-mobile-app-configuration](#deviceAppManagementUpdateMobileAppConfigurations)|UpdateMobileAppConfigurations|[Parameters](#ParametersdeviceAppManagementUpdateMobileAppConfigurations)|Not Found|
|[az devicescorpmgt deviceappmanagement update-targeted-managed-app-configuration](#deviceAppManagementUpdateTargetedManagedAppConfigurations)|UpdateTargetedManagedAppConfigurations|[Parameters](#ParametersdeviceAppManagementUpdateTargetedManagedAppConfigurations)|Not Found|
|[az devicescorpmgt deviceappmanagement update-vpp-token](#deviceAppManagementUpdateVppTokens)|UpdateVppTokens|[Parameters](#ParametersdeviceAppManagementUpdateVppTokens)|Not Found|
|[az devicescorpmgt deviceappmanagement update-window-information-protection-policy](#deviceAppManagementUpdateWindowsInformationProtectionPolicies)|UpdateWindowsInformationProtectionPolicies|[Parameters](#ParametersdeviceAppManagementUpdateWindowsInformationProtectionPolicies)|Not Found|

### <a name="CommandsIndeviceAppManagement.androidManagedAppProtections">Commands in `az devicescorpmgt deviceappmanagementandroidmanagedappprotection` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt deviceappmanagementandroidmanagedappprotection create-app](#deviceAppManagement.androidManagedAppProtectionsCreateApps)|CreateApps|[Parameters](#ParametersdeviceAppManagement.androidManagedAppProtectionsCreateApps)|Not Found|
|[az devicescorpmgt deviceappmanagementandroidmanagedappprotection delete-app](#deviceAppManagement.androidManagedAppProtectionsDeleteApps)|DeleteApps|[Parameters](#ParametersdeviceAppManagement.androidManagedAppProtectionsDeleteApps)|Not Found|
|[az devicescorpmgt deviceappmanagementandroidmanagedappprotection delete-deployment-summary](#deviceAppManagement.androidManagedAppProtectionsDeleteDeploymentSummary)|DeleteDeploymentSummary|[Parameters](#ParametersdeviceAppManagement.androidManagedAppProtectionsDeleteDeploymentSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementandroidmanagedappprotection list-app](#deviceAppManagement.androidManagedAppProtectionsListApps)|ListApps|[Parameters](#ParametersdeviceAppManagement.androidManagedAppProtectionsListApps)|Not Found|
|[az devicescorpmgt deviceappmanagementandroidmanagedappprotection show-app](#deviceAppManagement.androidManagedAppProtectionsGetApps)|GetApps|[Parameters](#ParametersdeviceAppManagement.androidManagedAppProtectionsGetApps)|Not Found|
|[az devicescorpmgt deviceappmanagementandroidmanagedappprotection show-deployment-summary](#deviceAppManagement.androidManagedAppProtectionsGetDeploymentSummary)|GetDeploymentSummary|[Parameters](#ParametersdeviceAppManagement.androidManagedAppProtectionsGetDeploymentSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementandroidmanagedappprotection update-app](#deviceAppManagement.androidManagedAppProtectionsUpdateApps)|UpdateApps|[Parameters](#ParametersdeviceAppManagement.androidManagedAppProtectionsUpdateApps)|Not Found|
|[az devicescorpmgt deviceappmanagementandroidmanagedappprotection update-deployment-summary](#deviceAppManagement.androidManagedAppProtectionsUpdateDeploymentSummary)|UpdateDeploymentSummary|[Parameters](#ParametersdeviceAppManagement.androidManagedAppProtectionsUpdateDeploymentSummary)|Not Found|

### <a name="CommandsIndeviceAppManagement.defaultManagedAppProtections">Commands in `az devicescorpmgt deviceappmanagementdefaultmanagedappprotection` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt deviceappmanagementdefaultmanagedappprotection create-app](#deviceAppManagement.defaultManagedAppProtectionsCreateApps)|CreateApps|[Parameters](#ParametersdeviceAppManagement.defaultManagedAppProtectionsCreateApps)|Not Found|
|[az devicescorpmgt deviceappmanagementdefaultmanagedappprotection delete-app](#deviceAppManagement.defaultManagedAppProtectionsDeleteApps)|DeleteApps|[Parameters](#ParametersdeviceAppManagement.defaultManagedAppProtectionsDeleteApps)|Not Found|
|[az devicescorpmgt deviceappmanagementdefaultmanagedappprotection delete-deployment-summary](#deviceAppManagement.defaultManagedAppProtectionsDeleteDeploymentSummary)|DeleteDeploymentSummary|[Parameters](#ParametersdeviceAppManagement.defaultManagedAppProtectionsDeleteDeploymentSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementdefaultmanagedappprotection list-app](#deviceAppManagement.defaultManagedAppProtectionsListApps)|ListApps|[Parameters](#ParametersdeviceAppManagement.defaultManagedAppProtectionsListApps)|Not Found|
|[az devicescorpmgt deviceappmanagementdefaultmanagedappprotection show-app](#deviceAppManagement.defaultManagedAppProtectionsGetApps)|GetApps|[Parameters](#ParametersdeviceAppManagement.defaultManagedAppProtectionsGetApps)|Not Found|
|[az devicescorpmgt deviceappmanagementdefaultmanagedappprotection show-deployment-summary](#deviceAppManagement.defaultManagedAppProtectionsGetDeploymentSummary)|GetDeploymentSummary|[Parameters](#ParametersdeviceAppManagement.defaultManagedAppProtectionsGetDeploymentSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementdefaultmanagedappprotection update-app](#deviceAppManagement.defaultManagedAppProtectionsUpdateApps)|UpdateApps|[Parameters](#ParametersdeviceAppManagement.defaultManagedAppProtectionsUpdateApps)|Not Found|
|[az devicescorpmgt deviceappmanagementdefaultmanagedappprotection update-deployment-summary](#deviceAppManagement.defaultManagedAppProtectionsUpdateDeploymentSummary)|UpdateDeploymentSummary|[Parameters](#ParametersdeviceAppManagement.defaultManagedAppProtectionsUpdateDeploymentSummary)|Not Found|

### <a name="CommandsIndeviceAppManagement.deviceAppManagement">Commands in `az devicescorpmgt deviceappmanagementdeviceappmanagement` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt deviceappmanagementdeviceappmanagement show-device-app-management](#deviceAppManagement.deviceAppManagementGetDeviceAppManagement)|GetDeviceAppManagement|[Parameters](#ParametersdeviceAppManagement.deviceAppManagementGetDeviceAppManagement)|Not Found|
|[az devicescorpmgt deviceappmanagementdeviceappmanagement update-device-app-management](#deviceAppManagement.deviceAppManagementUpdateDeviceAppManagement)|UpdateDeviceAppManagement|[Parameters](#ParametersdeviceAppManagement.deviceAppManagementUpdateDeviceAppManagement)|Not Found|

### <a name="CommandsIndeviceAppManagement.iosManagedAppProtections">Commands in `az devicescorpmgt deviceappmanagementiosmanagedappprotection` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt deviceappmanagementiosmanagedappprotection create-app](#deviceAppManagement.iosManagedAppProtectionsCreateApps)|CreateApps|[Parameters](#ParametersdeviceAppManagement.iosManagedAppProtectionsCreateApps)|Not Found|
|[az devicescorpmgt deviceappmanagementiosmanagedappprotection delete-app](#deviceAppManagement.iosManagedAppProtectionsDeleteApps)|DeleteApps|[Parameters](#ParametersdeviceAppManagement.iosManagedAppProtectionsDeleteApps)|Not Found|
|[az devicescorpmgt deviceappmanagementiosmanagedappprotection delete-deployment-summary](#deviceAppManagement.iosManagedAppProtectionsDeleteDeploymentSummary)|DeleteDeploymentSummary|[Parameters](#ParametersdeviceAppManagement.iosManagedAppProtectionsDeleteDeploymentSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementiosmanagedappprotection list-app](#deviceAppManagement.iosManagedAppProtectionsListApps)|ListApps|[Parameters](#ParametersdeviceAppManagement.iosManagedAppProtectionsListApps)|Not Found|
|[az devicescorpmgt deviceappmanagementiosmanagedappprotection show-app](#deviceAppManagement.iosManagedAppProtectionsGetApps)|GetApps|[Parameters](#ParametersdeviceAppManagement.iosManagedAppProtectionsGetApps)|Not Found|
|[az devicescorpmgt deviceappmanagementiosmanagedappprotection show-deployment-summary](#deviceAppManagement.iosManagedAppProtectionsGetDeploymentSummary)|GetDeploymentSummary|[Parameters](#ParametersdeviceAppManagement.iosManagedAppProtectionsGetDeploymentSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementiosmanagedappprotection update-app](#deviceAppManagement.iosManagedAppProtectionsUpdateApps)|UpdateApps|[Parameters](#ParametersdeviceAppManagement.iosManagedAppProtectionsUpdateApps)|Not Found|
|[az devicescorpmgt deviceappmanagementiosmanagedappprotection update-deployment-summary](#deviceAppManagement.iosManagedAppProtectionsUpdateDeploymentSummary)|UpdateDeploymentSummary|[Parameters](#ParametersdeviceAppManagement.iosManagedAppProtectionsUpdateDeploymentSummary)|Not Found|

### <a name="CommandsIndeviceAppManagement.managedAppPolicies">Commands in `az devicescorpmgt deviceappmanagementmanagedapppolicy` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt deviceappmanagementmanagedapppolicy target-app](#deviceAppManagement.managedAppPoliciestargetApps)|targetApps|[Parameters](#ParametersdeviceAppManagement.managedAppPoliciestargetApps)|Not Found|

### <a name="CommandsIndeviceAppManagement.managedAppRegistrations">Commands in `az devicescorpmgt deviceappmanagementmanagedappregistration` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt deviceappmanagementmanagedappregistration create-applied-policy](#deviceAppManagement.managedAppRegistrationsCreateAppliedPolicies)|CreateAppliedPolicies|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsCreateAppliedPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedappregistration create-intended-policy](#deviceAppManagement.managedAppRegistrationsCreateIntendedPolicies)|CreateIntendedPolicies|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsCreateIntendedPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedappregistration create-operation](#deviceAppManagement.managedAppRegistrationsCreateOperations)|CreateOperations|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsCreateOperations)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedappregistration delete-applied-policy](#deviceAppManagement.managedAppRegistrationsDeleteAppliedPolicies)|DeleteAppliedPolicies|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsDeleteAppliedPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedappregistration delete-intended-policy](#deviceAppManagement.managedAppRegistrationsDeleteIntendedPolicies)|DeleteIntendedPolicies|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsDeleteIntendedPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedappregistration delete-operation](#deviceAppManagement.managedAppRegistrationsDeleteOperations)|DeleteOperations|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsDeleteOperations)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedappregistration list-applied-policy](#deviceAppManagement.managedAppRegistrationsListAppliedPolicies)|ListAppliedPolicies|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsListAppliedPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedappregistration list-intended-policy](#deviceAppManagement.managedAppRegistrationsListIntendedPolicies)|ListIntendedPolicies|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsListIntendedPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedappregistration list-operation](#deviceAppManagement.managedAppRegistrationsListOperations)|ListOperations|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsListOperations)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedappregistration show-applied-policy](#deviceAppManagement.managedAppRegistrationsGetAppliedPolicies)|GetAppliedPolicies|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsGetAppliedPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedappregistration show-intended-policy](#deviceAppManagement.managedAppRegistrationsGetIntendedPolicies)|GetIntendedPolicies|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsGetIntendedPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedappregistration show-operation](#deviceAppManagement.managedAppRegistrationsGetOperations)|GetOperations|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsGetOperations)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedappregistration show-user-id-with-flagged-app-registration](#deviceAppManagement.managedAppRegistrationsgetUserIdsWithFlaggedAppRegistration)|getUserIdsWithFlaggedAppRegistration|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsgetUserIdsWithFlaggedAppRegistration)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedappregistration update-applied-policy](#deviceAppManagement.managedAppRegistrationsUpdateAppliedPolicies)|UpdateAppliedPolicies|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsUpdateAppliedPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedappregistration update-intended-policy](#deviceAppManagement.managedAppRegistrationsUpdateIntendedPolicies)|UpdateIntendedPolicies|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsUpdateIntendedPolicies)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedappregistration update-operation](#deviceAppManagement.managedAppRegistrationsUpdateOperations)|UpdateOperations|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrationsUpdateOperations)|Not Found|

### <a name="CommandsIndeviceAppManagement.managedAppRegistrations.appliedPolicies">Commands in `az devicescorpmgt deviceappmanagementmanagedappregistrationsappliedpolicy` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt deviceappmanagementmanagedappregistrationsappliedpolicy target-app](#deviceAppManagement.managedAppRegistrations.appliedPoliciestargetApps)|targetApps|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrations.appliedPoliciestargetApps)|Not Found|

### <a name="CommandsIndeviceAppManagement.managedAppRegistrations.intendedPolicies">Commands in `az devicescorpmgt deviceappmanagementmanagedappregistrationsintendedpolicy` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt deviceappmanagementmanagedappregistrationsintendedpolicy target-app](#deviceAppManagement.managedAppRegistrations.intendedPoliciestargetApps)|targetApps|[Parameters](#ParametersdeviceAppManagement.managedAppRegistrations.intendedPoliciestargetApps)|Not Found|

### <a name="CommandsIndeviceAppManagement.managedEBooks">Commands in `az devicescorpmgt deviceappmanagementmanagedebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt deviceappmanagementmanagedebook assign](#deviceAppManagement.managedEBooksassign)|assign|[Parameters](#ParametersdeviceAppManagement.managedEBooksassign)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook create-assignment](#deviceAppManagement.managedEBooksCreateAssignments)|CreateAssignments|[Parameters](#ParametersdeviceAppManagement.managedEBooksCreateAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook create-device-state](#deviceAppManagement.managedEBooksCreateDeviceStates)|CreateDeviceStates|[Parameters](#ParametersdeviceAppManagement.managedEBooksCreateDeviceStates)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook create-user-state-summary](#deviceAppManagement.managedEBooksCreateUserStateSummary)|CreateUserStateSummary|[Parameters](#ParametersdeviceAppManagement.managedEBooksCreateUserStateSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook delete-assignment](#deviceAppManagement.managedEBooksDeleteAssignments)|DeleteAssignments|[Parameters](#ParametersdeviceAppManagement.managedEBooksDeleteAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook delete-device-state](#deviceAppManagement.managedEBooksDeleteDeviceStates)|DeleteDeviceStates|[Parameters](#ParametersdeviceAppManagement.managedEBooksDeleteDeviceStates)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook delete-install-summary](#deviceAppManagement.managedEBooksDeleteInstallSummary)|DeleteInstallSummary|[Parameters](#ParametersdeviceAppManagement.managedEBooksDeleteInstallSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook delete-user-state-summary](#deviceAppManagement.managedEBooksDeleteUserStateSummary)|DeleteUserStateSummary|[Parameters](#ParametersdeviceAppManagement.managedEBooksDeleteUserStateSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook list-assignment](#deviceAppManagement.managedEBooksListAssignments)|ListAssignments|[Parameters](#ParametersdeviceAppManagement.managedEBooksListAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook list-device-state](#deviceAppManagement.managedEBooksListDeviceStates)|ListDeviceStates|[Parameters](#ParametersdeviceAppManagement.managedEBooksListDeviceStates)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook list-user-state-summary](#deviceAppManagement.managedEBooksListUserStateSummary)|ListUserStateSummary|[Parameters](#ParametersdeviceAppManagement.managedEBooksListUserStateSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook show-assignment](#deviceAppManagement.managedEBooksGetAssignments)|GetAssignments|[Parameters](#ParametersdeviceAppManagement.managedEBooksGetAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook show-device-state](#deviceAppManagement.managedEBooksGetDeviceStates)|GetDeviceStates|[Parameters](#ParametersdeviceAppManagement.managedEBooksGetDeviceStates)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook show-install-summary](#deviceAppManagement.managedEBooksGetInstallSummary)|GetInstallSummary|[Parameters](#ParametersdeviceAppManagement.managedEBooksGetInstallSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook show-user-state-summary](#deviceAppManagement.managedEBooksGetUserStateSummary)|GetUserStateSummary|[Parameters](#ParametersdeviceAppManagement.managedEBooksGetUserStateSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook update-assignment](#deviceAppManagement.managedEBooksUpdateAssignments)|UpdateAssignments|[Parameters](#ParametersdeviceAppManagement.managedEBooksUpdateAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook update-device-state](#deviceAppManagement.managedEBooksUpdateDeviceStates)|UpdateDeviceStates|[Parameters](#ParametersdeviceAppManagement.managedEBooksUpdateDeviceStates)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook update-install-summary](#deviceAppManagement.managedEBooksUpdateInstallSummary)|UpdateInstallSummary|[Parameters](#ParametersdeviceAppManagement.managedEBooksUpdateInstallSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebook update-user-state-summary](#deviceAppManagement.managedEBooksUpdateUserStateSummary)|UpdateUserStateSummary|[Parameters](#ParametersdeviceAppManagement.managedEBooksUpdateUserStateSummary)|Not Found|

### <a name="CommandsIndeviceAppManagement.managedEBooks.userStateSummary">Commands in `az devicescorpmgt deviceappmanagementmanagedebooksuserstatesummary` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt deviceappmanagementmanagedebooksuserstatesummary create-device-state](#deviceAppManagement.managedEBooks.userStateSummaryCreateDeviceStates)|CreateDeviceStates|[Parameters](#ParametersdeviceAppManagement.managedEBooks.userStateSummaryCreateDeviceStates)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebooksuserstatesummary delete-device-state](#deviceAppManagement.managedEBooks.userStateSummaryDeleteDeviceStates)|DeleteDeviceStates|[Parameters](#ParametersdeviceAppManagement.managedEBooks.userStateSummaryDeleteDeviceStates)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebooksuserstatesummary list-device-state](#deviceAppManagement.managedEBooks.userStateSummaryListDeviceStates)|ListDeviceStates|[Parameters](#ParametersdeviceAppManagement.managedEBooks.userStateSummaryListDeviceStates)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebooksuserstatesummary show-device-state](#deviceAppManagement.managedEBooks.userStateSummaryGetDeviceStates)|GetDeviceStates|[Parameters](#ParametersdeviceAppManagement.managedEBooks.userStateSummaryGetDeviceStates)|Not Found|
|[az devicescorpmgt deviceappmanagementmanagedebooksuserstatesummary update-device-state](#deviceAppManagement.managedEBooks.userStateSummaryUpdateDeviceStates)|UpdateDeviceStates|[Parameters](#ParametersdeviceAppManagement.managedEBooks.userStateSummaryUpdateDeviceStates)|Not Found|

### <a name="CommandsIndeviceAppManagement.mobileApps">Commands in `az devicescorpmgt deviceappmanagementmobileapp` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt deviceappmanagementmobileapp assign](#deviceAppManagement.mobileAppsassign)|assign|[Parameters](#ParametersdeviceAppManagement.mobileAppsassign)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileapp create-assignment](#deviceAppManagement.mobileAppsCreateAssignments)|CreateAssignments|[Parameters](#ParametersdeviceAppManagement.mobileAppsCreateAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileapp create-ref-category](#deviceAppManagement.mobileAppsCreateRefCategories)|CreateRefCategories|[Parameters](#ParametersdeviceAppManagement.mobileAppsCreateRefCategories)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileapp delete-assignment](#deviceAppManagement.mobileAppsDeleteAssignments)|DeleteAssignments|[Parameters](#ParametersdeviceAppManagement.mobileAppsDeleteAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileapp list-assignment](#deviceAppManagement.mobileAppsListAssignments)|ListAssignments|[Parameters](#ParametersdeviceAppManagement.mobileAppsListAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileapp list-category](#deviceAppManagement.mobileAppsListCategories)|ListCategories|[Parameters](#ParametersdeviceAppManagement.mobileAppsListCategories)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileapp list-ref-category](#deviceAppManagement.mobileAppsListRefCategories)|ListRefCategories|[Parameters](#ParametersdeviceAppManagement.mobileAppsListRefCategories)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileapp show-assignment](#deviceAppManagement.mobileAppsGetAssignments)|GetAssignments|[Parameters](#ParametersdeviceAppManagement.mobileAppsGetAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileapp update-assignment](#deviceAppManagement.mobileAppsUpdateAssignments)|UpdateAssignments|[Parameters](#ParametersdeviceAppManagement.mobileAppsUpdateAssignments)|Not Found|

### <a name="CommandsIndeviceAppManagement.mobileAppConfigurations">Commands in `az devicescorpmgt deviceappmanagementmobileappconfiguration` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration assign](#deviceAppManagement.mobileAppConfigurationsassign)|assign|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsassign)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration create-assignment](#deviceAppManagement.mobileAppConfigurationsCreateAssignments)|CreateAssignments|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsCreateAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration create-device-statuses](#deviceAppManagement.mobileAppConfigurationsCreateDeviceStatuses)|CreateDeviceStatuses|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsCreateDeviceStatuses)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration create-user-statuses](#deviceAppManagement.mobileAppConfigurationsCreateUserStatuses)|CreateUserStatuses|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsCreateUserStatuses)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration delete-assignment](#deviceAppManagement.mobileAppConfigurationsDeleteAssignments)|DeleteAssignments|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsDeleteAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration delete-device-status-summary](#deviceAppManagement.mobileAppConfigurationsDeleteDeviceStatusSummary)|DeleteDeviceStatusSummary|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsDeleteDeviceStatusSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration delete-device-statuses](#deviceAppManagement.mobileAppConfigurationsDeleteDeviceStatuses)|DeleteDeviceStatuses|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsDeleteDeviceStatuses)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration delete-user-status-summary](#deviceAppManagement.mobileAppConfigurationsDeleteUserStatusSummary)|DeleteUserStatusSummary|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsDeleteUserStatusSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration delete-user-statuses](#deviceAppManagement.mobileAppConfigurationsDeleteUserStatuses)|DeleteUserStatuses|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsDeleteUserStatuses)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration list-assignment](#deviceAppManagement.mobileAppConfigurationsListAssignments)|ListAssignments|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsListAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration list-device-statuses](#deviceAppManagement.mobileAppConfigurationsListDeviceStatuses)|ListDeviceStatuses|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsListDeviceStatuses)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration list-user-statuses](#deviceAppManagement.mobileAppConfigurationsListUserStatuses)|ListUserStatuses|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsListUserStatuses)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration show-assignment](#deviceAppManagement.mobileAppConfigurationsGetAssignments)|GetAssignments|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsGetAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration show-device-status-summary](#deviceAppManagement.mobileAppConfigurationsGetDeviceStatusSummary)|GetDeviceStatusSummary|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsGetDeviceStatusSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration show-device-statuses](#deviceAppManagement.mobileAppConfigurationsGetDeviceStatuses)|GetDeviceStatuses|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsGetDeviceStatuses)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration show-user-status-summary](#deviceAppManagement.mobileAppConfigurationsGetUserStatusSummary)|GetUserStatusSummary|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsGetUserStatusSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration show-user-statuses](#deviceAppManagement.mobileAppConfigurationsGetUserStatuses)|GetUserStatuses|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsGetUserStatuses)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration update-assignment](#deviceAppManagement.mobileAppConfigurationsUpdateAssignments)|UpdateAssignments|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsUpdateAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration update-device-status-summary](#deviceAppManagement.mobileAppConfigurationsUpdateDeviceStatusSummary)|UpdateDeviceStatusSummary|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsUpdateDeviceStatusSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration update-device-statuses](#deviceAppManagement.mobileAppConfigurationsUpdateDeviceStatuses)|UpdateDeviceStatuses|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsUpdateDeviceStatuses)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration update-user-status-summary](#deviceAppManagement.mobileAppConfigurationsUpdateUserStatusSummary)|UpdateUserStatusSummary|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsUpdateUserStatusSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementmobileappconfiguration update-user-statuses](#deviceAppManagement.mobileAppConfigurationsUpdateUserStatuses)|UpdateUserStatuses|[Parameters](#ParametersdeviceAppManagement.mobileAppConfigurationsUpdateUserStatuses)|Not Found|

### <a name="CommandsIndeviceAppManagement.targetedManagedAppConfigurations">Commands in `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration assign](#deviceAppManagement.targetedManagedAppConfigurationsassign)|assign|[Parameters](#ParametersdeviceAppManagement.targetedManagedAppConfigurationsassign)|Not Found|
|[az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration create-app](#deviceAppManagement.targetedManagedAppConfigurationsCreateApps)|CreateApps|[Parameters](#ParametersdeviceAppManagement.targetedManagedAppConfigurationsCreateApps)|Not Found|
|[az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration create-assignment](#deviceAppManagement.targetedManagedAppConfigurationsCreateAssignments)|CreateAssignments|[Parameters](#ParametersdeviceAppManagement.targetedManagedAppConfigurationsCreateAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration delete-app](#deviceAppManagement.targetedManagedAppConfigurationsDeleteApps)|DeleteApps|[Parameters](#ParametersdeviceAppManagement.targetedManagedAppConfigurationsDeleteApps)|Not Found|
|[az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration delete-assignment](#deviceAppManagement.targetedManagedAppConfigurationsDeleteAssignments)|DeleteAssignments|[Parameters](#ParametersdeviceAppManagement.targetedManagedAppConfigurationsDeleteAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration delete-deployment-summary](#deviceAppManagement.targetedManagedAppConfigurationsDeleteDeploymentSummary)|DeleteDeploymentSummary|[Parameters](#ParametersdeviceAppManagement.targetedManagedAppConfigurationsDeleteDeploymentSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration list-app](#deviceAppManagement.targetedManagedAppConfigurationsListApps)|ListApps|[Parameters](#ParametersdeviceAppManagement.targetedManagedAppConfigurationsListApps)|Not Found|
|[az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration list-assignment](#deviceAppManagement.targetedManagedAppConfigurationsListAssignments)|ListAssignments|[Parameters](#ParametersdeviceAppManagement.targetedManagedAppConfigurationsListAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration show-app](#deviceAppManagement.targetedManagedAppConfigurationsGetApps)|GetApps|[Parameters](#ParametersdeviceAppManagement.targetedManagedAppConfigurationsGetApps)|Not Found|
|[az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration show-assignment](#deviceAppManagement.targetedManagedAppConfigurationsGetAssignments)|GetAssignments|[Parameters](#ParametersdeviceAppManagement.targetedManagedAppConfigurationsGetAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration show-deployment-summary](#deviceAppManagement.targetedManagedAppConfigurationsGetDeploymentSummary)|GetDeploymentSummary|[Parameters](#ParametersdeviceAppManagement.targetedManagedAppConfigurationsGetDeploymentSummary)|Not Found|
|[az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration target-app](#deviceAppManagement.targetedManagedAppConfigurationstargetApps)|targetApps|[Parameters](#ParametersdeviceAppManagement.targetedManagedAppConfigurationstargetApps)|Not Found|
|[az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration update-app](#deviceAppManagement.targetedManagedAppConfigurationsUpdateApps)|UpdateApps|[Parameters](#ParametersdeviceAppManagement.targetedManagedAppConfigurationsUpdateApps)|Not Found|
|[az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration update-assignment](#deviceAppManagement.targetedManagedAppConfigurationsUpdateAssignments)|UpdateAssignments|[Parameters](#ParametersdeviceAppManagement.targetedManagedAppConfigurationsUpdateAssignments)|Not Found|
|[az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration update-deployment-summary](#deviceAppManagement.targetedManagedAppConfigurationsUpdateDeploymentSummary)|UpdateDeploymentSummary|[Parameters](#ParametersdeviceAppManagement.targetedManagedAppConfigurationsUpdateDeploymentSummary)|Not Found|

### <a name="CommandsIndeviceAppManagement.vppTokens">Commands in `az devicescorpmgt deviceappmanagementvpptoken` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt deviceappmanagementvpptoken sync-license](#deviceAppManagement.vppTokenssyncLicenses)|syncLicenses|[Parameters](#ParametersdeviceAppManagement.vppTokenssyncLicenses)|Not Found|

### <a name="CommandsInusers">Commands in `az devicescorpmgt user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt user create-device-management-troubleshooting-event](#usersCreateDeviceManagementTroubleshootingEvents)|CreateDeviceManagementTroubleshootingEvents|[Parameters](#ParametersusersCreateDeviceManagementTroubleshootingEvents)|Not Found|
|[az devicescorpmgt user create-managed-device](#usersCreateManagedDevices)|CreateManagedDevices|[Parameters](#ParametersusersCreateManagedDevices)|Not Found|
|[az devicescorpmgt user create-ref-managed-app-registration](#usersCreateRefManagedAppRegistrations)|CreateRefManagedAppRegistrations|[Parameters](#ParametersusersCreateRefManagedAppRegistrations)|Not Found|
|[az devicescorpmgt user delete-device-management-troubleshooting-event](#usersDeleteDeviceManagementTroubleshootingEvents)|DeleteDeviceManagementTroubleshootingEvents|[Parameters](#ParametersusersDeleteDeviceManagementTroubleshootingEvents)|Not Found|
|[az devicescorpmgt user delete-managed-device](#usersDeleteManagedDevices)|DeleteManagedDevices|[Parameters](#ParametersusersDeleteManagedDevices)|Not Found|
|[az devicescorpmgt user list-device-management-troubleshooting-event](#usersListDeviceManagementTroubleshootingEvents)|ListDeviceManagementTroubleshootingEvents|[Parameters](#ParametersusersListDeviceManagementTroubleshootingEvents)|Not Found|
|[az devicescorpmgt user list-managed-app-registration](#usersListManagedAppRegistrations)|ListManagedAppRegistrations|[Parameters](#ParametersusersListManagedAppRegistrations)|Not Found|
|[az devicescorpmgt user list-managed-device](#usersListManagedDevices)|ListManagedDevices|[Parameters](#ParametersusersListManagedDevices)|Not Found|
|[az devicescorpmgt user list-ref-managed-app-registration](#usersListRefManagedAppRegistrations)|ListRefManagedAppRegistrations|[Parameters](#ParametersusersListRefManagedAppRegistrations)|Not Found|
|[az devicescorpmgt user show-device-management-troubleshooting-event](#usersGetDeviceManagementTroubleshootingEvents)|GetDeviceManagementTroubleshootingEvents|[Parameters](#ParametersusersGetDeviceManagementTroubleshootingEvents)|Not Found|
|[az devicescorpmgt user show-managed-device](#usersGetManagedDevices)|GetManagedDevices|[Parameters](#ParametersusersGetManagedDevices)|Not Found|
|[az devicescorpmgt user update-device-management-troubleshooting-event](#usersUpdateDeviceManagementTroubleshootingEvents)|UpdateDeviceManagementTroubleshootingEvents|[Parameters](#ParametersusersUpdateDeviceManagementTroubleshootingEvents)|Not Found|
|[az devicescorpmgt user update-managed-device](#usersUpdateManagedDevices)|UpdateManagedDevices|[Parameters](#ParametersusersUpdateManagedDevices)|Not Found|

### <a name="CommandsInusers.managedDevices">Commands in `az devicescorpmgt usersmanageddevice` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescorpmgt usersmanageddevice create-device-compliance-policy-state](#users.managedDevicesCreateDeviceCompliancePolicyStates)|CreateDeviceCompliancePolicyStates|[Parameters](#Parametersusers.managedDevicesCreateDeviceCompliancePolicyStates)|Not Found|
|[az devicescorpmgt usersmanageddevice create-device-configuration-state](#users.managedDevicesCreateDeviceConfigurationStates)|CreateDeviceConfigurationStates|[Parameters](#Parametersusers.managedDevicesCreateDeviceConfigurationStates)|Not Found|
|[az devicescorpmgt usersmanageddevice delete-device-category](#users.managedDevicesDeleteDeviceCategory)|DeleteDeviceCategory|[Parameters](#Parametersusers.managedDevicesDeleteDeviceCategory)|Not Found|
|[az devicescorpmgt usersmanageddevice delete-device-compliance-policy-state](#users.managedDevicesDeleteDeviceCompliancePolicyStates)|DeleteDeviceCompliancePolicyStates|[Parameters](#Parametersusers.managedDevicesDeleteDeviceCompliancePolicyStates)|Not Found|
|[az devicescorpmgt usersmanageddevice delete-device-configuration-state](#users.managedDevicesDeleteDeviceConfigurationStates)|DeleteDeviceConfigurationStates|[Parameters](#Parametersusers.managedDevicesDeleteDeviceConfigurationStates)|Not Found|
|[az devicescorpmgt usersmanageddevice list-device-compliance-policy-state](#users.managedDevicesListDeviceCompliancePolicyStates)|ListDeviceCompliancePolicyStates|[Parameters](#Parametersusers.managedDevicesListDeviceCompliancePolicyStates)|Not Found|
|[az devicescorpmgt usersmanageddevice list-device-configuration-state](#users.managedDevicesListDeviceConfigurationStates)|ListDeviceConfigurationStates|[Parameters](#Parametersusers.managedDevicesListDeviceConfigurationStates)|Not Found|
|[az devicescorpmgt usersmanageddevice show-device-category](#users.managedDevicesGetDeviceCategory)|GetDeviceCategory|[Parameters](#Parametersusers.managedDevicesGetDeviceCategory)|Not Found|
|[az devicescorpmgt usersmanageddevice show-device-compliance-policy-state](#users.managedDevicesGetDeviceCompliancePolicyStates)|GetDeviceCompliancePolicyStates|[Parameters](#Parametersusers.managedDevicesGetDeviceCompliancePolicyStates)|Not Found|
|[az devicescorpmgt usersmanageddevice show-device-configuration-state](#users.managedDevicesGetDeviceConfigurationStates)|GetDeviceConfigurationStates|[Parameters](#Parametersusers.managedDevicesGetDeviceConfigurationStates)|Not Found|
|[az devicescorpmgt usersmanageddevice update-device-category](#users.managedDevicesUpdateDeviceCategory)|UpdateDeviceCategory|[Parameters](#Parametersusers.managedDevicesUpdateDeviceCategory)|Not Found|
|[az devicescorpmgt usersmanageddevice update-device-compliance-policy-state](#users.managedDevicesUpdateDeviceCompliancePolicyStates)|UpdateDeviceCompliancePolicyStates|[Parameters](#Parametersusers.managedDevicesUpdateDeviceCompliancePolicyStates)|Not Found|
|[az devicescorpmgt usersmanageddevice update-device-configuration-state](#users.managedDevicesUpdateDeviceConfigurationStates)|UpdateDeviceConfigurationStates|[Parameters](#Parametersusers.managedDevicesUpdateDeviceConfigurationStates)|Not Found|


## COMMAND DETAILS
### group `az devicescorpmgt deviceappmanagement`
#### <a name="deviceAppManagementCreateAndroidManagedAppProtections">Command `az devicescorpmgt deviceappmanagement create-android-managed-app-protection`</a>


##### <a name="ParametersdeviceAppManagementCreateAndroidManagedAppProtections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New navigation property|body|body|

#### <a name="deviceAppManagementCreateDefaultManagedAppProtections">Command `az devicescorpmgt deviceappmanagement create-default-managed-app-protection`</a>


##### <a name="ParametersdeviceAppManagementCreateDefaultManagedAppProtections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New navigation property|body|body|

#### <a name="deviceAppManagementCreateIosManagedAppProtections">Command `az devicescorpmgt deviceappmanagement create-io-managed-app-protection`</a>


##### <a name="ParametersdeviceAppManagementCreateIosManagedAppProtections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New navigation property|body|body|

#### <a name="deviceAppManagementCreateManagedAppPolicies">Command `az devicescorpmgt deviceappmanagement create-managed-app-policy`</a>


##### <a name="ParametersdeviceAppManagementCreateManagedAppPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagementCreateManagedAppRegistrations">Command `az devicescorpmgt deviceappmanagement create-managed-app-registration`</a>


##### <a name="ParametersdeviceAppManagementCreateManagedAppRegistrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--app-identifier**|dictionary|The identifier for a mobile app.|app_identifier|appIdentifier|
|**--application-version**|string|App version|application_version|applicationVersion|
|**--created-date-time**|date-time|Date and time of creation|created_date_time|createdDateTime|
|**--device-name**|string|Host device name|device_name|deviceName|
|**--device-tag**|string|App management SDK generated tag, which helps relate apps hosted on the same device. Not guaranteed to relate apps in all conditions.|device_tag|deviceTag|
|**--device-type**|string|Host device type|device_type|deviceType|
|**--flagged-reasons**|array|Zero or more reasons an app registration is flagged. E.g. app running on rooted device|flagged_reasons|flaggedReasons|
|**--last-sync-date-time**|date-time|Date and time of last the app synced with management service.|last_sync_date_time|lastSyncDateTime|
|**--management-sdk-version**|string|App management SDK version|management_sdk_version|managementSdkVersion|
|**--platform-version**|string|Operating System version|platform_version|platformVersion|
|**--user-id**|string|The user Id to who this app registration belongs.|user_id|userId|
|**--version**|string|Version of the entity.|version|version|
|**--applied-policies**|array|Zero or more policys already applied on the registered app when it last synchronized with managment service.|applied_policies|appliedPolicies|
|**--intended-policies**|array|Zero or more policies admin intended for the app as of now.|intended_policies|intendedPolicies|
|**--operations**|array|Zero or more long running operations triggered on the app registration.|operations|operations|

#### <a name="deviceAppManagementCreateManagedAppStatuses">Command `az devicescorpmgt deviceappmanagement create-managed-app-statuses`</a>


##### <a name="ParametersdeviceAppManagementCreateManagedAppStatuses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|Friendly name of the status report.|display_name|displayName|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagementCreateManagedEBooks">Command `az devicescorpmgt deviceappmanagement create-managed-e-book`</a>


##### <a name="ParametersdeviceAppManagementCreateManagedEBooks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time when the eBook file was created.|created_date_time|createdDateTime|
|**--description**|string|Description.|description|description|
|**--display-name**|string|Name of the eBook.|display_name|displayName|
|**--information-url**|string|The more information Url.|information_url|informationUrl|
|**--large-cover**|object|Contains properties for a generic mime content.|large_cover|largeCover|
|**--last-modified-date-time**|date-time|The date and time when the eBook was last modified.|last_modified_date_time|lastModifiedDateTime|
|**--privacy-information-url**|string|The privacy statement Url.|privacy_information_url|privacyInformationUrl|
|**--published-date-time**|date-time|The date and time when the eBook was published.|published_date_time|publishedDateTime|
|**--publisher**|string|Publisher.|publisher|publisher|
|**--assignments**|array|The list of assignments for this eBook.|assignments|assignments|
|**--device-states**|array|The list of installation states for this eBook.|device_states|deviceStates|
|**--install-summary**|object|Contains properties for the installation summary of a book for a device.|install_summary|installSummary|
|**--user-state-summary**|array|The list of installation states for this eBook.|user_state_summary|userStateSummary|

#### <a name="deviceAppManagementCreateMdmWindowsInformationProtectionPolicies">Command `az devicescorpmgt deviceappmanagement create-mdm-window-information-protection-policy`</a>


##### <a name="ParametersdeviceAppManagementCreateMdmWindowsInformationProtectionPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|
|**--azure-rights-management-services-allowed**|boolean|Specifies whether to allow Azure RMS encryption for WIP|azure_rights_management_services_allowed|azureRightsManagementServicesAllowed|
|**--data-recovery-certificate**|object|Windows Information Protection DataRecoveryCertificate|data_recovery_certificate|dataRecoveryCertificate|
|**--enforcement-level**|choice||enforcement_level|enforcementLevel|
|**--enterprise-domain**|string|Primary enterprise domain|enterprise_domain|enterpriseDomain|
|**--enterprise-internal-proxy-servers**|array|This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseProxiedDomains policy to force traffic to the matched domains through these proxies|enterprise_internal_proxy_servers|enterpriseInternalProxyServers|
|**--enterprise-ip-ranges**|array|Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to|enterprise_ip_ranges|enterpriseIPRanges|
|**--enterprise-ip-ranges-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false|enterprise_ip_ranges_are_authoritative|enterpriseIPRangesAreAuthoritative|
|**--enterprise-network-domain-names**|array|This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected These locations will be considered a safe destination for enterprise data to be shared to|enterprise_network_domain_names|enterpriseNetworkDomainNames|
|**--enterprise-protected-domain-names**|array|List of enterprise domains to be protected|enterprise_protected_domain_names|enterpriseProtectedDomainNames|
|**--enterprise-proxied-domains**|array|Contains a list of Enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy|enterprise_proxied_domains|enterpriseProxiedDomains|
|**--enterprise-proxy-servers**|array|This is a list of proxy servers. Any server not on this list is considered non-enterprise|enterprise_proxy_servers|enterpriseProxyServers|
|**--enterprise-proxy-servers-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false|enterprise_proxy_servers_are_authoritative|enterpriseProxyServersAreAuthoritative|
|**--exempt-apps**|array|Exempt applications can also access enterprise data, but the data handled by those applications are not protected. This is because some critical enterprise applications may have compatibility problems with encrypted data.|exempt_apps|exemptApps|
|**--icons-visible**|boolean|Determines whether overlays are added to icons for WIP protected files in Explorer and enterprise only app tiles in the Start menu. Starting in Windows 10, version 1703 this setting also configures the visibility of the WIP icon in the title bar of a WIP-protected app|icons_visible|iconsVisible|
|**--indexing-encrypted-stores-or-items-blocked**|boolean|This switch is for the Windows Search Indexer, to allow or disallow indexing of items|indexing_encrypted_stores_or_items_blocked|indexingEncryptedStoresOrItemsBlocked|
|**--is-assigned**|boolean|Indicates if the policy is deployed to any inclusion groups or not.|is_assigned|isAssigned|
|**--neutral-domain-resources**|array|List of domain names that can used for work or personal resource|neutral_domain_resources|neutralDomainResources|
|**--protected-apps**|array|Protected applications can access enterprise data and the data handled by those applications are protected with encryption|protected_apps|protectedApps|
|**--protection-under-lock-config-required**|boolean|Specifies whether the protection under lock feature (also known as encrypt under pin) should be configured|protection_under_lock_config_required|protectionUnderLockConfigRequired|
|**--revoke-on-unenroll-disabled**|boolean|This policy controls whether to revoke the WIP keys when a device unenrolls from the management service. If set to 1 (Don't revoke keys), the keys will not be revoked and the user will continue to have access to protected files after unenrollment. If the keys are not revoked, there will be no revoked file cleanup subsequently.|revoke_on_unenroll_disabled|revokeOnUnenrollDisabled|
|**--rights-management-services-template-id**|uuid|TemplateID GUID to use for RMS encryption. The RMS template allows the IT admin to configure the details about who has access to RMS-protected file and how long they have access|rights_management_services_template_id|rightsManagementServicesTemplateId|
|**--smb-auto-encrypted-file-extensions**|array|Specifies a list of file extensions, so that files with these extensions are encrypted when copying from an SMB share within the corporate boundary|smb_auto_encrypted_file_extensions|smbAutoEncryptedFileExtensions|
|**--assignments**|array|Navigation property to list of security groups targeted for policy.|assignments|assignments|
|**--exempt-app-locker-files**|array|Another way to input exempt apps through xml files|exempt_app_locker_files|exemptAppLockerFiles|
|**--protected-app-locker-files**|array|Another way to input protected apps through xml files|protected_app_locker_files|protectedAppLockerFiles|

#### <a name="deviceAppManagementCreateMobileApps">Command `az devicescorpmgt deviceappmanagement create-mobile-app`</a>


##### <a name="ParametersdeviceAppManagementCreateMobileApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the app was created.|created_date_time|createdDateTime|
|**--description**|string|The description of the app.|description|description|
|**--developer**|string|The developer of the app.|developer|developer|
|**--display-name**|string|The admin provided or imported title of the app.|display_name|displayName|
|**--information-url**|string|The more information Url.|information_url|informationUrl|
|**--is-featured**|boolean|The value indicating whether the app is marked as featured by the admin.|is_featured|isFeatured|
|**--large-icon**|object|Contains properties for a generic mime content.|large_icon|largeIcon|
|**--last-modified-date-time**|date-time|The date and time the app was last modified.|last_modified_date_time|lastModifiedDateTime|
|**--notes**|string|Notes for the app.|notes|notes|
|**--owner**|string|The owner of the app.|owner|owner|
|**--privacy-information-url**|string|The privacy statement Url.|privacy_information_url|privacyInformationUrl|
|**--publisher**|string|The publisher of the app.|publisher|publisher|
|**--publishing-state**|choice||publishing_state|publishingState|
|**--assignments**|array|The list of group assignments for this mobile app.|assignments|assignments|
|**--categories**|array|The list of categories for this app.|categories|categories|

#### <a name="deviceAppManagementCreateMobileAppCategories">Command `az devicescorpmgt deviceappmanagement create-mobile-app-category`</a>


##### <a name="ParametersdeviceAppManagementCreateMobileAppCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The name of the app category.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time the mobileAppCategory was last modified.|last_modified_date_time|lastModifiedDateTime|

#### <a name="deviceAppManagementCreateMobileAppConfigurations">Command `az devicescorpmgt deviceappmanagement create-mobile-app-configuration`</a>


##### <a name="ParametersdeviceAppManagementCreateMobileAppConfigurations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|DateTime the object was created.|created_date_time|createdDateTime|
|**--description**|string|Admin provided description of the Device Configuration.|description|description|
|**--display-name**|string|Admin provided name of the device configuration.|display_name|displayName|
|**--last-modified-date-time**|date-time|DateTime the object was last modified.|last_modified_date_time|lastModifiedDateTime|
|**--targeted-mobile-apps**|array|the associated app.|targeted_mobile_apps|targetedMobileApps|
|**--version**|integer|Version of the device configuration.|version|version|
|**--assignments**|array|The list of group assignemenets for app configration.|assignments|assignments|
|**--device-statuses**|array|List of ManagedDeviceMobileAppConfigurationDeviceStatus.|device_statuses|deviceStatuses|
|**--device-status-summary**|object|Contains properties, inherited properties and actions for an MDM mobile app configuration device status summary.|device_status_summary|deviceStatusSummary|
|**--user-statuses**|array|List of ManagedDeviceMobileAppConfigurationUserStatus.|user_statuses|userStatuses|
|**--user-status-summary**|object|Contains properties, inherited properties and actions for an MDM mobile app configuration user status summary.|user_status_summary|userStatusSummary|

#### <a name="deviceAppManagementCreateTargetedManagedAppConfigurations">Command `az devicescorpmgt deviceappmanagement create-targeted-managed-app-configuration`</a>


##### <a name="ParametersdeviceAppManagementCreateTargetedManagedAppConfigurations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|
|**--custom-settings**|array|A set of string key and string value pairs to be sent to apps for users to whom the configuration is scoped, unalterned by this service|custom_settings|customSettings|
|**--deployed-app-count**|integer|Count of apps to which the current policy is deployed.|deployed_app_count|deployedAppCount|
|**--is-assigned**|boolean|Indicates if the policy is deployed to any inclusion groups or not.|is_assigned|isAssigned|
|**--apps**|array|List of apps to which the policy is deployed.|apps|apps|
|**--assignments**|array|Navigation property to list of inclusion and exclusion groups to which the policy is deployed.|assignments|assignments|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--configuration-deployed-user-count**|integer|Not yet documented|configuration_deployed_user_count|configurationDeployedUserCount|
|**--configuration-deployment-summary-per-app**|array|Not yet documented|configuration_deployment_summary_per_app|configurationDeploymentSummaryPerApp|
|**--microsoft-graph-managed-app-policy-deployment-summary-display-name**|string|Not yet documented|microsoft_graph_managed_app_policy_deployment_summary_display_name|displayName|
|**--last-refresh-time**|date-time|Not yet documented|last_refresh_time|lastRefreshTime|
|**--microsoft-graph-managed-app-policy-deployment-summary-version**|string|Version of the entity.|microsoft_graph_managed_app_policy_deployment_summary_version|version|

#### <a name="deviceAppManagementCreateVppTokens">Command `az devicescorpmgt deviceappmanagement create-vpp-token`</a>


##### <a name="ParametersdeviceAppManagementCreateVppTokens">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--apple-id**|string|The apple Id associated with the given Apple Volume Purchase Program Token.|apple_id|appleId|
|**--automatically-update-apps**|boolean|Whether or not apps for the VPP token will be automatically updated.|automatically_update_apps|automaticallyUpdateApps|
|**--country-or-region**|string|Whether or not apps for the VPP token will be automatically updated.|country_or_region|countryOrRegion|
|**--expiration-date-time**|date-time|The expiration date time of the Apple Volume Purchase Program Token.|expiration_date_time|expirationDateTime|
|**--last-modified-date-time**|date-time|Last modification date time associated with the Apple Volume Purchase Program Token.|last_modified_date_time|lastModifiedDateTime|
|**--last-sync-date-time**|date-time|The last time when an application sync was done with the Apple volume purchase program service using the Apple Volume Purchase Program Token.|last_sync_date_time|lastSyncDateTime|
|**--last-sync-status**|choice||last_sync_status|lastSyncStatus|
|**--organization-name**|string|The organization associated with the Apple Volume Purchase Program Token|organization_name|organizationName|
|**--state**|choice||state|state|
|**--token**|string|The Apple Volume Purchase Program Token string downloaded from the Apple Volume Purchase Program.|token|token|
|**--vpp-token-account-type**|choice||vpp_token_account_type|vppTokenAccountType|

#### <a name="deviceAppManagementCreateWindowsInformationProtectionPolicies">Command `az devicescorpmgt deviceappmanagement create-window-information-protection-policy`</a>


##### <a name="ParametersdeviceAppManagementCreateWindowsInformationProtectionPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|
|**--azure-rights-management-services-allowed**|boolean|Specifies whether to allow Azure RMS encryption for WIP|azure_rights_management_services_allowed|azureRightsManagementServicesAllowed|
|**--data-recovery-certificate**|object|Windows Information Protection DataRecoveryCertificate|data_recovery_certificate|dataRecoveryCertificate|
|**--enforcement-level**|choice||enforcement_level|enforcementLevel|
|**--enterprise-domain**|string|Primary enterprise domain|enterprise_domain|enterpriseDomain|
|**--enterprise-internal-proxy-servers**|array|This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseProxiedDomains policy to force traffic to the matched domains through these proxies|enterprise_internal_proxy_servers|enterpriseInternalProxyServers|
|**--enterprise-ip-ranges**|array|Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to|enterprise_ip_ranges|enterpriseIPRanges|
|**--enterprise-ip-ranges-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false|enterprise_ip_ranges_are_authoritative|enterpriseIPRangesAreAuthoritative|
|**--enterprise-network-domain-names**|array|This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected These locations will be considered a safe destination for enterprise data to be shared to|enterprise_network_domain_names|enterpriseNetworkDomainNames|
|**--enterprise-protected-domain-names**|array|List of enterprise domains to be protected|enterprise_protected_domain_names|enterpriseProtectedDomainNames|
|**--enterprise-proxied-domains**|array|Contains a list of Enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy|enterprise_proxied_domains|enterpriseProxiedDomains|
|**--enterprise-proxy-servers**|array|This is a list of proxy servers. Any server not on this list is considered non-enterprise|enterprise_proxy_servers|enterpriseProxyServers|
|**--enterprise-proxy-servers-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false|enterprise_proxy_servers_are_authoritative|enterpriseProxyServersAreAuthoritative|
|**--exempt-apps**|array|Exempt applications can also access enterprise data, but the data handled by those applications are not protected. This is because some critical enterprise applications may have compatibility problems with encrypted data.|exempt_apps|exemptApps|
|**--icons-visible**|boolean|Determines whether overlays are added to icons for WIP protected files in Explorer and enterprise only app tiles in the Start menu. Starting in Windows 10, version 1703 this setting also configures the visibility of the WIP icon in the title bar of a WIP-protected app|icons_visible|iconsVisible|
|**--indexing-encrypted-stores-or-items-blocked**|boolean|This switch is for the Windows Search Indexer, to allow or disallow indexing of items|indexing_encrypted_stores_or_items_blocked|indexingEncryptedStoresOrItemsBlocked|
|**--is-assigned**|boolean|Indicates if the policy is deployed to any inclusion groups or not.|is_assigned|isAssigned|
|**--neutral-domain-resources**|array|List of domain names that can used for work or personal resource|neutral_domain_resources|neutralDomainResources|
|**--protected-apps**|array|Protected applications can access enterprise data and the data handled by those applications are protected with encryption|protected_apps|protectedApps|
|**--protection-under-lock-config-required**|boolean|Specifies whether the protection under lock feature (also known as encrypt under pin) should be configured|protection_under_lock_config_required|protectionUnderLockConfigRequired|
|**--revoke-on-unenroll-disabled**|boolean|This policy controls whether to revoke the WIP keys when a device unenrolls from the management service. If set to 1 (Don't revoke keys), the keys will not be revoked and the user will continue to have access to protected files after unenrollment. If the keys are not revoked, there will be no revoked file cleanup subsequently.|revoke_on_unenroll_disabled|revokeOnUnenrollDisabled|
|**--rights-management-services-template-id**|uuid|TemplateID GUID to use for RMS encryption. The RMS template allows the IT admin to configure the details about who has access to RMS-protected file and how long they have access|rights_management_services_template_id|rightsManagementServicesTemplateId|
|**--smb-auto-encrypted-file-extensions**|array|Specifies a list of file extensions, so that files with these extensions are encrypted when copying from an SMB share within the corporate boundary|smb_auto_encrypted_file_extensions|smbAutoEncryptedFileExtensions|
|**--assignments**|array|Navigation property to list of security groups targeted for policy.|assignments|assignments|
|**--exempt-app-locker-files**|array|Another way to input exempt apps through xml files|exempt_app_locker_files|exemptAppLockerFiles|
|**--protected-app-locker-files**|array|Another way to input protected apps through xml files|protected_app_locker_files|protectedAppLockerFiles|
|**--days-without-contact-before-unenroll**|integer|Offline interval before app data is wiped (days)|days_without_contact_before_unenroll|daysWithoutContactBeforeUnenroll|
|**--mdm-enrollment-url**|string|Enrollment url for the MDM|mdm_enrollment_url|mdmEnrollmentUrl|
|**--minutes-of-inactivity-before-device-lock**|integer|Specifies the maximum amount of time (in minutes) allowed after the device is idle that will cause the device to become PIN or password locked.   Range is an integer X where 0 <= X <= 999.|minutes_of_inactivity_before_device_lock|minutesOfInactivityBeforeDeviceLock|
|**--number-of-past-pins-remembered**|integer|Integer value that specifies the number of past PINs that can be associated to a user account that can't be reused. The largest number you can configure for this policy setting is 50. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then storage of previous PINs is not required. This node was added in Windows 10, version 1511. Default is 0.|number_of_past_pins_remembered|numberOfPastPinsRemembered|
|**--password-maximum-attempt-count**|integer|The number of authentication failures allowed before the device will be wiped. A value of 0 disables device wipe functionality. Range is an integer X where 4 <= X <= 16 for desktop and 0 <= X <= 999 for mobile devices.|password_maximum_attempt_count|passwordMaximumAttemptCount|
|**--pin-expiration-days**|integer|Integer value specifies the period of time (in days) that a PIN can be used before the system requires the user to change it. The largest number you can configure for this policy setting is 730. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then the user's PIN will never expire. This node was added in Windows 10, version 1511. Default is 0.|pin_expiration_days|pinExpirationDays|
|**--pin-lowercase-letters**|choice||pin_lowercase_letters|pinLowercaseLetters|
|**--pin-minimum-length**|integer|Integer value that sets the minimum number of characters required for the PIN. Default value is 4. The lowest number you can configure for this policy setting is 4. The largest number you can configure must be less than the number configured in the Maximum PIN length policy setting or the number 127, whichever is the lowest.|pin_minimum_length|pinMinimumLength|
|**--pin-special-characters**|choice||pin_special_characters|pinSpecialCharacters|
|**--pin-uppercase-letters**|choice||pin_uppercase_letters|pinUppercaseLetters|
|**--revoke-on-mdm-handoff-disabled**|boolean|New property in RS2, pending documentation|revoke_on_mdm_handoff_disabled|revokeOnMdmHandoffDisabled|
|**--windows-hello-for-business-blocked**|boolean|Boolean value that sets Windows Hello for Business as a method for signing into Windows.|windows_hello_for_business_blocked|windowsHelloForBusinessBlocked|

#### <a name="deviceAppManagementDeleteAndroidManagedAppProtections">Command `az devicescorpmgt deviceappmanagement delete-android-managed-app-protection`</a>


##### <a name="ParametersdeviceAppManagementDeleteAndroidManagedAppProtections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--android-managed-app-protection-id**|string|key: id of androidManagedAppProtection|android_managed_app_protection_id|androidManagedAppProtection-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagementDeleteDefaultManagedAppProtections">Command `az devicescorpmgt deviceappmanagement delete-default-managed-app-protection`</a>


##### <a name="ParametersdeviceAppManagementDeleteDefaultManagedAppProtections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--default-managed-app-protection-id**|string|key: id of defaultManagedAppProtection|default_managed_app_protection_id|defaultManagedAppProtection-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagementDeleteIosManagedAppProtections">Command `az devicescorpmgt deviceappmanagement delete-io-managed-app-protection`</a>


##### <a name="ParametersdeviceAppManagementDeleteIosManagedAppProtections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ios-managed-app-protection-id**|string|key: id of iosManagedAppProtection|ios_managed_app_protection_id|iosManagedAppProtection-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagementDeleteManagedAppPolicies">Command `az devicescorpmgt deviceappmanagement delete-managed-app-policy`</a>


##### <a name="ParametersdeviceAppManagementDeleteManagedAppPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagementDeleteManagedAppRegistrations">Command `az devicescorpmgt deviceappmanagement delete-managed-app-registration`</a>


##### <a name="ParametersdeviceAppManagementDeleteManagedAppRegistrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagementDeleteManagedAppStatuses">Command `az devicescorpmgt deviceappmanagement delete-managed-app-statuses`</a>


##### <a name="ParametersdeviceAppManagementDeleteManagedAppStatuses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-status-id**|string|key: id of managedAppStatus|managed_app_status_id|managedAppStatus-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagementDeleteManagedEBooks">Command `az devicescorpmgt deviceappmanagement delete-managed-e-book`</a>


##### <a name="ParametersdeviceAppManagementDeleteManagedEBooks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagementDeleteMdmWindowsInformationProtectionPolicies">Command `az devicescorpmgt deviceappmanagement delete-mdm-window-information-protection-policy`</a>


##### <a name="ParametersdeviceAppManagementDeleteMdmWindowsInformationProtectionPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mdm-windows-information-protection-policy-id**|string|key: id of mdmWindowsInformationProtectionPolicy|mdm_windows_information_protection_policy_id|mdmWindowsInformationProtectionPolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagementDeleteMobileApps">Command `az devicescorpmgt deviceappmanagement delete-mobile-app`</a>


##### <a name="ParametersdeviceAppManagementDeleteMobileApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagementDeleteMobileAppCategories">Command `az devicescorpmgt deviceappmanagement delete-mobile-app-category`</a>


##### <a name="ParametersdeviceAppManagementDeleteMobileAppCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-category-id**|string|key: id of mobileAppCategory|mobile_app_category_id|mobileAppCategory-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagementDeleteMobileAppConfigurations">Command `az devicescorpmgt deviceappmanagement delete-mobile-app-configuration`</a>


##### <a name="ParametersdeviceAppManagementDeleteMobileAppConfigurations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagementDeleteTargetedManagedAppConfigurations">Command `az devicescorpmgt deviceappmanagement delete-targeted-managed-app-configuration`</a>


##### <a name="ParametersdeviceAppManagementDeleteTargetedManagedAppConfigurations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagementDeleteVppTokens">Command `az devicescorpmgt deviceappmanagement delete-vpp-token`</a>


##### <a name="ParametersdeviceAppManagementDeleteVppTokens">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vpp-token-id**|string|key: id of vppToken|vpp_token_id|vppToken-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagementDeleteWindowsInformationProtectionPolicies">Command `az devicescorpmgt deviceappmanagement delete-window-information-protection-policy`</a>


##### <a name="ParametersdeviceAppManagementDeleteWindowsInformationProtectionPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--windows-information-protection-policy-id**|string|key: id of windowsInformationProtectionPolicy|windows_information_protection_policy_id|windowsInformationProtectionPolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagementListAndroidManagedAppProtections">Command `az devicescorpmgt deviceappmanagement list-android-managed-app-protection`</a>


##### <a name="ParametersdeviceAppManagementListAndroidManagedAppProtections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementListDefaultManagedAppProtections">Command `az devicescorpmgt deviceappmanagement list-default-managed-app-protection`</a>


##### <a name="ParametersdeviceAppManagementListDefaultManagedAppProtections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementListIosManagedAppProtections">Command `az devicescorpmgt deviceappmanagement list-io-managed-app-protection`</a>


##### <a name="ParametersdeviceAppManagementListIosManagedAppProtections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementListManagedAppPolicies">Command `az devicescorpmgt deviceappmanagement list-managed-app-policy`</a>


##### <a name="ParametersdeviceAppManagementListManagedAppPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementListManagedAppRegistrations">Command `az devicescorpmgt deviceappmanagement list-managed-app-registration`</a>


##### <a name="ParametersdeviceAppManagementListManagedAppRegistrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementListManagedAppStatuses">Command `az devicescorpmgt deviceappmanagement list-managed-app-statuses`</a>


##### <a name="ParametersdeviceAppManagementListManagedAppStatuses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementListManagedEBooks">Command `az devicescorpmgt deviceappmanagement list-managed-e-book`</a>


##### <a name="ParametersdeviceAppManagementListManagedEBooks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementListMdmWindowsInformationProtectionPolicies">Command `az devicescorpmgt deviceappmanagement list-mdm-window-information-protection-policy`</a>


##### <a name="ParametersdeviceAppManagementListMdmWindowsInformationProtectionPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementListMobileApps">Command `az devicescorpmgt deviceappmanagement list-mobile-app`</a>


##### <a name="ParametersdeviceAppManagementListMobileApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementListMobileAppCategories">Command `az devicescorpmgt deviceappmanagement list-mobile-app-category`</a>


##### <a name="ParametersdeviceAppManagementListMobileAppCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementListMobileAppConfigurations">Command `az devicescorpmgt deviceappmanagement list-mobile-app-configuration`</a>


##### <a name="ParametersdeviceAppManagementListMobileAppConfigurations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementListTargetedManagedAppConfigurations">Command `az devicescorpmgt deviceappmanagement list-targeted-managed-app-configuration`</a>


##### <a name="ParametersdeviceAppManagementListTargetedManagedAppConfigurations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementListVppTokens">Command `az devicescorpmgt deviceappmanagement list-vpp-token`</a>


##### <a name="ParametersdeviceAppManagementListVppTokens">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementListWindowsInformationProtectionPolicies">Command `az devicescorpmgt deviceappmanagement list-window-information-protection-policy`</a>


##### <a name="ParametersdeviceAppManagementListWindowsInformationProtectionPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementGetAndroidManagedAppProtections">Command `az devicescorpmgt deviceappmanagement show-android-managed-app-protection`</a>


##### <a name="ParametersdeviceAppManagementGetAndroidManagedAppProtections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--android-managed-app-protection-id**|string|key: id of androidManagedAppProtection|android_managed_app_protection_id|androidManagedAppProtection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementGetDefaultManagedAppProtections">Command `az devicescorpmgt deviceappmanagement show-default-managed-app-protection`</a>


##### <a name="ParametersdeviceAppManagementGetDefaultManagedAppProtections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--default-managed-app-protection-id**|string|key: id of defaultManagedAppProtection|default_managed_app_protection_id|defaultManagedAppProtection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementGetIosManagedAppProtections">Command `az devicescorpmgt deviceappmanagement show-io-managed-app-protection`</a>


##### <a name="ParametersdeviceAppManagementGetIosManagedAppProtections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ios-managed-app-protection-id**|string|key: id of iosManagedAppProtection|ios_managed_app_protection_id|iosManagedAppProtection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementGetManagedAppPolicies">Command `az devicescorpmgt deviceappmanagement show-managed-app-policy`</a>


##### <a name="ParametersdeviceAppManagementGetManagedAppPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementGetManagedAppRegistrations">Command `az devicescorpmgt deviceappmanagement show-managed-app-registration`</a>


##### <a name="ParametersdeviceAppManagementGetManagedAppRegistrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementGetManagedAppStatuses">Command `az devicescorpmgt deviceappmanagement show-managed-app-statuses`</a>


##### <a name="ParametersdeviceAppManagementGetManagedAppStatuses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-status-id**|string|key: id of managedAppStatus|managed_app_status_id|managedAppStatus-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementGetManagedEBooks">Command `az devicescorpmgt deviceappmanagement show-managed-e-book`</a>


##### <a name="ParametersdeviceAppManagementGetManagedEBooks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementGetMdmWindowsInformationProtectionPolicies">Command `az devicescorpmgt deviceappmanagement show-mdm-window-information-protection-policy`</a>


##### <a name="ParametersdeviceAppManagementGetMdmWindowsInformationProtectionPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mdm-windows-information-protection-policy-id**|string|key: id of mdmWindowsInformationProtectionPolicy|mdm_windows_information_protection_policy_id|mdmWindowsInformationProtectionPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementGetMobileApps">Command `az devicescorpmgt deviceappmanagement show-mobile-app`</a>


##### <a name="ParametersdeviceAppManagementGetMobileApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementGetMobileAppCategories">Command `az devicescorpmgt deviceappmanagement show-mobile-app-category`</a>


##### <a name="ParametersdeviceAppManagementGetMobileAppCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-category-id**|string|key: id of mobileAppCategory|mobile_app_category_id|mobileAppCategory-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementGetMobileAppConfigurations">Command `az devicescorpmgt deviceappmanagement show-mobile-app-configuration`</a>


##### <a name="ParametersdeviceAppManagementGetMobileAppConfigurations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementGetTargetedManagedAppConfigurations">Command `az devicescorpmgt deviceappmanagement show-targeted-managed-app-configuration`</a>


##### <a name="ParametersdeviceAppManagementGetTargetedManagedAppConfigurations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementGetVppTokens">Command `az devicescorpmgt deviceappmanagement show-vpp-token`</a>


##### <a name="ParametersdeviceAppManagementGetVppTokens">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vpp-token-id**|string|key: id of vppToken|vpp_token_id|vppToken-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementGetWindowsInformationProtectionPolicies">Command `az devicescorpmgt deviceappmanagement show-window-information-protection-policy`</a>


##### <a name="ParametersdeviceAppManagementGetWindowsInformationProtectionPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--windows-information-protection-policy-id**|string|key: id of windowsInformationProtectionPolicy|windows_information_protection_policy_id|windowsInformationProtectionPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagementsyncMicrosoftStoreForBusinessApps">Command `az devicescorpmgt deviceappmanagement sync-microsoft-store-for-business-app`</a>


##### <a name="ParametersdeviceAppManagementsyncMicrosoftStoreForBusinessApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

#### <a name="deviceAppManagementUpdateAndroidManagedAppProtections">Command `az devicescorpmgt deviceappmanagement update-android-managed-app-protection`</a>


##### <a name="ParametersdeviceAppManagementUpdateAndroidManagedAppProtections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--android-managed-app-protection-id**|string|key: id of androidManagedAppProtection|android_managed_app_protection_id|androidManagedAppProtection-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="deviceAppManagementUpdateDefaultManagedAppProtections">Command `az devicescorpmgt deviceappmanagement update-default-managed-app-protection`</a>


##### <a name="ParametersdeviceAppManagementUpdateDefaultManagedAppProtections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--default-managed-app-protection-id**|string|key: id of defaultManagedAppProtection|default_managed_app_protection_id|defaultManagedAppProtection-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="deviceAppManagementUpdateIosManagedAppProtections">Command `az devicescorpmgt deviceappmanagement update-io-managed-app-protection`</a>


##### <a name="ParametersdeviceAppManagementUpdateIosManagedAppProtections">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ios-managed-app-protection-id**|string|key: id of iosManagedAppProtection|ios_managed_app_protection_id|iosManagedAppProtection-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="deviceAppManagementUpdateManagedAppPolicies">Command `az devicescorpmgt deviceappmanagement update-managed-app-policy`</a>


##### <a name="ParametersdeviceAppManagementUpdateManagedAppPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagementUpdateManagedAppRegistrations">Command `az devicescorpmgt deviceappmanagement update-managed-app-registration`</a>


##### <a name="ParametersdeviceAppManagementUpdateManagedAppRegistrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--id**|string|Read-only.|id|id|
|**--app-identifier**|dictionary|The identifier for a mobile app.|app_identifier|appIdentifier|
|**--application-version**|string|App version|application_version|applicationVersion|
|**--created-date-time**|date-time|Date and time of creation|created_date_time|createdDateTime|
|**--device-name**|string|Host device name|device_name|deviceName|
|**--device-tag**|string|App management SDK generated tag, which helps relate apps hosted on the same device. Not guaranteed to relate apps in all conditions.|device_tag|deviceTag|
|**--device-type**|string|Host device type|device_type|deviceType|
|**--flagged-reasons**|array|Zero or more reasons an app registration is flagged. E.g. app running on rooted device|flagged_reasons|flaggedReasons|
|**--last-sync-date-time**|date-time|Date and time of last the app synced with management service.|last_sync_date_time|lastSyncDateTime|
|**--management-sdk-version**|string|App management SDK version|management_sdk_version|managementSdkVersion|
|**--platform-version**|string|Operating System version|platform_version|platformVersion|
|**--user-id**|string|The user Id to who this app registration belongs.|user_id|userId|
|**--version**|string|Version of the entity.|version|version|
|**--applied-policies**|array|Zero or more policys already applied on the registered app when it last synchronized with managment service.|applied_policies|appliedPolicies|
|**--intended-policies**|array|Zero or more policies admin intended for the app as of now.|intended_policies|intendedPolicies|
|**--operations**|array|Zero or more long running operations triggered on the app registration.|operations|operations|

#### <a name="deviceAppManagementUpdateManagedAppStatuses">Command `az devicescorpmgt deviceappmanagement update-managed-app-statuses`</a>


##### <a name="ParametersdeviceAppManagementUpdateManagedAppStatuses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-status-id**|string|key: id of managedAppStatus|managed_app_status_id|managedAppStatus-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|Friendly name of the status report.|display_name|displayName|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagementUpdateManagedEBooks">Command `az devicescorpmgt deviceappmanagement update-managed-e-book`</a>


##### <a name="ParametersdeviceAppManagementUpdateManagedEBooks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time when the eBook file was created.|created_date_time|createdDateTime|
|**--description**|string|Description.|description|description|
|**--display-name**|string|Name of the eBook.|display_name|displayName|
|**--information-url**|string|The more information Url.|information_url|informationUrl|
|**--large-cover**|object|Contains properties for a generic mime content.|large_cover|largeCover|
|**--last-modified-date-time**|date-time|The date and time when the eBook was last modified.|last_modified_date_time|lastModifiedDateTime|
|**--privacy-information-url**|string|The privacy statement Url.|privacy_information_url|privacyInformationUrl|
|**--published-date-time**|date-time|The date and time when the eBook was published.|published_date_time|publishedDateTime|
|**--publisher**|string|Publisher.|publisher|publisher|
|**--assignments**|array|The list of assignments for this eBook.|assignments|assignments|
|**--device-states**|array|The list of installation states for this eBook.|device_states|deviceStates|
|**--install-summary**|object|Contains properties for the installation summary of a book for a device.|install_summary|installSummary|
|**--user-state-summary**|array|The list of installation states for this eBook.|user_state_summary|userStateSummary|

#### <a name="deviceAppManagementUpdateMdmWindowsInformationProtectionPolicies">Command `az devicescorpmgt deviceappmanagement update-mdm-window-information-protection-policy`</a>


##### <a name="ParametersdeviceAppManagementUpdateMdmWindowsInformationProtectionPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mdm-windows-information-protection-policy-id**|string|key: id of mdmWindowsInformationProtectionPolicy|mdm_windows_information_protection_policy_id|mdmWindowsInformationProtectionPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|
|**--azure-rights-management-services-allowed**|boolean|Specifies whether to allow Azure RMS encryption for WIP|azure_rights_management_services_allowed|azureRightsManagementServicesAllowed|
|**--data-recovery-certificate**|object|Windows Information Protection DataRecoveryCertificate|data_recovery_certificate|dataRecoveryCertificate|
|**--enforcement-level**|choice||enforcement_level|enforcementLevel|
|**--enterprise-domain**|string|Primary enterprise domain|enterprise_domain|enterpriseDomain|
|**--enterprise-internal-proxy-servers**|array|This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseProxiedDomains policy to force traffic to the matched domains through these proxies|enterprise_internal_proxy_servers|enterpriseInternalProxyServers|
|**--enterprise-ip-ranges**|array|Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to|enterprise_ip_ranges|enterpriseIPRanges|
|**--enterprise-ip-ranges-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false|enterprise_ip_ranges_are_authoritative|enterpriseIPRangesAreAuthoritative|
|**--enterprise-network-domain-names**|array|This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected These locations will be considered a safe destination for enterprise data to be shared to|enterprise_network_domain_names|enterpriseNetworkDomainNames|
|**--enterprise-protected-domain-names**|array|List of enterprise domains to be protected|enterprise_protected_domain_names|enterpriseProtectedDomainNames|
|**--enterprise-proxied-domains**|array|Contains a list of Enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy|enterprise_proxied_domains|enterpriseProxiedDomains|
|**--enterprise-proxy-servers**|array|This is a list of proxy servers. Any server not on this list is considered non-enterprise|enterprise_proxy_servers|enterpriseProxyServers|
|**--enterprise-proxy-servers-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false|enterprise_proxy_servers_are_authoritative|enterpriseProxyServersAreAuthoritative|
|**--exempt-apps**|array|Exempt applications can also access enterprise data, but the data handled by those applications are not protected. This is because some critical enterprise applications may have compatibility problems with encrypted data.|exempt_apps|exemptApps|
|**--icons-visible**|boolean|Determines whether overlays are added to icons for WIP protected files in Explorer and enterprise only app tiles in the Start menu. Starting in Windows 10, version 1703 this setting also configures the visibility of the WIP icon in the title bar of a WIP-protected app|icons_visible|iconsVisible|
|**--indexing-encrypted-stores-or-items-blocked**|boolean|This switch is for the Windows Search Indexer, to allow or disallow indexing of items|indexing_encrypted_stores_or_items_blocked|indexingEncryptedStoresOrItemsBlocked|
|**--is-assigned**|boolean|Indicates if the policy is deployed to any inclusion groups or not.|is_assigned|isAssigned|
|**--neutral-domain-resources**|array|List of domain names that can used for work or personal resource|neutral_domain_resources|neutralDomainResources|
|**--protected-apps**|array|Protected applications can access enterprise data and the data handled by those applications are protected with encryption|protected_apps|protectedApps|
|**--protection-under-lock-config-required**|boolean|Specifies whether the protection under lock feature (also known as encrypt under pin) should be configured|protection_under_lock_config_required|protectionUnderLockConfigRequired|
|**--revoke-on-unenroll-disabled**|boolean|This policy controls whether to revoke the WIP keys when a device unenrolls from the management service. If set to 1 (Don't revoke keys), the keys will not be revoked and the user will continue to have access to protected files after unenrollment. If the keys are not revoked, there will be no revoked file cleanup subsequently.|revoke_on_unenroll_disabled|revokeOnUnenrollDisabled|
|**--rights-management-services-template-id**|uuid|TemplateID GUID to use for RMS encryption. The RMS template allows the IT admin to configure the details about who has access to RMS-protected file and how long they have access|rights_management_services_template_id|rightsManagementServicesTemplateId|
|**--smb-auto-encrypted-file-extensions**|array|Specifies a list of file extensions, so that files with these extensions are encrypted when copying from an SMB share within the corporate boundary|smb_auto_encrypted_file_extensions|smbAutoEncryptedFileExtensions|
|**--assignments**|array|Navigation property to list of security groups targeted for policy.|assignments|assignments|
|**--exempt-app-locker-files**|array|Another way to input exempt apps through xml files|exempt_app_locker_files|exemptAppLockerFiles|
|**--protected-app-locker-files**|array|Another way to input protected apps through xml files|protected_app_locker_files|protectedAppLockerFiles|

#### <a name="deviceAppManagementUpdateMobileApps">Command `az devicescorpmgt deviceappmanagement update-mobile-app`</a>


##### <a name="ParametersdeviceAppManagementUpdateMobileApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the app was created.|created_date_time|createdDateTime|
|**--description**|string|The description of the app.|description|description|
|**--developer**|string|The developer of the app.|developer|developer|
|**--display-name**|string|The admin provided or imported title of the app.|display_name|displayName|
|**--information-url**|string|The more information Url.|information_url|informationUrl|
|**--is-featured**|boolean|The value indicating whether the app is marked as featured by the admin.|is_featured|isFeatured|
|**--large-icon**|object|Contains properties for a generic mime content.|large_icon|largeIcon|
|**--last-modified-date-time**|date-time|The date and time the app was last modified.|last_modified_date_time|lastModifiedDateTime|
|**--notes**|string|Notes for the app.|notes|notes|
|**--owner**|string|The owner of the app.|owner|owner|
|**--privacy-information-url**|string|The privacy statement Url.|privacy_information_url|privacyInformationUrl|
|**--publisher**|string|The publisher of the app.|publisher|publisher|
|**--publishing-state**|choice||publishing_state|publishingState|
|**--assignments**|array|The list of group assignments for this mobile app.|assignments|assignments|
|**--categories**|array|The list of categories for this app.|categories|categories|

#### <a name="deviceAppManagementUpdateMobileAppCategories">Command `az devicescorpmgt deviceappmanagement update-mobile-app-category`</a>


##### <a name="ParametersdeviceAppManagementUpdateMobileAppCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-category-id**|string|key: id of mobileAppCategory|mobile_app_category_id|mobileAppCategory-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The name of the app category.|display_name|displayName|
|**--last-modified-date-time**|date-time|The date and time the mobileAppCategory was last modified.|last_modified_date_time|lastModifiedDateTime|

#### <a name="deviceAppManagementUpdateMobileAppConfigurations">Command `az devicescorpmgt deviceappmanagement update-mobile-app-configuration`</a>


##### <a name="ParametersdeviceAppManagementUpdateMobileAppConfigurations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|DateTime the object was created.|created_date_time|createdDateTime|
|**--description**|string|Admin provided description of the Device Configuration.|description|description|
|**--display-name**|string|Admin provided name of the device configuration.|display_name|displayName|
|**--last-modified-date-time**|date-time|DateTime the object was last modified.|last_modified_date_time|lastModifiedDateTime|
|**--targeted-mobile-apps**|array|the associated app.|targeted_mobile_apps|targetedMobileApps|
|**--version**|integer|Version of the device configuration.|version|version|
|**--assignments**|array|The list of group assignemenets for app configration.|assignments|assignments|
|**--device-statuses**|array|List of ManagedDeviceMobileAppConfigurationDeviceStatus.|device_statuses|deviceStatuses|
|**--device-status-summary**|object|Contains properties, inherited properties and actions for an MDM mobile app configuration device status summary.|device_status_summary|deviceStatusSummary|
|**--user-statuses**|array|List of ManagedDeviceMobileAppConfigurationUserStatus.|user_statuses|userStatuses|
|**--user-status-summary**|object|Contains properties, inherited properties and actions for an MDM mobile app configuration user status summary.|user_status_summary|userStatusSummary|

#### <a name="deviceAppManagementUpdateTargetedManagedAppConfigurations">Command `az devicescorpmgt deviceappmanagement update-targeted-managed-app-configuration`</a>


##### <a name="ParametersdeviceAppManagementUpdateTargetedManagedAppConfigurations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|
|**--custom-settings**|array|A set of string key and string value pairs to be sent to apps for users to whom the configuration is scoped, unalterned by this service|custom_settings|customSettings|
|**--deployed-app-count**|integer|Count of apps to which the current policy is deployed.|deployed_app_count|deployedAppCount|
|**--is-assigned**|boolean|Indicates if the policy is deployed to any inclusion groups or not.|is_assigned|isAssigned|
|**--apps**|array|List of apps to which the policy is deployed.|apps|apps|
|**--assignments**|array|Navigation property to list of inclusion and exclusion groups to which the policy is deployed.|assignments|assignments|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--configuration-deployed-user-count**|integer|Not yet documented|configuration_deployed_user_count|configurationDeployedUserCount|
|**--configuration-deployment-summary-per-app**|array|Not yet documented|configuration_deployment_summary_per_app|configurationDeploymentSummaryPerApp|
|**--microsoft-graph-managed-app-policy-deployment-summary-display-name**|string|Not yet documented|microsoft_graph_managed_app_policy_deployment_summary_display_name|displayName|
|**--last-refresh-time**|date-time|Not yet documented|last_refresh_time|lastRefreshTime|
|**--microsoft-graph-managed-app-policy-deployment-summary-version**|string|Version of the entity.|microsoft_graph_managed_app_policy_deployment_summary_version|version|

#### <a name="deviceAppManagementUpdateVppTokens">Command `az devicescorpmgt deviceappmanagement update-vpp-token`</a>


##### <a name="ParametersdeviceAppManagementUpdateVppTokens">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vpp-token-id**|string|key: id of vppToken|vpp_token_id|vppToken-id|
|**--id**|string|Read-only.|id|id|
|**--apple-id**|string|The apple Id associated with the given Apple Volume Purchase Program Token.|apple_id|appleId|
|**--automatically-update-apps**|boolean|Whether or not apps for the VPP token will be automatically updated.|automatically_update_apps|automaticallyUpdateApps|
|**--country-or-region**|string|Whether or not apps for the VPP token will be automatically updated.|country_or_region|countryOrRegion|
|**--expiration-date-time**|date-time|The expiration date time of the Apple Volume Purchase Program Token.|expiration_date_time|expirationDateTime|
|**--last-modified-date-time**|date-time|Last modification date time associated with the Apple Volume Purchase Program Token.|last_modified_date_time|lastModifiedDateTime|
|**--last-sync-date-time**|date-time|The last time when an application sync was done with the Apple volume purchase program service using the Apple Volume Purchase Program Token.|last_sync_date_time|lastSyncDateTime|
|**--last-sync-status**|choice||last_sync_status|lastSyncStatus|
|**--organization-name**|string|The organization associated with the Apple Volume Purchase Program Token|organization_name|organizationName|
|**--state**|choice||state|state|
|**--token**|string|The Apple Volume Purchase Program Token string downloaded from the Apple Volume Purchase Program.|token|token|
|**--vpp-token-account-type**|choice||vpp_token_account_type|vppTokenAccountType|

#### <a name="deviceAppManagementUpdateWindowsInformationProtectionPolicies">Command `az devicescorpmgt deviceappmanagement update-window-information-protection-policy`</a>


##### <a name="ParametersdeviceAppManagementUpdateWindowsInformationProtectionPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--windows-information-protection-policy-id**|string|key: id of windowsInformationProtectionPolicy|windows_information_protection_policy_id|windowsInformationProtectionPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|
|**--azure-rights-management-services-allowed**|boolean|Specifies whether to allow Azure RMS encryption for WIP|azure_rights_management_services_allowed|azureRightsManagementServicesAllowed|
|**--data-recovery-certificate**|object|Windows Information Protection DataRecoveryCertificate|data_recovery_certificate|dataRecoveryCertificate|
|**--enforcement-level**|choice||enforcement_level|enforcementLevel|
|**--enterprise-domain**|string|Primary enterprise domain|enterprise_domain|enterpriseDomain|
|**--enterprise-internal-proxy-servers**|array|This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseProxiedDomains policy to force traffic to the matched domains through these proxies|enterprise_internal_proxy_servers|enterpriseInternalProxyServers|
|**--enterprise-ip-ranges**|array|Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to|enterprise_ip_ranges|enterpriseIPRanges|
|**--enterprise-ip-ranges-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false|enterprise_ip_ranges_are_authoritative|enterpriseIPRangesAreAuthoritative|
|**--enterprise-network-domain-names**|array|This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected These locations will be considered a safe destination for enterprise data to be shared to|enterprise_network_domain_names|enterpriseNetworkDomainNames|
|**--enterprise-protected-domain-names**|array|List of enterprise domains to be protected|enterprise_protected_domain_names|enterpriseProtectedDomainNames|
|**--enterprise-proxied-domains**|array|Contains a list of Enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy|enterprise_proxied_domains|enterpriseProxiedDomains|
|**--enterprise-proxy-servers**|array|This is a list of proxy servers. Any server not on this list is considered non-enterprise|enterprise_proxy_servers|enterpriseProxyServers|
|**--enterprise-proxy-servers-are-authoritative**|boolean|Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false|enterprise_proxy_servers_are_authoritative|enterpriseProxyServersAreAuthoritative|
|**--exempt-apps**|array|Exempt applications can also access enterprise data, but the data handled by those applications are not protected. This is because some critical enterprise applications may have compatibility problems with encrypted data.|exempt_apps|exemptApps|
|**--icons-visible**|boolean|Determines whether overlays are added to icons for WIP protected files in Explorer and enterprise only app tiles in the Start menu. Starting in Windows 10, version 1703 this setting also configures the visibility of the WIP icon in the title bar of a WIP-protected app|icons_visible|iconsVisible|
|**--indexing-encrypted-stores-or-items-blocked**|boolean|This switch is for the Windows Search Indexer, to allow or disallow indexing of items|indexing_encrypted_stores_or_items_blocked|indexingEncryptedStoresOrItemsBlocked|
|**--is-assigned**|boolean|Indicates if the policy is deployed to any inclusion groups or not.|is_assigned|isAssigned|
|**--neutral-domain-resources**|array|List of domain names that can used for work or personal resource|neutral_domain_resources|neutralDomainResources|
|**--protected-apps**|array|Protected applications can access enterprise data and the data handled by those applications are protected with encryption|protected_apps|protectedApps|
|**--protection-under-lock-config-required**|boolean|Specifies whether the protection under lock feature (also known as encrypt under pin) should be configured|protection_under_lock_config_required|protectionUnderLockConfigRequired|
|**--revoke-on-unenroll-disabled**|boolean|This policy controls whether to revoke the WIP keys when a device unenrolls from the management service. If set to 1 (Don't revoke keys), the keys will not be revoked and the user will continue to have access to protected files after unenrollment. If the keys are not revoked, there will be no revoked file cleanup subsequently.|revoke_on_unenroll_disabled|revokeOnUnenrollDisabled|
|**--rights-management-services-template-id**|uuid|TemplateID GUID to use for RMS encryption. The RMS template allows the IT admin to configure the details about who has access to RMS-protected file and how long they have access|rights_management_services_template_id|rightsManagementServicesTemplateId|
|**--smb-auto-encrypted-file-extensions**|array|Specifies a list of file extensions, so that files with these extensions are encrypted when copying from an SMB share within the corporate boundary|smb_auto_encrypted_file_extensions|smbAutoEncryptedFileExtensions|
|**--assignments**|array|Navigation property to list of security groups targeted for policy.|assignments|assignments|
|**--exempt-app-locker-files**|array|Another way to input exempt apps through xml files|exempt_app_locker_files|exemptAppLockerFiles|
|**--protected-app-locker-files**|array|Another way to input protected apps through xml files|protected_app_locker_files|protectedAppLockerFiles|
|**--days-without-contact-before-unenroll**|integer|Offline interval before app data is wiped (days)|days_without_contact_before_unenroll|daysWithoutContactBeforeUnenroll|
|**--mdm-enrollment-url**|string|Enrollment url for the MDM|mdm_enrollment_url|mdmEnrollmentUrl|
|**--minutes-of-inactivity-before-device-lock**|integer|Specifies the maximum amount of time (in minutes) allowed after the device is idle that will cause the device to become PIN or password locked.   Range is an integer X where 0 <= X <= 999.|minutes_of_inactivity_before_device_lock|minutesOfInactivityBeforeDeviceLock|
|**--number-of-past-pins-remembered**|integer|Integer value that specifies the number of past PINs that can be associated to a user account that can't be reused. The largest number you can configure for this policy setting is 50. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then storage of previous PINs is not required. This node was added in Windows 10, version 1511. Default is 0.|number_of_past_pins_remembered|numberOfPastPinsRemembered|
|**--password-maximum-attempt-count**|integer|The number of authentication failures allowed before the device will be wiped. A value of 0 disables device wipe functionality. Range is an integer X where 4 <= X <= 16 for desktop and 0 <= X <= 999 for mobile devices.|password_maximum_attempt_count|passwordMaximumAttemptCount|
|**--pin-expiration-days**|integer|Integer value specifies the period of time (in days) that a PIN can be used before the system requires the user to change it. The largest number you can configure for this policy setting is 730. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then the user's PIN will never expire. This node was added in Windows 10, version 1511. Default is 0.|pin_expiration_days|pinExpirationDays|
|**--pin-lowercase-letters**|choice||pin_lowercase_letters|pinLowercaseLetters|
|**--pin-minimum-length**|integer|Integer value that sets the minimum number of characters required for the PIN. Default value is 4. The lowest number you can configure for this policy setting is 4. The largest number you can configure must be less than the number configured in the Maximum PIN length policy setting or the number 127, whichever is the lowest.|pin_minimum_length|pinMinimumLength|
|**--pin-special-characters**|choice||pin_special_characters|pinSpecialCharacters|
|**--pin-uppercase-letters**|choice||pin_uppercase_letters|pinUppercaseLetters|
|**--revoke-on-mdm-handoff-disabled**|boolean|New property in RS2, pending documentation|revoke_on_mdm_handoff_disabled|revokeOnMdmHandoffDisabled|
|**--windows-hello-for-business-blocked**|boolean|Boolean value that sets Windows Hello for Business as a method for signing into Windows.|windows_hello_for_business_blocked|windowsHelloForBusinessBlocked|

### group `az devicescorpmgt deviceappmanagementandroidmanagedappprotection`
#### <a name="deviceAppManagement.androidManagedAppProtectionsCreateApps">Command `az devicescorpmgt deviceappmanagementandroidmanagedappprotection create-app`</a>


##### <a name="ParametersdeviceAppManagement.androidManagedAppProtectionsCreateApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--android-managed-app-protection-id**|string|key: id of androidManagedAppProtection|android_managed_app_protection_id|androidManagedAppProtection-id|
|**--id**|string|Read-only.|id|id|
|**--mobile-app-identifier**|dictionary|The identifier for a mobile app.|mobile_app_identifier|mobileAppIdentifier|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagement.androidManagedAppProtectionsDeleteApps">Command `az devicescorpmgt deviceappmanagementandroidmanagedappprotection delete-app`</a>


##### <a name="ParametersdeviceAppManagement.androidManagedAppProtectionsDeleteApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--android-managed-app-protection-id**|string|key: id of androidManagedAppProtection|android_managed_app_protection_id|androidManagedAppProtection-id|
|**--managed-mobile-app-id**|string|key: id of managedMobileApp|managed_mobile_app_id|managedMobileApp-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.androidManagedAppProtectionsDeleteDeploymentSummary">Command `az devicescorpmgt deviceappmanagementandroidmanagedappprotection delete-deployment-summary`</a>


##### <a name="ParametersdeviceAppManagement.androidManagedAppProtectionsDeleteDeploymentSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--android-managed-app-protection-id**|string|key: id of androidManagedAppProtection|android_managed_app_protection_id|androidManagedAppProtection-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.androidManagedAppProtectionsListApps">Command `az devicescorpmgt deviceappmanagementandroidmanagedappprotection list-app`</a>


##### <a name="ParametersdeviceAppManagement.androidManagedAppProtectionsListApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--android-managed-app-protection-id**|string|key: id of androidManagedAppProtection|android_managed_app_protection_id|androidManagedAppProtection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.androidManagedAppProtectionsGetApps">Command `az devicescorpmgt deviceappmanagementandroidmanagedappprotection show-app`</a>


##### <a name="ParametersdeviceAppManagement.androidManagedAppProtectionsGetApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--android-managed-app-protection-id**|string|key: id of androidManagedAppProtection|android_managed_app_protection_id|androidManagedAppProtection-id|
|**--managed-mobile-app-id**|string|key: id of managedMobileApp|managed_mobile_app_id|managedMobileApp-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.androidManagedAppProtectionsGetDeploymentSummary">Command `az devicescorpmgt deviceappmanagementandroidmanagedappprotection show-deployment-summary`</a>


##### <a name="ParametersdeviceAppManagement.androidManagedAppProtectionsGetDeploymentSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--android-managed-app-protection-id**|string|key: id of androidManagedAppProtection|android_managed_app_protection_id|androidManagedAppProtection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.androidManagedAppProtectionsUpdateApps">Command `az devicescorpmgt deviceappmanagementandroidmanagedappprotection update-app`</a>


##### <a name="ParametersdeviceAppManagement.androidManagedAppProtectionsUpdateApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--android-managed-app-protection-id**|string|key: id of androidManagedAppProtection|android_managed_app_protection_id|androidManagedAppProtection-id|
|**--managed-mobile-app-id**|string|key: id of managedMobileApp|managed_mobile_app_id|managedMobileApp-id|
|**--id**|string|Read-only.|id|id|
|**--mobile-app-identifier**|dictionary|The identifier for a mobile app.|mobile_app_identifier|mobileAppIdentifier|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagement.androidManagedAppProtectionsUpdateDeploymentSummary">Command `az devicescorpmgt deviceappmanagementandroidmanagedappprotection update-deployment-summary`</a>


##### <a name="ParametersdeviceAppManagement.androidManagedAppProtectionsUpdateDeploymentSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--android-managed-app-protection-id**|string|key: id of androidManagedAppProtection|android_managed_app_protection_id|androidManagedAppProtection-id|
|**--id**|string|Read-only.|id|id|
|**--configuration-deployed-user-count**|integer|Not yet documented|configuration_deployed_user_count|configurationDeployedUserCount|
|**--configuration-deployment-summary-per-app**|array|Not yet documented|configuration_deployment_summary_per_app|configurationDeploymentSummaryPerApp|
|**--display-name**|string|Not yet documented|display_name|displayName|
|**--last-refresh-time**|date-time|Not yet documented|last_refresh_time|lastRefreshTime|
|**--version**|string|Version of the entity.|version|version|

### group `az devicescorpmgt deviceappmanagementdefaultmanagedappprotection`
#### <a name="deviceAppManagement.defaultManagedAppProtectionsCreateApps">Command `az devicescorpmgt deviceappmanagementdefaultmanagedappprotection create-app`</a>


##### <a name="ParametersdeviceAppManagement.defaultManagedAppProtectionsCreateApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--default-managed-app-protection-id**|string|key: id of defaultManagedAppProtection|default_managed_app_protection_id|defaultManagedAppProtection-id|
|**--id**|string|Read-only.|id|id|
|**--mobile-app-identifier**|dictionary|The identifier for a mobile app.|mobile_app_identifier|mobileAppIdentifier|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagement.defaultManagedAppProtectionsDeleteApps">Command `az devicescorpmgt deviceappmanagementdefaultmanagedappprotection delete-app`</a>


##### <a name="ParametersdeviceAppManagement.defaultManagedAppProtectionsDeleteApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--default-managed-app-protection-id**|string|key: id of defaultManagedAppProtection|default_managed_app_protection_id|defaultManagedAppProtection-id|
|**--managed-mobile-app-id**|string|key: id of managedMobileApp|managed_mobile_app_id|managedMobileApp-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.defaultManagedAppProtectionsDeleteDeploymentSummary">Command `az devicescorpmgt deviceappmanagementdefaultmanagedappprotection delete-deployment-summary`</a>


##### <a name="ParametersdeviceAppManagement.defaultManagedAppProtectionsDeleteDeploymentSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--default-managed-app-protection-id**|string|key: id of defaultManagedAppProtection|default_managed_app_protection_id|defaultManagedAppProtection-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.defaultManagedAppProtectionsListApps">Command `az devicescorpmgt deviceappmanagementdefaultmanagedappprotection list-app`</a>


##### <a name="ParametersdeviceAppManagement.defaultManagedAppProtectionsListApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--default-managed-app-protection-id**|string|key: id of defaultManagedAppProtection|default_managed_app_protection_id|defaultManagedAppProtection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.defaultManagedAppProtectionsGetApps">Command `az devicescorpmgt deviceappmanagementdefaultmanagedappprotection show-app`</a>


##### <a name="ParametersdeviceAppManagement.defaultManagedAppProtectionsGetApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--default-managed-app-protection-id**|string|key: id of defaultManagedAppProtection|default_managed_app_protection_id|defaultManagedAppProtection-id|
|**--managed-mobile-app-id**|string|key: id of managedMobileApp|managed_mobile_app_id|managedMobileApp-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.defaultManagedAppProtectionsGetDeploymentSummary">Command `az devicescorpmgt deviceappmanagementdefaultmanagedappprotection show-deployment-summary`</a>


##### <a name="ParametersdeviceAppManagement.defaultManagedAppProtectionsGetDeploymentSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--default-managed-app-protection-id**|string|key: id of defaultManagedAppProtection|default_managed_app_protection_id|defaultManagedAppProtection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.defaultManagedAppProtectionsUpdateApps">Command `az devicescorpmgt deviceappmanagementdefaultmanagedappprotection update-app`</a>


##### <a name="ParametersdeviceAppManagement.defaultManagedAppProtectionsUpdateApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--default-managed-app-protection-id**|string|key: id of defaultManagedAppProtection|default_managed_app_protection_id|defaultManagedAppProtection-id|
|**--managed-mobile-app-id**|string|key: id of managedMobileApp|managed_mobile_app_id|managedMobileApp-id|
|**--id**|string|Read-only.|id|id|
|**--mobile-app-identifier**|dictionary|The identifier for a mobile app.|mobile_app_identifier|mobileAppIdentifier|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagement.defaultManagedAppProtectionsUpdateDeploymentSummary">Command `az devicescorpmgt deviceappmanagementdefaultmanagedappprotection update-deployment-summary`</a>


##### <a name="ParametersdeviceAppManagement.defaultManagedAppProtectionsUpdateDeploymentSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--default-managed-app-protection-id**|string|key: id of defaultManagedAppProtection|default_managed_app_protection_id|defaultManagedAppProtection-id|
|**--id**|string|Read-only.|id|id|
|**--configuration-deployed-user-count**|integer|Not yet documented|configuration_deployed_user_count|configurationDeployedUserCount|
|**--configuration-deployment-summary-per-app**|array|Not yet documented|configuration_deployment_summary_per_app|configurationDeploymentSummaryPerApp|
|**--display-name**|string|Not yet documented|display_name|displayName|
|**--last-refresh-time**|date-time|Not yet documented|last_refresh_time|lastRefreshTime|
|**--version**|string|Version of the entity.|version|version|

### group `az devicescorpmgt deviceappmanagementdeviceappmanagement`
#### <a name="deviceAppManagement.deviceAppManagementGetDeviceAppManagement">Command `az devicescorpmgt deviceappmanagementdeviceappmanagement show-device-app-management`</a>


##### <a name="ParametersdeviceAppManagement.deviceAppManagementGetDeviceAppManagement">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.deviceAppManagementUpdateDeviceAppManagement">Command `az devicescorpmgt deviceappmanagementdeviceappmanagement update-device-app-management`</a>


##### <a name="ParametersdeviceAppManagement.deviceAppManagementUpdateDeviceAppManagement">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--is-enabled-for-microsoft-store-for-business**|boolean|Whether the account is enabled for syncing applications from the Microsoft Store for Business.|is_enabled_for_microsoft_store_for_business|isEnabledForMicrosoftStoreForBusiness|
|**--microsoft-store-for-business-language**|string|The locale information used to sync applications from the Microsoft Store for Business. Cultures that are specific to a country/region. The names of these cultures follow RFC 4646 (Windows Vista and later). The format is -<country/regioncode2>, where  is a lowercase two-letter code derived from ISO 639-1 and <country/regioncode2> is an uppercase two-letter code derived from ISO 3166. For example, en-US for English (United States) is a specific culture.|microsoft_store_for_business_language|microsoftStoreForBusinessLanguage|
|**--microsoft-store-for-business-last-completed-application-sync-time**|date-time|The last time an application sync from the Microsoft Store for Business was completed.|microsoft_store_for_business_last_completed_application_sync_time|microsoftStoreForBusinessLastCompletedApplicationSyncTime|
|**--microsoft-store-for-business-last-successful-sync-date-time**|date-time|The last time the apps from the Microsoft Store for Business were synced successfully for the account.|microsoft_store_for_business_last_successful_sync_date_time|microsoftStoreForBusinessLastSuccessfulSyncDateTime|
|**--managed-e-books**|array|The Managed eBook.|managed_e_books|managedEBooks|
|**--mobile-app-categories**|array|The mobile app categories.|mobile_app_categories|mobileAppCategories|
|**--mobile-app-configurations**|array|The Managed Device Mobile Application Configurations.|mobile_app_configurations|mobileAppConfigurations|
|**--mobile-apps**|array|The mobile apps.|mobile_apps|mobileApps|
|**--vpp-tokens**|array|List of Vpp tokens for this organization.|vpp_tokens|vppTokens|
|**--android-managed-app-protections**|array|Android managed app policies.|android_managed_app_protections|androidManagedAppProtections|
|**--default-managed-app-protections**|array|Default managed app policies.|default_managed_app_protections|defaultManagedAppProtections|
|**--ios-managed-app-protections**|array|iOS managed app policies.|ios_managed_app_protections|iosManagedAppProtections|
|**--managed-app-policies**|array|Managed app policies.|managed_app_policies|managedAppPolicies|
|**--managed-app-registrations**|array|The managed app registrations.|managed_app_registrations|managedAppRegistrations|
|**--managed-app-statuses**|array|The managed app statuses.|managed_app_statuses|managedAppStatuses|
|**--mdm-windows-information-protection-policies**|array|Windows information protection for apps running on devices which are MDM enrolled.|mdm_windows_information_protection_policies|mdmWindowsInformationProtectionPolicies|
|**--targeted-managed-app-configurations**|array|Targeted managed app configurations.|targeted_managed_app_configurations|targetedManagedAppConfigurations|
|**--windows-information-protection-policies**|array|Windows information protection for apps running on devices which are not MDM enrolled.|windows_information_protection_policies|windowsInformationProtectionPolicies|

### group `az devicescorpmgt deviceappmanagementiosmanagedappprotection`
#### <a name="deviceAppManagement.iosManagedAppProtectionsCreateApps">Command `az devicescorpmgt deviceappmanagementiosmanagedappprotection create-app`</a>


##### <a name="ParametersdeviceAppManagement.iosManagedAppProtectionsCreateApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ios-managed-app-protection-id**|string|key: id of iosManagedAppProtection|ios_managed_app_protection_id|iosManagedAppProtection-id|
|**--id**|string|Read-only.|id|id|
|**--mobile-app-identifier**|dictionary|The identifier for a mobile app.|mobile_app_identifier|mobileAppIdentifier|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagement.iosManagedAppProtectionsDeleteApps">Command `az devicescorpmgt deviceappmanagementiosmanagedappprotection delete-app`</a>


##### <a name="ParametersdeviceAppManagement.iosManagedAppProtectionsDeleteApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ios-managed-app-protection-id**|string|key: id of iosManagedAppProtection|ios_managed_app_protection_id|iosManagedAppProtection-id|
|**--managed-mobile-app-id**|string|key: id of managedMobileApp|managed_mobile_app_id|managedMobileApp-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.iosManagedAppProtectionsDeleteDeploymentSummary">Command `az devicescorpmgt deviceappmanagementiosmanagedappprotection delete-deployment-summary`</a>


##### <a name="ParametersdeviceAppManagement.iosManagedAppProtectionsDeleteDeploymentSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ios-managed-app-protection-id**|string|key: id of iosManagedAppProtection|ios_managed_app_protection_id|iosManagedAppProtection-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.iosManagedAppProtectionsListApps">Command `az devicescorpmgt deviceappmanagementiosmanagedappprotection list-app`</a>


##### <a name="ParametersdeviceAppManagement.iosManagedAppProtectionsListApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ios-managed-app-protection-id**|string|key: id of iosManagedAppProtection|ios_managed_app_protection_id|iosManagedAppProtection-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.iosManagedAppProtectionsGetApps">Command `az devicescorpmgt deviceappmanagementiosmanagedappprotection show-app`</a>


##### <a name="ParametersdeviceAppManagement.iosManagedAppProtectionsGetApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ios-managed-app-protection-id**|string|key: id of iosManagedAppProtection|ios_managed_app_protection_id|iosManagedAppProtection-id|
|**--managed-mobile-app-id**|string|key: id of managedMobileApp|managed_mobile_app_id|managedMobileApp-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.iosManagedAppProtectionsGetDeploymentSummary">Command `az devicescorpmgt deviceappmanagementiosmanagedappprotection show-deployment-summary`</a>


##### <a name="ParametersdeviceAppManagement.iosManagedAppProtectionsGetDeploymentSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ios-managed-app-protection-id**|string|key: id of iosManagedAppProtection|ios_managed_app_protection_id|iosManagedAppProtection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.iosManagedAppProtectionsUpdateApps">Command `az devicescorpmgt deviceappmanagementiosmanagedappprotection update-app`</a>


##### <a name="ParametersdeviceAppManagement.iosManagedAppProtectionsUpdateApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ios-managed-app-protection-id**|string|key: id of iosManagedAppProtection|ios_managed_app_protection_id|iosManagedAppProtection-id|
|**--managed-mobile-app-id**|string|key: id of managedMobileApp|managed_mobile_app_id|managedMobileApp-id|
|**--id**|string|Read-only.|id|id|
|**--mobile-app-identifier**|dictionary|The identifier for a mobile app.|mobile_app_identifier|mobileAppIdentifier|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagement.iosManagedAppProtectionsUpdateDeploymentSummary">Command `az devicescorpmgt deviceappmanagementiosmanagedappprotection update-deployment-summary`</a>


##### <a name="ParametersdeviceAppManagement.iosManagedAppProtectionsUpdateDeploymentSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ios-managed-app-protection-id**|string|key: id of iosManagedAppProtection|ios_managed_app_protection_id|iosManagedAppProtection-id|
|**--id**|string|Read-only.|id|id|
|**--configuration-deployed-user-count**|integer|Not yet documented|configuration_deployed_user_count|configurationDeployedUserCount|
|**--configuration-deployment-summary-per-app**|array|Not yet documented|configuration_deployment_summary_per_app|configurationDeploymentSummaryPerApp|
|**--display-name**|string|Not yet documented|display_name|displayName|
|**--last-refresh-time**|date-time|Not yet documented|last_refresh_time|lastRefreshTime|
|**--version**|string|Version of the entity.|version|version|

### group `az devicescorpmgt deviceappmanagementmanagedapppolicy`
#### <a name="deviceAppManagement.managedAppPoliciestargetApps">Command `az devicescorpmgt deviceappmanagementmanagedapppolicy target-app`</a>


##### <a name="ParametersdeviceAppManagement.managedAppPoliciestargetApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--apps**|array||apps|apps|

### group `az devicescorpmgt deviceappmanagementmanagedappregistration`
#### <a name="deviceAppManagement.managedAppRegistrationsCreateAppliedPolicies">Command `az devicescorpmgt deviceappmanagementmanagedappregistration create-applied-policy`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsCreateAppliedPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagement.managedAppRegistrationsCreateIntendedPolicies">Command `az devicescorpmgt deviceappmanagementmanagedappregistration create-intended-policy`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsCreateIntendedPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagement.managedAppRegistrationsCreateOperations">Command `az devicescorpmgt deviceappmanagementmanagedappregistration create-operation`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsCreateOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The operation name.|display_name|displayName|
|**--last-modified-date-time**|date-time|The last time the app operation was modified.|last_modified_date_time|lastModifiedDateTime|
|**--state**|string|The current state of the operation|state|state|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagement.managedAppRegistrationsDeleteAppliedPolicies">Command `az devicescorpmgt deviceappmanagementmanagedappregistration delete-applied-policy`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsDeleteAppliedPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.managedAppRegistrationsDeleteIntendedPolicies">Command `az devicescorpmgt deviceappmanagementmanagedappregistration delete-intended-policy`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsDeleteIntendedPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.managedAppRegistrationsDeleteOperations">Command `az devicescorpmgt deviceappmanagementmanagedappregistration delete-operation`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsDeleteOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-operation-id**|string|key: id of managedAppOperation|managed_app_operation_id|managedAppOperation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.managedAppRegistrationsListAppliedPolicies">Command `az devicescorpmgt deviceappmanagementmanagedappregistration list-applied-policy`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsListAppliedPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.managedAppRegistrationsListIntendedPolicies">Command `az devicescorpmgt deviceappmanagementmanagedappregistration list-intended-policy`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsListIntendedPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.managedAppRegistrationsListOperations">Command `az devicescorpmgt deviceappmanagementmanagedappregistration list-operation`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsListOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.managedAppRegistrationsGetAppliedPolicies">Command `az devicescorpmgt deviceappmanagementmanagedappregistration show-applied-policy`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsGetAppliedPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.managedAppRegistrationsGetIntendedPolicies">Command `az devicescorpmgt deviceappmanagementmanagedappregistration show-intended-policy`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsGetIntendedPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.managedAppRegistrationsGetOperations">Command `az devicescorpmgt deviceappmanagementmanagedappregistration show-operation`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsGetOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-operation-id**|string|key: id of managedAppOperation|managed_app_operation_id|managedAppOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.managedAppRegistrationsgetUserIdsWithFlaggedAppRegistration">Command `az devicescorpmgt deviceappmanagementmanagedappregistration show-user-id-with-flagged-app-registration`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsgetUserIdsWithFlaggedAppRegistration">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

#### <a name="deviceAppManagement.managedAppRegistrationsUpdateAppliedPolicies">Command `az devicescorpmgt deviceappmanagementmanagedappregistration update-applied-policy`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsUpdateAppliedPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagement.managedAppRegistrationsUpdateIntendedPolicies">Command `az devicescorpmgt deviceappmanagementmanagedappregistration update-intended-policy`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsUpdateIntendedPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The date and time the policy was created.|created_date_time|createdDateTime|
|**--description**|string|The policy's description.|description|description|
|**--display-name**|string|Policy display name.|display_name|displayName|
|**--last-modified-date-time**|date-time|Last time the policy was modified.|last_modified_date_time|lastModifiedDateTime|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagement.managedAppRegistrationsUpdateOperations">Command `az devicescorpmgt deviceappmanagementmanagedappregistration update-operation`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrationsUpdateOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-operation-id**|string|key: id of managedAppOperation|managed_app_operation_id|managedAppOperation-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The operation name.|display_name|displayName|
|**--last-modified-date-time**|date-time|The last time the app operation was modified.|last_modified_date_time|lastModifiedDateTime|
|**--state**|string|The current state of the operation|state|state|
|**--version**|string|Version of the entity.|version|version|

### group `az devicescorpmgt deviceappmanagementmanagedappregistrationsappliedpolicy`
#### <a name="deviceAppManagement.managedAppRegistrations.appliedPoliciestargetApps">Command `az devicescorpmgt deviceappmanagementmanagedappregistrationsappliedpolicy target-app`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrations.appliedPoliciestargetApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--apps**|array||apps|apps|

### group `az devicescorpmgt deviceappmanagementmanagedappregistrationsintendedpolicy`
#### <a name="deviceAppManagement.managedAppRegistrations.intendedPoliciestargetApps">Command `az devicescorpmgt deviceappmanagementmanagedappregistrationsintendedpolicy target-app`</a>


##### <a name="ParametersdeviceAppManagement.managedAppRegistrations.intendedPoliciestargetApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-app-registration-id**|string|key: id of managedAppRegistration|managed_app_registration_id|managedAppRegistration-id|
|**--managed-app-policy-id**|string|key: id of managedAppPolicy|managed_app_policy_id|managedAppPolicy-id|
|**--apps**|array||apps|apps|

### group `az devicescorpmgt deviceappmanagementmanagedebook`
#### <a name="deviceAppManagement.managedEBooksassign">Command `az devicescorpmgt deviceappmanagementmanagedebook assign`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksassign">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--managed-e-book-assignments**|array||managed_e_book_assignments|managedEBookAssignments|

#### <a name="deviceAppManagement.managedEBooksCreateAssignments">Command `az devicescorpmgt deviceappmanagementmanagedebook create-assignment`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksCreateAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--id**|string|Read-only.|id|id|
|**--install-intent**|choice||install_intent|installIntent|
|**--target**|dictionary|Base type for assignment targets.|target|target|

#### <a name="deviceAppManagement.managedEBooksCreateDeviceStates">Command `az devicescorpmgt deviceappmanagementmanagedebook create-device-state`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksCreateDeviceStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--id**|string|Read-only.|id|id|
|**--device-id**|string|Device Id.|device_id|deviceId|
|**--device-name**|string|Device name.|device_name|deviceName|
|**--error-code**|string|The error code for install failures.|error_code|errorCode|
|**--install-state**|choice||install_state|installState|
|**--last-sync-date-time**|date-time|Last sync date and time.|last_sync_date_time|lastSyncDateTime|
|**--os-description**|string|OS Description.|os_description|osDescription|
|**--os-version**|string|OS Version.|os_version|osVersion|
|**--user-name**|string|Device User Name.|user_name|userName|

#### <a name="deviceAppManagement.managedEBooksCreateUserStateSummary">Command `az devicescorpmgt deviceappmanagementmanagedebook create-user-state-summary`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksCreateUserStateSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--id**|string|Read-only.|id|id|
|**--failed-device-count**|integer|Failed Device Count.|failed_device_count|failedDeviceCount|
|**--installed-device-count**|integer|Installed Device Count.|installed_device_count|installedDeviceCount|
|**--not-installed-device-count**|integer|Not installed device count.|not_installed_device_count|notInstalledDeviceCount|
|**--user-name**|string|User name.|user_name|userName|
|**--device-states**|array|The install state of the eBook.|device_states|deviceStates|

#### <a name="deviceAppManagement.managedEBooksDeleteAssignments">Command `az devicescorpmgt deviceappmanagementmanagedebook delete-assignment`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksDeleteAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--managed-e-book-assignment-id**|string|key: id of managedEBookAssignment|managed_e_book_assignment_id|managedEBookAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.managedEBooksDeleteDeviceStates">Command `az devicescorpmgt deviceappmanagementmanagedebook delete-device-state`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksDeleteDeviceStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--device-install-state-id**|string|key: id of deviceInstallState|device_install_state_id|deviceInstallState-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.managedEBooksDeleteInstallSummary">Command `az devicescorpmgt deviceappmanagementmanagedebook delete-install-summary`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksDeleteInstallSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.managedEBooksDeleteUserStateSummary">Command `az devicescorpmgt deviceappmanagementmanagedebook delete-user-state-summary`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksDeleteUserStateSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--user-install-state-summary-id**|string|key: id of userInstallStateSummary|user_install_state_summary_id|userInstallStateSummary-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.managedEBooksListAssignments">Command `az devicescorpmgt deviceappmanagementmanagedebook list-assignment`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksListAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.managedEBooksListDeviceStates">Command `az devicescorpmgt deviceappmanagementmanagedebook list-device-state`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksListDeviceStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.managedEBooksListUserStateSummary">Command `az devicescorpmgt deviceappmanagementmanagedebook list-user-state-summary`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksListUserStateSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.managedEBooksGetAssignments">Command `az devicescorpmgt deviceappmanagementmanagedebook show-assignment`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksGetAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--managed-e-book-assignment-id**|string|key: id of managedEBookAssignment|managed_e_book_assignment_id|managedEBookAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.managedEBooksGetDeviceStates">Command `az devicescorpmgt deviceappmanagementmanagedebook show-device-state`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksGetDeviceStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--device-install-state-id**|string|key: id of deviceInstallState|device_install_state_id|deviceInstallState-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.managedEBooksGetInstallSummary">Command `az devicescorpmgt deviceappmanagementmanagedebook show-install-summary`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksGetInstallSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.managedEBooksGetUserStateSummary">Command `az devicescorpmgt deviceappmanagementmanagedebook show-user-state-summary`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksGetUserStateSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--user-install-state-summary-id**|string|key: id of userInstallStateSummary|user_install_state_summary_id|userInstallStateSummary-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.managedEBooksUpdateAssignments">Command `az devicescorpmgt deviceappmanagementmanagedebook update-assignment`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksUpdateAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--managed-e-book-assignment-id**|string|key: id of managedEBookAssignment|managed_e_book_assignment_id|managedEBookAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--install-intent**|choice||install_intent|installIntent|
|**--target**|dictionary|Base type for assignment targets.|target|target|

#### <a name="deviceAppManagement.managedEBooksUpdateDeviceStates">Command `az devicescorpmgt deviceappmanagementmanagedebook update-device-state`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksUpdateDeviceStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--device-install-state-id**|string|key: id of deviceInstallState|device_install_state_id|deviceInstallState-id|
|**--id**|string|Read-only.|id|id|
|**--device-id**|string|Device Id.|device_id|deviceId|
|**--device-name**|string|Device name.|device_name|deviceName|
|**--error-code**|string|The error code for install failures.|error_code|errorCode|
|**--install-state**|choice||install_state|installState|
|**--last-sync-date-time**|date-time|Last sync date and time.|last_sync_date_time|lastSyncDateTime|
|**--os-description**|string|OS Description.|os_description|osDescription|
|**--os-version**|string|OS Version.|os_version|osVersion|
|**--user-name**|string|Device User Name.|user_name|userName|

#### <a name="deviceAppManagement.managedEBooksUpdateInstallSummary">Command `az devicescorpmgt deviceappmanagementmanagedebook update-install-summary`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksUpdateInstallSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--id**|string|Read-only.|id|id|
|**--failed-device-count**|integer|Number of Devices that have failed to install this book.|failed_device_count|failedDeviceCount|
|**--failed-user-count**|integer|Number of Users that have 1 or more device that failed to install this book.|failed_user_count|failedUserCount|
|**--installed-device-count**|integer|Number of Devices that have successfully installed this book.|installed_device_count|installedDeviceCount|
|**--installed-user-count**|integer|Number of Users whose devices have all succeeded to install this book.|installed_user_count|installedUserCount|
|**--not-installed-device-count**|integer|Number of Devices that does not have this book installed.|not_installed_device_count|notInstalledDeviceCount|
|**--not-installed-user-count**|integer|Number of Users that did not install this book.|not_installed_user_count|notInstalledUserCount|

#### <a name="deviceAppManagement.managedEBooksUpdateUserStateSummary">Command `az devicescorpmgt deviceappmanagementmanagedebook update-user-state-summary`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooksUpdateUserStateSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--user-install-state-summary-id**|string|key: id of userInstallStateSummary|user_install_state_summary_id|userInstallStateSummary-id|
|**--id**|string|Read-only.|id|id|
|**--failed-device-count**|integer|Failed Device Count.|failed_device_count|failedDeviceCount|
|**--installed-device-count**|integer|Installed Device Count.|installed_device_count|installedDeviceCount|
|**--not-installed-device-count**|integer|Not installed device count.|not_installed_device_count|notInstalledDeviceCount|
|**--user-name**|string|User name.|user_name|userName|
|**--device-states**|array|The install state of the eBook.|device_states|deviceStates|

### group `az devicescorpmgt deviceappmanagementmanagedebooksuserstatesummary`
#### <a name="deviceAppManagement.managedEBooks.userStateSummaryCreateDeviceStates">Command `az devicescorpmgt deviceappmanagementmanagedebooksuserstatesummary create-device-state`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooks.userStateSummaryCreateDeviceStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--user-install-state-summary-id**|string|key: id of userInstallStateSummary|user_install_state_summary_id|userInstallStateSummary-id|
|**--id**|string|Read-only.|id|id|
|**--device-id**|string|Device Id.|device_id|deviceId|
|**--device-name**|string|Device name.|device_name|deviceName|
|**--error-code**|string|The error code for install failures.|error_code|errorCode|
|**--install-state**|choice||install_state|installState|
|**--last-sync-date-time**|date-time|Last sync date and time.|last_sync_date_time|lastSyncDateTime|
|**--os-description**|string|OS Description.|os_description|osDescription|
|**--os-version**|string|OS Version.|os_version|osVersion|
|**--user-name**|string|Device User Name.|user_name|userName|

#### <a name="deviceAppManagement.managedEBooks.userStateSummaryDeleteDeviceStates">Command `az devicescorpmgt deviceappmanagementmanagedebooksuserstatesummary delete-device-state`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooks.userStateSummaryDeleteDeviceStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--user-install-state-summary-id**|string|key: id of userInstallStateSummary|user_install_state_summary_id|userInstallStateSummary-id|
|**--device-install-state-id**|string|key: id of deviceInstallState|device_install_state_id|deviceInstallState-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.managedEBooks.userStateSummaryListDeviceStates">Command `az devicescorpmgt deviceappmanagementmanagedebooksuserstatesummary list-device-state`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooks.userStateSummaryListDeviceStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--user-install-state-summary-id**|string|key: id of userInstallStateSummary|user_install_state_summary_id|userInstallStateSummary-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.managedEBooks.userStateSummaryGetDeviceStates">Command `az devicescorpmgt deviceappmanagementmanagedebooksuserstatesummary show-device-state`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooks.userStateSummaryGetDeviceStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--user-install-state-summary-id**|string|key: id of userInstallStateSummary|user_install_state_summary_id|userInstallStateSummary-id|
|**--device-install-state-id**|string|key: id of deviceInstallState|device_install_state_id|deviceInstallState-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.managedEBooks.userStateSummaryUpdateDeviceStates">Command `az devicescorpmgt deviceappmanagementmanagedebooksuserstatesummary update-device-state`</a>


##### <a name="ParametersdeviceAppManagement.managedEBooks.userStateSummaryUpdateDeviceStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-e-book-id**|string|key: id of managedEBook|managed_e_book_id|managedEBook-id|
|**--user-install-state-summary-id**|string|key: id of userInstallStateSummary|user_install_state_summary_id|userInstallStateSummary-id|
|**--device-install-state-id**|string|key: id of deviceInstallState|device_install_state_id|deviceInstallState-id|
|**--id**|string|Read-only.|id|id|
|**--device-id**|string|Device Id.|device_id|deviceId|
|**--device-name**|string|Device name.|device_name|deviceName|
|**--error-code**|string|The error code for install failures.|error_code|errorCode|
|**--install-state**|choice||install_state|installState|
|**--last-sync-date-time**|date-time|Last sync date and time.|last_sync_date_time|lastSyncDateTime|
|**--os-description**|string|OS Description.|os_description|osDescription|
|**--os-version**|string|OS Version.|os_version|osVersion|
|**--user-name**|string|Device User Name.|user_name|userName|

### group `az devicescorpmgt deviceappmanagementmobileapp`
#### <a name="deviceAppManagement.mobileAppsassign">Command `az devicescorpmgt deviceappmanagementmobileapp assign`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppsassign">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--mobile-app-assignments**|array||mobile_app_assignments|mobileAppAssignments|

#### <a name="deviceAppManagement.mobileAppsCreateAssignments">Command `az devicescorpmgt deviceappmanagementmobileapp create-assignment`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppsCreateAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--id**|string|Read-only.|id|id|
|**--intent**|choice||intent|intent|
|**--settings**|dictionary|Abstract class to contain properties used to assign a mobile app to a group.|settings|settings|
|**--target**|dictionary|Base type for assignment targets.|target|target|

#### <a name="deviceAppManagement.mobileAppsCreateRefCategories">Command `az devicescorpmgt deviceappmanagementmobileapp create-ref-category`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppsCreateRefCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="deviceAppManagement.mobileAppsDeleteAssignments">Command `az devicescorpmgt deviceappmanagementmobileapp delete-assignment`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppsDeleteAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--mobile-app-assignment-id**|string|key: id of mobileAppAssignment|mobile_app_assignment_id|mobileAppAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.mobileAppsListAssignments">Command `az devicescorpmgt deviceappmanagementmobileapp list-assignment`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppsListAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.mobileAppsListCategories">Command `az devicescorpmgt deviceappmanagementmobileapp list-category`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppsListCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.mobileAppsListRefCategories">Command `az devicescorpmgt deviceappmanagementmobileapp list-ref-category`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppsListRefCategories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="deviceAppManagement.mobileAppsGetAssignments">Command `az devicescorpmgt deviceappmanagementmobileapp show-assignment`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppsGetAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--mobile-app-assignment-id**|string|key: id of mobileAppAssignment|mobile_app_assignment_id|mobileAppAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.mobileAppsUpdateAssignments">Command `az devicescorpmgt deviceappmanagementmobileapp update-assignment`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppsUpdateAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--mobile-app-id**|string|key: id of mobileApp|mobile_app_id|mobileApp-id|
|**--mobile-app-assignment-id**|string|key: id of mobileAppAssignment|mobile_app_assignment_id|mobileAppAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--intent**|choice||intent|intent|
|**--settings**|dictionary|Abstract class to contain properties used to assign a mobile app to a group.|settings|settings|
|**--target**|dictionary|Base type for assignment targets.|target|target|

### group `az devicescorpmgt deviceappmanagementmobileappconfiguration`
#### <a name="deviceAppManagement.mobileAppConfigurationsassign">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration assign`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsassign">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--assignments**|array||assignments|assignments|

#### <a name="deviceAppManagement.mobileAppConfigurationsCreateAssignments">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration create-assignment`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsCreateAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--target**|dictionary|Base type for assignment targets.|target|target|

#### <a name="deviceAppManagement.mobileAppConfigurationsCreateDeviceStatuses">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration create-device-statuses`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsCreateDeviceStatuses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--compliance-grace-period-expiration-date-time**|date-time|The DateTime when device compliance grace period expires|compliance_grace_period_expiration_date_time|complianceGracePeriodExpirationDateTime|
|**--device-display-name**|string|Device name of the DevicePolicyStatus.|device_display_name|deviceDisplayName|
|**--device-model**|string|The device model that is being reported|device_model|deviceModel|
|**--last-reported-date-time**|date-time|Last modified date time of the policy report.|last_reported_date_time|lastReportedDateTime|
|**--status**|choice||status|status|
|**--user-name**|string|The User Name that is being reported|user_name|userName|
|**--user-principal-name**|string|UserPrincipalName.|user_principal_name|userPrincipalName|

#### <a name="deviceAppManagement.mobileAppConfigurationsCreateUserStatuses">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration create-user-statuses`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsCreateUserStatuses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--devices-count**|integer|Devices count for that user.|devices_count|devicesCount|
|**--last-reported-date-time**|date-time|Last modified date time of the policy report.|last_reported_date_time|lastReportedDateTime|
|**--status**|choice||status|status|
|**--user-display-name**|string|User name of the DevicePolicyStatus.|user_display_name|userDisplayName|
|**--user-principal-name**|string|UserPrincipalName.|user_principal_name|userPrincipalName|

#### <a name="deviceAppManagement.mobileAppConfigurationsDeleteAssignments">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration delete-assignment`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsDeleteAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--managed-device-mobile-app-configuration-assignment-id**|string|key: id of managedDeviceMobileAppConfigurationAssignment|managed_device_mobile_app_configuration_assignment_id|managedDeviceMobileAppConfigurationAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.mobileAppConfigurationsDeleteDeviceStatusSummary">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration delete-device-status-summary`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsDeleteDeviceStatusSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.mobileAppConfigurationsDeleteDeviceStatuses">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration delete-device-statuses`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsDeleteDeviceStatuses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--managed-device-mobile-app-configuration-device-status-id**|string|key: id of managedDeviceMobileAppConfigurationDeviceStatus|managed_device_mobile_app_configuration_device_status_id|managedDeviceMobileAppConfigurationDeviceStatus-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.mobileAppConfigurationsDeleteUserStatusSummary">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration delete-user-status-summary`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsDeleteUserStatusSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.mobileAppConfigurationsDeleteUserStatuses">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration delete-user-statuses`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsDeleteUserStatuses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--managed-device-mobile-app-configuration-user-status-id**|string|key: id of managedDeviceMobileAppConfigurationUserStatus|managed_device_mobile_app_configuration_user_status_id|managedDeviceMobileAppConfigurationUserStatus-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.mobileAppConfigurationsListAssignments">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration list-assignment`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsListAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.mobileAppConfigurationsListDeviceStatuses">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration list-device-statuses`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsListDeviceStatuses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.mobileAppConfigurationsListUserStatuses">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration list-user-statuses`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsListUserStatuses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.mobileAppConfigurationsGetAssignments">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration show-assignment`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsGetAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--managed-device-mobile-app-configuration-assignment-id**|string|key: id of managedDeviceMobileAppConfigurationAssignment|managed_device_mobile_app_configuration_assignment_id|managedDeviceMobileAppConfigurationAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.mobileAppConfigurationsGetDeviceStatusSummary">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration show-device-status-summary`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsGetDeviceStatusSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.mobileAppConfigurationsGetDeviceStatuses">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration show-device-statuses`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsGetDeviceStatuses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--managed-device-mobile-app-configuration-device-status-id**|string|key: id of managedDeviceMobileAppConfigurationDeviceStatus|managed_device_mobile_app_configuration_device_status_id|managedDeviceMobileAppConfigurationDeviceStatus-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.mobileAppConfigurationsGetUserStatusSummary">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration show-user-status-summary`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsGetUserStatusSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.mobileAppConfigurationsGetUserStatuses">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration show-user-statuses`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsGetUserStatuses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--managed-device-mobile-app-configuration-user-status-id**|string|key: id of managedDeviceMobileAppConfigurationUserStatus|managed_device_mobile_app_configuration_user_status_id|managedDeviceMobileAppConfigurationUserStatus-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.mobileAppConfigurationsUpdateAssignments">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration update-assignment`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsUpdateAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--managed-device-mobile-app-configuration-assignment-id**|string|key: id of managedDeviceMobileAppConfigurationAssignment|managed_device_mobile_app_configuration_assignment_id|managedDeviceMobileAppConfigurationAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--target**|dictionary|Base type for assignment targets.|target|target|

#### <a name="deviceAppManagement.mobileAppConfigurationsUpdateDeviceStatusSummary">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration update-device-status-summary`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsUpdateDeviceStatusSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--configuration-version**|integer|Version of the policy for that overview|configuration_version|configurationVersion|
|**--error-count**|integer|Number of error devices|error_count|errorCount|
|**--failed-count**|integer|Number of failed devices|failed_count|failedCount|
|**--last-update-date-time**|date-time|Last update time|last_update_date_time|lastUpdateDateTime|
|**--not-applicable-count**|integer|Number of not applicable devices|not_applicable_count|notApplicableCount|
|**--pending-count**|integer|Number of pending devices|pending_count|pendingCount|
|**--success-count**|integer|Number of succeeded devices|success_count|successCount|

#### <a name="deviceAppManagement.mobileAppConfigurationsUpdateDeviceStatuses">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration update-device-statuses`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsUpdateDeviceStatuses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--managed-device-mobile-app-configuration-device-status-id**|string|key: id of managedDeviceMobileAppConfigurationDeviceStatus|managed_device_mobile_app_configuration_device_status_id|managedDeviceMobileAppConfigurationDeviceStatus-id|
|**--id**|string|Read-only.|id|id|
|**--compliance-grace-period-expiration-date-time**|date-time|The DateTime when device compliance grace period expires|compliance_grace_period_expiration_date_time|complianceGracePeriodExpirationDateTime|
|**--device-display-name**|string|Device name of the DevicePolicyStatus.|device_display_name|deviceDisplayName|
|**--device-model**|string|The device model that is being reported|device_model|deviceModel|
|**--last-reported-date-time**|date-time|Last modified date time of the policy report.|last_reported_date_time|lastReportedDateTime|
|**--status**|choice||status|status|
|**--user-name**|string|The User Name that is being reported|user_name|userName|
|**--user-principal-name**|string|UserPrincipalName.|user_principal_name|userPrincipalName|

#### <a name="deviceAppManagement.mobileAppConfigurationsUpdateUserStatusSummary">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration update-user-status-summary`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsUpdateUserStatusSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--configuration-version**|integer|Version of the policy for that overview|configuration_version|configurationVersion|
|**--error-count**|integer|Number of error Users|error_count|errorCount|
|**--failed-count**|integer|Number of failed Users|failed_count|failedCount|
|**--last-update-date-time**|date-time|Last update time|last_update_date_time|lastUpdateDateTime|
|**--not-applicable-count**|integer|Number of not applicable users|not_applicable_count|notApplicableCount|
|**--pending-count**|integer|Number of pending Users|pending_count|pendingCount|
|**--success-count**|integer|Number of succeeded Users|success_count|successCount|

#### <a name="deviceAppManagement.mobileAppConfigurationsUpdateUserStatuses">Command `az devicescorpmgt deviceappmanagementmobileappconfiguration update-user-statuses`</a>


##### <a name="ParametersdeviceAppManagement.mobileAppConfigurationsUpdateUserStatuses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--managed-device-mobile-app-configuration-id**|string|key: id of managedDeviceMobileAppConfiguration|managed_device_mobile_app_configuration_id|managedDeviceMobileAppConfiguration-id|
|**--managed-device-mobile-app-configuration-user-status-id**|string|key: id of managedDeviceMobileAppConfigurationUserStatus|managed_device_mobile_app_configuration_user_status_id|managedDeviceMobileAppConfigurationUserStatus-id|
|**--id**|string|Read-only.|id|id|
|**--devices-count**|integer|Devices count for that user.|devices_count|devicesCount|
|**--last-reported-date-time**|date-time|Last modified date time of the policy report.|last_reported_date_time|lastReportedDateTime|
|**--status**|choice||status|status|
|**--user-display-name**|string|User name of the DevicePolicyStatus.|user_display_name|userDisplayName|
|**--user-principal-name**|string|UserPrincipalName.|user_principal_name|userPrincipalName|

### group `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration`
#### <a name="deviceAppManagement.targetedManagedAppConfigurationsassign">Command `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration assign`</a>


##### <a name="ParametersdeviceAppManagement.targetedManagedAppConfigurationsassign">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--assignments**|array||assignments|assignments|

#### <a name="deviceAppManagement.targetedManagedAppConfigurationsCreateApps">Command `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration create-app`</a>


##### <a name="ParametersdeviceAppManagement.targetedManagedAppConfigurationsCreateApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--mobile-app-identifier**|dictionary|The identifier for a mobile app.|mobile_app_identifier|mobileAppIdentifier|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagement.targetedManagedAppConfigurationsCreateAssignments">Command `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration create-assignment`</a>


##### <a name="ParametersdeviceAppManagement.targetedManagedAppConfigurationsCreateAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--target**|dictionary|Base type for assignment targets.|target|target|

#### <a name="deviceAppManagement.targetedManagedAppConfigurationsDeleteApps">Command `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration delete-app`</a>


##### <a name="ParametersdeviceAppManagement.targetedManagedAppConfigurationsDeleteApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--managed-mobile-app-id**|string|key: id of managedMobileApp|managed_mobile_app_id|managedMobileApp-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.targetedManagedAppConfigurationsDeleteAssignments">Command `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration delete-assignment`</a>


##### <a name="ParametersdeviceAppManagement.targetedManagedAppConfigurationsDeleteAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--targeted-managed-app-policy-assignment-id**|string|key: id of targetedManagedAppPolicyAssignment|targeted_managed_app_policy_assignment_id|targetedManagedAppPolicyAssignment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.targetedManagedAppConfigurationsDeleteDeploymentSummary">Command `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration delete-deployment-summary`</a>


##### <a name="ParametersdeviceAppManagement.targetedManagedAppConfigurationsDeleteDeploymentSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="deviceAppManagement.targetedManagedAppConfigurationsListApps">Command `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration list-app`</a>


##### <a name="ParametersdeviceAppManagement.targetedManagedAppConfigurationsListApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.targetedManagedAppConfigurationsListAssignments">Command `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration list-assignment`</a>


##### <a name="ParametersdeviceAppManagement.targetedManagedAppConfigurationsListAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.targetedManagedAppConfigurationsGetApps">Command `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration show-app`</a>


##### <a name="ParametersdeviceAppManagement.targetedManagedAppConfigurationsGetApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--managed-mobile-app-id**|string|key: id of managedMobileApp|managed_mobile_app_id|managedMobileApp-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.targetedManagedAppConfigurationsGetAssignments">Command `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration show-assignment`</a>


##### <a name="ParametersdeviceAppManagement.targetedManagedAppConfigurationsGetAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--targeted-managed-app-policy-assignment-id**|string|key: id of targetedManagedAppPolicyAssignment|targeted_managed_app_policy_assignment_id|targetedManagedAppPolicyAssignment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.targetedManagedAppConfigurationsGetDeploymentSummary">Command `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration show-deployment-summary`</a>


##### <a name="ParametersdeviceAppManagement.targetedManagedAppConfigurationsGetDeploymentSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="deviceAppManagement.targetedManagedAppConfigurationstargetApps">Command `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration target-app`</a>


##### <a name="ParametersdeviceAppManagement.targetedManagedAppConfigurationstargetApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--apps**|array||apps|apps|

#### <a name="deviceAppManagement.targetedManagedAppConfigurationsUpdateApps">Command `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration update-app`</a>


##### <a name="ParametersdeviceAppManagement.targetedManagedAppConfigurationsUpdateApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--managed-mobile-app-id**|string|key: id of managedMobileApp|managed_mobile_app_id|managedMobileApp-id|
|**--id**|string|Read-only.|id|id|
|**--mobile-app-identifier**|dictionary|The identifier for a mobile app.|mobile_app_identifier|mobileAppIdentifier|
|**--version**|string|Version of the entity.|version|version|

#### <a name="deviceAppManagement.targetedManagedAppConfigurationsUpdateAssignments">Command `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration update-assignment`</a>


##### <a name="ParametersdeviceAppManagement.targetedManagedAppConfigurationsUpdateAssignments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--targeted-managed-app-policy-assignment-id**|string|key: id of targetedManagedAppPolicyAssignment|targeted_managed_app_policy_assignment_id|targetedManagedAppPolicyAssignment-id|
|**--id**|string|Read-only.|id|id|
|**--target**|dictionary|Base type for assignment targets.|target|target|

#### <a name="deviceAppManagement.targetedManagedAppConfigurationsUpdateDeploymentSummary">Command `az devicescorpmgt deviceappmanagementtargetedmanagedappconfiguration update-deployment-summary`</a>


##### <a name="ParametersdeviceAppManagement.targetedManagedAppConfigurationsUpdateDeploymentSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--targeted-managed-app-configuration-id**|string|key: id of targetedManagedAppConfiguration|targeted_managed_app_configuration_id|targetedManagedAppConfiguration-id|
|**--id**|string|Read-only.|id|id|
|**--configuration-deployed-user-count**|integer|Not yet documented|configuration_deployed_user_count|configurationDeployedUserCount|
|**--configuration-deployment-summary-per-app**|array|Not yet documented|configuration_deployment_summary_per_app|configurationDeploymentSummaryPerApp|
|**--display-name**|string|Not yet documented|display_name|displayName|
|**--last-refresh-time**|date-time|Not yet documented|last_refresh_time|lastRefreshTime|
|**--version**|string|Version of the entity.|version|version|

### group `az devicescorpmgt deviceappmanagementvpptoken`
#### <a name="deviceAppManagement.vppTokenssyncLicenses">Command `az devicescorpmgt deviceappmanagementvpptoken sync-license`</a>


##### <a name="ParametersdeviceAppManagement.vppTokenssyncLicenses">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--vpp-token-id**|string|key: id of vppToken|vpp_token_id|vppToken-id|

### group `az devicescorpmgt user`
#### <a name="usersCreateDeviceManagementTroubleshootingEvents">Command `az devicescorpmgt user create-device-management-troubleshooting-event`</a>


##### <a name="ParametersusersCreateDeviceManagementTroubleshootingEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--correlation-id**|string|Id used for tracing the failure in the service.|correlation_id|correlationId|
|**--event-date-time**|date-time|Time when the event occurred .|event_date_time|eventDateTime|

#### <a name="usersCreateManagedDevices">Command `az devicescorpmgt user create-managed-device`</a>


##### <a name="ParametersusersCreateManagedDevices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|object|New navigation property|body|body|

#### <a name="usersCreateRefManagedAppRegistrations">Command `az devicescorpmgt user create-ref-managed-app-registration`</a>


##### <a name="ParametersusersCreateRefManagedAppRegistrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="usersDeleteDeviceManagementTroubleshootingEvents">Command `az devicescorpmgt user delete-device-management-troubleshooting-event`</a>


##### <a name="ParametersusersDeleteDeviceManagementTroubleshootingEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--device-management-troubleshooting-event-id**|string|key: id of deviceManagementTroubleshootingEvent|device_management_troubleshooting_event_id|deviceManagementTroubleshootingEvent-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteManagedDevices">Command `az devicescorpmgt user delete-managed-device`</a>


##### <a name="ParametersusersDeleteManagedDevices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersListDeviceManagementTroubleshootingEvents">Command `az devicescorpmgt user list-device-management-troubleshooting-event`</a>


##### <a name="ParametersusersListDeviceManagementTroubleshootingEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListManagedAppRegistrations">Command `az devicescorpmgt user list-managed-app-registration`</a>


##### <a name="ParametersusersListManagedAppRegistrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListManagedDevices">Command `az devicescorpmgt user list-managed-device`</a>


##### <a name="ParametersusersListManagedDevices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListRefManagedAppRegistrations">Command `az devicescorpmgt user list-ref-managed-app-registration`</a>


##### <a name="ParametersusersListRefManagedAppRegistrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="usersGetDeviceManagementTroubleshootingEvents">Command `az devicescorpmgt user show-device-management-troubleshooting-event`</a>


##### <a name="ParametersusersGetDeviceManagementTroubleshootingEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--device-management-troubleshooting-event-id**|string|key: id of deviceManagementTroubleshootingEvent|device_management_troubleshooting_event_id|deviceManagementTroubleshootingEvent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetManagedDevices">Command `az devicescorpmgt user show-managed-device`</a>


##### <a name="ParametersusersGetManagedDevices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateDeviceManagementTroubleshootingEvents">Command `az devicescorpmgt user update-device-management-troubleshooting-event`</a>


##### <a name="ParametersusersUpdateDeviceManagementTroubleshootingEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--device-management-troubleshooting-event-id**|string|key: id of deviceManagementTroubleshootingEvent|device_management_troubleshooting_event_id|deviceManagementTroubleshootingEvent-id|
|**--id**|string|Read-only.|id|id|
|**--correlation-id**|string|Id used for tracing the failure in the service.|correlation_id|correlationId|
|**--event-date-time**|date-time|Time when the event occurred .|event_date_time|eventDateTime|

#### <a name="usersUpdateManagedDevices">Command `az devicescorpmgt user update-managed-device`</a>


##### <a name="ParametersusersUpdateManagedDevices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--body**|object|New navigation property values|body|body|

### group `az devicescorpmgt usersmanageddevice`
#### <a name="users.managedDevicesCreateDeviceCompliancePolicyStates">Command `az devicescorpmgt usersmanageddevice create-device-compliance-policy-state`</a>


##### <a name="Parametersusers.managedDevicesCreateDeviceCompliancePolicyStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The name of the policy for this policyBase|display_name|displayName|
|**--platform-type**|choice||platform_type|platformType|
|**--setting-count**|integer|Count of how many setting a policy holds|setting_count|settingCount|
|**--setting-states**|array||setting_states|settingStates|
|**--state**|choice||state|state|
|**--version**|integer|The version of the policy|version|version|

#### <a name="users.managedDevicesCreateDeviceConfigurationStates">Command `az devicescorpmgt usersmanageddevice create-device-configuration-state`</a>


##### <a name="Parametersusers.managedDevicesCreateDeviceConfigurationStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The name of the policy for this policyBase|display_name|displayName|
|**--platform-type**|choice||platform_type|platformType|
|**--setting-count**|integer|Count of how many setting a policy holds|setting_count|settingCount|
|**--setting-states**|array||setting_states|settingStates|
|**--state**|choice||state|state|
|**--version**|integer|The version of the policy|version|version|

#### <a name="users.managedDevicesDeleteDeviceCategory">Command `az devicescorpmgt usersmanageddevice delete-device-category`</a>


##### <a name="Parametersusers.managedDevicesDeleteDeviceCategory">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.managedDevicesDeleteDeviceCompliancePolicyStates">Command `az devicescorpmgt usersmanageddevice delete-device-compliance-policy-state`</a>


##### <a name="Parametersusers.managedDevicesDeleteDeviceCompliancePolicyStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--device-compliance-policy-state-id**|string|key: id of deviceCompliancePolicyState|device_compliance_policy_state_id|deviceCompliancePolicyState-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.managedDevicesDeleteDeviceConfigurationStates">Command `az devicescorpmgt usersmanageddevice delete-device-configuration-state`</a>


##### <a name="Parametersusers.managedDevicesDeleteDeviceConfigurationStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--device-configuration-state-id**|string|key: id of deviceConfigurationState|device_configuration_state_id|deviceConfigurationState-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.managedDevicesListDeviceCompliancePolicyStates">Command `az devicescorpmgt usersmanageddevice list-device-compliance-policy-state`</a>


##### <a name="Parametersusers.managedDevicesListDeviceCompliancePolicyStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.managedDevicesListDeviceConfigurationStates">Command `az devicescorpmgt usersmanageddevice list-device-configuration-state`</a>


##### <a name="Parametersusers.managedDevicesListDeviceConfigurationStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.managedDevicesGetDeviceCategory">Command `az devicescorpmgt usersmanageddevice show-device-category`</a>


##### <a name="Parametersusers.managedDevicesGetDeviceCategory">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.managedDevicesGetDeviceCompliancePolicyStates">Command `az devicescorpmgt usersmanageddevice show-device-compliance-policy-state`</a>


##### <a name="Parametersusers.managedDevicesGetDeviceCompliancePolicyStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--device-compliance-policy-state-id**|string|key: id of deviceCompliancePolicyState|device_compliance_policy_state_id|deviceCompliancePolicyState-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.managedDevicesGetDeviceConfigurationStates">Command `az devicescorpmgt usersmanageddevice show-device-configuration-state`</a>


##### <a name="Parametersusers.managedDevicesGetDeviceConfigurationStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--device-configuration-state-id**|string|key: id of deviceConfigurationState|device_configuration_state_id|deviceConfigurationState-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.managedDevicesUpdateDeviceCategory">Command `az devicescorpmgt usersmanageddevice update-device-category`</a>


##### <a name="Parametersusers.managedDevicesUpdateDeviceCategory">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string|Optional description for the device category.|description|description|
|**--display-name**|string|Display name for the device category.|display_name|displayName|

#### <a name="users.managedDevicesUpdateDeviceCompliancePolicyStates">Command `az devicescorpmgt usersmanageddevice update-device-compliance-policy-state`</a>


##### <a name="Parametersusers.managedDevicesUpdateDeviceCompliancePolicyStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--device-compliance-policy-state-id**|string|key: id of deviceCompliancePolicyState|device_compliance_policy_state_id|deviceCompliancePolicyState-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The name of the policy for this policyBase|display_name|displayName|
|**--platform-type**|choice||platform_type|platformType|
|**--setting-count**|integer|Count of how many setting a policy holds|setting_count|settingCount|
|**--setting-states**|array||setting_states|settingStates|
|**--state**|choice||state|state|
|**--version**|integer|The version of the policy|version|version|

#### <a name="users.managedDevicesUpdateDeviceConfigurationStates">Command `az devicescorpmgt usersmanageddevice update-device-configuration-state`</a>


##### <a name="Parametersusers.managedDevicesUpdateDeviceConfigurationStates">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--device-configuration-state-id**|string|key: id of deviceConfigurationState|device_configuration_state_id|deviceConfigurationState-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The name of the policy for this policyBase|display_name|displayName|
|**--platform-type**|choice||platform_type|platformType|
|**--setting-count**|integer|Count of how many setting a policy holds|setting_count|settingCount|
|**--setting-states**|array||setting_states|settingStates|
|**--state**|choice||state|state|
|**--version**|integer|The version of the policy|version|version|
