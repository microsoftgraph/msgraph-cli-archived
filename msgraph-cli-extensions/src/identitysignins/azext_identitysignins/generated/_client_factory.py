# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_identitysignins_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.identitysignins import IdentitySignIns
    return get_mgmt_service_client(cli_ctx,
                                   IdentitySignIns,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_data_policy_operation_data_policy_operation(cli_ctx, *_):
    return cf_identitysignins_cl(cli_ctx).data_policy_operation_data_policy_operation


def cf_identity(cli_ctx, *_):
    return cf_identitysignins_cl(cli_ctx).identity


def cf_identity_conditional_access(cli_ctx, *_):
    return cf_identitysignins_cl(cli_ctx).identity_conditional_access


def cf_identity_provider_identity_provider(cli_ctx, *_):
    return cf_identitysignins_cl(cli_ctx).identity_provider_identity_provider


def cf_information_protection_information_protection(cli_ctx, *_):
    return cf_identitysignins_cl(cli_ctx).information_protection_information_protection


def cf_information_protection(cli_ctx, *_):
    return cf_identitysignins_cl(cli_ctx).information_protection


def cf_information_protection_threat_assessment_request(cli_ctx, *_):
    return cf_identitysignins_cl(cli_ctx).information_protection_threat_assessment_request


def cf_invitation_invitation(cli_ctx, *_):
    return cf_identitysignins_cl(cli_ctx).invitation_invitation


def cf_invitation(cli_ctx, *_):
    return cf_identitysignins_cl(cli_ctx).invitation


def cf_oauth2permission_grant_oauth2permission_grant(cli_ctx, *_):
    return cf_identitysignins_cl(cli_ctx).oauth2_permission_grant_oauth2_permission_grant


def cf_oauth2permission_grant(cli_ctx, *_):
    return cf_identitysignins_cl(cli_ctx).oauth2_permission_grant


def cf_organization(cli_ctx, *_):
    return cf_identitysignins_cl(cli_ctx).organization


def cf_policy_policy_root(cli_ctx, *_):
    return cf_identitysignins_cl(cli_ctx).policy_policy_root


def cf_policy(cli_ctx, *_):
    return cf_identitysignins_cl(cli_ctx).policy


def cf_policy_permission_grant_policy(cli_ctx, *_):
    return cf_identitysignins_cl(cli_ctx).policy_permission_grant_policy