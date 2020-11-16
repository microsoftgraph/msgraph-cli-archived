# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

CLOUDS = {
    'PUBLIC': {
        'client_id': 'f7218512-c727-4138-9fb9-a0fe2500650c',
        'endpoint': 'graph.microsoft.com',
        'authority': 'https://login.microsoftonline.com'
    },
    'US_GOV_L4': {
        'client_id': '',
        'endpoint': 'https://graph.microsoft.us',
        'authority': 'https://login.microsoftonline.us'
    },
    'US_GOV_L5': {
        'client_id': '',
        'endpoint': 'https://dod-graph.microsoft.us',
        'authority': 'https://login.microsoftonline.us'
    },
    'GERMANY': {
        'client_id': '',
        'endpoint': 'https://graph.microsoft.de',
        'authority': 'https://login.microsoftonline.de'
    },
    'CHINA': {
        'client_id': '',
        'endpoint': 'https://microsoftgraph.chinacloudapi.cn',
        'authority': '	https://login.chinacloudapi.cn'
    }
}
