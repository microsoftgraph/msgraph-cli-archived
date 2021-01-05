# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class Enum100(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    TASKS = "tasks"

class Enum101(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CREATED_BY = "createdBy"
    DISPLAY_NAME = "displayName"
    TASKS = "tasks"

class Enum102(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    TASKS = "tasks"

class Enum103(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    PARENT_URL = "parentUrl"
    PARENT_URL_DESC = "parentUrl desc"
    STATUS = "status"
    STATUS_DESC = "status desc"

class Enum104(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    PARENT_URL = "parentUrl"
    STATUS = "status"
    DEFINITION = "definition"
    TRIGGER = "trigger"

class Enum105(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    DEFINITION = "definition"
    TRIGGER = "trigger"

class Enum106(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    PARENT_URL = "parentUrl"
    STATUS = "status"
    DEFINITION = "definition"
    TRIGGER = "trigger"

class Enum107(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    DEFINITION = "definition"
    TRIGGER = "trigger"

class Enum108(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CREATED_BY = "createdBy"
    DISPLAY_NAME = "displayName"
    TASKS = "tasks"

class Enum109(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    TASKS = "tasks"

class Enum110(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    EVENT = "event"
    DEFINITION = "definition"

class Enum111(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    DEFINITION = "definition"

class Enum28(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APP_VERSION = "appVersion"
    DEVICE_HEALTH = "deviceHealth"
    DISPLAY_NAME = "displayName"
    FULLY_QUALIFIED_DOMAIN_NAME = "fullyQualifiedDomainName"
    LOCATION = "location"
    NAME = "name"
    OPERATING_SYSTEM = "operatingSystem"
    REGISTERED_DATE_TIME = "registeredDateTime"

class Enum29(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    STATUS = "status"
    STATUS_DESC = "status desc"

class Enum30(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CREATED_DATE_TIME = "createdDateTime"
    STATUS = "status"

class Enum31(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CREATED_DATE_TIME = "createdDateTime"
    STATUS = "status"

class Enum32(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CAPABILITIES = "capabilities"
    CAPABILITIES_DESC = "capabilities desc"
    DEFAULTS = "defaults"
    DEFAULTS_DESC = "defaults desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    IS_ACCEPTING_JOBS = "isAcceptingJobs"
    IS_ACCEPTING_JOBS_DESC = "isAcceptingJobs desc"
    LOCATION = "location"
    LOCATION_DESC = "location desc"
    MANUFACTURER = "manufacturer"
    MANUFACTURER_DESC = "manufacturer desc"
    MODEL = "model"
    MODEL_DESC = "model desc"
    NAME = "name"
    NAME_DESC = "name desc"
    STATUS = "status"
    STATUS_DESC = "status desc"
    ACCEPTING_JOBS = "acceptingJobs"
    ACCEPTING_JOBS_DESC = "acceptingJobs desc"
    IS_SHARED = "isShared"
    IS_SHARED_DESC = "isShared desc"
    REGISTERED_DATE_TIME = "registeredDateTime"
    REGISTERED_DATE_TIME_DESC = "registeredDateTime desc"

class Enum33(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CAPABILITIES = "capabilities"
    DEFAULTS = "defaults"
    DISPLAY_NAME = "displayName"
    IS_ACCEPTING_JOBS = "isAcceptingJobs"
    LOCATION = "location"
    MANUFACTURER = "manufacturer"
    MODEL = "model"
    NAME = "name"
    STATUS = "status"
    ACCEPTING_JOBS = "acceptingJobs"
    IS_SHARED = "isShared"
    REGISTERED_DATE_TIME = "registeredDateTime"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    CONNECTORS = "connectors"
    SHARE = "share"
    SHARES = "shares"
    TASK_TRIGGERS = "taskTriggers"

class Enum34(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    CONNECTORS = "connectors"
    SHARE = "share"
    SHARES = "shares"
    TASK_TRIGGERS = "taskTriggers"

class Enum35(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CAPABILITIES = "capabilities"
    DEFAULTS = "defaults"
    DISPLAY_NAME = "displayName"
    IS_ACCEPTING_JOBS = "isAcceptingJobs"
    LOCATION = "location"
    MANUFACTURER = "manufacturer"
    MODEL = "model"
    NAME = "name"
    STATUS = "status"
    ACCEPTING_JOBS = "acceptingJobs"
    IS_SHARED = "isShared"
    REGISTERED_DATE_TIME = "registeredDateTime"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    CONNECTORS = "connectors"
    SHARE = "share"
    SHARES = "shares"
    TASK_TRIGGERS = "taskTriggers"

class Enum36(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    CONNECTORS = "connectors"
    SHARE = "share"
    SHARES = "shares"
    TASK_TRIGGERS = "taskTriggers"

class Enum37(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"

class Enum38(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"

class Enum39(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"

class Enum40(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    IP_ADDRESS = "ipAddress"
    IP_ADDRESS_DESC = "ipAddress desc"
    USER_PRINCIPAL_NAME = "userPrincipalName"
    USER_PRINCIPAL_NAME_DESC = "userPrincipalName desc"

class Enum41(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"
    IP_ADDRESS = "ipAddress"
    USER_PRINCIPAL_NAME = "userPrincipalName"

class Enum42(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"
    IP_ADDRESS = "ipAddress"
    USER_PRINCIPAL_NAME = "userPrincipalName"

class Enum43(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    APP_VERSION = "appVersion"
    APP_VERSION_DESC = "appVersion desc"
    DEVICE_HEALTH = "deviceHealth"
    DEVICE_HEALTH_DESC = "deviceHealth desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    FULLY_QUALIFIED_DOMAIN_NAME = "fullyQualifiedDomainName"
    FULLY_QUALIFIED_DOMAIN_NAME_DESC = "fullyQualifiedDomainName desc"
    LOCATION = "location"
    LOCATION_DESC = "location desc"
    NAME = "name"
    NAME_DESC = "name desc"
    OPERATING_SYSTEM = "operatingSystem"
    OPERATING_SYSTEM_DESC = "operatingSystem desc"
    REGISTERED_DATE_TIME = "registeredDateTime"
    REGISTERED_DATE_TIME_DESC = "registeredDateTime desc"

class Enum44(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APP_VERSION = "appVersion"
    DEVICE_HEALTH = "deviceHealth"
    DISPLAY_NAME = "displayName"
    FULLY_QUALIFIED_DOMAIN_NAME = "fullyQualifiedDomainName"
    LOCATION = "location"
    NAME = "name"
    OPERATING_SYSTEM = "operatingSystem"
    REGISTERED_DATE_TIME = "registeredDateTime"

class Enum45(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    APP_VERSION = "appVersion"
    APP_VERSION_DESC = "appVersion desc"
    DEVICE_HEALTH = "deviceHealth"
    DEVICE_HEALTH_DESC = "deviceHealth desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    FULLY_QUALIFIED_DOMAIN_NAME = "fullyQualifiedDomainName"
    FULLY_QUALIFIED_DOMAIN_NAME_DESC = "fullyQualifiedDomainName desc"
    LOCATION = "location"
    LOCATION_DESC = "location desc"
    NAME = "name"
    NAME_DESC = "name desc"
    OPERATING_SYSTEM = "operatingSystem"
    OPERATING_SYSTEM_DESC = "operatingSystem desc"
    REGISTERED_DATE_TIME = "registeredDateTime"
    REGISTERED_DATE_TIME_DESC = "registeredDateTime desc"

class Enum46(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CAPABILITIES = "capabilities"
    DEFAULTS = "defaults"
    DISPLAY_NAME = "displayName"
    IS_ACCEPTING_JOBS = "isAcceptingJobs"
    LOCATION = "location"
    MANUFACTURER = "manufacturer"
    MODEL = "model"
    NAME = "name"
    STATUS = "status"
    ALLOW_ALL_USERS = "allowAllUsers"
    CREATED_DATE_TIME = "createdDateTime"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    PRINTER = "printer"

class Enum47(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    PRINTER = "printer"

class Enum48(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CAPABILITIES = "capabilities"
    CAPABILITIES_DESC = "capabilities desc"
    DEFAULTS = "defaults"
    DEFAULTS_DESC = "defaults desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    IS_ACCEPTING_JOBS = "isAcceptingJobs"
    IS_ACCEPTING_JOBS_DESC = "isAcceptingJobs desc"
    LOCATION = "location"
    LOCATION_DESC = "location desc"
    MANUFACTURER = "manufacturer"
    MANUFACTURER_DESC = "manufacturer desc"
    MODEL = "model"
    MODEL_DESC = "model desc"
    NAME = "name"
    NAME_DESC = "name desc"
    STATUS = "status"
    STATUS_DESC = "status desc"
    ALLOW_ALL_USERS = "allowAllUsers"
    ALLOW_ALL_USERS_DESC = "allowAllUsers desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"

class Enum49(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CAPABILITIES = "capabilities"
    DEFAULTS = "defaults"
    DISPLAY_NAME = "displayName"
    IS_ACCEPTING_JOBS = "isAcceptingJobs"
    LOCATION = "location"
    MANUFACTURER = "manufacturer"
    MODEL = "model"
    NAME = "name"
    STATUS = "status"
    ALLOW_ALL_USERS = "allowAllUsers"
    CREATED_DATE_TIME = "createdDateTime"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    PRINTER = "printer"

class Enum50(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    PRINTER = "printer"

class Enum51(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CAPABILITIES = "capabilities"
    CAPABILITIES_DESC = "capabilities desc"
    DEFAULTS = "defaults"
    DEFAULTS_DESC = "defaults desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    IS_ACCEPTING_JOBS = "isAcceptingJobs"
    IS_ACCEPTING_JOBS_DESC = "isAcceptingJobs desc"
    LOCATION = "location"
    LOCATION_DESC = "location desc"
    MANUFACTURER = "manufacturer"
    MANUFACTURER_DESC = "manufacturer desc"
    MODEL = "model"
    MODEL_DESC = "model desc"
    NAME = "name"
    NAME_DESC = "name desc"
    STATUS = "status"
    STATUS_DESC = "status desc"
    ALLOW_ALL_USERS = "allowAllUsers"
    ALLOW_ALL_USERS_DESC = "allowAllUsers desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"

class Enum52(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    EVENT = "event"
    EVENT_DESC = "event desc"

class Enum53(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    EVENT = "event"
    DEFINITION = "definition"

class Enum54(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    DEFINITION = "definition"

class Enum55(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    EVENT = "event"
    DEFINITION = "definition"

class Enum56(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    DEFINITION = "definition"

class Enum57(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CREATED_BY = "createdBy"
    DISPLAY_NAME = "displayName"
    TASKS = "tasks"

class Enum58(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    TASKS = "tasks"

class Enum59(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CAPABILITIES = "capabilities"
    CAPABILITIES_DESC = "capabilities desc"
    DEFAULTS = "defaults"
    DEFAULTS_DESC = "defaults desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    IS_ACCEPTING_JOBS = "isAcceptingJobs"
    IS_ACCEPTING_JOBS_DESC = "isAcceptingJobs desc"
    LOCATION = "location"
    LOCATION_DESC = "location desc"
    MANUFACTURER = "manufacturer"
    MANUFACTURER_DESC = "manufacturer desc"
    MODEL = "model"
    MODEL_DESC = "model desc"
    NAME = "name"
    NAME_DESC = "name desc"
    STATUS = "status"
    STATUS_DESC = "status desc"
    ALLOW_ALL_USERS = "allowAllUsers"
    ALLOW_ALL_USERS_DESC = "allowAllUsers desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"

class Enum60(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CAPABILITIES = "capabilities"
    DEFAULTS = "defaults"
    DISPLAY_NAME = "displayName"
    IS_ACCEPTING_JOBS = "isAcceptingJobs"
    LOCATION = "location"
    MANUFACTURER = "manufacturer"
    MODEL = "model"
    NAME = "name"
    STATUS = "status"
    ALLOW_ALL_USERS = "allowAllUsers"
    CREATED_DATE_TIME = "createdDateTime"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    PRINTER = "printer"

class Enum61(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    PRINTER = "printer"

class Enum62(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CAPABILITIES = "capabilities"
    DEFAULTS = "defaults"
    DISPLAY_NAME = "displayName"
    IS_ACCEPTING_JOBS = "isAcceptingJobs"
    LOCATION = "location"
    MANUFACTURER = "manufacturer"
    MODEL = "model"
    NAME = "name"
    STATUS = "status"
    ALLOW_ALL_USERS = "allowAllUsers"
    CREATED_DATE_TIME = "createdDateTime"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    PRINTER = "printer"

class Enum63(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    PRINTER = "printer"

class Enum64(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"

class Enum65(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"

class Enum66(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"

class Enum67(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    IP_ADDRESS = "ipAddress"
    IP_ADDRESS_DESC = "ipAddress desc"
    USER_PRINCIPAL_NAME = "userPrincipalName"
    USER_PRINCIPAL_NAME_DESC = "userPrincipalName desc"

class Enum68(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"
    IP_ADDRESS = "ipAddress"
    USER_PRINCIPAL_NAME = "userPrincipalName"

class Enum69(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"
    IP_ADDRESS = "ipAddress"
    USER_PRINCIPAL_NAME = "userPrincipalName"

class Enum70(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CAPABILITIES = "capabilities"
    DEFAULTS = "defaults"
    DISPLAY_NAME = "displayName"
    IS_ACCEPTING_JOBS = "isAcceptingJobs"
    LOCATION = "location"
    MANUFACTURER = "manufacturer"
    MODEL = "model"
    NAME = "name"
    STATUS = "status"
    ACCEPTING_JOBS = "acceptingJobs"
    IS_SHARED = "isShared"
    REGISTERED_DATE_TIME = "registeredDateTime"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    CONNECTORS = "connectors"
    SHARE = "share"
    SHARES = "shares"
    TASK_TRIGGERS = "taskTriggers"

class Enum71(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    CONNECTORS = "connectors"
    SHARE = "share"
    SHARES = "shares"
    TASK_TRIGGERS = "taskTriggers"

class Enum72(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"

class Enum73(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APPLICATION_SIGN_IN_DETAILED_SUMMARY = "applicationSignInDetailedSummary"
    CREDENTIAL_USER_REGISTRATION_DETAILS = "credentialUserRegistrationDetails"
    USER_CREDENTIAL_USAGE_DETAILS = "userCredentialUsageDetails"
    DAILY_PRINT_USAGE_SUMMARIES_BY_PRINTER = "dailyPrintUsageSummariesByPrinter"
    DAILY_PRINT_USAGE_SUMMARIES_BY_USER = "dailyPrintUsageSummariesByUser"
    MONTHLY_PRINT_USAGE_SUMMARIES_BY_PRINTER = "monthlyPrintUsageSummariesByPrinter"
    MONTHLY_PRINT_USAGE_SUMMARIES_BY_USER = "monthlyPrintUsageSummariesByUser"

class Enum74(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    APPLICATION_SIGN_IN_DETAILED_SUMMARY = "applicationSignInDetailedSummary"
    CREDENTIAL_USER_REGISTRATION_DETAILS = "credentialUserRegistrationDetails"
    USER_CREDENTIAL_USAGE_DETAILS = "userCredentialUsageDetails"
    DAILY_PRINT_USAGE_SUMMARIES_BY_PRINTER = "dailyPrintUsageSummariesByPrinter"
    DAILY_PRINT_USAGE_SUMMARIES_BY_USER = "dailyPrintUsageSummariesByUser"
    MONTHLY_PRINT_USAGE_SUMMARIES_BY_PRINTER = "monthlyPrintUsageSummariesByPrinter"
    MONTHLY_PRINT_USAGE_SUMMARIES_BY_USER = "monthlyPrintUsageSummariesByUser"

class Enum75(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APPLICATION_SIGN_IN_DETAILED_SUMMARY = "applicationSignInDetailedSummary"
    CREDENTIAL_USER_REGISTRATION_DETAILS = "credentialUserRegistrationDetails"
    USER_CREDENTIAL_USAGE_DETAILS = "userCredentialUsageDetails"
    DAILY_PRINT_USAGE_SUMMARIES_BY_PRINTER = "dailyPrintUsageSummariesByPrinter"
    DAILY_PRINT_USAGE_SUMMARIES_BY_USER = "dailyPrintUsageSummariesByUser"
    MONTHLY_PRINT_USAGE_SUMMARIES_BY_PRINTER = "monthlyPrintUsageSummariesByPrinter"
    MONTHLY_PRINT_USAGE_SUMMARIES_BY_USER = "monthlyPrintUsageSummariesByUser"

class Enum76(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    APPLICATION_SIGN_IN_DETAILED_SUMMARY = "applicationSignInDetailedSummary"
    CREDENTIAL_USER_REGISTRATION_DETAILS = "credentialUserRegistrationDetails"
    USER_CREDENTIAL_USAGE_DETAILS = "userCredentialUsageDetails"
    DAILY_PRINT_USAGE_SUMMARIES_BY_PRINTER = "dailyPrintUsageSummariesByPrinter"
    DAILY_PRINT_USAGE_SUMMARIES_BY_USER = "dailyPrintUsageSummariesByUser"
    MONTHLY_PRINT_USAGE_SUMMARIES_BY_PRINTER = "monthlyPrintUsageSummariesByPrinter"
    MONTHLY_PRINT_USAGE_SUMMARIES_BY_USER = "monthlyPrintUsageSummariesByUser"

class Enum77(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"

class Enum78(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ENDPOINTS = "endpoints"

class Enum79(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    ENDPOINTS = "endpoints"

class Enum80(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ENDPOINTS = "endpoints"

class Enum81(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    ENDPOINTS = "endpoints"

class Enum82(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    URI = "uri"
    URI_DESC = "uri desc"

class Enum83(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"
    URI = "uri"

class Enum84(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"
    URI = "uri"

class Enum85(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CAPABILITIES = "capabilities"
    CAPABILITIES_DESC = "capabilities desc"
    DEFAULTS = "defaults"
    DEFAULTS_DESC = "defaults desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    IS_ACCEPTING_JOBS = "isAcceptingJobs"
    IS_ACCEPTING_JOBS_DESC = "isAcceptingJobs desc"
    LOCATION = "location"
    LOCATION_DESC = "location desc"
    MANUFACTURER = "manufacturer"
    MANUFACTURER_DESC = "manufacturer desc"
    MODEL = "model"
    MODEL_DESC = "model desc"
    NAME = "name"
    NAME_DESC = "name desc"
    STATUS = "status"
    STATUS_DESC = "status desc"
    ALLOW_ALL_USERS = "allowAllUsers"
    ALLOW_ALL_USERS_DESC = "allowAllUsers desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"

class Enum86(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CAPABILITIES = "capabilities"
    DEFAULTS = "defaults"
    DISPLAY_NAME = "displayName"
    IS_ACCEPTING_JOBS = "isAcceptingJobs"
    LOCATION = "location"
    MANUFACTURER = "manufacturer"
    MODEL = "model"
    NAME = "name"
    STATUS = "status"
    ALLOW_ALL_USERS = "allowAllUsers"
    CREATED_DATE_TIME = "createdDateTime"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    PRINTER = "printer"

class Enum87(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    PRINTER = "printer"

class Enum88(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CAPABILITIES = "capabilities"
    DEFAULTS = "defaults"
    DISPLAY_NAME = "displayName"
    IS_ACCEPTING_JOBS = "isAcceptingJobs"
    LOCATION = "location"
    MANUFACTURER = "manufacturer"
    MODEL = "model"
    NAME = "name"
    STATUS = "status"
    ALLOW_ALL_USERS = "allowAllUsers"
    CREATED_DATE_TIME = "createdDateTime"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    PRINTER = "printer"

class Enum89(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    PRINTER = "printer"

class Enum90(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"

class Enum91(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"

class Enum92(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"

class Enum93(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    IP_ADDRESS = "ipAddress"
    IP_ADDRESS_DESC = "ipAddress desc"
    USER_PRINCIPAL_NAME = "userPrincipalName"
    USER_PRINCIPAL_NAME_DESC = "userPrincipalName desc"

class Enum94(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"
    IP_ADDRESS = "ipAddress"
    USER_PRINCIPAL_NAME = "userPrincipalName"

class Enum95(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DISPLAY_NAME = "displayName"
    IP_ADDRESS = "ipAddress"
    USER_PRINCIPAL_NAME = "userPrincipalName"

class Enum96(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CAPABILITIES = "capabilities"
    DEFAULTS = "defaults"
    DISPLAY_NAME = "displayName"
    IS_ACCEPTING_JOBS = "isAcceptingJobs"
    LOCATION = "location"
    MANUFACTURER = "manufacturer"
    MODEL = "model"
    NAME = "name"
    STATUS = "status"
    ACCEPTING_JOBS = "acceptingJobs"
    IS_SHARED = "isShared"
    REGISTERED_DATE_TIME = "registeredDateTime"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    CONNECTORS = "connectors"
    SHARE = "share"
    SHARES = "shares"
    TASK_TRIGGERS = "taskTriggers"

class Enum97(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    JOBS = "jobs"
    ALLOWED_GROUPS = "allowedGroups"
    ALLOWED_USERS = "allowedUsers"
    CONNECTORS = "connectors"
    SHARE = "share"
    SHARES = "shares"
    TASK_TRIGGERS = "taskTriggers"

class Enum98(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    CREATED_BY = "createdBy"
    CREATED_BY_DESC = "createdBy desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"

class Enum99(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    CREATED_BY = "createdBy"
    DISPLAY_NAME = "displayName"
    TASKS = "tasks"

class Get0ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SETTINGS = "settings"
    CONNECTORS = "connectors"
    OPERATIONS = "operations"
    PRINTERS = "printers"
    PRINTER_SHARES = "printerShares"
    REPORTS = "reports"
    SERVICES = "services"
    SHARES = "shares"
    TASK_DEFINITIONS = "taskDefinitions"

class Get1ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    CONNECTORS = "connectors"
    OPERATIONS = "operations"
    PRINTERS = "printers"
    PRINTER_SHARES = "printerShares"
    REPORTS = "reports"
    SERVICES = "services"
    SHARES = "shares"
    TASK_DEFINITIONS = "taskDefinitions"

class Get5ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    APP_VERSION = "appVersion"
    APP_VERSION_DESC = "appVersion desc"
    DEVICE_HEALTH = "deviceHealth"
    DEVICE_HEALTH_DESC = "deviceHealth desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    FULLY_QUALIFIED_DOMAIN_NAME = "fullyQualifiedDomainName"
    FULLY_QUALIFIED_DOMAIN_NAME_DESC = "fullyQualifiedDomainName desc"
    LOCATION = "location"
    LOCATION_DESC = "location desc"
    NAME = "name"
    NAME_DESC = "name desc"
    OPERATING_SYSTEM = "operatingSystem"
    OPERATING_SYSTEM_DESC = "operatingSystem desc"
    REGISTERED_DATE_TIME = "registeredDateTime"
    REGISTERED_DATE_TIME_DESC = "registeredDateTime desc"

class Get6ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APP_VERSION = "appVersion"
    DEVICE_HEALTH = "deviceHealth"
    DISPLAY_NAME = "displayName"
    FULLY_QUALIFIED_DOMAIN_NAME = "fullyQualifiedDomainName"
    LOCATION = "location"
    NAME = "name"
    OPERATING_SYSTEM = "operatingSystem"
    REGISTERED_DATE_TIME = "registeredDateTime"

class MicrosoftGraphFeatureType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    REGISTRATION = "registration"
    RESET = "reset"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphPrintColorConfiguration(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    BLACK_AND_WHITE = "blackAndWhite"
    GRAYSCALE = "grayscale"
    COLOR = "color"
    AUTO = "auto"

class MicrosoftGraphPrintColorMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    BLACK_AND_WHITE = "blackAndWhite"
    GRAYSCALE = "grayscale"
    COLOR = "color"
    AUTO = "auto"

class MicrosoftGraphPrintDuplexConfiguration(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    TWO_SIDED_LONG_EDGE = "twoSidedLongEdge"
    TWO_SIDED_SHORT_EDGE = "twoSidedShortEdge"
    ONE_SIDED = "oneSided"

class MicrosoftGraphPrintDuplexMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    FLIP_ON_LONG_EDGE = "flipOnLongEdge"
    FLIP_ON_SHORT_EDGE = "flipOnShortEdge"
    ONE_SIDED = "oneSided"

class MicrosoftGraphPrinterFeedDirection(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    LONG_EDGE_FIRST = "longEdgeFirst"
    SHORT_EDGE_FIRST = "shortEdgeFirst"

class MicrosoftGraphPrinterFeedOrientation(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    LONG_EDGE_FIRST = "longEdgeFirst"
    SHORT_EDGE_FIRST = "shortEdgeFirst"

class MicrosoftGraphPrinterProcessingState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNKNOWN = "unknown"
    IDLE = "idle"
    PROCESSING = "processing"
    STOPPED = "stopped"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphPrinterProcessingStateDetail(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    PAUSED = "paused"
    DISCONNECTED = "disconnected"
    MEDIA_JAM = "mediaJam"
    MEDIA_NEEDED = "mediaNeeded"
    MEDIA_LOW = "mediaLow"
    MEDIA_EMPTY = "mediaEmpty"
    COVER_OPEN = "coverOpen"
    INTERLOCK_OPEN = "interlockOpen"
    QUEUE_FULL = "queueFull"
    OUTPUT_TRAY_MISSING = "outputTrayMissing"
    OUTPUT_AREA_FULL = "outputAreaFull"
    MARKER_SUPPLY_LOW = "markerSupplyLow"
    MARKER_SUPPLY_EMPTY = "markerSupplyEmpty"
    INPUT_TRAY_MISSING = "inputTrayMissing"
    OUTPUT_ALMOST_FULL = "outputAlmostFull"
    MARKER_WASTE_ALMOST_FULL = "markerWasteAlmostFull"
    MARKER_WASTE_FULL = "markerWasteFull"
    FUSER_OVER_TEMP = "fuserOverTemp"
    FUSER_UNDER_TEMP = "fuserUnderTemp"
    OTHER = "other"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphPrinterProcessingStateReason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    PAUSED = "paused"
    DISCONNECTED = "disconnected"
    MEDIA_JAM = "mediaJam"
    MEDIA_NEEDED = "mediaNeeded"
    MEDIA_LOW = "mediaLow"
    MEDIA_EMPTY = "mediaEmpty"
    COVER_OPEN = "coverOpen"
    INTERLOCK_OPEN = "interlockOpen"
    QUEUE_FULL = "queueFull"
    OUTPUT_TRAY_MISSING = "outputTrayMissing"
    OUTPUT_AREA_FULL = "outputAreaFull"
    MARKER_SUPPLY_LOW = "markerSupplyLow"
    MARKER_SUPPLY_EMPTY = "markerSupplyEmpty"
    INPUT_TRAY_MISSING = "inputTrayMissing"
    OUTPUT_ALMOST_FULL = "outputAlmostFull"
    MARKER_WASTE_ALMOST_FULL = "markerWasteAlmostFull"
    MARKER_WASTE_FULL = "markerWasteFull"
    FUSER_OVER_TEMP = "fuserOverTemp"
    FUSER_UNDER_TEMP = "fuserUnderTemp"
    OTHER = "other"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphPrintEvent(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    JOB_STARTED = "jobStarted"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphPrintFinishing(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    STAPLE = "staple"
    PUNCH = "punch"
    COVER = "cover"
    BIND = "bind"
    SADDLE_STITCH = "saddleStitch"
    STITCH_EDGE = "stitchEdge"
    STAPLE_TOP_LEFT = "stapleTopLeft"
    STAPLE_BOTTOM_LEFT = "stapleBottomLeft"
    STAPLE_TOP_RIGHT = "stapleTopRight"
    STAPLE_BOTTOM_RIGHT = "stapleBottomRight"
    STITCH_LEFT_EDGE = "stitchLeftEdge"
    STITCH_TOP_EDGE = "stitchTopEdge"
    STITCH_RIGHT_EDGE = "stitchRightEdge"
    STITCH_BOTTOM_EDGE = "stitchBottomEdge"
    STAPLE_DUAL_LEFT = "stapleDualLeft"
    STAPLE_DUAL_TOP = "stapleDualTop"
    STAPLE_DUAL_RIGHT = "stapleDualRight"
    STAPLE_DUAL_BOTTOM = "stapleDualBottom"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphPrintJobProcessingState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNKNOWN = "unknown"
    PENDING = "pending"
    PROCESSING = "processing"
    PAUSED = "paused"
    STOPPED = "stopped"
    COMPLETED = "completed"
    CANCELED = "canceled"
    ABORTED = "aborted"

class MicrosoftGraphPrintJobStateDetail(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UPLOAD_PENDING = "uploadPending"
    TRANSFORMING = "transforming"
    COMPLETED_SUCCESSFULLY = "completedSuccessfully"
    COMPLETED_WITH_WARNINGS = "completedWithWarnings"
    COMPLETED_WITH_ERRORS = "completedWithErrors"
    RELEASE_WAIT = "releaseWait"
    INTERPRETING = "interpreting"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphPrintMediaType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    STATIONERY = "stationery"
    TRANSPARENCY = "transparency"
    ENVELOPE = "envelope"
    ENVELOPE_PLAIN = "envelopePlain"
    CONTINUOUS = "continuous"
    SCREEN = "screen"
    SCREEN_PAGED = "screenPaged"
    CONTINUOUS_LONG = "continuousLong"
    CONTINUOUS_SHORT = "continuousShort"
    ENVELOPE_WINDOW = "envelopeWindow"
    MULTI_PART_FORM = "multiPartForm"
    MULTI_LAYER = "multiLayer"
    LABELS = "labels"

class MicrosoftGraphPrintMultipageLayout(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    CLOCKWISE_FROM_TOP_LEFT = "clockwiseFromTopLeft"
    COUNTERCLOCKWISE_FROM_TOP_LEFT = "counterclockwiseFromTopLeft"
    COUNTERCLOCKWISE_FROM_TOP_RIGHT = "counterclockwiseFromTopRight"
    CLOCKWISE_FROM_TOP_RIGHT = "clockwiseFromTopRight"
    COUNTERCLOCKWISE_FROM_BOTTOM_LEFT = "counterclockwiseFromBottomLeft"
    CLOCKWISE_FROM_BOTTOM_LEFT = "clockwiseFromBottomLeft"
    COUNTERCLOCKWISE_FROM_BOTTOM_RIGHT = "counterclockwiseFromBottomRight"
    CLOCKWISE_FROM_BOTTOM_RIGHT = "clockwiseFromBottomRight"

class MicrosoftGraphPrintOperationProcessingState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_STARTED = "notStarted"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphPrintOrientation(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    PORTRAIT = "portrait"
    LANDSCAPE = "landscape"
    REVERSE_LANDSCAPE = "reverseLandscape"
    REVERSE_PORTRAIT = "reversePortrait"

class MicrosoftGraphPrintPresentationDirection(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    CLOCKWISE_FROM_TOP_LEFT = "clockwiseFromTopLeft"
    COUNTER_CLOCKWISE_FROM_TOP_LEFT = "counterClockwiseFromTopLeft"
    COUNTER_CLOCKWISE_FROM_TOP_RIGHT = "counterClockwiseFromTopRight"
    CLOCKWISE_FROM_TOP_RIGHT = "clockwiseFromTopRight"
    COUNTER_CLOCKWISE_FROM_BOTTOM_LEFT = "counterClockwiseFromBottomLeft"
    CLOCKWISE_FROM_BOTTOM_LEFT = "clockwiseFromBottomLeft"
    COUNTER_CLOCKWISE_FROM_BOTTOM_RIGHT = "counterClockwiseFromBottomRight"
    CLOCKWISE_FROM_BOTTOM_RIGHT = "clockwiseFromBottomRight"

class MicrosoftGraphPrintQuality(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphPrintScaling(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    AUTO = "auto"
    SHRINK_TO_FIT = "shrinkToFit"
    FILL = "fill"
    FIT = "fit"
    NONE = "none"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphPrintTaskProcessingState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    ABORTED = "aborted"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphRegistrationAuthMethod(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    EMAIL = "email"
    MOBILE_PHONE = "mobilePhone"
    OFFICE_PHONE = "officePhone"
    SECURITY_QUESTION = "securityQuestion"
    APP_NOTIFICATION = "appNotification"
    APP_CODE = "appCode"
    ALTERNATE_MOBILE_PHONE = "alternateMobilePhone"
    FIDO = "fido"
    APP_PASSWORD = "appPassword"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

class MicrosoftGraphUsageAuthMethod(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    EMAIL = "email"
    MOBILE_SMS = "mobileSMS"
    MOBILE_CALL = "mobileCall"
    OFFICE_PHONE = "officePhone"
    SECURITY_QUESTION = "securityQuestion"
    APP_NOTIFICATION = "appNotification"
    APP_CODE = "appCode"
    ALTERNATE_MOBILE_CALL = "alternateMobileCall"
    FIDO = "fido"
    APP_PASSWORD = "appPassword"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"