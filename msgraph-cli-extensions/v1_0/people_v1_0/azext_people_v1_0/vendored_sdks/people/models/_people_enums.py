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
    LASTMODIFIEDDATETIME = "lastModifiedDateTime"
    RESOURCEREFERENCE = "resourceReference"
    RESOURCEVISUALIZATION = "resourceVisualization"
    WEIGHT = "weight"
    RESOURCE = "resource"

class Enum11(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    RESOURCE = "resource"

class Enum12(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    IDDESC = "id desc"
    LASTUSED = "lastUsed"
    LASTUSEDDESC = "lastUsed desc"
    RESOURCEREFERENCE = "resourceReference"
    RESOURCEREFERENCEDESC = "resourceReference desc"
    RESOURCEVISUALIZATION = "resourceVisualization"
    RESOURCEVISUALIZATIONDESC = "resourceVisualization desc"

class Enum13(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    LASTUSED = "lastUsed"
    RESOURCEREFERENCE = "resourceReference"
    RESOURCEVISUALIZATION = "resourceVisualization"
    RESOURCE = "resource"

class Enum14(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    RESOURCE = "resource"

class Enum15(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    LASTUSED = "lastUsed"
    RESOURCEREFERENCE = "resourceReference"
    RESOURCEVISUALIZATION = "resourceVisualization"
    RESOURCE = "resource"

class Enum16(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    RESOURCE = "resource"

class Enum17(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    IDDESC = "id desc"
    BIRTHDAY = "birthday"
    BIRTHDAYDESC = "birthday desc"
    COMPANYNAME = "companyName"
    COMPANYNAMEDESC = "companyName desc"
    DEPARTMENT = "department"
    DEPARTMENTDESC = "department desc"
    DISPLAYNAME = "displayName"
    DISPLAYNAMEDESC = "displayName desc"
    GIVENNAME = "givenName"
    GIVENNAMEDESC = "givenName desc"
    IMADDRESS = "imAddress"
    IMADDRESSDESC = "imAddress desc"
    ISFAVORITE = "isFavorite"
    ISFAVORITEDESC = "isFavorite desc"
    JOBTITLE = "jobTitle"
    JOBTITLEDESC = "jobTitle desc"
    OFFICELOCATION = "officeLocation"
    OFFICELOCATIONDESC = "officeLocation desc"
    PERSONNOTES = "personNotes"
    PERSONNOTESDESC = "personNotes desc"
    PERSONTYPE = "personType"
    PERSONTYPEDESC = "personType desc"
    PHONES = "phones"
    PHONESDESC = "phones desc"
    POSTALADDRESSES = "postalAddresses"
    POSTALADDRESSESDESC = "postalAddresses desc"
    PROFESSION = "profession"
    PROFESSIONDESC = "profession desc"
    SCOREDEMAILADDRESSES = "scoredEmailAddresses"
    SCOREDEMAILADDRESSESDESC = "scoredEmailAddresses desc"
    SURNAME = "surname"
    SURNAMEDESC = "surname desc"
    USERPRINCIPALNAME = "userPrincipalName"
    USERPRINCIPALNAMEDESC = "userPrincipalName desc"
    WEBSITES = "websites"
    WEBSITESDESC = "websites desc"
    YOMICOMPANY = "yomiCompany"
    YOMICOMPANYDESC = "yomiCompany desc"

class Enum18(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    BIRTHDAY = "birthday"
    COMPANYNAME = "companyName"
    DEPARTMENT = "department"
    DISPLAYNAME = "displayName"
    GIVENNAME = "givenName"
    IMADDRESS = "imAddress"
    ISFAVORITE = "isFavorite"
    JOBTITLE = "jobTitle"
    OFFICELOCATION = "officeLocation"
    PERSONNOTES = "personNotes"
    PERSONTYPE = "personType"
    PHONES = "phones"
    POSTALADDRESSES = "postalAddresses"
    PROFESSION = "profession"
    SCOREDEMAILADDRESSES = "scoredEmailAddresses"
    SURNAME = "surname"
    USERPRINCIPALNAME = "userPrincipalName"
    WEBSITES = "websites"
    YOMICOMPANY = "yomiCompany"

class Enum24(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    BIRTHDAY = "birthday"
    COMPANYNAME = "companyName"
    DEPARTMENT = "department"
    DISPLAYNAME = "displayName"
    GIVENNAME = "givenName"
    IMADDRESS = "imAddress"
    ISFAVORITE = "isFavorite"
    JOBTITLE = "jobTitle"
    OFFICELOCATION = "officeLocation"
    PERSONNOTES = "personNotes"
    PERSONTYPE = "personType"
    PHONES = "phones"
    POSTALADDRESSES = "postalAddresses"
    PROFESSION = "profession"
    SCOREDEMAILADDRESSES = "scoredEmailAddresses"
    SURNAME = "surname"
    USERPRINCIPALNAME = "userPrincipalName"
    WEBSITES = "websites"
    YOMICOMPANY = "yomiCompany"

class Enum5(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    LASTSHARED = "lastShared"
    RESOURCEREFERENCE = "resourceReference"
    RESOURCEVISUALIZATION = "resourceVisualization"
    SHARINGHISTORY = "sharingHistory"
    LASTSHAREDMETHOD = "lastSharedMethod"
    RESOURCE = "resource"

class Enum7(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    IDDESC = "id desc"
    LASTMODIFIEDDATETIME = "lastModifiedDateTime"
    LASTMODIFIEDDATETIMEDESC = "lastModifiedDateTime desc"
    RESOURCEREFERENCE = "resourceReference"
    RESOURCEREFERENCEDESC = "resourceReference desc"
    RESOURCEVISUALIZATION = "resourceVisualization"
    RESOURCEVISUALIZATIONDESC = "resourceVisualization desc"
    WEIGHT = "weight"
    WEIGHTDESC = "weight desc"

class Enum8(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    LASTMODIFIEDDATETIME = "lastModifiedDateTime"
    RESOURCEREFERENCE = "resourceReference"
    RESOURCEVISUALIZATION = "resourceVisualization"
    WEIGHT = "weight"
    RESOURCE = "resource"

class Enum9(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    RESOURCE = "resource"

class Get1itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    SHARED = "shared"
    TRENDING = "trending"
    USED = "used"

class Get2itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    SHARED = "shared"
    TRENDING = "trending"
    USED = "used"

class Get3itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    LASTSHAREDMETHOD = "lastSharedMethod"
    RESOURCE = "resource"

class Get6itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    IDDESC = "id desc"
    LASTSHARED = "lastShared"
    LASTSHAREDDESC = "lastShared desc"
    RESOURCEREFERENCE = "resourceReference"
    RESOURCEREFERENCEDESC = "resourceReference desc"
    RESOURCEVISUALIZATION = "resourceVisualization"
    RESOURCEVISUALIZATIONDESC = "resourceVisualization desc"
    SHARINGHISTORY = "sharingHistory"
    SHARINGHISTORYDESC = "sharingHistory desc"

class Get7itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ID = "id"
    LASTSHARED = "lastShared"
    RESOURCEREFERENCE = "resourceReference"
    RESOURCEVISUALIZATION = "resourceVisualization"
    SHARINGHISTORY = "sharingHistory"
    LASTSHAREDMETHOD = "lastSharedMethod"
    RESOURCE = "resource"

class Get8itemsitem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ASTERISK = "*"
    LASTSHAREDMETHOD = "lastSharedMethod"
    RESOURCE = "resource"

class Microsoftgraphlocationtype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "default"
    CONFERENCEROOM = "conferenceRoom"
    HOMEADDRESS = "homeAddress"
    BUSINESSADDRESS = "businessAddress"
    GEOCOORDINATES = "geoCoordinates"
    STREETADDRESS = "streetAddress"
    HOTEL = "hotel"
    RESTAURANT = "restaurant"
    LOCALBUSINESS = "localBusiness"
    POSTALADDRESS = "postalAddress"

class Microsoftgraphlocationuniqueidtype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNKNOWN = "unknown"
    LOCATIONSTORE = "locationStore"
    DIRECTORY = "directory"
    PRIVATE = "private"
    BING = "bing"

class Microsoftgraphphonetype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    HOME = "home"
    BUSINESS = "business"
    MOBILE = "mobile"
    OTHER = "other"
    ASSISTANT = "assistant"
    HOMEFAX = "homeFax"
    BUSINESSFAX = "businessFax"
    OTHERFAX = "otherFax"
    PAGER = "pager"
    RADIO = "radio"

class Microsoftgraphselectionlikelihoodinfo(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOTSPECIFIED = "notSpecified"
    HIGH = "high"

class Microsoftgraphwebsitetype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    OTHER = "other"
    HOME = "home"
    WORK = "work"
    BLOG = "blog"
    PROFILE = "profile"
