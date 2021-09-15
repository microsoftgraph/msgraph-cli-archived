# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_devicescorpmgt_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_devicescorpmgt.vendored_sdks.devicescorpmgt import DevicesCorporateManagement
    return get_mgmt_service_client(cli_ctx,
                                   DevicesCorporateManagement,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_deviceappmanagementdeviceappmanagement(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).deviceappmanagementdeviceappmanagement


def cf_deviceappmanagement(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).deviceappmanagement


def cf_deviceappmanagementandroidmanagedappprotection(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).deviceappmanagementandroidmanagedappprotections


def cf_deviceappmanagementdefaultmanagedappprotection(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).deviceappmanagementdefaultmanagedappprotections


def cf_deviceappmanagementiosmanagedappprotection(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).deviceappmanagementiosmanagedappprotections


def cf_deviceappmanagementmanagedapppolicy(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).deviceappmanagementmanagedapppolicies


def cf_deviceappmanagementmanagedappregistration(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).deviceappmanagementmanagedappregistrations


def cf_deviceappmanagementmanagedappregistrationsappliedpolicy(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).deviceappmanagementmanagedappregistrationsappliedpolicies


def cf_deviceappmanagementmanagedappregistrationsintendedpolicy(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).deviceappmanagementmanagedappregistrationsintendedpolicies


def cf_deviceappmanagementmanagedebook(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).deviceappmanagementmanagedebooks


def cf_deviceappmanagementmanagedebooksuserstatesummary(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).deviceappmanagementmanagedebooksuserstatesummary


def cf_deviceappmanagementmobileappconfiguration(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).deviceappmanagementmobileappconfigurations


def cf_deviceappmanagementmobileapp(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).deviceappmanagementmobileapps


def cf_deviceappmanagementtargetedmanagedappconfiguration(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).deviceappmanagementtargetedmanagedappconfigurations


def cf_deviceappmanagementvpptoken(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).deviceappmanagementvpptokens


def cf_user(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).users


def cf_usersmanageddevice(cli_ctx, *_):
    return cf_devicescorpmgt_cl(cli_ctx).usersmanageddevices
