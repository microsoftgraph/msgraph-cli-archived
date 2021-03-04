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


class Enum10(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum11(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum12(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum13(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum14(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum15(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum16(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    CONTRACT_TYPE = "contractType"
    CONTRACT_TYPE_DESC = "contractType desc"
    CUSTOMER_ID = "customerId"
    CUSTOMER_ID_DESC = "customerId desc"
    DEFAULT_DOMAIN_NAME = "defaultDomainName"
    DEFAULT_DOMAIN_NAME_DESC = "defaultDomainName desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"

class Enum17(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    CONTRACT_TYPE = "contractType"
    CUSTOMER_ID = "customerId"
    DEFAULT_DOMAIN_NAME = "defaultDomainName"
    DISPLAY_NAME = "displayName"

class Enum18(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    CONTRACT_TYPE = "contractType"
    CUSTOMER_ID = "customerId"
    DEFAULT_DOMAIN_NAME = "defaultDomainName"
    DISPLAY_NAME = "displayName"

class Enum19(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    ACCOUNT_ENABLED = "accountEnabled"
    ACCOUNT_ENABLED_DESC = "accountEnabled desc"
    ALTERNATIVE_SECURITY_IDS = "alternativeSecurityIds"
    ALTERNATIVE_SECURITY_IDS_DESC = "alternativeSecurityIds desc"
    APPROXIMATE_LAST_SIGN_IN_DATE_TIME = "approximateLastSignInDateTime"
    APPROXIMATE_LAST_SIGN_IN_DATE_TIME_DESC = "approximateLastSignInDateTime desc"
    COMPLIANCE_EXPIRATION_DATE_TIME = "complianceExpirationDateTime"
    COMPLIANCE_EXPIRATION_DATE_TIME_DESC = "complianceExpirationDateTime desc"
    DEVICE_ID = "deviceId"
    DEVICE_ID_DESC = "deviceId desc"
    DEVICE_METADATA = "deviceMetadata"
    DEVICE_METADATA_DESC = "deviceMetadata desc"
    DEVICE_VERSION = "deviceVersion"
    DEVICE_VERSION_DESC = "deviceVersion desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    IS_COMPLIANT = "isCompliant"
    IS_COMPLIANT_DESC = "isCompliant desc"
    IS_MANAGED = "isManaged"
    IS_MANAGED_DESC = "isManaged desc"
    MDM_APP_ID = "mdmAppId"
    MDM_APP_ID_DESC = "mdmAppId desc"
    ON_PREMISES_LAST_SYNC_DATE_TIME = "onPremisesLastSyncDateTime"
    ON_PREMISES_LAST_SYNC_DATE_TIME_DESC = "onPremisesLastSyncDateTime desc"
    ON_PREMISES_SYNC_ENABLED = "onPremisesSyncEnabled"
    ON_PREMISES_SYNC_ENABLED_DESC = "onPremisesSyncEnabled desc"
    OPERATING_SYSTEM = "operatingSystem"
    OPERATING_SYSTEM_DESC = "operatingSystem desc"
    OPERATING_SYSTEM_VERSION = "operatingSystemVersion"
    OPERATING_SYSTEM_VERSION_DESC = "operatingSystemVersion desc"
    PHYSICAL_IDS = "physicalIds"
    PHYSICAL_IDS_DESC = "physicalIds desc"
    PROFILE_TYPE = "profileType"
    PROFILE_TYPE_DESC = "profileType desc"
    SYSTEM_LABELS = "systemLabels"
    SYSTEM_LABELS_DESC = "systemLabels desc"
    TRUST_TYPE = "trustType"
    TRUST_TYPE_DESC = "trustType desc"

class Enum20(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    ACCOUNT_ENABLED = "accountEnabled"
    ALTERNATIVE_SECURITY_IDS = "alternativeSecurityIds"
    APPROXIMATE_LAST_SIGN_IN_DATE_TIME = "approximateLastSignInDateTime"
    COMPLIANCE_EXPIRATION_DATE_TIME = "complianceExpirationDateTime"
    DEVICE_ID = "deviceId"
    DEVICE_METADATA = "deviceMetadata"
    DEVICE_VERSION = "deviceVersion"
    DISPLAY_NAME = "displayName"
    IS_COMPLIANT = "isCompliant"
    IS_MANAGED = "isManaged"
    MDM_APP_ID = "mdmAppId"
    ON_PREMISES_LAST_SYNC_DATE_TIME = "onPremisesLastSyncDateTime"
    ON_PREMISES_SYNC_ENABLED = "onPremisesSyncEnabled"
    OPERATING_SYSTEM = "operatingSystem"
    OPERATING_SYSTEM_VERSION = "operatingSystemVersion"
    PHYSICAL_IDS = "physicalIds"
    PROFILE_TYPE = "profileType"
    SYSTEM_LABELS = "systemLabels"
    TRUST_TYPE = "trustType"
    MEMBER_OF = "memberOf"
    REGISTERED_OWNERS = "registeredOwners"
    REGISTERED_USERS = "registeredUsers"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"
    EXTENSIONS = "extensions"

class Enum21(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    MEMBER_OF = "memberOf"
    REGISTERED_OWNERS = "registeredOwners"
    REGISTERED_USERS = "registeredUsers"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"
    EXTENSIONS = "extensions"

class Enum22(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    ACCOUNT_ENABLED = "accountEnabled"
    ALTERNATIVE_SECURITY_IDS = "alternativeSecurityIds"
    APPROXIMATE_LAST_SIGN_IN_DATE_TIME = "approximateLastSignInDateTime"
    COMPLIANCE_EXPIRATION_DATE_TIME = "complianceExpirationDateTime"
    DEVICE_ID = "deviceId"
    DEVICE_METADATA = "deviceMetadata"
    DEVICE_VERSION = "deviceVersion"
    DISPLAY_NAME = "displayName"
    IS_COMPLIANT = "isCompliant"
    IS_MANAGED = "isManaged"
    MDM_APP_ID = "mdmAppId"
    ON_PREMISES_LAST_SYNC_DATE_TIME = "onPremisesLastSyncDateTime"
    ON_PREMISES_SYNC_ENABLED = "onPremisesSyncEnabled"
    OPERATING_SYSTEM = "operatingSystem"
    OPERATING_SYSTEM_VERSION = "operatingSystemVersion"
    PHYSICAL_IDS = "physicalIds"
    PROFILE_TYPE = "profileType"
    SYSTEM_LABELS = "systemLabels"
    TRUST_TYPE = "trustType"
    MEMBER_OF = "memberOf"
    REGISTERED_OWNERS = "registeredOwners"
    REGISTERED_USERS = "registeredUsers"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"
    EXTENSIONS = "extensions"

class Enum23(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    MEMBER_OF = "memberOf"
    REGISTERED_OWNERS = "registeredOwners"
    REGISTERED_USERS = "registeredUsers"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"
    EXTENSIONS = "extensions"

class Enum24(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"

class Enum25(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum26(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum27(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum28(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum29(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum30(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum31(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum32(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum33(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum34(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum35(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum36(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum38(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    ADMINISTRATIVE_UNITS = "administrativeUnits"
    DELETED_ITEMS = "deletedItems"

class Enum39(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    VISIBILITY = "visibility"
    VISIBILITY_DESC = "visibility desc"

class Enum40(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"
    VISIBILITY = "visibility"
    MEMBERS = "members"
    SCOPED_ROLE_MEMBERS = "scopedRoleMembers"
    EXTENSIONS = "extensions"

class Enum41(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    MEMBERS = "members"
    SCOPED_ROLE_MEMBERS = "scopedRoleMembers"
    EXTENSIONS = "extensions"

class Enum42(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"
    VISIBILITY = "visibility"
    MEMBERS = "members"
    SCOPED_ROLE_MEMBERS = "scopedRoleMembers"
    EXTENSIONS = "extensions"

class Enum43(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    MEMBERS = "members"
    SCOPED_ROLE_MEMBERS = "scopedRoleMembers"
    EXTENSIONS = "extensions"

class Enum44(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"

class Enum45(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum46(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum47(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum48(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    ADMINISTRATIVE_UNIT_ID = "administrativeUnitId"
    ADMINISTRATIVE_UNIT_ID_DESC = "administrativeUnitId desc"
    ROLE_ID = "roleId"
    ROLE_ID_DESC = "roleId desc"
    ROLE_MEMBER_INFO = "roleMemberInfo"
    ROLE_MEMBER_INFO_DESC = "roleMemberInfo desc"

class Enum49(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ADMINISTRATIVE_UNIT_ID = "administrativeUnitId"
    ROLE_ID = "roleId"
    ROLE_MEMBER_INFO = "roleMemberInfo"

class Enum50(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ADMINISTRATIVE_UNIT_ID = "administrativeUnitId"
    ROLE_ID = "roleId"
    ROLE_MEMBER_INFO = "roleMemberInfo"

class Enum51(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum52(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum53(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum54(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    ROLE_TEMPLATE_ID = "roleTemplateId"
    ROLE_TEMPLATE_ID_DESC = "roleTemplateId desc"

class Enum55(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"
    ROLE_TEMPLATE_ID = "roleTemplateId"
    MEMBERS = "members"
    SCOPED_MEMBERS = "scopedMembers"

class Enum56(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    MEMBERS = "members"
    SCOPED_MEMBERS = "scopedMembers"

class Enum57(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"
    ROLE_TEMPLATE_ID = "roleTemplateId"
    MEMBERS = "members"
    SCOPED_MEMBERS = "scopedMembers"

class Enum58(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    MEMBERS = "members"
    SCOPED_MEMBERS = "scopedMembers"

class Enum59(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum6(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum60(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum61(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum62(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    ADMINISTRATIVE_UNIT_ID = "administrativeUnitId"
    ADMINISTRATIVE_UNIT_ID_DESC = "administrativeUnitId desc"
    ROLE_ID = "roleId"
    ROLE_ID_DESC = "roleId desc"
    ROLE_MEMBER_INFO = "roleMemberInfo"
    ROLE_MEMBER_INFO_DESC = "roleMemberInfo desc"

class Enum63(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ADMINISTRATIVE_UNIT_ID = "administrativeUnitId"
    ROLE_ID = "roleId"
    ROLE_MEMBER_INFO = "roleMemberInfo"

class Enum64(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ADMINISTRATIVE_UNIT_ID = "administrativeUnitId"
    ROLE_ID = "roleId"
    ROLE_MEMBER_INFO = "roleMemberInfo"

class Enum65(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    DESCRIPTION = "description"
    DESCRIPTION_DESC = "description desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"

class Enum66(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"

class Enum67(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    DESCRIPTION = "description"
    DISPLAY_NAME = "displayName"

class Enum68(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    AUTHENTICATION_TYPE = "authenticationType"
    AUTHENTICATION_TYPE_DESC = "authenticationType desc"
    AVAILABILITY_STATUS = "availabilityStatus"
    AVAILABILITY_STATUS_DESC = "availabilityStatus desc"
    IS_ADMIN_MANAGED = "isAdminManaged"
    IS_ADMIN_MANAGED_DESC = "isAdminManaged desc"
    IS_DEFAULT = "isDefault"
    IS_DEFAULT_DESC = "isDefault desc"
    IS_INITIAL = "isInitial"
    IS_INITIAL_DESC = "isInitial desc"
    IS_ROOT = "isRoot"
    IS_ROOT_DESC = "isRoot desc"
    IS_VERIFIED = "isVerified"
    IS_VERIFIED_DESC = "isVerified desc"
    MANUFACTURER = "manufacturer"
    MANUFACTURER_DESC = "manufacturer desc"
    MODEL = "model"
    MODEL_DESC = "model desc"
    PASSWORD_NOTIFICATION_WINDOW_IN_DAYS = "passwordNotificationWindowInDays"
    PASSWORD_NOTIFICATION_WINDOW_IN_DAYS_DESC = "passwordNotificationWindowInDays desc"
    PASSWORD_VALIDITY_PERIOD_IN_DAYS = "passwordValidityPeriodInDays"
    PASSWORD_VALIDITY_PERIOD_IN_DAYS_DESC = "passwordValidityPeriodInDays desc"
    STATE = "state"
    STATE_DESC = "state desc"
    SUPPORTED_SERVICES = "supportedServices"
    SUPPORTED_SERVICES_DESC = "supportedServices desc"

class Enum69(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    AUTHENTICATION_TYPE = "authenticationType"
    AVAILABILITY_STATUS = "availabilityStatus"
    IS_ADMIN_MANAGED = "isAdminManaged"
    IS_DEFAULT = "isDefault"
    IS_INITIAL = "isInitial"
    IS_ROOT = "isRoot"
    IS_VERIFIED = "isVerified"
    MANUFACTURER = "manufacturer"
    MODEL = "model"
    PASSWORD_NOTIFICATION_WINDOW_IN_DAYS = "passwordNotificationWindowInDays"
    PASSWORD_VALIDITY_PERIOD_IN_DAYS = "passwordValidityPeriodInDays"
    STATE = "state"
    SUPPORTED_SERVICES = "supportedServices"
    DOMAIN_NAME_REFERENCES = "domainNameReferences"
    SERVICE_CONFIGURATION_RECORDS = "serviceConfigurationRecords"
    VERIFICATION_DNS_RECORDS = "verificationDnsRecords"

class Enum7(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum70(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    DOMAIN_NAME_REFERENCES = "domainNameReferences"
    SERVICE_CONFIGURATION_RECORDS = "serviceConfigurationRecords"
    VERIFICATION_DNS_RECORDS = "verificationDnsRecords"

class Enum71(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    AUTHENTICATION_TYPE = "authenticationType"
    AVAILABILITY_STATUS = "availabilityStatus"
    IS_ADMIN_MANAGED = "isAdminManaged"
    IS_DEFAULT = "isDefault"
    IS_INITIAL = "isInitial"
    IS_ROOT = "isRoot"
    IS_VERIFIED = "isVerified"
    MANUFACTURER = "manufacturer"
    MODEL = "model"
    PASSWORD_NOTIFICATION_WINDOW_IN_DAYS = "passwordNotificationWindowInDays"
    PASSWORD_VALIDITY_PERIOD_IN_DAYS = "passwordValidityPeriodInDays"
    STATE = "state"
    SUPPORTED_SERVICES = "supportedServices"
    DOMAIN_NAME_REFERENCES = "domainNameReferences"
    SERVICE_CONFIGURATION_RECORDS = "serviceConfigurationRecords"
    VERIFICATION_DNS_RECORDS = "verificationDnsRecords"

class Enum72(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    DOMAIN_NAME_REFERENCES = "domainNameReferences"
    SERVICE_CONFIGURATION_RECORDS = "serviceConfigurationRecords"
    VERIFICATION_DNS_RECORDS = "verificationDnsRecords"

class Enum73(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum74(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum75(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum76(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    IS_OPTIONAL = "isOptional"
    IS_OPTIONAL_DESC = "isOptional desc"
    LABEL = "label"
    LABEL_DESC = "label desc"
    RECORD_TYPE = "recordType"
    RECORD_TYPE_DESC = "recordType desc"
    SUPPORTED_SERVICE = "supportedService"
    SUPPORTED_SERVICE_DESC = "supportedService desc"
    TTL = "ttl"
    TTL_DESC = "ttl desc"

class Enum77(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    IS_OPTIONAL = "isOptional"
    LABEL = "label"
    RECORD_TYPE = "recordType"
    SUPPORTED_SERVICE = "supportedService"
    TTL = "ttl"

class Enum78(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    IS_OPTIONAL = "isOptional"
    LABEL = "label"
    RECORD_TYPE = "recordType"
    SUPPORTED_SERVICE = "supportedService"
    TTL = "ttl"

class Enum79(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    IS_OPTIONAL = "isOptional"
    IS_OPTIONAL_DESC = "isOptional desc"
    LABEL = "label"
    LABEL_DESC = "label desc"
    RECORD_TYPE = "recordType"
    RECORD_TYPE_DESC = "recordType desc"
    SUPPORTED_SERVICE = "supportedService"
    SUPPORTED_SERVICE_DESC = "supportedService desc"
    TTL = "ttl"
    TTL_DESC = "ttl desc"

class Enum8(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"

class Enum80(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    IS_OPTIONAL = "isOptional"
    LABEL = "label"
    RECORD_TYPE = "recordType"
    SUPPORTED_SERVICE = "supportedService"
    TTL = "ttl"

class Enum81(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    IS_OPTIONAL = "isOptional"
    LABEL = "label"
    RECORD_TYPE = "recordType"
    SUPPORTED_SERVICE = "supportedService"
    TTL = "ttl"

class Enum82(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    ASSIGNED_PLANS = "assignedPlans"
    ASSIGNED_PLANS_DESC = "assignedPlans desc"
    BUSINESS_PHONES = "businessPhones"
    BUSINESS_PHONES_DESC = "businessPhones desc"
    CITY = "city"
    CITY_DESC = "city desc"
    COUNTRY = "country"
    COUNTRY_DESC = "country desc"
    COUNTRY_LETTER_CODE = "countryLetterCode"
    COUNTRY_LETTER_CODE_DESC = "countryLetterCode desc"
    CREATED_DATE_TIME = "createdDateTime"
    CREATED_DATE_TIME_DESC = "createdDateTime desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    MARKETING_NOTIFICATION_EMAILS = "marketingNotificationEmails"
    MARKETING_NOTIFICATION_EMAILS_DESC = "marketingNotificationEmails desc"
    ON_PREMISES_LAST_SYNC_DATE_TIME = "onPremisesLastSyncDateTime"
    ON_PREMISES_LAST_SYNC_DATE_TIME_DESC = "onPremisesLastSyncDateTime desc"
    ON_PREMISES_SYNC_ENABLED = "onPremisesSyncEnabled"
    ON_PREMISES_SYNC_ENABLED_DESC = "onPremisesSyncEnabled desc"
    POSTAL_CODE = "postalCode"
    POSTAL_CODE_DESC = "postalCode desc"
    PREFERRED_LANGUAGE = "preferredLanguage"
    PREFERRED_LANGUAGE_DESC = "preferredLanguage desc"
    PRIVACY_PROFILE = "privacyProfile"
    PRIVACY_PROFILE_DESC = "privacyProfile desc"
    PROVISIONED_PLANS = "provisionedPlans"
    PROVISIONED_PLANS_DESC = "provisionedPlans desc"
    SECURITY_COMPLIANCE_NOTIFICATION_MAILS = "securityComplianceNotificationMails"
    SECURITY_COMPLIANCE_NOTIFICATION_MAILS_DESC = "securityComplianceNotificationMails desc"
    SECURITY_COMPLIANCE_NOTIFICATION_PHONES = "securityComplianceNotificationPhones"
    SECURITY_COMPLIANCE_NOTIFICATION_PHONES_DESC = "securityComplianceNotificationPhones desc"
    STATE = "state"
    STATE_DESC = "state desc"
    STREET = "street"
    STREET_DESC = "street desc"
    TECHNICAL_NOTIFICATION_MAILS = "technicalNotificationMails"
    TECHNICAL_NOTIFICATION_MAILS_DESC = "technicalNotificationMails desc"
    TENANT_TYPE = "tenantType"
    TENANT_TYPE_DESC = "tenantType desc"
    VERIFIED_DOMAINS = "verifiedDomains"
    VERIFIED_DOMAINS_DESC = "verifiedDomains desc"
    MOBILE_DEVICE_MANAGEMENT_AUTHORITY = "mobileDeviceManagementAuthority"
    MOBILE_DEVICE_MANAGEMENT_AUTHORITY_DESC = "mobileDeviceManagementAuthority desc"

class Enum83(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    ASSIGNED_PLANS = "assignedPlans"
    BUSINESS_PHONES = "businessPhones"
    CITY = "city"
    COUNTRY = "country"
    COUNTRY_LETTER_CODE = "countryLetterCode"
    CREATED_DATE_TIME = "createdDateTime"
    DISPLAY_NAME = "displayName"
    MARKETING_NOTIFICATION_EMAILS = "marketingNotificationEmails"
    ON_PREMISES_LAST_SYNC_DATE_TIME = "onPremisesLastSyncDateTime"
    ON_PREMISES_SYNC_ENABLED = "onPremisesSyncEnabled"
    POSTAL_CODE = "postalCode"
    PREFERRED_LANGUAGE = "preferredLanguage"
    PRIVACY_PROFILE = "privacyProfile"
    PROVISIONED_PLANS = "provisionedPlans"
    SECURITY_COMPLIANCE_NOTIFICATION_MAILS = "securityComplianceNotificationMails"
    SECURITY_COMPLIANCE_NOTIFICATION_PHONES = "securityComplianceNotificationPhones"
    STATE = "state"
    STREET = "street"
    TECHNICAL_NOTIFICATION_MAILS = "technicalNotificationMails"
    TENANT_TYPE = "tenantType"
    VERIFIED_DOMAINS = "verifiedDomains"
    MOBILE_DEVICE_MANAGEMENT_AUTHORITY = "mobileDeviceManagementAuthority"
    CERTIFICATE_BASED_AUTH_CONFIGURATION = "certificateBasedAuthConfiguration"
    EXTENSIONS = "extensions"

class Enum84(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    CERTIFICATE_BASED_AUTH_CONFIGURATION = "certificateBasedAuthConfiguration"
    EXTENSIONS = "extensions"

class Enum86(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    ASSIGNED_PLANS = "assignedPlans"
    BUSINESS_PHONES = "businessPhones"
    CITY = "city"
    COUNTRY = "country"
    COUNTRY_LETTER_CODE = "countryLetterCode"
    CREATED_DATE_TIME = "createdDateTime"
    DISPLAY_NAME = "displayName"
    MARKETING_NOTIFICATION_EMAILS = "marketingNotificationEmails"
    ON_PREMISES_LAST_SYNC_DATE_TIME = "onPremisesLastSyncDateTime"
    ON_PREMISES_SYNC_ENABLED = "onPremisesSyncEnabled"
    POSTAL_CODE = "postalCode"
    PREFERRED_LANGUAGE = "preferredLanguage"
    PRIVACY_PROFILE = "privacyProfile"
    PROVISIONED_PLANS = "provisionedPlans"
    SECURITY_COMPLIANCE_NOTIFICATION_MAILS = "securityComplianceNotificationMails"
    SECURITY_COMPLIANCE_NOTIFICATION_PHONES = "securityComplianceNotificationPhones"
    STATE = "state"
    STREET = "street"
    TECHNICAL_NOTIFICATION_MAILS = "technicalNotificationMails"
    TENANT_TYPE = "tenantType"
    VERIFIED_DOMAINS = "verifiedDomains"
    MOBILE_DEVICE_MANAGEMENT_AUTHORITY = "mobileDeviceManagementAuthority"
    CERTIFICATE_BASED_AUTH_CONFIGURATION = "certificateBasedAuthConfiguration"
    EXTENSIONS = "extensions"

class Enum87(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    CERTIFICATE_BASED_AUTH_CONFIGURATION = "certificateBasedAuthConfiguration"
    EXTENSIONS = "extensions"

class Enum88(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"

class Enum89(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    APPLIES_TO = "appliesTo"
    APPLIES_TO_DESC = "appliesTo desc"
    CAPABILITY_STATUS = "capabilityStatus"
    CAPABILITY_STATUS_DESC = "capabilityStatus desc"
    CONSUMED_UNITS = "consumedUnits"
    CONSUMED_UNITS_DESC = "consumedUnits desc"
    PREPAID_UNITS = "prepaidUnits"
    PREPAID_UNITS_DESC = "prepaidUnits desc"
    SERVICE_PLANS = "servicePlans"
    SERVICE_PLANS_DESC = "servicePlans desc"
    SKU_ID = "skuId"
    SKU_ID_DESC = "skuId desc"
    SKU_PART_NUMBER = "skuPartNumber"
    SKU_PART_NUMBER_DESC = "skuPartNumber desc"

class Enum9(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"

class Enum90(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APPLIES_TO = "appliesTo"
    CAPABILITY_STATUS = "capabilityStatus"
    CONSUMED_UNITS = "consumedUnits"
    PREPAID_UNITS = "prepaidUnits"
    SERVICE_PLANS = "servicePlans"
    SKU_ID = "skuId"
    SKU_PART_NUMBER = "skuPartNumber"

class Enum91(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    APPLIES_TO = "appliesTo"
    CAPABILITY_STATUS = "capabilityStatus"
    CONSUMED_UNITS = "consumedUnits"
    PREPAID_UNITS = "prepaidUnits"
    SERVICE_PLANS = "servicePlans"
    SKU_ID = "skuId"
    SKU_PART_NUMBER = "skuPartNumber"

class Enum92(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    ADMINISTRATIVE_UNIT_ID = "administrativeUnitId"
    ADMINISTRATIVE_UNIT_ID_DESC = "administrativeUnitId desc"
    ROLE_ID = "roleId"
    ROLE_ID_DESC = "roleId desc"
    ROLE_MEMBER_INFO = "roleMemberInfo"
    ROLE_MEMBER_INFO_DESC = "roleMemberInfo desc"

class Enum93(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ADMINISTRATIVE_UNIT_ID = "administrativeUnitId"
    ROLE_ID = "roleId"
    ROLE_MEMBER_INFO = "roleMemberInfo"

class Enum94(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ADMINISTRATIVE_UNIT_ID = "administrativeUnitId"
    ROLE_ID = "roleId"
    ROLE_MEMBER_INFO = "roleMemberInfo"

class Get0ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ADMINISTRATIVE_UNITS = "administrativeUnits"
    DELETED_ITEMS = "deletedItems"

class Get1ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    ADDRESSES = "addresses"
    COMPANY_NAME = "companyName"
    DEPARTMENT = "department"
    DISPLAY_NAME = "displayName"
    GIVEN_NAME = "givenName"
    JOB_TITLE = "jobTitle"
    MAIL = "mail"
    MAIL_NICKNAME = "mailNickname"
    ON_PREMISES_LAST_SYNC_DATE_TIME = "onPremisesLastSyncDateTime"
    ON_PREMISES_PROVISIONING_ERRORS = "onPremisesProvisioningErrors"
    ON_PREMISES_SYNC_ENABLED = "onPremisesSyncEnabled"
    PHONES = "phones"
    PROXY_ADDRESSES = "proxyAddresses"
    SURNAME = "surname"
    DIRECT_REPORTS = "directReports"
    MANAGER = "manager"
    MEMBER_OF = "memberOf"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"

class Get2ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    DIRECT_REPORTS = "directReports"
    MANAGER = "manager"
    MEMBER_OF = "memberOf"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"

class Get5ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    ID_DESC = "id desc"
    DELETED_DATE_TIME = "deletedDateTime"
    DELETED_DATE_TIME_DESC = "deletedDateTime desc"
    ADDRESSES = "addresses"
    ADDRESSES_DESC = "addresses desc"
    COMPANY_NAME = "companyName"
    COMPANY_NAME_DESC = "companyName desc"
    DEPARTMENT = "department"
    DEPARTMENT_DESC = "department desc"
    DISPLAY_NAME = "displayName"
    DISPLAY_NAME_DESC = "displayName desc"
    GIVEN_NAME = "givenName"
    GIVEN_NAME_DESC = "givenName desc"
    JOB_TITLE = "jobTitle"
    JOB_TITLE_DESC = "jobTitle desc"
    MAIL = "mail"
    MAIL_DESC = "mail desc"
    MAIL_NICKNAME = "mailNickname"
    MAIL_NICKNAME_DESC = "mailNickname desc"
    ON_PREMISES_LAST_SYNC_DATE_TIME = "onPremisesLastSyncDateTime"
    ON_PREMISES_LAST_SYNC_DATE_TIME_DESC = "onPremisesLastSyncDateTime desc"
    ON_PREMISES_PROVISIONING_ERRORS = "onPremisesProvisioningErrors"
    ON_PREMISES_PROVISIONING_ERRORS_DESC = "onPremisesProvisioningErrors desc"
    ON_PREMISES_SYNC_ENABLED = "onPremisesSyncEnabled"
    ON_PREMISES_SYNC_ENABLED_DESC = "onPremisesSyncEnabled desc"
    PHONES = "phones"
    PHONES_DESC = "phones desc"
    PROXY_ADDRESSES = "proxyAddresses"
    PROXY_ADDRESSES_DESC = "proxyAddresses desc"
    SURNAME = "surname"
    SURNAME_DESC = "surname desc"

class Get6ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    DELETED_DATE_TIME = "deletedDateTime"
    ADDRESSES = "addresses"
    COMPANY_NAME = "companyName"
    DEPARTMENT = "department"
    DISPLAY_NAME = "displayName"
    GIVEN_NAME = "givenName"
    JOB_TITLE = "jobTitle"
    MAIL = "mail"
    MAIL_NICKNAME = "mailNickname"
    ON_PREMISES_LAST_SYNC_DATE_TIME = "onPremisesLastSyncDateTime"
    ON_PREMISES_PROVISIONING_ERRORS = "onPremisesProvisioningErrors"
    ON_PREMISES_SYNC_ENABLED = "onPremisesSyncEnabled"
    PHONES = "phones"
    PROXY_ADDRESSES = "proxyAddresses"
    SURNAME = "surname"
    DIRECT_REPORTS = "directReports"
    MANAGER = "manager"
    MEMBER_OF = "memberOf"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"

class Get7ItemsItem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    DIRECT_REPORTS = "directReports"
    MANAGER = "manager"
    MEMBER_OF = "memberOf"
    TRANSITIVE_MEMBER_OF = "transitiveMemberOf"

class MicrosoftGraphMdmAuthority(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNKNOWN = "unknown"
    INTUNE = "intune"
    SCCM = "sccm"
    OFFICE365 = "office365"

class MicrosoftGraphPhoneType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    HOME = "home"
    BUSINESS = "business"
    MOBILE = "mobile"
    OTHER = "other"
    ASSISTANT = "assistant"
    HOME_FAX = "homeFax"
    BUSINESS_FAX = "businessFax"
    OTHER_FAX = "otherFax"
    PAGER = "pager"
    RADIO = "radio"
