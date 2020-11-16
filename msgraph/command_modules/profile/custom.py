# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

CLOUDS = {
    'PUBLIC': {
        'client_id': '',
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


def list_clouds():
    for cloud in list(CLOUDS.keys()):
        print(cloud)


def select_cloud():
    print('Selecting a cloud')


def add_cloud():
    print('Adding a cloud')


def reset_cloud():
    print('Resetting a cloud')
