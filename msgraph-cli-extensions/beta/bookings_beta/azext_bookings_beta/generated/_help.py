# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['bookings booking-business-booking-business'] = """
    type: group
    short-summary: bookings booking-business-booking-business
"""

helps['bookings booking-business-booking-business delete'] = """
    type: command
    short-summary: "Delete entity from bookingBusinesses"
"""

helps['bookings booking-business-booking-business create-booking-business'] = """
    type: command
    short-summary: "Add new entity to bookingBusinesses"
    parameters:
      - name: --address
        short-summary: "physicalAddress"
        long-summary: |
            Usage: --address city=XX country-or-region=XX postal-code=XX post-office-box=XX state=XX street=XX type=XX

            city: The city.
            country-or-region: The country or region. It's a free-format string value, for example, 'United States'.
            postal-code: The postal code.
            state: The state.
            street: The street.
      - name: --business-hours
        long-summary: |
            Usage: --business-hours day=XX time-slots=XX

            time-slots: A list of start/end times during a day.

            Multiple actions can be specified by using more than one --business-hours argument.
      - name: --scheduling-policy
        short-summary: "This type represents the set of policies that dictate how bookings can be created in a Booking \
Calendar."
        long-summary: |
            Usage: --scheduling-policy allow-staff-selection=XX maximum-advance=XX minimum-lead-time=XX \
send-confirmations-to-owner=XX time-slot-interval=XX

            allow-staff-selection: Allow customers to choose a specific person for the booking.
            maximum-advance: Maximum number of days in advance that a booking can be made.
            minimum-lead-time: Minimum lead time for bookings and cancellations.
            send-confirmations-to-owner: Notify the business via email when a booking is created or changed.
            time-slot-interval: Duration of each time slot.
      - name: --customers
        short-summary: "All customers of this business."
        long-summary: |
            Usage: --customers email-address=XX display-name=XX id=XX

            email-address: The e-mail address of this person.
            display-name: Display name of this entity.
            id: Read-only.

            Multiple actions can be specified by using more than one --customers argument.
"""

helps['bookings booking-business-booking-business get-booking-business'] = """
    type: command
    short-summary: "Get entity from bookingBusinesses by key"
"""

helps['bookings booking-business-booking-business list-booking-business'] = """
    type: command
    short-summary: "Get entities from bookingBusinesses"
"""

helps['bookings booking-business-booking-business update-booking-business'] = """
    type: command
    short-summary: "Update entity in bookingBusinesses"
    parameters:
      - name: --address
        short-summary: "physicalAddress"
        long-summary: |
            Usage: --address city=XX country-or-region=XX postal-code=XX post-office-box=XX state=XX street=XX type=XX

            city: The city.
            country-or-region: The country or region. It's a free-format string value, for example, 'United States'.
            postal-code: The postal code.
            state: The state.
            street: The street.
      - name: --business-hours
        long-summary: |
            Usage: --business-hours day=XX time-slots=XX

            time-slots: A list of start/end times during a day.

            Multiple actions can be specified by using more than one --business-hours argument.
      - name: --scheduling-policy
        short-summary: "This type represents the set of policies that dictate how bookings can be created in a Booking \
Calendar."
        long-summary: |
            Usage: --scheduling-policy allow-staff-selection=XX maximum-advance=XX minimum-lead-time=XX \
send-confirmations-to-owner=XX time-slot-interval=XX

            allow-staff-selection: Allow customers to choose a specific person for the booking.
            maximum-advance: Maximum number of days in advance that a booking can be made.
            minimum-lead-time: Minimum lead time for bookings and cancellations.
            send-confirmations-to-owner: Notify the business via email when a booking is created or changed.
            time-slot-interval: Duration of each time slot.
      - name: --customers
        short-summary: "All customers of this business."
        long-summary: |
            Usage: --customers email-address=XX display-name=XX id=XX

            email-address: The e-mail address of this person.
            display-name: Display name of this entity.
            id: Read-only.

            Multiple actions can be specified by using more than one --customers argument.
"""

helps['bookings booking-business'] = """
    type: group
    short-summary: bookings booking-business
"""

helps['bookings booking-business delete'] = """
    type: command
    short-summary: "Delete navigation property staffMembers for bookingBusinesses"
