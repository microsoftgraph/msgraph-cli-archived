# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=line-too-long

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_cloudcommunications_v1_0.generated._client_factory import cf_user

    cloudcommunications_v1_0_user = CliCommandType(
        operations_tmpl='azext_cloudcommunications_v1_0.vendored_sdks.cloudcommunications.operations._user_operations#UserOperations.{}',
        client_factory=cf_user,
    )
    with self.command_group('cloudcommunications user', cloudcommunications_v1_0_user, client_factory=cf_user) as g:
        g.custom_command('delete', 'cloudcommunications_user_delete', confirmation=True)
        g.custom_command('create-online-meeting', 'cloudcommunications_user_create_online_meeting')
        g.custom_command('list-online-meeting', 'cloudcommunications_user_list_online_meeting')
        g.custom_command('show-online-meeting', 'cloudcommunications_user_show_online_meeting')
        g.custom_command('update-online-meeting', 'cloudcommunications_user_update_online_meeting')

    with self.command_group('cloudcommunications_v1_0', is_experimental=True):
        pass