# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az identitysignins_v1_0|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az identitysignins_v1_0` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az identitysignins data-policy-operation-data-policy-operation|dataPolicyOperations.dataPolicyOperation|[commands](#CommandsIndataPolicyOperations.dataPolicyOperation)|
|az identitysignins identity|identity|[commands](#CommandsInidentity)|
|az identitysignins identity-conditional-access|identity.conditionalAccess|[commands](#CommandsInidentity.conditionalAccess)|
|az identitysignins identity-provider-identity-provider|identityProviders.identityProvider|[commands](#CommandsInidentityProviders.identityProvider)|
|az identitysignins information-protection-information-protection|informationProtection.informationProtection|[commands](#CommandsIninformationProtection.informationProtection)|
|az identitysignins information-protection|informationProtection|[commands](#CommandsIninformationProtection)|
|az identitysignins information-protection-threat-assessment-request|informationProtection.threatAssessmentRequests|[commands](#CommandsIninformationProtection.threatAssessmentRequests)|
|az identitysignins invitation-invitation|invitations.invitation|[commands](#CommandsIninvitations.invitation)|
|az identitysignins invitation|invitations|[commands](#CommandsIninvitations)|
|az identitysignins oauth2-permission-grant-o-auth2-permission-grant|oauth2PermissionGrants.oAuth2PermissionGrant|[commands](#CommandsInoauth2PermissionGrants.oAuth2PermissionGrant)|
|az identitysignins oauth2-permission-grant|oauth2PermissionGrants|[commands](#CommandsInoauth2PermissionGrants)|
|az identitysignins organization|organization|[commands](#CommandsInorganization)|
|az identitysignins policy-policy-root|policies.policyRoot|[commands](#CommandsInpolicies.policyRoot)|
|az identitysignins policy|policies|[commands](#CommandsInpolicies)|
|az identitysignins policy-permission-grant-policy|policies.permissionGrantPolicies|[commands](#CommandsInpolicies.permissionGrantPolicies)|

## COMMANDS
### <a name="CommandsIndataPolicyOperations.dataPolicyOperation">Commands in `az identitysignins data-policy-operation-data-policy-operation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins data-policy-operation-data-policy-operation delete](#dataPolicyOperations.dataPolicyOperationDeleteDataPolicyOperation)|DeleteDataPolicyOperation|[Parameters](#ParametersdataPolicyOperations.dataPolicyOperationDeleteDataPolicyOperation)|Not Found|
|[az identitysignins data-policy-operation-data-policy-operation create-data-policy-operation](#dataPolicyOperations.dataPolicyOperationCreateDataPolicyOperation)|CreateDataPolicyOperation|[Parameters](#ParametersdataPolicyOperations.dataPolicyOperationCreateDataPolicyOperation)|Not Found|
|[az identitysignins data-policy-operation-data-policy-operation list-data-policy-operation](#dataPolicyOperations.dataPolicyOperationListDataPolicyOperation)|ListDataPolicyOperation|[Parameters](#ParametersdataPolicyOperations.dataPolicyOperationListDataPolicyOperation)|Not Found|
|[az identitysignins data-policy-operation-data-policy-operation show-data-policy-operation](#dataPolicyOperations.dataPolicyOperationGetDataPolicyOperation)|GetDataPolicyOperation|[Parameters](#ParametersdataPolicyOperations.dataPolicyOperationGetDataPolicyOperation)|Not Found|
|[az identitysignins data-policy-operation-data-policy-operation update-data-policy-operation](#dataPolicyOperations.dataPolicyOperationUpdateDataPolicyOperation)|UpdateDataPolicyOperation|[Parameters](#ParametersdataPolicyOperations.dataPolicyOperationUpdateDataPolicyOperation)|Not Found|

### <a name="CommandsInidentity">Commands in `az identitysignins identity` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins identity delete](#identityDeleteConditionalAccess)|DeleteConditionalAccess|[Parameters](#ParametersidentityDeleteConditionalAccess)|Not Found|
|[az identitysignins identity show-conditional-access](#identityGetConditionalAccess)|GetConditionalAccess|[Parameters](#ParametersidentityGetConditionalAccess)|Not Found|
|[az identitysignins identity update-conditional-access](#identityUpdateConditionalAccess)|UpdateConditionalAccess|[Parameters](#ParametersidentityUpdateConditionalAccess)|Not Found|

### <a name="CommandsInidentity.conditionalAccess">Commands in `az identitysignins identity-conditional-access` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins identity-conditional-access delete](#identity.conditionalAccessDeleteNamedLocations)|DeleteNamedLocations|[Parameters](#Parametersidentity.conditionalAccessDeleteNamedLocations)|Not Found|
|[az identitysignins identity-conditional-access delete](#identity.conditionalAccessDeletePolicies)|DeletePolicies|[Parameters](#Parametersidentity.conditionalAccessDeletePolicies)|Not Found|
|[az identitysignins identity-conditional-access create-named-location](#identity.conditionalAccessCreateNamedLocations)|CreateNamedLocations|[Parameters](#Parametersidentity.conditionalAccessCreateNamedLocations)|Not Found|
|[az identitysignins identity-conditional-access create-policy](#identity.conditionalAccessCreatePolicies)|CreatePolicies|[Parameters](#Parametersidentity.conditionalAccessCreatePolicies)|Not Found|
|[az identitysignins identity-conditional-access list-named-location](#identity.conditionalAccessListNamedLocations)|ListNamedLocations|[Parameters](#Parametersidentity.conditionalAccessListNamedLocations)|Not Found|
|[az identitysignins identity-conditional-access list-policy](#identity.conditionalAccessListPolicies)|ListPolicies|[Parameters](#Parametersidentity.conditionalAccessListPolicies)|Not Found|
|[az identitysignins identity-conditional-access show-named-location](#identity.conditionalAccessGetNamedLocations)|GetNamedLocations|[Parameters](#Parametersidentity.conditionalAccessGetNamedLocations)|Not Found|
|[az identitysignins identity-conditional-access show-policy](#identity.conditionalAccessGetPolicies)|GetPolicies|[Parameters](#Parametersidentity.conditionalAccessGetPolicies)|Not Found|
|[az identitysignins identity-conditional-access update-named-location](#identity.conditionalAccessUpdateNamedLocations)|UpdateNamedLocations|[Parameters](#Parametersidentity.conditionalAccessUpdateNamedLocations)|Not Found|
|[az identitysignins identity-conditional-access update-policy](#identity.conditionalAccessUpdatePolicies)|UpdatePolicies|[Parameters](#Parametersidentity.conditionalAccessUpdatePolicies)|Not Found|

### <a name="CommandsInidentityProviders.identityProvider">Commands in `az identitysignins identity-provider-identity-provider` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins identity-provider-identity-provider delete](#identityProviders.identityProviderDeleteIdentityProvider)|DeleteIdentityProvider|[Parameters](#ParametersidentityProviders.identityProviderDeleteIdentityProvider)|Not Found|
|[az identitysignins identity-provider-identity-provider create-identity-provider](#identityProviders.identityProviderCreateIdentityProvider)|CreateIdentityProvider|[Parameters](#ParametersidentityProviders.identityProviderCreateIdentityProvider)|Not Found|
|[az identitysignins identity-provider-identity-provider list-identity-provider](#identityProviders.identityProviderListIdentityProvider)|ListIdentityProvider|[Parameters](#ParametersidentityProviders.identityProviderListIdentityProvider)|Not Found|
|[az identitysignins identity-provider-identity-provider show-identity-provider](#identityProviders.identityProviderGetIdentityProvider)|GetIdentityProvider|[Parameters](#ParametersidentityProviders.identityProviderGetIdentityProvider)|Not Found|
|[az identitysignins identity-provider-identity-provider update-identity-provider](#identityProviders.identityProviderUpdateIdentityProvider)|UpdateIdentityProvider|[Parameters](#ParametersidentityProviders.identityProviderUpdateIdentityProvider)|Not Found|

### <a name="CommandsIninformationProtection">Commands in `az identitysignins information-protection` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins information-protection delete](#informationProtectionDeleteThreatAssessmentRequests)|DeleteThreatAssessmentRequests|[Parameters](#ParametersinformationProtectionDeleteThreatAssessmentRequests)|Not Found|
|[az identitysignins information-protection create-threat-assessment-request](#informationProtectionCreateThreatAssessmentRequests)|CreateThreatAssessmentRequests|[Parameters](#ParametersinformationProtectionCreateThreatAssessmentRequests)|Not Found|
|[az identitysignins information-protection list-threat-assessment-request](#informationProtectionListThreatAssessmentRequests)|ListThreatAssessmentRequests|[Parameters](#ParametersinformationProtectionListThreatAssessmentRequests)|Not Found|
|[az identitysignins information-protection show-threat-assessment-request](#informationProtectionGetThreatAssessmentRequests)|GetThreatAssessmentRequests|[Parameters](#ParametersinformationProtectionGetThreatAssessmentRequests)|Not Found|
|[az identitysignins information-protection update-threat-assessment-request](#informationProtectionUpdateThreatAssessmentRequests)|UpdateThreatAssessmentRequests|[Parameters](#ParametersinformationProtectionUpdateThreatAssessmentRequests)|Not Found|

### <a name="CommandsIninformationProtection.informationProtection">Commands in `az identitysignins information-protection-information-protection` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins information-protection-information-protection show-information-protection](#informationProtection.informationProtectionGetInformationProtection)|GetInformationProtection|[Parameters](#ParametersinformationProtection.informationProtectionGetInformationProtection)|Not Found|
|[az identitysignins information-protection-information-protection update-information-protection](#informationProtection.informationProtectionUpdateInformationProtection)|UpdateInformationProtection|[Parameters](#ParametersinformationProtection.informationProtectionUpdateInformationProtection)|Not Found|

### <a name="CommandsIninformationProtection.threatAssessmentRequests">Commands in `az identitysignins information-protection-threat-assessment-request` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins information-protection-threat-assessment-request delete](#informationProtection.threatAssessmentRequestsDeleteResults)|DeleteResults|[Parameters](#ParametersinformationProtection.threatAssessmentRequestsDeleteResults)|Not Found|
|[az identitysignins information-protection-threat-assessment-request create-result](#informationProtection.threatAssessmentRequestsCreateResults)|CreateResults|[Parameters](#ParametersinformationProtection.threatAssessmentRequestsCreateResults)|Not Found|
|[az identitysignins information-protection-threat-assessment-request list-result](#informationProtection.threatAssessmentRequestsListResults)|ListResults|[Parameters](#ParametersinformationProtection.threatAssessmentRequestsListResults)|Not Found|
|[az identitysignins information-protection-threat-assessment-request show-result](#informationProtection.threatAssessmentRequestsGetResults)|GetResults|[Parameters](#ParametersinformationProtection.threatAssessmentRequestsGetResults)|Not Found|
|[az identitysignins information-protection-threat-assessment-request update-result](#informationProtection.threatAssessmentRequestsUpdateResults)|UpdateResults|[Parameters](#ParametersinformationProtection.threatAssessmentRequestsUpdateResults)|Not Found|

### <a name="CommandsIninvitations">Commands in `az identitysignins invitation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins invitation delete](#invitationsDeleteRefInvitedUser)|DeleteRefInvitedUser|[Parameters](#ParametersinvitationsDeleteRefInvitedUser)|Not Found|
|[az identitysignins invitation set-ref-invited-user](#invitationsSetRefInvitedUser)|SetRefInvitedUser|[Parameters](#ParametersinvitationsSetRefInvitedUser)|Not Found|
|[az identitysignins invitation show-invited-user](#invitationsGetInvitedUser)|GetInvitedUser|[Parameters](#ParametersinvitationsGetInvitedUser)|Not Found|
|[az identitysignins invitation show-ref-invited-user](#invitationsGetRefInvitedUser)|GetRefInvitedUser|[Parameters](#ParametersinvitationsGetRefInvitedUser)|Not Found|

### <a name="CommandsIninvitations.invitation">Commands in `az identitysignins invitation-invitation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins invitation-invitation delete](#invitations.invitationDeleteInvitation)|DeleteInvitation|[Parameters](#Parametersinvitations.invitationDeleteInvitation)|Not Found|
|[az identitysignins invitation-invitation create-invitation](#invitations.invitationCreateInvitation)|CreateInvitation|[Parameters](#Parametersinvitations.invitationCreateInvitation)|Not Found|
|[az identitysignins invitation-invitation list-invitation](#invitations.invitationListInvitation)|ListInvitation|[Parameters](#Parametersinvitations.invitationListInvitation)|Not Found|
|[az identitysignins invitation-invitation show-invitation](#invitations.invitationGetInvitation)|GetInvitation|[Parameters](#Parametersinvitations.invitationGetInvitation)|Not Found|
|[az identitysignins invitation-invitation update-invitation](#invitations.invitationUpdateInvitation)|UpdateInvitation|[Parameters](#Parametersinvitations.invitationUpdateInvitation)|Not Found|

### <a name="CommandsInoauth2PermissionGrants">Commands in `az identitysignins oauth2-permission-grant` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins oauth2-permission-grant delta](#oauth2PermissionGrantsdelta)|delta|[Parameters](#Parametersoauth2PermissionGrantsdelta)|Not Found|

### <a name="CommandsInoauth2PermissionGrants.oAuth2PermissionGrant">Commands in `az identitysignins oauth2-permission-grant-o-auth2-permission-grant` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins oauth2-permission-grant-o-auth2-permission-grant delete](#oauth2PermissionGrants.oAuth2PermissionGrantDeleteOAuth2PermissionGrant)|DeleteOAuth2PermissionGrant|[Parameters](#Parametersoauth2PermissionGrants.oAuth2PermissionGrantDeleteOAuth2PermissionGrant)|Not Found|
|[az identitysignins oauth2-permission-grant-o-auth2-permission-grant create-o-auth2-permission-grant](#oauth2PermissionGrants.oAuth2PermissionGrantCreateOAuth2PermissionGrant)|CreateOAuth2PermissionGrant|[Parameters](#Parametersoauth2PermissionGrants.oAuth2PermissionGrantCreateOAuth2PermissionGrant)|Not Found|
|[az identitysignins oauth2-permission-grant-o-auth2-permission-grant list-o-auth2-permission-grant](#oauth2PermissionGrants.oAuth2PermissionGrantListOAuth2PermissionGrant)|ListOAuth2PermissionGrant|[Parameters](#Parametersoauth2PermissionGrants.oAuth2PermissionGrantListOAuth2PermissionGrant)|Not Found|
|[az identitysignins oauth2-permission-grant-o-auth2-permission-grant show-o-auth2-permission-grant](#oauth2PermissionGrants.oAuth2PermissionGrantGetOAuth2PermissionGrant)|GetOAuth2PermissionGrant|[Parameters](#Parametersoauth2PermissionGrants.oAuth2PermissionGrantGetOAuth2PermissionGrant)|Not Found|
|[az identitysignins oauth2-permission-grant-o-auth2-permission-grant update-o-auth2-permission-grant](#oauth2PermissionGrants.oAuth2PermissionGrantUpdateOAuth2PermissionGrant)|UpdateOAuth2PermissionGrant|[Parameters](#Parametersoauth2PermissionGrants.oAuth2PermissionGrantUpdateOAuth2PermissionGrant)|Not Found|

### <a name="CommandsInorganization">Commands in `az identitysignins organization` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins organization create-ref-certificate-based-auth-configuration](#organizationCreateRefCertificateBasedAuthConfiguration)|CreateRefCertificateBasedAuthConfiguration|[Parameters](#ParametersorganizationCreateRefCertificateBasedAuthConfiguration)|Not Found|
|[az identitysignins organization list-certificate-based-auth-configuration](#organizationListCertificateBasedAuthConfiguration)|ListCertificateBasedAuthConfiguration|[Parameters](#ParametersorganizationListCertificateBasedAuthConfiguration)|Not Found|
|[az identitysignins organization list-ref-certificate-based-auth-configuration](#organizationListRefCertificateBasedAuthConfiguration)|ListRefCertificateBasedAuthConfiguration|[Parameters](#ParametersorganizationListRefCertificateBasedAuthConfiguration)|Not Found|

### <a name="CommandsInpolicies">Commands in `az identitysignins policy` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins policy delete](#policiesDeleteActivityBasedTimeoutPolicies)|DeleteActivityBasedTimeoutPolicies|[Parameters](#ParameterspoliciesDeleteActivityBasedTimeoutPolicies)|Not Found|
|[az identitysignins policy delete](#policiesDeleteClaimsMappingPolicies)|DeleteClaimsMappingPolicies|[Parameters](#ParameterspoliciesDeleteClaimsMappingPolicies)|Not Found|
|[az identitysignins policy delete](#policiesDeleteConditionalAccessPolicies)|DeleteConditionalAccessPolicies|[Parameters](#ParameterspoliciesDeleteConditionalAccessPolicies)|Not Found|
|[az identitysignins policy delete](#policiesDeleteHomeRealmDiscoveryPolicies)|DeleteHomeRealmDiscoveryPolicies|[Parameters](#ParameterspoliciesDeleteHomeRealmDiscoveryPolicies)|Not Found|
|[az identitysignins policy delete](#policiesDeletePermissionGrantPolicies)|DeletePermissionGrantPolicies|[Parameters](#ParameterspoliciesDeletePermissionGrantPolicies)|Not Found|
|[az identitysignins policy delete](#policiesDeleteTokenIssuancePolicies)|DeleteTokenIssuancePolicies|[Parameters](#ParameterspoliciesDeleteTokenIssuancePolicies)|Not Found|
|[az identitysignins policy delete](#policiesDeleteTokenLifetimePolicies)|DeleteTokenLifetimePolicies|[Parameters](#ParameterspoliciesDeleteTokenLifetimePolicies)|Not Found|
|[az identitysignins policy delete](#policiesDeleteIdentitySecurityDefaultsEnforcementPolicy)|DeleteIdentitySecurityDefaultsEnforcementPolicy|[Parameters](#ParameterspoliciesDeleteIdentitySecurityDefaultsEnforcementPolicy)|Not Found|
|[az identitysignins policy create-activity-based-timeout-policy](#policiesCreateActivityBasedTimeoutPolicies)|CreateActivityBasedTimeoutPolicies|[Parameters](#ParameterspoliciesCreateActivityBasedTimeoutPolicies)|Not Found|
|[az identitysignins policy create-claim-mapping-policy](#policiesCreateClaimsMappingPolicies)|CreateClaimsMappingPolicies|[Parameters](#ParameterspoliciesCreateClaimsMappingPolicies)|Not Found|
|[az identitysignins policy create-conditional-access-policy](#policiesCreateConditionalAccessPolicies)|CreateConditionalAccessPolicies|[Parameters](#ParameterspoliciesCreateConditionalAccessPolicies)|Not Found|
|[az identitysignins policy create-home-realm-discovery-policy](#policiesCreateHomeRealmDiscoveryPolicies)|CreateHomeRealmDiscoveryPolicies|[Parameters](#ParameterspoliciesCreateHomeRealmDiscoveryPolicies)|Not Found|
|[az identitysignins policy create-permission-grant-policy](#policiesCreatePermissionGrantPolicies)|CreatePermissionGrantPolicies|[Parameters](#ParameterspoliciesCreatePermissionGrantPolicies)|Not Found|
|[az identitysignins policy create-token-issuance-policy](#policiesCreateTokenIssuancePolicies)|CreateTokenIssuancePolicies|[Parameters](#ParameterspoliciesCreateTokenIssuancePolicies)|Not Found|
|[az identitysignins policy create-token-lifetime-policy](#policiesCreateTokenLifetimePolicies)|CreateTokenLifetimePolicies|[Parameters](#ParameterspoliciesCreateTokenLifetimePolicies)|Not Found|
|[az identitysignins policy list-activity-based-timeout-policy](#policiesListActivityBasedTimeoutPolicies)|ListActivityBasedTimeoutPolicies|[Parameters](#ParameterspoliciesListActivityBasedTimeoutPolicies)|Not Found|
|[az identitysignins policy list-claim-mapping-policy](#policiesListClaimsMappingPolicies)|ListClaimsMappingPolicies|[Parameters](#ParameterspoliciesListClaimsMappingPolicies)|Not Found|
|[az identitysignins policy list-conditional-access-policy](#policiesListConditionalAccessPolicies)|ListConditionalAccessPolicies|[Parameters](#ParameterspoliciesListConditionalAccessPolicies)|Not Found|
|[az identitysignins policy list-home-realm-discovery-policy](#policiesListHomeRealmDiscoveryPolicies)|ListHomeRealmDiscoveryPolicies|[Parameters](#ParameterspoliciesListHomeRealmDiscoveryPolicies)|Not Found|
|[az identitysignins policy list-permission-grant-policy](#policiesListPermissionGrantPolicies)|ListPermissionGrantPolicies|[Parameters](#ParameterspoliciesListPermissionGrantPolicies)|Not Found|
|[az identitysignins policy list-token-issuance-policy](#policiesListTokenIssuancePolicies)|ListTokenIssuancePolicies|[Parameters](#ParameterspoliciesListTokenIssuancePolicies)|Not Found|
|[az identitysignins policy list-token-lifetime-policy](#policiesListTokenLifetimePolicies)|ListTokenLifetimePolicies|[Parameters](#ParameterspoliciesListTokenLifetimePolicies)|Not Found|
|[az identitysignins policy show-activity-based-timeout-policy](#policiesGetActivityBasedTimeoutPolicies)|GetActivityBasedTimeoutPolicies|[Parameters](#ParameterspoliciesGetActivityBasedTimeoutPolicies)|Not Found|
|[az identitysignins policy show-claim-mapping-policy](#policiesGetClaimsMappingPolicies)|GetClaimsMappingPolicies|[Parameters](#ParameterspoliciesGetClaimsMappingPolicies)|Not Found|
|[az identitysignins policy show-conditional-access-policy](#policiesGetConditionalAccessPolicies)|GetConditionalAccessPolicies|[Parameters](#ParameterspoliciesGetConditionalAccessPolicies)|Not Found|
|[az identitysignins policy show-home-realm-discovery-policy](#policiesGetHomeRealmDiscoveryPolicies)|GetHomeRealmDiscoveryPolicies|[Parameters](#ParameterspoliciesGetHomeRealmDiscoveryPolicies)|Not Found|
|[az identitysignins policy show-identity-security-default-enforcement-policy](#policiesGetIdentitySecurityDefaultsEnforcementPolicy)|GetIdentitySecurityDefaultsEnforcementPolicy|[Parameters](#ParameterspoliciesGetIdentitySecurityDefaultsEnforcementPolicy)|Not Found|
|[az identitysignins policy show-permission-grant-policy](#policiesGetPermissionGrantPolicies)|GetPermissionGrantPolicies|[Parameters](#ParameterspoliciesGetPermissionGrantPolicies)|Not Found|
|[az identitysignins policy show-token-issuance-policy](#policiesGetTokenIssuancePolicies)|GetTokenIssuancePolicies|[Parameters](#ParameterspoliciesGetTokenIssuancePolicies)|Not Found|
|[az identitysignins policy show-token-lifetime-policy](#policiesGetTokenLifetimePolicies)|GetTokenLifetimePolicies|[Parameters](#ParameterspoliciesGetTokenLifetimePolicies)|Not Found|
|[az identitysignins policy update-activity-based-timeout-policy](#policiesUpdateActivityBasedTimeoutPolicies)|UpdateActivityBasedTimeoutPolicies|[Parameters](#ParameterspoliciesUpdateActivityBasedTimeoutPolicies)|Not Found|
|[az identitysignins policy update-claim-mapping-policy](#policiesUpdateClaimsMappingPolicies)|UpdateClaimsMappingPolicies|[Parameters](#ParameterspoliciesUpdateClaimsMappingPolicies)|Not Found|
|[az identitysignins policy update-conditional-access-policy](#policiesUpdateConditionalAccessPolicies)|UpdateConditionalAccessPolicies|[Parameters](#ParameterspoliciesUpdateConditionalAccessPolicies)|Not Found|
|[az identitysignins policy update-home-realm-discovery-policy](#policiesUpdateHomeRealmDiscoveryPolicies)|UpdateHomeRealmDiscoveryPolicies|[Parameters](#ParameterspoliciesUpdateHomeRealmDiscoveryPolicies)|Not Found|
|[az identitysignins policy update-identity-security-default-enforcement-policy](#policiesUpdateIdentitySecurityDefaultsEnforcementPolicy)|UpdateIdentitySecurityDefaultsEnforcementPolicy|[Parameters](#ParameterspoliciesUpdateIdentitySecurityDefaultsEnforcementPolicy)|Not Found|
|[az identitysignins policy update-permission-grant-policy](#policiesUpdatePermissionGrantPolicies)|UpdatePermissionGrantPolicies|[Parameters](#ParameterspoliciesUpdatePermissionGrantPolicies)|Not Found|
|[az identitysignins policy update-token-issuance-policy](#policiesUpdateTokenIssuancePolicies)|UpdateTokenIssuancePolicies|[Parameters](#ParameterspoliciesUpdateTokenIssuancePolicies)|Not Found|
|[az identitysignins policy update-token-lifetime-policy](#policiesUpdateTokenLifetimePolicies)|UpdateTokenLifetimePolicies|[Parameters](#ParameterspoliciesUpdateTokenLifetimePolicies)|Not Found|

### <a name="CommandsInpolicies.permissionGrantPolicies">Commands in `az identitysignins policy-permission-grant-policy` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins policy-permission-grant-policy delete](#policies.permissionGrantPoliciesDeleteExcludes)|DeleteExcludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesDeleteExcludes)|Not Found|
|[az identitysignins policy-permission-grant-policy delete](#policies.permissionGrantPoliciesDeleteIncludes)|DeleteIncludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesDeleteIncludes)|Not Found|
|[az identitysignins policy-permission-grant-policy create-exclude](#policies.permissionGrantPoliciesCreateExcludes)|CreateExcludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesCreateExcludes)|Not Found|
|[az identitysignins policy-permission-grant-policy create-include](#policies.permissionGrantPoliciesCreateIncludes)|CreateIncludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesCreateIncludes)|Not Found|
|[az identitysignins policy-permission-grant-policy list-exclude](#policies.permissionGrantPoliciesListExcludes)|ListExcludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesListExcludes)|Not Found|
|[az identitysignins policy-permission-grant-policy list-include](#policies.permissionGrantPoliciesListIncludes)|ListIncludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesListIncludes)|Not Found|
|[az identitysignins policy-permission-grant-policy show-exclude](#policies.permissionGrantPoliciesGetExcludes)|GetExcludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesGetExcludes)|Not Found|
|[az identitysignins policy-permission-grant-policy show-include](#policies.permissionGrantPoliciesGetIncludes)|GetIncludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesGetIncludes)|Not Found|
|[az identitysignins policy-permission-grant-policy update-exclude](#policies.permissionGrantPoliciesUpdateExcludes)|UpdateExcludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesUpdateExcludes)|Not Found|
|[az identitysignins policy-permission-grant-policy update-include](#policies.permissionGrantPoliciesUpdateIncludes)|UpdateIncludes|[Parameters](#Parameterspolicies.permissionGrantPoliciesUpdateIncludes)|Not Found|

### <a name="CommandsInpolicies.policyRoot">Commands in `az identitysignins policy-policy-root` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az identitysignins policy-policy-root show-policy-root](#policies.policyRootGetPolicyRoot)|GetPolicyRoot|[Parameters](#Parameterspolicies.policyRootGetPolicyRoot)|Not Found|
|[az identitysignins policy-policy-root update-policy-root](#policies.policyRootUpdatePolicyRoot)|UpdatePolicyRoot|[Parameters](#Parameterspolicies.policyRootUpdatePolicyRoot)|Not Found|


## COMMAND DETAILS

### group `az identitysignins data-policy-operation-data-policy-operation`
#### <a name="dataPolicyOperations.dataPolicyOperationDeleteDataPolicyOperation">Command `az identitysignins data-policy-operation-data-policy-operation delete`</a>

##### <a name="ParametersdataPolicyOperations.dataPolicyOperationDeleteDataPolicyOperation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--data-policy-operation-id**|string|key: id of dataPolicyOperation|data_policy_operation_id|dataPolicyOperation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="dataPolicyOperations.dataPolicyOperationCreateDataPolicyOperation">Command `az identitysignins data-policy-operation-data-policy-operation create-data-policy-operation`</a>

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

#### <a name="dataPolicyOperations.dataPolicyOperationListDataPolicyOperation">Command `az identitysignins data-policy-operation-data-policy-operation list-data-policy-operation`</a>

##### <a name="ParametersdataPolicyOperations.dataPolicyOperationListDataPolicyOperation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="dataPolicyOperations.dataPolicyOperationGetDataPolicyOperation">Command `az identitysignins data-policy-operation-data-policy-operation show-data-policy-operation`</a>

##### <a name="ParametersdataPolicyOperations.dataPolicyOperationGetDataPolicyOperation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--data-policy-operation-id**|string|key: id of dataPolicyOperation|data_policy_operation_id|dataPolicyOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="dataPolicyOperations.dataPolicyOperationUpdateDataPolicyOperation">Command `az identitysignins data-policy-operation-data-policy-operation update-data-policy-operation`</a>

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
#### <a name="identityDeleteConditionalAccess">Command `az identitysignins identity delete`</a>

##### <a name="ParametersidentityDeleteConditionalAccess">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="identityGetConditionalAccess">Command `az identitysignins identity show-conditional-access`</a>

##### <a name="ParametersidentityGetConditionalAccess">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identityUpdateConditionalAccess">Command `az identitysignins identity update-conditional-access`</a>

##### <a name="ParametersidentityUpdateConditionalAccess">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--named-locations**|array||named_locations|namedLocations|
|**--policies**|array||policies|policies|

### group `az identitysignins identity-conditional-access`
#### <a name="identity.conditionalAccessDeleteNamedLocations">Command `az identitysignins identity-conditional-access delete`</a>

##### <a name="Parametersidentity.conditionalAccessDeleteNamedLocations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--named-location-id**|string|key: id of namedLocation|named_location_id|namedLocation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="identity.conditionalAccessDeletePolicies">Command `az identitysignins identity-conditional-access delete`</a>

##### <a name="Parametersidentity.conditionalAccessDeletePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--conditional-access-policy-id**|string|key: id of conditionalAccessPolicy|conditional_access_policy_id|conditionalAccessPolicy-id|

#### <a name="identity.conditionalAccessCreateNamedLocations">Command `az identitysignins identity-conditional-access create-named-location`</a>

##### <a name="Parametersidentity.conditionalAccessCreateNamedLocations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents creation date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|Human-readable name of the location.|display_name|displayName|
|**--modified-date-time**|date-time|The Timestamp type represents last modified date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|modified_date_time|modifiedDateTime|

#### <a name="identity.conditionalAccessCreatePolicies">Command `az identitysignins identity-conditional-access create-policy`</a>

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
|**--client-app-types**|array|Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other.|client_app_types|clientAppTypes|
|**--locations**|object|conditionalAccessLocations|locations|locations|
|**--platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--sign-in-risk-levels**|array|Risk levels included in the policy. Possible values are: low, medium, high, none.|sign_in_risk_levels|signInRiskLevels|
|**--users**|object|conditionalAccessUsers|users|users|

#### <a name="identity.conditionalAccessListNamedLocations">Command `az identitysignins identity-conditional-access list-named-location`</a>

##### <a name="Parametersidentity.conditionalAccessListNamedLocations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identity.conditionalAccessListPolicies">Command `az identitysignins identity-conditional-access list-policy`</a>

##### <a name="Parametersidentity.conditionalAccessListPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identity.conditionalAccessGetNamedLocations">Command `az identitysignins identity-conditional-access show-named-location`</a>

##### <a name="Parametersidentity.conditionalAccessGetNamedLocations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--named-location-id**|string|key: id of namedLocation|named_location_id|namedLocation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identity.conditionalAccessGetPolicies">Command `az identitysignins identity-conditional-access show-policy`</a>

##### <a name="Parametersidentity.conditionalAccessGetPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--conditional-access-policy-id**|string|key: id of conditionalAccessPolicy|conditional_access_policy_id|conditionalAccessPolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identity.conditionalAccessUpdateNamedLocations">Command `az identitysignins identity-conditional-access update-named-location`</a>

##### <a name="Parametersidentity.conditionalAccessUpdateNamedLocations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--named-location-id**|string|key: id of namedLocation|named_location_id|namedLocation-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents creation date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|created_date_time|createdDateTime|
|**--display-name**|string|Human-readable name of the location.|display_name|displayName|
|**--modified-date-time**|date-time|The Timestamp type represents last modified date and time of the location using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.|modified_date_time|modifiedDateTime|

#### <a name="identity.conditionalAccessUpdatePolicies">Command `az identitysignins identity-conditional-access update-policy`</a>

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
|**--client-app-types**|array|Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other.|client_app_types|clientAppTypes|
|**--locations**|object|conditionalAccessLocations|locations|locations|
|**--platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--sign-in-risk-levels**|array|Risk levels included in the policy. Possible values are: low, medium, high, none.|sign_in_risk_levels|signInRiskLevels|
|**--users**|object|conditionalAccessUsers|users|users|

### group `az identitysignins identity-provider-identity-provider`
#### <a name="identityProviders.identityProviderDeleteIdentityProvider">Command `az identitysignins identity-provider-identity-provider delete`</a>

##### <a name="ParametersidentityProviders.identityProviderDeleteIdentityProvider">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-provider-id**|string|key: id of identityProvider|identity_provider_id|identityProvider-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="identityProviders.identityProviderCreateIdentityProvider">Command `az identitysignins identity-provider-identity-provider create-identity-provider`</a>

##### <a name="ParametersidentityProviders.identityProviderCreateIdentityProvider">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--client-id**|string||client_id|clientId|
|**--client-secret**|string||client_secret|clientSecret|
|**--name**|string||name|name|
|**--type**|string||type|type|

#### <a name="identityProviders.identityProviderListIdentityProvider">Command `az identitysignins identity-provider-identity-provider list-identity-provider`</a>

##### <a name="ParametersidentityProviders.identityProviderListIdentityProvider">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identityProviders.identityProviderGetIdentityProvider">Command `az identitysignins identity-provider-identity-provider show-identity-provider`</a>

##### <a name="ParametersidentityProviders.identityProviderGetIdentityProvider">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-provider-id**|string|key: id of identityProvider|identity_provider_id|identityProvider-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="identityProviders.identityProviderUpdateIdentityProvider">Command `az identitysignins identity-provider-identity-provider update-identity-provider`</a>

##### <a name="ParametersidentityProviders.identityProviderUpdateIdentityProvider">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--identity-provider-id**|string|key: id of identityProvider|identity_provider_id|identityProvider-id|
|**--id**|string|Read-only.|id|id|
|**--client-id**|string||client_id|clientId|
|**--client-secret**|string||client_secret|clientSecret|
|**--name**|string||name|name|
|**--type**|string||type|type|

### group `az identitysignins information-protection`
#### <a name="informationProtectionDeleteThreatAssessmentRequests">Command `az identitysignins information-protection delete`</a>

##### <a name="ParametersinformationProtectionDeleteThreatAssessmentRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="informationProtectionCreateThreatAssessmentRequests">Command `az identitysignins information-protection create-threat-assessment-request`</a>

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

#### <a name="informationProtectionListThreatAssessmentRequests">Command `az identitysignins information-protection list-threat-assessment-request`</a>

##### <a name="ParametersinformationProtectionListThreatAssessmentRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtectionGetThreatAssessmentRequests">Command `az identitysignins information-protection show-threat-assessment-request`</a>

##### <a name="ParametersinformationProtectionGetThreatAssessmentRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtectionUpdateThreatAssessmentRequests">Command `az identitysignins information-protection update-threat-assessment-request`</a>

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

### group `az identitysignins information-protection-information-protection`
#### <a name="informationProtection.informationProtectionGetInformationProtection">Command `az identitysignins information-protection-information-protection show-information-protection`</a>

##### <a name="ParametersinformationProtection.informationProtectionGetInformationProtection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtection.informationProtectionUpdateInformationProtection">Command `az identitysignins information-protection-information-protection update-information-protection`</a>

##### <a name="ParametersinformationProtection.informationProtectionUpdateInformationProtection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--threat-assessment-requests**|array||threat_assessment_requests|threatAssessmentRequests|

### group `az identitysignins information-protection-threat-assessment-request`
#### <a name="informationProtection.threatAssessmentRequestsDeleteResults">Command `az identitysignins information-protection-threat-assessment-request delete`</a>

##### <a name="ParametersinformationProtection.threatAssessmentRequestsDeleteResults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--threat-assessment-result-id**|string|key: id of threatAssessmentResult|threat_assessment_result_id|threatAssessmentResult-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="informationProtection.threatAssessmentRequestsCreateResults">Command `az identitysignins information-protection-threat-assessment-request create-result`</a>

##### <a name="ParametersinformationProtection.threatAssessmentRequestsCreateResults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'.|created_date_time|createdDateTime|
|**--message**|string|The result message for each threat assessment.|message|message|
|**--result-type**|choice||result_type|resultType|

#### <a name="informationProtection.threatAssessmentRequestsListResults">Command `az identitysignins information-protection-threat-assessment-request list-result`</a>

##### <a name="ParametersinformationProtection.threatAssessmentRequestsListResults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtection.threatAssessmentRequestsGetResults">Command `az identitysignins information-protection-threat-assessment-request show-result`</a>

##### <a name="ParametersinformationProtection.threatAssessmentRequestsGetResults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--threat-assessment-request-id**|string|key: id of threatAssessmentRequest|threat_assessment_request_id|threatAssessmentRequest-id|
|**--threat-assessment-result-id**|string|key: id of threatAssessmentResult|threat_assessment_result_id|threatAssessmentResult-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="informationProtection.threatAssessmentRequestsUpdateResults">Command `az identitysignins information-protection-threat-assessment-request update-result`</a>

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
#### <a name="invitationsDeleteRefInvitedUser">Command `az identitysignins invitation delete`</a>

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

### group `az identitysignins invitation-invitation`
#### <a name="invitations.invitationDeleteInvitation">Command `az identitysignins invitation-invitation delete`</a>

##### <a name="Parametersinvitations.invitationDeleteInvitation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: id of invitation|invitation_id|invitation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="invitations.invitationCreateInvitation">Command `az identitysignins invitation-invitation create-invitation`</a>

##### <a name="Parametersinvitations.invitationCreateInvitation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--invited-user-display-name**|string|The display name of the user being invited.|invited_user_display_name|invitedUserDisplayName|
|**--invited-user-email-address**|string|The email address of the user being invited. Required. The following special characters are not permitted in the email address:Tilde (~)Exclamation point (!)Number sign (#)Dollar sign ($)Percent (%)Circumflex (^)Ampersand (&)Asterisk (*)Parentheses (( ))Plus sign (+)Equal sign (=)Brackets ([ ])Braces ({ })Backslash (/)Slash mark (/)Pipe (/|)Semicolon (;)Colon (:)Quotation marks (')Angle brackets (< >)Question mark (?)Comma (,)However, the following exceptions apply:A period (.) or a hyphen (-) is permitted anywhere in the user name, except at the beginning or end of the name.An underscore (_) is permitted anywhere in the user name. This includes at the beginning or end of the name.|invited_user_email_address|invitedUserEmailAddress|
|**--invited-user-type**|string|The userType of the user being invited. By default, this is Guest. You can invite as Member if you are a company administrator.|invited_user_type|invitedUserType|
|**--invite-redeem-url**|string|The URL the user can use to redeem their invitation. Read-only|invite_redeem_url|inviteRedeemUrl|
|**--invite-redirect-url**|string|The URL the user should be redirected to once the invitation is redeemed. Required.|invite_redirect_url|inviteRedirectUrl|
|**--send-invitation-message**|boolean|Indicates whether an email should be sent to the user being invited or not. The default is false.|send_invitation_message|sendInvitationMessage|
|**--status**|string|The status of the invitation. Possible values: PendingAcceptance, Completed, InProgress, and Error|status|status|
|**--invited-user**|object|Represents an Azure Active Directory user object.|invited_user|invitedUser|
|**--cc-recipients**|array|Additional recipients the invitation message should be sent to. Currently only 1 additional recipient is supported.|cc_recipients|ccRecipients|
|**--customized-message-body**|string|Customized message body you want to send if you don't want the default message.|customized_message_body|customizedMessageBody|
|**--message-language**|string|The language you want to send the default message in. If the customizedMessageBody is specified, this property is ignored, and the message is sent using the customizedMessageBody. The language format should be in ISO 639. The default is en-US.|message_language|messageLanguage|

#### <a name="invitations.invitationListInvitation">Command `az identitysignins invitation-invitation list-invitation`</a>

##### <a name="Parametersinvitations.invitationListInvitation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="invitations.invitationGetInvitation">Command `az identitysignins invitation-invitation show-invitation`</a>

##### <a name="Parametersinvitations.invitationGetInvitation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--invitation-id**|string|key: id of invitation|invitation_id|invitation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="invitations.invitationUpdateInvitation">Command `az identitysignins invitation-invitation update-invitation`</a>

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
|**--send-invitation-message**|boolean|Indicates whether an email should be sent to the user being invited or not. The default is false.|send_invitation_message|sendInvitationMessage|
|**--status**|string|The status of the invitation. Possible values: PendingAcceptance, Completed, InProgress, and Error|status|status|
|**--invited-user**|object|Represents an Azure Active Directory user object.|invited_user|invitedUser|
|**--cc-recipients**|array|Additional recipients the invitation message should be sent to. Currently only 1 additional recipient is supported.|cc_recipients|ccRecipients|
|**--customized-message-body**|string|Customized message body you want to send if you don't want the default message.|customized_message_body|customizedMessageBody|
|**--message-language**|string|The language you want to send the default message in. If the customizedMessageBody is specified, this property is ignored, and the message is sent using the customizedMessageBody. The language format should be in ISO 639. The default is en-US.|message_language|messageLanguage|

### group `az identitysignins oauth2-permission-grant`
#### <a name="oauth2PermissionGrantsdelta">Command `az identitysignins oauth2-permission-grant delta`</a>

##### <a name="Parametersoauth2PermissionGrantsdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
### group `az identitysignins oauth2-permission-grant-o-auth2-permission-grant`
#### <a name="oauth2PermissionGrants.oAuth2PermissionGrantDeleteOAuth2PermissionGrant">Command `az identitysignins oauth2-permission-grant-o-auth2-permission-grant delete`</a>

##### <a name="Parametersoauth2PermissionGrants.oAuth2PermissionGrantDeleteOAuth2PermissionGrant">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--o-auth2-permission-grant-id**|string|key: id of oAuth2PermissionGrant|o_auth2_permission_grant_id|oAuth2PermissionGrant-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="oauth2PermissionGrants.oAuth2PermissionGrantCreateOAuth2PermissionGrant">Command `az identitysignins oauth2-permission-grant-o-auth2-permission-grant create-o-auth2-permission-grant`</a>

##### <a name="Parametersoauth2PermissionGrants.oAuth2PermissionGrantCreateOAuth2PermissionGrant">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--client-id**|string|The id of the client service principal for the application which is authorized to act on behalf of a signed-in user when accessing an API. Required. Supports $filter (eq only).|client_id|clientId|
|**--consent-type**|string|Indicates if authorization is granted for the client application to impersonate all users or only a specific user. AllPrincipals indicates authorization to impersonate all users. Principal indicates authorization to impersonate a specific user. Consent on behalf of all users can be granted by an administrator. Non-admin users may be authorized to consent on behalf of themselves in some cases, for some delegated permissions. Required. Supports $filter (eq only).|consent_type|consentType|
|**--principal-id**|string|The id of the user on behalf of whom the client is authorized to access the resource, when consentType is Principal. If consentType is AllPrincipals this value is null. Required when consentType is Principal.|principal_id|principalId|
|**--resource-id**|string|The id of the resource service principal to which access is authorized. This identifies the API which the client is authorized to attempt to call on behalf of a signed-in user.|resource_id|resourceId|
|**--scope**|string|A space-separated list of the claim values for delegated permissions which should be included in access tokens for the resource application (the API). For example, openid User.Read GroupMember.Read.All. Each claim value should match the value field of one of the delegated permissions defined by the API, listed in the publishedPermissionScopes property of the resource service principal.|scope|scope|

#### <a name="oauth2PermissionGrants.oAuth2PermissionGrantListOAuth2PermissionGrant">Command `az identitysignins oauth2-permission-grant-o-auth2-permission-grant list-o-auth2-permission-grant`</a>

##### <a name="Parametersoauth2PermissionGrants.oAuth2PermissionGrantListOAuth2PermissionGrant">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="oauth2PermissionGrants.oAuth2PermissionGrantGetOAuth2PermissionGrant">Command `az identitysignins oauth2-permission-grant-o-auth2-permission-grant show-o-auth2-permission-grant`</a>

##### <a name="Parametersoauth2PermissionGrants.oAuth2PermissionGrantGetOAuth2PermissionGrant">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--o-auth2-permission-grant-id**|string|key: id of oAuth2PermissionGrant|o_auth2_permission_grant_id|oAuth2PermissionGrant-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="oauth2PermissionGrants.oAuth2PermissionGrantUpdateOAuth2PermissionGrant">Command `az identitysignins oauth2-permission-grant-o-auth2-permission-grant update-o-auth2-permission-grant`</a>

##### <a name="Parametersoauth2PermissionGrants.oAuth2PermissionGrantUpdateOAuth2PermissionGrant">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--o-auth2-permission-grant-id**|string|key: id of oAuth2PermissionGrant|o_auth2_permission_grant_id|oAuth2PermissionGrant-id|
|**--id**|string|Read-only.|id|id|
|**--client-id**|string|The id of the client service principal for the application which is authorized to act on behalf of a signed-in user when accessing an API. Required. Supports $filter (eq only).|client_id|clientId|
|**--consent-type**|string|Indicates if authorization is granted for the client application to impersonate all users or only a specific user. AllPrincipals indicates authorization to impersonate all users. Principal indicates authorization to impersonate a specific user. Consent on behalf of all users can be granted by an administrator. Non-admin users may be authorized to consent on behalf of themselves in some cases, for some delegated permissions. Required. Supports $filter (eq only).|consent_type|consentType|
|**--principal-id**|string|The id of the user on behalf of whom the client is authorized to access the resource, when consentType is Principal. If consentType is AllPrincipals this value is null. Required when consentType is Principal.|principal_id|principalId|
|**--resource-id**|string|The id of the resource service principal to which access is authorized. This identifies the API which the client is authorized to attempt to call on behalf of a signed-in user.|resource_id|resourceId|
|**--scope**|string|A space-separated list of the claim values for delegated permissions which should be included in access tokens for the resource application (the API). For example, openid User.Read GroupMember.Read.All. Each claim value should match the value field of one of the delegated permissions defined by the API, listed in the publishedPermissionScopes property of the resource service principal.|scope|scope|

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

### group `az identitysignins policy`
#### <a name="policiesDeleteActivityBasedTimeoutPolicies">Command `az identitysignins policy delete`</a>

##### <a name="ParameterspoliciesDeleteActivityBasedTimeoutPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--activity-based-timeout-policy-id**|string|key: id of activityBasedTimeoutPolicy|activity_based_timeout_policy_id|activityBasedTimeoutPolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policiesDeleteClaimsMappingPolicies">Command `az identitysignins policy delete`</a>

##### <a name="ParameterspoliciesDeleteClaimsMappingPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--claims-mapping-policy-id**|string|key: id of claimsMappingPolicy|claims_mapping_policy_id|claimsMappingPolicy-id|

#### <a name="policiesDeleteConditionalAccessPolicies">Command `az identitysignins policy delete`</a>

##### <a name="ParameterspoliciesDeleteConditionalAccessPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--conditional-access-policy-id**|string|key: id of conditionalAccessPolicy|conditional_access_policy_id|conditionalAccessPolicy-id|

#### <a name="policiesDeleteHomeRealmDiscoveryPolicies">Command `az identitysignins policy delete`</a>

##### <a name="ParameterspoliciesDeleteHomeRealmDiscoveryPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--home-realm-discovery-policy-id**|string|key: id of homeRealmDiscoveryPolicy|home_realm_discovery_policy_id|homeRealmDiscoveryPolicy-id|

#### <a name="policiesDeletePermissionGrantPolicies">Command `az identitysignins policy delete`</a>

##### <a name="ParameterspoliciesDeletePermissionGrantPolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|

#### <a name="policiesDeleteTokenIssuancePolicies">Command `az identitysignins policy delete`</a>

##### <a name="ParameterspoliciesDeleteTokenIssuancePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--token-issuance-policy-id**|string|key: id of tokenIssuancePolicy|token_issuance_policy_id|tokenIssuancePolicy-id|

#### <a name="policiesDeleteTokenLifetimePolicies">Command `az identitysignins policy delete`</a>

##### <a name="ParameterspoliciesDeleteTokenLifetimePolicies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--token-lifetime-policy-id**|string|key: id of tokenLifetimePolicy|token_lifetime_policy_id|tokenLifetimePolicy-id|

#### <a name="policiesDeleteIdentitySecurityDefaultsEnforcementPolicy">Command `az identitysignins policy delete`</a>

##### <a name="ParameterspoliciesDeleteIdentitySecurityDefaultsEnforcementPolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
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
|**--client-app-types**|array|Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other.|client_app_types|clientAppTypes|
|**--locations**|object|conditionalAccessLocations|locations|locations|
|**--platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--sign-in-risk-levels**|array|Risk levels included in the policy. Possible values are: low, medium, high, none.|sign_in_risk_levels|signInRiskLevels|
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

#### <a name="policiesListActivityBasedTimeoutPolicies">Command `az identitysignins policy list-activity-based-timeout-policy`</a>

##### <a name="ParameterspoliciesListActivityBasedTimeoutPolicies">Parameters</a> 
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
|**--client-app-types**|array|Client application types included in the policy. Possible values are: all, browser, mobileAppsAndDesktopClients, exchangeActiveSync, easSupported, other.|client_app_types|clientAppTypes|
|**--locations**|object|conditionalAccessLocations|locations|locations|
|**--platforms**|object|conditionalAccessPlatforms|platforms|platforms|
|**--sign-in-risk-levels**|array|Risk levels included in the policy. Possible values are: low, medium, high, none.|sign_in_risk_levels|signInRiskLevels|
|**--users**|object|conditionalAccessUsers|users|users|

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

### group `az identitysignins policy-permission-grant-policy`
#### <a name="policies.permissionGrantPoliciesDeleteExcludes">Command `az identitysignins policy-permission-grant-policy delete`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesDeleteExcludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--permission-grant-condition-set-id**|string|key: id of permissionGrantConditionSet|permission_grant_condition_set_id|permissionGrantConditionSet-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="policies.permissionGrantPoliciesDeleteIncludes">Command `az identitysignins policy-permission-grant-policy delete`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesDeleteIncludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="policies.permissionGrantPoliciesCreateExcludes">Command `az identitysignins policy-permission-grant-policy create-exclude`</a>

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

#### <a name="policies.permissionGrantPoliciesCreateIncludes">Command `az identitysignins policy-permission-grant-policy create-include`</a>

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

#### <a name="policies.permissionGrantPoliciesListExcludes">Command `az identitysignins policy-permission-grant-policy list-exclude`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesListExcludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policies.permissionGrantPoliciesListIncludes">Command `az identitysignins policy-permission-grant-policy list-include`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesListIncludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policies.permissionGrantPoliciesGetExcludes">Command `az identitysignins policy-permission-grant-policy show-exclude`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesGetExcludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--permission-grant-condition-set-id**|string|key: id of permissionGrantConditionSet|permission_grant_condition_set_id|permissionGrantConditionSet-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policies.permissionGrantPoliciesGetIncludes">Command `az identitysignins policy-permission-grant-policy show-include`</a>

##### <a name="Parameterspolicies.permissionGrantPoliciesGetIncludes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--permission-grant-policy-id**|string|key: id of permissionGrantPolicy|permission_grant_policy_id|permissionGrantPolicy-id|
|**--permission-grant-condition-set-id**|string|key: id of permissionGrantConditionSet|permission_grant_condition_set_id|permissionGrantConditionSet-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policies.permissionGrantPoliciesUpdateExcludes">Command `az identitysignins policy-permission-grant-policy update-exclude`</a>

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

#### <a name="policies.permissionGrantPoliciesUpdateIncludes">Command `az identitysignins policy-permission-grant-policy update-include`</a>

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

### group `az identitysignins policy-policy-root`
#### <a name="policies.policyRootGetPolicyRoot">Command `az identitysignins policy-policy-root show-policy-root`</a>

##### <a name="Parameterspolicies.policyRootGetPolicyRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="policies.policyRootUpdatePolicyRoot">Command `az identitysignins policy-policy-root update-policy-root`</a>

##### <a name="Parameterspolicies.policyRootUpdatePolicyRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--activity-based-timeout-policies**|array||activity_based_timeout_policies|activityBasedTimeoutPolicies|
|**--claims-mapping-policies**|array||claims_mapping_policies|claimsMappingPolicies|
|**--home-realm-discovery-policies**|array||home_realm_discovery_policies|homeRealmDiscoveryPolicies|
|**--permission-grant-policies**|array||permission_grant_policies|permissionGrantPolicies|
|**--token-issuance-policies**|array||token_issuance_policies|tokenIssuancePolicies|
|**--token-lifetime-policies**|array||token_lifetime_policies|tokenLifetimePolicies|
|**--conditional-access-policies**|array||conditional_access_policies|conditionalAccessPolicies|
|**--identity-security-defaults-enforcement-policy**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|identity_security_defaults_enforcement_policy|identitySecurityDefaultsEnforcementPolicy|
