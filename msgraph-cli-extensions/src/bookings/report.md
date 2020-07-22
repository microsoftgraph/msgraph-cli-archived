# Azure CLI Module Creation Report

### bookings cancel

cancel a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses.calendarView|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|cancel|cancel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--booking-appointment-id**|string|key: bookingAppointment-id of bookingAppointment|booking_appointment_id|bookingAppointment-id|
|**--cancellation-message**|string||cancellation_message|cancellationMessage|

### bookings create-appointment

create-appointment a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-appointment|CreateAppointments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--id**|string|Read-only.|id|id|
|**--self-service-appointment-id**|string||self_service_appointment_id|selfServiceAppointmentId|
|**--customer-id**|string|The id of the booking customer associated with this appointment.|customer_id|customerId|
|**--customer-name**|string||customer_name|customerName|
|**--customer-email-address**|string||customer_email_address|customerEmailAddress|
|**--customer-phone**|string||customer_phone|customerPhone|
|**--customer-notes**|string|Notes from the customer associated with this appointment.|customer_notes|customerNotes|
|**--service-id**|string|The id of the booking service associated with this appointment.|service_id|serviceId|
|**--service-name**|string|The name of the booking service associated with this appointment.|service_name|serviceName|
|**--start**|object|dateTimeTimeZone|start|start|
|**--end**|object|dateTimeTimeZone|end|end|
|**--duration**|duration||duration|duration|
|**--pre-buffer**|duration||pre_buffer|preBuffer|
|**--post-buffer**|duration||post_buffer|postBuffer|
|**--price-type**|choice||price_type|priceType|
|**--price**|number||price|price|
|**--service-notes**|string||service_notes|serviceNotes|
|**--reminders**|array||reminders|reminders|
|**--opt-out-of-customer-email**|boolean||opt_out_of_customer_email|optOutOfCustomerEmail|
|**--staff-member-ids**|array||staff_member_ids|staffMemberIds|
|**--invoice-amount**|number||invoice_amount|invoiceAmount|
|**--invoice-date**|object|dateTimeTimeZone|invoice_date|invoiceDate|
|**--invoice-id**|string||invoice_id|invoiceId|
|**--invoice-status**|choice||invoice_status|invoiceStatus|
|**--invoice-url**|string||invoice_url|invoiceUrl|
|**--service-location-display-name**|string|The name associated with the location.|display_name|displayName|
|**--service-location-location-email-address**|string|Optional email address of the location.|location_email_address|locationEmailAddress|
|**--service-location-address**|object|physicalAddress|address|address|
|**--service-location-coordinates**|object|outlookGeoCoordinates|coordinates|coordinates|
|**--service-location-location-uri**|string|Optional URI representing the location.|location_uri|locationUri|
|**--service-location-location-type**|choice||location_type|locationType|
|**--service-location-unique-id**|string|For internal use only.|unique_id|uniqueId|
|**--service-location-unique-id-type**|choice||unique_id_type|uniqueIdType|
|**--customer-location-display-name**|string|The name associated with the location.|microsoft_graph_location_display_name|displayName|
|**--customer-location-location-email-address**|string|Optional email address of the location.|microsoft_graph_location_email_address_location_email_address|locationEmailAddress|
|**--customer-location-address**|object|physicalAddress|microsoft_graph_physical_address|address|
|**--customer-location-coordinates**|object|outlookGeoCoordinates|microsoft_graph_outlook_geo_coordinates|coordinates|
|**--customer-location-location-uri**|string|Optional URI representing the location.|microsoft_graph_location_uri|locationUri|
|**--customer-location-location-type**|choice||microsoft_graph_location_type|locationType|
|**--customer-location-unique-id**|string|For internal use only.|microsoft_graph_location_unique_id|uniqueId|
|**--customer-location-unique-id-type**|choice||microsoft_graph_location_unique_id_type_unique_id_type|uniqueIdType|

### bookings create-booking-business

create-booking-business a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses.bookingBusiness|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-booking-business|CreateBookingBusiness|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|Display name of this entity.|display_name|displayName|
|**--business-type**|string||business_type|businessType|
|**--address**|object|physicalAddress|address|address|
|**--phone**|string||phone|phone|
|**--email**|string||email|email|
|**--web-site-url**|string|The URL of the business web site.|web_site_url|webSiteUrl|
|**--default-currency-iso**|string||default_currency_iso|defaultCurrencyIso|
|**--business-hours**|array||business_hours|businessHours|
|**--scheduling-policy**|object|bookingSchedulingPolicy|scheduling_policy|schedulingPolicy|
|**--is-published**|boolean||is_published|isPublished|
|**--public-url**|string||public_url|publicUrl|
|**--appointments**|array|All appointments in this business.|appointments|appointments|
|**--calendar-view**|array|A calendar view of appointments in this business.|calendar_view|calendarView|
|**--customers**|array|All customers of this business.|customers|customers|
|**--services**|array|All services offered by this business.|services|services|
|**--staff-members**|array|All staff members that provides services in this business.|staff_members|staffMembers|