"""

helps['bookings booking-business create-appointment'] = """
    type: command
    short-summary: "Create new navigation property to appointments for bookingBusinesses"
    parameters:
      - name: --end
        short-summary: "dateTimeTimeZone"
        long-summary: |
            Usage: --end date-time=XX time-zone=XX

            date-time: A single point of time in a combined date and time representation ({date}T{time}; for example, \
2017-08-29T04:00:00.0000000).
            time-zone: Represents a time zone, for example, 'Pacific Standard Time'. See below for more possible \
values.
      - name: --invoice-date
        short-summary: "dateTimeTimeZone"
        long-summary: |
            Usage: --invoice-date date-time=XX time-zone=XX

            date-time: A single point of time in a combined date and time representation ({date}T{time}; for example, \
2017-08-29T04:00:00.0000000).
            time-zone: Represents a time zone, for example, 'Pacific Standard Time'. See below for more possible \
values.
      - name: --reminders
        long-summary: |
            Usage: --reminders message=XX offset=XX recipients=XX

            message: Message to send.
            offset: How much time before an appointment the reminder should be sent.

            Multiple actions can be specified by using more than one --reminders argument.
      - name: --start
        short-summary: "dateTimeTimeZone"
        long-summary: |
            Usage: --start date-time=XX time-zone=XX

            date-time: A single point of time in a combined date and time representation ({date}T{time}; for example, \
2017-08-29T04:00:00.0000000).
            time-zone: Represents a time zone, for example, 'Pacific Standard Time'. See below for more possible \
values.
      - name: --service-location-address
        short-summary: "physicalAddress"
        long-summary: |
            Usage: --service-location-address city=XX country-or-region=XX postal-code=XX post-office-box=XX state=XX \
street=XX type=XX

            city: The city.
            country-or-region: The country or region. It's a free-format string value, for example, 'United States'.
            postal-code: The postal code.
            state: The state.
            street: The street.
      - name: --service-location-coordinates
        short-summary: "outlookGeoCoordinates"
        long-summary: |
            Usage: --service-location-coordinates accuracy=XX altitude=XX altitude-accuracy=XX latitude=XX \
longitude=XX

            accuracy: The accuracy of the latitude and longitude. As an example, the accuracy can be measured in \
meters, such as the latitude and longitude are accurate to within 50 meters.
            altitude: The altitude of the location.
            altitude-accuracy: The accuracy of the altitude.
            latitude: The latitude of the location.
            longitude: The longitude of the location.
      - name: --customer-location-address
        short-summary: "physicalAddress"
        long-summary: |
            Usage: --customer-location-address city=XX country-or-region=XX postal-code=XX post-office-box=XX state=XX \
street=XX type=XX

            city: The city.
            country-or-region: The country or region. It's a free-format string value, for example, 'United States'.
            postal-code: The postal code.
            state: The state.
            street: The street.
      - name: --customer-location-coordinates
        short-summary: "outlookGeoCoordinates"
        long-summary: |
            Usage: --customer-location-coordinates accuracy=XX altitude=XX altitude-accuracy=XX latitude=XX \
longitude=XX

            accuracy: The accuracy of the latitude and longitude. As an example, the accuracy can be measured in \
meters, such as the latitude and longitude are accurate to within 50 meters.
            altitude: The altitude of the location.
            altitude-accuracy: The accuracy of the altitude.
            latitude: The latitude of the location.
            longitude: The longitude of the location.
"""

helps['bookings booking-business create-calendar-view'] = """
    type: command
    short-summary: "Create new navigation property to calendarView for bookingBusinesses"
    parameters:
      - name: --end
        short-summary: "dateTimeTimeZone"
        long-summary: |
            Usage: --end date-time=XX time-zone=XX

            date-time: A single point of time in a combined date and time representation ({date}T{time}; for example, \
2017-08-29T04:00:00.0000000).
            time-zone: Represents a time zone, for example, 'Pacific Standard Time'. See below for more possible \
values.
      - name: --invoice-date
        short-summary: "dateTimeTimeZone"
        long-summary: |
            Usage: --invoice-date date-time=XX time-zone=XX

            date-time: A single point of time in a combined date and time representation ({date}T{time}; for example, \
2017-08-29T04:00:00.0000000).
            time-zone: Represents a time zone, for example, 'Pacific Standard Time'. See below for more possible \
