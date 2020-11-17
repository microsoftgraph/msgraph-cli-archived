# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

CLOUDS = {
    'PUBLIC': {
        'endpoint': 'https://graph.microsoft.com',
        'authority': 'https://login.microsoftonline.com'
    },
    'US_GOV_L4': {
        'endpoint': 'https://graph.microsoft.us',
        'authority': 'https://login.microsoftonline.us'
    },
    'US_GOV_L5': {
        'endpoint': 'https://dod-graph.microsoft.us',
        'authority': 'https://login.microsoftonline.us'
    },
    'GERMANY': {
        'endpoint': 'https://graph.microsoft.de',
        'authority': 'https://login.microsoftonline.de'
    },
    'CHINA': {
        'endpoint': 'https://microsoftgraph.chinacloudapi.cn',
        'authority': 'https://login.chinacloudapi.cn'
    }
}
