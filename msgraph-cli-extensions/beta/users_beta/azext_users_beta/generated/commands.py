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

    from azext_users_beta.generated._client_factory import cf_user_user
    users_beta_user_user = CliCommandType(
        operations_tmpl='azext_users_beta.vendored_sdks.users.operations._user_user_operations#UserUserOperations.{}',
        client_factory=cf_user_user)
    with self.command_group('users user-user', users_beta_user_user, client_factory=cf_user_user,
                            is_experimental=True) as g:
        g.custom_command('delete', 'users_user_user_delete', confirmation=True)
        g.custom_command('create-user', 'users_user_user_create_user')
        g.custom_command('get-user', 'users_user_user_get_user')
        g.custom_command('list-user', 'users_user_user_list_user')
        g.custom_command('update-user', 'users_user_user_update_user')

    from azext_users_beta.generated._client_factory import cf_user
    users_beta_user = CliCommandType(
        operations_tmpl='azext_users_beta.vendored_sdks.users.operations._user_operations#UserOperations.{}',
        client_factory=cf_user)
    with self.command_group('users user', users_beta_user, client_factory=cf_user, is_experimental=True) as g:
        g.custom_command('delete', 'users_user_delete', confirmation=True)
        g.custom_command('create-extension', 'users_user_create_extension')
        g.custom_command('create-license-detail', 'users_user_create_license_detail')
        g.custom_command('create-notification', 'users_user_create_notification')
        g.custom_command('create-photo', 'users_user_create_photo')
        g.custom_command('create-ref-created-object', 'users_user_create_ref_created_object')
        g.custom_command('create-ref-direct-report', 'users_user_create_ref_direct_report')
        g.custom_command('create-ref-member-of', 'users_user_create_ref_member_of')
        g.custom_command('create-ref-owned-device', 'users_user_create_ref_owned_device')
        g.custom_command('create-ref-owned-object', 'users_user_create_ref_owned_object')
        g.custom_command('create-ref-registered-device', 'users_user_create_ref_registered_device')
        g.custom_command('create-ref-transitive-member-of', 'users_user_create_ref_transitive_member_of')
        g.custom_command('get-extension', 'users_user_get_extension')
        g.custom_command('get-license-detail', 'users_user_get_license_detail')
        g.custom_command('get-manager', 'users_user_get_manager')
        g.custom_command('get-notification', 'users_user_get_notification')
        g.custom_command('get-outlook', 'users_user_get_outlook')
        g.custom_command('get-photo', 'users_user_get_photo')
        g.custom_command('get-photo-content', 'users_user_get_photo_content')
        g.custom_command('get-ref-manager', 'users_user_get_ref_manager')
        g.custom_command('get-setting', 'users_user_get_setting')
        g.custom_command('get-todo', 'users_user_get_todo')
        g.custom_command('list-created-object', 'users_user_list_created_object')
        g.custom_command('list-direct-report', 'users_user_list_direct_report')
        g.custom_command('list-extension', 'users_user_list_extension')
        g.custom_command('list-license-detail', 'users_user_list_license_detail')
        g.custom_command('list-member-of', 'users_user_list_member_of')
        g.custom_command('list-notification', 'users_user_list_notification')
        g.custom_command('list-owned-device', 'users_user_list_owned_device')
        g.custom_command('list-owned-object', 'users_user_list_owned_object')
        g.custom_command('list-photo', 'users_user_list_photo')
        g.custom_command('list-ref-created-object', 'users_user_list_ref_created_object')
        g.custom_command('list-ref-direct-report', 'users_user_list_ref_direct_report')
        g.custom_command('list-ref-member-of', 'users_user_list_ref_member_of')
        g.custom_command('list-ref-owned-device', 'users_user_list_ref_owned_device')
        g.custom_command('list-ref-owned-object', 'users_user_list_ref_owned_object')
        g.custom_command('list-ref-registered-device', 'users_user_list_ref_registered_device')
        g.custom_command('list-ref-transitive-member-of', 'users_user_list_ref_transitive_member_of')
        g.custom_command('list-registered-device', 'users_user_list_registered_device')
        g.custom_command('list-transitive-member-of', 'users_user_list_transitive_member_of')
        g.custom_command('set-photo-content', 'users_user_set_photo_content')
        g.custom_command('set-ref-manager', 'users_user_set_ref_manager')
        g.custom_command('update-extension', 'users_user_update_extension')
        g.custom_command('update-license-detail', 'users_user_update_license_detail')
        g.custom_command('update-notification', 'users_user_update_notification')
        g.custom_command('update-outlook', 'users_user_update_outlook')
        g.custom_command('update-photo', 'users_user_update_photo')
        g.custom_command('update-setting', 'users_user_update_setting')
        g.custom_command('update-todo', 'users_user_update_todo')

    from azext_users_beta.generated._client_factory import cf_user_outlook
    users_beta_user_outlook = CliCommandType(
        operations_tmpl='azext_users_beta.vendored_sdks.users.operations._user_outlook_operations#UserOutlookOperations'
        '.{}',
        client_factory=cf_user_outlook)
    with self.command_group('users user-outlook', users_beta_user_outlook, client_factory=cf_user_outlook,
                            is_experimental=True) as g:
        g.custom_command('delete', 'users_user_outlook_delete', confirmation=True)
        g.custom_command('create-master-category', 'users_user_outlook_create_master_category')
        g.custom_command('create-task', 'users_user_outlook_create_task')
        g.custom_command('create-task-folder', 'users_user_outlook_create_task_folder')
        g.custom_command('create-task-group', 'users_user_outlook_create_task_group')
        g.custom_command('get-master-category', 'users_user_outlook_get_master_category')
        g.custom_command('get-task', 'users_user_outlook_get_task')
        g.custom_command('get-task-folder', 'users_user_outlook_get_task_folder')
        g.custom_command('get-task-group', 'users_user_outlook_get_task_group')
        g.custom_command('list-master-category', 'users_user_outlook_list_master_category')
        g.custom_command('list-task', 'users_user_outlook_list_task')
        g.custom_command('list-task-folder', 'users_user_outlook_list_task_folder')
        g.custom_command('list-task-group', 'users_user_outlook_list_task_group')
        g.custom_command('update-master-category', 'users_user_outlook_update_master_category')
        g.custom_command('update-task', 'users_user_outlook_update_task')
        g.custom_command('update-task-folder', 'users_user_outlook_update_task_folder')
        g.custom_command('update-task-group', 'users_user_outlook_update_task_group')

    from azext_users_beta.generated._client_factory import cf_user_outlook_task_folder
    users_beta_user_outlook_task_folder = CliCommandType(
        operations_tmpl='azext_users_beta.vendored_sdks.users.operations._user_outlook_task_folder_operations#UserOutlo'
        'okTaskFolderOperations.{}',
        client_factory=cf_user_outlook_task_folder)
    with self.command_group('users user-outlook-task-folder', users_beta_user_outlook_task_folder,
                            client_factory=cf_user_outlook_task_folder, is_experimental=True) as g:
        g.custom_command('delete', 'users_user_outlook_task_folder_delete', confirmation=True)
        g.custom_command('create-multi-value-extended-property', 'users_user_outlook_task_folder_create_multi_value_ext'
                         'ended_property')
        g.custom_command('create-single-value-extended-property', 'users_user_outlook_task_folder_create_single_value_e'
                         'xtended_property')
        g.custom_command('create-task', 'users_user_outlook_task_folder_create_task')
        g.custom_command('get-multi-value-extended-property', 'users_user_outlook_task_folder_get_multi_value_extended_'
                         'property')
        g.custom_command('get-single-value-extended-property', 'users_user_outlook_task_folder_get_single_value_extende'
                         'd_property')
        g.custom_command('get-task', 'users_user_outlook_task_folder_get_task')
        g.custom_command('list-multi-value-extended-property', 'users_user_outlook_task_folder_list_multi_value_extende'
                         'd_property')
        g.custom_command('list-single-value-extended-property', 'users_user_outlook_task_folder_list_single_value_exten'
                         'ded_property')
        g.custom_command('list-task', 'users_user_outlook_task_folder_list_task')
        g.custom_command('update-multi-value-extended-property', 'users_user_outlook_task_folder_update_multi_value_ext'
                         'ended_property')
        g.custom_command('update-single-value-extended-property', 'users_user_outlook_task_folder_update_single_value_e'
                         'xtended_property')
        g.custom_command('update-task', 'users_user_outlook_task_folder_update_task')

    from azext_users_beta.generated._client_factory import cf_user_outlook_task_folder_task
    users_beta_user_outlook_task_folder_task = CliCommandType(
        operations_tmpl='azext_users_beta.vendored_sdks.users.operations._user_outlook_task_folder_task_operations#User'
        'OutlookTaskFolderTaskOperations.{}',
        client_factory=cf_user_outlook_task_folder_task)
    with self.command_group('users user-outlook-task-folder-task', users_beta_user_outlook_task_folder_task,
                            client_factory=cf_user_outlook_task_folder_task, is_experimental=True) as g:
        g.custom_command('delete', 'users_user_outlook_task_folder_task_delete', confirmation=True)
        g.custom_command('create-attachment', 'users_user_outlook_task_folder_task_create_attachment')
        g.custom_command('create-multi-value-extended-property', 'users_user_outlook_task_folder_task_create_multi_valu'
                         'e_extended_property')
        g.custom_command('create-single-value-extended-property', 'users_user_outlook_task_folder_task_create_single_va'
                         'lue_extended_property')
        g.custom_command('get-attachment', 'users_user_outlook_task_folder_task_get_attachment')
        g.custom_command('get-multi-value-extended-property', 'users_user_outlook_task_folder_task_get_multi_value_exte'
                         'nded_property')
        g.custom_command('get-single-value-extended-property', 'users_user_outlook_task_folder_task_get_single_value_ex'
                         'tended_property')
        g.custom_command('list-attachment', 'users_user_outlook_task_folder_task_list_attachment')
        g.custom_command('list-multi-value-extended-property', 'users_user_outlook_task_folder_task_list_multi_value_ex'
                         'tended_property')
        g.custom_command('list-single-value-extended-property', 'users_user_outlook_task_folder_task_list_single_value_'
                         'extended_property')
        g.custom_command('update-attachment', 'users_user_outlook_task_folder_task_update_attachment')
        g.custom_command('update-multi-value-extended-property', 'users_user_outlook_task_folder_task_update_multi_valu'
                         'e_extended_property')
        g.custom_command('update-single-value-extended-property', 'users_user_outlook_task_folder_task_update_single_va'
                         'lue_extended_property')

    from azext_users_beta.generated._client_factory import cf_user_outlook_task_group
    users_beta_user_outlook_task_group = CliCommandType(
        operations_tmpl='azext_users_beta.vendored_sdks.users.operations._user_outlook_task_group_operations#UserOutloo'
        'kTaskGroupOperations.{}',
        client_factory=cf_user_outlook_task_group)
    with self.command_group('users user-outlook-task-group', users_beta_user_outlook_task_group,
                            client_factory=cf_user_outlook_task_group, is_experimental=True) as g:
        g.custom_command('delete', 'users_user_outlook_task_group_delete', confirmation=True)
        g.custom_command('create-task-folder', 'users_user_outlook_task_group_create_task_folder')
        g.custom_command('get-task-folder', 'users_user_outlook_task_group_get_task_folder')
        g.custom_command('list-task-folder', 'users_user_outlook_task_group_list_task_folder')
        g.custom_command('update-task-folder', 'users_user_outlook_task_group_update_task_folder')

    from azext_users_beta.generated._client_factory import cf_user_outlook_task_group_task_folder
    users_beta_user_outlook_task_group_task_folder = CliCommandType(
        operations_tmpl='azext_users_beta.vendored_sdks.users.operations._user_outlook_task_group_task_folder_operation'
        's#UserOutlookTaskGroupTaskFolderOperations.{}',
        client_factory=cf_user_outlook_task_group_task_folder)
    with self.command_group('users user-outlook-task-group-task-folder',
                            users_beta_user_outlook_task_group_task_folder,
                            client_factory=cf_user_outlook_task_group_task_folder, is_experimental=True) as g:
        g.custom_command('delete', 'users_user_outlook_task_group_task_folder_delete', confirmation=True)
        g.custom_command('create-multi-value-extended-property', 'users_user_outlook_task_group_task_folder_create_mult'
                         'i_value_extended_property')
        g.custom_command('create-single-value-extended-property', 'users_user_outlook_task_group_task_folder_create_sin'
                         'gle_value_extended_property')
        g.custom_command('create-task', 'users_user_outlook_task_group_task_folder_create_task')
        g.custom_command('get-multi-value-extended-property', 'users_user_outlook_task_group_task_folder_get_multi_valu'
                         'e_extended_property')
        g.custom_command('get-single-value-extended-property', 'users_user_outlook_task_group_task_folder_get_single_va'
                         'lue_extended_property')
        g.custom_command('get-task', 'users_user_outlook_task_group_task_folder_get_task')
        g.custom_command('list-multi-value-extended-property', 'users_user_outlook_task_group_task_folder_list_multi_va'
                         'lue_extended_property')
        g.custom_command('list-single-value-extended-property', 'users_user_outlook_task_group_task_folder_list_single_'
                         'value_extended_property')
        g.custom_command('list-task', 'users_user_outlook_task_group_task_folder_list_task')
        g.custom_command('update-multi-value-extended-property', 'users_user_outlook_task_group_task_folder_update_mult'
                         'i_value_extended_property')
        g.custom_command('update-single-value-extended-property', 'users_user_outlook_task_group_task_folder_update_sin'
                         'gle_value_extended_property')
        g.custom_command('update-task', 'users_user_outlook_task_group_task_folder_update_task')

    from azext_users_beta.generated._client_factory import cf_user_outlook_task_group_task_folder_task
    users_beta_user_outlook_task_group_task_folder_task = CliCommandType(
        operations_tmpl='azext_users_beta.vendored_sdks.users.operations._user_outlook_task_group_task_folder_task_oper'
        'ations#UserOutlookTaskGroupTaskFolderTaskOperations.{}',
        client_factory=cf_user_outlook_task_group_task_folder_task)
    with self.command_group('users user-outlook-task-group-task-folder-task',
                            users_beta_user_outlook_task_group_task_folder_task,
                            client_factory=cf_user_outlook_task_group_task_folder_task, is_experimental=True) as g:
        g.custom_command('delete', 'users_user_outlook_task_group_task_folder_task_delete', confirmation=True)
        g.custom_command('create-attachment', 'users_user_outlook_task_group_task_folder_task_create_attachment')
        g.custom_command('create-multi-value-extended-property', 'users_user_outlook_task_group_task_folder_task_create'
                         '_multi_value_extended_property')
        g.custom_command('create-single-value-extended-property', 'users_user_outlook_task_group_task_folder_task_creat'
                         'e_single_value_extended_property')
        g.custom_command('get-attachment', 'users_user_outlook_task_group_task_folder_task_get_attachment')
        g.custom_command('get-multi-value-extended-property', 'users_user_outlook_task_group_task_folder_task_get_multi'
                         '_value_extended_property')
        g.custom_command('get-single-value-extended-property', 'users_user_outlook_task_group_task_folder_task_get_sing'
                         'le_value_extended_property')
        g.custom_command('list-attachment', 'users_user_outlook_task_group_task_folder_task_list_attachment')
        g.custom_command('list-multi-value-extended-property', 'users_user_outlook_task_group_task_folder_task_list_mul'
                         'ti_value_extended_property')
        g.custom_command('list-single-value-extended-property', 'users_user_outlook_task_group_task_folder_task_list_si'
                         'ngle_value_extended_property')
        g.custom_command('update-attachment', 'users_user_outlook_task_group_task_folder_task_update_attachment')
        g.custom_command('update-multi-value-extended-property', 'users_user_outlook_task_group_task_folder_task_update'
                         '_multi_value_extended_property')
        g.custom_command('update-single-value-extended-property', 'users_user_outlook_task_group_task_folder_task_updat'
                         'e_single_value_extended_property')

    from azext_users_beta.generated._client_factory import cf_user_outlook_task
    users_beta_user_outlook_task = CliCommandType(
        operations_tmpl='azext_users_beta.vendored_sdks.users.operations._user_outlook_task_operations#UserOutlookTaskO'
        'perations.{}',
        client_factory=cf_user_outlook_task)
    with self.command_group('users user-outlook-task', users_beta_user_outlook_task,
                            client_factory=cf_user_outlook_task, is_experimental=True) as g:
        g.custom_command('delete', 'users_user_outlook_task_delete', confirmation=True)
        g.custom_command('create-attachment', 'users_user_outlook_task_create_attachment')
        g.custom_command('create-multi-value-extended-property', 'users_user_outlook_task_create_multi_value_extended_p'
                         'roperty')
        g.custom_command('create-single-value-extended-property', 'users_user_outlook_task_create_single_value_extended'
                         '_property')
        g.custom_command('get-attachment', 'users_user_outlook_task_get_attachment')
        g.custom_command('get-multi-value-extended-property', 'users_user_outlook_task_get_multi_value_extended_propert'
                         'y')
        g.custom_command('get-single-value-extended-property', 'users_user_outlook_task_get_single_value_extended_prope'
                         'rty')
        g.custom_command('list-attachment', 'users_user_outlook_task_list_attachment')
        g.custom_command('list-multi-value-extended-property', 'users_user_outlook_task_list_multi_value_extended_prope'
                         'rty')
        g.custom_command('list-single-value-extended-property', 'users_user_outlook_task_list_single_value_extended_pro'
                         'perty')
        g.custom_command('update-attachment', 'users_user_outlook_task_update_attachment')
        g.custom_command('update-multi-value-extended-property', 'users_user_outlook_task_update_multi_value_extended_p'
                         'roperty')
        g.custom_command('update-single-value-extended-property', 'users_user_outlook_task_update_single_value_extended'
                         '_property')

    from azext_users_beta.generated._client_factory import cf_user_setting
    users_beta_user_setting = CliCommandType(
        operations_tmpl='azext_users_beta.vendored_sdks.users.operations._user_setting_operations#UserSettingOperations'
        '.{}',
        client_factory=cf_user_setting)
    with self.command_group('users user-setting', users_beta_user_setting, client_factory=cf_user_setting,
                            is_experimental=True) as g:
        g.custom_command('delete', 'users_user_setting_delete', confirmation=True)
        g.custom_command('get-regional-and-language-setting', 'users_user_setting_get_regional_and_language_setting')
        g.custom_command('get-shift-preference', 'users_user_setting_get_shift_preference')
        g.custom_command('update-regional-and-language-setting', 'users_user_setting_update_regional_and_language_setti'
                         'ng')
        g.custom_command('update-shift-preference', 'users_user_setting_update_shift_preference')

    from azext_users_beta.generated._client_factory import cf_user_todo
    users_beta_user_todo = CliCommandType(
        operations_tmpl='azext_users_beta.vendored_sdks.users.operations._user_todo_operations#UserTodoOperations.{}',
        client_factory=cf_user_todo)
    with self.command_group('users user-todo', users_beta_user_todo, client_factory=cf_user_todo,
                            is_experimental=True) as g:
        g.custom_command('delete', 'users_user_todo_delete', confirmation=True)
        g.custom_command('create-list', 'users_user_todo_create_list')
        g.custom_command('get-list', 'users_user_todo_get_list')
        g.custom_command('list-list', 'users_user_todo_list_list')
        g.custom_command('update-list', 'users_user_todo_update_list')

    from azext_users_beta.generated._client_factory import cf_user_todo_list
    users_beta_user_todo_list = CliCommandType(
        operations_tmpl='azext_users_beta.vendored_sdks.users.operations._user_todo_list_operations#UserTodoListOperati'
        'ons.{}',
        client_factory=cf_user_todo_list)
    with self.command_group('users user-todo-list', users_beta_user_todo_list, client_factory=cf_user_todo_list,
                            is_experimental=True) as g:
        g.custom_command('delete', 'users_user_todo_list_delete', confirmation=True)
        g.custom_command('create-extension', 'users_user_todo_list_create_extension')
        g.custom_command('create-task', 'users_user_todo_list_create_task')
        g.custom_command('get-extension', 'users_user_todo_list_get_extension')
        g.custom_command('get-task', 'users_user_todo_list_get_task')
        g.custom_command('list-extension', 'users_user_todo_list_list_extension')
        g.custom_command('list-task', 'users_user_todo_list_list_task')
        g.custom_command('update-extension', 'users_user_todo_list_update_extension')
        g.custom_command('update-task', 'users_user_todo_list_update_task')

    from azext_users_beta.generated._client_factory import cf_user_todo_list_task
    users_beta_user_todo_list_task = CliCommandType(
        operations_tmpl='azext_users_beta.vendored_sdks.users.operations._user_todo_list_task_operations#UserTodoListTa'
        'skOperations.{}',
        client_factory=cf_user_todo_list_task)
    with self.command_group('users user-todo-list-task', users_beta_user_todo_list_task,
                            client_factory=cf_user_todo_list_task, is_experimental=True) as g:
        g.custom_command('delete', 'users_user_todo_list_task_delete', confirmation=True)
        g.custom_command('create-extension', 'users_user_todo_list_task_create_extension')
        g.custom_command('create-linked-resource', 'users_user_todo_list_task_create_linked_resource')
        g.custom_command('get-extension', 'users_user_todo_list_task_get_extension')
        g.custom_command('get-linked-resource', 'users_user_todo_list_task_get_linked_resource')
        g.custom_command('list-extension', 'users_user_todo_list_task_list_extension')
        g.custom_command('list-linked-resource', 'users_user_todo_list_task_list_linked_resource')
        g.custom_command('update-extension', 'users_user_todo_list_task_update_extension')
        g.custom_command('update-linked-resource', 'users_user_todo_list_task_update_linked_resource')
