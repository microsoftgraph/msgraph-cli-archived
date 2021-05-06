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


class AddBody(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.body = action

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
            elif kl == 'content-type':
                d['content_type'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter body. All possible keys are: content, '
                               'content-type'.format(k))
        return d


class AddEnd(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.end = action

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
            if kl == 'date-time':
                d['date_time'] = v[0]
            elif kl == 'time-zone':
                d['time_zone'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter end. All possible keys are: date-time, '
                               'time-zone'.format(k))
        return d


class AddResponseStatus(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.response_status = action

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
            if kl == 'response':
                d['response'] = v[0]
            elif kl == 'time':
                d['time'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter response_status. All possible keys are: '
                               'response, time'.format(k))
        return d


class AddAttachments(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAttachments, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'content-type':
                d['content_type'] = v[0]
            elif kl == 'is-inline':
                d['is_inline'] = v[0]
            elif kl == 'last-modified-date-time':
                d['last_modified_date_time'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
            elif kl == 'size':
                d['size'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter attachments. All possible keys are: '
                               'content-type, is-inline, last-modified-date-time, name, size, id'.format(k))
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


class AddCalendarGroupCreateCalendarViewMultiValueExtendedProperties(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddCalendarGroupCreateCalendarViewMultiValueExtendedProperties, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'value':
                d['value'] = v
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter multi_value_extended_properties. All '
                               'possible keys are: value, id'.format(k))
        return d


class AddCalendarGroupCreateCalendarViewSingleValueExtendedProperties(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddCalendarGroupCreateCalendarViewSingleValueExtendedProperties, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'value':
                d['value'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter single_value_extended_properties. All '
                               'possible keys are: value, id'.format(k))
        return d


class AddPattern(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.pattern = action

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
            if kl == 'day-of-month':
                d['day_of_month'] = v[0]
            elif kl == 'days-of-week':
                d['days_of_week'] = v
            elif kl == 'first-day-of-week':
                d['first_day_of_week'] = v[0]
            elif kl == 'index':
                d['index'] = v[0]
            elif kl == 'interval':
                d['interval'] = v[0]
            elif kl == 'month':
                d['month'] = v[0]
            elif kl == 'type':
                d['type'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter pattern. All possible keys are: '
                               'day-of-month, days-of-week, first-day-of-week, index, interval, month, type'.format(k))
        return d


class AddRange(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.range = action

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
            if kl == 'end-date':
                d['end_date'] = v[0]
            elif kl == 'number-of-occurrences':
                d['number_of_occurrences'] = v[0]
            elif kl == 'recurrence-time-zone':
                d['recurrence_time_zone'] = v[0]
            elif kl == 'start-date':
                d['start_date'] = v[0]
            elif kl == 'type':
                d['type'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter range. All possible keys are: end-date, '
                               'number-of-occurrences, recurrence-time-zone, start-date, type'.format(k))
        return d


class AddOwner(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.email_address = action

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
            if kl == 'address':
                d['address'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter email_address. All possible keys are: '
                               'address, name'.format(k))
        return d


class AddPhones(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddPhones, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'language':
                d['language'] = v[0]
            elif kl == 'number':
                d['number'] = v[0]
            elif kl == 'region':
                d['region'] = v[0]
            elif kl == 'type':
                d['type'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter phones. All possible keys are: language, '
                               'number, region, type'.format(k))
        return d


class AddAddress(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.address = action

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
            if kl == 'city':
                d['city'] = v[0]
            elif kl == 'country-or-region':
                d['country_or_region'] = v[0]
            elif kl == 'postal-code':
                d['postal_code'] = v[0]
            elif kl == 'state':
                d['state'] = v[0]
            elif kl == 'street':
                d['street'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter address. All possible keys are: city, '
                               'country-or-region, postal-code, state, street'.format(k))
        return d


class AddCoordinates(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.coordinates = action

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
            if kl == 'accuracy':
                d['accuracy'] = v[0]
            elif kl == 'altitude':
                d['altitude'] = v[0]
            elif kl == 'altitude-accuracy':
                d['altitude_accuracy'] = v[0]
            elif kl == 'latitude':
                d['latitude'] = v[0]
            elif kl == 'longitude':
                d['longitude'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter coordinates. All possible keys are: '
                               'accuracy, altitude, altitude-accuracy, latitude, longitude'.format(k))
        return d


class AddCalendarGroupUpdateCalendarMultiValueExtendedProperties(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddCalendarGroupUpdateCalendarMultiValueExtendedProperties, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'value':
                d['value'] = v
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter multi_value_extended_properties. All '
                               'possible keys are: value, id'.format(k))
        return d


class AddCalendarGroupUpdateCalendarSingleValueExtendedProperties(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddCalendarGroupUpdateCalendarSingleValueExtendedProperties, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'value':
                d['value'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter single_value_extended_properties. All '
                               'possible keys are: value, id'.format(k))
        return d
