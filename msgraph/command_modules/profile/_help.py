# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from knack.help_files import helps

helps['profile set-version'] = """
type: command
short-summary: Set version of graph to use.
parameters:
  - name: --graph-version
    type: string
    short-summary: Graph version to use
examples:
  - name: Set Graph Version
    text: >
      mg profile set-version --graph-version beta
"""

helps['profile set-cloud'] = """
type: command
short-summary: Set a cloud.
parameters:
  - name: --name
    type: string
    short-summary: Cloud to use
examples:
  - name: Set cloud
    text: >
      mg set-cloud --name PUBLIC
"""

helps['profile show-profile'] = """
type: command
short-summary: Show profile information
"""

helps['profile show-clouds'] = """
type: command
short-summary: Show list of supported clouds
"""

helps['profile delete-cloud'] = """
type: command
short-summary: Deletes a user defined cloud
parameters:
  - name: --name
    type: string
    short-summary: Cloud to delete
examples:
  - name: Delete cloud
    text: >
      mg cloud delete --name CUSTOM_CLOUD
"""

helps['profile add-cloud'] = """
type: command
short-summary: Add a custom cloud
parameters:
  - name: --name
    type: string
    short-summary:  Cloud's name
    long-summary: The cloud's name is shown in the list of clouds when a user runs mg cloud select.
  - name: --graph-endpoint
    type: string
    short-summary: Cloud's endpoint
  - name: --azure-ad-endpoint
    short-summary: Cloud's authentication endpoint
examples:
  - name: Add a new cloud
    text: >
      mg cloud add --name CUSTOM_CLOUD --endpoint https://graph.microsoft.com --authority https://graph.microsoftonline.com
"""

helps['profile update-cloud'] = """
type: command
short-summary: update a user defined cloud
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
      mg cloud update --cloud CUSTOM_CLOUD --name UPDATED_NAME
"""
