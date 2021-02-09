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

    from azext_education_v1_0.generated._client_factory import cf_education_education_root
    education_v1_0_education_education_root = CliCommandType(
        operations_tmpl='azext_education_v1_0.vendored_sdks.education.operations._education_education_root_operations#E'
        'ducationEducationRootOperations.{}',
        client_factory=cf_education_education_root)
    with self.command_group('education education-root', education_v1_0_education_education_root,
                            client_factory=cf_education_education_root, is_experimental=True) as g:
        g.custom_command('get-root', 'education_education_root_get_root')
        g.custom_command('update-root', 'education_education_root_update_root')

    from azext_education_v1_0.generated._client_factory import cf_education
    education_v1_0_education = CliCommandType(
        operations_tmpl='azext_education_v1_0.vendored_sdks.education.operations._education_operations#EducationOperati'
        'ons.{}',
        client_factory=cf_education)
    with self.command_group('education education', education_v1_0_education, client_factory=cf_education,
                            is_experimental=True) as g:
        g.custom_command('delete', 'education_education_delete', confirmation=True)
        g.custom_command('create-class', 'education_education_create_class')
        g.custom_command('create-school', 'education_education_create_school')
        g.custom_command('create-user', 'education_education_create_user')
        g.custom_command('get-class', 'education_education_get_class')
        g.custom_command('get-me', 'education_education_get_me')
        g.custom_command('get-school', 'education_education_get_school')
        g.custom_command('get-user', 'education_education_get_user')
        g.custom_command('list-class', 'education_education_list_class')
        g.custom_command('list-school', 'education_education_list_school')
        g.custom_command('list-user', 'education_education_list_user')
        g.custom_command('update-class', 'education_education_update_class')
        g.custom_command('update-me', 'education_education_update_me')
        g.custom_command('update-school', 'education_education_update_school')
        g.custom_command('update-user', 'education_education_update_user')

    from azext_education_v1_0.generated._client_factory import cf_education_class
    education_v1_0_education_class = CliCommandType(
        operations_tmpl='azext_education_v1_0.vendored_sdks.education.operations._education_class_operations#EducationC'
        'lassOperations.{}',
        client_factory=cf_education_class)
    with self.command_group('education education-class', education_v1_0_education_class,
                            client_factory=cf_education_class, is_experimental=True) as g:
        g.custom_command('delete', 'education_education_class_delete', confirmation=True)
        g.custom_command('create-ref-member', 'education_education_class_create_ref_member')
        g.custom_command('create-ref-school', 'education_education_class_create_ref_school')
        g.custom_command('create-ref-teacher', 'education_education_class_create_ref_teacher')
        g.custom_command('get-group', 'education_education_class_get_group')
        g.custom_command('get-ref-group', 'education_education_class_get_ref_group')
        g.custom_command('list-member', 'education_education_class_list_member')
        g.custom_command('list-ref-member', 'education_education_class_list_ref_member')
        g.custom_command('list-ref-school', 'education_education_class_list_ref_school')
        g.custom_command('list-ref-teacher', 'education_education_class_list_ref_teacher')
        g.custom_command('list-school', 'education_education_class_list_school')
        g.custom_command('list-teacher', 'education_education_class_list_teacher')
        g.custom_command('set-ref-group', 'education_education_class_set_ref_group')

    from azext_education_v1_0.generated._client_factory import cf_education_me
    education_v1_0_education_me = CliCommandType(
        operations_tmpl='azext_education_v1_0.vendored_sdks.education.operations._education_me_operations#EducationMeOp'
        'erations.{}',
        client_factory=cf_education_me)
    with self.command_group('education education-me', education_v1_0_education_me, client_factory=cf_education_me,
                            is_experimental=True) as g:
        g.custom_command('delete', 'education_education_me_delete', confirmation=True)
        g.custom_command('create-ref-class', 'education_education_me_create_ref_class')
        g.custom_command('create-ref-school', 'education_education_me_create_ref_school')
        g.custom_command('get-ref-user', 'education_education_me_get_ref_user')
        g.custom_command('get-user', 'education_education_me_get_user')
        g.custom_command('list-class', 'education_education_me_list_class')
        g.custom_command('list-ref-class', 'education_education_me_list_ref_class')
        g.custom_command('list-ref-school', 'education_education_me_list_ref_school')
        g.custom_command('list-school', 'education_education_me_list_school')
        g.custom_command('set-ref-user', 'education_education_me_set_ref_user')

    from azext_education_v1_0.generated._client_factory import cf_education_school
    education_v1_0_education_school = CliCommandType(
        operations_tmpl='azext_education_v1_0.vendored_sdks.education.operations._education_school_operations#Education'
        'SchoolOperations.{}',
        client_factory=cf_education_school)
    with self.command_group('education education-school', education_v1_0_education_school,
                            client_factory=cf_education_school, is_experimental=True) as g:
        g.custom_command('create-ref-class', 'education_education_school_create_ref_class')
        g.custom_command('create-ref-user', 'education_education_school_create_ref_user')
        g.custom_command('list-class', 'education_education_school_list_class')
        g.custom_command('list-ref-class', 'education_education_school_list_ref_class')
        g.custom_command('list-ref-user', 'education_education_school_list_ref_user')
        g.custom_command('list-user', 'education_education_school_list_user')

    from azext_education_v1_0.generated._client_factory import cf_education_user
    education_v1_0_education_user = CliCommandType(
        operations_tmpl='azext_education_v1_0.vendored_sdks.education.operations._education_user_operations#EducationUs'
        'erOperations.{}',
        client_factory=cf_education_user)
    with self.command_group('education education-user', education_v1_0_education_user,
                            client_factory=cf_education_user, is_experimental=True) as g:
        g.custom_command('delete', 'education_education_user_delete', confirmation=True)
        g.custom_command('create-ref-class', 'education_education_user_create_ref_class')
        g.custom_command('create-ref-school', 'education_education_user_create_ref_school')
        g.custom_command('get-ref-user', 'education_education_user_get_ref_user')
        g.custom_command('get-user', 'education_education_user_get_user')
        g.custom_command('list-class', 'education_education_user_list_class')
        g.custom_command('list-ref-class', 'education_education_user_list_ref_class')
        g.custom_command('list-ref-school', 'education_education_user_list_ref_school')
        g.custom_command('list-school', 'education_education_user_list_school')
        g.custom_command('set-ref-user', 'education_education_user_set_ref_user')