### bookings create-booking-currency

create-booking-currency a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingCurrencies.bookingCurrency|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-booking-currency|CreateBookingCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--symbol**|string||symbol|symbol|

### bookings create-calendar-view

create-calendar-view a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-calendar-view|CreateCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--id**|string|Read-only.|id|id|
|**--self-service-appointment-id**|string||self_service_appointment_id|selfServiceAppointmentId|
|**--customer-id**|string|The id of the booking customer associated with this appointment.|customer_id|customerId|
|**--customer-name**|string||customer_name|customerName|
|**--customer-email-address**|string||customer_email_address|customerEmailAddress|
|**--customer-phone**|string||customer_phone|customerPhone|
|**--customer-notes**|string|Notes from the customer associated with this appointment.|customer_notes|customerNotes|
|**--service-id**|string|The id of the booking service associated with this appointment.|service_id|serviceId|
|**--service-name**|string|The name of the booking service associated with this appointment.|service_name|serviceName|
|**--start**|object|dateTimeTimeZone|start|start|
|**--end**|object|dateTimeTimeZone|end|end|
|**--duration**|duration||duration|duration|
|**--pre-buffer**|duration||pre_buffer|preBuffer|
|**--post-buffer**|duration||post_buffer|postBuffer|
|**--price-type**|choice||price_type|priceType|
|**--price**|number||price|price|
|**--service-notes**|string||service_notes|serviceNotes|
|**--reminders**|array||reminders|reminders|
|**--opt-out-of-customer-email**|boolean||opt_out_of_customer_email|optOutOfCustomerEmail|
|**--staff-member-ids**|array||staff_member_ids|staffMemberIds|
|**--invoice-amount**|number||invoice_amount|invoiceAmount|
|**--invoice-date**|object|dateTimeTimeZone|invoice_date|invoiceDate|
|**--invoice-id**|string||invoice_id|invoiceId|
|**--invoice-status**|choice||invoice_status|invoiceStatus|
|**--invoice-url**|string||invoice_url|invoiceUrl|
|**--service-location-display-name**|string|The name associated with the location.|display_name|displayName|
|**--service-location-location-email-address**|string|Optional email address of the location.|location_email_address|locationEmailAddress|
|**--service-location-address**|object|physicalAddress|address|address|
|**--service-location-coordinates**|object|outlookGeoCoordinates|coordinates|coordinates|
|**--service-location-location-uri**|string|Optional URI representing the location.|location_uri|locationUri|
|**--service-location-location-type**|choice||location_type|locationType|
|**--service-location-unique-id**|string|For internal use only.|unique_id|uniqueId|
|**--service-location-unique-id-type**|choice||unique_id_type|uniqueIdType|
|**--customer-location-display-name**|string|The name associated with the location.|microsoft_graph_location_display_name|displayName|
|**--customer-location-location-email-address**|string|Optional email address of the location.|microsoft_graph_location_email_address_location_email_address|locationEmailAddress|
|**--customer-location-address**|object|physicalAddress|microsoft_graph_physical_address|address|
|**--customer-location-coordinates**|object|outlookGeoCoordinates|microsoft_graph_outlook_geo_coordinates|coordinates|
|**--customer-location-location-uri**|string|Optional URI representing the location.|microsoft_graph_location_uri|locationUri|
|**--customer-location-location-type**|choice||microsoft_graph_location_type|locationType|
|**--customer-location-unique-id**|string|For internal use only.|microsoft_graph_location_unique_id|uniqueId|
|**--customer-location-unique-id-type**|choice||microsoft_graph_location_unique_id_type_unique_id_type|uniqueIdType|

### bookings create-customer

create-customer a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-customer|CreateCustomers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|Display name of this entity.|display_name|displayName|
|**--email-address**|string|The e-mail address of this person.|email_address|emailAddress|

### bookings create-service