values.
      - name: --reminders
        long-summary: |
            Usage: --reminders message=XX offset=XX recipients=XX

            message: Message to send.
            offset: How much time before an appointment the reminder should be sent.

            Multiple actions can be specified by using more than one --reminders argument.
      - name: --start
        short-summary: "dateTimeTimeZone"
        long-summary: |
            Usage: --start date-time=XX time-zone=XX

            date-time: A single point of time in a combined date and time representation ({date}T{time}; for example, \
2017-08-29T04:00:00.0000000).
            time-zone: Represents a time zone, for example, 'Pacific Standard Time'. See below for more possible \
values.
      - name: --service-location-address
        short-summary: "physicalAddress"
        long-summary: |
            Usage: --service-location-address city=XX country-or-region=XX postal-code=XX post-office-box=XX state=XX \
street=XX type=XX

            city: The city.
            country-or-region: The country or region. It's a free-format string value, for example, 'United States'.
            postal-code: The postal code.
            state: The state.
            street: The street.
      - name: --service-location-coordinates
        short-summary: "outlookGeoCoordinates"
        long-summary: |
            Usage: --service-location-coordinates accuracy=XX altitude=XX altitude-accuracy=XX latitude=XX \
longitude=XX

            accuracy: The accuracy of the latitude and longitude. As an example, the accuracy can be measured in \
meters, such as the latitude and longitude are accurate to within 50 meters.
            altitude: The altitude of the location.
            altitude-accuracy: The accuracy of the altitude.
            latitude: The latitude of the location.
            longitude: The longitude of the location.
      - name: --customer-location-address
        short-summary: "physicalAddress"
        long-summary: |
            Usage: --customer-location-address city=XX country-or-region=XX postal-code=XX post-office-box=XX state=XX \
street=XX type=XX

            city: The city.
            country-or-region: The country or region. It's a free-format string value, for example, 'United States'.
            postal-code: The postal code.
            state: The state.
            street: The street.
      - name: --customer-location-coordinates
        short-summary: "outlookGeoCoordinates"
        long-summary: |
            Usage: --customer-location-coordinates accuracy=XX altitude=XX altitude-accuracy=XX latitude=XX \
longitude=XX

            accuracy: The accuracy of the latitude and longitude. As an example, the accuracy can be measured in \
meters, such as the latitude and longitude are accurate to within 50 meters.
            altitude: The altitude of the location.
            altitude-accuracy: The accuracy of the altitude.
            latitude: The latitude of the location.
            longitude: The longitude of the location.
"""

helps['bookings booking-business create-customer'] = """
    type: command
    short-summary: "Create new navigation property to customers for bookingBusinesses"
"""

helps['bookings booking-business create-service'] = """
    type: command
    short-summary: "Create new navigation property to services for bookingBusinesses"
    parameters:
      - name: --default-reminders
        short-summary: "The default reminders set in an appointment of this service."
        long-summary: |
            Usage: --default-reminders message=XX offset=XX recipients=XX

            message: Message to send.
            offset: How much time before an appointment the reminder should be sent.

            Multiple actions can be specified by using more than one --default-reminders argument.
      - name: --scheduling-policy
        short-summary: "This type represents the set of policies that dictate how bookings can be created in a Booking \
Calendar."
        long-summary: |
            Usage: --scheduling-policy allow-staff-selection=XX maximum-advance=XX minimum-lead-time=XX \
send-confirmations-to-owner=XX time-slot-interval=XX

            allow-staff-selection: Allow customers to choose a specific person for the booking.
            maximum-advance: Maximum number of days in advance that a booking can be made.
            minimum-lead-time: Minimum lead time for bookings and cancellations.
            send-confirmations-to-owner: Notify the business via email when a booking is created or changed.
            time-slot-interval: Duration of each time slot.
      - name: --default-location-address
        short-summary: "physicalAddress"
        long-summary: |
            Usage: --default-location-address city=XX country-or-region=XX postal-code=XX post-office-box=XX state=XX \
street=XX type=XX

            city: The city.
            country-or-region: The country or region. It's a free-format string value, for example, 'United States'.
            postal-code: The postal code.
            state: The state.
            street: The street.
      - name: --default-location-coordinates
        short-summary: "outlookGeoCoordinates"
        long-summary: |
            Usage: --default-location-coordinates accuracy=XX altitude=XX altitude-accuracy=XX latitude=XX \
