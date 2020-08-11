# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from azure.identity import InteractiveBrowserCredential

from knack.help_files import helps

helps['login'] = """
type: command
short-summary: Log in to Microsoft Graph
examples:
    - name: Login in interactively
      text: >
        mg login
"""

helps['logout'] = """
type: command
short-summary: Log out 
long-summary: Log out from Microsoft Graph session
"""