create-service a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-service|CreateServices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|Display name of this entity.|display_name|displayName|
|**--default-duration**|duration||default_duration|defaultDuration|
|**--default-price**|number||default_price|defaultPrice|
|**--default-price-type**|choice||default_price_type|defaultPriceType|
|**--default-reminders**|array|The default reminders set in an appointment of this service.|default_reminders|defaultReminders|
|**--description**|string||description|description|
|**--is-hidden-from-customers**|boolean||is_hidden_from_customers|isHiddenFromCustomers|
|**--notes**|string||notes|notes|
|**--pre-buffer**|duration||pre_buffer|preBuffer|
|**--post-buffer**|duration||post_buffer|postBuffer|
|**--scheduling-policy**|object|bookingSchedulingPolicy|scheduling_policy|schedulingPolicy|
|**--staff-member-ids**|array||staff_member_ids|staffMemberIds|
|**--default-location-display-name**|string|The name associated with the location.|microsoft_graph_location_display_name|displayName|
|**--default-location-location-email-address**|string|Optional email address of the location.|location_email_address|locationEmailAddress|
|**--default-location-address**|object|physicalAddress|address|address|
|**--default-location-coordinates**|object|outlookGeoCoordinates|coordinates|coordinates|
|**--default-location-location-uri**|string|Optional URI representing the location.|location_uri|locationUri|
|**--default-location-location-type**|choice||location_type|locationType|
|**--default-location-unique-id**|string|For internal use only.|unique_id|uniqueId|
|**--default-location-unique-id-type**|choice||unique_id_type|uniqueIdType|

### bookings create-staff-member

create-staff-member a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-staff-member|CreateStaffMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|Display name of this entity.|display_name|displayName|
|**--email-address**|string|The e-mail address of this person.|email_address|emailAddress|
|**--availability-is-affected-by-personal-calendar**|boolean||availability_is_affected_by_personal_calendar|availabilityIsAffectedByPersonalCalendar|
|**--color-index**|integer||color_index|colorIndex|
|**--role**|choice||role|role|
|**--use-business-hours**|boolean||use_business_hours|useBusinessHours|
|**--working-hours**|array||working_hours|workingHours|

### bookings delete

delete a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingCurrencies.bookingCurrency|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteBookingCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-currency-id**|string|key: bookingCurrency-id of bookingCurrency|booking_currency_id|bookingCurrency-id|
|**--if-match**|string|ETag|if_match|If-Match|

### bookings get-appointment

get-appointment a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-appointment|GetAppointments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--booking-appointment-id**|string|key: bookingAppointment-id of bookingAppointment|booking_appointment_id|bookingAppointment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### bookings get-booking-business

get-booking-business a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses.bookingBusiness|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-booking-business|GetBookingBusiness|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### bookings get-booking-currency

get-booking-currency a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingCurrencies.bookingCurrency|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-booking-currency|GetBookingCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-currency-id**|string|key: bookingCurrency-id of bookingCurrency|booking_currency_id|bookingCurrency-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### bookings get-calendar-view

get-calendar-view a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-calendar-view|GetCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--booking-appointment-id**|string|key: bookingAppointment-id of bookingAppointment|booking_appointment_id|bookingAppointment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### bookings get-customer

get-customer a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-customer|GetCustomers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--booking-customer-id**|string|key: bookingCustomer-id of bookingCustomer|booking_customer_id|bookingCustomer-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### bookings get-service

get-service a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-service|GetServices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--booking-service-id**|string|key: bookingService-id of bookingService|booking_service_id|bookingService-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### bookings get-staff-member

get-staff-member a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-staff-member|GetStaffMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--booking-staff-member-id**|string|key: bookingStaffMember-id of bookingStaffMember|booking_staff_member_id|bookingStaffMember-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### bookings list-appointment

list-appointment a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-appointment|ListAppointments|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### bookings list-booking-business

list-booking-business a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses.bookingBusiness|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-booking-business|ListBookingBusiness|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### bookings list-booking-currency

list-booking-currency a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingCurrencies.bookingCurrency|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-booking-currency|ListBookingCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### bookings list-calendar-view

list-calendar-view a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-calendar-view|ListCalendarView|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### bookings list-customer

list-customer a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-customer|ListCustomers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### bookings list-service

list-service a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-service|ListServices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### bookings list-staff-member

list-staff-member a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-staff-member|ListStaffMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### bookings publish

publish a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|publish|publish|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|

### bookings unpublish

unpublish a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingBusinesses|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|unpublish|unpublish|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-business-id**|string|key: bookingBusiness-id of bookingBusiness|booking_business_id|bookingBusiness-id|

### bookings update

update a bookings.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|bookings|bookingCurrencies.bookingCurrency|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateBookingCurrency|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--booking-currency-id**|string|key: bookingCurrency-id of bookingCurrency|booking_currency_id|bookingCurrency-id|
|**--id**|string|Read-only.|id|id|
|**--symbol**|string||symbol|symbol|
