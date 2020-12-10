# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
'''
Update the _help.py file after changing the signature or behavior of functions in this file
'''
from knack.prompting import prompt_choice_list
from msgraph.cli.core.constants import DEFAULT_CLOUDS
from msgraph.cli.core.profile import read_profile, write_profile
from ._cloud_manager import CloudManager

cloud_manager = CloudManager()


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


def select_cloud():
    supported_clouds = cloud_manager.get_clouds()
    formatted = []

    for cloud_name in supported_clouds:
        cloud = supported_clouds[cloud_name]
        formatted.append({
            'name':
            cloud.get('name'),
            'desc':
            f"""Graph Endpoint: {cloud.get('graph_endpoint')} - Azure AD Endpoint: {cloud.get('azure_ad_endpoint')}
            """
        })

    selected = prompt_choice_list('Select a cloud \n', formatted)
    name = formatted[selected].get('name')

    cloud_manager.set_current_cloud(name)
    print(f'{name} cloud selected')


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


def select_version():
    supported_versions = ['v1.0', 'beta']
    profile = read_profile()

    selected = prompt_choice_list('Select graph version', supported_versions)
    selected_version = supported_versions[selected]

    profile.update({'version': selected_version})
    write_profile(profile, error_msg='An error occured while setting the selected version')

    print(f'Version {selected_version} selected')


def show_profile():
    profile = read_profile()

    # remove user_defined_clouds from the profile local variable.
    # The user just wants to see the cloud and version information.
    profile.pop('user_defined_clouds')
    return profile


def _validate(url: str):
    from urllib import request

    try:
        request.urlopen(url)
    except IOError as error:
        raise Exception('Invalid endpoint')
