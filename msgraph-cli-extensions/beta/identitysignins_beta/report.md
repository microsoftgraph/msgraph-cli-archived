# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az identitysignins_beta|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az identitysignins_beta` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az identitysignins datapolicyoperationsdatapolicyoperation|dataPolicyOperations.dataPolicyOperation|[commands](#CommandsIndataPolicyOperations.dataPolicyOperation)|
|az identitysignins identity|identity|[commands](#CommandsInidentity)|
|az identitysignins identityconditionalaccess|identity.conditionalAccess|[commands](#CommandsInidentity.conditionalAccess)|
|az identitysignins identityprovidersidentityprovider|identityProviders.identityProvider|[commands](#CommandsInidentityProviders.identityProvider)|
|az identitysignins identityprovider|identityProviders|[commands](#CommandsInidentityProviders)|
|az identitysignins informationprotection|informationProtection.informationProtection|[commands](#CommandsIninformationProtection.informationProtection)|
|az identitysignins informationprotection|informationProtection|[commands](#CommandsIninformationProtection)|
|az identitysignins informationprotectiondatalosspreventionpolicy|informationProtection.dataLossPreventionPolicies|[commands](#CommandsIninformationProtection.dataLossPreventionPolicies)|
|az identitysignins informationprotectionpolicy|informationProtection.policy|[commands](#CommandsIninformationProtection.policy)|
|az identitysignins informationprotectionpolicylabel|informationProtection.policy.labels|[commands](#CommandsIninformationProtection.policy.labels)|
|az identitysignins informationprotectionsensitivitylabel|informationProtection.sensitivityLabels|[commands](#CommandsIninformationProtection.sensitivityLabels)|
|az identitysignins informationprotectionsensitivitylabelssublabel|informationProtection.sensitivityLabels.sublabels|[commands](#CommandsIninformationProtection.sensitivityLabels.sublabels)|
|az identitysignins informationprotectionthreatassessmentrequest|informationProtection.threatAssessmentRequests|[commands](#CommandsIninformationProtection.threatAssessmentRequests)|
|az identitysignins invitationsinvitation|invitations.invitation|[commands](#CommandsIninvitations.invitation)|
|az identitysignins invitation|invitations|[commands](#CommandsIninvitations)|
|az identitysignins oauth2permissiongrantsoauth2permissiongrant|oauth2PermissionGrants.oAuth2PermissionGrant|[commands](#CommandsInoauth2PermissionGrants.oAuth2PermissionGrant)|
|az identitysignins oauth2permissiongrant|oauth2PermissionGrants|[commands](#CommandsInoauth2PermissionGrants)|
|az identitysignins organization|organization|[commands](#CommandsInorganization)|
|az identitysignins policiespolicyroot|policies.policyRoot|[commands](#CommandsInpolicies.policyRoot)|
|az identitysignins policy|policies|[commands](#CommandsInpolicies)|
|az identitysignins policiespermissiongrantpolicy|policies.permissionGrantPolicies|[commands](#CommandsInpolicies.permissionGrantPolicies)|
|az identitysignins riskdetectionsriskdetection|riskDetections.riskDetection|[commands](#CommandsInriskDetections.riskDetection)|
|az identitysignins riskyusersriskyuser|riskyUsers.riskyUser|[commands](#CommandsInriskyUsers.riskyUser)|
|az identitysignins riskyuser|riskyUsers|[commands](#CommandsInriskyUsers)|
|az identitysignins trustframework|trustFramework.trustFramework|[commands](#CommandsIntrustFramework.trustFramework)|
|az identitysignins trustframework|trustFramework|[commands](#CommandsIntrustFramework)|
|az identitysignins trustframeworkkeyset|trustFramework.keySets|[commands](#CommandsIntrustFramework.keySets)|
|az identitysignins user|users|[commands](#CommandsInusers)|
|az identitysignins usersauthentication|users.authentication|[commands](#CommandsInusers.authentication)|

## COMMANDS
### <a name="CommandsIndataPolicyOperations.dataPolicyOperation">Commands in `az identitysignins datapolicyoperationsdatapolicyoperation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins datapolicyoperationsdatapolicyoperation create-data-policy-operation](#dataPolicyOperations.dataPolicyOperationCreateDataPolicyOperation)|CreateDataPolicyOperation|[Parameters](#ParametersdataPolicyOperations.dataPolicyOperationCreateDataPolicyOperation)|Not Found|
|[az identitysignins datapolicyoperationsdatapolicyoperation delete-data-policy-operation](#dataPolicyOperations.dataPolicyOperationDeleteDataPolicyOperation)|DeleteDataPolicyOperation|[Parameters](#ParametersdataPolicyOperations.dataPolicyOperationDeleteDataPolicyOperation)|Not Found|
|[az identitysignins datapolicyoperationsdatapolicyoperation list-data-policy-operation](#dataPolicyOperations.dataPolicyOperationListDataPolicyOperation)|ListDataPolicyOperation|[Parameters](#ParametersdataPolicyOperations.dataPolicyOperationListDataPolicyOperation)|Not Found|
|[az identitysignins datapolicyoperationsdatapolicyoperation show-data-policy-operation](#dataPolicyOperations.dataPolicyOperationGetDataPolicyOperation)|GetDataPolicyOperation|[Parameters](#ParametersdataPolicyOperations.dataPolicyOperationGetDataPolicyOperation)|Not Found|
|[az identitysignins datapolicyoperationsdatapolicyoperation update-data-policy-operation](#dataPolicyOperations.dataPolicyOperationUpdateDataPolicyOperation)|UpdateDataPolicyOperation|[Parameters](#ParametersdataPolicyOperations.dataPolicyOperationUpdateDataPolicyOperation)|Not Found|

### <a name="CommandsInidentity">Commands in `az identitysignins identity` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins identity create-user-flow](#identityCreateUserFlows)|CreateUserFlows|[Parameters](#ParametersidentityCreateUserFlows)|Not Found|
|[az identitysignins identity delete-conditional-access](#identityDeleteConditionalAccess)|DeleteConditionalAccess|[Parameters](#ParametersidentityDeleteConditionalAccess)|Not Found|
|[az identitysignins identity delete-user-flow](#identityDeleteUserFlows)|DeleteUserFlows|[Parameters](#ParametersidentityDeleteUserFlows)|Not Found|
|[az identitysignins identity list-user-flow](#identityListUserFlows)|ListUserFlows|[Parameters](#ParametersidentityListUserFlows)|Not Found|
|[az identitysignins identity show-conditional-access](#identityGetConditionalAccess)|GetConditionalAccess|[Parameters](#ParametersidentityGetConditionalAccess)|Not Found|
|[az identitysignins identity show-user-flow](#identityGetUserFlows)|GetUserFlows|[Parameters](#ParametersidentityGetUserFlows)|Not Found|
|[az identitysignins identity update-conditional-access](#identityUpdateConditionalAccess)|UpdateConditionalAccess|[Parameters](#ParametersidentityUpdateConditionalAccess)|Not Found|
|[az identitysignins identity update-user-flow](#identityUpdateUserFlows)|UpdateUserFlows|[Parameters](#ParametersidentityUpdateUserFlows)|Not Found|

### <a name="CommandsInidentity.conditionalAccess">Commands in `az identitysignins identityconditionalaccess` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins identityconditionalaccess create-named-location](#identity.conditionalAccessCreateNamedLocations)|CreateNamedLocations|[Parameters](#Parametersidentity.conditionalAccessCreateNamedLocations)|Not Found|
|[az identitysignins identityconditionalaccess create-policy](#identity.conditionalAccessCreatePolicies)|CreatePolicies|[Parameters](#Parametersidentity.conditionalAccessCreatePolicies)|Not Found|
|[az identitysignins identityconditionalaccess delete-named-location](#identity.conditionalAccessDeleteNamedLocations)|DeleteNamedLocations|[Parameters](#Parametersidentity.conditionalAccessDeleteNamedLocations)|Not Found|
|[az identitysignins identityconditionalaccess delete-policy](#identity.conditionalAccessDeletePolicies)|DeletePolicies|[Parameters](#Parametersidentity.conditionalAccessDeletePolicies)|Not Found|
|[az identitysignins identityconditionalaccess list-named-location](#identity.conditionalAccessListNamedLocations)|ListNamedLocations|[Parameters](#Parametersidentity.conditionalAccessListNamedLocations)|Not Found|
|[az identitysignins identityconditionalaccess list-policy](#identity.conditionalAccessListPolicies)|ListPolicies|[Parameters](#Parametersidentity.conditionalAccessListPolicies)|Not Found|
|[az identitysignins identityconditionalaccess show-named-location](#identity.conditionalAccessGetNamedLocations)|GetNamedLocations|[Parameters](#Parametersidentity.conditionalAccessGetNamedLocations)|Not Found|
|[az identitysignins identityconditionalaccess show-policy](#identity.conditionalAccessGetPolicies)|GetPolicies|[Parameters](#Parametersidentity.conditionalAccessGetPolicies)|Not Found|
|[az identitysignins identityconditionalaccess update-named-location](#identity.conditionalAccessUpdateNamedLocations)|UpdateNamedLocations|[Parameters](#Parametersidentity.conditionalAccessUpdateNamedLocations)|Not Found|
|[az identitysignins identityconditionalaccess update-policy](#identity.conditionalAccessUpdatePolicies)|UpdatePolicies|[Parameters](#Parametersidentity.conditionalAccessUpdatePolicies)|Not Found|

### <a name="CommandsInidentityProviders">Commands in `az identitysignins identityprovider` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins identityprovider available-provider-type](#identityProvidersavailableProviderTypes)|availableProviderTypes|[Parameters](#ParametersidentityProvidersavailableProviderTypes)|Not Found|

### <a name="CommandsInidentityProviders.identityProvider">Commands in `az identitysignins identityprovidersidentityprovider` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins identityprovidersidentityprovider create-identity-provider](#identityProviders.identityProviderCreateIdentityProvider)|CreateIdentityProvider|[Parameters](#ParametersidentityProviders.identityProviderCreateIdentityProvider)|Not Found|
|[az identitysignins identityprovidersidentityprovider delete-identity-provider](#identityProviders.identityProviderDeleteIdentityProvider)|DeleteIdentityProvider|[Parameters](#ParametersidentityProviders.identityProviderDeleteIdentityProvider)|Not Found|
|[az identitysignins identityprovidersidentityprovider list-identity-provider](#identityProviders.identityProviderListIdentityProvider)|ListIdentityProvider|[Parameters](#ParametersidentityProviders.identityProviderListIdentityProvider)|Not Found|
|[az identitysignins identityprovidersidentityprovider show-identity-provider](#identityProviders.identityProviderGetIdentityProvider)|GetIdentityProvider|[Parameters](#ParametersidentityProviders.identityProviderGetIdentityProvider)|Not Found|
|[az identitysignins identityprovidersidentityprovider update-identity-provider](#identityProviders.identityProviderUpdateIdentityProvider)|UpdateIdentityProvider|[Parameters](#ParametersidentityProviders.identityProviderUpdateIdentityProvider)|Not Found|

### <a name="CommandsIninformationProtection.informationProtection">Commands in `az identitysignins informationprotection` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins informationprotection show-information-protection](#informationProtection.informationProtectionGetInformationProtection)|GetInformationProtection|[Parameters](#ParametersinformationProtection.informationProtectionGetInformationProtection)|Not Found|
|[az identitysignins informationprotection update-information-protection](#informationProtection.informationProtectionUpdateInformationProtection)|UpdateInformationProtection|[Parameters](#ParametersinformationProtection.informationProtectionUpdateInformationProtection)|Not Found|

### <a name="CommandsIninformationProtection">Commands in `az identitysignins informationprotection` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins informationprotection create-data-loss-prevention-policy](#informationProtectionCreateDataLossPreventionPolicies)|CreateDataLossPreventionPolicies|[Parameters](#ParametersinformationProtectionCreateDataLossPreventionPolicies)|Not Found|
|[az identitysignins informationprotection create-sensitivity-label](#informationProtectionCreateSensitivityLabels)|CreateSensitivityLabels|[Parameters](#ParametersinformationProtectionCreateSensitivityLabels)|Not Found|
|[az identitysignins informationprotection create-threat-assessment-request](#informationProtectionCreateThreatAssessmentRequests)|CreateThreatAssessmentRequests|[Parameters](#ParametersinformationProtectionCreateThreatAssessmentRequests)|Not Found|
|[az identitysignins informationprotection delete-data-loss-prevention-policy](#informationProtectionDeleteDataLossPreventionPolicies)|DeleteDataLossPreventionPolicies|[Parameters](#ParametersinformationProtectionDeleteDataLossPreventionPolicies)|Not Found|
|[az identitysignins informationprotection delete-policy](#informationProtectionDeletePolicy)|DeletePolicy|[Parameters](#ParametersinformationProtectionDeletePolicy)|Not Found|
|[az identitysignins informationprotection delete-sensitivity-label](#informationProtectionDeleteSensitivityLabels)|DeleteSensitivityLabels|[Parameters](#ParametersinformationProtectionDeleteSensitivityLabels)|Not Found|
|[az identitysignins informationprotection delete-sensitivity-policy-setting](#informationProtectionDeleteSensitivityPolicySettings)|DeleteSensitivityPolicySettings|[Parameters](#ParametersinformationProtectionDeleteSensitivityPolicySettings)|Not Found|
|[az identitysignins informationprotection delete-threat-assessment-request](#informationProtectionDeleteThreatAssessmentRequests)|DeleteThreatAssessmentRequests|[Parameters](#ParametersinformationProtectionDeleteThreatAssessmentRequests)|Not Found|
|[az identitysignins informationprotection evaluate-label-and-policy](#informationProtectionevaluateLabelsAndPolicies)|evaluateLabelsAndPolicies|[Parameters](#ParametersinformationProtectionevaluateLabelsAndPolicies)|Not Found|
|[az identitysignins informationprotection list-data-loss-prevention-policy](#informationProtectionListDataLossPreventionPolicies)|ListDataLossPreventionPolicies|[Parameters](#ParametersinformationProtectionListDataLossPreventionPolicies)|Not Found|
|[az identitysignins informationprotection list-sensitivity-label](#informationProtectionListSensitivityLabels)|ListSensitivityLabels|[Parameters](#ParametersinformationProtectionListSensitivityLabels)|Not Found|
|[az identitysignins informationprotection list-threat-assessment-request](#informationProtectionListThreatAssessmentRequests)|ListThreatAssessmentRequests|[Parameters](#ParametersinformationProtectionListThreatAssessmentRequests)|Not Found|
|[az identitysignins informationprotection show-data-loss-prevention-policy](#informationProtectionGetDataLossPreventionPolicies)|GetDataLossPreventionPolicies|[Parameters](#ParametersinformationProtectionGetDataLossPreventionPolicies)|Not Found|
|[az identitysignins informationprotection show-policy](#informationProtectionGetPolicy)|GetPolicy|[Parameters](#ParametersinformationProtectionGetPolicy)|Not Found|
|[az identitysignins informationprotection show-sensitivity-label](#informationProtectionGetSensitivityLabels)|GetSensitivityLabels|[Parameters](#ParametersinformationProtectionGetSensitivityLabels)|Not Found|
|[az identitysignins informationprotection show-sensitivity-policy-setting](#informationProtectionGetSensitivityPolicySettings)|GetSensitivityPolicySettings|[Parameters](#ParametersinformationProtectionGetSensitivityPolicySettings)|Not Found|
|[az identitysignins informationprotection show-threat-assessment-request](#informationProtectionGetThreatAssessmentRequests)|GetThreatAssessmentRequests|[Parameters](#ParametersinformationProtectionGetThreatAssessmentRequests)|Not Found|
|[az identitysignins informationprotection update-data-loss-prevention-policy](#informationProtectionUpdateDataLossPreventionPolicies)|UpdateDataLossPreventionPolicies|[Parameters](#ParametersinformationProtectionUpdateDataLossPreventionPolicies)|Not Found|
|[az identitysignins informationprotection update-policy](#informationProtectionUpdatePolicy)|UpdatePolicy|[Parameters](#ParametersinformationProtectionUpdatePolicy)|Not Found|
|[az identitysignins informationprotection update-sensitivity-label](#informationProtectionUpdateSensitivityLabels)|UpdateSensitivityLabels|[Parameters](#ParametersinformationProtectionUpdateSensitivityLabels)|Not Found|
|[az identitysignins informationprotection update-sensitivity-policy-setting](#informationProtectionUpdateSensitivityPolicySettings)|UpdateSensitivityPolicySettings|[Parameters](#ParametersinformationProtectionUpdateSensitivityPolicySettings)|Not Found|
|[az identitysignins informationprotection update-threat-assessment-request](#informationProtectionUpdateThreatAssessmentRequests)|UpdateThreatAssessmentRequests|[Parameters](#ParametersinformationProtectionUpdateThreatAssessmentRequests)|Not Found|

### <a name="CommandsIninformationProtection.dataLossPreventionPolicies">Commands in `az identitysignins informationprotectiondatalosspreventionpolicy` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins informationprotectiondatalosspreventionpolicy evaluate](#informationProtection.dataLossPreventionPoliciesevaluate)|evaluate|[Parameters](#ParametersinformationProtection.dataLossPreventionPoliciesevaluate)|Not Found|

### <a name="CommandsIninformationProtection.policy">Commands in `az identitysignins informationprotectionpolicy` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins informationprotectionpolicy create-label](#informationProtection.policyCreateLabels)|CreateLabels|[Parameters](#ParametersinformationProtection.policyCreateLabels)|Not Found|
|[az identitysignins informationprotectionpolicy delete-label](#informationProtection.policyDeleteLabels)|DeleteLabels|[Parameters](#ParametersinformationProtection.policyDeleteLabels)|Not Found|
|[az identitysignins informationprotectionpolicy list-label](#informationProtection.policyListLabels)|ListLabels|[Parameters](#ParametersinformationProtection.policyListLabels)|Not Found|
|[az identitysignins informationprotectionpolicy show-label](#informationProtection.policyGetLabels)|GetLabels|[Parameters](#ParametersinformationProtection.policyGetLabels)|Not Found|
|[az identitysignins informationprotectionpolicy update-label](#informationProtection.policyUpdateLabels)|UpdateLabels|[Parameters](#ParametersinformationProtection.policyUpdateLabels)|Not Found|

### <a name="CommandsIninformationProtection.policy.labels">Commands in `az identitysignins informationprotectionpolicylabel` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins informationprotectionpolicylabel evaluate-application](#informationProtection.policy.labelsevaluateApplication)|evaluateApplication|[Parameters](#ParametersinformationProtection.policy.labelsevaluateApplication)|Not Found|
|[az identitysignins informationprotectionpolicylabel evaluate-classification-result](#informationProtection.policy.labelsevaluateClassificationResults)|evaluateClassificationResults|[Parameters](#ParametersinformationProtection.policy.labelsevaluateClassificationResults)|Not Found|
|[az identitysignins informationprotectionpolicylabel evaluate-removal](#informationProtection.policy.labelsevaluateRemoval)|evaluateRemoval|[Parameters](#ParametersinformationProtection.policy.labelsevaluateRemoval)|Not Found|
|[az identitysignins informationprotectionpolicylabel extract-label](#informationProtection.policy.labelsextractLabel)|extractLabel|[Parameters](#ParametersinformationProtection.policy.labelsextractLabel)|Not Found|

### <a name="CommandsIninformationProtection.sensitivityLabels">Commands in `az identitysignins informationprotectionsensitivitylabel` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins informationprotectionsensitivitylabel create-sublabel](#informationProtection.sensitivityLabelsCreateSublabels)|CreateSublabels|[Parameters](#ParametersinformationProtection.sensitivityLabelsCreateSublabels)|Not Found|
|[az identitysignins informationprotectionsensitivitylabel delete-sublabel](#informationProtection.sensitivityLabelsDeleteSublabels)|DeleteSublabels|[Parameters](#ParametersinformationProtection.sensitivityLabelsDeleteSublabels)|Not Found|
|[az identitysignins informationprotectionsensitivitylabel evaluate](#informationProtection.sensitivityLabelsevaluate)|evaluate|[Parameters](#ParametersinformationProtection.sensitivityLabelsevaluate)|Not Found|
|[az identitysignins informationprotectionsensitivitylabel list-sublabel](#informationProtection.sensitivityLabelsListSublabels)|ListSublabels|[Parameters](#ParametersinformationProtection.sensitivityLabelsListSublabels)|Not Found|
|[az identitysignins informationprotectionsensitivitylabel show-sublabel](#informationProtection.sensitivityLabelsGetSublabels)|GetSublabels|[Parameters](#ParametersinformationProtection.sensitivityLabelsGetSublabels)|Not Found|
|[az identitysignins informationprotectionsensitivitylabel update-sublabel](#informationProtection.sensitivityLabelsUpdateSublabels)|UpdateSublabels|[Parameters](#ParametersinformationProtection.sensitivityLabelsUpdateSublabels)|Not Found|

### <a name="CommandsIninformationProtection.sensitivityLabels.sublabels">Commands in `az identitysignins informationprotectionsensitivitylabelssublabel` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins informationprotectionsensitivitylabelssublabel evaluate](#informationProtection.sensitivityLabels.sublabelsevaluate)|evaluate|[Parameters](#ParametersinformationProtection.sensitivityLabels.sublabelsevaluate)|Not Found|

### <a name="CommandsIninformationProtection.threatAssessmentRequests">Commands in `az identitysignins informationprotectionthreatassessmentrequest` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins informationprotectionthreatassessmentrequest create-result](#informationProtection.threatAssessmentRequestsCreateResults)|CreateResults|[Parameters](#ParametersinformationProtection.threatAssessmentRequestsCreateResults)|Not Found|
|[az identitysignins informationprotectionthreatassessmentrequest delete-result](#informationProtection.threatAssessmentRequestsDeleteResults)|DeleteResults|[Parameters](#ParametersinformationProtection.threatAssessmentRequestsDeleteResults)|Not Found|
|[az identitysignins informationprotectionthreatassessmentrequest list-result](#informationProtection.threatAssessmentRequestsListResults)|ListResults|[Parameters](#ParametersinformationProtection.threatAssessmentRequestsListResults)|Not Found|
|[az identitysignins informationprotectionthreatassessmentrequest show-result](#informationProtection.threatAssessmentRequestsGetResults)|GetResults|[Parameters](#ParametersinformationProtection.threatAssessmentRequestsGetResults)|Not Found|
|[az identitysignins informationprotectionthreatassessmentrequest update-result](#informationProtection.threatAssessmentRequestsUpdateResults)|UpdateResults|[Parameters](#ParametersinformationProtection.threatAssessmentRequestsUpdateResults)|Not Found|

### <a name="CommandsIninvitations">Commands in `az identitysignins invitation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins invitation delete-ref-invited-user](#invitationsDeleteRefInvitedUser)|DeleteRefInvitedUser|[Parameters](#ParametersinvitationsDeleteRefInvitedUser)|Not Found|
|[az identitysignins invitation set-ref-invited-user](#invitationsSetRefInvitedUser)|SetRefInvitedUser|[Parameters](#ParametersinvitationsSetRefInvitedUser)|Not Found|
|[az identitysignins invitation show-invited-user](#invitationsGetInvitedUser)|GetInvitedUser|[Parameters](#ParametersinvitationsGetInvitedUser)|Not Found|
|[az identitysignins invitation show-ref-invited-user](#invitationsGetRefInvitedUser)|GetRefInvitedUser|[Parameters](#ParametersinvitationsGetRefInvitedUser)|Not Found|

### <a name="CommandsIninvitations.invitation">Commands in `az identitysignins invitationsinvitation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins invitationsinvitation create-invitation](#invitations.invitationCreateInvitation)|CreateInvitation|[Parameters](#Parametersinvitations.invitationCreateInvitation)|Not Found|
|[az identitysignins invitationsinvitation delete-invitation](#invitations.invitationDeleteInvitation)|DeleteInvitation|[Parameters](#Parametersinvitations.invitationDeleteInvitation)|Not Found|
|[az identitysignins invitationsinvitation list-invitation](#invitations.invitationListInvitation)|ListInvitation|[Parameters](#Parametersinvitations.invitationListInvitation)|Not Found|
|[az identitysignins invitationsinvitation show-invitation](#invitations.invitationGetInvitation)|GetInvitation|[Parameters](#Parametersinvitations.invitationGetInvitation)|Not Found|
|[az identitysignins invitationsinvitation update-invitation](#invitations.invitationUpdateInvitation)|UpdateInvitation|[Parameters](#Parametersinvitations.invitationUpdateInvitation)|Not Found|

### <a name="CommandsInoauth2PermissionGrants">Commands in `az identitysignins oauth2permissiongrant` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins oauth2permissiongrant delta](#oauth2PermissionGrantsdelta)|delta|[Parameters](#Parametersoauth2PermissionGrantsdelta)|Not Found|

### <a name="CommandsInoauth2PermissionGrants.oAuth2PermissionGrant">Commands in `az identitysignins oauth2permissiongrantsoauth2permissiongrant` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins oauth2permissiongrantsoauth2permissiongrant create-o-auth2-permission-grant](#oauth2PermissionGrants.oAuth2PermissionGrantCreateOAuth2PermissionGrant)|CreateOAuth2PermissionGrant|[Parameters](#Parametersoauth2PermissionGrants.oAuth2PermissionGrantCreateOAuth2PermissionGrant)|Not Found|
|[az identitysignins oauth2permissiongrantsoauth2permissiongrant delete-o-auth2-permission-grant](#oauth2PermissionGrants.oAuth2PermissionGrantDeleteOAuth2PermissionGrant)|DeleteOAuth2PermissionGrant|[Parameters](#Parametersoauth2PermissionGrants.oAuth2PermissionGrantDeleteOAuth2PermissionGrant)|Not Found|
|[az identitysignins oauth2permissiongrantsoauth2permissiongrant list-o-auth2-permission-grant](#oauth2PermissionGrants.oAuth2PermissionGrantListOAuth2PermissionGrant)|ListOAuth2PermissionGrant|[Parameters](#Parametersoauth2PermissionGrants.oAuth2PermissionGrantListOAuth2PermissionGrant)|Not Found|
|[az identitysignins oauth2permissiongrantsoauth2permissiongrant show-o-auth2-permission-grant](#oauth2PermissionGrants.oAuth2PermissionGrantGetOAuth2PermissionGrant)|GetOAuth2PermissionGrant|[Parameters](#Parametersoauth2PermissionGrants.oAuth2PermissionGrantGetOAuth2PermissionGrant)|Not Found|
|[az identitysignins oauth2permissiongrantsoauth2permissiongrant update-o-auth2-permission-grant](#oauth2PermissionGrants.oAuth2PermissionGrantUpdateOAuth2PermissionGrant)|UpdateOAuth2PermissionGrant|[Parameters](#Parametersoauth2PermissionGrants.oAuth2PermissionGrantUpdateOAuth2PermissionGrant)|Not Found|

### <a name="CommandsInorganization">Commands in `az identitysignins organization` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins organization create-ref-certificate-based-auth-configuration](#organizationCreateRefCertificateBasedAuthConfiguration)|CreateRefCertificateBasedAuthConfiguration|[Parameters](#ParametersorganizationCreateRefCertificateBasedAuthConfiguration)|Not Found|
|[az identitysignins organization list-certificate-based-auth-configuration](#organizationListCertificateBasedAuthConfiguration)|ListCertificateBasedAuthConfiguration|[Parameters](#ParametersorganizationListCertificateBasedAuthConfiguration)|Not Found|
|[az identitysignins organization list-ref-certificate-based-auth-configuration](#organizationListRefCertificateBasedAuthConfiguration)|ListRefCertificateBasedAuthConfiguration|[Parameters](#ParametersorganizationListRefCertificateBasedAuthConfiguration)|Not Found|

### <a name="CommandsInpolicies.permissionGrantPolicies">Commands in `az identitysignins policiespermissiongrantpolicy` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins policiespermissiongrantpolicy create-exclude](#policies.permissionGrantPoliciesCreateExcludes)|CreateExcludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesCreateExcludes)|Not Found|
|[az identitysignins policiespermissiongrantpolicy create-include](#policies.permissionGrantPoliciesCreateIncludes)|CreateIncludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesCreateIncludes)|Not Found|
|[az identitysignins policiespermissiongrantpolicy delete-exclude](#policies.permissionGrantPoliciesDeleteExcludes)|DeleteExcludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesDeleteExcludes)|Not Found|
|[az identitysignins policiespermissiongrantpolicy delete-include](#policies.permissionGrantPoliciesDeleteIncludes)|DeleteIncludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesDeleteIncludes)|Not Found|
|[az identitysignins policiespermissiongrantpolicy list-exclude](#policies.permissionGrantPoliciesListExcludes)|ListExcludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesListExcludes)|Not Found|
|[az identitysignins policiespermissiongrantpolicy list-include](#policies.permissionGrantPoliciesListIncludes)|ListIncludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesListIncludes)|Not Found|
|[az identitysignins policiespermissiongrantpolicy show-exclude](#policies.permissionGrantPoliciesGetExcludes)|GetExcludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesGetExcludes)|Not Found|
|[az identitysignins policiespermissiongrantpolicy show-include](#policies.permissionGrantPoliciesGetIncludes)|GetIncludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesGetIncludes)|Not Found|
|[az identitysignins policiespermissiongrantpolicy update-exclude](#policies.permissionGrantPoliciesUpdateExcludes)|UpdateExcludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesUpdateExcludes)|Not Found|
|[az identitysignins policiespermissiongrantpolicy update-include](#policies.permissionGrantPoliciesUpdateIncludes)|UpdateIncludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesUpdateIncludes)|Not Found|

### <a name="CommandsInpolicies.policyRoot">Commands in `az identitysignins policiespolicyroot` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins policiespolicyroot show-policy-root](#policies.policyRootGetPolicyRoot)|GetPolicyRoot|[Parameters](#Parameterspolicies.policyRootGetPolicyRoot)|Not Found|
|[az identitysignins policiespolicyroot update-policy-root](#policies.policyRootUpdatePolicyRoot)|UpdatePolicyRoot|[Parameters](#Parameterspolicies.policyRootUpdatePolicyRoot)|Not Found|

### <a name="CommandsInpolicies">Commands in `az identitysignins policy` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins policy create-activity-based-timeout-policy](#policiesCreateActivityBasedTimeoutPolicies)|CreateActivityBasedTimeoutPolicies|[Parameters](#ParameterspoliciesCreateActivityBasedTimeoutPolicies)|Not Found|
|[az identitysignins policy create-authorization-policy](#policiesCreateAuthorizationPolicy)|CreateAuthorizationPolicy|[Parameters](#ParameterspoliciesCreateAuthorizationPolicy)|Not Found|
|[az identitysignins policy create-claim-mapping-policy](#policiesCreateClaimsMappingPolicies)|CreateClaimsMappingPolicies|[Parameters](#ParameterspoliciesCreateClaimsMappingPolicies)|Not Found|
|[az identitysignins policy create-conditional-access-policy](#policiesCreateConditionalAccessPolicies)|CreateConditionalAccessPolicies|[Parameters](#ParameterspoliciesCreateConditionalAccessPolicies)|Not Found|
|[az identitysignins policy create-home-realm-discovery-policy](#policiesCreateHomeRealmDiscoveryPolicies)|CreateHomeRealmDiscoveryPolicies|[Parameters](#ParameterspoliciesCreateHomeRealmDiscoveryPolicies)|Not Found|
|[az identitysignins policy create-permission-grant-policy](#policiesCreatePermissionGrantPolicies)|CreatePermissionGrantPolicies|[Parameters](#ParameterspoliciesCreatePermissionGrantPolicies)|Not Found|
|[az identitysignins policy create-private-link-resource-policy](#policiesCreatePrivateLinkResourcePolicies)|CreatePrivateLinkResourcePolicies|[Parameters](#ParameterspoliciesCreatePrivateLinkResourcePolicies)|Not Found|
|[az identitysignins policy create-token-issuance-policy](#policiesCreateTokenIssuancePolicies)|CreateTokenIssuancePolicies|[Parameters](#ParameterspoliciesCreateTokenIssuancePolicies)|Not Found|
|[az identitysignins policy create-token-lifetime-policy](#policiesCreateTokenLifetimePolicies)|CreateTokenLifetimePolicies|[Parameters](#ParameterspoliciesCreateTokenLifetimePolicies)|Not Found|
|[az identitysignins policy delete-activity-based-timeout-policy](#policiesDeleteActivityBasedTimeoutPolicies)|DeleteActivityBasedTimeoutPolicies|[Parameters](#ParameterspoliciesDeleteActivityBasedTimeoutPolicies)|Not Found|
|[az identitysignins policy delete-admin-consent-request-policy](#policiesDeleteAdminConsentRequestPolicy)|DeleteAdminConsentRequestPolicy|[Parameters](#ParameterspoliciesDeleteAdminConsentRequestPolicy)|Not Found|
|[az identitysignins policy delete-authentication-flow-policy](#policiesDeleteAuthenticationFlowsPolicy)|DeleteAuthenticationFlowsPolicy|[Parameters](#ParameterspoliciesDeleteAuthenticationFlowsPolicy)|Not Found|
|[az identitysignins policy delete-authorization-policy](#policiesDeleteAuthorizationPolicy)|DeleteAuthorizationPolicy|[Parameters](#ParameterspoliciesDeleteAuthorizationPolicy)|Not Found|
|[az identitysignins policy delete-b2-c-authentication-method-policy](#policiesDeleteB2cAuthenticationMethodsPolicy)|DeleteB2cAuthenticationMethodsPolicy|[Parameters](#ParameterspoliciesDeleteB2cAuthenticationMethodsPolicy)|Not Found|
|[az identitysignins policy delete-claim-mapping-policy](#policiesDeleteClaimsMappingPolicies)|DeleteClaimsMappingPolicies|[Parameters](#ParameterspoliciesDeleteClaimsMappingPolicies)|Not Found|
|[az identitysignins policy delete-conditional-access-policy](#policiesDeleteConditionalAccessPolicies)|DeleteConditionalAccessPolicies|[Parameters](#ParameterspoliciesDeleteConditionalAccessPolicies)|Not Found|
|[az identitysignins policy delete-device-registration-policy](#policiesDeleteDeviceRegistrationPolicy)|DeleteDeviceRegistrationPolicy|[Parameters](#ParameterspoliciesDeleteDeviceRegistrationPolicy)|Not Found|
|[az identitysignins policy delete-directory-role-access-review-policy](#policiesDeleteDirectoryRoleAccessReviewPolicy)|DeleteDirectoryRoleAccessReviewPolicy|[Parameters](#ParameterspoliciesDeleteDirectoryRoleAccessReviewPolicy)|Not Found|
|[az identitysignins policy delete-home-realm-discovery-policy](#policiesDeleteHomeRealmDiscoveryPolicies)|DeleteHomeRealmDiscoveryPolicies|[Parameters](#ParameterspoliciesDeleteHomeRealmDiscoveryPolicies)|Not Found|
|[az identitysignins policy delete-identity-security-default-enforcement-policy](#policiesDeleteIdentitySecurityDefaultsEnforcementPolicy)|DeleteIdentitySecurityDefaultsEnforcementPolicy|[Parameters](#ParameterspoliciesDeleteIdentitySecurityDefaultsEnforcementPolicy)|Not Found|
|[az identitysignins policy delete-permission-grant-policy](#policiesDeletePermissionGrantPolicies)|DeletePermissionGrantPolicies|[Parameters](#ParameterspoliciesDeletePermissionGrantPolicies)|Not Found|
|[az identitysignins policy delete-private-link-resource-policy](#policiesDeletePrivateLinkResourcePolicies)|DeletePrivateLinkResourcePolicies|[Parameters](#ParameterspoliciesDeletePrivateLinkResourcePolicies)|Not Found|
|[az identitysignins policy delete-token-issuance-policy](#policiesDeleteTokenIssuancePolicies)|DeleteTokenIssuancePolicies|[Parameters](#ParameterspoliciesDeleteTokenIssuancePolicies)|Not Found|
|[az identitysignins policy delete-token-lifetime-policy](#policiesDeleteTokenLifetimePolicies)|DeleteTokenLifetimePolicies|[Parameters](#ParameterspoliciesDeleteTokenLifetimePolicies)|Not Found|
|[az identitysignins policy list-activity-based-timeout-policy](#policiesListActivityBasedTimeoutPolicies)|ListActivityBasedTimeoutPolicies|[Parameters](#ParameterspoliciesListActivityBasedTimeoutPolicies)|Not Found|
|[az identitysignins policy list-authorization-policy](#policiesListAuthorizationPolicy)|ListAuthorizationPolicy|[Parameters](#ParameterspoliciesListAuthorizationPolicy)|Not Found|
|[az identitysignins policy list-claim-mapping-policy](#policiesListClaimsMappingPolicies)|ListClaimsMappingPolicies|[Parameters](#ParameterspoliciesListClaimsMappingPolicies)|Not Found|
|[az identitysignins policy list-conditional-access-policy](#policiesListConditionalAccessPolicies)|ListConditionalAccessPolicies|[Parameters](#ParameterspoliciesListConditionalAccessPolicies)|Not Found|
|[az identitysignins policy list-home-realm-discovery-policy](#policiesListHomeRealmDiscoveryPolicies)|ListHomeRealmDiscoveryPolicies|[Parameters](#ParameterspoliciesListHomeRealmDiscoveryPolicies)|Not Found|
|[az identitysignins policy list-permission-grant-policy](#policiesListPermissionGrantPolicies)|ListPermissionGrantPolicies|[Parameters](#ParameterspoliciesListPermissionGrantPolicies)|Not Found|
|[az identitysignins policy list-private-link-resource-policy](#policiesListPrivateLinkResourcePolicies)|ListPrivateLinkResourcePolicies|[Parameters](#ParameterspoliciesListPrivateLinkResourcePolicies)|Not Found|
|[az identitysignins policy list-token-issuance-policy](#policiesListTokenIssuancePolicies)|ListTokenIssuancePolicies|[Parameters](#ParameterspoliciesListTokenIssuancePolicies)|Not Found|
|[az identitysignins policy list-token-lifetime-policy](#policiesListTokenLifetimePolicies)|ListTokenLifetimePolicies|[Parameters](#ParameterspoliciesListTokenLifetimePolicies)|Not Found|
|[az identitysignins policy show-activity-based-timeout-policy](#policiesGetActivityBasedTimeoutPolicies)|GetActivityBasedTimeoutPolicies|[Parameters](#ParameterspoliciesGetActivityBasedTimeoutPolicies)|Not Found|
|[az identitysignins policy show-admin-consent-request-policy](#policiesGetAdminConsentRequestPolicy)|GetAdminConsentRequestPolicy|[Parameters](#ParameterspoliciesGetAdminConsentRequestPolicy)|Not Found|
|[az identitysignins policy show-authentication-flow-policy](#policiesGetAuthenticationFlowsPolicy)|GetAuthenticationFlowsPolicy|[Parameters](#ParameterspoliciesGetAuthenticationFlowsPolicy)|Not Found|
|[az identitysignins policy show-authorization-policy](#policiesGetAuthorizationPolicy)|GetAuthorizationPolicy|[Parameters](#ParameterspoliciesGetAuthorizationPolicy)|Not Found|
|[az identitysignins policy show-b2-c-authentication-method-policy](#policiesGetB2cAuthenticationMethodsPolicy)|GetB2cAuthenticationMethodsPolicy|[Parameters](#ParameterspoliciesGetB2cAuthenticationMethodsPolicy)|Not Found|
|[az identitysignins policy show-claim-mapping-policy](#policiesGetClaimsMappingPolicies)|GetClaimsMappingPolicies|[Parameters](#ParameterspoliciesGetClaimsMappingPolicies)|Not Found|
|[az identitysignins policy show-conditional-access-policy](#policiesGetConditionalAccessPolicies)|GetConditionalAccessPolicies|[Parameters](#ParameterspoliciesGetConditionalAccessPolicies)|Not Found|
|[az identitysignins policy show-device-registration-policy](#policiesGetDeviceRegistrationPolicy)|GetDeviceRegistrationPolicy|[Parameters](#ParameterspoliciesGetDeviceRegistrationPolicy)|Not Found|
|[az identitysignins policy show-directory-role-access-review-policy](#policiesGetDirectoryRoleAccessReviewPolicy)|GetDirectoryRoleAccessReviewPolicy|[Parameters](#ParameterspoliciesGetDirectoryRoleAccessReviewPolicy)|Not Found|
|[az identitysignins policy show-home-realm-discovery-policy](#policiesGetHomeRealmDiscoveryPolicies)|GetHomeRealmDiscoveryPolicies|[Parameters](#ParameterspoliciesGetHomeRealmDiscoveryPolicies)|Not Found|
|[az identitysignins policy show-identity-security-default-enforcement-policy](#policiesGetIdentitySecurityDefaultsEnforcementPolicy)|GetIdentitySecurityDefaultsEnforcementPolicy|[Parameters](#ParameterspoliciesGetIdentitySecurityDefaultsEnforcementPolicy)|Not Found|
|[az identitysignins policy show-permission-grant-policy](#policiesGetPermissionGrantPolicies)|GetPermissionGrantPolicies|[Parameters](#ParameterspoliciesGetPermissionGrantPolicies)|Not Found|
|[az identitysignins policy show-private-link-resource-policy](#policiesGetPrivateLinkResourcePolicies)|GetPrivateLinkResourcePolicies|[Parameters](#ParameterspoliciesGetPrivateLinkResourcePolicies)|Not Found|
|[az identitysignins policy show-token-issuance-policy](#policiesGetTokenIssuancePolicies)|GetTokenIssuancePolicies|[Parameters](#ParameterspoliciesGetTokenIssuancePolicies)|Not Found|
|[az identitysignins policy show-token-lifetime-policy](#policiesGetTokenLifetimePolicies)|GetTokenLifetimePolicies|[Parameters](#ParameterspoliciesGetTokenLifetimePolicies)|Not Found|
|[az identitysignins policy update-activity-based-timeout-policy](#policiesUpdateActivityBasedTimeoutPolicies)|UpdateActivityBasedTimeoutPolicies|[Parameters](#ParameterspoliciesUpdateActivityBasedTimeoutPolicies)|Not Found|
|[az identitysignins policy update-admin-consent-request-policy](#policiesUpdateAdminConsentRequestPolicy)|UpdateAdminConsentRequestPolicy|[Parameters](#ParameterspoliciesUpdateAdminConsentRequestPolicy)|Not Found|
|[az identitysignins policy update-authentication-flow-policy](#policiesUpdateAuthenticationFlowsPolicy)|UpdateAuthenticationFlowsPolicy|[Parameters](#ParameterspoliciesUpdateAuthenticationFlowsPolicy)|Not Found|
|[az identitysignins policy update-authorization-policy](#policiesUpdateAuthorizationPolicy)|UpdateAuthorizationPolicy|[Parameters](#ParameterspoliciesUpdateAuthorizationPolicy)|Not Found|
|[az identitysignins policy update-b2-c-authentication-method-policy](#policiesUpdateB2cAuthenticationMethodsPolicy)|UpdateB2cAuthenticationMethodsPolicy|[Parameters](#ParameterspoliciesUpdateB2cAuthenticationMethodsPolicy)|Not Found|
|[az identitysignins policy update-claim-mapping-policy](#policiesUpdateClaimsMappingPolicies)|UpdateClaimsMappingPolicies|[Parameters](#ParameterspoliciesUpdateClaimsMappingPolicies)|Not Found|
|[az identitysignins policy update-conditional-access-policy](#policiesUpdateConditionalAccessPolicies)|UpdateConditionalAccessPolicies|[Parameters](#ParameterspoliciesUpdateConditionalAccessPolicies)|Not Found|
|[az identitysignins policy update-device-registration-policy](#policiesUpdateDeviceRegistrationPolicy)|UpdateDeviceRegistrationPolicy|[Parameters](#ParameterspoliciesUpdateDeviceRegistrationPolicy)|Not Found|
|[az identitysignins policy update-directory-role-access-review-policy](#policiesUpdateDirectoryRoleAccessReviewPolicy)|UpdateDirectoryRoleAccessReviewPolicy|[Parameters](#ParameterspoliciesUpdateDirectoryRoleAccessReviewPolicy)|Not Found|
|[az identitysignins policy update-home-realm-discovery-policy](#policiesUpdateHomeRealmDiscoveryPolicies)|UpdateHomeRealmDiscoveryPolicies|[Parameters](#ParameterspoliciesUpdateHomeRealmDiscoveryPolicies)|Not Found|
|[az identitysignins policy update-identity-security-default-enforcement-policy](#policiesUpdateIdentitySecurityDefaultsEnforcementPolicy)|UpdateIdentitySecurityDefaultsEnforcementPolicy|[Parameters](#ParameterspoliciesUpdateIdentitySecurityDefaultsEnforcementPolicy)|Not Found|
|[az identitysignins policy update-permission-grant-policy](#policiesUpdatePermissionGrantPolicies)|UpdatePermissionGrantPolicies|[Parameters](#ParameterspoliciesUpdatePermissionGrantPolicies)|Not Found|
|[az identitysignins policy update-private-link-resource-policy](#policiesUpdatePrivateLinkResourcePolicies)|UpdatePrivateLinkResourcePolicies|[Parameters](#ParameterspoliciesUpdatePrivateLinkResourcePolicies)|Not Found|
|[az identitysignins policy update-token-issuance-policy](#policiesUpdateTokenIssuancePolicies)|UpdateTokenIssuancePolicies|[Parameters](#ParameterspoliciesUpdateTokenIssuancePolicies)|Not Found|
|[az identitysignins policy update-token-lifetime-policy](#policiesUpdateTokenLifetimePolicies)|UpdateTokenLifetimePolicies|[Parameters](#ParameterspoliciesUpdateTokenLifetimePolicies)|Not Found|

### <a name="CommandsInriskDetections.riskDetection">Commands in `az identitysignins riskdetectionsriskdetection` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins riskdetectionsriskdetection create-risk-detection](#riskDetections.riskDetectionCreateRiskDetection)|CreateRiskDetection|[Parameters](#ParametersriskDetections.riskDetectionCreateRiskDetection)|Not Found|
|[az identitysignins riskdetectionsriskdetection delete-risk-detection](#riskDetections.riskDetectionDeleteRiskDetection)|DeleteRiskDetection|[Parameters](#ParametersriskDetections.riskDetectionDeleteRiskDetection)|Not Found|
|[az identitysignins riskdetectionsriskdetection list-risk-detection](#riskDetections.riskDetectionListRiskDetection)|ListRiskDetection|[Parameters](#ParametersriskDetections.riskDetectionListRiskDetection)|Not Found|
|[az identitysignins riskdetectionsriskdetection show-risk-detection](#riskDetections.riskDetectionGetRiskDetection)|GetRiskDetection|[Parameters](#ParametersriskDetections.riskDetectionGetRiskDetection)|Not Found|
|[az identitysignins riskdetectionsriskdetection update-risk-detection](#riskDetections.riskDetectionUpdateRiskDetection)|UpdateRiskDetection|[Parameters](#ParametersriskDetections.riskDetectionUpdateRiskDetection)|Not Found|

### <a name="CommandsInriskyUsers">Commands in `az identitysignins riskyuser` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins riskyuser confirm-compromised](#riskyUsersconfirmCompromised)|confirmCompromised|[Parameters](#ParametersriskyUsersconfirmCompromised)|Not Found|
|[az identitysignins riskyuser create-history](#riskyUsersCreateHistory)|CreateHistory|[Parameters](#ParametersriskyUsersCreateHistory)|Not Found|
|[az identitysignins riskyuser delete-history](#riskyUsersDeleteHistory)|DeleteHistory|[Parameters](#ParametersriskyUsersDeleteHistory)|Not Found|
|[az identitysignins riskyuser dismiss](#riskyUsersdismiss)|dismiss|[Parameters](#ParametersriskyUsersdismiss)|Not Found|
|[az identitysignins riskyuser list-history](#riskyUsersListHistory)|ListHistory|[Parameters](#ParametersriskyUsersListHistory)|Not Found|
|[az identitysignins riskyuser show-history](#riskyUsersGetHistory)|GetHistory|[Parameters](#ParametersriskyUsersGetHistory)|Not Found|
|[az identitysignins riskyuser update-history](#riskyUsersUpdateHistory)|UpdateHistory|[Parameters](#ParametersriskyUsersUpdateHistory)|Not Found|

### <a name="CommandsInriskyUsers.riskyUser">Commands in `az identitysignins riskyusersriskyuser` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins riskyusersriskyuser create-risky-user](#riskyUsers.riskyUserCreateRiskyUser)|CreateRiskyUser|[Parameters](#ParametersriskyUsers.riskyUserCreateRiskyUser)|Not Found|
|[az identitysignins riskyusersriskyuser delete-risky-user](#riskyUsers.riskyUserDeleteRiskyUser)|DeleteRiskyUser|[Parameters](#ParametersriskyUsers.riskyUserDeleteRiskyUser)|Not Found|
|[az identitysignins riskyusersriskyuser list-risky-user](#riskyUsers.riskyUserListRiskyUser)|ListRiskyUser|[Parameters](#ParametersriskyUsers.riskyUserListRiskyUser)|Not Found|
|[az identitysignins riskyusersriskyuser show-risky-user](#riskyUsers.riskyUserGetRiskyUser)|GetRiskyUser|[Parameters](#ParametersriskyUsers.riskyUserGetRiskyUser)|Not Found|
|[az identitysignins riskyusersriskyuser update-risky-user](#riskyUsers.riskyUserUpdateRiskyUser)|UpdateRiskyUser|[Parameters](#ParametersriskyUsers.riskyUserUpdateRiskyUser)|Not Found|

### <a name="CommandsIntrustFramework.trustFramework">Commands in `az identitysignins trustframework` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins trustframework show-trust-framework](#trustFramework.trustFrameworkGetTrustFramework)|GetTrustFramework|[Parameters](#ParameterstrustFramework.trustFrameworkGetTrustFramework)|Not Found|
|[az identitysignins trustframework update-trust-framework](#trustFramework.trustFrameworkUpdateTrustFramework)|UpdateTrustFramework|[Parameters](#ParameterstrustFramework.trustFrameworkUpdateTrustFramework)|Not Found|

### <a name="CommandsIntrustFramework">Commands in `az identitysignins trustframework` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins trustframework create-key-set](#trustFrameworkCreateKeySets)|CreateKeySets|[Parameters](#ParameterstrustFrameworkCreateKeySets)|Not Found|
|[az identitysignins trustframework create-policy](#trustFrameworkCreatePolicies)|CreatePolicies|[Parameters](#ParameterstrustFrameworkCreatePolicies)|Not Found|
|[az identitysignins trustframework delete-key-set](#trustFrameworkDeleteKeySets)|DeleteKeySets|[Parameters](#ParameterstrustFrameworkDeleteKeySets)|Not Found|
|[az identitysignins trustframework delete-policy](#trustFrameworkDeletePolicies)|DeletePolicies|[Parameters](#ParameterstrustFrameworkDeletePolicies)|Not Found|
|[az identitysignins trustframework list-key-set](#trustFrameworkListKeySets)|ListKeySets|[Parameters](#ParameterstrustFrameworkListKeySets)|Not Found|
|[az identitysignins trustframework list-policy](#trustFrameworkListPolicies)|ListPolicies|[Parameters](#ParameterstrustFrameworkListPolicies)|Not Found|
|[az identitysignins trustframework set-policy-content](#trustFrameworkSetPoliciesContent)|SetPoliciesContent|[Parameters](#ParameterstrustFrameworkSetPoliciesContent)|Not Found|
|[az identitysignins trustframework show-key-set](#trustFrameworkGetKeySets)|GetKeySets|[Parameters](#ParameterstrustFrameworkGetKeySets)|Not Found|
|[az identitysignins trustframework show-policy](#trustFrameworkGetPolicies)|GetPolicies|[Parameters](#ParameterstrustFrameworkGetPolicies)|Not Found|
|[az identitysignins trustframework show-policy-content](#trustFrameworkGetPoliciesContent)|GetPoliciesContent|[Parameters](#ParameterstrustFrameworkGetPoliciesContent)|Not Found|
|[az identitysignins trustframework update-key-set](#trustFrameworkUpdateKeySets)|UpdateKeySets|[Parameters](#ParameterstrustFrameworkUpdateKeySets)|Not Found|
|[az identitysignins trustframework update-policy](#trustFrameworkUpdatePolicies)|UpdatePolicies|[Parameters](#ParameterstrustFrameworkUpdatePolicies)|Not Found|

### <a name="CommandsIntrustFramework.keySets">Commands in `az identitysignins trustframeworkkeyset` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins trustframeworkkeyset generate-key](#trustFramework.keySetsgenerateKey)|generateKey|[Parameters](#ParameterstrustFramework.keySetsgenerateKey)|Not Found|
|[az identitysignins trustframeworkkeyset show-active-key](#trustFramework.keySetsgetActiveKey)|getActiveKey|[Parameters](#ParameterstrustFramework.keySetsgetActiveKey)|Not Found|
|[az identitysignins trustframeworkkeyset upload-certificate](#trustFramework.keySetsuploadCertificate)|uploadCertificate|[Parameters](#ParameterstrustFramework.keySetsuploadCertificate)|Not Found|
|[az identitysignins trustframeworkkeyset upload-pkcs12](#trustFramework.keySetsuploadPkcs12)|uploadPkcs12|[Parameters](#ParameterstrustFramework.keySetsuploadPkcs12)|Not Found|
|[az identitysignins trustframeworkkeyset upload-secret](#trustFramework.keySetsuploadSecret)|uploadSecret|[Parameters](#ParameterstrustFramework.keySetsuploadSecret)|Not Found|

### <a name="CommandsInusers">Commands in `az identitysignins user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins user delete-authentication](#usersDeleteAuthentication)|DeleteAuthentication|[Parameters](#ParametersusersDeleteAuthentication)|Not Found|
|[az identitysignins user delete-information-protection](#usersDeleteInformationProtection)|DeleteInformationProtection|[Parameters](#ParametersusersDeleteInformationProtection)|Not Found|
|[az identitysignins user show-authentication](#usersGetAuthentication)|GetAuthentication|[Parameters](#ParametersusersGetAuthentication)|Not Found|
|[az identitysignins user show-information-protection](#usersGetInformationProtection)|GetInformationProtection|[Parameters](#ParametersusersGetInformationProtection)|Not Found|
|[az identitysignins user update-authentication](#usersUpdateAuthentication)|UpdateAuthentication|[Parameters](#ParametersusersUpdateAuthentication)|Not Found|
|[az identitysignins user update-information-protection](#usersUpdateInformationProtection)|UpdateInformationProtection|[Parameters](#ParametersusersUpdateInformationProtection)|Not Found|

### <a name="CommandsInusers.authentication">Commands in `az identitysignins usersauthentication` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins usersauthentication create-email-method](#users.authenticationCreateEmailMethods)|CreateEmailMethods|[Parameters](#Parametersusers.authenticationCreateEmailMethods)|Not Found|
|[az identitysignins usersauthentication create-fido2-method](#users.authenticationCreateFido2Methods)|CreateFido2Methods|[Parameters](#Parametersusers.authenticationCreateFido2Methods)|Not Found|
|[az identitysignins usersauthentication create-method](#users.authenticationCreateMethods)|CreateMethods|[Parameters](#Parametersusers.authenticationCreateMethods)|Not Found|
|[az identitysignins usersauthentication create-microsoft-authenticator-method](#users.authenticationCreateMicrosoftAuthenticatorMethods)|CreateMicrosoftAuthenticatorMethods|[Parameters](#Parametersusers.authenticationCreateMicrosoftAuthenticatorMethods)|Not Found|
|[az identitysignins usersauthentication create-oath-method](#users.authenticationCreateOathMethods)|CreateOathMethods|[Parameters](#Parametersusers.authenticationCreateOathMethods)|Not Found|
|[az identitysignins usersauthentication create-operation](#users.authenticationCreateOperations)|CreateOperations|[Parameters](#Parametersusers.authenticationCreateOperations)|Not Found|
|[az identitysignins usersauthentication create-password-method](#users.authenticationCreatePasswordMethods)|CreatePasswordMethods|[Parameters](#Parametersusers.authenticationCreatePasswordMethods)|Not Found|
|[az identitysignins usersauthentication create-passwordless-microsoft-authenticator-method](#users.authenticationCreatePasswordlessMicrosoftAuthenticatorMethods)|CreatePasswordlessMicrosoftAuthenticatorMethods|[Parameters](#Parametersusers.authenticationCreatePasswordlessMicrosoftAuthenticatorMethods)|Not Found|
|[az identitysignins usersauthentication create-phone-method](#users.authenticationCreatePhoneMethods)|CreatePhoneMethods|[Parameters](#Parametersusers.authenticationCreatePhoneMethods)|Not Found|
|[az identitysignins usersauthentication create-security-question-method](#users.authenticationCreateSecurityQuestionMethods)|CreateSecurityQuestionMethods|[Parameters](#Parametersusers.authenticationCreateSecurityQuestionMethods)|Not Found|
|[az identitysignins usersauthentication create-temporary-access-pass-method](#users.authenticationCreateTemporaryAccessPassMethods)|CreateTemporaryAccessPassMethods|[Parameters](#Parametersusers.authenticationCreateTemporaryAccessPassMethods)|Not Found|
|[az identitysignins usersauthentication delete-email-method](#users.authenticationDeleteEmailMethods)|DeleteEmailMethods|[Parameters](#Parametersusers.authenticationDeleteEmailMethods)|Not Found|
|[az identitysignins usersauthentication delete-fido2-method](#users.authenticationDeleteFido2Methods)|DeleteFido2Methods|[Parameters](#Parametersusers.authenticationDeleteFido2Methods)|Not Found|
|[az identitysignins usersauthentication delete-method](#users.authenticationDeleteMethods)|DeleteMethods|[Parameters](#Parametersusers.authenticationDeleteMethods)|Not Found|
|[az identitysignins usersauthentication delete-microsoft-authenticator-method](#users.authenticationDeleteMicrosoftAuthenticatorMethods)|DeleteMicrosoftAuthenticatorMethods|[Parameters](#Parametersusers.authenticationDeleteMicrosoftAuthenticatorMethods)|Not Found|
|[az identitysignins usersauthentication delete-oath-method](#users.authenticationDeleteOathMethods)|DeleteOathMethods|[Parameters](#Parametersusers.authenticationDeleteOathMethods)|Not Found|
|[az identitysignins usersauthentication delete-operation](#users.authenticationDeleteOperations)|DeleteOperations|[Parameters](#Parametersusers.authenticationDeleteOperations)|Not Found|
|[az identitysignins usersauthentication delete-password-method](#users.authenticationDeletePasswordMethods)|DeletePasswordMethods|[Parameters](#Parametersusers.authenticationDeletePasswordMethods)|Not Found|
|[az identitysignins usersauthentication delete-passwordless-microsoft-authenticator-method](#users.authenticationDeletePasswordlessMicrosoftAuthenticatorMethods)|DeletePasswordlessMicrosoftAuthenticatorMethods|[Parameters](#Parametersusers.authenticationDeletePasswordlessMicrosoftAuthenticatorMethods)|Not Found|
|[az identitysignins usersauthentication delete-phone-method](#users.authenticationDeletePhoneMethods)|DeletePhoneMethods|[Parameters](#Parametersusers.authenticationDeletePhoneMethods)|Not Found|
|[az identitysignins usersauthentication delete-security-question-method](#users.authenticationDeleteSecurityQuestionMethods)|DeleteSecurityQuestionMethods|[Parameters](#Parametersusers.authenticationDeleteSecurityQuestionMethods)|Not Found|
|[az identitysignins usersauthentication delete-temporary-access-pass-method](#users.authenticationDeleteTemporaryAccessPassMethods)|DeleteTemporaryAccessPassMethods|[Parameters](#Parametersusers.authenticationDeleteTemporaryAccessPassMethods)|Not Found|
|[az identitysignins usersauthentication list-email-method](#users.authenticationListEmailMethods)|ListEmailMethods|[Parameters](#Parametersusers.authenticationListEmailMethods)|Not Found|
|[az identitysignins usersauthentication list-fido2-method](#users.authenticationListFido2Methods)|ListFido2Methods|[Parameters](#Parametersusers.authenticationListFido2Methods)|Not Found|
|[az identitysignins usersauthentication list-method](#users.authenticationListMethods)|ListMethods|[Parameters](#Parametersusers.authenticationListMethods)|Not Found|
|[az identitysignins usersauthentication list-microsoft-authenticator-method](#users.authenticationListMicrosoftAuthenticatorMethods)|ListMicrosoftAuthenticatorMethods|[Parameters](#Parametersusers.authenticationListMicrosoftAuthenticatorMethods)|Not Found|
|[az identitysignins usersauthentication list-oath-method](#users.authenticationListOathMethods)|ListOathMethods|[Parameters](#Parametersusers.authenticationListOathMethods)|Not Found|
|[az identitysignins usersauthentication list-operation](#users.authenticationListOperations)|ListOperations|[Parameters](#Parametersusers.authenticationListOperations)|Not Found|
|[az identitysignins usersauthentication list-password-method](#users.authenticationListPasswordMethods)|ListPasswordMethods|[Parameters](#Parametersusers.authenticationListPasswordMethods)|Not Found|
|[az identitysignins usersauthentication list-passwordless-microsoft-authenticator-method](#users.authenticationListPasswordlessMicrosoftAuthenticatorMethods)|ListPasswordlessMicrosoftAuthenticatorMethods|[Parameters](#Parametersusers.authenticationListPasswordlessMicrosoftAuthenticatorMethods)|Not Found|
|[az identitysignins usersauthentication list-phone-method](#users.authenticationListPhoneMethods)|ListPhoneMethods|[Parameters](#Parametersusers.authenticationListPhoneMethods)|Not Found|
|[az identitysignins usersauthentication list-security-question-method](#users.authenticationListSecurityQuestionMethods)|ListSecurityQuestionMethods|[Parameters](#Parametersusers.authenticationListSecurityQuestionMethods)|Not Found|
|[az identitysignins usersauthentication list-temporary-access-pass-method](#users.authenticationListTemporaryAccessPassMethods)|ListTemporaryAccessPassMethods|[Parameters](#Parametersusers.authenticationListTemporaryAccessPassMethods)|Not Found|
|[az identitysignins usersauthentication show-email-method](#users.authenticationGetEmailMethods)|GetEmailMethods|[Parameters](#Parametersusers.authenticationGetEmailMethods)|Not Found|
|[az identitysignins usersauthentication show-fido2-method](#users.authenticationGetFido2Methods)|GetFido2Methods|[Parameters](#Parametersusers.authenticationGetFido2Methods)|Not Found|
|[az identitysignins usersauthentication show-method](#users.authenticationGetMethods)|GetMethods|[Parameters](#Parametersusers.authenticationGetMethods)|Not Found|
|[az identitysignins usersauthentication show-microsoft-authenticator-method](#users.authenticationGetMicrosoftAuthenticatorMethods)|GetMicrosoftAuthenticatorMethods|[Parameters](#Parametersusers.authenticationGetMicrosoftAuthenticatorMethods)|Not Found|
|[az identitysignins usersauthentication show-oath-method](#users.authenticationGetOathMethods)|GetOathMethods|[Parameters](#Parametersusers.authenticationGetOathMethods)|Not Found|
|[az identitysignins usersauthentication show-operation](#users.authenticationGetOperations)|GetOperations|[Parameters](#Parametersusers.authenticationGetOperations)|Not Found|
|[az identitysignins usersauthentication show-password-method](#users.authenticationGetPasswordMethods)|GetPasswordMethods|[Parameters](#Parametersusers.authenticationGetPasswordMethods)|Not Found|
|[az identitysignins usersauthentication show-passwordless-microsoft-authenticator-method](#users.authenticationGetPasswordlessMicrosoftAuthenticatorMethods)|GetPasswordlessMicrosoftAuthenticatorMethods|[Parameters](#Parametersusers.authenticationGetPasswordlessMicrosoftAuthenticatorMethods)|Not Found|
|[az identitysignins usersauthentication show-phone-method](#users.authenticationGetPhoneMethods)|GetPhoneMethods|[Parameters](#Parametersusers.authenticationGetPhoneMethods)|Not Found|
|[az identitysignins usersauthentication show-security-question-method](#users.authenticationGetSecurityQuestionMethods)|GetSecurityQuestionMethods|[Parameters](#Parametersusers.authenticationGetSecurityQuestionMethods)|Not Found|
|[az identitysignins usersauthentication show-temporary-access-pass-method](#users.authenticationGetTemporaryAccessPassMethods)|GetTemporaryAccessPassMethods|[Parameters](#Parametersusers.authenticationGetTemporaryAccessPassMethods)|Not Found|
|[az identitysignins usersauthentication update-email-method](#users.authenticationUpdateEmailMethods)|UpdateEmailMethods|[Parameters](#Parametersusers.authenticationUpdateEmailMethods)|Not Found|
|[az identitysignins usersauthentication update-fido2-method](#users.authenticationUpdateFido2Methods)|UpdateFido2Methods|[Parameters](#Parametersusers.authenticationUpdateFido2Methods)|Not Found|
|[az identitysignins usersauthentication update-method](#users.authenticationUpdateMethods)|UpdateMethods|[Parameters](#Parametersusers.authenticationUpdateMethods)|Not Found|
|[az identitysignins usersauthentication update-microsoft-authenticator-method](#users.authenticationUpdateMicrosoftAuthenticatorMethods)|UpdateMicrosoftAuthenticatorMethods|[Parameters](#Parametersusers.authenticationUpdateMicrosoftAuthenticatorMethods)|Not Found|
|[az identitysignins usersauthentication update-oath-method](#users.authenticationUpdateOathMethods)|UpdateOathMethods|[Parameters](#Parametersusers.authenticationUpdateOathMethods)|Not Found|
|[az identitysignins usersauthentication update-operation](#users.authenticationUpdateOperations)|UpdateOperations|[Parameters](#Parametersusers.authenticationUpdateOperations)|Not Found|
|[az identitysignins usersauthentication update-password-method](#users.authenticationUpdatePasswordMethods)|UpdatePasswordMethods|[Parameters](#Parametersusers.authenticationUpdatePasswordMethods)|Not Found|
|[az identitysignins usersauthentication update-passwordless-microsoft-authenticator-method](#users.authenticationUpdatePasswordlessMicrosoftAuthenticatorMethods)|UpdatePasswordlessMicrosoftAuthenticatorMethods|[Parameters](#Parametersusers.authenticationUpdatePasswordlessMicrosoftAuthenticatorMethods)|Not Found|
|[az identitysignins usersauthentication update-phone-method](#users.authenticationUpdatePhoneMethods)|UpdatePhoneMethods|[Parameters](#Parametersusers.authenticationUpdatePhoneMethods)|Not Found|
|[az identitysignins usersauthentication update-security-question-method](#users.authenticationUpdateSecurityQuestionMethods)|UpdateSecurityQuestionMethods|[Parameters](#Parametersusers.authenticationUpdateSecurityQuestionMethods)|Not Found|
|[az identitysignins usersauthentication update-temporary-access-pass-method](#users.authenticationUpdateTemporaryAccessPassMethods)|UpdateTemporaryAccessPassMethods|[Parameters](#Parametersusers.authenticationUpdateTemporaryAccessPassMethods)|Not Found|


## COMMAND DETAILS

### group `az identitysignins datapolicyoperationsdatapolicyoperation`
#### <a name="dataPolicyOperations.dataPolicyOperationCreateDataPolicyOperation">Command `az identitysignins datapolicyoperationsdatapolicyoperation create-data-policy-operation`</a>

##### <a name="ParametersdataPolicyOperations.dataPolicyOperationCreateDataPolicyOperation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--completed-date-time**|date-time|Represents when the request for this data policy operation was completed, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Null until the operation completes.|completed_date_time|completedDateTime|
|**--progress**|number|Specifies the progress of an operation.|progress|progress|
|**--status**|choice||status|status|
|**--storage-location**|string|The URL location to where data is being exported for export requests.|storage_location|storageLocation|
|**--submitted-date-time**|date-time|Represents when the request for this data operation was submitted, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|submitted_date_time|submittedDateTime|
|**--user-id**|string|The id for the user on whom the operation is performed.|user_id|userId|

#### <a name="dataPolicyOperations.dataPolicyOperationDeleteDataPolicyOperation">Command `az identitysignins datapolicyoperationsdatapolicyoperation delete-data-policy-operation`</a>

##### <a name="ParametersdataPolicyOperations.dataPolicyOperationDeleteDataPolicyOperation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--data-policy-operation-id**|string|key: id of dataPolicyOperation|data_policy_operation_id|dataPolicyOperation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="dataPolicyOperations.dataPolicyOperationListDataPolicyOperation">Command `az identitysignins datapolicyoperationsdatapolicyoperation list-data-policy-operation`</a>

##### <a name="ParametersdataPolicyOperations.dataPolicyOperationListDataPolicyOperation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="dataPolicyOperations.dataPolicyOperationGetDataPolicyOperation">Command `az identitysignins datapolicyoperationsdatapolicyoperation show-data-policy-operation`</a>

##### <a name="ParametersdataPolicyOperations.dataPolicyOperationGetDataPolicyOperation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--data-policy-operation-id**|string|key: id of dataPolicyOperation|data_policy_operation_id|dataPolicyOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="dataPolicyOperations.dataPolicyOperationUpdateDataPolicyOperation">Command `az identitysignins datapolicyoperationsdatapolicyoperation update-data-policy-operation`</a>

##### <a name="ParametersdataPolicyOperations.dataPolicyOperationUpdateDataPolicyOperation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--data-policy-operation-id**|string|key: id of dataPolicyOperation|data_policy_operation_id|dataPolicyOperation-id|
|**--id**|string|Read-only.|id|id|
|**--completed-date-time**|date-time|Represents when the request for this data policy operation was completed, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Null until the operation completes.|completed_date_time|completedDateTime|
|**--progress**|number|Specifies the progress of an operation.|progress|progress|
|**--status**|choice||status|status|
|**--storage-location**|string|The URL location to where data is being exported for export requests.|storage_location|storageLocation|
|**--submitted-date-time**|date-time|Represents when the request for this data operation was submitted, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|submitted_date_time|submittedDateTime|
|**--user-id**|string|The id for the user on whom the operation is performed.|user_id|userId|

### group `az identitysignins identity`
#### <a name="identityCreateUserFlows">Command `az identitysignins identity create-user-flow`</a>

##### <a name="ParametersidentityCreateUserFlows">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--user-flow-type**|choice||user_flow_type|userFlowType|
|**--user-flow-type-version**|number||user_flow_type_version|userFlowTypeVersion|

#### <a name="identityDeleteConditionalAccess">Command `az identitysignins identity delete-conditional-access`</a>

##### <a name="ParametersidentityDeleteConditionalAccess">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="identityDeleteUserFlows">Command `az identitysignins identity delete-user-flow`</a>

##### <a name="ParametersidentityDeleteUserFlows">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-user-flow-id**|string|key: id of identityUserFlow|identity_user_flow_id|identityUserFlow-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="identityListUserFlows">Command `az identitysignins identity list-user-flow`</a>

##### <a name="ParametersidentityListUserFlows">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identityGetConditionalAccess">Command `az identitysignins identity show-conditional-access`</a>

##### <a name="ParametersidentityGetConditionalAccess">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identityGetUserFlows">Command `az identitysignins identity show-user-flow`</a>

##### <a name="ParametersidentityGetUserFlows">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-user-flow-id**|string|key: id of identityUserFlow|identity_user_flow_id|identityUserFlow-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identityUpdateConditionalAccess">Command `az identitysignins identity update-conditional-access`</a>

##### <a name="ParametersidentityUpdateConditionalAccess">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--named-locations**|array||named_locations|namedLocations|
|**--policies**|array||policies|policies|

#### <a name="identityUpdateUserFlows">Command `az identitysignins identity update-user-flow`</a>

##### <a name="ParametersidentityUpdateUserFlows">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-user-flow-id**|string|key: id of identityUserFlow|identity_user_flow_id|identityUserFlow-id|
|**--id**|string|Read-only.|id|id|
|**--user-flow-type**|choice||user_flow_type|userFlowType|
|**--user-flow-type-version**|number||user_flow_type_version|userFlowTypeVersion|

### group `az identitysignins identityconditionalaccess`
#### <a name="identity.conditionalAccessCreateNamedLocations">Command `az identitysignins identityconditionalaccess create-named-location`</a>

##### <a name="Parametersidentity.conditionalAccessCreateNamedLocations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents creation date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|Human-readable name of the location.|display_name|displayName|
|**--modified-date-time**|date-time|The Timestamp type represents last modified date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|modified_date_time|modifiedDateTime|

#### <a name="identity.conditionalAccessCreatePolicies">Command `az identitysignins identityconditionalaccess create-policy`</a>

##### <a name="Parametersidentity.conditionalAccessCreatePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|created_date_time|createdDateTime|
|**--description**|string||description|description|
|**--display-name**|string|Specifies a display name for the conditionalAccessPolicy object.|display_name|displayName|
|**--grant-controls**|object|conditionalAccessGrantControls|grant_controls|grantControls|
|**--modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|modified_date_time|modifiedDateTime|
|**--state**|choice||state|state|
|**--application-enforced-restrictions**|object|applicationEnforcedRestrictionsSessionControl|application_enforced_restrictions|applicationEnforcedRestrictions|
|**--cloud-app-security**|object|cloudAppSecuritySessionControl|cloud_app_security|cloudAppSecurity|
|**--persistent-browser**|object|persistentBrowserSessionControl|persistent_browser|persistentBrowser|
|**--sign-in-frequency**|object|signInFrequencySessionControl|sign_in_frequency|signInFrequency|
|**--applications**|object|conditionalAccessApplications|applications|applications|
|**--client-applications**|object|conditionalAccessClientApplications|client_applications|clientApplications|
|**--client-app-types**|array|Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other.|client_app_types|clientAppTypes|
|**--devices**|object|conditionalAccessDevices|devices|devices|
|**--device-states**|object|conditionalAccessDeviceStates|device_states|deviceStates|
|**--locations**|object|conditionalAccessLocations|locations|locations|
|**--platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--sign-in-risk-levels**|array|Risk levels included in the policy. Possible values are: low, medium, high, none.|sign_in_risk_levels|signInRiskLevels|
|**--user-risk-levels**|array||user_risk_levels|userRiskLevels|
|**--users**|object|conditionalAccessUsers|users|users|

#### <a name="identity.conditionalAccessDeleteNamedLocations">Command `az identitysignins identityconditionalaccess delete-named-location`</a>

##### <a name="Parametersidentity.conditionalAccessDeleteNamedLocations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--named-location-id**|string|key: id of namedLocation|named_location_id|namedLocation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="identity.conditionalAccessDeletePolicies">Command `az identitysignins identityconditionalaccess delete-policy`</a>

##### <a name="Parametersidentity.conditionalAccessDeletePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--conditional-access-policy-id**|string|key: id of conditionalAccessPolicy|conditional_access_policy_id|conditionalAccessPolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="identity.conditionalAccessListNamedLocations">Command `az identitysignins identityconditionalaccess list-named-location`</a>

##### <a name="Parametersidentity.conditionalAccessListNamedLocations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identity.conditionalAccessListPolicies">Command `az identitysignins identityconditionalaccess list-policy`</a>

##### <a name="Parametersidentity.conditionalAccessListPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identity.conditionalAccessGetNamedLocations">Command `az identitysignins identityconditionalaccess show-named-location`</a>

##### <a name="Parametersidentity.conditionalAccessGetNamedLocations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--named-location-id**|string|key: id of namedLocation|named_location_id|namedLocation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identity.conditionalAccessGetPolicies">Command `az identitysignins identityconditionalaccess show-policy`</a>

##### <a name="Parametersidentity.conditionalAccessGetPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--conditional-access-policy-id**|string|key: id of conditionalAccessPolicy|conditional_access_policy_id|conditionalAccessPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identity.conditionalAccessUpdateNamedLocations">Command `az identitysignins identityconditionalaccess update-named-location`</a>

##### <a name="Parametersidentity.conditionalAccessUpdateNamedLocations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--named-location-id**|string|key: id of namedLocation|named_location_id|namedLocation-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents creation date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|Human-readable name of the location.|display_name|displayName|
|**--modified-date-time**|date-time|The Timestamp type represents last modified date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|modified_date_time|modifiedDateTime|

#### <a name="identity.conditionalAccessUpdatePolicies">Command `az identitysignins identityconditionalaccess update-policy`</a>

##### <a name="Parametersidentity.conditionalAccessUpdatePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--conditional-access-policy-id**|string|key: id of conditionalAccessPolicy|conditional_access_policy_id|conditionalAccessPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|created_date_time|createdDateTime|
|**--description**|string||description|description|
|**--display-name**|string|Specifies a display name for the conditionalAccessPolicy object.|display_name|displayName|
|**--grant-controls**|object|conditionalAccessGrantControls|grant_controls|grantControls|
|**--modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|modified_date_time|modifiedDateTime|
|**--state**|choice||state|state|
|**--application-enforced-restrictions**|object|applicationEnforcedRestrictionsSessionControl|application_enforced_restrictions|applicationEnforcedRestrictions|
|**--cloud-app-security**|object|cloudAppSecuritySessionControl|cloud_app_security|cloudAppSecurity|
|**--persistent-browser**|object|persistentBrowserSessionControl|persistent_browser|persistentBrowser|
|**--sign-in-frequency**|object|signInFrequencySessionControl|sign_in_frequency|signInFrequency|
|**--applications**|object|conditionalAccessApplications|applications|applications|
|**--client-applications**|object|conditionalAccessClientApplications|client_applications|clientApplications|
|**--client-app-types**|array|Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other.|client_app_types|clientAppTypes|
|**--devices**|object|conditionalAccessDevices|devices|devices|
|**--device-states**|object|conditionalAccessDeviceStates|device_states|deviceStates|
|**--locations**|object|conditionalAccessLocations|locations|locations|
|**--platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--sign-in-risk-levels**|array|Risk levels included in the policy. Possible values are: low, medium, high, none.|sign_in_risk_levels|signInRiskLevels|
|**--user-risk-levels**|array||user_risk_levels|userRiskLevels|
|**--users**|object|conditionalAccessUsers|users|users|

### group `az identitysignins identityprovider`
#### <a name="identityProvidersavailableProviderTypes">Command `az identitysignins identityprovider available-provider-type`</a>

##### <a name="ParametersidentityProvidersavailableProviderTypes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
### group `az identitysignins identityprovidersidentityprovider`
#### <a name="identityProviders.identityProviderCreateIdentityProvider">Command `az identitysignins identityprovidersidentityprovider create-identity-provider`</a>

##### <a name="ParametersidentityProviders.identityProviderCreateIdentityProvider">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--client-id**|string||client_id|clientId|
|**--client-secret**|string||client_secret|clientSecret|
|**--name**|string||name|name|
|**--type**|string||type|type|

#### <a name="identityProviders.identityProviderDeleteIdentityProvider">Command `az identitysignins identityprovidersidentityprovider delete-identity-provider`</a>

##### <a name="ParametersidentityProviders.identityProviderDeleteIdentityProvider">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-provider-id**|string|key: id of identityProvider|identity_provider_id|identityProvider-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="identityProviders.identityProviderListIdentityProvider">Command `az identitysignins identityprovidersidentityprovider list-identity-provider`</a>

##### <a name="ParametersidentityProviders.identityProviderListIdentityProvider">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identityProviders.identityProviderGetIdentityProvider">Command `az identitysignins identityprovidersidentityprovider show-identity-provider`</a>

##### <a name="ParametersidentityProviders.identityProviderGetIdentityProvider">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-provider-id**|string|key: id of identityProvider|identity_provider_id|identityProvider-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identityProviders.identityProviderUpdateIdentityProvider">Command `az identitysignins identityprovidersidentityprovider update-identity-provider`</a>

##### <a name="ParametersidentityProviders.identityProviderUpdateIdentityProvider">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-provider-id**|string|key: id of identityProvider|identity_provider_id|identityProvider-id|
|**--id**|string|Read-only.|id|id|
|**--client-id**|string||client_id|clientId|
|**--client-secret**|string||client_secret|clientSecret|
|**--name**|string||name|name|
|**--type**|string||type|type|

### group `az identitysignins informationprotection`
#### <a name="informationProtection.informationProtectionGetInformationProtection">Command `az identitysignins informationprotection show-information-protection`</a>

##### <a name="ParametersinformationProtection.informationProtectionGetInformationProtection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtection.informationProtectionUpdateInformationProtection">Command `az identitysignins informationprotection update-information-protection`</a>

##### <a name="ParametersinformationProtection.informationProtectionUpdateInformationProtection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--data-loss-prevention-policies**|array||data_loss_prevention_policies|dataLossPreventionPolicies|
|**--sensitivity-labels**|array||sensitivity_labels|sensitivityLabels|
|**--sensitivity-policy-settings**|object|sensitivityPolicySettings|sensitivity_policy_settings|sensitivityPolicySettings|
|**--threat-assessment-requests**|array||threat_assessment_requests|threatAssessmentRequests|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--labels**|array||labels|labels|

### group `az identitysignins informationprotection`
#### <a name="informationProtectionCreateDataLossPreventionPolicies">Command `az identitysignins informationprotection create-data-loss-prevention-policy`</a>

##### <a name="ParametersinformationProtectionCreateDataLossPreventionPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--name**|string||name|name|

#### <a name="informationProtectionCreateSensitivityLabels">Command `az identitysignins informationprotection create-sensitivity-label`</a>

##### <a name="ParametersinformationProtectionCreateSensitivityLabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--applicable-to**|choice||applicable_to|applicableTo|
|**--application-mode**|choice||application_mode|applicationMode|
|**--assigned-policies**|array||assigned_policies|assignedPolicies|
|**--auto-labeling**|object|autoLabeling|auto_labeling|autoLabeling|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--is-default**|boolean||is_default|isDefault|
|**--is-endpoint-protection-enabled**|boolean||is_endpoint_protection_enabled|isEndpointProtectionEnabled|
|**--label-actions**|array||label_actions|labelActions|
|**--name**|string||name|name|
|**--priority**|integer||priority|priority|
|**--tool-tip**|string||tool_tip|toolTip|
|**--sublabels**|array||sublabels|sublabels|

#### <a name="informationProtectionCreateThreatAssessmentRequests">Command `az identitysignins informationprotection create-threat-assessment-request`</a>

##### <a name="ParametersinformationProtectionCreateThreatAssessmentRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--category**|choice||category|category|
|**--content-type**|choice||content_type|contentType|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--expected-assessment**|choice||expected_assessment|expectedAssessment|
|**--request-source**|choice||request_source|requestSource|
|**--status**|choice||status|status|
|**--results**|array|A collection of threat assessment results. Read-only. By default, a GET /threatAssessmentRequests/{id} does not return this property unless you apply $expand on it.|results|results|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="informationProtectionDeleteDataLossPreventionPolicies">Command `az identitysignins informationprotection delete-data-loss-prevention-policy`</a>

##### <a name="ParametersinformationProtectionDeleteDataLossPreventionPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--data-loss-prevention-policy-id**|string|key: id of dataLossPreventionPolicy|data_loss_prevention_policy_id|dataLossPreventionPolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="informationProtectionDeletePolicy">Command `az identitysignins informationprotection delete-policy`</a>

##### <a name="ParametersinformationProtectionDeletePolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="informationProtectionDeleteSensitivityLabels">Command `az identitysignins informationprotection delete-sensitivity-label`</a>

##### <a name="ParametersinformationProtectionDeleteSensitivityLabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="informationProtectionDeleteSensitivityPolicySettings">Command `az identitysignins informationprotection delete-sensitivity-policy-setting`</a>

##### <a name="ParametersinformationProtectionDeleteSensitivityPolicySettings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="informationProtectionDeleteThreatAssessmentRequests">Command `az identitysignins informationprotection delete-threat-assessment-request`</a>

##### <a name="ParametersinformationProtectionDeleteThreatAssessmentRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="informationProtectionevaluateLabelsAndPolicies">Command `az identitysignins informationprotection evaluate-label-and-policy`</a>

##### <a name="ParametersinformationProtectionevaluateLabelsAndPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--classify-text**|object|textClassificationRequest|classify_text|classifyText|
|**--evaluation-input**|object|dlpEvaluationInput|evaluation_input|evaluationInput|
|**--notification-info**|object|dlpNotification|notification_info|notificationInfo|
|**--target**|string||target|target|
|**--current-label**|object|currentLabel|current_label|currentLabel|
|**--discovered-sensitive-types**|array||discovered_sensitive_types|discoveredSensitiveTypes|

#### <a name="informationProtectionListDataLossPreventionPolicies">Command `az identitysignins informationprotection list-data-loss-prevention-policy`</a>

##### <a name="ParametersinformationProtectionListDataLossPreventionPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtectionListSensitivityLabels">Command `az identitysignins informationprotection list-sensitivity-label`</a>

##### <a name="ParametersinformationProtectionListSensitivityLabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtectionListThreatAssessmentRequests">Command `az identitysignins informationprotection list-threat-assessment-request`</a>

##### <a name="ParametersinformationProtectionListThreatAssessmentRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtectionGetDataLossPreventionPolicies">Command `az identitysignins informationprotection show-data-loss-prevention-policy`</a>

##### <a name="ParametersinformationProtectionGetDataLossPreventionPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--data-loss-prevention-policy-id**|string|key: id of dataLossPreventionPolicy|data_loss_prevention_policy_id|dataLossPreventionPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtectionGetPolicy">Command `az identitysignins informationprotection show-policy`</a>

##### <a name="ParametersinformationProtectionGetPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtectionGetSensitivityLabels">Command `az identitysignins informationprotection show-sensitivity-label`</a>

##### <a name="ParametersinformationProtectionGetSensitivityLabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtectionGetSensitivityPolicySettings">Command `az identitysignins informationprotection show-sensitivity-policy-setting`</a>

##### <a name="ParametersinformationProtectionGetSensitivityPolicySettings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtectionGetThreatAssessmentRequests">Command `az identitysignins informationprotection show-threat-assessment-request`</a>

##### <a name="ParametersinformationProtectionGetThreatAssessmentRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtectionUpdateDataLossPreventionPolicies">Command `az identitysignins informationprotection update-data-loss-prevention-policy`</a>

##### <a name="ParametersinformationProtectionUpdateDataLossPreventionPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--data-loss-prevention-policy-id**|string|key: id of dataLossPreventionPolicy|data_loss_prevention_policy_id|dataLossPreventionPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string||name|name|

#### <a name="informationProtectionUpdatePolicy">Command `az identitysignins informationprotection update-policy`</a>

##### <a name="ParametersinformationProtectionUpdatePolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--labels**|array||labels|labels|

#### <a name="informationProtectionUpdateSensitivityLabels">Command `az identitysignins informationprotection update-sensitivity-label`</a>

##### <a name="ParametersinformationProtectionUpdateSensitivityLabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--id**|string|Read-only.|id|id|
|**--applicable-to**|choice||applicable_to|applicableTo|
|**--application-mode**|choice||application_mode|applicationMode|
|**--assigned-policies**|array||assigned_policies|assignedPolicies|
|**--auto-labeling**|object|autoLabeling|auto_labeling|autoLabeling|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--is-default**|boolean||is_default|isDefault|
|**--is-endpoint-protection-enabled**|boolean||is_endpoint_protection_enabled|isEndpointProtectionEnabled|
|**--label-actions**|array||label_actions|labelActions|
|**--name**|string||name|name|
|**--priority**|integer||priority|priority|
|**--tool-tip**|string||tool_tip|toolTip|
|**--sublabels**|array||sublabels|sublabels|

#### <a name="informationProtectionUpdateSensitivityPolicySettings">Command `az identitysignins informationprotection update-sensitivity-policy-setting`</a>

##### <a name="ParametersinformationProtectionUpdateSensitivityPolicySettings">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--applicable-to**|choice||applicable_to|applicableTo|
|**--downgrade-sensitivity-requires-justification**|boolean||downgrade_sensitivity_requires_justification|downgradeSensitivityRequiresJustification|
|**--help-web-url**|string||help_web_url|helpWebUrl|
|**--is-mandatory**|boolean||is_mandatory|isMandatory|

#### <a name="informationProtectionUpdateThreatAssessmentRequests">Command `az identitysignins informationprotection update-threat-assessment-request`</a>

##### <a name="ParametersinformationProtectionUpdateThreatAssessmentRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--id**|string|Read-only.|id|id|
|**--category**|choice||category|category|
|**--content-type**|choice||content_type|contentType|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--expected-assessment**|choice||expected_assessment|expectedAssessment|
|**--request-source**|choice||request_source|requestSource|
|**--status**|choice||status|status|
|**--results**|array|A collection of threat assessment results. Read-only. By default, a GET /threatAssessmentRequests/{id} does not return this property unless you apply $expand on it.|results|results|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

### group `az identitysignins informationprotectiondatalosspreventionpolicy`
#### <a name="informationProtection.dataLossPreventionPoliciesevaluate">Command `az identitysignins informationprotectiondatalosspreventionpolicy evaluate`</a>

##### <a name="ParametersinformationProtection.dataLossPreventionPoliciesevaluate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--target**|string||target|target|
|**--author**|string||author|author|
|**--access-scope**|choice||access_scope|accessScope|
|**--current-label**|object|currentLabel|current_label|currentLabel|
|**--discovered-sensitive-types**|array||discovered_sensitive_types|discoveredSensitiveTypes|

### group `az identitysignins informationprotectionpolicy`
#### <a name="informationProtection.policyCreateLabels">Command `az identitysignins informationprotectionpolicy create-label`</a>

##### <a name="ParametersinformationProtection.policyCreateLabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--color**|string||color|color|
|**--description**|string||description|description|
|**--is-active**|boolean||is_active|isActive|
|**--name**|string||name|name|
|**--parent**|object|parentLabelDetails|parent|parent|
|**--sensitivity**|integer||sensitivity|sensitivity|
|**--tooltip**|string||tooltip|tooltip|

#### <a name="informationProtection.policyDeleteLabels">Command `az identitysignins informationprotectionpolicy delete-label`</a>

##### <a name="ParametersinformationProtection.policyDeleteLabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--information-protection-label-id**|string|key: id of informationProtectionLabel|information_protection_label_id|informationProtectionLabel-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="informationProtection.policyListLabels">Command `az identitysignins informationprotectionpolicy list-label`</a>

##### <a name="ParametersinformationProtection.policyListLabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtection.policyGetLabels">Command `az identitysignins informationprotectionpolicy show-label`</a>

##### <a name="ParametersinformationProtection.policyGetLabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--information-protection-label-id**|string|key: id of informationProtectionLabel|information_protection_label_id|informationProtectionLabel-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtection.policyUpdateLabels">Command `az identitysignins informationprotectionpolicy update-label`</a>

##### <a name="ParametersinformationProtection.policyUpdateLabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--information-protection-label-id**|string|key: id of informationProtectionLabel|information_protection_label_id|informationProtectionLabel-id|
|**--id**|string|Read-only.|id|id|
|**--color**|string||color|color|
|**--description**|string||description|description|
|**--is-active**|boolean||is_active|isActive|
|**--name**|string||name|name|
|**--parent**|object|parentLabelDetails|parent|parent|
|**--sensitivity**|integer||sensitivity|sensitivity|
|**--tooltip**|string||tooltip|tooltip|

### group `az identitysignins informationprotectionpolicylabel`
#### <a name="informationProtection.policy.labelsevaluateApplication">Command `az identitysignins informationprotectionpolicylabel evaluate-application`</a>

##### <a name="ParametersinformationProtection.policy.labelsevaluateApplication">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--assignment-method**|choice||assignment_method|assignmentMethod|
|**--downgrade-justification**|object|downgradeJustification|downgrade_justification|downgradeJustification|
|**--extended-properties**|array||extended_properties|extendedProperties|
|**--label-id**|uuid||label_id|labelId|
|**--format**|choice||format|format|
|**--identifier**|string||identifier|identifier|
|**--metadata**|array||metadata|metadata|
|**--state**|choice||state|state|

#### <a name="informationProtection.policy.labelsevaluateClassificationResults">Command `az identitysignins informationprotectionpolicylabel evaluate-classification-result`</a>

##### <a name="ParametersinformationProtection.policy.labelsevaluateClassificationResults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--classification-results**|array||classification_results|classificationResults|
|**--format**|choice||format|format|
|**--identifier**|string||identifier|identifier|
|**--metadata**|array||metadata|metadata|
|**--state**|choice||state|state|

#### <a name="informationProtection.policy.labelsevaluateRemoval">Command `az identitysignins informationprotectionpolicylabel evaluate-removal`</a>

##### <a name="ParametersinformationProtection.policy.labelsevaluateRemoval">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--downgrade-justification**|object|downgradeJustification|downgrade_justification|downgradeJustification|
|**--format**|choice||format|format|
|**--identifier**|string||identifier|identifier|
|**--metadata**|array||metadata|metadata|
|**--state**|choice||state|state|

#### <a name="informationProtection.policy.labelsextractLabel">Command `az identitysignins informationprotectionpolicylabel extract-label`</a>

##### <a name="ParametersinformationProtection.policy.labelsextractLabel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--format**|choice||format|format|
|**--identifier**|string||identifier|identifier|
|**--metadata**|array||metadata|metadata|
|**--state**|choice||state|state|

### group `az identitysignins informationprotectionsensitivitylabel`
#### <a name="informationProtection.sensitivityLabelsCreateSublabels">Command `az identitysignins informationprotectionsensitivitylabel create-sublabel`</a>

##### <a name="ParametersinformationProtection.sensitivityLabelsCreateSublabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--id**|string|Read-only.|id|id|
|**--applicable-to**|choice||applicable_to|applicableTo|
|**--application-mode**|choice||application_mode|applicationMode|
|**--assigned-policies**|array||assigned_policies|assignedPolicies|
|**--auto-labeling**|object|autoLabeling|auto_labeling|autoLabeling|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--is-default**|boolean||is_default|isDefault|
|**--is-endpoint-protection-enabled**|boolean||is_endpoint_protection_enabled|isEndpointProtectionEnabled|
|**--label-actions**|array||label_actions|labelActions|
|**--name**|string||name|name|
|**--priority**|integer||priority|priority|
|**--tool-tip**|string||tool_tip|toolTip|
|**--sublabels**|array||sublabels|sublabels|

#### <a name="informationProtection.sensitivityLabelsDeleteSublabels">Command `az identitysignins informationprotectionsensitivitylabel delete-sublabel`</a>

##### <a name="ParametersinformationProtection.sensitivityLabelsDeleteSublabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--sensitivity-label-id1**|string|key: id of sensitivityLabel|sensitivity_label_id1|sensitivityLabel-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="informationProtection.sensitivityLabelsevaluate">Command `az identitysignins informationprotectionsensitivitylabel evaluate`</a>

##### <a name="ParametersinformationProtection.sensitivityLabelsevaluate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--discovered-sensitive-types**|array||discovered_sensitive_types|discoveredSensitiveTypes|
|**--current-label**|object|currentLabel|current_label|currentLabel|

#### <a name="informationProtection.sensitivityLabelsListSublabels">Command `az identitysignins informationprotectionsensitivitylabel list-sublabel`</a>

##### <a name="ParametersinformationProtection.sensitivityLabelsListSublabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtection.sensitivityLabelsGetSublabels">Command `az identitysignins informationprotectionsensitivitylabel show-sublabel`</a>

##### <a name="ParametersinformationProtection.sensitivityLabelsGetSublabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--sensitivity-label-id1**|string|key: id of sensitivityLabel|sensitivity_label_id1|sensitivityLabel-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtection.sensitivityLabelsUpdateSublabels">Command `az identitysignins informationprotectionsensitivitylabel update-sublabel`</a>

##### <a name="ParametersinformationProtection.sensitivityLabelsUpdateSublabels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--sensitivity-label-id1**|string|key: id of sensitivityLabel|sensitivity_label_id1|sensitivityLabel-id1|
|**--id**|string|Read-only.|id|id|
|**--applicable-to**|choice||applicable_to|applicableTo|
|**--application-mode**|choice||application_mode|applicationMode|
|**--assigned-policies**|array||assigned_policies|assignedPolicies|
|**--auto-labeling**|object|autoLabeling|auto_labeling|autoLabeling|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--is-default**|boolean||is_default|isDefault|
|**--is-endpoint-protection-enabled**|boolean||is_endpoint_protection_enabled|isEndpointProtectionEnabled|
|**--label-actions**|array||label_actions|labelActions|
|**--name**|string||name|name|
|**--priority**|integer||priority|priority|
|**--tool-tip**|string||tool_tip|toolTip|
|**--sublabels**|array||sublabels|sublabels|

### group `az identitysignins informationprotectionsensitivitylabelssublabel`
#### <a name="informationProtection.sensitivityLabels.sublabelsevaluate">Command `az identitysignins informationprotectionsensitivitylabelssublabel evaluate`</a>

##### <a name="ParametersinformationProtection.sensitivityLabels.sublabelsevaluate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--sensitivity-label-id**|string|key: id of sensitivityLabel|sensitivity_label_id|sensitivityLabel-id|
|**--discovered-sensitive-types**|array||discovered_sensitive_types|discoveredSensitiveTypes|
|**--current-label**|object|currentLabel|current_label|currentLabel|

### group `az identitysignins informationprotectionthreatassessmentrequest`
#### <a name="informationProtection.threatAssessmentRequestsCreateResults">Command `az identitysignins informationprotectionthreatassessmentrequest create-result`</a>

##### <a name="ParametersinformationProtection.threatAssessmentRequestsCreateResults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--message**|string|The result message for each threat assessment.|message|message|
|**--result-type**|choice||result_type|resultType|

#### <a name="informationProtection.threatAssessmentRequestsDeleteResults">Command `az identitysignins informationprotectionthreatassessmentrequest delete-result`</a>

##### <a name="ParametersinformationProtection.threatAssessmentRequestsDeleteResults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--threat-assessment-result-id**|string|key: id of threatAssessmentResult|threat_assessment_result_id|threatAssessmentResult-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="informationProtection.threatAssessmentRequestsListResults">Command `az identitysignins informationprotectionthreatassessmentrequest list-result`</a>

##### <a name="ParametersinformationProtection.threatAssessmentRequestsListResults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtection.threatAssessmentRequestsGetResults">Command `az identitysignins informationprotectionthreatassessmentrequest show-result`</a>

##### <a name="ParametersinformationProtection.threatAssessmentRequestsGetResults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--threat-assessment-result-id**|string|key: id of threatAssessmentResult|threat_assessment_result_id|threatAssessmentResult-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtection.threatAssessmentRequestsUpdateResults">Command `az identitysignins informationprotectionthreatassessmentrequest update-result`</a>

##### <a name="ParametersinformationProtection.threatAssessmentRequestsUpdateResults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--threat-assessment-result-id**|string|key: id of threatAssessmentResult|threat_assessment_result_id|threatAssessmentResult-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--message**|string|The result message for each threat assessment.|message|message|
|**--result-type**|choice||result_type|resultType|

### group `az identitysignins invitation`
#### <a name="invitationsDeleteRefInvitedUser">Command `az identitysignins invitation delete-ref-invited-user`</a>

##### <a name="ParametersinvitationsDeleteRefInvitedUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: id of invitation|invitation_id|invitation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="invitationsSetRefInvitedUser">Command `az identitysignins invitation set-ref-invited-user`</a>

##### <a name="ParametersinvitationsSetRefInvitedUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: id of invitation|invitation_id|invitation-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="invitationsGetInvitedUser">Command `az identitysignins invitation show-invited-user`</a>

##### <a name="ParametersinvitationsGetInvitedUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: id of invitation|invitation_id|invitation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="invitationsGetRefInvitedUser">Command `az identitysignins invitation show-ref-invited-user`</a>

##### <a name="ParametersinvitationsGetRefInvitedUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: id of invitation|invitation_id|invitation-id|

### group `az identitysignins invitationsinvitation`
#### <a name="invitations.invitationCreateInvitation">Command `az identitysignins invitationsinvitation create-invitation`</a>

##### <a name="Parametersinvitations.invitationCreateInvitation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--invited-user-display-name**|string|The display name of the user being invited.|invited_user_display_name|invitedUserDisplayName|
|**--invited-user-email-address**|string|The email address of the user being invited. Required. The following special characters are not permitted in the email address:Tilde (~)Exclamation point (!)Number sign (#)Dollar sign ($)Percent (%)Circumflex (^)Ampersand (&)Asterisk (*)Parentheses (( ))Plus sign (+)Equal sign (=)Brackets ([ ])Braces ({ })Backslash (/)Slash mark (/)Pipe (/|)Semicolon (;)Colon (:)Quotation marks (')Angle brackets (< >)Question mark (?)Comma (,)However, the following exceptions apply:A period (.) or a hyphen (-) is permitted anywhere in the user name, except at the beginning or end of the name.An underscore (_) is permitted anywhere in the user name. This includes at the beginning or end of the name.|invited_user_email_address|invitedUserEmailAddress|
|**--invited-user-type**|string|The userType of the user being invited. By default, this is Guest. You can invite as Member if you are a company administrator.|invited_user_type|invitedUserType|
|**--invite-redeem-url**|string|The URL the user can use to redeem their invitation. Read-only|invite_redeem_url|inviteRedeemUrl|
|**--invite-redirect-url**|string|The URL the user should be redirected to once the invitation is redeemed. Required.|invite_redirect_url|inviteRedirectUrl|
|**--reset-redemption**|boolean||reset_redemption|resetRedemption|
|**--send-invitation-message**|boolean|Indicates whether an email should be sent to the user being invited or not. The default is false.|send_invitation_message|sendInvitationMessage|
|**--status**|string|The status of the invitation. Possible values: PendingAcceptance, Completed, InProgress, and Error|status|status|
|**--invited-user**|object|Represents an Azure Active Directory user object.|invited_user|invitedUser|
|**--cc-recipients**|array|Additional recipients the invitation message should be sent to. Currently only 1 additional recipient is supported.|cc_recipients|ccRecipients|
|**--customized-message-body**|string|Customized message body you want to send if you don't want the default message.|customized_message_body|customizedMessageBody|
|**--message-language**|string|The language you want to send the default message in. If the customizedMessageBody is specified, this property is ignored, and the message is sent using the customizedMessageBody. The language format should be in ISO 639. The default is en-US.|message_language|messageLanguage|

#### <a name="invitations.invitationDeleteInvitation">Command `az identitysignins invitationsinvitation delete-invitation`</a>

##### <a name="Parametersinvitations.invitationDeleteInvitation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: id of invitation|invitation_id|invitation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="invitations.invitationListInvitation">Command `az identitysignins invitationsinvitation list-invitation`</a>

##### <a name="Parametersinvitations.invitationListInvitation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="invitations.invitationGetInvitation">Command `az identitysignins invitationsinvitation show-invitation`</a>

##### <a name="Parametersinvitations.invitationGetInvitation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: id of invitation|invitation_id|invitation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="invitations.invitationUpdateInvitation">Command `az identitysignins invitationsinvitation update-invitation`</a>

##### <a name="Parametersinvitations.invitationUpdateInvitation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: id of invitation|invitation_id|invitation-id|
|**--id**|string|Read-only.|id|id|
|**--invited-user-display-name**|string|The display name of the user being invited.|invited_user_display_name|invitedUserDisplayName|
|**--invited-user-email-address**|string|The email address of the user being invited. Required. The following special characters are not permitted in the email address:Tilde (~)Exclamation point (!)Number sign (#)Dollar sign ($)Percent (%)Circumflex (^)Ampersand (&)Asterisk (*)Parentheses (( ))Plus sign (+)Equal sign (=)Brackets ([ ])Braces ({ })Backslash (/)Slash mark (/)Pipe (/|)Semicolon (;)Colon (:)Quotation marks (')Angle brackets (< >)Question mark (?)Comma (,)However, the following exceptions apply:A period (.) or a hyphen (-) is permitted anywhere in the user name, except at the beginning or end of the name.An underscore (_) is permitted anywhere in the user name. This includes at the beginning or end of the name.|invited_user_email_address|invitedUserEmailAddress|
|**--invited-user-type**|string|The userType of the user being invited. By default, this is Guest. You can invite as Member if you are a company administrator.|invited_user_type|invitedUserType|
|**--invite-redeem-url**|string|The URL the user can use to redeem their invitation. Read-only|invite_redeem_url|inviteRedeemUrl|
|**--invite-redirect-url**|string|The URL the user should be redirected to once the invitation is redeemed. Required.|invite_redirect_url|inviteRedirectUrl|
|**--reset-redemption**|boolean||reset_redemption|resetRedemption|
|**--send-invitation-message**|boolean|Indicates whether an email should be sent to the user being invited or not. The default is false.|send_invitation_message|sendInvitationMessage|
|**--status**|string|The status of the invitation. Possible values: PendingAcceptance, Completed, InProgress, and Error|status|status|
|**--invited-user**|object|Represents an Azure Active Directory user object.|invited_user|invitedUser|
|**--cc-recipients**|array|Additional recipients the invitation message should be sent to. Currently only 1 additional recipient is supported.|cc_recipients|ccRecipients|
|**--customized-message-body**|string|Customized message body you want to send if you don't want the default message.|customized_message_body|customizedMessageBody|
|**--message-language**|string|The language you want to send the default message in. If the customizedMessageBody is specified, this property is ignored, and the message is sent using the customizedMessageBody. The language format should be in ISO 639. The default is en-US.|message_language|messageLanguage|

### group `az identitysignins oauth2permissiongrant`
#### <a name="oauth2PermissionGrantsdelta">Command `az identitysignins oauth2permissiongrant delta`</a>

##### <a name="Parametersoauth2PermissionGrantsdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
### group `az identitysignins oauth2permissiongrantsoauth2permissiongrant`
#### <a name="oauth2PermissionGrants.oAuth2PermissionGrantCreateOAuth2PermissionGrant">Command `az identitysignins oauth2permissiongrantsoauth2permissiongrant create-o-auth2-permission-grant`</a>

##### <a name="Parametersoauth2PermissionGrants.oAuth2PermissionGrantCreateOAuth2PermissionGrant">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--client-id**|string|The id of the client service principal for the application which is authorized to act on behalf of a signed-in user when accessing an API. Required. Supports $filter (eq only).|client_id|clientId|
|**--consent-type**|string|Indicates if authorization is granted for the client application to impersonate all users or only a specific user. AllPrincipals indicates authorization to impersonate all users. Principal indicates authorization to impersonate a specific user. Consent on behalf of all users can be granted by an administrator. Non-admin users may be authorized to consent on behalf of themselves in some cases, for some delegated permissions. Required. Supports $filter (eq only).|consent_type|consentType|
|**--expiry-time**|date-time||expiry_time|expiryTime|
|**--principal-id**|string|The id of the user on behalf of whom the client is authorized to access the resource, when consentType is Principal. If consentType is AllPrincipals this value is null. Required when consentType is Principal.|principal_id|principalId|
|**--resource-id**|string|The id of the resource service principal to which access is authorized. This identifies the API which the client is authorized to attempt to call on behalf of a signed-in user.|resource_id|resourceId|
|**--scope**|string|A space-separated list of the claim values for delegated permissions which should be included in access tokens for the resource application (the API). For example, openid User.Read GroupMember.Read.All. Each claim value should match the value field of one of the delegated permissions defined by the API, listed in the publishedPermissionScopes property of the resource service principal.|scope|scope|
|**--start-time**|date-time||start_time|startTime|

#### <a name="oauth2PermissionGrants.oAuth2PermissionGrantDeleteOAuth2PermissionGrant">Command `az identitysignins oauth2permissiongrantsoauth2permissiongrant delete-o-auth2-permission-grant`</a>

##### <a name="Parametersoauth2PermissionGrants.oAuth2PermissionGrantDeleteOAuth2PermissionGrant">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--o-auth2-permission-grant-id**|string|key: id of oAuth2PermissionGrant|o_auth2_permission_grant_id|oAuth2PermissionGrant-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="oauth2PermissionGrants.oAuth2PermissionGrantListOAuth2PermissionGrant">Command `az identitysignins oauth2permissiongrantsoauth2permissiongrant list-o-auth2-permission-grant`</a>

##### <a name="Parametersoauth2PermissionGrants.oAuth2PermissionGrantListOAuth2PermissionGrant">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="oauth2PermissionGrants.oAuth2PermissionGrantGetOAuth2PermissionGrant">Command `az identitysignins oauth2permissiongrantsoauth2permissiongrant show-o-auth2-permission-grant`</a>

##### <a name="Parametersoauth2PermissionGrants.oAuth2PermissionGrantGetOAuth2PermissionGrant">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--o-auth2-permission-grant-id**|string|key: id of oAuth2PermissionGrant|o_auth2_permission_grant_id|oAuth2PermissionGrant-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="oauth2PermissionGrants.oAuth2PermissionGrantUpdateOAuth2PermissionGrant">Command `az identitysignins oauth2permissiongrantsoauth2permissiongrant update-o-auth2-permission-grant`</a>

##### <a name="Parametersoauth2PermissionGrants.oAuth2PermissionGrantUpdateOAuth2PermissionGrant">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--o-auth2-permission-grant-id**|string|key: id of oAuth2PermissionGrant|o_auth2_permission_grant_id|oAuth2PermissionGrant-id|
|**--id**|string|Read-only.|id|id|
|**--client-id**|string|The id of the client service principal for the application which is authorized to act on behalf of a signed-in user when accessing an API. Required. Supports $filter (eq only).|client_id|clientId|
|**--consent-type**|string|Indicates if authorization is granted for the client application to impersonate all users or only a specific user. AllPrincipals indicates authorization to impersonate all users. Principal indicates authorization to impersonate a specific user. Consent on behalf of all users can be granted by an administrator. Non-admin users may be authorized to consent on behalf of themselves in some cases, for some delegated permissions. Required. Supports $filter (eq only).|consent_type|consentType|
|**--expiry-time**|date-time||expiry_time|expiryTime|
|**--principal-id**|string|The id of the user on behalf of whom the client is authorized to access the resource, when consentType is Principal. If consentType is AllPrincipals this value is null. Required when consentType is Principal.|principal_id|principalId|
|**--resource-id**|string|The id of the resource service principal to which access is authorized. This identifies the API which the client is authorized to attempt to call on behalf of a signed-in user.|resource_id|resourceId|
|**--scope**|string|A space-separated list of the claim values for delegated permissions which should be included in access tokens for the resource application (the API). For example, openid User.Read GroupMember.Read.All. Each claim value should match the value field of one of the delegated permissions defined by the API, listed in the publishedPermissionScopes property of the resource service principal.|scope|scope|
|**--start-time**|date-time||start_time|startTime|

### group `az identitysignins organization`
#### <a name="organizationCreateRefCertificateBasedAuthConfiguration">Command `az identitysignins organization create-ref-certificate-based-auth-configuration`</a>

##### <a name="ParametersorganizationCreateRefCertificateBasedAuthConfiguration">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="organizationListCertificateBasedAuthConfiguration">Command `az identitysignins organization list-certificate-based-auth-configuration`</a>

##### <a name="ParametersorganizationListCertificateBasedAuthConfiguration">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="organizationListRefCertificateBasedAuthConfiguration">Command `az identitysignins organization list-ref-certificate-based-auth-configuration`</a>

##### <a name="ParametersorganizationListRefCertificateBasedAuthConfiguration">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--organization-id**|string|key: id of organization|organization_id|organization-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### group `az identitysignins policiespermissiongrantpolicy`
#### <a name="policies.permissionGrantPoliciesCreateExcludes">Command `az identitysignins policiespermissiongrantpolicy create-exclude`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesCreateExcludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--client-application-ids**|array||client_application_ids|clientApplicationIds|
|**--client-application-publisher-ids**|array||client_application_publisher_ids|clientApplicationPublisherIds|
|**--client-applications-from-verified-publisher-only**|boolean||client_applications_from_verified_publisher_only|clientApplicationsFromVerifiedPublisherOnly|
|**--client-application-tenant-ids**|array||client_application_tenant_ids|clientApplicationTenantIds|
|**--permission-classification**|string||permission_classification|permissionClassification|
|**--permissions**|array||permissions|permissions|
|**--permission-type**|choice||permission_type|permissionType|
|**--resource-application**|string||resource_application|resourceApplication|

#### <a name="policies.permissionGrantPoliciesCreateIncludes">Command `az identitysignins policiespermissiongrantpolicy create-include`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesCreateIncludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--client-application-ids**|array||client_application_ids|clientApplicationIds|
|**--client-application-publisher-ids**|array||client_application_publisher_ids|clientApplicationPublisherIds|
|**--client-applications-from-verified-publisher-only**|boolean||client_applications_from_verified_publisher_only|clientApplicationsFromVerifiedPublisherOnly|
|**--client-application-tenant-ids**|array||client_application_tenant_ids|clientApplicationTenantIds|
|**--permission-classification**|string||permission_classification|permissionClassification|
|**--permissions**|array||permissions|permissions|
|**--permission-type**|choice||permission_type|permissionType|
|**--resource-application**|string||resource_application|resourceApplication|

#### <a name="policies.permissionGrantPoliciesDeleteExcludes">Command `az identitysignins policiespermissiongrantpolicy delete-exclude`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesDeleteExcludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--permission-grant-condition-set-id**|string|key: id of permissionGrantConditionSet|permission_grant_condition_set_id|permissionGrantConditionSet-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policies.permissionGrantPoliciesDeleteIncludes">Command `az identitysignins policiespermissiongrantpolicy delete-include`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesDeleteIncludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--permission-grant-condition-set-id**|string|key: id of permissionGrantConditionSet|permission_grant_condition_set_id|permissionGrantConditionSet-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policies.permissionGrantPoliciesListExcludes">Command `az identitysignins policiespermissiongrantpolicy list-exclude`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesListExcludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policies.permissionGrantPoliciesListIncludes">Command `az identitysignins policiespermissiongrantpolicy list-include`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesListIncludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policies.permissionGrantPoliciesGetExcludes">Command `az identitysignins policiespermissiongrantpolicy show-exclude`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesGetExcludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--permission-grant-condition-set-id**|string|key: id of permissionGrantConditionSet|permission_grant_condition_set_id|permissionGrantConditionSet-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policies.permissionGrantPoliciesGetIncludes">Command `az identitysignins policiespermissiongrantpolicy show-include`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesGetIncludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--permission-grant-condition-set-id**|string|key: id of permissionGrantConditionSet|permission_grant_condition_set_id|permissionGrantConditionSet-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policies.permissionGrantPoliciesUpdateExcludes">Command `az identitysignins policiespermissiongrantpolicy update-exclude`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesUpdateExcludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--permission-grant-condition-set-id**|string|key: id of permissionGrantConditionSet|permission_grant_condition_set_id|permissionGrantConditionSet-id|
|**--id**|string|Read-only.|id|id|
|**--client-application-ids**|array||client_application_ids|clientApplicationIds|
|**--client-application-publisher-ids**|array||client_application_publisher_ids|clientApplicationPublisherIds|
|**--client-applications-from-verified-publisher-only**|boolean||client_applications_from_verified_publisher_only|clientApplicationsFromVerifiedPublisherOnly|
|**--client-application-tenant-ids**|array||client_application_tenant_ids|clientApplicationTenantIds|
|**--permission-classification**|string||permission_classification|permissionClassification|
|**--permissions**|array||permissions|permissions|
|**--permission-type**|choice||permission_type|permissionType|
|**--resource-application**|string||resource_application|resourceApplication|

#### <a name="policies.permissionGrantPoliciesUpdateIncludes">Command `az identitysignins policiespermissiongrantpolicy update-include`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesUpdateIncludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--permission-grant-condition-set-id**|string|key: id of permissionGrantConditionSet|permission_grant_condition_set_id|permissionGrantConditionSet-id|
|**--id**|string|Read-only.|id|id|
|**--client-application-ids**|array||client_application_ids|clientApplicationIds|
|**--client-application-publisher-ids**|array||client_application_publisher_ids|clientApplicationPublisherIds|
|**--client-applications-from-verified-publisher-only**|boolean||client_applications_from_verified_publisher_only|clientApplicationsFromVerifiedPublisherOnly|
|**--client-application-tenant-ids**|array||client_application_tenant_ids|clientApplicationTenantIds|
|**--permission-classification**|string||permission_classification|permissionClassification|
|**--permissions**|array||permissions|permissions|
|**--permission-type**|choice||permission_type|permissionType|
|**--resource-application**|string||resource_application|resourceApplication|

### group `az identitysignins policiespolicyroot`
#### <a name="policies.policyRootGetPolicyRoot">Command `az identitysignins policiespolicyroot show-policy-root`</a>

##### <a name="Parameterspolicies.policyRootGetPolicyRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policies.policyRootUpdatePolicyRoot">Command `az identitysignins policiespolicyroot update-policy-root`</a>

##### <a name="Parameterspolicies.policyRootUpdatePolicyRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--b2-c-authentication-methods-policy**|object|b2cAuthenticationMethodsPolicy|b2_c_authentication_methods_policy|b2cAuthenticationMethodsPolicy|
|**--activity-based-timeout-policies**|array||activity_based_timeout_policies|activityBasedTimeoutPolicies|
|**--authorization-policy**|array||authorization_policy|authorizationPolicy|
|**--claims-mapping-policies**|array||claims_mapping_policies|claimsMappingPolicies|
|**--home-realm-discovery-policies**|array||home_realm_discovery_policies|homeRealmDiscoveryPolicies|
|**--permission-grant-policies**|array||permission_grant_policies|permissionGrantPolicies|
|**--private-link-resource-policies**|array||private_link_resource_policies|privateLinkResourcePolicies|
|**--token-issuance-policies**|array||token_issuance_policies|tokenIssuancePolicies|
|**--token-lifetime-policies**|array||token_lifetime_policies|tokenLifetimePolicies|
|**--conditional-access-policies**|array||conditional_access_policies|conditionalAccessPolicies|
|**--identity-security-defaults-enforcement-policy**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|identity_security_defaults_enforcement_policy|identitySecurityDefaultsEnforcementPolicy|
|**--id**|string|Read-only.|id|id|
|**--apply-actions**|array||apply_actions|applyActions|
|**--auto-apply-decisions-enabled**|boolean||auto_apply_decisions_enabled|autoApplyDecisionsEnabled|
|**--default-decision**|string||default_decision|defaultDecision|
|**--default-decision-enabled**|boolean||default_decision_enabled|defaultDecisionEnabled|
|**--instance-duration-in-days**|integer||instance_duration_in_days|instanceDurationInDays|
|**--justification-required-on-approval**|boolean||justification_required_on_approval|justificationRequiredOnApproval|
|**--mail-notifications-enabled**|boolean||mail_notifications_enabled|mailNotificationsEnabled|
|**--recommendations-enabled**|boolean||recommendations_enabled|recommendationsEnabled|
|**--reminder-notifications-enabled**|boolean||reminder_notifications_enabled|reminderNotificationsEnabled|
|**--pattern**|object|recurrencePattern|pattern|pattern|
|**--range**|object|recurrenceRange|range|range|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--admin-consent-request-policy-is-enabled**|boolean||is_enabled|isEnabled|
|**--notify-reviewers**|boolean||notify_reviewers|notifyReviewers|
|**--reminders-enabled**|boolean||reminders_enabled|remindersEnabled|
|**--request-duration-in-days**|integer||request_duration_in_days|requestDurationInDays|
|**--reviewers**|array||reviewers|reviewers|
|**--version**|integer||version|version|
|**--id1**|string|Read-only.|id1|id|
|**--id2**|string|Read-only.|id2|id|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--is-enabled**|boolean||is_enabled|isEnabled|

### group `az identitysignins policy`
#### <a name="policiesCreateActivityBasedTimeoutPolicies">Command `az identitysignins policy create-activity-based-timeout-policy`</a>

##### <a name="ParameterspoliciesCreateActivityBasedTimeoutPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

#### <a name="policiesCreateAuthorizationPolicy">Command `az identitysignins policy create-authorization-policy`</a>

##### <a name="ParameterspoliciesCreateAuthorizationPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--allowed-to-sign-up-email-based-subscriptions**|boolean||allowed_to_sign_up_email_based_subscriptions|allowedToSignUpEmailBasedSubscriptions|
|**--allowed-to-use-sspr**|boolean||allowed_to_use_sspr|allowedToUseSSPR|
|**--allow-email-verified-users-to-join-organization**|boolean||allow_email_verified_users_to_join_organization|allowEmailVerifiedUsersToJoinOrganization|
|**--allow-invites-from**|choice||allow_invites_from|allowInvitesFrom|
|**--block-msol-power-shell**|boolean||block_msol_power_shell|blockMsolPowerShell|
|**--default-user-role-permissions**|object|defaultUserRolePermissions|default_user_role_permissions|defaultUserRolePermissions|
|**--enabled-preview-features**|array||enabled_preview_features|enabledPreviewFeatures|
|**--guest-user-role-id**|uuid||guest_user_role_id|guestUserRoleId|
|**--permission-grant-policy-ids-assigned-to-default-user-role**|array||permission_grant_policy_ids_assigned_to_default_user_role|permissionGrantPolicyIdsAssignedToDefaultUserRole|

#### <a name="policiesCreateClaimsMappingPolicies">Command `az identitysignins policy create-claim-mapping-policy`</a>

##### <a name="ParameterspoliciesCreateClaimsMappingPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

#### <a name="policiesCreateConditionalAccessPolicies">Command `az identitysignins policy create-conditional-access-policy`</a>

##### <a name="ParameterspoliciesCreateConditionalAccessPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|created_date_time|createdDateTime|
|**--description**|string||description|description|
|**--display-name**|string|Specifies a display name for the conditionalAccessPolicy object.|display_name|displayName|
|**--grant-controls**|object|conditionalAccessGrantControls|grant_controls|grantControls|
|**--modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|modified_date_time|modifiedDateTime|
|**--state**|choice||state|state|
|**--application-enforced-restrictions**|object|applicationEnforcedRestrictionsSessionControl|application_enforced_restrictions|applicationEnforcedRestrictions|
|**--cloud-app-security**|object|cloudAppSecuritySessionControl|cloud_app_security|cloudAppSecurity|
|**--persistent-browser**|object|persistentBrowserSessionControl|persistent_browser|persistentBrowser|
|**--sign-in-frequency**|object|signInFrequencySessionControl|sign_in_frequency|signInFrequency|
|**--applications**|object|conditionalAccessApplications|applications|applications|
|**--client-applications**|object|conditionalAccessClientApplications|client_applications|clientApplications|
|**--client-app-types**|array|Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other.|client_app_types|clientAppTypes|
|**--devices**|object|conditionalAccessDevices|devices|devices|
|**--device-states**|object|conditionalAccessDeviceStates|device_states|deviceStates|
|**--locations**|object|conditionalAccessLocations|locations|locations|
|**--platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--sign-in-risk-levels**|array|Risk levels included in the policy. Possible values are: low, medium, high, none.|sign_in_risk_levels|signInRiskLevels|
|**--user-risk-levels**|array||user_risk_levels|userRiskLevels|
|**--users**|object|conditionalAccessUsers|users|users|

#### <a name="policiesCreateHomeRealmDiscoveryPolicies">Command `az identitysignins policy create-home-realm-discovery-policy`</a>

##### <a name="ParameterspoliciesCreateHomeRealmDiscoveryPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

#### <a name="policiesCreatePermissionGrantPolicies">Command `az identitysignins policy create-permission-grant-policy`</a>

##### <a name="ParameterspoliciesCreatePermissionGrantPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--excludes**|array||excludes|excludes|
|**--includes**|array||includes|includes|

#### <a name="policiesCreatePrivateLinkResourcePolicies">Command `az identitysignins policy create-private-link-resource-policy`</a>

##### <a name="ParameterspoliciesCreatePrivateLinkResourcePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--allowed-tenant-ids**|array||allowed_tenant_ids|allowedTenantIds|
|**--arm-resource-id**|string||arm_resource_id|armResourceId|

#### <a name="policiesCreateTokenIssuancePolicies">Command `az identitysignins policy create-token-issuance-policy`</a>

##### <a name="ParameterspoliciesCreateTokenIssuancePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

#### <a name="policiesCreateTokenLifetimePolicies">Command `az identitysignins policy create-token-lifetime-policy`</a>

##### <a name="ParameterspoliciesCreateTokenLifetimePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

#### <a name="policiesDeleteActivityBasedTimeoutPolicies">Command `az identitysignins policy delete-activity-based-timeout-policy`</a>

##### <a name="ParameterspoliciesDeleteActivityBasedTimeoutPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--activity-based-timeout-policy-id**|string|key: id of activityBasedTimeoutPolicy|activity_based_timeout_policy_id|activityBasedTimeoutPolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesDeleteAdminConsentRequestPolicy">Command `az identitysignins policy delete-admin-consent-request-policy`</a>

##### <a name="ParameterspoliciesDeleteAdminConsentRequestPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesDeleteAuthenticationFlowsPolicy">Command `az identitysignins policy delete-authentication-flow-policy`</a>

##### <a name="ParameterspoliciesDeleteAuthenticationFlowsPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesDeleteAuthorizationPolicy">Command `az identitysignins policy delete-authorization-policy`</a>

##### <a name="ParameterspoliciesDeleteAuthorizationPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--authorization-policy-id**|string|key: id of authorizationPolicy|authorization_policy_id|authorizationPolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesDeleteB2cAuthenticationMethodsPolicy">Command `az identitysignins policy delete-b2-c-authentication-method-policy`</a>

##### <a name="ParameterspoliciesDeleteB2cAuthenticationMethodsPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesDeleteClaimsMappingPolicies">Command `az identitysignins policy delete-claim-mapping-policy`</a>

##### <a name="ParameterspoliciesDeleteClaimsMappingPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--claims-mapping-policy-id**|string|key: id of claimsMappingPolicy|claims_mapping_policy_id|claimsMappingPolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesDeleteConditionalAccessPolicies">Command `az identitysignins policy delete-conditional-access-policy`</a>

##### <a name="ParameterspoliciesDeleteConditionalAccessPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--conditional-access-policy-id**|string|key: id of conditionalAccessPolicy|conditional_access_policy_id|conditionalAccessPolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesDeleteDeviceRegistrationPolicy">Command `az identitysignins policy delete-device-registration-policy`</a>

##### <a name="ParameterspoliciesDeleteDeviceRegistrationPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesDeleteDirectoryRoleAccessReviewPolicy">Command `az identitysignins policy delete-directory-role-access-review-policy`</a>

##### <a name="ParameterspoliciesDeleteDirectoryRoleAccessReviewPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesDeleteHomeRealmDiscoveryPolicies">Command `az identitysignins policy delete-home-realm-discovery-policy`</a>

##### <a name="ParameterspoliciesDeleteHomeRealmDiscoveryPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--home-realm-discovery-policy-id**|string|key: id of homeRealmDiscoveryPolicy|home_realm_discovery_policy_id|homeRealmDiscoveryPolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesDeleteIdentitySecurityDefaultsEnforcementPolicy">Command `az identitysignins policy delete-identity-security-default-enforcement-policy`</a>

##### <a name="ParameterspoliciesDeleteIdentitySecurityDefaultsEnforcementPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesDeletePermissionGrantPolicies">Command `az identitysignins policy delete-permission-grant-policy`</a>

##### <a name="ParameterspoliciesDeletePermissionGrantPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesDeletePrivateLinkResourcePolicies">Command `az identitysignins policy delete-private-link-resource-policy`</a>

##### <a name="ParameterspoliciesDeletePrivateLinkResourcePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--private-link-resource-id**|string|key: id of privateLinkResource|private_link_resource_id|privateLinkResource-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesDeleteTokenIssuancePolicies">Command `az identitysignins policy delete-token-issuance-policy`</a>

##### <a name="ParameterspoliciesDeleteTokenIssuancePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--token-issuance-policy-id**|string|key: id of tokenIssuancePolicy|token_issuance_policy_id|tokenIssuancePolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesDeleteTokenLifetimePolicies">Command `az identitysignins policy delete-token-lifetime-policy`</a>

##### <a name="ParameterspoliciesDeleteTokenLifetimePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--token-lifetime-policy-id**|string|key: id of tokenLifetimePolicy|token_lifetime_policy_id|tokenLifetimePolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesListActivityBasedTimeoutPolicies">Command `az identitysignins policy list-activity-based-timeout-policy`</a>

##### <a name="ParameterspoliciesListActivityBasedTimeoutPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesListAuthorizationPolicy">Command `az identitysignins policy list-authorization-policy`</a>

##### <a name="ParameterspoliciesListAuthorizationPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesListClaimsMappingPolicies">Command `az identitysignins policy list-claim-mapping-policy`</a>

##### <a name="ParameterspoliciesListClaimsMappingPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesListConditionalAccessPolicies">Command `az identitysignins policy list-conditional-access-policy`</a>

##### <a name="ParameterspoliciesListConditionalAccessPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesListHomeRealmDiscoveryPolicies">Command `az identitysignins policy list-home-realm-discovery-policy`</a>

##### <a name="ParameterspoliciesListHomeRealmDiscoveryPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesListPermissionGrantPolicies">Command `az identitysignins policy list-permission-grant-policy`</a>

##### <a name="ParameterspoliciesListPermissionGrantPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesListPrivateLinkResourcePolicies">Command `az identitysignins policy list-private-link-resource-policy`</a>

##### <a name="ParameterspoliciesListPrivateLinkResourcePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesListTokenIssuancePolicies">Command `az identitysignins policy list-token-issuance-policy`</a>

##### <a name="ParameterspoliciesListTokenIssuancePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesListTokenLifetimePolicies">Command `az identitysignins policy list-token-lifetime-policy`</a>

##### <a name="ParameterspoliciesListTokenLifetimePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesGetActivityBasedTimeoutPolicies">Command `az identitysignins policy show-activity-based-timeout-policy`</a>

##### <a name="ParameterspoliciesGetActivityBasedTimeoutPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--activity-based-timeout-policy-id**|string|key: id of activityBasedTimeoutPolicy|activity_based_timeout_policy_id|activityBasedTimeoutPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesGetAdminConsentRequestPolicy">Command `az identitysignins policy show-admin-consent-request-policy`</a>

##### <a name="ParameterspoliciesGetAdminConsentRequestPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesGetAuthenticationFlowsPolicy">Command `az identitysignins policy show-authentication-flow-policy`</a>

##### <a name="ParameterspoliciesGetAuthenticationFlowsPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesGetAuthorizationPolicy">Command `az identitysignins policy show-authorization-policy`</a>

##### <a name="ParameterspoliciesGetAuthorizationPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--authorization-policy-id**|string|key: id of authorizationPolicy|authorization_policy_id|authorizationPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesGetB2cAuthenticationMethodsPolicy">Command `az identitysignins policy show-b2-c-authentication-method-policy`</a>

##### <a name="ParameterspoliciesGetB2cAuthenticationMethodsPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesGetClaimsMappingPolicies">Command `az identitysignins policy show-claim-mapping-policy`</a>

##### <a name="ParameterspoliciesGetClaimsMappingPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--claims-mapping-policy-id**|string|key: id of claimsMappingPolicy|claims_mapping_policy_id|claimsMappingPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesGetConditionalAccessPolicies">Command `az identitysignins policy show-conditional-access-policy`</a>

##### <a name="ParameterspoliciesGetConditionalAccessPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--conditional-access-policy-id**|string|key: id of conditionalAccessPolicy|conditional_access_policy_id|conditionalAccessPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesGetDeviceRegistrationPolicy">Command `az identitysignins policy show-device-registration-policy`</a>

##### <a name="ParameterspoliciesGetDeviceRegistrationPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesGetDirectoryRoleAccessReviewPolicy">Command `az identitysignins policy show-directory-role-access-review-policy`</a>

##### <a name="ParameterspoliciesGetDirectoryRoleAccessReviewPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesGetHomeRealmDiscoveryPolicies">Command `az identitysignins policy show-home-realm-discovery-policy`</a>

##### <a name="ParameterspoliciesGetHomeRealmDiscoveryPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--home-realm-discovery-policy-id**|string|key: id of homeRealmDiscoveryPolicy|home_realm_discovery_policy_id|homeRealmDiscoveryPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesGetIdentitySecurityDefaultsEnforcementPolicy">Command `az identitysignins policy show-identity-security-default-enforcement-policy`</a>

##### <a name="ParameterspoliciesGetIdentitySecurityDefaultsEnforcementPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesGetPermissionGrantPolicies">Command `az identitysignins policy show-permission-grant-policy`</a>

##### <a name="ParameterspoliciesGetPermissionGrantPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesGetPrivateLinkResourcePolicies">Command `az identitysignins policy show-private-link-resource-policy`</a>

##### <a name="ParameterspoliciesGetPrivateLinkResourcePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--private-link-resource-id**|string|key: id of privateLinkResource|private_link_resource_id|privateLinkResource-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesGetTokenIssuancePolicies">Command `az identitysignins policy show-token-issuance-policy`</a>

##### <a name="ParameterspoliciesGetTokenIssuancePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--token-issuance-policy-id**|string|key: id of tokenIssuancePolicy|token_issuance_policy_id|tokenIssuancePolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesGetTokenLifetimePolicies">Command `az identitysignins policy show-token-lifetime-policy`</a>

##### <a name="ParameterspoliciesGetTokenLifetimePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--token-lifetime-policy-id**|string|key: id of tokenLifetimePolicy|token_lifetime_policy_id|tokenLifetimePolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policiesUpdateActivityBasedTimeoutPolicies">Command `az identitysignins policy update-activity-based-timeout-policy`</a>

##### <a name="ParameterspoliciesUpdateActivityBasedTimeoutPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--activity-based-timeout-policy-id**|string|key: id of activityBasedTimeoutPolicy|activity_based_timeout_policy_id|activityBasedTimeoutPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

#### <a name="policiesUpdateAdminConsentRequestPolicy">Command `az identitysignins policy update-admin-consent-request-policy`</a>

##### <a name="ParameterspoliciesUpdateAdminConsentRequestPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--is-enabled**|boolean||is_enabled|isEnabled|
|**--notify-reviewers**|boolean||notify_reviewers|notifyReviewers|
|**--reminders-enabled**|boolean||reminders_enabled|remindersEnabled|
|**--request-duration-in-days**|integer||request_duration_in_days|requestDurationInDays|
|**--reviewers**|array||reviewers|reviewers|
|**--version**|integer||version|version|

#### <a name="policiesUpdateAuthenticationFlowsPolicy">Command `az identitysignins policy update-authentication-flow-policy`</a>

##### <a name="ParameterspoliciesUpdateAuthenticationFlowsPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--description**|string||description|description|
|**--display-name**|string||display_name|displayName|
|**--is-enabled**|boolean||is_enabled|isEnabled|

#### <a name="policiesUpdateAuthorizationPolicy">Command `az identitysignins policy update-authorization-policy`</a>

##### <a name="ParameterspoliciesUpdateAuthorizationPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--authorization-policy-id**|string|key: id of authorizationPolicy|authorization_policy_id|authorizationPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--allowed-to-sign-up-email-based-subscriptions**|boolean||allowed_to_sign_up_email_based_subscriptions|allowedToSignUpEmailBasedSubscriptions|
|**--allowed-to-use-sspr**|boolean||allowed_to_use_sspr|allowedToUseSSPR|
|**--allow-email-verified-users-to-join-organization**|boolean||allow_email_verified_users_to_join_organization|allowEmailVerifiedUsersToJoinOrganization|
|**--allow-invites-from**|choice||allow_invites_from|allowInvitesFrom|
|**--block-msol-power-shell**|boolean||block_msol_power_shell|blockMsolPowerShell|
|**--default-user-role-permissions**|object|defaultUserRolePermissions|default_user_role_permissions|defaultUserRolePermissions|
|**--enabled-preview-features**|array||enabled_preview_features|enabledPreviewFeatures|
|**--guest-user-role-id**|uuid||guest_user_role_id|guestUserRoleId|
|**--permission-grant-policy-ids-assigned-to-default-user-role**|array||permission_grant_policy_ids_assigned_to_default_user_role|permissionGrantPolicyIdsAssignedToDefaultUserRole|

#### <a name="policiesUpdateB2cAuthenticationMethodsPolicy">Command `az identitysignins policy update-b2-c-authentication-method-policy`</a>

##### <a name="ParameterspoliciesUpdateB2cAuthenticationMethodsPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--is-email-password-authentication-enabled**|boolean||is_email_password_authentication_enabled|isEmailPasswordAuthenticationEnabled|
|**--is-phone-one-time-password-authentication-enabled**|boolean||is_phone_one_time_password_authentication_enabled|isPhoneOneTimePasswordAuthenticationEnabled|
|**--is-user-name-authentication-enabled**|boolean||is_user_name_authentication_enabled|isUserNameAuthenticationEnabled|

#### <a name="policiesUpdateClaimsMappingPolicies">Command `az identitysignins policy update-claim-mapping-policy`</a>

##### <a name="ParameterspoliciesUpdateClaimsMappingPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--claims-mapping-policy-id**|string|key: id of claimsMappingPolicy|claims_mapping_policy_id|claimsMappingPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

#### <a name="policiesUpdateConditionalAccessPolicies">Command `az identitysignins policy update-conditional-access-policy`</a>

##### <a name="ParameterspoliciesUpdateConditionalAccessPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--conditional-access-policy-id**|string|key: id of conditionalAccessPolicy|conditional_access_policy_id|conditionalAccessPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|created_date_time|createdDateTime|
|**--description**|string||description|description|
|**--display-name**|string|Specifies a display name for the conditionalAccessPolicy object.|display_name|displayName|
|**--grant-controls**|object|conditionalAccessGrantControls|grant_controls|grantControls|
|**--modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Readonly.|modified_date_time|modifiedDateTime|
|**--state**|choice||state|state|
|**--application-enforced-restrictions**|object|applicationEnforcedRestrictionsSessionControl|application_enforced_restrictions|applicationEnforcedRestrictions|
|**--cloud-app-security**|object|cloudAppSecuritySessionControl|cloud_app_security|cloudAppSecurity|
|**--persistent-browser**|object|persistentBrowserSessionControl|persistent_browser|persistentBrowser|
|**--sign-in-frequency**|object|signInFrequencySessionControl|sign_in_frequency|signInFrequency|
|**--applications**|object|conditionalAccessApplications|applications|applications|
|**--client-applications**|object|conditionalAccessClientApplications|client_applications|clientApplications|
|**--client-app-types**|array|Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other.|client_app_types|clientAppTypes|
|**--devices**|object|conditionalAccessDevices|devices|devices|
|**--device-states**|object|conditionalAccessDeviceStates|device_states|deviceStates|
|**--locations**|object|conditionalAccessLocations|locations|locations|
|**--platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--sign-in-risk-levels**|array|Risk levels included in the policy. Possible values are: low, medium, high, none.|sign_in_risk_levels|signInRiskLevels|
|**--user-risk-levels**|array||user_risk_levels|userRiskLevels|
|**--users**|object|conditionalAccessUsers|users|users|

#### <a name="policiesUpdateDeviceRegistrationPolicy">Command `az identitysignins policy update-device-registration-policy`</a>

##### <a name="ParameterspoliciesUpdateDeviceRegistrationPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|

#### <a name="policiesUpdateDirectoryRoleAccessReviewPolicy">Command `az identitysignins policy update-directory-role-access-review-policy`</a>

##### <a name="ParameterspoliciesUpdateDirectoryRoleAccessReviewPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--apply-actions**|array||apply_actions|applyActions|
|**--auto-apply-decisions-enabled**|boolean||auto_apply_decisions_enabled|autoApplyDecisionsEnabled|
|**--default-decision**|string||default_decision|defaultDecision|
|**--default-decision-enabled**|boolean||default_decision_enabled|defaultDecisionEnabled|
|**--instance-duration-in-days**|integer||instance_duration_in_days|instanceDurationInDays|
|**--justification-required-on-approval**|boolean||justification_required_on_approval|justificationRequiredOnApproval|
|**--mail-notifications-enabled**|boolean||mail_notifications_enabled|mailNotificationsEnabled|
|**--recommendations-enabled**|boolean||recommendations_enabled|recommendationsEnabled|
|**--reminder-notifications-enabled**|boolean||reminder_notifications_enabled|reminderNotificationsEnabled|
|**--pattern**|object|recurrencePattern|pattern|pattern|
|**--range**|object|recurrenceRange|range|range|

#### <a name="policiesUpdateHomeRealmDiscoveryPolicies">Command `az identitysignins policy update-home-realm-discovery-policy`</a>

##### <a name="ParameterspoliciesUpdateHomeRealmDiscoveryPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--home-realm-discovery-policy-id**|string|key: id of homeRealmDiscoveryPolicy|home_realm_discovery_policy_id|homeRealmDiscoveryPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

#### <a name="policiesUpdateIdentitySecurityDefaultsEnforcementPolicy">Command `az identitysignins policy update-identity-security-default-enforcement-policy`</a>

##### <a name="ParameterspoliciesUpdateIdentitySecurityDefaultsEnforcementPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--is-enabled**|boolean|If set to true, Azure Active Directory security defaults is enabled for the tenant.|is_enabled|isEnabled|

#### <a name="policiesUpdatePermissionGrantPolicies">Command `az identitysignins policy update-permission-grant-policy`</a>

##### <a name="ParameterspoliciesUpdatePermissionGrantPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--excludes**|array||excludes|excludes|
|**--includes**|array||includes|includes|

#### <a name="policiesUpdatePrivateLinkResourcePolicies">Command `az identitysignins policy update-private-link-resource-policy`</a>

##### <a name="ParameterspoliciesUpdatePrivateLinkResourcePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--private-link-resource-id**|string|key: id of privateLinkResource|private_link_resource_id|privateLinkResource-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-tenant-ids**|array||allowed_tenant_ids|allowedTenantIds|
|**--arm-resource-id**|string||arm_resource_id|armResourceId|

#### <a name="policiesUpdateTokenIssuancePolicies">Command `az identitysignins policy update-token-issuance-policy`</a>

##### <a name="ParameterspoliciesUpdateTokenIssuancePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--token-issuance-policy-id**|string|key: id of tokenIssuancePolicy|token_issuance_policy_id|tokenIssuancePolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

#### <a name="policiesUpdateTokenLifetimePolicies">Command `az identitysignins policy update-token-lifetime-policy`</a>

##### <a name="ParameterspoliciesUpdateTokenLifetimePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--token-lifetime-policy-id**|string|key: id of tokenLifetimePolicy|token_lifetime_policy_id|tokenLifetimePolicy-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--description**|string|Description for this policy.|description|description|
|**--display-name**|string|Display name for this policy.|display_name|displayName|
|**--definition**|array|A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.|definition|definition|
|**--is-organization-default**|boolean|If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.|is_organization_default|isOrganizationDefault|
|**--applies-to**|array||applies_to|appliesTo|

### group `az identitysignins riskdetectionsriskdetection`
#### <a name="riskDetections.riskDetectionCreateRiskDetection">Command `az identitysignins riskdetectionsriskdetection create-risk-detection`</a>

##### <a name="ParametersriskDetections.riskDetectionCreateRiskDetection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--activity**|choice||activity|activity|
|**--activity-date-time**|date-time|Date and time that the risky activity occurred.|activity_date_time|activityDateTime|
|**--additional-info**|string|Additional information associated with the risk detection in JSON format.|additional_info|additionalInfo|
|**--correlation-id**|string|Correlation ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.|correlation_id|correlationId|
|**--detected-date-time**|date-time|Date and time that the risk was detected.|detected_date_time|detectedDateTime|
|**--detection-timing-type**|choice||detection_timing_type|detectionTimingType|
|**--ip-address**|string|Provides the IP address of the client from where the risk occurred.|ip_address|ipAddress|
|**--last-updated-date-time**|date-time|Date and time that the risk detection was last updated.|last_updated_date_time|lastUpdatedDateTime|
|**--request-id**|string|Request ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.|request_id|requestId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-type**|string|The type of risk event detected. The possible values are unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence, genericadminConfirmedUserCompromised, mcasImpossibleTravel, mcasSuspiciousInboxManipulationRules, investigationsThreatIntelligenceSigninLinked, maliciousIPAddressValidCredentialsBlockedIP, and unknownFutureValue. If the risk detection is a premium detection, will show generic|risk_event_type|riskEventType|
|**--risk-level**|choice||risk_level|riskLevel|
|**--risk-state**|choice||risk_state|riskState|
|**--risk-type**|choice||risk_type|riskType|
|**--source**|string|Source of the risk detection. For example, 'activeDirectory'.|source|source|
|**--token-issuer-type**|choice||token_issuer_type|tokenIssuerType|
|**--user-display-name**|string|The user principal name (UPN) of the user.|user_display_name|userDisplayName|
|**--user-id**|string|Unique ID of the user.|user_id|userId|
|**--user-principal-name**|string|The user principal name (UPN) of the user.|user_principal_name|userPrincipalName|
|**--city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|

#### <a name="riskDetections.riskDetectionDeleteRiskDetection">Command `az identitysignins riskdetectionsriskdetection delete-risk-detection`</a>

##### <a name="ParametersriskDetections.riskDetectionDeleteRiskDetection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risk-detection-id**|string|key: id of riskDetection|risk_detection_id|riskDetection-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="riskDetections.riskDetectionListRiskDetection">Command `az identitysignins riskdetectionsriskdetection list-risk-detection`</a>

##### <a name="ParametersriskDetections.riskDetectionListRiskDetection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="riskDetections.riskDetectionGetRiskDetection">Command `az identitysignins riskdetectionsriskdetection show-risk-detection`</a>

##### <a name="ParametersriskDetections.riskDetectionGetRiskDetection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risk-detection-id**|string|key: id of riskDetection|risk_detection_id|riskDetection-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="riskDetections.riskDetectionUpdateRiskDetection">Command `az identitysignins riskdetectionsriskdetection update-risk-detection`</a>

##### <a name="ParametersriskDetections.riskDetectionUpdateRiskDetection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risk-detection-id**|string|key: id of riskDetection|risk_detection_id|riskDetection-id|
|**--id**|string|Read-only.|id|id|
|**--activity**|choice||activity|activity|
|**--activity-date-time**|date-time|Date and time that the risky activity occurred.|activity_date_time|activityDateTime|
|**--additional-info**|string|Additional information associated with the risk detection in JSON format.|additional_info|additionalInfo|
|**--correlation-id**|string|Correlation ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.|correlation_id|correlationId|
|**--detected-date-time**|date-time|Date and time that the risk was detected.|detected_date_time|detectedDateTime|
|**--detection-timing-type**|choice||detection_timing_type|detectionTimingType|
|**--ip-address**|string|Provides the IP address of the client from where the risk occurred.|ip_address|ipAddress|
|**--last-updated-date-time**|date-time|Date and time that the risk detection was last updated.|last_updated_date_time|lastUpdatedDateTime|
|**--request-id**|string|Request ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.|request_id|requestId|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-event-type**|string|The type of risk event detected. The possible values are unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence, genericadminConfirmedUserCompromised, mcasImpossibleTravel, mcasSuspiciousInboxManipulationRules, investigationsThreatIntelligenceSigninLinked, maliciousIPAddressValidCredentialsBlockedIP, and unknownFutureValue. If the risk detection is a premium detection, will show generic|risk_event_type|riskEventType|
|**--risk-level**|choice||risk_level|riskLevel|
|**--risk-state**|choice||risk_state|riskState|
|**--risk-type**|choice||risk_type|riskType|
|**--source**|string|Source of the risk detection. For example, 'activeDirectory'.|source|source|
|**--token-issuer-type**|choice||token_issuer_type|tokenIssuerType|
|**--user-display-name**|string|The user principal name (UPN) of the user.|user_display_name|userDisplayName|
|**--user-id**|string|Unique ID of the user.|user_id|userId|
|**--user-principal-name**|string|The user principal name (UPN) of the user.|user_principal_name|userPrincipalName|
|**--city**|string|Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|city|city|
|**--country-or-region**|string|Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.|country_or_region|countryOrRegion|
|**--geo-coordinates**|object|geoCoordinates|geo_coordinates|geoCoordinates|
|**--state**|string|Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.|state|state|

### group `az identitysignins riskyuser`
#### <a name="riskyUsersconfirmCompromised">Command `az identitysignins riskyuser confirm-compromised`</a>

##### <a name="ParametersriskyUsersconfirmCompromised">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-ids**|array||user_ids|userIds|

#### <a name="riskyUsersCreateHistory">Command `az identitysignins riskyuser create-history`</a>

##### <a name="ParametersriskyUsersCreateHistory">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: id of riskyUser|risky_user_id|riskyUser-id|
|**--id**|string|Read-only.|id|id|
|**--is-deleted**|boolean|Indicates whether the user is deleted. Possible values are: true, false|is_deleted|isDeleted|
|**--is-processing**|boolean|Indicates wehther a user's risky state is being processed by the backend|is_processing|isProcessing|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-last-updated-date-time**|date-time|The date and time that the risky user was last updated.|risk_last_updated_date_time|riskLastUpdatedDateTime|
|**--risk-level**|choice||risk_level|riskLevel|
|**--risk-state**|choice||risk_state|riskState|
|**--user-display-name**|string|Risky user display name.|user_display_name|userDisplayName|
|**--user-principal-name**|string|Risky user principal name.|user_principal_name|userPrincipalName|
|**--history**|array|The activity related to user risk level change|history|history|
|**--activity**|object|riskUserActivity|activity|activity|
|**--initiated-by**|string|The id of actor that does the operation.|initiated_by|initiatedBy|
|**--user-id**|string|The id of the user.|user_id|userId|

#### <a name="riskyUsersDeleteHistory">Command `az identitysignins riskyuser delete-history`</a>

##### <a name="ParametersriskyUsersDeleteHistory">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: id of riskyUser|risky_user_id|riskyUser-id|
|**--risky-user-history-item-id**|string|key: id of riskyUserHistoryItem|risky_user_history_item_id|riskyUserHistoryItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="riskyUsersdismiss">Command `az identitysignins riskyuser dismiss`</a>

##### <a name="ParametersriskyUsersdismiss">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-ids**|array||user_ids|userIds|

#### <a name="riskyUsersListHistory">Command `az identitysignins riskyuser list-history`</a>

##### <a name="ParametersriskyUsersListHistory">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: id of riskyUser|risky_user_id|riskyUser-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="riskyUsersGetHistory">Command `az identitysignins riskyuser show-history`</a>

##### <a name="ParametersriskyUsersGetHistory">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: id of riskyUser|risky_user_id|riskyUser-id|
|**--risky-user-history-item-id**|string|key: id of riskyUserHistoryItem|risky_user_history_item_id|riskyUserHistoryItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="riskyUsersUpdateHistory">Command `az identitysignins riskyuser update-history`</a>

##### <a name="ParametersriskyUsersUpdateHistory">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: id of riskyUser|risky_user_id|riskyUser-id|
|**--risky-user-history-item-id**|string|key: id of riskyUserHistoryItem|risky_user_history_item_id|riskyUserHistoryItem-id|
|**--id**|string|Read-only.|id|id|
|**--is-deleted**|boolean|Indicates whether the user is deleted. Possible values are: true, false|is_deleted|isDeleted|
|**--is-processing**|boolean|Indicates wehther a user's risky state is being processed by the backend|is_processing|isProcessing|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-last-updated-date-time**|date-time|The date and time that the risky user was last updated.|risk_last_updated_date_time|riskLastUpdatedDateTime|
|**--risk-level**|choice||risk_level|riskLevel|
|**--risk-state**|choice||risk_state|riskState|
|**--user-display-name**|string|Risky user display name.|user_display_name|userDisplayName|
|**--user-principal-name**|string|Risky user principal name.|user_principal_name|userPrincipalName|
|**--history**|array|The activity related to user risk level change|history|history|
|**--activity**|object|riskUserActivity|activity|activity|
|**--initiated-by**|string|The id of actor that does the operation.|initiated_by|initiatedBy|
|**--user-id**|string|The id of the user.|user_id|userId|

### group `az identitysignins riskyusersriskyuser`
#### <a name="riskyUsers.riskyUserCreateRiskyUser">Command `az identitysignins riskyusersriskyuser create-risky-user`</a>

##### <a name="ParametersriskyUsers.riskyUserCreateRiskyUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--is-deleted**|boolean|Indicates whether the user is deleted. Possible values are: true, false|is_deleted|isDeleted|
|**--is-processing**|boolean|Indicates wehther a user's risky state is being processed by the backend|is_processing|isProcessing|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-last-updated-date-time**|date-time|The date and time that the risky user was last updated.|risk_last_updated_date_time|riskLastUpdatedDateTime|
|**--risk-level**|choice||risk_level|riskLevel|
|**--risk-state**|choice||risk_state|riskState|
|**--user-display-name**|string|Risky user display name.|user_display_name|userDisplayName|
|**--user-principal-name**|string|Risky user principal name.|user_principal_name|userPrincipalName|
|**--history**|array|The activity related to user risk level change|history|history|

#### <a name="riskyUsers.riskyUserDeleteRiskyUser">Command `az identitysignins riskyusersriskyuser delete-risky-user`</a>

##### <a name="ParametersriskyUsers.riskyUserDeleteRiskyUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: id of riskyUser|risky_user_id|riskyUser-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="riskyUsers.riskyUserListRiskyUser">Command `az identitysignins riskyusersriskyuser list-risky-user`</a>

##### <a name="ParametersriskyUsers.riskyUserListRiskyUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="riskyUsers.riskyUserGetRiskyUser">Command `az identitysignins riskyusersriskyuser show-risky-user`</a>

##### <a name="ParametersriskyUsers.riskyUserGetRiskyUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: id of riskyUser|risky_user_id|riskyUser-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="riskyUsers.riskyUserUpdateRiskyUser">Command `az identitysignins riskyusersriskyuser update-risky-user`</a>

##### <a name="ParametersriskyUsers.riskyUserUpdateRiskyUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--risky-user-id**|string|key: id of riskyUser|risky_user_id|riskyUser-id|
|**--id**|string|Read-only.|id|id|
|**--is-deleted**|boolean|Indicates whether the user is deleted. Possible values are: true, false|is_deleted|isDeleted|
|**--is-processing**|boolean|Indicates wehther a user's risky state is being processed by the backend|is_processing|isProcessing|
|**--risk-detail**|choice||risk_detail|riskDetail|
|**--risk-last-updated-date-time**|date-time|The date and time that the risky user was last updated.|risk_last_updated_date_time|riskLastUpdatedDateTime|
|**--risk-level**|choice||risk_level|riskLevel|
|**--risk-state**|choice||risk_state|riskState|
|**--user-display-name**|string|Risky user display name.|user_display_name|userDisplayName|
|**--user-principal-name**|string|Risky user principal name.|user_principal_name|userPrincipalName|
|**--history**|array|The activity related to user risk level change|history|history|

### group `az identitysignins trustframework`
#### <a name="trustFramework.trustFrameworkGetTrustFramework">Command `az identitysignins trustframework show-trust-framework`</a>

##### <a name="ParameterstrustFramework.trustFrameworkGetTrustFramework">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="trustFramework.trustFrameworkUpdateTrustFramework">Command `az identitysignins trustframework update-trust-framework`</a>

##### <a name="ParameterstrustFramework.trustFrameworkUpdateTrustFramework">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--key-sets**|array||key_sets|keySets|
|**--policies**|array||policies|policies|

### group `az identitysignins trustframework`
#### <a name="trustFrameworkCreateKeySets">Command `az identitysignins trustframework create-key-set`</a>

##### <a name="ParameterstrustFrameworkCreateKeySets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--keys**|array||keys|keys|

#### <a name="trustFrameworkCreatePolicies">Command `az identitysignins trustframework create-policy`</a>

##### <a name="ParameterstrustFrameworkCreatePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|

#### <a name="trustFrameworkDeleteKeySets">Command `az identitysignins trustframework delete-key-set`</a>

##### <a name="ParameterstrustFrameworkDeleteKeySets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-key-set-id**|string|key: id of trustFrameworkKeySet|trust_framework_key_set_id|trustFrameworkKeySet-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="trustFrameworkDeletePolicies">Command `az identitysignins trustframework delete-policy`</a>

##### <a name="ParameterstrustFrameworkDeletePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-policy-id**|string|key: id of trustFrameworkPolicy|trust_framework_policy_id|trustFrameworkPolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="trustFrameworkListKeySets">Command `az identitysignins trustframework list-key-set`</a>

##### <a name="ParameterstrustFrameworkListKeySets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="trustFrameworkListPolicies">Command `az identitysignins trustframework list-policy`</a>

##### <a name="ParameterstrustFrameworkListPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="trustFrameworkSetPoliciesContent">Command `az identitysignins trustframework set-policy-content`</a>

##### <a name="ParameterstrustFrameworkSetPoliciesContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-policy-id**|string|key: id of trustFrameworkPolicy|trust_framework_policy_id|trustFrameworkPolicy-id|
|**--data**|binary|New media content.|data|data|

#### <a name="trustFrameworkGetKeySets">Command `az identitysignins trustframework show-key-set`</a>

##### <a name="ParameterstrustFrameworkGetKeySets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-key-set-id**|string|key: id of trustFrameworkKeySet|trust_framework_key_set_id|trustFrameworkKeySet-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="trustFrameworkGetPolicies">Command `az identitysignins trustframework show-policy`</a>

##### <a name="ParameterstrustFrameworkGetPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-policy-id**|string|key: id of trustFrameworkPolicy|trust_framework_policy_id|trustFrameworkPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="trustFrameworkGetPoliciesContent">Command `az identitysignins trustframework show-policy-content`</a>

##### <a name="ParameterstrustFrameworkGetPoliciesContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-policy-id**|string|key: id of trustFrameworkPolicy|trust_framework_policy_id|trustFrameworkPolicy-id|

#### <a name="trustFrameworkUpdateKeySets">Command `az identitysignins trustframework update-key-set`</a>

##### <a name="ParameterstrustFrameworkUpdateKeySets">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-key-set-id**|string|key: id of trustFrameworkKeySet|trust_framework_key_set_id|trustFrameworkKeySet-id|
|**--id**|string|Read-only.|id|id|
|**--keys**|array||keys|keys|

#### <a name="trustFrameworkUpdatePolicies">Command `az identitysignins trustframework update-policy`</a>

##### <a name="ParameterstrustFrameworkUpdatePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-policy-id**|string|key: id of trustFrameworkPolicy|trust_framework_policy_id|trustFrameworkPolicy-id|
|**--id**|string|Read-only.|id|id|

### group `az identitysignins trustframeworkkeyset`
#### <a name="trustFramework.keySetsgenerateKey">Command `az identitysignins trustframeworkkeyset generate-key`</a>

##### <a name="ParameterstrustFramework.keySetsgenerateKey">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-key-set-id**|string|key: id of trustFrameworkKeySet|trust_framework_key_set_id|trustFrameworkKeySet-id|
|**--use**|string||use|use|
|**--kty**|string||kty|kty|
|**--nbf**|integer||nbf|nbf|
|**--exp**|integer||exp|exp|

#### <a name="trustFramework.keySetsgetActiveKey">Command `az identitysignins trustframeworkkeyset show-active-key`</a>

##### <a name="ParameterstrustFramework.keySetsgetActiveKey">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-key-set-id**|string|key: id of trustFrameworkKeySet|trust_framework_key_set_id|trustFrameworkKeySet-id|

#### <a name="trustFramework.keySetsuploadCertificate">Command `az identitysignins trustframeworkkeyset upload-certificate`</a>

##### <a name="ParameterstrustFramework.keySetsuploadCertificate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-key-set-id**|string|key: id of trustFrameworkKeySet|trust_framework_key_set_id|trustFrameworkKeySet-id|
|**--key**|string||key|key|

#### <a name="trustFramework.keySetsuploadPkcs12">Command `az identitysignins trustframeworkkeyset upload-pkcs12`</a>

##### <a name="ParameterstrustFramework.keySetsuploadPkcs12">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-key-set-id**|string|key: id of trustFrameworkKeySet|trust_framework_key_set_id|trustFrameworkKeySet-id|
|**--key**|string||key|key|
|**--password**|string||password|password|

#### <a name="trustFramework.keySetsuploadSecret">Command `az identitysignins trustframeworkkeyset upload-secret`</a>

##### <a name="ParameterstrustFramework.keySetsuploadSecret">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--trust-framework-key-set-id**|string|key: id of trustFrameworkKeySet|trust_framework_key_set_id|trustFrameworkKeySet-id|
|**--use**|string||use|use|
|**--k**|string||k|k|
|**--nbf**|integer||nbf|nbf|
|**--exp**|integer||exp|exp|

### group `az identitysignins user`
#### <a name="usersDeleteAuthentication">Command `az identitysignins user delete-authentication`</a>

##### <a name="ParametersusersDeleteAuthentication">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteInformationProtection">Command `az identitysignins user delete-information-protection`</a>

##### <a name="ParametersusersDeleteInformationProtection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersGetAuthentication">Command `az identitysignins user show-authentication`</a>

##### <a name="ParametersusersGetAuthentication">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetInformationProtection">Command `az identitysignins user show-information-protection`</a>

##### <a name="ParametersusersGetInformationProtection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateAuthentication">Command `az identitysignins user update-authentication`</a>

##### <a name="ParametersusersUpdateAuthentication">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--email-methods**|array||email_methods|emailMethods|
|**--fido2-methods**|array||fido2_methods|fido2Methods|
|**--methods**|array||methods|methods|
|**--microsoft-authenticator-methods**|array||microsoft_authenticator_methods|microsoftAuthenticatorMethods|
|**--oath-methods**|array||oath_methods|oathMethods|
|**--operations**|array||operations|operations|
|**--passwordless-microsoft-authenticator-methods**|array||passwordless_microsoft_authenticator_methods|passwordlessMicrosoftAuthenticatorMethods|
|**--password-methods**|array||password_methods|passwordMethods|
|**--phone-methods**|array||phone_methods|phoneMethods|
|**--security-question-methods**|array||security_question_methods|securityQuestionMethods|
|**--temporary-access-pass-methods**|array||temporary_access_pass_methods|temporaryAccessPassMethods|

#### <a name="usersUpdateInformationProtection">Command `az identitysignins user update-information-protection`</a>

##### <a name="ParametersusersUpdateInformationProtection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--data-loss-prevention-policies**|array||data_loss_prevention_policies|dataLossPreventionPolicies|
|**--sensitivity-labels**|array||sensitivity_labels|sensitivityLabels|
|**--sensitivity-policy-settings**|object|sensitivityPolicySettings|sensitivity_policy_settings|sensitivityPolicySettings|
|**--threat-assessment-requests**|array||threat_assessment_requests|threatAssessmentRequests|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--labels**|array||labels|labels|

### group `az identitysignins usersauthentication`
#### <a name="users.authenticationCreateEmailMethods">Command `az identitysignins usersauthentication create-email-method`</a>

##### <a name="Parametersusers.authenticationCreateEmailMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.authenticationCreateFido2Methods">Command `az identitysignins usersauthentication create-fido2-method`</a>

##### <a name="Parametersusers.authenticationCreateFido2Methods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.authenticationCreateMethods">Command `az identitysignins usersauthentication create-method`</a>

##### <a name="Parametersusers.authenticationCreateMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.authenticationCreateMicrosoftAuthenticatorMethods">Command `az identitysignins usersauthentication create-microsoft-authenticator-method`</a>

##### <a name="Parametersusers.authenticationCreateMicrosoftAuthenticatorMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.authenticationCreateOathMethods">Command `az identitysignins usersauthentication create-oath-method`</a>

##### <a name="Parametersusers.authenticationCreateOathMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.authenticationCreateOperations">Command `az identitysignins usersauthentication create-operation`</a>

##### <a name="Parametersusers.authenticationCreateOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-action-date-time**|date-time||last_action_date_time|lastActionDateTime|
|**--resource-location**|string||resource_location|resourceLocation|
|**--status**|choice||status|status|
|**--status-detail**|string||status_detail|statusDetail|

#### <a name="users.authenticationCreatePasswordMethods">Command `az identitysignins usersauthentication create-password-method`</a>

##### <a name="Parametersusers.authenticationCreatePasswordMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--creation-date-time**|date-time||creation_date_time|creationDateTime|
|**--password**|string||password|password|

#### <a name="users.authenticationCreatePasswordlessMicrosoftAuthenticatorMethods">Command `az identitysignins usersauthentication create-passwordless-microsoft-authenticator-method`</a>

##### <a name="Parametersusers.authenticationCreatePasswordlessMicrosoftAuthenticatorMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.authenticationCreatePhoneMethods">Command `az identitysignins usersauthentication create-phone-method`</a>

##### <a name="Parametersusers.authenticationCreatePhoneMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--phone-number**|string||phone_number|phoneNumber|
|**--phone-type**|choice||phone_type|phoneType|
|**--sms-sign-in-state**|choice||sms_sign_in_state|smsSignInState|

#### <a name="users.authenticationCreateSecurityQuestionMethods">Command `az identitysignins usersauthentication create-security-question-method`</a>

##### <a name="Parametersusers.authenticationCreateSecurityQuestionMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.authenticationCreateTemporaryAccessPassMethods">Command `az identitysignins usersauthentication create-temporary-access-pass-method`</a>

##### <a name="Parametersusers.authenticationCreateTemporaryAccessPassMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.authenticationDeleteEmailMethods">Command `az identitysignins usersauthentication delete-email-method`</a>

##### <a name="Parametersusers.authenticationDeleteEmailMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--email-authentication-method-id**|string|key: id of emailAuthenticationMethod|email_authentication_method_id|emailAuthenticationMethod-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.authenticationDeleteFido2Methods">Command `az identitysignins usersauthentication delete-fido2-method`</a>

##### <a name="Parametersusers.authenticationDeleteFido2Methods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--fido2-authentication-method-id**|string|key: id of fido2AuthenticationMethod|fido2_authentication_method_id|fido2AuthenticationMethod-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.authenticationDeleteMethods">Command `az identitysignins usersauthentication delete-method`</a>

##### <a name="Parametersusers.authenticationDeleteMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--authentication-method-id**|string|key: id of authenticationMethod|authentication_method_id|authenticationMethod-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.authenticationDeleteMicrosoftAuthenticatorMethods">Command `az identitysignins usersauthentication delete-microsoft-authenticator-method`</a>

##### <a name="Parametersusers.authenticationDeleteMicrosoftAuthenticatorMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--microsoft-authenticator-authentication-method-id**|string|key: id of microsoftAuthenticatorAuthenticationMethod|microsoft_authenticator_authentication_method_id|microsoftAuthenticatorAuthenticationMethod-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.authenticationDeleteOathMethods">Command `az identitysignins usersauthentication delete-oath-method`</a>

##### <a name="Parametersusers.authenticationDeleteOathMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--software-oath-authentication-method-id**|string|key: id of softwareOathAuthenticationMethod|software_oath_authentication_method_id|softwareOathAuthenticationMethod-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.authenticationDeleteOperations">Command `az identitysignins usersauthentication delete-operation`</a>

##### <a name="Parametersusers.authenticationDeleteOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--long-running-operation-id**|string|key: id of longRunningOperation|long_running_operation_id|longRunningOperation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.authenticationDeletePasswordMethods">Command `az identitysignins usersauthentication delete-password-method`</a>

##### <a name="Parametersusers.authenticationDeletePasswordMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--password-authentication-method-id**|string|key: id of passwordAuthenticationMethod|password_authentication_method_id|passwordAuthenticationMethod-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.authenticationDeletePasswordlessMicrosoftAuthenticatorMethods">Command `az identitysignins usersauthentication delete-passwordless-microsoft-authenticator-method`</a>

##### <a name="Parametersusers.authenticationDeletePasswordlessMicrosoftAuthenticatorMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--passwordless-microsoft-authenticator-authentication-method-id**|string|key: id of passwordlessMicrosoftAuthenticatorAuthenticationMethod|passwordless_microsoft_authenticator_authentication_method_id|passwordlessMicrosoftAuthenticatorAuthenticationMethod-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.authenticationDeletePhoneMethods">Command `az identitysignins usersauthentication delete-phone-method`</a>

##### <a name="Parametersusers.authenticationDeletePhoneMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--phone-authentication-method-id**|string|key: id of phoneAuthenticationMethod|phone_authentication_method_id|phoneAuthenticationMethod-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.authenticationDeleteSecurityQuestionMethods">Command `az identitysignins usersauthentication delete-security-question-method`</a>

##### <a name="Parametersusers.authenticationDeleteSecurityQuestionMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--security-question-authentication-method-id**|string|key: id of securityQuestionAuthenticationMethod|security_question_authentication_method_id|securityQuestionAuthenticationMethod-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.authenticationDeleteTemporaryAccessPassMethods">Command `az identitysignins usersauthentication delete-temporary-access-pass-method`</a>

##### <a name="Parametersusers.authenticationDeleteTemporaryAccessPassMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--temporary-access-pass-authentication-method-id**|string|key: id of temporaryAccessPassAuthenticationMethod|temporary_access_pass_authentication_method_id|temporaryAccessPassAuthenticationMethod-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.authenticationListEmailMethods">Command `az identitysignins usersauthentication list-email-method`</a>

##### <a name="Parametersusers.authenticationListEmailMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationListFido2Methods">Command `az identitysignins usersauthentication list-fido2-method`</a>

##### <a name="Parametersusers.authenticationListFido2Methods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationListMethods">Command `az identitysignins usersauthentication list-method`</a>

##### <a name="Parametersusers.authenticationListMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationListMicrosoftAuthenticatorMethods">Command `az identitysignins usersauthentication list-microsoft-authenticator-method`</a>

##### <a name="Parametersusers.authenticationListMicrosoftAuthenticatorMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationListOathMethods">Command `az identitysignins usersauthentication list-oath-method`</a>

##### <a name="Parametersusers.authenticationListOathMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationListOperations">Command `az identitysignins usersauthentication list-operation`</a>

##### <a name="Parametersusers.authenticationListOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationListPasswordMethods">Command `az identitysignins usersauthentication list-password-method`</a>

##### <a name="Parametersusers.authenticationListPasswordMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationListPasswordlessMicrosoftAuthenticatorMethods">Command `az identitysignins usersauthentication list-passwordless-microsoft-authenticator-method`</a>

##### <a name="Parametersusers.authenticationListPasswordlessMicrosoftAuthenticatorMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationListPhoneMethods">Command `az identitysignins usersauthentication list-phone-method`</a>

##### <a name="Parametersusers.authenticationListPhoneMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationListSecurityQuestionMethods">Command `az identitysignins usersauthentication list-security-question-method`</a>

##### <a name="Parametersusers.authenticationListSecurityQuestionMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationListTemporaryAccessPassMethods">Command `az identitysignins usersauthentication list-temporary-access-pass-method`</a>

##### <a name="Parametersusers.authenticationListTemporaryAccessPassMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationGetEmailMethods">Command `az identitysignins usersauthentication show-email-method`</a>

##### <a name="Parametersusers.authenticationGetEmailMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--email-authentication-method-id**|string|key: id of emailAuthenticationMethod|email_authentication_method_id|emailAuthenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationGetFido2Methods">Command `az identitysignins usersauthentication show-fido2-method`</a>

##### <a name="Parametersusers.authenticationGetFido2Methods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--fido2-authentication-method-id**|string|key: id of fido2AuthenticationMethod|fido2_authentication_method_id|fido2AuthenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationGetMethods">Command `az identitysignins usersauthentication show-method`</a>

##### <a name="Parametersusers.authenticationGetMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--authentication-method-id**|string|key: id of authenticationMethod|authentication_method_id|authenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationGetMicrosoftAuthenticatorMethods">Command `az identitysignins usersauthentication show-microsoft-authenticator-method`</a>

##### <a name="Parametersusers.authenticationGetMicrosoftAuthenticatorMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--microsoft-authenticator-authentication-method-id**|string|key: id of microsoftAuthenticatorAuthenticationMethod|microsoft_authenticator_authentication_method_id|microsoftAuthenticatorAuthenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationGetOathMethods">Command `az identitysignins usersauthentication show-oath-method`</a>

##### <a name="Parametersusers.authenticationGetOathMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--software-oath-authentication-method-id**|string|key: id of softwareOathAuthenticationMethod|software_oath_authentication_method_id|softwareOathAuthenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationGetOperations">Command `az identitysignins usersauthentication show-operation`</a>

##### <a name="Parametersusers.authenticationGetOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--long-running-operation-id**|string|key: id of longRunningOperation|long_running_operation_id|longRunningOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationGetPasswordMethods">Command `az identitysignins usersauthentication show-password-method`</a>

##### <a name="Parametersusers.authenticationGetPasswordMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--password-authentication-method-id**|string|key: id of passwordAuthenticationMethod|password_authentication_method_id|passwordAuthenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationGetPasswordlessMicrosoftAuthenticatorMethods">Command `az identitysignins usersauthentication show-passwordless-microsoft-authenticator-method`</a>

##### <a name="Parametersusers.authenticationGetPasswordlessMicrosoftAuthenticatorMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--passwordless-microsoft-authenticator-authentication-method-id**|string|key: id of passwordlessMicrosoftAuthenticatorAuthenticationMethod|passwordless_microsoft_authenticator_authentication_method_id|passwordlessMicrosoftAuthenticatorAuthenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationGetPhoneMethods">Command `az identitysignins usersauthentication show-phone-method`</a>

##### <a name="Parametersusers.authenticationGetPhoneMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--phone-authentication-method-id**|string|key: id of phoneAuthenticationMethod|phone_authentication_method_id|phoneAuthenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationGetSecurityQuestionMethods">Command `az identitysignins usersauthentication show-security-question-method`</a>

##### <a name="Parametersusers.authenticationGetSecurityQuestionMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--security-question-authentication-method-id**|string|key: id of securityQuestionAuthenticationMethod|security_question_authentication_method_id|securityQuestionAuthenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationGetTemporaryAccessPassMethods">Command `az identitysignins usersauthentication show-temporary-access-pass-method`</a>

##### <a name="Parametersusers.authenticationGetTemporaryAccessPassMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--temporary-access-pass-authentication-method-id**|string|key: id of temporaryAccessPassAuthenticationMethod|temporary_access_pass_authentication_method_id|temporaryAccessPassAuthenticationMethod-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.authenticationUpdateEmailMethods">Command `az identitysignins usersauthentication update-email-method`</a>

##### <a name="Parametersusers.authenticationUpdateEmailMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--email-authentication-method-id**|string|key: id of emailAuthenticationMethod|email_authentication_method_id|emailAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.authenticationUpdateFido2Methods">Command `az identitysignins usersauthentication update-fido2-method`</a>

##### <a name="Parametersusers.authenticationUpdateFido2Methods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--fido2-authentication-method-id**|string|key: id of fido2AuthenticationMethod|fido2_authentication_method_id|fido2AuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.authenticationUpdateMethods">Command `az identitysignins usersauthentication update-method`</a>

##### <a name="Parametersusers.authenticationUpdateMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--authentication-method-id**|string|key: id of authenticationMethod|authentication_method_id|authenticationMethod-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.authenticationUpdateMicrosoftAuthenticatorMethods">Command `az identitysignins usersauthentication update-microsoft-authenticator-method`</a>

##### <a name="Parametersusers.authenticationUpdateMicrosoftAuthenticatorMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--microsoft-authenticator-authentication-method-id**|string|key: id of microsoftAuthenticatorAuthenticationMethod|microsoft_authenticator_authentication_method_id|microsoftAuthenticatorAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.authenticationUpdateOathMethods">Command `az identitysignins usersauthentication update-oath-method`</a>

##### <a name="Parametersusers.authenticationUpdateOathMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--software-oath-authentication-method-id**|string|key: id of softwareOathAuthenticationMethod|software_oath_authentication_method_id|softwareOathAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.authenticationUpdateOperations">Command `az identitysignins usersauthentication update-operation`</a>

##### <a name="Parametersusers.authenticationUpdateOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--long-running-operation-id**|string|key: id of longRunningOperation|long_running_operation_id|longRunningOperation-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--last-action-date-time**|date-time||last_action_date_time|lastActionDateTime|
|**--resource-location**|string||resource_location|resourceLocation|
|**--status**|choice||status|status|
|**--status-detail**|string||status_detail|statusDetail|

#### <a name="users.authenticationUpdatePasswordMethods">Command `az identitysignins usersauthentication update-password-method`</a>

##### <a name="Parametersusers.authenticationUpdatePasswordMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--password-authentication-method-id**|string|key: id of passwordAuthenticationMethod|password_authentication_method_id|passwordAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|
|**--creation-date-time**|date-time||creation_date_time|creationDateTime|
|**--password**|string||password|password|

#### <a name="users.authenticationUpdatePasswordlessMicrosoftAuthenticatorMethods">Command `az identitysignins usersauthentication update-passwordless-microsoft-authenticator-method`</a>

##### <a name="Parametersusers.authenticationUpdatePasswordlessMicrosoftAuthenticatorMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--passwordless-microsoft-authenticator-authentication-method-id**|string|key: id of passwordlessMicrosoftAuthenticatorAuthenticationMethod|passwordless_microsoft_authenticator_authentication_method_id|passwordlessMicrosoftAuthenticatorAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.authenticationUpdatePhoneMethods">Command `az identitysignins usersauthentication update-phone-method`</a>

##### <a name="Parametersusers.authenticationUpdatePhoneMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--phone-authentication-method-id**|string|key: id of phoneAuthenticationMethod|phone_authentication_method_id|phoneAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|
|**--phone-number**|string||phone_number|phoneNumber|
|**--phone-type**|choice||phone_type|phoneType|
|**--sms-sign-in-state**|choice||sms_sign_in_state|smsSignInState|

#### <a name="users.authenticationUpdateSecurityQuestionMethods">Command `az identitysignins usersauthentication update-security-question-method`</a>

##### <a name="Parametersusers.authenticationUpdateSecurityQuestionMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--security-question-authentication-method-id**|string|key: id of securityQuestionAuthenticationMethod|security_question_authentication_method_id|securityQuestionAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.authenticationUpdateTemporaryAccessPassMethods">Command `az identitysignins usersauthentication update-temporary-access-pass-method`</a>

##### <a name="Parametersusers.authenticationUpdateTemporaryAccessPassMethods">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--temporary-access-pass-authentication-method-id**|string|key: id of temporaryAccessPassAuthenticationMethod|temporary_access_pass_authentication_method_id|temporaryAccessPassAuthenticationMethod-id|
|**--id**|string|Read-only.|id|id|