longitude=XX

            accuracy: The accuracy of the latitude and longitude. As an example, the accuracy can be measured in \
meters, such as the latitude and longitude are accurate to within 50 meters.
            altitude: The altitude of the location.
            altitude-accuracy: The accuracy of the altitude.
            latitude: The latitude of the location.
            longitude: The longitude of the location.
"""

helps['bookings booking-business create-staff-member'] = """
    type: command
    short-summary: "Create new navigation property to staffMembers for bookingBusinesses"
    parameters:
      - name: --working-hours
        long-summary: |
            Usage: --working-hours day=XX time-slots=XX

            time-slots: A list of start/end times during a day.

            Multiple actions can be specified by using more than one --working-hours argument.
"""

helps['bookings booking-business get-appointment'] = """
    type: command
    short-summary: "Get appointments from bookingBusinesses"
"""

helps['bookings booking-business get-calendar-view'] = """
    type: command
    short-summary: "Get calendarView from bookingBusinesses"
"""

helps['bookings booking-business get-customer'] = """
    type: command
    short-summary: "Get customers from bookingBusinesses"
"""

helps['bookings booking-business get-service'] = """
    type: command
    short-summary: "Get services from bookingBusinesses"
"""

helps['bookings booking-business get-staff-member'] = """
    type: command
    short-summary: "Get staffMembers from bookingBusinesses"
"""

helps['bookings booking-business list-appointment'] = """
    type: command
    short-summary: "Get appointments from bookingBusinesses"
"""

helps['bookings booking-business list-calendar-view'] = """
    type: command
    short-summary: "Get calendarView from bookingBusinesses"
"""

helps['bookings booking-business list-customer'] = """
    type: command
    short-summary: "Get customers from bookingBusinesses"
"""

helps['bookings booking-business list-service'] = """
    type: command
    short-summary: "Get services from bookingBusinesses"
"""

helps['bookings booking-business list-staff-member'] = """
    type: command
    short-summary: "Get staffMembers from bookingBusinesses"
"""

helps['bookings booking-business publish'] = """
    type: command
    short-summary: "Invoke action publish"
"""

helps['bookings booking-business unpublish'] = """
    type: command
    short-summary: "Invoke action unpublish"
"""

helps['bookings booking-business update-appointment'] = """
    type: command
    short-summary: "Update the navigation property appointments in bookingBusinesses"
    parameters:
      - name: --end
        short-summary: "dateTimeTimeZone"
        long-summary: |
            Usage: --end date-time=XX time-zone=XX

            date-time: A single point of time in a combined date and time representation ({date}T{time}; for example, \
2017-08-29T04:00:00.0000000).
            time-zone: Represents a time zone, for example, 'Pacific Standard Time'. See below for more possible \
values.
      - name: --invoice-date
        short-summary: "dateTimeTimeZone"
        long-summary: |
            Usage: --invoice-date date-time=XX time-zone=XX

            date-time: A single point of time in a combined date and time representation ({date}T{time}; for example, \
2017-08-29T04:00:00.0000000).
            time-zone: Represents a time zone, for example, 'Pacific Standard Time'. See below for more possible \
values.
      - name: --reminders
        long-summary: |
            Usage: --reminders message=XX offset=XX recipients=XX

            message: Message to send.
            offset: How much time before an appointment the reminder should be sent.

            Multiple actions can be specified by using more than one --reminders argument.
      - name: --start
        short-summary: "dateTimeTimeZone"
        long-summary: |
            Usage: --start date-time=XX time-zone=XX

            date-time: A single point of time in a combined date and time representation ({date}T{time}; for example, \
2017-08-29T04:00:00.0000000).
            time-zone: Represents a time zone, for example, 'Pacific Standard Time'. See below for more possible \
values.
      - name: --service-location-address
        short-summary: "physicalAddress"
        long-summary: |
            Usage: --service-location-address city=XX country-or-region=XX postal-code=XX post-office-box=XX state=XX \
street=XX type=XX

            city: The city.
            country-or-region: The country or region. It's a free-format string value, for example, 'United States'.
            postal-code: The postal code.
            state: The state.
            street: The street.
      - name: --service-location-coordinates
        short-summary: "outlookGeoCoordinates"
        long-summary: |
            Usage: --service-location-coordinates accuracy=XX altitude=XX altitude-accuracy=XX latitude=XX \
