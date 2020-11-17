# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from knack.help_files import helps

helps['cloud select'] = """
type: command
short-summary: Select a cloud from supported clouds.
"""

helps['cloud add'] = """
type: command
short-summary: Add a custom cloud
parameters:
  - name: --name
    type: string
    short-summary:  Cloud's name
    long-summary: The cloud's name is shown in the list of clouds when a user runs mg cloud select.
  - name: --endpoint
    type: string
    short-summary: Cloud's endpoint
  - name: --authority
    short-summary: Cloud's authentication endpoint
examples:
  - name: Add a new cloud
    text: >
      mg cloud add --name CUSTOM_CLOUD --endpoint https://graph.microsoft.com --authority https://graph.microsoftonline.com
"""