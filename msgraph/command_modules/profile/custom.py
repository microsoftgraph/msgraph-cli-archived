# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from os import path
from pathlib import Path
import json
from knack.prompting import prompt_choice_list
from msgraph.cli.core.exceptions import CLIException

from .constants import CLOUDS

#TODO: Move this variable to constants.py
PROFILE_LOCATION = path.join(Path.home(), '.mg', 'profile.json')


def select_cloud():
    profile = read_profile()

    user_defined_clouds = profile.get('user_defined_clouds', {})

    for cloud in user_defined_clouds:
        CLOUDS.update(cloud)

    supported_clouds = list(CLOUDS.keys())
    selected = prompt_choice_list('Select a cloud', supported_clouds)

    profile['cloud'] = CLOUDS.get(supported_clouds[selected])
    write_profile(json.dumps(profile))

    print(f'Selected {supported_clouds[selected]}')
    # Save selected cloud in profile.json


def add_cloud(name: str, endpoint: str, authority: str):
    cloud = {name: {'endpoint': endpoint, 'authority': authority}}

    profile = read_profile()

    try:
        user_defined_clouds = profile['user_defined_clouds']
        user_defined_clouds.append(cloud)
    except KeyError:
        profile['user_defined_clouds'] = [cloud]

    write_profile(json.dumps(profile))
    print(f'Cloud "{name}" added successfully')


def reset_cloud():
    print('Resetting a cloud')


#TODO: Abstract reading and writing to profile
def read_profile() -> dict:
    result = None

    try:
        with open(PROFILE_LOCATION, 'r') as file:
            result = file.read()
        return json.loads(result)
    except IOError as ex:
        return {}


def write_profile(profile: str):
    try:
        with open(PROFILE_LOCATION, 'w') as file:
            file.write(profile)
    except IOError as ex:
        raise CLIException('Selected cloud was not set, CLI will use the PublicCLoud') from ex
