# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from knack.help_files import helps

helps['login'] = """
type: command
short-summary: Log in to Microsoft Graph
long-summary: Logs in a user to Microsoft Graph with the specified scopes. You must specify the scopes before you use commands. You will need to log out and log back in to consent to additional scopes.
examples:
    - name: Login in interactively
      text: >
        mg login --scopes "user.read, mail.read"
"""

helps['logout'] = """
type: command
short-summary: Log out of Microsoft Graph
"""
