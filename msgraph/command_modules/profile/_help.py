# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from knack.help_files import helps
helps['profile select-version'] = """
type: command
short-summary: Select a graph-version from supported versions.
"""

helps['profile select-cloud'] = """
type: command
short-summary: Select a cloud from supported clouds.
"""

helps['profile show-profile'] = """
type: command
short-summary: Show profile information
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