longitude=XX

            accuracy: The accuracy of the latitude and longitude. As an example, the accuracy can be measured in \
meters, such as the latitude and longitude are accurate to within 50 meters.
            altitude: The altitude of the location.
            altitude-accuracy: The accuracy of the altitude.
            latitude: The latitude of the location.
            longitude: The longitude of the location.
      - name: --customer-location-address
        short-summary: "physicalAddress"
        long-summary: |
            Usage: --customer-location-address city=XX country-or-region=XX postal-code=XX post-office-box=XX state=XX \
street=XX type=XX

            city: The city.
            country-or-region: The country or region. It's a free-format string value, for example, 'United States'.
            postal-code: The postal code.
            state: The state.
            street: The street.
      - name: --customer-location-coordinates
        short-summary: "outlookGeoCoordinates"
        long-summary: |
            Usage: --customer-location-coordinates accuracy=XX altitude=XX altitude-accuracy=XX latitude=XX \
longitude=XX

            accuracy: The accuracy of the latitude and longitude. As an example, the accuracy can be measured in \
meters, such as the latitude and longitude are accurate to within 50 meters.
            altitude: The altitude of the location.
            altitude-accuracy: The accuracy of the altitude.
            latitude: The latitude of the location.
            longitude: The longitude of the location.
"""

helps['bookings booking-business update-calendar-view'] = """
    type: command
    short-summary: "Update the navigation property calendarView in bookingBusinesses"
    parameters:
      - name: --end
        short-summary: "dateTimeTimeZone"
        long-summary: |
            Usage: --end date-time=XX time-zone=XX

            date-time: A single point of time in a combined date and time representation ({date}T{time}; for example, \
2017-08-29T04:00:00.0000000).
            time-zone: Represents a time zone, for example, 'Pacific Standard Time'. See below for more possible \
values.
      - name: --invoice-date
        short-summary: "dateTimeTimeZone"
        long-summary: |
            Usage: --invoice-date date-time=XX time-zone=XX

            date-time: A single point of time in a combined date and time representation ({date}T{time}; for example, \
2017-08-29T04:00:00.0000000).
            time-zone: Represents a time zone, for example, 'Pacific Standard Time'. See below for more possible \
values.
      - name: --reminders
        long-summary: |
            Usage: --reminders message=XX offset=XX recipients=XX

            message: Message to send.
            offset: How much time before an appointment the reminder should be sent.

            Multiple actions can be specified by using more than one --reminders argument.
      - name: --start
        short-summary: "dateTimeTimeZone"
        long-summary: |
            Usage: --start date-time=XX time-zone=XX

            date-time: A single point of time in a combined date and time representation ({date}T{time}; for example, \
2017-08-29T04:00:00.0000000).
            time-zone: Represents a time zone, for example, 'Pacific Standard Time'. See below for more possible \
values.
      - name: --service-location-address
        short-summary: "physicalAddress"
        long-summary: |
            Usage: --service-location-address city=XX country-or-region=XX postal-code=XX post-office-box=XX state=XX \
street=XX type=XX

            city: The city.
            country-or-region: The country or region. It's a free-format string value, for example, 'United States'.
            postal-code: The postal code.
            state: The state.
            street: The street.
      - name: --service-location-coordinates
        short-summary: "outlookGeoCoordinates"
        long-summary: |
            Usage: --service-location-coordinates accuracy=XX altitude=XX altitude-accuracy=XX latitude=XX \
longitude=XX

            accuracy: The accuracy of the latitude and longitude. As an example, the accuracy can be measured in \
meters, such as the latitude and longitude are accurate to within 50 meters.
            altitude: The altitude of the location.
            altitude-accuracy: The accuracy of the altitude.
            latitude: The latitude of the location.
            longitude: The longitude of the location.
      - name: --customer-location-address
        short-summary: "physicalAddress"
        long-summary: |
            Usage: --customer-location-address city=XX country-or-region=XX postal-code=XX post-office-box=XX state=XX \
street=XX type=XX

            city: The city.
            country-or-region: The country or region. It's a free-format string value, for example, 'United States'.
            postal-code: The postal code.
            state: The state.
            street: The street.
      - name: --customer-location-coordinates
        short-summary: "outlookGeoCoordinates"
        long-summary: |
            Usage: --customer-location-coordinates accuracy=XX altitude=XX altitude-accuracy=XX latitude=XX \
