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

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_usersmail.generated._client_factory import cf_user
    usersmail_user = CliCommandType(
        operations_tmpl='azext_usersmail.vendored_sdks.usersmail.operations._user_operations#UserOperations.{}',
        client_factory=cf_user)
    with self.command_group('usersmail', usersmail_user, client_factory=cf_user) as g:
        g.custom_command('create-mail-folder', 'usersmail_create_mail_folder')
        g.custom_command('create-message', 'usersmail_create_message')
        g.custom_command('get-inference-classification', 'usersmail_get_inference_classification')
        g.custom_command('get-mail-folder', 'usersmail_get_mail_folder')
        g.custom_command('get-message', 'usersmail_get_message')
        g.custom_command('list-mail-folder', 'usersmail_list_mail_folder')
        g.custom_command('list-message', 'usersmail_list_message')
        g.custom_command('update-inference-classification', 'usersmail_update_inference_classification')
        g.custom_command('update-mail-folder', 'usersmail_update_mail_folder')
        g.custom_command('update-message', 'usersmail_update_message')

    from azext_usersmail.generated._client_factory import cf_user_inference_classification
    usersmail_user_inference_classification = CliCommandType(
        operations_tmpl='azext_usersmail.vendored_sdks.usersmail.operations._user_inference_classification_operations#U'
        'serInferenceClassificationOperations.{}',
        client_factory=cf_user_inference_classification)
    with self.command_group('usersmail', usersmail_user_inference_classification,
                            client_factory=cf_user_inference_classification) as g:
        g.custom_command('create-override', 'usersmail_create_override')
        g.custom_command('get-override', 'usersmail_get_override')
        g.custom_command('list-override', 'usersmail_list_override')
        g.custom_command('update-override', 'usersmail_update_override')

    from azext_usersmail.generated._client_factory import cf_user_mail_folder
    usersmail_user_mail_folder = CliCommandType(
        operations_tmpl='azext_usersmail.vendored_sdks.usersmail.operations._user_mail_folder_operations#UserMailFolder'
        'Operations.{}',
        client_factory=cf_user_mail_folder)
    with self.command_group('usersmail', usersmail_user_mail_folder, client_factory=cf_user_mail_folder) as g:
        g.custom_command('create-child-folder', 'usersmail_create_child_folder')
        g.custom_command('create-message', 'usersmail_create_message')
        g.custom_command('create-message-rule', 'usersmail_create_message_rule')
        g.custom_command('create-multi-value-extended-property', 'usersmail_create_multi_value_extended_property')
        g.custom_command('create-single-value-extended-property', 'usersmail_create_single_value_extended_property')
        g.custom_command('create-user-configuration', 'usersmail_create_user_configuration')
        g.custom_command('get-child-folder', 'usersmail_get_child_folder')
        g.custom_command('get-message', 'usersmail_get_message')
        g.custom_command('get-message-rule', 'usersmail_get_message_rule')
        g.custom_command('get-multi-value-extended-property', 'usersmail_get_multi_value_extended_property')
        g.custom_command('get-single-value-extended-property', 'usersmail_get_single_value_extended_property')
        g.custom_command('get-user-configuration', 'usersmail_get_user_configuration')
        g.custom_command('list-child-folder', 'usersmail_list_child_folder')
        g.custom_command('list-message', 'usersmail_list_message')
        g.custom_command('list-message-rule', 'usersmail_list_message_rule')
        g.custom_command('list-multi-value-extended-property', 'usersmail_list_multi_value_extended_property')
        g.custom_command('list-single-value-extended-property', 'usersmail_list_single_value_extended_property')
        g.custom_command('list-user-configuration', 'usersmail_list_user_configuration')
        g.custom_command('update-child-folder', 'usersmail_update_child_folder')
        g.custom_command('update-message', 'usersmail_update_message')
        g.custom_command('update-message-rule', 'usersmail_update_message_rule')
        g.custom_command('update-multi-value-extended-property', 'usersmail_update_multi_value_extended_property')
        g.custom_command('update-single-value-extended-property', 'usersmail_update_single_value_extended_property')
        g.custom_command('update-user-configuration', 'usersmail_update_user_configuration')

    from azext_usersmail.generated._client_factory import cf_user_mail_folder_message
    usersmail_user_mail_folder_message = CliCommandType(
        operations_tmpl='azext_usersmail.vendored_sdks.usersmail.operations._user_mail_folder_message_operations#UserMa'
        'ilFolderMessageOperations.{}',
        client_factory=cf_user_mail_folder_message)
    with self.command_group('usersmail', usersmail_user_mail_folder_message,
                            client_factory=cf_user_mail_folder_message) as g:
        g.custom_command('create-attachment', 'usersmail_create_attachment')
        g.custom_command('create-extension', 'usersmail_create_extension')
        g.custom_command('create-mention', 'usersmail_create_mention')
        g.custom_command('create-multi-value-extended-property', 'usersmail_create_multi_value_extended_property')
        g.custom_command('create-single-value-extended-property', 'usersmail_create_single_value_extended_property')
        g.custom_command('get-attachment', 'usersmail_get_attachment')
        g.custom_command('get-extension', 'usersmail_get_extension')
        g.custom_command('get-mention', 'usersmail_get_mention')
        g.custom_command('get-multi-value-extended-property', 'usersmail_get_multi_value_extended_property')
        g.custom_command('get-single-value-extended-property', 'usersmail_get_single_value_extended_property')
        g.custom_command('list-attachment', 'usersmail_list_attachment')
        g.custom_command('list-extension', 'usersmail_list_extension')
        g.custom_command('list-mention', 'usersmail_list_mention')
        g.custom_command('list-multi-value-extended-property', 'usersmail_list_multi_value_extended_property')
        g.custom_command('list-single-value-extended-property', 'usersmail_list_single_value_extended_property')
        g.custom_command('update-attachment', 'usersmail_update_attachment')
        g.custom_command('update-extension', 'usersmail_update_extension')
        g.custom_command('update-mention', 'usersmail_update_mention')
        g.custom_command('update-multi-value-extended-property', 'usersmail_update_multi_value_extended_property')
        g.custom_command('update-single-value-extended-property', 'usersmail_update_single_value_extended_property')

    from azext_usersmail.generated._client_factory import cf_user_message
    usersmail_user_message = CliCommandType(
        operations_tmpl='azext_usersmail.vendored_sdks.usersmail.operations._user_message_operations#UserMessageOperati'
        'ons.{}',
        client_factory=cf_user_message)
    with self.command_group('usersmail', usersmail_user_message, client_factory=cf_user_message) as g:
        g.custom_command('create-attachment', 'usersmail_create_attachment')
        g.custom_command('create-extension', 'usersmail_create_extension')
        g.custom_command('create-mention', 'usersmail_create_mention')
        g.custom_command('create-multi-value-extended-property', 'usersmail_create_multi_value_extended_property')
        g.custom_command('create-single-value-extended-property', 'usersmail_create_single_value_extended_property')
        g.custom_command('get-attachment', 'usersmail_get_attachment')
        g.custom_command('get-extension', 'usersmail_get_extension')
        g.custom_command('get-mention', 'usersmail_get_mention')
        g.custom_command('get-multi-value-extended-property', 'usersmail_get_multi_value_extended_property')
        g.custom_command('get-single-value-extended-property', 'usersmail_get_single_value_extended_property')
        g.custom_command('list-attachment', 'usersmail_list_attachment')
        g.custom_command('list-extension', 'usersmail_list_extension')
        g.custom_command('list-mention', 'usersmail_list_mention')
        g.custom_command('list-multi-value-extended-property', 'usersmail_list_multi_value_extended_property')
        g.custom_command('list-single-value-extended-property', 'usersmail_list_single_value_extended_property')
        g.custom_command('update-attachment', 'usersmail_update_attachment')
        g.custom_command('update-extension', 'usersmail_update_extension')
        g.custom_command('update-mention', 'usersmail_update_mention')
        g.custom_command('update-multi-value-extended-property', 'usersmail_update_multi_value_extended_property')
        g.custom_command('update-single-value-extended-property', 'usersmail_update_single_value_extended_property')
