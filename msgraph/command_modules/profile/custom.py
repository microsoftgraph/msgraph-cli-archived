# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.prompting import prompt_choice_list

from .constants import CLOUDS


def select_cloud():
    supported_clouds = list(CLOUDS.keys())
    selected = prompt_choice_list('Select a cloud', supported_clouds)
    print(f'Selected {supported_clouds[selected]}')
    # Save selected cloud in profile.json


def add_cloud():
    print('Adding a cloud')


def reset_cloud():
    print('Resetting a cloud')