longitude=XX

            accuracy: The accuracy of the latitude and longitude. As an example, the accuracy can be measured in \
meters, such as the latitude and longitude are accurate to within 50 meters.
            altitude: The altitude of the location.
            altitude-accuracy: The accuracy of the altitude.
            latitude: The latitude of the location.
            longitude: The longitude of the location.
"""

helps['bookings booking-business update-customer'] = """
    type: command
    short-summary: "Update the navigation property customers in bookingBusinesses"
"""

helps['bookings booking-business update-service'] = """
    type: command
    short-summary: "Update the navigation property services in bookingBusinesses"
    parameters:
      - name: --default-reminders
        short-summary: "The default reminders set in an appointment of this service."
        long-summary: |
            Usage: --default-reminders message=XX offset=XX recipients=XX

            message: Message to send.
            offset: How much time before an appointment the reminder should be sent.

            Multiple actions can be specified by using more than one --default-reminders argument.
      - name: --scheduling-policy
        short-summary: "This type represents the set of policies that dictate how bookings can be created in a Booking \
Calendar."
        long-summary: |
            Usage: --scheduling-policy allow-staff-selection=XX maximum-advance=XX minimum-lead-time=XX \
send-confirmations-to-owner=XX time-slot-interval=XX

            allow-staff-selection: Allow customers to choose a specific person for the booking.
            maximum-advance: Maximum number of days in advance that a booking can be made.
            minimum-lead-time: Minimum lead time for bookings and cancellations.
            send-confirmations-to-owner: Notify the business via email when a booking is created or changed.
            time-slot-interval: Duration of each time slot.
      - name: --default-location-address
        short-summary: "physicalAddress"
        long-summary: |
            Usage: --default-location-address city=XX country-or-region=XX postal-code=XX post-office-box=XX state=XX \
street=XX type=XX

            city: The city.
            country-or-region: The country or region. It's a free-format string value, for example, 'United States'.
            postal-code: The postal code.
            state: The state.
            street: The street.
      - name: --default-location-coordinates
        short-summary: "outlookGeoCoordinates"
        long-summary: |
            Usage: --default-location-coordinates accuracy=XX altitude=XX altitude-accuracy=XX latitude=XX \
longitude=XX

            accuracy: The accuracy of the latitude and longitude. As an example, the accuracy can be measured in \
meters, such as the latitude and longitude are accurate to within 50 meters.
            altitude: The altitude of the location.
            altitude-accuracy: The accuracy of the altitude.
            latitude: The latitude of the location.
            longitude: The longitude of the location.
"""

helps['bookings booking-business update-staff-member'] = """
    type: command
    short-summary: "Update the navigation property staffMembers in bookingBusinesses"
    parameters:
      - name: --working-hours
        long-summary: |
            Usage: --working-hours day=XX time-slots=XX

            time-slots: A list of start/end times during a day.

            Multiple actions can be specified by using more than one --working-hours argument.
"""

helps['bookings booking-business-appointment'] = """
    type: group
    short-summary: bookings booking-business-appointment
"""

helps['bookings booking-business-appointment cancel'] = """
    type: command
    short-summary: "Invoke action cancel"
"""

helps['bookings booking-business-calendar-view'] = """
    type: group
    short-summary: bookings booking-business-calendar-view
"""

helps['bookings booking-business-calendar-view cancel'] = """
    type: command
    short-summary: "Invoke action cancel"
"""

helps['bookings booking-currency-booking-currency'] = """
    type: group
    short-summary: bookings booking-currency-booking-currency
"""

helps['bookings booking-currency-booking-currency delete'] = """
    type: command
    short-summary: "Delete entity from bookingCurrencies"
"""

helps['bookings booking-currency-booking-currency create-booking-currency'] = """
    type: command
    short-summary: "Add new entity to bookingCurrencies"
"""

helps['bookings booking-currency-booking-currency get-booking-currency'] = """
    type: command
    short-summary: "Get entity from bookingCurrencies by key"
"""

helps['bookings booking-currency-booking-currency list-booking-currency'] = """
    type: command
    short-summary: "Get entities from bookingCurrencies"
"""

helps['bookings booking-currency-booking-currency update-booking-currency'] = """
    type: command
    short-summary: "Update entity in bookingCurrencies"
"""
