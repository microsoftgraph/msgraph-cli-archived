# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
'''
Update the _help.py file after changing the signature or behavior of functions in this file
'''

from msgraph.cli.core.profile import ProfileProvider
from msgraph.cli.core.exceptions import CLIError
from msgraph.cli.core.constants import GRAPH_VERSIONS

from ._cloud_manager import CloudManager

profile_provider = ProfileProvider()
cloud_manager = CloudManager(profile_provider)


def delete_cloud(name: str):
    cloud_manager.delete_cloud(name)
    print(f'Cloud "{name}" deleted successfully')


def add_cloud(name: str, graph_endpoint: str, azure_ad_endpoint: str):
    _validate(graph_endpoint)

    properties = {
        'name': name,
        'graph_endpoint': graph_endpoint,
        'azure_ad_endpoint': azure_ad_endpoint
    }

    cloud_manager.create_cloud(name, properties)
    print(f'Cloud "{name}" added successfully')


def show_clouds():
    return cloud_manager.get_clouds()


def set_cloud(name: str):
    supported_clouds = cloud_manager.get_clouds()

    if name not in supported_clouds.keys():
        raise CLIError(
            f'Cloud {name} not found. Run "mg profile show-clouds" to see available clouds')

    cloud_manager.set_current_cloud(name)
    print(f'Using cloud: {name}')


def update_cloud(cloud: str, name=None, graph_endpoint=None, azure_ad_endpoint=None):

    update_props = {}

    if name:
        update_props.update({'name': name})
    if graph_endpoint:
        _validate(graph_endpoint)
        update_props.update({'graph_endpoint': graph_endpoint})
    if azure_ad_endpoint:
        update_props.update({'azure_ad_endpoint': azure_ad_endpoint})

    updated = cloud_manager.update_cloud(cloud, update_props)

    if updated:
        print(f'{cloud} updated successfully')
    else:
        print(f'{cloud} does not exist')


def set_version(graph_version: str):
    if graph_version not in GRAPH_VERSIONS:
        raise CLIError(
            f'{graph_version} not supported. "v1.0" and "beta" are the supported graph versions.')

    profile = profile_provider.read_profile()
    profile.update({'version': graph_version})
    profile_provider.write_profile(profile,
                                   error_msg='An error occured while setting the selected version')

    print(f'Using graph version: {graph_version}')


def show_profile():
    profile = profile_provider.read_profile()
    # remove user_defined_clouds from the profile local variable.
    # The user wants to see just the cloud and version information.
    profile.pop('user_defined_clouds')

    return profile


def _validate(url: str):
    from urllib import request

    try:
        request.urlopen(url)
    except IOError as error:
        raise Exception('Invalid endpoint') from error
