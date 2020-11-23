# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import json
from knack.prompting import prompt_choice_list
from msgraph.cli.core.constants import DEFAULT_CLOUDS
from msgraph.cli import read_profile, write_profile


def select_cloud():
    profile = read_profile()
    user_defined_clouds = profile.get('user_defined_clouds', {})

    for cloud in user_defined_clouds:
        DEFAULT_CLOUDS.update(cloud)
    supported_clouds = list(DEFAULT_CLOUDS.keys())

    selected = prompt_choice_list('Select a cloud', supported_clouds)
    profile['cloud'] = DEFAULT_CLOUDS.get(supported_clouds[selected])
    write_profile(json.dumps(profile))

    print(f'Selected {supported_clouds[selected]} cloud')


def add_cloud(name: str, endpoint: str, authority: str):
    _validate(endpoint)

    cloud = {name: {'endpoint': endpoint, 'authority': authority}}

    profile = read_profile()

    try:
        user_defined_clouds = profile['user_defined_clouds']
        user_defined_clouds.append(cloud)
    except KeyError:
        profile['user_defined_clouds'] = [cloud]

    write_profile(json.dumps(profile))
    print(f'Cloud "{name}" added successfully')


def _validate(url: str):
    from urllib import request

    try:
        request.urlopen(url)
    except IOError as error:
        raise Exception('Invalid endpoint')