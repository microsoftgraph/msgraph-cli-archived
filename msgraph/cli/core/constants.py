# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from pathlib import Path
from os import path

AUTH_RECORD_LOCATION = path.join(Path.home(), '.mg', 'record.txt')
PROFILE_LOCATION = path.join(Path.home(), '.mg', 'profile.json')
DEFAULT_CLIENT_ID = '837b13ab-6d14-4dc7-837f-8954cc87fdc0'
DEFAULT_AUTHORITY = 'https://login.microsoftonline.com'

CLI_COMMON_KWARGS = [
    'min_api', 'max_api', 'resource_type', 'operation_group', 'custom_command_type', 'command_type',
    'is_preview', 'preview_info', 'is_experimental', 'experimental_info', 'local_context_attribute'
]

CLI_COMMAND_KWARGS = [
    'transform', 'table_transformer', 'confirmation', 'exception_handler', 'client_factory',
    'operations_tmpl', 'no_wait_param', 'supports_no_wait', 'validator', 'client_arg_name',
    'doc_string_source', 'deprecate_info', 'supports_local_cache', 'model_path'
] + CLI_COMMON_KWARGS

EXCLUDED_PARAMS = [
    'self', 'raw', 'polling', 'custom_headers', 'operation_config', 'content_version', 'kwargs',
    'client', 'no_wait'
]

DEFAULT_CLOUDS = {
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