# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from collections import defaultdict
from knack.util import CLIError


class AddAssignedLicenses(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAssignedLicenses, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'disabled-plans':
                d['disabled_plans'] = v
            elif kl == 'sku-id':
                d['sku_id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter assigned_licenses. All possible keys are: '
                               'disabled-plans, sku-id'.format(k))
        return d


class AddAssignedPlans(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAssignedPlans, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'assigned-date-time':
                d['assigned_date_time'] = v[0]
            elif kl == 'capability-status':
                d['capability_status'] = v[0]
            elif kl == 'service':
                d['service'] = v[0]
            elif kl == 'service-plan-id':
                d['service_plan_id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter assigned_plans. All possible keys are: '
                               'assigned-date-time, capability-status, service, service-plan-id'.format(k))
        return d


class AddIdentities(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddIdentities, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'issuer':
                d['issuer'] = v[0]
            elif kl == 'issuer-assigned-id':
                d['issuer_assigned_id'] = v[0]
            elif kl == 'sign-in-type':
                d['sign_in_type'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter identities. All possible keys are: '
                               'issuer, issuer-assigned-id, sign-in-type'.format(k))
        return d


class AddLicenseAssignmentStates(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddLicenseAssignmentStates, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'assigned-by-group':
                d['assigned_by_group'] = v[0]
            elif kl == 'disabled-plans':
                d['disabled_plans'] = v
            elif kl == 'error':
                d['error'] = v[0]
            elif kl == 'sku-id':
                d['sku_id'] = v[0]
            elif kl == 'state':
                d['state'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter license_assignment_states. All possible '
                               'keys are: assigned-by-group, disabled-plans, error, sku-id, state'.format(k))
        return d


class AddOnPremisesExtensionAttributes(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.on_premises_extension_attributes = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'extension-attribute1':
                d['extension_attribute1'] = v[0]
            elif kl == 'extension-attribute10':
                d['extension_attribute10'] = v[0]
            elif kl == 'extension-attribute11':
                d['extension_attribute11'] = v[0]
            elif kl == 'extension-attribute12':
                d['extension_attribute12'] = v[0]
            elif kl == 'extension-attribute13':
                d['extension_attribute13'] = v[0]
            elif kl == 'extension-attribute14':
                d['extension_attribute14'] = v[0]
            elif kl == 'extension-attribute15':
                d['extension_attribute15'] = v[0]
            elif kl == 'extension-attribute2':
                d['extension_attribute2'] = v[0]
            elif kl == 'extension-attribute3':
                d['extension_attribute3'] = v[0]
            elif kl == 'extension-attribute4':
                d['extension_attribute4'] = v[0]
            elif kl == 'extension-attribute5':
                d['extension_attribute5'] = v[0]
            elif kl == 'extension-attribute6':
                d['extension_attribute6'] = v[0]
            elif kl == 'extension-attribute7':
                d['extension_attribute7'] = v[0]
            elif kl == 'extension-attribute8':
                d['extension_attribute8'] = v[0]
            elif kl == 'extension-attribute9':
                d['extension_attribute9'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter on_premises_extension_attributes. All '
                               'possible keys are: extension-attribute1, extension-attribute10, extension-attribute11, '
                               'extension-attribute12, extension-attribute13, extension-attribute14, '
                               'extension-attribute15, extension-attribute2, extension-attribute3, '
                               'extension-attribute4, extension-attribute5, extension-attribute6, '
                               'extension-attribute7, extension-attribute8, extension-attribute9'.format(k))
        return d


class AddOnPremisesProvisioningErrors(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddOnPremisesProvisioningErrors, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'category':
                d['category'] = v[0]
            elif kl == 'occurred-date-time':
                d['occurred_date_time'] = v[0]
            elif kl == 'property-causing-error':
                d['property_causing_error'] = v[0]
            elif kl == 'value':
                d['value'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter on_premises_provisioning_errors. All '
                               'possible keys are: category, occurred-date-time, property-causing-error, value'.format(k))
        return d


class AddPasswordProfile(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.password_profile = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'force-change-password-next-sign-in':
                d['force_change_password_next_sign_in'] = v[0]
            elif kl == 'force-change-password-next-sign-in-with-mfa':
                d['force_change_password_next_sign_in_with_mfa'] = v[0]
            elif kl == 'password':
                d['password'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter password_profile. All possible keys are: '
                               'force-change-password-next-sign-in, force-change-password-next-sign-in-with-mfa, '
                               'password'.format(k))
        return d


class AddProvisionedPlans(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddProvisionedPlans, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'capability-status':
                d['capability_status'] = v[0]
            elif kl == 'provisioning-status':
                d['provisioning_status'] = v[0]
            elif kl == 'service':
                d['service'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter provisioned_plans. All possible keys are: '
                               'capability-status, provisioning-status, service'.format(k))
        return d


class AddAppRoleAssignments(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAppRoleAssignments, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'app-role-id':
                d['app_role_id'] = v[0]
            elif kl == 'created-date-time':
                d['created_date_time'] = v[0]
            elif kl == 'principal-display-name':
                d['principal_display_name'] = v[0]
            elif kl == 'principal-id':
                d['principal_id'] = v[0]
            elif kl == 'principal-type':
                d['principal_type'] = v[0]
            elif kl == 'resource-display-name':
                d['resource_display_name'] = v[0]
            elif kl == 'resource-id':
                d['resource_id'] = v[0]
            elif kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter app_role_assignments. All possible keys '
                               'are: app-role-id, created-date-time, principal-display-name, principal-id, '
                               'principal-type, resource-display-name, resource-id, deleted-date-time, id'.format(k))
        return d


class AddCreatedObjects(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddCreatedObjects, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter created_objects. All possible keys are: '
                               'deleted-date-time, id'.format(k))
        return d


class AddDirectReports(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDirectReports, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter direct_reports. All possible keys are: '
                               'deleted-date-time, id'.format(k))
        return d


class AddManager(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.manager = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter manager. All possible keys are: '
                               'deleted-date-time, id'.format(k))
        return d


class AddMemberOf(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddMemberOf, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter member_of. All possible keys are: '
                               'deleted-date-time, id'.format(k))
        return d


class AddOauth2PermissionGrants(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddOauth2PermissionGrants, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'client-id':
                d['client_id'] = v[0]
            elif kl == 'consent-type':
                d['consent_type'] = v[0]
            elif kl == 'principal-id':
                d['principal_id'] = v[0]
            elif kl == 'resource-id':
                d['resource_id'] = v[0]
            elif kl == 'scope':
                d['scope'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter oauth2_permission_grants. All possible '
                               'keys are: client-id, consent-type, principal-id, resource-id, scope, id'.format(k))
        return d


class AddOwnedDevices(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddOwnedDevices, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter owned_devices. All possible keys are: '
                               'deleted-date-time, id'.format(k))
        return d


class AddOwnedObjects(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddOwnedObjects, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter owned_objects. All possible keys are: '
                               'deleted-date-time, id'.format(k))
        return d


class AddRegisteredDevices(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddRegisteredDevices, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter registered_devices. All possible keys '
                               'are: deleted-date-time, id'.format(k))
        return d


class AddTransitiveMemberOf(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddTransitiveMemberOf, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'deleted-date-time':
                d['deleted_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter transitive_member_of. All possible keys '
                               'are: deleted-date-time, id'.format(k))
        return d


class AddPhoto(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.photo = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'height':
                d['height'] = v[0]
            elif kl == 'width':
                d['width'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter photo. All possible keys are: height, '
                               'width, id'.format(k))
        return d


class AddPhotos(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddPhotos, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'height':
                d['height'] = v[0]
            elif kl == 'width':
                d['width'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter photos. All possible keys are: height, '
                               'width, id'.format(k))
        return d


class AddExtensions(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddExtensions, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter extensions. All possible keys are: id'.
                format(k))
        return d


class AddDeviceManagementTroubleshootingEvents(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDeviceManagementTroubleshootingEvents, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'correlation-id':
                d['correlation_id'] = v[0]
            elif kl == 'event-date-time':
                d['event_date_time'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter device_management_troubleshooting_events. '
                               'All possible keys are: correlation-id, event-date-time, id'.format(k))
        return d


class AddResources(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddResources, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'content':
                d['content'] = v[0]
            elif kl == 'content-url':
                d['content_url'] = v[0]
            elif kl == 'self':
                d['self_property'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter resources. All possible keys are: '
                               'content, content-url, self, id'.format(k))
        return d


class AddApplication(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.application = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter application. All possible keys are: '
                               'display-name, id'.format(k))
        return d


class AddMasterCategories(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddMasterCategories, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'color':
                d['color'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter master_categories. All possible keys are: '
                               'color, display-name, id'.format(k))
        return d


class AddLanguage(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.language = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'locale':
                d['locale'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter language. All possible keys are: '
                               'display-name, locale'.format(k))
        return d


class AddServicePlans(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddServicePlans, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'applies-to':
                d['applies_to'] = v[0]
            elif kl == 'provisioning-status':
                d['provisioning_status'] = v[0]
            elif kl == 'service-plan-id':
                d['service_plan_id'] = v[0]
            elif kl == 'service-plan-name':
                d['service_plan_name'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter service_plans. All possible keys are: '
                               'applies-to, provisioning-status, service-plan-id, service-plan-name'.format(k))
        return d
