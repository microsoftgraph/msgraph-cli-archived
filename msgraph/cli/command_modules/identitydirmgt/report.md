# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az identitydirmgt|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az identitydirmgt` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az identitydirmgt contact-org-contact|contacts.orgContact|[commands](#CommandsIncontacts.orgContact)|
|az identitydirmgt contact|contacts|[commands](#CommandsIncontacts)|
|az identitydirmgt contract-contract|contracts.contract|[commands](#CommandsIncontracts.contract)|
|az identitydirmgt contract|contracts|[commands](#CommandsIncontracts)|
|az identitydirmgt device-device|devices.device|[commands](#CommandsIndevices.device)|
|az identitydirmgt device|devices|[commands](#CommandsIndevices)|
|az identitydirmgt directory-directory|directory.directory|[commands](#CommandsIndirectory.directory)|
|az identitydirmgt directory|directory|[commands](#CommandsIndirectory)|
|az identitydirmgt directory-administrative-unit|directory.administrativeUnits|[commands](#CommandsIndirectory.administrativeUnits)|
|az identitydirmgt directory-role-directory-role|directoryRoles.directoryRole|[commands](#CommandsIndirectoryRoles.directoryRole)|
|az identitydirmgt directory-role|directoryRoles|[commands](#CommandsIndirectoryRoles)|
|az identitydirmgt directory-role-template-directory-role-template|directoryRoleTemplates.directoryRoleTemplate|[commands](#CommandsIndirectoryRoleTemplates.directoryRoleTemplate)|
|az identitydirmgt directory-role-template|directoryRoleTemplates|[commands](#CommandsIndirectoryRoleTemplates)|
|az identitydirmgt domain-domain|domains.domain|[commands](#CommandsIndomains.domain)|
|az identitydirmgt domain|domains|[commands](#CommandsIndomains)|
|az identitydirmgt organization-organization|organization.organization|[commands](#CommandsInorganization.organization)|
|az identitydirmgt organization|organization|[commands](#CommandsInorganization)|
|az identitydirmgt subscribed-sku-subscribed-sku|subscribedSkus.subscribedSku|[commands](#CommandsInsubscribedSkus.subscribedSku)|
|az identitydirmgt user|users|[commands](#CommandsInusers)|

## COMMANDS
### <a name="CommandsIncontacts">Commands in `az identitydirmgt contact` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt contact check-member-group](#contactscheckMemberGroups)|checkMemberGroups|[Parameters](#ParameterscontactscheckMemberGroups)|Not Found|
|[az identitydirmgt contact check-member-object](#contactscheckMemberObjects)|checkMemberObjects|[Parameters](#ParameterscontactscheckMemberObjects)|Not Found|
|[az identitydirmgt contact create-ref-direct-report](#contactsCreateRefDirectReports)|CreateRefDirectReports|[Parameters](#ParameterscontactsCreateRefDirectReports)|Not Found|
|[az identitydirmgt contact create-ref-member-of](#contactsCreateRefMemberOf)|CreateRefMemberOf|[Parameters](#ParameterscontactsCreateRefMemberOf)|Not Found|
|[az identitydirmgt contact create-ref-transitive-member-of](#contactsCreateRefTransitiveMemberOf)|CreateRefTransitiveMemberOf|[Parameters](#ParameterscontactsCreateRefTransitiveMemberOf)|Not Found|
|[az identitydirmgt contact delete-ref-manager](#contactsDeleteRefManager)|DeleteRefManager|[Parameters](#ParameterscontactsDeleteRefManager)|Not Found|
|[az identitydirmgt contact delta](#contactsdelta)|delta|[Parameters](#Parameterscontactsdelta)|Not Found|
|[az identitydirmgt contact get-available-extension-property](#contactsgetAvailableExtensionProperties)|getAvailableExtensionProperties|[Parameters](#ParameterscontactsgetAvailableExtensionProperties)|Not Found|
|[az identitydirmgt contact get-by-id](#contactsgetByIds)|getByIds|[Parameters](#ParameterscontactsgetByIds)|Not Found|
|[az identitydirmgt contact get-member-group](#contactsgetMemberGroups)|getMemberGroups|[Parameters](#ParameterscontactsgetMemberGroups)|Not Found|
|[az identitydirmgt contact get-member-object](#contactsgetMemberObjects)|getMemberObjects|[Parameters](#ParameterscontactsgetMemberObjects)|Not Found|
|[az identitydirmgt contact list-direct-report](#contactsListDirectReports)|ListDirectReports|[Parameters](#ParameterscontactsListDirectReports)|Not Found|
|[az identitydirmgt contact list-member-of](#contactsListMemberOf)|ListMemberOf|[Parameters](#ParameterscontactsListMemberOf)|Not Found|
|[az identitydirmgt contact list-ref-direct-report](#contactsListRefDirectReports)|ListRefDirectReports|[Parameters](#ParameterscontactsListRefDirectReports)|Not Found|
|[az identitydirmgt contact list-ref-member-of](#contactsListRefMemberOf)|ListRefMemberOf|[Parameters](#ParameterscontactsListRefMemberOf)|Not Found|
|[az identitydirmgt contact list-ref-transitive-member-of](#contactsListRefTransitiveMemberOf)|ListRefTransitiveMemberOf|[Parameters](#ParameterscontactsListRefTransitiveMemberOf)|Not Found|
|[az identitydirmgt contact list-transitive-member-of](#contactsListTransitiveMemberOf)|ListTransitiveMemberOf|[Parameters](#ParameterscontactsListTransitiveMemberOf)|Not Found|
|[az identitydirmgt contact restore](#contactsrestore)|restore|[Parameters](#Parameterscontactsrestore)|Not Found|
|[az identitydirmgt contact set-ref-manager](#contactsSetRefManager)|SetRefManager|[Parameters](#ParameterscontactsSetRefManager)|Not Found|
|[az identitydirmgt contact show-manager](#contactsGetManager)|GetManager|[Parameters](#ParameterscontactsGetManager)|Not Found|
|[az identitydirmgt contact show-ref-manager](#contactsGetRefManager)|GetRefManager|[Parameters](#ParameterscontactsGetRefManager)|Not Found|
|[az identitydirmgt contact validate-property](#contactsvalidateProperties)|validateProperties|[Parameters](#ParameterscontactsvalidateProperties)|Not Found|

### <a name="CommandsIncontacts.orgContact">Commands in `az identitydirmgt contact-org-contact` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt contact-org-contact create-org-contact](#contacts.orgContactCreateOrgContact)|CreateOrgContact|[Parameters](#Parameterscontacts.orgContactCreateOrgContact)|Not Found|
|[az identitydirmgt contact-org-contact delete-org-contact](#contacts.orgContactDeleteOrgContact)|DeleteOrgContact|[Parameters](#Parameterscontacts.orgContactDeleteOrgContact)|Not Found|
|[az identitydirmgt contact-org-contact list-org-contact](#contacts.orgContactListOrgContact)|ListOrgContact|[Parameters](#Parameterscontacts.orgContactListOrgContact)|Not Found|
|[az identitydirmgt contact-org-contact show-org-contact](#contacts.orgContactGetOrgContact)|GetOrgContact|[Parameters](#Parameterscontacts.orgContactGetOrgContact)|Not Found|
|[az identitydirmgt contact-org-contact update-org-contact](#contacts.orgContactUpdateOrgContact)|UpdateOrgContact|[Parameters](#Parameterscontacts.orgContactUpdateOrgContact)|Not Found|

### <a name="CommandsIncontracts">Commands in `az identitydirmgt contract` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt contract check-member-group](#contractscheckMemberGroups)|checkMemberGroups|[Parameters](#ParameterscontractscheckMemberGroups)|Not Found|
|[az identitydirmgt contract check-member-object](#contractscheckMemberObjects)|checkMemberObjects|[Parameters](#ParameterscontractscheckMemberObjects)|Not Found|
|[az identitydirmgt contract get-available-extension-property](#contractsgetAvailableExtensionProperties)|getAvailableExtensionProperties|[Parameters](#ParameterscontractsgetAvailableExtensionProperties)|Not Found|
|[az identitydirmgt contract get-by-id](#contractsgetByIds)|getByIds|[Parameters](#ParameterscontractsgetByIds)|Not Found|
|[az identitydirmgt contract get-member-group](#contractsgetMemberGroups)|getMemberGroups|[Parameters](#ParameterscontractsgetMemberGroups)|Not Found|
|[az identitydirmgt contract get-member-object](#contractsgetMemberObjects)|getMemberObjects|[Parameters](#ParameterscontractsgetMemberObjects)|Not Found|
|[az identitydirmgt contract restore](#contractsrestore)|restore|[Parameters](#Parameterscontractsrestore)|Not Found|
|[az identitydirmgt contract validate-property](#contractsvalidateProperties)|validateProperties|[Parameters](#ParameterscontractsvalidateProperties)|Not Found|

### <a name="CommandsIncontracts.contract">Commands in `az identitydirmgt contract-contract` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt contract-contract create-contract](#contracts.contractCreateContract)|CreateContract|[Parameters](#Parameterscontracts.contractCreateContract)|Not Found|
|[az identitydirmgt contract-contract delete-contract](#contracts.contractDeleteContract)|DeleteContract|[Parameters](#Parameterscontracts.contractDeleteContract)|Not Found|
|[az identitydirmgt contract-contract list-contract](#contracts.contractListContract)|ListContract|[Parameters](#Parameterscontracts.contractListContract)|Not Found|
|[az identitydirmgt contract-contract show-contract](#contracts.contractGetContract)|GetContract|[Parameters](#Parameterscontracts.contractGetContract)|Not Found|
|[az identitydirmgt contract-contract update-contract](#contracts.contractUpdateContract)|UpdateContract|[Parameters](#Parameterscontracts.contractUpdateContract)|Not Found|

### <a name="CommandsIndevices">Commands in `az identitydirmgt device` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt device check-member-group](#devicescheckMemberGroups)|checkMemberGroups|[Parameters](#ParametersdevicescheckMemberGroups)|Not Found|
|[az identitydirmgt device check-member-object](#devicescheckMemberObjects)|checkMemberObjects|[Parameters](#ParametersdevicescheckMemberObjects)|Not Found|
|[az identitydirmgt device create-extension](#devicesCreateExtensions)|CreateExtensions|[Parameters](#ParametersdevicesCreateExtensions)|Not Found|
|[az identitydirmgt device create-ref-member-of](#devicesCreateRefMemberOf)|CreateRefMemberOf|[Parameters](#ParametersdevicesCreateRefMemberOf)|Not Found|
|[az identitydirmgt device create-ref-registered-owner](#devicesCreateRefRegisteredOwners)|CreateRefRegisteredOwners|[Parameters](#ParametersdevicesCreateRefRegisteredOwners)|Not Found|
|[az identitydirmgt device create-ref-registered-user](#devicesCreateRefRegisteredUsers)|CreateRefRegisteredUsers|[Parameters](#ParametersdevicesCreateRefRegisteredUsers)|Not Found|
|[az identitydirmgt device create-ref-transitive-member-of](#devicesCreateRefTransitiveMemberOf)|CreateRefTransitiveMemberOf|[Parameters](#ParametersdevicesCreateRefTransitiveMemberOf)|Not Found|
|[az identitydirmgt device delete-extension](#devicesDeleteExtensions)|DeleteExtensions|[Parameters](#ParametersdevicesDeleteExtensions)|Not Found|
|[az identitydirmgt device get-available-extension-property](#devicesgetAvailableExtensionProperties)|getAvailableExtensionProperties|[Parameters](#ParametersdevicesgetAvailableExtensionProperties)|Not Found|
|[az identitydirmgt device get-by-id](#devicesgetByIds)|getByIds|[Parameters](#ParametersdevicesgetByIds)|Not Found|
|[az identitydirmgt device get-member-group](#devicesgetMemberGroups)|getMemberGroups|[Parameters](#ParametersdevicesgetMemberGroups)|Not Found|
|[az identitydirmgt device get-member-object](#devicesgetMemberObjects)|getMemberObjects|[Parameters](#ParametersdevicesgetMemberObjects)|Not Found|
|[az identitydirmgt device list-extension](#devicesListExtensions)|ListExtensions|[Parameters](#ParametersdevicesListExtensions)|Not Found|
|[az identitydirmgt device list-member-of](#devicesListMemberOf)|ListMemberOf|[Parameters](#ParametersdevicesListMemberOf)|Not Found|
|[az identitydirmgt device list-ref-member-of](#devicesListRefMemberOf)|ListRefMemberOf|[Parameters](#ParametersdevicesListRefMemberOf)|Not Found|
|[az identitydirmgt device list-ref-registered-owner](#devicesListRefRegisteredOwners)|ListRefRegisteredOwners|[Parameters](#ParametersdevicesListRefRegisteredOwners)|Not Found|
|[az identitydirmgt device list-ref-registered-user](#devicesListRefRegisteredUsers)|ListRefRegisteredUsers|[Parameters](#ParametersdevicesListRefRegisteredUsers)|Not Found|
|[az identitydirmgt device list-ref-transitive-member-of](#devicesListRefTransitiveMemberOf)|ListRefTransitiveMemberOf|[Parameters](#ParametersdevicesListRefTransitiveMemberOf)|Not Found|
|[az identitydirmgt device list-registered-owner](#devicesListRegisteredOwners)|ListRegisteredOwners|[Parameters](#ParametersdevicesListRegisteredOwners)|Not Found|
|[az identitydirmgt device list-registered-user](#devicesListRegisteredUsers)|ListRegisteredUsers|[Parameters](#ParametersdevicesListRegisteredUsers)|Not Found|
|[az identitydirmgt device list-transitive-member-of](#devicesListTransitiveMemberOf)|ListTransitiveMemberOf|[Parameters](#ParametersdevicesListTransitiveMemberOf)|Not Found|
|[az identitydirmgt device restore](#devicesrestore)|restore|[Parameters](#Parametersdevicesrestore)|Not Found|
|[az identitydirmgt device show-extension](#devicesGetExtensions)|GetExtensions|[Parameters](#ParametersdevicesGetExtensions)|Not Found|
|[az identitydirmgt device update-extension](#devicesUpdateExtensions)|UpdateExtensions|[Parameters](#ParametersdevicesUpdateExtensions)|Not Found|
|[az identitydirmgt device validate-property](#devicesvalidateProperties)|validateProperties|[Parameters](#ParametersdevicesvalidateProperties)|Not Found|

### <a name="CommandsIndevices.device">Commands in `az identitydirmgt device-device` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt device-device create-device](#devices.deviceCreateDevice)|CreateDevice|[Parameters](#Parametersdevices.deviceCreateDevice)|Not Found|
|[az identitydirmgt device-device delete-device](#devices.deviceDeleteDevice)|DeleteDevice|[Parameters](#Parametersdevices.deviceDeleteDevice)|Not Found|
|[az identitydirmgt device-device list-device](#devices.deviceListDevice)|ListDevice|[Parameters](#Parametersdevices.deviceListDevice)|Not Found|
|[az identitydirmgt device-device show-device](#devices.deviceGetDevice)|GetDevice|[Parameters](#Parametersdevices.deviceGetDevice)|Not Found|
|[az identitydirmgt device-device update-device](#devices.deviceUpdateDevice)|UpdateDevice|[Parameters](#Parametersdevices.deviceUpdateDevice)|Not Found|

### <a name="CommandsIndirectory">Commands in `az identitydirmgt directory` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt directory create-administrative-unit](#directoryCreateAdministrativeUnits)|CreateAdministrativeUnits|[Parameters](#ParametersdirectoryCreateAdministrativeUnits)|Not Found|
|[az identitydirmgt directory create-deleted-item](#directoryCreateDeletedItems)|CreateDeletedItems|[Parameters](#ParametersdirectoryCreateDeletedItems)|Not Found|
|[az identitydirmgt directory delete-administrative-unit](#directoryDeleteAdministrativeUnits)|DeleteAdministrativeUnits|[Parameters](#ParametersdirectoryDeleteAdministrativeUnits)|Not Found|
|[az identitydirmgt directory delete-deleted-item](#directoryDeleteDeletedItems)|DeleteDeletedItems|[Parameters](#ParametersdirectoryDeleteDeletedItems)|Not Found|
|[az identitydirmgt directory list-administrative-unit](#directoryListAdministrativeUnits)|ListAdministrativeUnits|[Parameters](#ParametersdirectoryListAdministrativeUnits)|Not Found|
|[az identitydirmgt directory list-deleted-item](#directoryListDeletedItems)|ListDeletedItems|[Parameters](#ParametersdirectoryListDeletedItems)|Not Found|
|[az identitydirmgt directory show-administrative-unit](#directoryGetAdministrativeUnits)|GetAdministrativeUnits|[Parameters](#ParametersdirectoryGetAdministrativeUnits)|Not Found|
|[az identitydirmgt directory show-deleted-item](#directoryGetDeletedItems)|GetDeletedItems|[Parameters](#ParametersdirectoryGetDeletedItems)|Not Found|
|[az identitydirmgt directory update-administrative-unit](#directoryUpdateAdministrativeUnits)|UpdateAdministrativeUnits|[Parameters](#ParametersdirectoryUpdateAdministrativeUnits)|Not Found|
|[az identitydirmgt directory update-deleted-item](#directoryUpdateDeletedItems)|UpdateDeletedItems|[Parameters](#ParametersdirectoryUpdateDeletedItems)|Not Found|

### <a name="CommandsIndirectory.administrativeUnits">Commands in `az identitydirmgt directory-administrative-unit` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt directory-administrative-unit create-extension](#directory.administrativeUnitsCreateExtensions)|CreateExtensions|[Parameters](#Parametersdirectory.administrativeUnitsCreateExtensions)|Not Found|
|[az identitydirmgt directory-administrative-unit create-ref-member](#directory.administrativeUnitsCreateRefMembers)|CreateRefMembers|[Parameters](#Parametersdirectory.administrativeUnitsCreateRefMembers)|Not Found|
|[az identitydirmgt directory-administrative-unit create-scoped-role-member](#directory.administrativeUnitsCreateScopedRoleMembers)|CreateScopedRoleMembers|[Parameters](#Parametersdirectory.administrativeUnitsCreateScopedRoleMembers)|Not Found|
|[az identitydirmgt directory-administrative-unit delete-extension](#directory.administrativeUnitsDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersdirectory.administrativeUnitsDeleteExtensions)|Not Found|
|[az identitydirmgt directory-administrative-unit delete-scoped-role-member](#directory.administrativeUnitsDeleteScopedRoleMembers)|DeleteScopedRoleMembers|[Parameters](#Parametersdirectory.administrativeUnitsDeleteScopedRoleMembers)|Not Found|
|[az identitydirmgt directory-administrative-unit delta](#directory.administrativeUnitsdelta)|delta|[Parameters](#Parametersdirectory.administrativeUnitsdelta)|Not Found|
|[az identitydirmgt directory-administrative-unit list-extension](#directory.administrativeUnitsListExtensions)|ListExtensions|[Parameters](#Parametersdirectory.administrativeUnitsListExtensions)|Not Found|
|[az identitydirmgt directory-administrative-unit list-member](#directory.administrativeUnitsListMembers)|ListMembers|[Parameters](#Parametersdirectory.administrativeUnitsListMembers)|Not Found|
|[az identitydirmgt directory-administrative-unit list-ref-member](#directory.administrativeUnitsListRefMembers)|ListRefMembers|[Parameters](#Parametersdirectory.administrativeUnitsListRefMembers)|Not Found|
|[az identitydirmgt directory-administrative-unit list-scoped-role-member](#directory.administrativeUnitsListScopedRoleMembers)|ListScopedRoleMembers|[Parameters](#Parametersdirectory.administrativeUnitsListScopedRoleMembers)|Not Found|
|[az identitydirmgt directory-administrative-unit show-extension](#directory.administrativeUnitsGetExtensions)|GetExtensions|[Parameters](#Parametersdirectory.administrativeUnitsGetExtensions)|Not Found|
|[az identitydirmgt directory-administrative-unit show-scoped-role-member](#directory.administrativeUnitsGetScopedRoleMembers)|GetScopedRoleMembers|[Parameters](#Parametersdirectory.administrativeUnitsGetScopedRoleMembers)|Not Found|
|[az identitydirmgt directory-administrative-unit update-extension](#directory.administrativeUnitsUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersdirectory.administrativeUnitsUpdateExtensions)|Not Found|
|[az identitydirmgt directory-administrative-unit update-scoped-role-member](#directory.administrativeUnitsUpdateScopedRoleMembers)|UpdateScopedRoleMembers|[Parameters](#Parametersdirectory.administrativeUnitsUpdateScopedRoleMembers)|Not Found|

### <a name="CommandsIndirectory.directory">Commands in `az identitydirmgt directory-directory` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt directory-directory show-directory](#directory.directoryGetDirectory)|GetDirectory|[Parameters](#Parametersdirectory.directoryGetDirectory)|Not Found|
|[az identitydirmgt directory-directory update-directory](#directory.directoryUpdateDirectory)|UpdateDirectory|[Parameters](#Parametersdirectory.directoryUpdateDirectory)|Not Found|

### <a name="CommandsIndirectoryRoles">Commands in `az identitydirmgt directory-role` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt directory-role check-member-group](#directoryRolescheckMemberGroups)|checkMemberGroups|[Parameters](#ParametersdirectoryRolescheckMemberGroups)|Not Found|
|[az identitydirmgt directory-role check-member-object](#directoryRolescheckMemberObjects)|checkMemberObjects|[Parameters](#ParametersdirectoryRolescheckMemberObjects)|Not Found|
|[az identitydirmgt directory-role create-ref-member](#directoryRolesCreateRefMembers)|CreateRefMembers|[Parameters](#ParametersdirectoryRolesCreateRefMembers)|Not Found|
|[az identitydirmgt directory-role create-scoped-member](#directoryRolesCreateScopedMembers)|CreateScopedMembers|[Parameters](#ParametersdirectoryRolesCreateScopedMembers)|Not Found|
|[az identitydirmgt directory-role delete-scoped-member](#directoryRolesDeleteScopedMembers)|DeleteScopedMembers|[Parameters](#ParametersdirectoryRolesDeleteScopedMembers)|Not Found|
|[az identitydirmgt directory-role delta](#directoryRolesdelta)|delta|[Parameters](#ParametersdirectoryRolesdelta)|Not Found|
|[az identitydirmgt directory-role get-available-extension-property](#directoryRolesgetAvailableExtensionProperties)|getAvailableExtensionProperties|[Parameters](#ParametersdirectoryRolesgetAvailableExtensionProperties)|Not Found|
|[az identitydirmgt directory-role get-by-id](#directoryRolesgetByIds)|getByIds|[Parameters](#ParametersdirectoryRolesgetByIds)|Not Found|
|[az identitydirmgt directory-role get-member-group](#directoryRolesgetMemberGroups)|getMemberGroups|[Parameters](#ParametersdirectoryRolesgetMemberGroups)|Not Found|
|[az identitydirmgt directory-role get-member-object](#directoryRolesgetMemberObjects)|getMemberObjects|[Parameters](#ParametersdirectoryRolesgetMemberObjects)|Not Found|
|[az identitydirmgt directory-role list-member](#directoryRolesListMembers)|ListMembers|[Parameters](#ParametersdirectoryRolesListMembers)|Not Found|
|[az identitydirmgt directory-role list-ref-member](#directoryRolesListRefMembers)|ListRefMembers|[Parameters](#ParametersdirectoryRolesListRefMembers)|Not Found|
|[az identitydirmgt directory-role list-scoped-member](#directoryRolesListScopedMembers)|ListScopedMembers|[Parameters](#ParametersdirectoryRolesListScopedMembers)|Not Found|
|[az identitydirmgt directory-role restore](#directoryRolesrestore)|restore|[Parameters](#ParametersdirectoryRolesrestore)|Not Found|
|[az identitydirmgt directory-role show-scoped-member](#directoryRolesGetScopedMembers)|GetScopedMembers|[Parameters](#ParametersdirectoryRolesGetScopedMembers)|Not Found|
|[az identitydirmgt directory-role update-scoped-member](#directoryRolesUpdateScopedMembers)|UpdateScopedMembers|[Parameters](#ParametersdirectoryRolesUpdateScopedMembers)|Not Found|
|[az identitydirmgt directory-role validate-property](#directoryRolesvalidateProperties)|validateProperties|[Parameters](#ParametersdirectoryRolesvalidateProperties)|Not Found|

### <a name="CommandsIndirectoryRoles.directoryRole">Commands in `az identitydirmgt directory-role-directory-role` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt directory-role-directory-role create-directory-role](#directoryRoles.directoryRoleCreateDirectoryRole)|CreateDirectoryRole|[Parameters](#ParametersdirectoryRoles.directoryRoleCreateDirectoryRole)|Not Found|
|[az identitydirmgt directory-role-directory-role delete-directory-role](#directoryRoles.directoryRoleDeleteDirectoryRole)|DeleteDirectoryRole|[Parameters](#ParametersdirectoryRoles.directoryRoleDeleteDirectoryRole)|Not Found|
|[az identitydirmgt directory-role-directory-role list-directory-role](#directoryRoles.directoryRoleListDirectoryRole)|ListDirectoryRole|[Parameters](#ParametersdirectoryRoles.directoryRoleListDirectoryRole)|Not Found|
|[az identitydirmgt directory-role-directory-role show-directory-role](#directoryRoles.directoryRoleGetDirectoryRole)|GetDirectoryRole|[Parameters](#ParametersdirectoryRoles.directoryRoleGetDirectoryRole)|Not Found|
|[az identitydirmgt directory-role-directory-role update-directory-role](#directoryRoles.directoryRoleUpdateDirectoryRole)|UpdateDirectoryRole|[Parameters](#ParametersdirectoryRoles.directoryRoleUpdateDirectoryRole)|Not Found|

### <a name="CommandsIndirectoryRoleTemplates">Commands in `az identitydirmgt directory-role-template` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt directory-role-template check-member-group](#directoryRoleTemplatescheckMemberGroups)|checkMemberGroups|[Parameters](#ParametersdirectoryRoleTemplatescheckMemberGroups)|Not Found|
|[az identitydirmgt directory-role-template check-member-object](#directoryRoleTemplatescheckMemberObjects)|checkMemberObjects|[Parameters](#ParametersdirectoryRoleTemplatescheckMemberObjects)|Not Found|
|[az identitydirmgt directory-role-template get-available-extension-property](#directoryRoleTemplatesgetAvailableExtensionProperties)|getAvailableExtensionProperties|[Parameters](#ParametersdirectoryRoleTemplatesgetAvailableExtensionProperties)|Not Found|
|[az identitydirmgt directory-role-template get-by-id](#directoryRoleTemplatesgetByIds)|getByIds|[Parameters](#ParametersdirectoryRoleTemplatesgetByIds)|Not Found|
|[az identitydirmgt directory-role-template get-member-group](#directoryRoleTemplatesgetMemberGroups)|getMemberGroups|[Parameters](#ParametersdirectoryRoleTemplatesgetMemberGroups)|Not Found|
|[az identitydirmgt directory-role-template get-member-object](#directoryRoleTemplatesgetMemberObjects)|getMemberObjects|[Parameters](#ParametersdirectoryRoleTemplatesgetMemberObjects)|Not Found|
|[az identitydirmgt directory-role-template restore](#directoryRoleTemplatesrestore)|restore|[Parameters](#ParametersdirectoryRoleTemplatesrestore)|Not Found|
|[az identitydirmgt directory-role-template validate-property](#directoryRoleTemplatesvalidateProperties)|validateProperties|[Parameters](#ParametersdirectoryRoleTemplatesvalidateProperties)|Not Found|

### <a name="CommandsIndirectoryRoleTemplates.directoryRoleTemplate">Commands in `az identitydirmgt directory-role-template-directory-role-template` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt directory-role-template-directory-role-template create-directory-role-template](#directoryRoleTemplates.directoryRoleTemplateCreateDirectoryRoleTemplate)|CreateDirectoryRoleTemplate|[Parameters](#ParametersdirectoryRoleTemplates.directoryRoleTemplateCreateDirectoryRoleTemplate)|Not Found|
|[az identitydirmgt directory-role-template-directory-role-template delete-directory-role-template](#directoryRoleTemplates.directoryRoleTemplateDeleteDirectoryRoleTemplate)|DeleteDirectoryRoleTemplate|[Parameters](#ParametersdirectoryRoleTemplates.directoryRoleTemplateDeleteDirectoryRoleTemplate)|Not Found|
|[az identitydirmgt directory-role-template-directory-role-template list-directory-role-template](#directoryRoleTemplates.directoryRoleTemplateListDirectoryRoleTemplate)|ListDirectoryRoleTemplate|[Parameters](#ParametersdirectoryRoleTemplates.directoryRoleTemplateListDirectoryRoleTemplate)|Not Found|
|[az identitydirmgt directory-role-template-directory-role-template show-directory-role-template](#directoryRoleTemplates.directoryRoleTemplateGetDirectoryRoleTemplate)|GetDirectoryRoleTemplate|[Parameters](#ParametersdirectoryRoleTemplates.directoryRoleTemplateGetDirectoryRoleTemplate)|Not Found|
|[az identitydirmgt directory-role-template-directory-role-template update-directory-role-template](#directoryRoleTemplates.directoryRoleTemplateUpdateDirectoryRoleTemplate)|UpdateDirectoryRoleTemplate|[Parameters](#ParametersdirectoryRoleTemplates.directoryRoleTemplateUpdateDirectoryRoleTemplate)|Not Found|

### <a name="CommandsIndomains">Commands in `az identitydirmgt domain` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt domain create-ref-domain-name-reference](#domainsCreateRefDomainNameReferences)|CreateRefDomainNameReferences|[Parameters](#ParametersdomainsCreateRefDomainNameReferences)|Not Found|
|[az identitydirmgt domain create-service-configuration-record](#domainsCreateServiceConfigurationRecords)|CreateServiceConfigurationRecords|[Parameters](#ParametersdomainsCreateServiceConfigurationRecords)|Not Found|
|[az identitydirmgt domain create-verification-dns-record](#domainsCreateVerificationDnsRecords)|CreateVerificationDnsRecords|[Parameters](#ParametersdomainsCreateVerificationDnsRecords)|Not Found|
|[az identitydirmgt domain delete-service-configuration-record](#domainsDeleteServiceConfigurationRecords)|DeleteServiceConfigurationRecords|[Parameters](#ParametersdomainsDeleteServiceConfigurationRecords)|Not Found|
|[az identitydirmgt domain delete-verification-dns-record](#domainsDeleteVerificationDnsRecords)|DeleteVerificationDnsRecords|[Parameters](#ParametersdomainsDeleteVerificationDnsRecords)|Not Found|
|[az identitydirmgt domain force-delete](#domainsforceDelete)|forceDelete|[Parameters](#ParametersdomainsforceDelete)|Not Found|
|[az identitydirmgt domain list-domain-name-reference](#domainsListDomainNameReferences)|ListDomainNameReferences|[Parameters](#ParametersdomainsListDomainNameReferences)|Not Found|
|[az identitydirmgt domain list-ref-domain-name-reference](#domainsListRefDomainNameReferences)|ListRefDomainNameReferences|[Parameters](#ParametersdomainsListRefDomainNameReferences)|Not Found|
|[az identitydirmgt domain list-service-configuration-record](#domainsListServiceConfigurationRecords)|ListServiceConfigurationRecords|[Parameters](#ParametersdomainsListServiceConfigurationRecords)|Not Found|
|[az identitydirmgt domain list-verification-dns-record](#domainsListVerificationDnsRecords)|ListVerificationDnsRecords|[Parameters](#ParametersdomainsListVerificationDnsRecords)|Not Found|
|[az identitydirmgt domain show-service-configuration-record](#domainsGetServiceConfigurationRecords)|GetServiceConfigurationRecords|[Parameters](#ParametersdomainsGetServiceConfigurationRecords)|Not Found|
|[az identitydirmgt domain show-verification-dns-record](#domainsGetVerificationDnsRecords)|GetVerificationDnsRecords|[Parameters](#ParametersdomainsGetVerificationDnsRecords)|Not Found|
|[az identitydirmgt domain update-service-configuration-record](#domainsUpdateServiceConfigurationRecords)|UpdateServiceConfigurationRecords|[Parameters](#ParametersdomainsUpdateServiceConfigurationRecords)|Not Found|
|[az identitydirmgt domain update-verification-dns-record](#domainsUpdateVerificationDnsRecords)|UpdateVerificationDnsRecords|[Parameters](#ParametersdomainsUpdateVerificationDnsRecords)|Not Found|
|[az identitydirmgt domain verify](#domainsverify)|verify|[Parameters](#Parametersdomainsverify)|Not Found|

### <a name="CommandsIndomains.domain">Commands in `az identitydirmgt domain-domain` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt domain-domain create-domain](#domains.domainCreateDomain)|CreateDomain|[Parameters](#Parametersdomains.domainCreateDomain)|Not Found|
|[az identitydirmgt domain-domain delete-domain](#domains.domainDeleteDomain)|DeleteDomain|[Parameters](#Parametersdomains.domainDeleteDomain)|Not Found|
|[az identitydirmgt domain-domain list-domain](#domains.domainListDomain)|ListDomain|[Parameters](#Parametersdomains.domainListDomain)|Not Found|
|[az identitydirmgt domain-domain show-domain](#domains.domainGetDomain)|GetDomain|[Parameters](#Parametersdomains.domainGetDomain)|Not Found|
|[az identitydirmgt domain-domain update-domain](#domains.domainUpdateDomain)|UpdateDomain|[Parameters](#Parametersdomains.domainUpdateDomain)|Not Found|

### <a name="CommandsInorganization">Commands in `az identitydirmgt organization` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt organization check-member-group](#organizationcheckMemberGroups)|checkMemberGroups|[Parameters](#ParametersorganizationcheckMemberGroups)|Not Found|
|[az identitydirmgt organization check-member-object](#organizationcheckMemberObjects)|checkMemberObjects|[Parameters](#ParametersorganizationcheckMemberObjects)|Not Found|
|[az identitydirmgt organization create-extension](#organizationCreateExtensions)|CreateExtensions|[Parameters](#ParametersorganizationCreateExtensions)|Not Found|
|[az identitydirmgt organization delete-extension](#organizationDeleteExtensions)|DeleteExtensions|[Parameters](#ParametersorganizationDeleteExtensions)|Not Found|
|[az identitydirmgt organization get-available-extension-property](#organizationgetAvailableExtensionProperties)|getAvailableExtensionProperties|[Parameters](#ParametersorganizationgetAvailableExtensionProperties)|Not Found|
|[az identitydirmgt organization get-by-id](#organizationgetByIds)|getByIds|[Parameters](#ParametersorganizationgetByIds)|Not Found|
|[az identitydirmgt organization get-member-group](#organizationgetMemberGroups)|getMemberGroups|[Parameters](#ParametersorganizationgetMemberGroups)|Not Found|
|[az identitydirmgt organization get-member-object](#organizationgetMemberObjects)|getMemberObjects|[Parameters](#ParametersorganizationgetMemberObjects)|Not Found|
|[az identitydirmgt organization list-extension](#organizationListExtensions)|ListExtensions|[Parameters](#ParametersorganizationListExtensions)|Not Found|
|[az identitydirmgt organization restore](#organizationrestore)|restore|[Parameters](#Parametersorganizationrestore)|Not Found|
|[az identitydirmgt organization set-mobile-device-management-authority](#organizationsetMobileDeviceManagementAuthority)|setMobileDeviceManagementAuthority|[Parameters](#ParametersorganizationsetMobileDeviceManagementAuthority)|Not Found|
|[az identitydirmgt organization show-extension](#organizationGetExtensions)|GetExtensions|[Parameters](#ParametersorganizationGetExtensions)|Not Found|
|[az identitydirmgt organization update-extension](#organizationUpdateExtensions)|UpdateExtensions|[Parameters](#ParametersorganizationUpdateExtensions)|Not Found|
|[az identitydirmgt organization validate-property](#organizationvalidateProperties)|validateProperties|[Parameters](#ParametersorganizationvalidateProperties)|Not Found|

### <a name="CommandsInorganization.organization">Commands in `az identitydirmgt organization-organization` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt organization-organization create-organization](#organization.organizationCreateOrganization)|CreateOrganization|[Parameters](#Parametersorganization.organizationCreateOrganization)|Not Found|
|[az identitydirmgt organization-organization delete-organization](#organization.organizationDeleteOrganization)|DeleteOrganization|[Parameters](#Parametersorganization.organizationDeleteOrganization)|Not Found|
|[az identitydirmgt organization-organization list-organization](#organization.organizationListOrganization)|ListOrganization|[Parameters](#Parametersorganization.organizationListOrganization)|Not Found|
|[az identitydirmgt organization-organization show-organization](#organization.organizationGetOrganization)|GetOrganization|[Parameters](#Parametersorganization.organizationGetOrganization)|Not Found|
|[az identitydirmgt organization-organization update-organization](#organization.organizationUpdateOrganization)|UpdateOrganization|[Parameters](#Parametersorganization.organizationUpdateOrganization)|Not Found|

### <a name="CommandsInsubscribedSkus.subscribedSku">Commands in `az identitydirmgt subscribed-sku-subscribed-sku` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt subscribed-sku-subscribed-sku create-subscribed-sku](#subscribedSkus.subscribedSkuCreateSubscribedSku)|CreateSubscribedSku|[Parameters](#ParameterssubscribedSkus.subscribedSkuCreateSubscribedSku)|Not Found|
|[az identitydirmgt subscribed-sku-subscribed-sku delete-subscribed-sku](#subscribedSkus.subscribedSkuDeleteSubscribedSku)|DeleteSubscribedSku|[Parameters](#ParameterssubscribedSkus.subscribedSkuDeleteSubscribedSku)|Not Found|
|[az identitydirmgt subscribed-sku-subscribed-sku list-subscribed-sku](#subscribedSkus.subscribedSkuListSubscribedSku)|ListSubscribedSku|[Parameters](#ParameterssubscribedSkus.subscribedSkuListSubscribedSku)|Not Found|
|[az identitydirmgt subscribed-sku-subscribed-sku show-subscribed-sku](#subscribedSkus.subscribedSkuGetSubscribedSku)|GetSubscribedSku|[Parameters](#ParameterssubscribedSkus.subscribedSkuGetSubscribedSku)|Not Found|
|[az identitydirmgt subscribed-sku-subscribed-sku update-subscribed-sku](#subscribedSkus.subscribedSkuUpdateSubscribedSku)|UpdateSubscribedSku|[Parameters](#ParameterssubscribedSkus.subscribedSkuUpdateSubscribedSku)|Not Found|

### <a name="CommandsInusers">Commands in `az identitydirmgt user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitydirmgt user create-scoped-role-member-of](#usersCreateScopedRoleMemberOf)|CreateScopedRoleMemberOf|[Parameters](#ParametersusersCreateScopedRoleMemberOf)|Not Found|
|[az identitydirmgt user delete-scoped-role-member-of](#usersDeleteScopedRoleMemberOf)|DeleteScopedRoleMemberOf|[Parameters](#ParametersusersDeleteScopedRoleMemberOf)|Not Found|
|[az identitydirmgt user list-scoped-role-member-of](#usersListScopedRoleMemberOf)|ListScopedRoleMemberOf|[Parameters](#ParametersusersListScopedRoleMemberOf)|Not Found|
|[az identitydirmgt user show-scoped-role-member-of](#usersGetScopedRoleMemberOf)|GetScopedRoleMemberOf|[Parameters](#ParametersusersGetScopedRoleMemberOf)|Not Found|
|[az identitydirmgt user update-scoped-role-member-of](#usersUpdateScopedRoleMemberOf)|UpdateScopedRoleMemberOf|[Parameters](#ParametersusersUpdateScopedRoleMemberOf)|Not Found|


## COMMAND DETAILS

### group `az identitydirmgt contact`
#### <a name="contactscheckMemberGroups">Command `az identitydirmgt contact check-member-group`</a>

##### <a name="ParameterscontactscheckMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--group-ids**|array||group_ids|groupIds|

#### <a name="contactscheckMemberObjects">Command `az identitydirmgt contact check-member-object`</a>

##### <a name="ParameterscontactscheckMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--ids**|array||ids|ids|

#### <a name="contactsCreateRefDirectReports">Command `az identitydirmgt contact create-ref-direct-report`</a>

##### <a name="ParameterscontactsCreateRefDirectReports">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="contactsCreateRefMemberOf">Command `az identitydirmgt contact create-ref-member-of`</a>

##### <a name="ParameterscontactsCreateRefMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="contactsCreateRefTransitiveMemberOf">Command `az identitydirmgt contact create-ref-transitive-member-of`</a>

##### <a name="ParameterscontactsCreateRefTransitiveMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="contactsDeleteRefManager">Command `az identitydirmgt contact delete-ref-manager`</a>

##### <a name="ParameterscontactsDeleteRefManager">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="contactsdelta">Command `az identitydirmgt contact delta`</a>

##### <a name="Parameterscontactsdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="contactsgetAvailableExtensionProperties">Command `az identitydirmgt contact get-available-extension-property`</a>

##### <a name="ParameterscontactsgetAvailableExtensionProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

#### <a name="contactsgetByIds">Command `az identitydirmgt contact get-by-id`</a>

##### <a name="ParameterscontactsgetByIds">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

#### <a name="contactsgetMemberGroups">Command `az identitydirmgt contact get-member-group`</a>

##### <a name="ParameterscontactsgetMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="contactsgetMemberObjects">Command `az identitydirmgt contact get-member-object`</a>

##### <a name="ParameterscontactsgetMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="contactsListDirectReports">Command `az identitydirmgt contact list-direct-report`</a>

##### <a name="ParameterscontactsListDirectReports">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="contactsListMemberOf">Command `az identitydirmgt contact list-member-of`</a>

##### <a name="ParameterscontactsListMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="contactsListRefDirectReports">Command `az identitydirmgt contact list-ref-direct-report`</a>

##### <a name="ParameterscontactsListRefDirectReports">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="contactsListRefMemberOf">Command `az identitydirmgt contact list-ref-member-of`</a>

##### <a name="ParameterscontactsListRefMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="contactsListRefTransitiveMemberOf">Command `az identitydirmgt contact list-ref-transitive-member-of`</a>

##### <a name="ParameterscontactsListRefTransitiveMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="contactsListTransitiveMemberOf">Command `az identitydirmgt contact list-transitive-member-of`</a>

##### <a name="ParameterscontactsListTransitiveMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="contactsrestore">Command `az identitydirmgt contact restore`</a>

##### <a name="Parameterscontactsrestore">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|

#### <a name="contactsSetRefManager">Command `az identitydirmgt contact set-ref-manager`</a>

##### <a name="ParameterscontactsSetRefManager">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="contactsGetManager">Command `az identitydirmgt contact show-manager`</a>

##### <a name="ParameterscontactsGetManager">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="contactsGetRefManager">Command `az identitydirmgt contact show-ref-manager`</a>

##### <a name="ParameterscontactsGetRefManager">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|

#### <a name="contactsvalidateProperties">Command `az identitydirmgt contact validate-property`</a>

##### <a name="ParameterscontactsvalidateProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--entity-type**|string||entity_type|entityType|
|**--display-name**|string||display_name|displayName|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-behalf-of-user-id**|uuid||on_behalf_of_user_id|onBehalfOfUserId|

### group `az identitydirmgt contact-org-contact`
#### <a name="contacts.orgContactCreateOrgContact">Command `az identitydirmgt contact-org-contact create-org-contact`</a>

##### <a name="Parameterscontacts.orgContactCreateOrgContact">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--addresses**|array||addresses|addresses|
|**--company-name**|string||company_name|companyName|
|**--department**|string||department|department|
|**--display-name**|string||display_name|displayName|
|**--given-name**|string||given_name|givenName|
|**--job-title**|string||job_title|jobTitle|
|**--mail**|string||mail|mail|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-premises-last-sync-date-time**|date-time||on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-provisioning-errors**|array||on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--on-premises-sync-enabled**|boolean||on_premises_sync_enabled|onPremisesSyncEnabled|
|**--phones**|array||phones|phones|
|**--proxy-addresses**|array||proxy_addresses|proxyAddresses|
|**--surname**|string||surname|surname|
|**--direct-reports**|array||direct_reports|directReports|
|**--manager**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|manager|manager|
|**--member-of**|array||member_of|memberOf|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|

#### <a name="contacts.orgContactDeleteOrgContact">Command `az identitydirmgt contact-org-contact delete-org-contact`</a>

##### <a name="Parameterscontacts.orgContactDeleteOrgContact">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="contacts.orgContactListOrgContact">Command `az identitydirmgt contact-org-contact list-org-contact`</a>

##### <a name="Parameterscontacts.orgContactListOrgContact">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="contacts.orgContactGetOrgContact">Command `az identitydirmgt contact-org-contact show-org-contact`</a>

##### <a name="Parameterscontacts.orgContactGetOrgContact">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="contacts.orgContactUpdateOrgContact">Command `az identitydirmgt contact-org-contact update-org-contact`</a>

##### <a name="Parameterscontacts.orgContactUpdateOrgContact">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--org-contact-id**|string|key: id of orgContact|org_contact_id|orgContact-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--addresses**|array||addresses|addresses|
|**--company-name**|string||company_name|companyName|
|**--department**|string||department|department|
|**--display-name**|string||display_name|displayName|
|**--given-name**|string||given_name|givenName|
|**--job-title**|string||job_title|jobTitle|
|**--mail**|string||mail|mail|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-premises-last-sync-date-time**|date-time||on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-provisioning-errors**|array||on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--on-premises-sync-enabled**|boolean||on_premises_sync_enabled|onPremisesSyncEnabled|
|**--phones**|array||phones|phones|
|**--proxy-addresses**|array||proxy_addresses|proxyAddresses|
|**--surname**|string||surname|surname|
|**--direct-reports**|array||direct_reports|directReports|
|**--manager**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|manager|manager|
|**--member-of**|array||member_of|memberOf|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|

### group `az identitydirmgt contract`
#### <a name="contractscheckMemberGroups">Command `az identitydirmgt contract check-member-group`</a>

##### <a name="ParameterscontractscheckMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--group-ids**|array||group_ids|groupIds|

#### <a name="contractscheckMemberObjects">Command `az identitydirmgt contract check-member-object`</a>

##### <a name="ParameterscontractscheckMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--ids**|array||ids|ids|

#### <a name="contractsgetAvailableExtensionProperties">Command `az identitydirmgt contract get-available-extension-property`</a>

##### <a name="ParameterscontractsgetAvailableExtensionProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

#### <a name="contractsgetByIds">Command `az identitydirmgt contract get-by-id`</a>

##### <a name="ParameterscontractsgetByIds">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

#### <a name="contractsgetMemberGroups">Command `az identitydirmgt contract get-member-group`</a>

##### <a name="ParameterscontractsgetMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="contractsgetMemberObjects">Command `az identitydirmgt contract get-member-object`</a>

##### <a name="ParameterscontractsgetMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="contractsrestore">Command `az identitydirmgt contract restore`</a>

##### <a name="Parameterscontractsrestore">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|

#### <a name="contractsvalidateProperties">Command `az identitydirmgt contract validate-property`</a>

##### <a name="ParameterscontractsvalidateProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--entity-type**|string||entity_type|entityType|
|**--display-name**|string||display_name|displayName|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-behalf-of-user-id**|uuid||on_behalf_of_user_id|onBehalfOfUserId|

### group `az identitydirmgt contract-contract`
#### <a name="contracts.contractCreateContract">Command `az identitydirmgt contract-contract create-contract`</a>

##### <a name="Parameterscontracts.contractCreateContract">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--contract-type**|string|Type of contract.Possible values are: SyndicationPartner - Partner that exclusively resells and manages O365 and Intune for this customer. They resell and support their customers. BreadthPartner - Partner has the ability to provide administrative support for this customer. However, the partner is not allowed to resell to the customer.ResellerPartner - Partner that is similar to a syndication partner, except that the partner doesn’t have exclusive access to a tenant. In the syndication case, the customer cannot buy additional direct subscriptions from Microsoft or from other partners.|contract_type|contractType|
|**--customer-id**|uuid|The unique identifier for the customer tenant referenced by this partnership. Corresponds to the id property of the customer tenant's organization resource.|customer_id|customerId|
|**--default-domain-name**|string|A copy of the customer tenant's default domain name. The copy is made when the partnership with the customer is established. It is not automatically updated if the customer tenant's default domain name changes.|default_domain_name|defaultDomainName|
|**--display-name**|string|A copy of the customer tenant's display name. The copy is made when the partnership with the customer is established. It is not automatically updated if the customer tenant's display name changes.|display_name|displayName|

#### <a name="contracts.contractDeleteContract">Command `az identitydirmgt contract-contract delete-contract`</a>

##### <a name="Parameterscontracts.contractDeleteContract">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="contracts.contractListContract">Command `az identitydirmgt contract-contract list-contract`</a>

##### <a name="Parameterscontracts.contractListContract">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="contracts.contractGetContract">Command `az identitydirmgt contract-contract show-contract`</a>

##### <a name="Parameterscontracts.contractGetContract">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="contracts.contractUpdateContract">Command `az identitydirmgt contract-contract update-contract`</a>

##### <a name="Parameterscontracts.contractUpdateContract">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--contract-id**|string|key: id of contract|contract_id|contract-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--contract-type**|string|Type of contract.Possible values are: SyndicationPartner - Partner that exclusively resells and manages O365 and Intune for this customer. They resell and support their customers. BreadthPartner - Partner has the ability to provide administrative support for this customer. However, the partner is not allowed to resell to the customer.ResellerPartner - Partner that is similar to a syndication partner, except that the partner doesn’t have exclusive access to a tenant. In the syndication case, the customer cannot buy additional direct subscriptions from Microsoft or from other partners.|contract_type|contractType|
|**--customer-id**|uuid|The unique identifier for the customer tenant referenced by this partnership. Corresponds to the id property of the customer tenant's organization resource.|customer_id|customerId|
|**--default-domain-name**|string|A copy of the customer tenant's default domain name. The copy is made when the partnership with the customer is established. It is not automatically updated if the customer tenant's default domain name changes.|default_domain_name|defaultDomainName|
|**--display-name**|string|A copy of the customer tenant's display name. The copy is made when the partnership with the customer is established. It is not automatically updated if the customer tenant's display name changes.|display_name|displayName|

### group `az identitydirmgt device`
#### <a name="devicescheckMemberGroups">Command `az identitydirmgt device check-member-group`</a>

##### <a name="ParametersdevicescheckMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--group-ids**|array||group_ids|groupIds|

#### <a name="devicescheckMemberObjects">Command `az identitydirmgt device check-member-object`</a>

##### <a name="ParametersdevicescheckMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--ids**|array||ids|ids|

#### <a name="devicesCreateExtensions">Command `az identitydirmgt device create-extension`</a>

##### <a name="ParametersdevicesCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--id**|string|Read-only.|id|id|

#### <a name="devicesCreateRefMemberOf">Command `az identitydirmgt device create-ref-member-of`</a>

##### <a name="ParametersdevicesCreateRefMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="devicesCreateRefRegisteredOwners">Command `az identitydirmgt device create-ref-registered-owner`</a>

##### <a name="ParametersdevicesCreateRefRegisteredOwners">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="devicesCreateRefRegisteredUsers">Command `az identitydirmgt device create-ref-registered-user`</a>

##### <a name="ParametersdevicesCreateRefRegisteredUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="devicesCreateRefTransitiveMemberOf">Command `az identitydirmgt device create-ref-transitive-member-of`</a>

##### <a name="ParametersdevicesCreateRefTransitiveMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="devicesDeleteExtensions">Command `az identitydirmgt device delete-extension`</a>

##### <a name="ParametersdevicesDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="devicesgetAvailableExtensionProperties">Command `az identitydirmgt device get-available-extension-property`</a>

##### <a name="ParametersdevicesgetAvailableExtensionProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

#### <a name="devicesgetByIds">Command `az identitydirmgt device get-by-id`</a>

##### <a name="ParametersdevicesgetByIds">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

#### <a name="devicesgetMemberGroups">Command `az identitydirmgt device get-member-group`</a>

##### <a name="ParametersdevicesgetMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="devicesgetMemberObjects">Command `az identitydirmgt device get-member-object`</a>

##### <a name="ParametersdevicesgetMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="devicesListExtensions">Command `az identitydirmgt device list-extension`</a>

##### <a name="ParametersdevicesListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="devicesListMemberOf">Command `az identitydirmgt device list-member-of`</a>

##### <a name="ParametersdevicesListMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="devicesListRefMemberOf">Command `az identitydirmgt device list-ref-member-of`</a>

##### <a name="ParametersdevicesListRefMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="devicesListRefRegisteredOwners">Command `az identitydirmgt device list-ref-registered-owner`</a>

##### <a name="ParametersdevicesListRefRegisteredOwners">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="devicesListRefRegisteredUsers">Command `az identitydirmgt device list-ref-registered-user`</a>

##### <a name="ParametersdevicesListRefRegisteredUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="devicesListRefTransitiveMemberOf">Command `az identitydirmgt device list-ref-transitive-member-of`</a>

##### <a name="ParametersdevicesListRefTransitiveMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="devicesListRegisteredOwners">Command `az identitydirmgt device list-registered-owner`</a>

##### <a name="ParametersdevicesListRegisteredOwners">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="devicesListRegisteredUsers">Command `az identitydirmgt device list-registered-user`</a>

##### <a name="ParametersdevicesListRegisteredUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="devicesListTransitiveMemberOf">Command `az identitydirmgt device list-transitive-member-of`</a>

##### <a name="ParametersdevicesListTransitiveMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="devicesrestore">Command `az identitydirmgt device restore`</a>

##### <a name="Parametersdevicesrestore">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|

#### <a name="devicesGetExtensions">Command `az identitydirmgt device show-extension`</a>

##### <a name="ParametersdevicesGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="devicesUpdateExtensions">Command `az identitydirmgt device update-extension`</a>

##### <a name="ParametersdevicesUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="devicesvalidateProperties">Command `az identitydirmgt device validate-property`</a>

##### <a name="ParametersdevicesvalidateProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--entity-type**|string||entity_type|entityType|
|**--display-name**|string||display_name|displayName|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-behalf-of-user-id**|uuid||on_behalf_of_user_id|onBehalfOfUserId|

### group `az identitydirmgt device-device`
#### <a name="devices.deviceCreateDevice">Command `az identitydirmgt device-device create-device`</a>

##### <a name="Parametersdevices.deviceCreateDevice">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--account-enabled**|boolean|true if the account is enabled; otherwise, false. Required.|account_enabled|accountEnabled|
|**--alternative-security-ids**|array|For internal use only. Not nullable.|alternative_security_ids|alternativeSecurityIds|
|**--approximate-last-sign-in-date-time**|date-time|The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|approximate_last_sign_in_date_time|approximateLastSignInDateTime|
|**--compliance-expiration-date-time**|date-time|The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|compliance_expiration_date_time|complianceExpirationDateTime|
|**--device-id**|string|Unique identifier set by Azure Device Registration Service at the time of registration.|device_id|deviceId|
|**--device-metadata**|string|For interal use only. Set to null.|device_metadata|deviceMetadata|
|**--device-version**|integer|For interal use only.|device_version|deviceVersion|
|**--display-name**|string|The display name for the device. Required.|display_name|displayName|
|**--is-compliant**|boolean|true if the device complies with Mobile Device Management (MDM) policies; otherwise, false. Read-only. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices.|is_compliant|isCompliant|
|**--is-managed**|boolean|true if the device is managed by a Mobile Device Management (MDM) app; otherwise, false. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices.|is_managed|isManaged|
|**--mdm-app-id**|string|Application identifier used to register device into MDM. Read-only. Supports $filter.|mdm_app_id|mdmAppId|
|**--on-premises-last-sync-date-time**|date-time|The last time at which the object was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z' Read-only.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-sync-enabled**|boolean|true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--operating-system**|string|The type of operating system on the device. Required.|operating_system|operatingSystem|
|**--operating-system-version**|string|The version of the operating system on the device. Required.|operating_system_version|operatingSystemVersion|
|**--physical-ids**|array|For interal use only. Not nullable.|physical_ids|physicalIds|
|**--profile-type**|string|The profile type of the device. Possible values:RegisteredDevice (default)SecureVMPrinterSharedIoT|profile_type|profileType|
|**--system-labels**|array|List of labels applied to the device by the system.|system_labels|systemLabels|
|**--trust-type**|string|Type of trust for the joined device. Read-only. Possible values: Workplace - indicates bring your own personal devicesAzureAd - Cloud only joined devicesServerAd - on-premises domain joined devices joined to Azure AD. For more details, see Introduction to device management in Azure Active Directory|trust_type|trustType|
|**--member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--registered-owners**|array|The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Currently, there can be only one owner. Read-only. Nullable.|registered_owners|registeredOwners|
|**--registered-users**|array|Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable.|registered_users|registeredUsers|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--extensions**|array|The collection of open extensions defined for the device. Read-only. Nullable.|extensions|extensions|

#### <a name="devices.deviceDeleteDevice">Command `az identitydirmgt device-device delete-device`</a>

##### <a name="Parametersdevices.deviceDeleteDevice">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="devices.deviceListDevice">Command `az identitydirmgt device-device list-device`</a>

##### <a name="Parametersdevices.deviceListDevice">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="devices.deviceGetDevice">Command `az identitydirmgt device-device show-device`</a>

##### <a name="Parametersdevices.deviceGetDevice">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="devices.deviceUpdateDevice">Command `az identitydirmgt device-device update-device`</a>

##### <a name="Parametersdevices.deviceUpdateDevice">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--device-id**|string|key: id of device|device_id|device-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--account-enabled**|boolean|true if the account is enabled; otherwise, false. Required.|account_enabled|accountEnabled|
|**--alternative-security-ids**|array|For internal use only. Not nullable.|alternative_security_ids|alternativeSecurityIds|
|**--approximate-last-sign-in-date-time**|date-time|The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|approximate_last_sign_in_date_time|approximateLastSignInDateTime|
|**--compliance-expiration-date-time**|date-time|The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|compliance_expiration_date_time|complianceExpirationDateTime|
|**--microsoft-graph-device-id**|string|Unique identifier set by Azure Device Registration Service at the time of registration.|microsoft_graph_device_id|deviceId|
|**--device-metadata**|string|For interal use only. Set to null.|device_metadata|deviceMetadata|
|**--device-version**|integer|For interal use only.|device_version|deviceVersion|
|**--display-name**|string|The display name for the device. Required.|display_name|displayName|
|**--is-compliant**|boolean|true if the device complies with Mobile Device Management (MDM) policies; otherwise, false. Read-only. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices.|is_compliant|isCompliant|
|**--is-managed**|boolean|true if the device is managed by a Mobile Device Management (MDM) app; otherwise, false. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices.|is_managed|isManaged|
|**--mdm-app-id**|string|Application identifier used to register device into MDM. Read-only. Supports $filter.|mdm_app_id|mdmAppId|
|**--on-premises-last-sync-date-time**|date-time|The last time at which the object was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z' Read-only.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-sync-enabled**|boolean|true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--operating-system**|string|The type of operating system on the device. Required.|operating_system|operatingSystem|
|**--operating-system-version**|string|The version of the operating system on the device. Required.|operating_system_version|operatingSystemVersion|
|**--physical-ids**|array|For interal use only. Not nullable.|physical_ids|physicalIds|
|**--profile-type**|string|The profile type of the device. Possible values:RegisteredDevice (default)SecureVMPrinterSharedIoT|profile_type|profileType|
|**--system-labels**|array|List of labels applied to the device by the system.|system_labels|systemLabels|
|**--trust-type**|string|Type of trust for the joined device. Read-only. Possible values: Workplace - indicates bring your own personal devicesAzureAd - Cloud only joined devicesServerAd - on-premises domain joined devices joined to Azure AD. For more details, see Introduction to device management in Azure Active Directory|trust_type|trustType|
|**--member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--registered-owners**|array|The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Currently, there can be only one owner. Read-only. Nullable.|registered_owners|registeredOwners|
|**--registered-users**|array|Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable.|registered_users|registeredUsers|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--extensions**|array|The collection of open extensions defined for the device. Read-only. Nullable.|extensions|extensions|

### group `az identitydirmgt directory`
#### <a name="directoryCreateAdministrativeUnits">Command `az identitydirmgt directory create-administrative-unit`</a>

##### <a name="ParametersdirectoryCreateAdministrativeUnits">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|An optional description for the administrative unit.|description|description|
|**--display-name**|string|Display name for the administrative unit.|display_name|displayName|
|**--visibility**|string|Controls whether the adminstrative unit and its members are hidden or public. Can be set to HiddenMembership or Public. If not set, default behavior is Public. When set to HiddenMembership, only members of the administrative unit can list other members of the adminstrative unit.|visibility|visibility|
|**--members**|array|Users and groups that are members of this Adminsitrative Unit. HTTP Methods: GET (list members), POST (add members), DELETE (remove members).|members|members|
|**--scoped-role-members**|array|Scoped-role members of this Administrative Unit.  HTTP Methods: GET (list scopedRoleMemberships), POST (add scopedRoleMembership), DELETE (remove scopedRoleMembership).|scoped_role_members|scopedRoleMembers|
|**--extensions**|array||extensions|extensions|

#### <a name="directoryCreateDeletedItems">Command `az identitydirmgt directory create-deleted-item`</a>

##### <a name="ParametersdirectoryCreateDeletedItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|

#### <a name="directoryDeleteAdministrativeUnits">Command `az identitydirmgt directory delete-administrative-unit`</a>

##### <a name="ParametersdirectoryDeleteAdministrativeUnits">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="directoryDeleteDeletedItems">Command `az identitydirmgt directory delete-deleted-item`</a>

##### <a name="ParametersdirectoryDeleteDeletedItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="directoryListAdministrativeUnits">Command `az identitydirmgt directory list-administrative-unit`</a>

##### <a name="ParametersdirectoryListAdministrativeUnits">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directoryListDeletedItems">Command `az identitydirmgt directory list-deleted-item`</a>

##### <a name="ParametersdirectoryListDeletedItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directoryGetAdministrativeUnits">Command `az identitydirmgt directory show-administrative-unit`</a>

##### <a name="ParametersdirectoryGetAdministrativeUnits">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directoryGetDeletedItems">Command `az identitydirmgt directory show-deleted-item`</a>

##### <a name="ParametersdirectoryGetDeletedItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directoryUpdateAdministrativeUnits">Command `az identitydirmgt directory update-administrative-unit`</a>

##### <a name="ParametersdirectoryUpdateAdministrativeUnits">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|An optional description for the administrative unit.|description|description|
|**--display-name**|string|Display name for the administrative unit.|display_name|displayName|
|**--visibility**|string|Controls whether the adminstrative unit and its members are hidden or public. Can be set to HiddenMembership or Public. If not set, default behavior is Public. When set to HiddenMembership, only members of the administrative unit can list other members of the adminstrative unit.|visibility|visibility|
|**--members**|array|Users and groups that are members of this Adminsitrative Unit. HTTP Methods: GET (list members), POST (add members), DELETE (remove members).|members|members|
|**--scoped-role-members**|array|Scoped-role members of this Administrative Unit.  HTTP Methods: GET (list scopedRoleMemberships), POST (add scopedRoleMembership), DELETE (remove scopedRoleMembership).|scoped_role_members|scopedRoleMembers|
|**--extensions**|array||extensions|extensions|

#### <a name="directoryUpdateDeletedItems">Command `az identitydirmgt directory update-deleted-item`</a>

##### <a name="ParametersdirectoryUpdateDeletedItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-object-id**|string|key: id of directoryObject|directory_object_id|directoryObject-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|

### group `az identitydirmgt directory-administrative-unit`
#### <a name="directory.administrativeUnitsCreateExtensions">Command `az identitydirmgt directory-administrative-unit create-extension`</a>

##### <a name="Parametersdirectory.administrativeUnitsCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--id**|string|Read-only.|id|id|

#### <a name="directory.administrativeUnitsCreateRefMembers">Command `az identitydirmgt directory-administrative-unit create-ref-member`</a>

##### <a name="Parametersdirectory.administrativeUnitsCreateRefMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="directory.administrativeUnitsCreateScopedRoleMembers">Command `az identitydirmgt directory-administrative-unit create-scoped-role-member`</a>

##### <a name="Parametersdirectory.administrativeUnitsCreateScopedRoleMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--id**|string|Read-only.|id|id|
|**--microsoft-graph-scoped-role-membership-administrative-unit-id-administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|microsoft_graph_scoped_role_membership_administrative_unit_id_administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info**|object|identity|role_member_info|roleMemberInfo|

#### <a name="directory.administrativeUnitsDeleteExtensions">Command `az identitydirmgt directory-administrative-unit delete-extension`</a>

##### <a name="Parametersdirectory.administrativeUnitsDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="directory.administrativeUnitsDeleteScopedRoleMembers">Command `az identitydirmgt directory-administrative-unit delete-scoped-role-member`</a>

##### <a name="Parametersdirectory.administrativeUnitsDeleteScopedRoleMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="directory.administrativeUnitsdelta">Command `az identitydirmgt directory-administrative-unit delta`</a>

##### <a name="Parametersdirectory.administrativeUnitsdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="directory.administrativeUnitsListExtensions">Command `az identitydirmgt directory-administrative-unit list-extension`</a>

##### <a name="Parametersdirectory.administrativeUnitsListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directory.administrativeUnitsListMembers">Command `az identitydirmgt directory-administrative-unit list-member`</a>

##### <a name="Parametersdirectory.administrativeUnitsListMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directory.administrativeUnitsListRefMembers">Command `az identitydirmgt directory-administrative-unit list-ref-member`</a>

##### <a name="Parametersdirectory.administrativeUnitsListRefMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="directory.administrativeUnitsListScopedRoleMembers">Command `az identitydirmgt directory-administrative-unit list-scoped-role-member`</a>

##### <a name="Parametersdirectory.administrativeUnitsListScopedRoleMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directory.administrativeUnitsGetExtensions">Command `az identitydirmgt directory-administrative-unit show-extension`</a>

##### <a name="Parametersdirectory.administrativeUnitsGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directory.administrativeUnitsGetScopedRoleMembers">Command `az identitydirmgt directory-administrative-unit show-scoped-role-member`</a>

##### <a name="Parametersdirectory.administrativeUnitsGetScopedRoleMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directory.administrativeUnitsUpdateExtensions">Command `az identitydirmgt directory-administrative-unit update-extension`</a>

##### <a name="Parametersdirectory.administrativeUnitsUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="directory.administrativeUnitsUpdateScopedRoleMembers">Command `az identitydirmgt directory-administrative-unit update-scoped-role-member`</a>

##### <a name="Parametersdirectory.administrativeUnitsUpdateScopedRoleMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--administrative-unit-id**|string|key: id of administrativeUnit|administrative_unit_id|administrativeUnit-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--id**|string|Read-only.|id|id|
|**--microsoft-graph-scoped-role-membership-administrative-unit-id-administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|microsoft_graph_scoped_role_membership_administrative_unit_id_administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info**|object|identity|role_member_info|roleMemberInfo|

### group `az identitydirmgt directory-directory`
#### <a name="directory.directoryGetDirectory">Command `az identitydirmgt directory-directory show-directory`</a>

##### <a name="Parametersdirectory.directoryGetDirectory">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directory.directoryUpdateDirectory">Command `az identitydirmgt directory-directory update-directory`</a>

##### <a name="Parametersdirectory.directoryUpdateDirectory">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--administrative-units**|array||administrative_units|administrativeUnits|
|**--deleted-items**|array|Recently deleted items. Read-only. Nullable.|deleted_items|deletedItems|

### group `az identitydirmgt directory-role`
#### <a name="directoryRolescheckMemberGroups">Command `az identitydirmgt directory-role check-member-group`</a>

##### <a name="ParametersdirectoryRolescheckMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--group-ids**|array||group_ids|groupIds|

#### <a name="directoryRolescheckMemberObjects">Command `az identitydirmgt directory-role check-member-object`</a>

##### <a name="ParametersdirectoryRolescheckMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--ids**|array||ids|ids|

#### <a name="directoryRolesCreateRefMembers">Command `az identitydirmgt directory-role create-ref-member`</a>

##### <a name="ParametersdirectoryRolesCreateRefMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="directoryRolesCreateScopedMembers">Command `az identitydirmgt directory-role create-scoped-member`</a>

##### <a name="ParametersdirectoryRolesCreateScopedMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--id**|string|Read-only.|id|id|
|**--administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info**|object|identity|role_member_info|roleMemberInfo|

#### <a name="directoryRolesDeleteScopedMembers">Command `az identitydirmgt directory-role delete-scoped-member`</a>

##### <a name="ParametersdirectoryRolesDeleteScopedMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="directoryRolesdelta">Command `az identitydirmgt directory-role delta`</a>

##### <a name="ParametersdirectoryRolesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="directoryRolesgetAvailableExtensionProperties">Command `az identitydirmgt directory-role get-available-extension-property`</a>

##### <a name="ParametersdirectoryRolesgetAvailableExtensionProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

#### <a name="directoryRolesgetByIds">Command `az identitydirmgt directory-role get-by-id`</a>

##### <a name="ParametersdirectoryRolesgetByIds">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

#### <a name="directoryRolesgetMemberGroups">Command `az identitydirmgt directory-role get-member-group`</a>

##### <a name="ParametersdirectoryRolesgetMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="directoryRolesgetMemberObjects">Command `az identitydirmgt directory-role get-member-object`</a>

##### <a name="ParametersdirectoryRolesgetMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="directoryRolesListMembers">Command `az identitydirmgt directory-role list-member`</a>

##### <a name="ParametersdirectoryRolesListMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directoryRolesListRefMembers">Command `az identitydirmgt directory-role list-ref-member`</a>

##### <a name="ParametersdirectoryRolesListRefMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="directoryRolesListScopedMembers">Command `az identitydirmgt directory-role list-scoped-member`</a>

##### <a name="ParametersdirectoryRolesListScopedMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directoryRolesrestore">Command `az identitydirmgt directory-role restore`</a>

##### <a name="ParametersdirectoryRolesrestore">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|

#### <a name="directoryRolesGetScopedMembers">Command `az identitydirmgt directory-role show-scoped-member`</a>

##### <a name="ParametersdirectoryRolesGetScopedMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directoryRolesUpdateScopedMembers">Command `az identitydirmgt directory-role update-scoped-member`</a>

##### <a name="ParametersdirectoryRolesUpdateScopedMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--id**|string|Read-only.|id|id|
|**--administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info**|object|identity|role_member_info|roleMemberInfo|

#### <a name="directoryRolesvalidateProperties">Command `az identitydirmgt directory-role validate-property`</a>

##### <a name="ParametersdirectoryRolesvalidateProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--entity-type**|string||entity_type|entityType|
|**--display-name**|string||display_name|displayName|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-behalf-of-user-id**|uuid||on_behalf_of_user_id|onBehalfOfUserId|

### group `az identitydirmgt directory-role-directory-role`
#### <a name="directoryRoles.directoryRoleCreateDirectoryRole">Command `az identitydirmgt directory-role-directory-role create-directory-role`</a>

##### <a name="ParametersdirectoryRoles.directoryRoleCreateDirectoryRole">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|The description for the directory role. Read-only.|description|description|
|**--display-name**|string|The display name for the directory role. Read-only.|display_name|displayName|
|**--role-template-id**|string|The id of the directoryRoleTemplate that this role is based on. The property must be specified when activating a directory role in a tenant with a POST operation. After the directory role has been activated, the property is read only.|role_template_id|roleTemplateId|
|**--members**|array|Users that are members of this directory role. HTTP Methods: GET, POST, DELETE. Read-only. Nullable.|members|members|
|**--scoped-members**|array||scoped_members|scopedMembers|

#### <a name="directoryRoles.directoryRoleDeleteDirectoryRole">Command `az identitydirmgt directory-role-directory-role delete-directory-role`</a>

##### <a name="ParametersdirectoryRoles.directoryRoleDeleteDirectoryRole">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="directoryRoles.directoryRoleListDirectoryRole">Command `az identitydirmgt directory-role-directory-role list-directory-role`</a>

##### <a name="ParametersdirectoryRoles.directoryRoleListDirectoryRole">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directoryRoles.directoryRoleGetDirectoryRole">Command `az identitydirmgt directory-role-directory-role show-directory-role`</a>

##### <a name="ParametersdirectoryRoles.directoryRoleGetDirectoryRole">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directoryRoles.directoryRoleUpdateDirectoryRole">Command `az identitydirmgt directory-role-directory-role update-directory-role`</a>

##### <a name="ParametersdirectoryRoles.directoryRoleUpdateDirectoryRole">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-id**|string|key: id of directoryRole|directory_role_id|directoryRole-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|The description for the directory role. Read-only.|description|description|
|**--display-name**|string|The display name for the directory role. Read-only.|display_name|displayName|
|**--role-template-id**|string|The id of the directoryRoleTemplate that this role is based on. The property must be specified when activating a directory role in a tenant with a POST operation. After the directory role has been activated, the property is read only.|role_template_id|roleTemplateId|
|**--members**|array|Users that are members of this directory role. HTTP Methods: GET, POST, DELETE. Read-only. Nullable.|members|members|
|**--scoped-members**|array||scoped_members|scopedMembers|

### group `az identitydirmgt directory-role-template`
#### <a name="directoryRoleTemplatescheckMemberGroups">Command `az identitydirmgt directory-role-template check-member-group`</a>

##### <a name="ParametersdirectoryRoleTemplatescheckMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--group-ids**|array||group_ids|groupIds|

#### <a name="directoryRoleTemplatescheckMemberObjects">Command `az identitydirmgt directory-role-template check-member-object`</a>

##### <a name="ParametersdirectoryRoleTemplatescheckMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--ids**|array||ids|ids|

#### <a name="directoryRoleTemplatesgetAvailableExtensionProperties">Command `az identitydirmgt directory-role-template get-available-extension-property`</a>

##### <a name="ParametersdirectoryRoleTemplatesgetAvailableExtensionProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

#### <a name="directoryRoleTemplatesgetByIds">Command `az identitydirmgt directory-role-template get-by-id`</a>

##### <a name="ParametersdirectoryRoleTemplatesgetByIds">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

#### <a name="directoryRoleTemplatesgetMemberGroups">Command `az identitydirmgt directory-role-template get-member-group`</a>

##### <a name="ParametersdirectoryRoleTemplatesgetMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="directoryRoleTemplatesgetMemberObjects">Command `az identitydirmgt directory-role-template get-member-object`</a>

##### <a name="ParametersdirectoryRoleTemplatesgetMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="directoryRoleTemplatesrestore">Command `az identitydirmgt directory-role-template restore`</a>

##### <a name="ParametersdirectoryRoleTemplatesrestore">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|

#### <a name="directoryRoleTemplatesvalidateProperties">Command `az identitydirmgt directory-role-template validate-property`</a>

##### <a name="ParametersdirectoryRoleTemplatesvalidateProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--entity-type**|string||entity_type|entityType|
|**--display-name**|string||display_name|displayName|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-behalf-of-user-id**|uuid||on_behalf_of_user_id|onBehalfOfUserId|

### group `az identitydirmgt directory-role-template-directory-role-template`
#### <a name="directoryRoleTemplates.directoryRoleTemplateCreateDirectoryRoleTemplate">Command `az identitydirmgt directory-role-template-directory-role-template create-directory-role-template`</a>

##### <a name="ParametersdirectoryRoleTemplates.directoryRoleTemplateCreateDirectoryRoleTemplate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|The description to set for the directory role. Read-only.|description|description|
|**--display-name**|string|The display name to set for the directory role. Read-only.|display_name|displayName|

#### <a name="directoryRoleTemplates.directoryRoleTemplateDeleteDirectoryRoleTemplate">Command `az identitydirmgt directory-role-template-directory-role-template delete-directory-role-template`</a>

##### <a name="ParametersdirectoryRoleTemplates.directoryRoleTemplateDeleteDirectoryRoleTemplate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="directoryRoleTemplates.directoryRoleTemplateListDirectoryRoleTemplate">Command `az identitydirmgt directory-role-template-directory-role-template list-directory-role-template`</a>

##### <a name="ParametersdirectoryRoleTemplates.directoryRoleTemplateListDirectoryRoleTemplate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directoryRoleTemplates.directoryRoleTemplateGetDirectoryRoleTemplate">Command `az identitydirmgt directory-role-template-directory-role-template show-directory-role-template`</a>

##### <a name="ParametersdirectoryRoleTemplates.directoryRoleTemplateGetDirectoryRoleTemplate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="directoryRoleTemplates.directoryRoleTemplateUpdateDirectoryRoleTemplate">Command `az identitydirmgt directory-role-template-directory-role-template update-directory-role-template`</a>

##### <a name="ParametersdirectoryRoleTemplates.directoryRoleTemplateUpdateDirectoryRoleTemplate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--directory-role-template-id**|string|key: id of directoryRoleTemplate|directory_role_template_id|directoryRoleTemplate-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|The description to set for the directory role. Read-only.|description|description|
|**--display-name**|string|The display name to set for the directory role. Read-only.|display_name|displayName|

### group `az identitydirmgt domain`
#### <a name="domainsCreateRefDomainNameReferences">Command `az identitydirmgt domain create-ref-domain-name-reference`</a>

##### <a name="ParametersdomainsCreateRefDomainNameReferences">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="domainsCreateServiceConfigurationRecords">Command `az identitydirmgt domain create-service-configuration-record`</a>

##### <a name="ParametersdomainsCreateServiceConfigurationRecords">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--id**|string|Read-only.|id|id|
|**--is-optional**|boolean|If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.|is_optional|isOptional|
|**--label**|string|Value used when configuring the name of the DNS record at the DNS host.|label|label|
|**--record-type**|string|Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, TxtKey|record_type|recordType|
|**--supported-service**|string|Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune|supported_service|supportedService|
|**--ttl**|integer|Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable|ttl|ttl|

#### <a name="domainsCreateVerificationDnsRecords">Command `az identitydirmgt domain create-verification-dns-record`</a>

##### <a name="ParametersdomainsCreateVerificationDnsRecords">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--id**|string|Read-only.|id|id|
|**--is-optional**|boolean|If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.|is_optional|isOptional|
|**--label**|string|Value used when configuring the name of the DNS record at the DNS host.|label|label|
|**--record-type**|string|Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, TxtKey|record_type|recordType|
|**--supported-service**|string|Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune|supported_service|supportedService|
|**--ttl**|integer|Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable|ttl|ttl|

#### <a name="domainsDeleteServiceConfigurationRecords">Command `az identitydirmgt domain delete-service-configuration-record`</a>

##### <a name="ParametersdomainsDeleteServiceConfigurationRecords">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="domainsDeleteVerificationDnsRecords">Command `az identitydirmgt domain delete-verification-dns-record`</a>

##### <a name="ParametersdomainsDeleteVerificationDnsRecords">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="domainsforceDelete">Command `az identitydirmgt domain force-delete`</a>

##### <a name="ParametersdomainsforceDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--disable-user-accounts**|boolean||disable_user_accounts|disableUserAccounts|

#### <a name="domainsListDomainNameReferences">Command `az identitydirmgt domain list-domain-name-reference`</a>

##### <a name="ParametersdomainsListDomainNameReferences">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="domainsListRefDomainNameReferences">Command `az identitydirmgt domain list-ref-domain-name-reference`</a>

##### <a name="ParametersdomainsListRefDomainNameReferences">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="domainsListServiceConfigurationRecords">Command `az identitydirmgt domain list-service-configuration-record`</a>

##### <a name="ParametersdomainsListServiceConfigurationRecords">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="domainsListVerificationDnsRecords">Command `az identitydirmgt domain list-verification-dns-record`</a>

##### <a name="ParametersdomainsListVerificationDnsRecords">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="domainsGetServiceConfigurationRecords">Command `az identitydirmgt domain show-service-configuration-record`</a>

##### <a name="ParametersdomainsGetServiceConfigurationRecords">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="domainsGetVerificationDnsRecords">Command `az identitydirmgt domain show-verification-dns-record`</a>

##### <a name="ParametersdomainsGetVerificationDnsRecords">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="domainsUpdateServiceConfigurationRecords">Command `az identitydirmgt domain update-service-configuration-record`</a>

##### <a name="ParametersdomainsUpdateServiceConfigurationRecords">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--id**|string|Read-only.|id|id|
|**--is-optional**|boolean|If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.|is_optional|isOptional|
|**--label**|string|Value used when configuring the name of the DNS record at the DNS host.|label|label|
|**--record-type**|string|Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, TxtKey|record_type|recordType|
|**--supported-service**|string|Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune|supported_service|supportedService|
|**--ttl**|integer|Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable|ttl|ttl|

#### <a name="domainsUpdateVerificationDnsRecords">Command `az identitydirmgt domain update-verification-dns-record`</a>

##### <a name="ParametersdomainsUpdateVerificationDnsRecords">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--domain-dns-record-id**|string|key: id of domainDnsRecord|domain_dns_record_id|domainDnsRecord-id|
|**--id**|string|Read-only.|id|id|
|**--is-optional**|boolean|If false, this record must be configured by the customer at the DNS host for Microsoft Online Services to operate correctly with the domain.|is_optional|isOptional|
|**--label**|string|Value used when configuring the name of the DNS record at the DNS host.|label|label|
|**--record-type**|string|Indicates what type of DNS record this entity represents.The value can be one of the following: CName, Mx, Srv, TxtKey|record_type|recordType|
|**--supported-service**|string|Microsoft Online Service or feature that has a dependency on this DNS record.Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune|supported_service|supportedService|
|**--ttl**|integer|Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable|ttl|ttl|

#### <a name="domainsverify">Command `az identitydirmgt domain verify`</a>

##### <a name="Parametersdomainsverify">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|

### group `az identitydirmgt domain-domain`
#### <a name="domains.domainCreateDomain">Command `az identitydirmgt domain-domain create-domain`</a>

##### <a name="Parametersdomains.domainCreateDomain">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--authentication-type**|string|Indicates the configured authentication type for the domain. The value is either Managed or Federated. Managed indicates a cloud managed domain where Azure AD performs user authentication.Federated indicates authentication is federated with an identity provider such as the tenant's on-premises Active Directory via Active Directory Federation Services. This property is read-only and is not nullable.|authentication_type|authenticationType|
|**--availability-status**|string|This property is always null except when the verify action is used. When the verify action is used, a domain entity is returned in the response. The availabilityStatus property of the domain entity in the response is either AvailableImmediately or EmailVerifiedDomainTakeoverScheduled.|availability_status|availabilityStatus|
|**--is-admin-managed**|boolean|The value of the property is false if the DNS record management of the domain has been delegated to Microsoft 365. Otherwise, the value is true. Not nullable|is_admin_managed|isAdminManaged|
|**--is-default**|boolean|True if this is the default domain that is used for user creation. There is only one default domain per company. Not nullable|is_default|isDefault|
|**--is-initial**|boolean|True if this is the initial domain created by Microsoft Online Services (companyname.onmicrosoft.com). There is only one initial domain per company. Not nullable|is_initial|isInitial|
|**--is-root**|boolean|True if the domain is a verified root domain. Otherwise, false if the domain is a subdomain or unverified. Not nullable|is_root|isRoot|
|**--is-verified**|boolean|True if the domain has completed domain ownership verification. Not nullable|is_verified|isVerified|
|**--manufacturer**|string||manufacturer|manufacturer|
|**--model**|string||model|model|
|**--password-notification-window-in-days**|integer|Specifies the number of days before a user receives notification that their password will expire. If the property is not set, a default value of 14 days will be used.|password_notification_window_in_days|passwordNotificationWindowInDays|
|**--password-validity-period-in-days**|integer|Specifies the length of time that a password is valid before it must be changed. If the property is not set, a default value of 90 days will be used.|password_validity_period_in_days|passwordValidityPeriodInDays|
|**--state**|object|domainState|state|state|
|**--supported-services**|array|The capabilities assigned to the domain.Can include 0, 1 or more of following values: Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune The values which you can add/remove using Graph API include: Email, OfficeCommunicationsOnline, YammerNot nullable|supported_services|supportedServices|
|**--domain-name-references**|array|Read-only, Nullable|domain_name_references|domainNameReferences|
|**--service-configuration-records**|array|DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services.Read-only, Nullable|service_configuration_records|serviceConfigurationRecords|
|**--verification-dns-records**|array|DNS records that the customer adds to the DNS zone file of the domain before the customer can complete domain ownership verification with Azure AD.Read-only, Nullable|verification_dns_records|verificationDnsRecords|

#### <a name="domains.domainDeleteDomain">Command `az identitydirmgt domain-domain delete-domain`</a>

##### <a name="Parametersdomains.domainDeleteDomain">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="domains.domainListDomain">Command `az identitydirmgt domain-domain list-domain`</a>

##### <a name="Parametersdomains.domainListDomain">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="domains.domainGetDomain">Command `az identitydirmgt domain-domain show-domain`</a>

##### <a name="Parametersdomains.domainGetDomain">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="domains.domainUpdateDomain">Command `az identitydirmgt domain-domain update-domain`</a>

##### <a name="Parametersdomains.domainUpdateDomain">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--domain-id**|string|key: id of domain|domain_id|domain-id|
|**--id**|string|Read-only.|id|id|
|**--authentication-type**|string|Indicates the configured authentication type for the domain. The value is either Managed or Federated. Managed indicates a cloud managed domain where Azure AD performs user authentication.Federated indicates authentication is federated with an identity provider such as the tenant's on-premises Active Directory via Active Directory Federation Services. This property is read-only and is not nullable.|authentication_type|authenticationType|
|**--availability-status**|string|This property is always null except when the verify action is used. When the verify action is used, a domain entity is returned in the response. The availabilityStatus property of the domain entity in the response is either AvailableImmediately or EmailVerifiedDomainTakeoverScheduled.|availability_status|availabilityStatus|
|**--is-admin-managed**|boolean|The value of the property is false if the DNS record management of the domain has been delegated to Microsoft 365. Otherwise, the value is true. Not nullable|is_admin_managed|isAdminManaged|
|**--is-default**|boolean|True if this is the default domain that is used for user creation. There is only one default domain per company. Not nullable|is_default|isDefault|
|**--is-initial**|boolean|True if this is the initial domain created by Microsoft Online Services (companyname.onmicrosoft.com). There is only one initial domain per company. Not nullable|is_initial|isInitial|
|**--is-root**|boolean|True if the domain is a verified root domain. Otherwise, false if the domain is a subdomain or unverified. Not nullable|is_root|isRoot|
|**--is-verified**|boolean|True if the domain has completed domain ownership verification. Not nullable|is_verified|isVerified|
|**--manufacturer**|string||manufacturer|manufacturer|
|**--model**|string||model|model|
|**--password-notification-window-in-days**|integer|Specifies the number of days before a user receives notification that their password will expire. If the property is not set, a default value of 14 days will be used.|password_notification_window_in_days|passwordNotificationWindowInDays|
|**--password-validity-period-in-days**|integer|Specifies the length of time that a password is valid before it must be changed. If the property is not set, a default value of 90 days will be used.|password_validity_period_in_days|passwordValidityPeriodInDays|
|**--state**|object|domainState|state|state|
|**--supported-services**|array|The capabilities assigned to the domain.Can include 0, 1 or more of following values: Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune The values which you can add/remove using Graph API include: Email, OfficeCommunicationsOnline, YammerNot nullable|supported_services|supportedServices|
|**--domain-name-references**|array|Read-only, Nullable|domain_name_references|domainNameReferences|
|**--service-configuration-records**|array|DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services.Read-only, Nullable|service_configuration_records|serviceConfigurationRecords|
|**--verification-dns-records**|array|DNS records that the customer adds to the DNS zone file of the domain before the customer can complete domain ownership verification with Azure AD.Read-only, Nullable|verification_dns_records|verificationDnsRecords|

### group `az identitydirmgt organization`
#### <a name="organizationcheckMemberGroups">Command `az identitydirmgt organization check-member-group`</a>

##### <a name="ParametersorganizationcheckMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--group-ids**|array||group_ids|groupIds|

#### <a name="organizationcheckMemberObjects">Command `az identitydirmgt organization check-member-object`</a>

##### <a name="ParametersorganizationcheckMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--ids**|array||ids|ids|

#### <a name="organizationCreateExtensions">Command `az identitydirmgt organization create-extension`</a>

##### <a name="ParametersorganizationCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--id**|string|Read-only.|id|id|

#### <a name="organizationDeleteExtensions">Command `az identitydirmgt organization delete-extension`</a>

##### <a name="ParametersorganizationDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="organizationgetAvailableExtensionProperties">Command `az identitydirmgt organization get-available-extension-property`</a>

##### <a name="ParametersorganizationgetAvailableExtensionProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

#### <a name="organizationgetByIds">Command `az identitydirmgt organization get-by-id`</a>

##### <a name="ParametersorganizationgetByIds">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

#### <a name="organizationgetMemberGroups">Command `az identitydirmgt organization get-member-group`</a>

##### <a name="ParametersorganizationgetMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="organizationgetMemberObjects">Command `az identitydirmgt organization get-member-object`</a>

##### <a name="ParametersorganizationgetMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="organizationListExtensions">Command `az identitydirmgt organization list-extension`</a>

##### <a name="ParametersorganizationListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="organizationrestore">Command `az identitydirmgt organization restore`</a>

##### <a name="Parametersorganizationrestore">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|

#### <a name="organizationsetMobileDeviceManagementAuthority">Command `az identitydirmgt organization set-mobile-device-management-authority`</a>

##### <a name="ParametersorganizationsetMobileDeviceManagementAuthority">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|

#### <a name="organizationGetExtensions">Command `az identitydirmgt organization show-extension`</a>

##### <a name="ParametersorganizationGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="organizationUpdateExtensions">Command `az identitydirmgt organization update-extension`</a>

##### <a name="ParametersorganizationUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="organizationvalidateProperties">Command `az identitydirmgt organization validate-property`</a>

##### <a name="ParametersorganizationvalidateProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--entity-type**|string||entity_type|entityType|
|**--display-name**|string||display_name|displayName|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-behalf-of-user-id**|uuid||on_behalf_of_user_id|onBehalfOfUserId|

### group `az identitydirmgt organization-organization`
#### <a name="organization.organizationCreateOrganization">Command `az identitydirmgt organization-organization create-organization`</a>

##### <a name="Parametersorganization.organizationCreateOrganization">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--assigned-plans**|array|The collection of service plans associated with the tenant. Not nullable.|assigned_plans|assignedPlans|
|**--business-phones**|array|Telephone number for the organization. NOTE: Although this is a string collection, only one number can be set for this property.|business_phones|businessPhones|
|**--city**|string|City name of the address for the organization.|city|city|
|**--country**|string|Country/region name of the address for the organization.|country|country|
|**--country-letter-code**|string|Country/region abbreviation for the organization.|country_letter_code|countryLetterCode|
|**--created-date-time**|date-time|Timestamp of when the organization was created. The value cannot be modified and is automatically populated when the organization is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The display name for the tenant.|display_name|displayName|
|**--marketing-notification-emails**|array|Not nullable.|marketing_notification_emails|marketingNotificationEmails|
|**--on-premises-last-sync-date-time**|date-time|The time and date at which the tenant was last synced with the on-premise directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-sync-enabled**|boolean|true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default).|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--postal-code**|string|Postal code of the address for the organization.|postal_code|postalCode|
|**--preferred-language**|string|The preferred language for the organization. Should follow ISO 639-1 Code; for example 'en'.|preferred_language|preferredLanguage|
|**--privacy-profile**|object|privacyProfile|privacy_profile|privacyProfile|
|**--provisioned-plans**|array|Not nullable.|provisioned_plans|provisionedPlans|
|**--security-compliance-notification-mails**|array||security_compliance_notification_mails|securityComplianceNotificationMails|
|**--security-compliance-notification-phones**|array||security_compliance_notification_phones|securityComplianceNotificationPhones|
|**--state**|string|State name of the address for the organization.|state|state|
|**--street**|string|Street name of the address for organization.|street|street|
|**--technical-notification-mails**|array|Not nullable.|technical_notification_mails|technicalNotificationMails|
|**--tenant-type**|string||tenant_type|tenantType|
|**--verified-domains**|array|The collection of domains associated with this tenant. Not nullable.|verified_domains|verifiedDomains|
|**--mobile-device-management-authority**|choice||mobile_device_management_authority|mobileDeviceManagementAuthority|
|**--certificate-based-auth-configuration**|array|Navigation property to manage certificate-based authentication configuration. Only a single instance of certificateBasedAuthConfiguration can be created in the collection.|certificate_based_auth_configuration|certificateBasedAuthConfiguration|
|**--extensions**|array|The collection of open extensions defined for the organization. Read-only. Nullable.|extensions|extensions|

#### <a name="organization.organizationDeleteOrganization">Command `az identitydirmgt organization-organization delete-organization`</a>

##### <a name="Parametersorganization.organizationDeleteOrganization">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="organization.organizationListOrganization">Command `az identitydirmgt organization-organization list-organization`</a>

##### <a name="Parametersorganization.organizationListOrganization">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="organization.organizationGetOrganization">Command `az identitydirmgt organization-organization show-organization`</a>

##### <a name="Parametersorganization.organizationGetOrganization">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="organization.organizationUpdateOrganization">Command `az identitydirmgt organization-organization update-organization`</a>

##### <a name="Parametersorganization.organizationUpdateOrganization">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--assigned-plans**|array|The collection of service plans associated with the tenant. Not nullable.|assigned_plans|assignedPlans|
|**--business-phones**|array|Telephone number for the organization. NOTE: Although this is a string collection, only one number can be set for this property.|business_phones|businessPhones|
|**--city**|string|City name of the address for the organization.|city|city|
|**--country**|string|Country/region name of the address for the organization.|country|country|
|**--country-letter-code**|string|Country/region abbreviation for the organization.|country_letter_code|countryLetterCode|
|**--created-date-time**|date-time|Timestamp of when the organization was created. The value cannot be modified and is automatically populated when the organization is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|The display name for the tenant.|display_name|displayName|
|**--marketing-notification-emails**|array|Not nullable.|marketing_notification_emails|marketingNotificationEmails|
|**--on-premises-last-sync-date-time**|date-time|The time and date at which the tenant was last synced with the on-premise directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-sync-enabled**|boolean|true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default).|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--postal-code**|string|Postal code of the address for the organization.|postal_code|postalCode|
|**--preferred-language**|string|The preferred language for the organization. Should follow ISO 639-1 Code; for example 'en'.|preferred_language|preferredLanguage|
|**--privacy-profile**|object|privacyProfile|privacy_profile|privacyProfile|
|**--provisioned-plans**|array|Not nullable.|provisioned_plans|provisionedPlans|
|**--security-compliance-notification-mails**|array||security_compliance_notification_mails|securityComplianceNotificationMails|
|**--security-compliance-notification-phones**|array||security_compliance_notification_phones|securityComplianceNotificationPhones|
|**--state**|string|State name of the address for the organization.|state|state|
|**--street**|string|Street name of the address for organization.|street|street|
|**--technical-notification-mails**|array|Not nullable.|technical_notification_mails|technicalNotificationMails|
|**--tenant-type**|string||tenant_type|tenantType|
|**--verified-domains**|array|The collection of domains associated with this tenant. Not nullable.|verified_domains|verifiedDomains|
|**--mobile-device-management-authority**|choice||mobile_device_management_authority|mobileDeviceManagementAuthority|
|**--certificate-based-auth-configuration**|array|Navigation property to manage certificate-based authentication configuration. Only a single instance of certificateBasedAuthConfiguration can be created in the collection.|certificate_based_auth_configuration|certificateBasedAuthConfiguration|
|**--extensions**|array|The collection of open extensions defined for the organization. Read-only. Nullable.|extensions|extensions|

### group `az identitydirmgt subscribed-sku-subscribed-sku`
#### <a name="subscribedSkus.subscribedSkuCreateSubscribedSku">Command `az identitydirmgt subscribed-sku-subscribed-sku create-subscribed-sku`</a>

##### <a name="ParameterssubscribedSkus.subscribedSkuCreateSubscribedSku">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--applies-to**|string|For example, 'User' or 'Company'.|applies_to|appliesTo|
|**--capability-status**|string|Possible values are: Enabled, Warning, Suspended, Deleted, LockedOut.|capability_status|capabilityStatus|
|**--consumed-units**|integer|The number of licenses that have been assigned.|consumed_units|consumedUnits|
|**--prepaid-units**|object|licenseUnitsDetail|prepaid_units|prepaidUnits|
|**--service-plans**|array|Information about the service plans that are available with the SKU. Not nullable|service_plans|servicePlans|
|**--sku-id**|uuid|The unique identifier (GUID) for the service SKU.|sku_id|skuId|
|**--sku-part-number**|string|The SKU part number; for example: 'AAD_PREMIUM' or 'RMSBASIC'. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.|sku_part_number|skuPartNumber|

#### <a name="subscribedSkus.subscribedSkuDeleteSubscribedSku">Command `az identitydirmgt subscribed-sku-subscribed-sku delete-subscribed-sku`</a>

##### <a name="ParameterssubscribedSkus.subscribedSkuDeleteSubscribedSku">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscribed-sku-id**|string|key: id of subscribedSku|subscribed_sku_id|subscribedSku-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="subscribedSkus.subscribedSkuListSubscribedSku">Command `az identitydirmgt subscribed-sku-subscribed-sku list-subscribed-sku`</a>

##### <a name="ParameterssubscribedSkus.subscribedSkuListSubscribedSku">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="subscribedSkus.subscribedSkuGetSubscribedSku">Command `az identitydirmgt subscribed-sku-subscribed-sku show-subscribed-sku`</a>

##### <a name="ParameterssubscribedSkus.subscribedSkuGetSubscribedSku">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscribed-sku-id**|string|key: id of subscribedSku|subscribed_sku_id|subscribedSku-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="subscribedSkus.subscribedSkuUpdateSubscribedSku">Command `az identitydirmgt subscribed-sku-subscribed-sku update-subscribed-sku`</a>

##### <a name="ParameterssubscribedSkus.subscribedSkuUpdateSubscribedSku">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--subscribed-sku-id**|string|key: id of subscribedSku|subscribed_sku_id|subscribedSku-id|
|**--id**|string|Read-only.|id|id|
|**--applies-to**|string|For example, 'User' or 'Company'.|applies_to|appliesTo|
|**--capability-status**|string|Possible values are: Enabled, Warning, Suspended, Deleted, LockedOut.|capability_status|capabilityStatus|
|**--consumed-units**|integer|The number of licenses that have been assigned.|consumed_units|consumedUnits|
|**--prepaid-units**|object|licenseUnitsDetail|prepaid_units|prepaidUnits|
|**--service-plans**|array|Information about the service plans that are available with the SKU. Not nullable|service_plans|servicePlans|
|**--sku-id**|uuid|The unique identifier (GUID) for the service SKU.|sku_id|skuId|
|**--sku-part-number**|string|The SKU part number; for example: 'AAD_PREMIUM' or 'RMSBASIC'. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.|sku_part_number|skuPartNumber|

### group `az identitydirmgt user`
#### <a name="usersCreateScopedRoleMemberOf">Command `az identitydirmgt user create-scoped-role-member-of`</a>

##### <a name="ParametersusersCreateScopedRoleMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info**|object|identity|role_member_info|roleMemberInfo|

#### <a name="usersDeleteScopedRoleMemberOf">Command `az identitydirmgt user delete-scoped-role-member-of`</a>

##### <a name="ParametersusersDeleteScopedRoleMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersListScopedRoleMemberOf">Command `az identitydirmgt user list-scoped-role-member-of`</a>

##### <a name="ParametersusersListScopedRoleMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetScopedRoleMemberOf">Command `az identitydirmgt user show-scoped-role-member-of`</a>

##### <a name="ParametersusersGetScopedRoleMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateScopedRoleMemberOf">Command `az identitydirmgt user update-scoped-role-member-of`</a>

##### <a name="ParametersusersUpdateScopedRoleMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--scoped-role-membership-id**|string|key: id of scopedRoleMembership|scoped_role_membership_id|scopedRoleMembership-id|
|**--id**|string|Read-only.|id|id|
|**--administrative-unit-id**|string|Unique identifier for the administrative unit that the directory role is scoped to|administrative_unit_id|administrativeUnitId|
|**--role-id**|string|Unique identifier for the directory role that the member is in.|role_id|roleId|
|**--role-member-info**|object|identity|role_member_info|roleMemberInfo|
