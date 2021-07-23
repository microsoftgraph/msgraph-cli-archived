# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from knack.help_files import helps

helps['cloud set-version'] = """
type: command
short-summary: Set version of graph to use.
parameters:
  - name: --graph-version
    type: string
    short-summary: Graph version to use
examples:
  - name: Set Graph Version
    text: >
      mgc cloud set-version --graph-version beta
"""

helps['cloud set'] = """
type: command
short-summary: Set the active cloud.
parameters:
  - name: --name
    type: string
    short-summary: Cloud to use
examples:
  - name: Set cloud
    text: >
      mgc cloud set --name PUBLIC
"""

helps['cloud show'] = """
type: command
short-summary: Show profile information
"""

helps['cloud list'] = """
type: command
short-summary: Show list of supported clouds
"""

helps['cloud unregister'] = """
type: command
short-summary: Unregisters a user defined cloud
parameters:
  - name: --name
    type: string
    short-summary: Cloud to unregister
examples:
  - name: Delete cloud
    text: >
      mgc cloud unregister --name CUSTOM_CLOUD
"""

helps['cloud register'] = """
type: command
short-summary: Register a custom cloud
parameters:
  - name: --name
    type: string
    short-summary:  Cloud's name
    long-summary: The cloud's name is shown in the list of clouds when a user runs mgc cloud select.
  - name: --graph-endpoint
    type: string
    short-summary: Cloud's endpoint
  - name: --azure-ad-endpoint
    short-summary: Cloud's authentication endpoint
examples:
  - name: Register a new cloud
    text: >
      mgc cloud add --name CUSTOM_CLOUD --endpoint https://graph.microsoft.com --authority https://graph.microsoftonline.com
"""

helps['cloud update'] = """
type: command
short-summary: Update the configuration of a user defined cloud.
parameters:
  - name: --cloud
    type: string
    short-summary: Name of user defined cloud to update
  - name: --name
    type: string
    short-summary:  Cloud's name
  - name: --graph-endpoint
    type: string
    short-summary: Cloud's endpoint
  - name: --azure-ad-endpoint
    short-summary: Cloud's authentication endpoint
examples:
  - name: Update a user defined cloud
    text: >
      mgc cloud update --cloud CUSTOM_CLOUD --name UPDATED_NAME
"""
