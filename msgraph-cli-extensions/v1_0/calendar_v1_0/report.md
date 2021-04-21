# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az calendar_v1_0|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az calendar_v1_0` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az calendar group|groups|[commands](#CommandsIngroups)|
|az calendar groupscalendar|groups.calendar|[commands](#CommandsIngroups.calendar)|
|az calendar groupscalendarview|groups.calendar.calendarView|[commands](#CommandsIngroups.calendar.calendarView)|
|az calendar groupscalendarevent|groups.calendar.events|[commands](#CommandsIngroups.calendar.events)|
|az calendar groupscalendarview|groups.calendarView|[commands](#CommandsIngroups.calendarView)|
|az calendar groupscalendarviewcalendar|groups.calendarView.calendar|[commands](#CommandsIngroups.calendarView.calendar)|
|az calendar groupsevent|groups.events|[commands](#CommandsIngroups.events)|
|az calendar groupseventscalendar|groups.events.calendar|[commands](#CommandsIngroups.events.calendar)|
|az calendar placesplace|places.place|[commands](#CommandsInplaces.place)|
|az calendar user|users|[commands](#CommandsInusers)|
|az calendar userscalendar|users.calendar|[commands](#CommandsInusers.calendar)|
|az calendar userscalendarview|users.calendar.calendarView|[commands](#CommandsInusers.calendar.calendarView)|
|az calendar userscalendarevent|users.calendar.events|[commands](#CommandsInusers.calendar.events)|
|az calendar userscalendargroup|users.calendarGroups|[commands](#CommandsInusers.calendarGroups)|
|az calendar userscalendargroupscalendar|users.calendarGroups.calendars|[commands](#CommandsInusers.calendarGroups.calendars)|
|az calendar userscalendargroupscalendarscalendarview|users.calendarGroups.calendars.calendarView|[commands](#CommandsInusers.calendarGroups.calendars.calendarView)|
|az calendar userscalendargroupscalendarsevent|users.calendarGroups.calendars.events|[commands](#CommandsInusers.calendarGroups.calendars.events)|
|az calendar userscalendar|users.calendars|[commands](#CommandsInusers.calendars)|
|az calendar userscalendarscalendarview|users.calendars.calendarView|[commands](#CommandsInusers.calendars.calendarView)|
|az calendar userscalendarsevent|users.calendars.events|[commands](#CommandsInusers.calendars.events)|
|az calendar userscalendarview|users.calendarView|[commands](#CommandsInusers.calendarView)|
|az calendar userscalendarviewcalendar|users.calendarView.calendar|[commands](#CommandsInusers.calendarView.calendar)|
|az calendar usersevent|users.events|[commands](#CommandsInusers.events)|
|az calendar userseventscalendar|users.events.calendar|[commands](#CommandsInusers.events.calendar)|

## COMMANDS
### <a name="CommandsIngroups">Commands in `az calendar group` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar group create-calendar-view](#groupsCreateCalendarView)|CreateCalendarView|[Parameters](#ParametersgroupsCreateCalendarView)|Not Found|
|[az calendar group create-event](#groupsCreateEvents)|CreateEvents|[Parameters](#ParametersgroupsCreateEvents)|Not Found|
|[az calendar group delete-calendar](#groupsDeleteCalendar)|DeleteCalendar|[Parameters](#ParametersgroupsDeleteCalendar)|Not Found|
|[az calendar group delete-calendar-view](#groupsDeleteCalendarView)|DeleteCalendarView|[Parameters](#ParametersgroupsDeleteCalendarView)|Not Found|
|[az calendar group delete-event](#groupsDeleteEvents)|DeleteEvents|[Parameters](#ParametersgroupsDeleteEvents)|Not Found|
|[az calendar group list-calendar-view](#groupsListCalendarView)|ListCalendarView|[Parameters](#ParametersgroupsListCalendarView)|Not Found|
|[az calendar group list-event](#groupsListEvents)|ListEvents|[Parameters](#ParametersgroupsListEvents)|Not Found|
|[az calendar group show-calendar](#groupsGetCalendar)|GetCalendar|[Parameters](#ParametersgroupsGetCalendar)|Not Found|
|[az calendar group show-calendar-view](#groupsGetCalendarView)|GetCalendarView|[Parameters](#ParametersgroupsGetCalendarView)|Not Found|
|[az calendar group show-event](#groupsGetEvents)|GetEvents|[Parameters](#ParametersgroupsGetEvents)|Not Found|
|[az calendar group update-calendar](#groupsUpdateCalendar)|UpdateCalendar|[Parameters](#ParametersgroupsUpdateCalendar)|Not Found|
|[az calendar group update-calendar-view](#groupsUpdateCalendarView)|UpdateCalendarView|[Parameters](#ParametersgroupsUpdateCalendarView)|Not Found|
|[az calendar group update-event](#groupsUpdateEvents)|UpdateEvents|[Parameters](#ParametersgroupsUpdateEvents)|Not Found|

### <a name="CommandsIngroups.calendar">Commands in `az calendar groupscalendar` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar groupscalendar create-calendar-permission](#groups.calendarCreateCalendarPermissions)|CreateCalendarPermissions|[Parameters](#Parametersgroups.calendarCreateCalendarPermissions)|Not Found|
|[az calendar groupscalendar create-calendar-view](#groups.calendarCreateCalendarView)|CreateCalendarView|[Parameters](#Parametersgroups.calendarCreateCalendarView)|Not Found|
|[az calendar groupscalendar create-event](#groups.calendarCreateEvents)|CreateEvents|[Parameters](#Parametersgroups.calendarCreateEvents)|Not Found|
|[az calendar groupscalendar create-multi-value-extended-property](#groups.calendarCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendarCreateMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendar create-single-value-extended-property](#groups.calendarCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendarCreateSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendar delete-calendar-permission](#groups.calendarDeleteCalendarPermissions)|DeleteCalendarPermissions|[Parameters](#Parametersgroups.calendarDeleteCalendarPermissions)|Not Found|
|[az calendar groupscalendar delete-calendar-view](#groups.calendarDeleteCalendarView)|DeleteCalendarView|[Parameters](#Parametersgroups.calendarDeleteCalendarView)|Not Found|
|[az calendar groupscalendar delete-event](#groups.calendarDeleteEvents)|DeleteEvents|[Parameters](#Parametersgroups.calendarDeleteEvents)|Not Found|
|[az calendar groupscalendar delete-multi-value-extended-property](#groups.calendarDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendarDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendar delete-single-value-extended-property](#groups.calendarDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendarDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendar list-calendar-permission](#groups.calendarListCalendarPermissions)|ListCalendarPermissions|[Parameters](#Parametersgroups.calendarListCalendarPermissions)|Not Found|
|[az calendar groupscalendar list-calendar-view](#groups.calendarListCalendarView)|ListCalendarView|[Parameters](#Parametersgroups.calendarListCalendarView)|Not Found|
|[az calendar groupscalendar list-event](#groups.calendarListEvents)|ListEvents|[Parameters](#Parametersgroups.calendarListEvents)|Not Found|
|[az calendar groupscalendar list-multi-value-extended-property](#groups.calendarListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendarListMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendar list-single-value-extended-property](#groups.calendarListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendarListSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendar show-calendar-permission](#groups.calendarGetCalendarPermissions)|GetCalendarPermissions|[Parameters](#Parametersgroups.calendarGetCalendarPermissions)|Not Found|
|[az calendar groupscalendar show-calendar-view](#groups.calendarGetCalendarView)|GetCalendarView|[Parameters](#Parametersgroups.calendarGetCalendarView)|Not Found|
|[az calendar groupscalendar show-event](#groups.calendarGetEvents)|GetEvents|[Parameters](#Parametersgroups.calendarGetEvents)|Not Found|
|[az calendar groupscalendar show-multi-value-extended-property](#groups.calendarGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendarGetMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendar show-single-value-extended-property](#groups.calendarGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendarGetSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendar update-calendar-permission](#groups.calendarUpdateCalendarPermissions)|UpdateCalendarPermissions|[Parameters](#Parametersgroups.calendarUpdateCalendarPermissions)|Not Found|
|[az calendar groupscalendar update-calendar-view](#groups.calendarUpdateCalendarView)|UpdateCalendarView|[Parameters](#Parametersgroups.calendarUpdateCalendarView)|Not Found|
|[az calendar groupscalendar update-event](#groups.calendarUpdateEvents)|UpdateEvents|[Parameters](#Parametersgroups.calendarUpdateEvents)|Not Found|
|[az calendar groupscalendar update-multi-value-extended-property](#groups.calendarUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendarUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendar update-single-value-extended-property](#groups.calendarUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendarUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsIngroups.calendar.events">Commands in `az calendar groupscalendarevent` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar groupscalendarevent create-attachment](#groups.calendar.eventsCreateAttachments)|CreateAttachments|[Parameters](#Parametersgroups.calendar.eventsCreateAttachments)|Not Found|
|[az calendar groupscalendarevent create-extension](#groups.calendar.eventsCreateExtensions)|CreateExtensions|[Parameters](#Parametersgroups.calendar.eventsCreateExtensions)|Not Found|
|[az calendar groupscalendarevent create-instance](#groups.calendar.eventsCreateInstances)|CreateInstances|[Parameters](#Parametersgroups.calendar.eventsCreateInstances)|Not Found|
|[az calendar groupscalendarevent create-multi-value-extended-property](#groups.calendar.eventsCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendar.eventsCreateMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarevent create-single-value-extended-property](#groups.calendar.eventsCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendar.eventsCreateSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarevent delete-attachment](#groups.calendar.eventsDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersgroups.calendar.eventsDeleteAttachments)|Not Found|
|[az calendar groupscalendarevent delete-calendar](#groups.calendar.eventsDeleteCalendar)|DeleteCalendar|[Parameters](#Parametersgroups.calendar.eventsDeleteCalendar)|Not Found|
|[az calendar groupscalendarevent delete-extension](#groups.calendar.eventsDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersgroups.calendar.eventsDeleteExtensions)|Not Found|
|[az calendar groupscalendarevent delete-instance](#groups.calendar.eventsDeleteInstances)|DeleteInstances|[Parameters](#Parametersgroups.calendar.eventsDeleteInstances)|Not Found|
|[az calendar groupscalendarevent delete-multi-value-extended-property](#groups.calendar.eventsDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendar.eventsDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarevent delete-single-value-extended-property](#groups.calendar.eventsDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendar.eventsDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarevent list-attachment](#groups.calendar.eventsListAttachments)|ListAttachments|[Parameters](#Parametersgroups.calendar.eventsListAttachments)|Not Found|
|[az calendar groupscalendarevent list-extension](#groups.calendar.eventsListExtensions)|ListExtensions|[Parameters](#Parametersgroups.calendar.eventsListExtensions)|Not Found|
|[az calendar groupscalendarevent list-instance](#groups.calendar.eventsListInstances)|ListInstances|[Parameters](#Parametersgroups.calendar.eventsListInstances)|Not Found|
|[az calendar groupscalendarevent list-multi-value-extended-property](#groups.calendar.eventsListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendar.eventsListMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarevent list-single-value-extended-property](#groups.calendar.eventsListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendar.eventsListSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarevent show-attachment](#groups.calendar.eventsGetAttachments)|GetAttachments|[Parameters](#Parametersgroups.calendar.eventsGetAttachments)|Not Found|
|[az calendar groupscalendarevent show-calendar](#groups.calendar.eventsGetCalendar)|GetCalendar|[Parameters](#Parametersgroups.calendar.eventsGetCalendar)|Not Found|
|[az calendar groupscalendarevent show-extension](#groups.calendar.eventsGetExtensions)|GetExtensions|[Parameters](#Parametersgroups.calendar.eventsGetExtensions)|Not Found|
|[az calendar groupscalendarevent show-instance](#groups.calendar.eventsGetInstances)|GetInstances|[Parameters](#Parametersgroups.calendar.eventsGetInstances)|Not Found|
|[az calendar groupscalendarevent show-multi-value-extended-property](#groups.calendar.eventsGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendar.eventsGetMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarevent show-single-value-extended-property](#groups.calendar.eventsGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendar.eventsGetSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarevent update-attachment](#groups.calendar.eventsUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersgroups.calendar.eventsUpdateAttachments)|Not Found|
|[az calendar groupscalendarevent update-calendar](#groups.calendar.eventsUpdateCalendar)|UpdateCalendar|[Parameters](#Parametersgroups.calendar.eventsUpdateCalendar)|Not Found|
|[az calendar groupscalendarevent update-extension](#groups.calendar.eventsUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersgroups.calendar.eventsUpdateExtensions)|Not Found|
|[az calendar groupscalendarevent update-instance](#groups.calendar.eventsUpdateInstances)|UpdateInstances|[Parameters](#Parametersgroups.calendar.eventsUpdateInstances)|Not Found|
|[az calendar groupscalendarevent update-multi-value-extended-property](#groups.calendar.eventsUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendar.eventsUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarevent update-single-value-extended-property](#groups.calendar.eventsUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendar.eventsUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsIngroups.calendar.calendarView">Commands in `az calendar groupscalendarview` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar groupscalendarview create-attachment](#groups.calendar.calendarViewCreateAttachments)|CreateAttachments|[Parameters](#Parametersgroups.calendar.calendarViewCreateAttachments)|Not Found|
|[az calendar groupscalendarview create-extension](#groups.calendar.calendarViewCreateExtensions)|CreateExtensions|[Parameters](#Parametersgroups.calendar.calendarViewCreateExtensions)|Not Found|
|[az calendar groupscalendarview create-instance](#groups.calendar.calendarViewCreateInstances)|CreateInstances|[Parameters](#Parametersgroups.calendar.calendarViewCreateInstances)|Not Found|
|[az calendar groupscalendarview create-multi-value-extended-property](#groups.calendar.calendarViewCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendar.calendarViewCreateMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview create-single-value-extended-property](#groups.calendar.calendarViewCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendar.calendarViewCreateSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview delete-attachment](#groups.calendar.calendarViewDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersgroups.calendar.calendarViewDeleteAttachments)|Not Found|
|[az calendar groupscalendarview delete-calendar](#groups.calendar.calendarViewDeleteCalendar)|DeleteCalendar|[Parameters](#Parametersgroups.calendar.calendarViewDeleteCalendar)|Not Found|
|[az calendar groupscalendarview delete-extension](#groups.calendar.calendarViewDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersgroups.calendar.calendarViewDeleteExtensions)|Not Found|
|[az calendar groupscalendarview delete-instance](#groups.calendar.calendarViewDeleteInstances)|DeleteInstances|[Parameters](#Parametersgroups.calendar.calendarViewDeleteInstances)|Not Found|
|[az calendar groupscalendarview delete-multi-value-extended-property](#groups.calendar.calendarViewDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendar.calendarViewDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview delete-single-value-extended-property](#groups.calendar.calendarViewDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendar.calendarViewDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview list-attachment](#groups.calendar.calendarViewListAttachments)|ListAttachments|[Parameters](#Parametersgroups.calendar.calendarViewListAttachments)|Not Found|
|[az calendar groupscalendarview list-extension](#groups.calendar.calendarViewListExtensions)|ListExtensions|[Parameters](#Parametersgroups.calendar.calendarViewListExtensions)|Not Found|
|[az calendar groupscalendarview list-instance](#groups.calendar.calendarViewListInstances)|ListInstances|[Parameters](#Parametersgroups.calendar.calendarViewListInstances)|Not Found|
|[az calendar groupscalendarview list-multi-value-extended-property](#groups.calendar.calendarViewListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendar.calendarViewListMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview list-single-value-extended-property](#groups.calendar.calendarViewListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendar.calendarViewListSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview show-attachment](#groups.calendar.calendarViewGetAttachments)|GetAttachments|[Parameters](#Parametersgroups.calendar.calendarViewGetAttachments)|Not Found|
|[az calendar groupscalendarview show-calendar](#groups.calendar.calendarViewGetCalendar)|GetCalendar|[Parameters](#Parametersgroups.calendar.calendarViewGetCalendar)|Not Found|
|[az calendar groupscalendarview show-extension](#groups.calendar.calendarViewGetExtensions)|GetExtensions|[Parameters](#Parametersgroups.calendar.calendarViewGetExtensions)|Not Found|
|[az calendar groupscalendarview show-instance](#groups.calendar.calendarViewGetInstances)|GetInstances|[Parameters](#Parametersgroups.calendar.calendarViewGetInstances)|Not Found|
|[az calendar groupscalendarview show-multi-value-extended-property](#groups.calendar.calendarViewGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendar.calendarViewGetMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview show-single-value-extended-property](#groups.calendar.calendarViewGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendar.calendarViewGetSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview update-attachment](#groups.calendar.calendarViewUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersgroups.calendar.calendarViewUpdateAttachments)|Not Found|
|[az calendar groupscalendarview update-calendar](#groups.calendar.calendarViewUpdateCalendar)|UpdateCalendar|[Parameters](#Parametersgroups.calendar.calendarViewUpdateCalendar)|Not Found|
|[az calendar groupscalendarview update-extension](#groups.calendar.calendarViewUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersgroups.calendar.calendarViewUpdateExtensions)|Not Found|
|[az calendar groupscalendarview update-instance](#groups.calendar.calendarViewUpdateInstances)|UpdateInstances|[Parameters](#Parametersgroups.calendar.calendarViewUpdateInstances)|Not Found|
|[az calendar groupscalendarview update-multi-value-extended-property](#groups.calendar.calendarViewUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendar.calendarViewUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview update-single-value-extended-property](#groups.calendar.calendarViewUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendar.calendarViewUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsIngroups.calendarView">Commands in `az calendar groupscalendarview` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar groupscalendarview create-attachment](#groups.calendarViewCreateAttachments)|CreateAttachments|[Parameters](#Parametersgroups.calendarViewCreateAttachments)|Not Found|
|[az calendar groupscalendarview create-extension](#groups.calendarViewCreateExtensions)|CreateExtensions|[Parameters](#Parametersgroups.calendarViewCreateExtensions)|Not Found|
|[az calendar groupscalendarview create-instance](#groups.calendarViewCreateInstances)|CreateInstances|[Parameters](#Parametersgroups.calendarViewCreateInstances)|Not Found|
|[az calendar groupscalendarview create-multi-value-extended-property](#groups.calendarViewCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendarViewCreateMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview create-single-value-extended-property](#groups.calendarViewCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendarViewCreateSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview delete-attachment](#groups.calendarViewDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersgroups.calendarViewDeleteAttachments)|Not Found|
|[az calendar groupscalendarview delete-calendar](#groups.calendarViewDeleteCalendar)|DeleteCalendar|[Parameters](#Parametersgroups.calendarViewDeleteCalendar)|Not Found|
|[az calendar groupscalendarview delete-extension](#groups.calendarViewDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersgroups.calendarViewDeleteExtensions)|Not Found|
|[az calendar groupscalendarview delete-instance](#groups.calendarViewDeleteInstances)|DeleteInstances|[Parameters](#Parametersgroups.calendarViewDeleteInstances)|Not Found|
|[az calendar groupscalendarview delete-multi-value-extended-property](#groups.calendarViewDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendarViewDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview delete-single-value-extended-property](#groups.calendarViewDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendarViewDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview list-attachment](#groups.calendarViewListAttachments)|ListAttachments|[Parameters](#Parametersgroups.calendarViewListAttachments)|Not Found|
|[az calendar groupscalendarview list-extension](#groups.calendarViewListExtensions)|ListExtensions|[Parameters](#Parametersgroups.calendarViewListExtensions)|Not Found|
|[az calendar groupscalendarview list-instance](#groups.calendarViewListInstances)|ListInstances|[Parameters](#Parametersgroups.calendarViewListInstances)|Not Found|
|[az calendar groupscalendarview list-multi-value-extended-property](#groups.calendarViewListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendarViewListMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview list-single-value-extended-property](#groups.calendarViewListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendarViewListSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview show-attachment](#groups.calendarViewGetAttachments)|GetAttachments|[Parameters](#Parametersgroups.calendarViewGetAttachments)|Not Found|
|[az calendar groupscalendarview show-calendar](#groups.calendarViewGetCalendar)|GetCalendar|[Parameters](#Parametersgroups.calendarViewGetCalendar)|Not Found|
|[az calendar groupscalendarview show-extension](#groups.calendarViewGetExtensions)|GetExtensions|[Parameters](#Parametersgroups.calendarViewGetExtensions)|Not Found|
|[az calendar groupscalendarview show-instance](#groups.calendarViewGetInstances)|GetInstances|[Parameters](#Parametersgroups.calendarViewGetInstances)|Not Found|
|[az calendar groupscalendarview show-multi-value-extended-property](#groups.calendarViewGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendarViewGetMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview show-single-value-extended-property](#groups.calendarViewGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendarViewGetSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview update-attachment](#groups.calendarViewUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersgroups.calendarViewUpdateAttachments)|Not Found|
|[az calendar groupscalendarview update-calendar](#groups.calendarViewUpdateCalendar)|UpdateCalendar|[Parameters](#Parametersgroups.calendarViewUpdateCalendar)|Not Found|
|[az calendar groupscalendarview update-extension](#groups.calendarViewUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersgroups.calendarViewUpdateExtensions)|Not Found|
|[az calendar groupscalendarview update-instance](#groups.calendarViewUpdateInstances)|UpdateInstances|[Parameters](#Parametersgroups.calendarViewUpdateInstances)|Not Found|
|[az calendar groupscalendarview update-multi-value-extended-property](#groups.calendarViewUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendarViewUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarview update-single-value-extended-property](#groups.calendarViewUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendarViewUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsIngroups.calendarView.calendar">Commands in `az calendar groupscalendarviewcalendar` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar groupscalendarviewcalendar create-calendar-permission](#groups.calendarView.calendarCreateCalendarPermissions)|CreateCalendarPermissions|[Parameters](#Parametersgroups.calendarView.calendarCreateCalendarPermissions)|Not Found|
|[az calendar groupscalendarviewcalendar create-calendar-view](#groups.calendarView.calendarCreateCalendarView)|CreateCalendarView|[Parameters](#Parametersgroups.calendarView.calendarCreateCalendarView)|Not Found|
|[az calendar groupscalendarviewcalendar create-event](#groups.calendarView.calendarCreateEvents)|CreateEvents|[Parameters](#Parametersgroups.calendarView.calendarCreateEvents)|Not Found|
|[az calendar groupscalendarviewcalendar create-multi-value-extended-property](#groups.calendarView.calendarCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendarView.calendarCreateMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarviewcalendar create-single-value-extended-property](#groups.calendarView.calendarCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendarView.calendarCreateSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarviewcalendar delete-calendar-permission](#groups.calendarView.calendarDeleteCalendarPermissions)|DeleteCalendarPermissions|[Parameters](#Parametersgroups.calendarView.calendarDeleteCalendarPermissions)|Not Found|
|[az calendar groupscalendarviewcalendar delete-calendar-view](#groups.calendarView.calendarDeleteCalendarView)|DeleteCalendarView|[Parameters](#Parametersgroups.calendarView.calendarDeleteCalendarView)|Not Found|
|[az calendar groupscalendarviewcalendar delete-event](#groups.calendarView.calendarDeleteEvents)|DeleteEvents|[Parameters](#Parametersgroups.calendarView.calendarDeleteEvents)|Not Found|
|[az calendar groupscalendarviewcalendar delete-multi-value-extended-property](#groups.calendarView.calendarDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendarView.calendarDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarviewcalendar delete-single-value-extended-property](#groups.calendarView.calendarDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendarView.calendarDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarviewcalendar list-calendar-permission](#groups.calendarView.calendarListCalendarPermissions)|ListCalendarPermissions|[Parameters](#Parametersgroups.calendarView.calendarListCalendarPermissions)|Not Found|
|[az calendar groupscalendarviewcalendar list-calendar-view](#groups.calendarView.calendarListCalendarView)|ListCalendarView|[Parameters](#Parametersgroups.calendarView.calendarListCalendarView)|Not Found|
|[az calendar groupscalendarviewcalendar list-event](#groups.calendarView.calendarListEvents)|ListEvents|[Parameters](#Parametersgroups.calendarView.calendarListEvents)|Not Found|
|[az calendar groupscalendarviewcalendar list-multi-value-extended-property](#groups.calendarView.calendarListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendarView.calendarListMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarviewcalendar list-single-value-extended-property](#groups.calendarView.calendarListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendarView.calendarListSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarviewcalendar show-calendar-permission](#groups.calendarView.calendarGetCalendarPermissions)|GetCalendarPermissions|[Parameters](#Parametersgroups.calendarView.calendarGetCalendarPermissions)|Not Found|
|[az calendar groupscalendarviewcalendar show-calendar-view](#groups.calendarView.calendarGetCalendarView)|GetCalendarView|[Parameters](#Parametersgroups.calendarView.calendarGetCalendarView)|Not Found|
|[az calendar groupscalendarviewcalendar show-event](#groups.calendarView.calendarGetEvents)|GetEvents|[Parameters](#Parametersgroups.calendarView.calendarGetEvents)|Not Found|
|[az calendar groupscalendarviewcalendar show-multi-value-extended-property](#groups.calendarView.calendarGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendarView.calendarGetMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarviewcalendar show-single-value-extended-property](#groups.calendarView.calendarGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendarView.calendarGetSingleValueExtendedProperties)|Not Found|
|[az calendar groupscalendarviewcalendar update-calendar-permission](#groups.calendarView.calendarUpdateCalendarPermissions)|UpdateCalendarPermissions|[Parameters](#Parametersgroups.calendarView.calendarUpdateCalendarPermissions)|Not Found|
|[az calendar groupscalendarviewcalendar update-calendar-view](#groups.calendarView.calendarUpdateCalendarView)|UpdateCalendarView|[Parameters](#Parametersgroups.calendarView.calendarUpdateCalendarView)|Not Found|
|[az calendar groupscalendarviewcalendar update-event](#groups.calendarView.calendarUpdateEvents)|UpdateEvents|[Parameters](#Parametersgroups.calendarView.calendarUpdateEvents)|Not Found|
|[az calendar groupscalendarviewcalendar update-multi-value-extended-property](#groups.calendarView.calendarUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersgroups.calendarView.calendarUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar groupscalendarviewcalendar update-single-value-extended-property](#groups.calendarView.calendarUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersgroups.calendarView.calendarUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsIngroups.events">Commands in `az calendar groupsevent` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar groupsevent create-attachment](#groups.eventsCreateAttachments)|CreateAttachments|[Parameters](#Parametersgroups.eventsCreateAttachments)|Not Found|
|[az calendar groupsevent create-extension](#groups.eventsCreateExtensions)|CreateExtensions|[Parameters](#Parametersgroups.eventsCreateExtensions)|Not Found|
|[az calendar groupsevent create-instance](#groups.eventsCreateInstances)|CreateInstances|[Parameters](#Parametersgroups.eventsCreateInstances)|Not Found|
|[az calendar groupsevent create-multi-value-extended-property](#groups.eventsCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersgroups.eventsCreateMultiValueExtendedProperties)|Not Found|
|[az calendar groupsevent create-single-value-extended-property](#groups.eventsCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersgroups.eventsCreateSingleValueExtendedProperties)|Not Found|
|[az calendar groupsevent delete-attachment](#groups.eventsDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersgroups.eventsDeleteAttachments)|Not Found|
|[az calendar groupsevent delete-calendar](#groups.eventsDeleteCalendar)|DeleteCalendar|[Parameters](#Parametersgroups.eventsDeleteCalendar)|Not Found|
|[az calendar groupsevent delete-extension](#groups.eventsDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersgroups.eventsDeleteExtensions)|Not Found|
|[az calendar groupsevent delete-instance](#groups.eventsDeleteInstances)|DeleteInstances|[Parameters](#Parametersgroups.eventsDeleteInstances)|Not Found|
|[az calendar groupsevent delete-multi-value-extended-property](#groups.eventsDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersgroups.eventsDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar groupsevent delete-single-value-extended-property](#groups.eventsDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersgroups.eventsDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar groupsevent list-attachment](#groups.eventsListAttachments)|ListAttachments|[Parameters](#Parametersgroups.eventsListAttachments)|Not Found|
|[az calendar groupsevent list-extension](#groups.eventsListExtensions)|ListExtensions|[Parameters](#Parametersgroups.eventsListExtensions)|Not Found|
|[az calendar groupsevent list-instance](#groups.eventsListInstances)|ListInstances|[Parameters](#Parametersgroups.eventsListInstances)|Not Found|
|[az calendar groupsevent list-multi-value-extended-property](#groups.eventsListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersgroups.eventsListMultiValueExtendedProperties)|Not Found|
|[az calendar groupsevent list-single-value-extended-property](#groups.eventsListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersgroups.eventsListSingleValueExtendedProperties)|Not Found|
|[az calendar groupsevent show-attachment](#groups.eventsGetAttachments)|GetAttachments|[Parameters](#Parametersgroups.eventsGetAttachments)|Not Found|
|[az calendar groupsevent show-calendar](#groups.eventsGetCalendar)|GetCalendar|[Parameters](#Parametersgroups.eventsGetCalendar)|Not Found|
|[az calendar groupsevent show-extension](#groups.eventsGetExtensions)|GetExtensions|[Parameters](#Parametersgroups.eventsGetExtensions)|Not Found|
|[az calendar groupsevent show-instance](#groups.eventsGetInstances)|GetInstances|[Parameters](#Parametersgroups.eventsGetInstances)|Not Found|
|[az calendar groupsevent show-multi-value-extended-property](#groups.eventsGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersgroups.eventsGetMultiValueExtendedProperties)|Not Found|
|[az calendar groupsevent show-single-value-extended-property](#groups.eventsGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersgroups.eventsGetSingleValueExtendedProperties)|Not Found|
|[az calendar groupsevent update-attachment](#groups.eventsUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersgroups.eventsUpdateAttachments)|Not Found|
|[az calendar groupsevent update-calendar](#groups.eventsUpdateCalendar)|UpdateCalendar|[Parameters](#Parametersgroups.eventsUpdateCalendar)|Not Found|
|[az calendar groupsevent update-extension](#groups.eventsUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersgroups.eventsUpdateExtensions)|Not Found|
|[az calendar groupsevent update-instance](#groups.eventsUpdateInstances)|UpdateInstances|[Parameters](#Parametersgroups.eventsUpdateInstances)|Not Found|
|[az calendar groupsevent update-multi-value-extended-property](#groups.eventsUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersgroups.eventsUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar groupsevent update-single-value-extended-property](#groups.eventsUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersgroups.eventsUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsIngroups.events.calendar">Commands in `az calendar groupseventscalendar` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar groupseventscalendar create-calendar-permission](#groups.events.calendarCreateCalendarPermissions)|CreateCalendarPermissions|[Parameters](#Parametersgroups.events.calendarCreateCalendarPermissions)|Not Found|
|[az calendar groupseventscalendar create-calendar-view](#groups.events.calendarCreateCalendarView)|CreateCalendarView|[Parameters](#Parametersgroups.events.calendarCreateCalendarView)|Not Found|
|[az calendar groupseventscalendar create-event](#groups.events.calendarCreateEvents)|CreateEvents|[Parameters](#Parametersgroups.events.calendarCreateEvents)|Not Found|
|[az calendar groupseventscalendar create-multi-value-extended-property](#groups.events.calendarCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersgroups.events.calendarCreateMultiValueExtendedProperties)|Not Found|
|[az calendar groupseventscalendar create-single-value-extended-property](#groups.events.calendarCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersgroups.events.calendarCreateSingleValueExtendedProperties)|Not Found|
|[az calendar groupseventscalendar delete-calendar-permission](#groups.events.calendarDeleteCalendarPermissions)|DeleteCalendarPermissions|[Parameters](#Parametersgroups.events.calendarDeleteCalendarPermissions)|Not Found|
|[az calendar groupseventscalendar delete-calendar-view](#groups.events.calendarDeleteCalendarView)|DeleteCalendarView|[Parameters](#Parametersgroups.events.calendarDeleteCalendarView)|Not Found|
|[az calendar groupseventscalendar delete-event](#groups.events.calendarDeleteEvents)|DeleteEvents|[Parameters](#Parametersgroups.events.calendarDeleteEvents)|Not Found|
|[az calendar groupseventscalendar delete-multi-value-extended-property](#groups.events.calendarDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersgroups.events.calendarDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar groupseventscalendar delete-single-value-extended-property](#groups.events.calendarDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersgroups.events.calendarDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar groupseventscalendar list-calendar-permission](#groups.events.calendarListCalendarPermissions)|ListCalendarPermissions|[Parameters](#Parametersgroups.events.calendarListCalendarPermissions)|Not Found|
|[az calendar groupseventscalendar list-calendar-view](#groups.events.calendarListCalendarView)|ListCalendarView|[Parameters](#Parametersgroups.events.calendarListCalendarView)|Not Found|
|[az calendar groupseventscalendar list-event](#groups.events.calendarListEvents)|ListEvents|[Parameters](#Parametersgroups.events.calendarListEvents)|Not Found|
|[az calendar groupseventscalendar list-multi-value-extended-property](#groups.events.calendarListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersgroups.events.calendarListMultiValueExtendedProperties)|Not Found|
|[az calendar groupseventscalendar list-single-value-extended-property](#groups.events.calendarListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersgroups.events.calendarListSingleValueExtendedProperties)|Not Found|
|[az calendar groupseventscalendar show-calendar-permission](#groups.events.calendarGetCalendarPermissions)|GetCalendarPermissions|[Parameters](#Parametersgroups.events.calendarGetCalendarPermissions)|Not Found|
|[az calendar groupseventscalendar show-calendar-view](#groups.events.calendarGetCalendarView)|GetCalendarView|[Parameters](#Parametersgroups.events.calendarGetCalendarView)|Not Found|
|[az calendar groupseventscalendar show-event](#groups.events.calendarGetEvents)|GetEvents|[Parameters](#Parametersgroups.events.calendarGetEvents)|Not Found|
|[az calendar groupseventscalendar show-multi-value-extended-property](#groups.events.calendarGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersgroups.events.calendarGetMultiValueExtendedProperties)|Not Found|
|[az calendar groupseventscalendar show-single-value-extended-property](#groups.events.calendarGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersgroups.events.calendarGetSingleValueExtendedProperties)|Not Found|
|[az calendar groupseventscalendar update-calendar-permission](#groups.events.calendarUpdateCalendarPermissions)|UpdateCalendarPermissions|[Parameters](#Parametersgroups.events.calendarUpdateCalendarPermissions)|Not Found|
|[az calendar groupseventscalendar update-calendar-view](#groups.events.calendarUpdateCalendarView)|UpdateCalendarView|[Parameters](#Parametersgroups.events.calendarUpdateCalendarView)|Not Found|
|[az calendar groupseventscalendar update-event](#groups.events.calendarUpdateEvents)|UpdateEvents|[Parameters](#Parametersgroups.events.calendarUpdateEvents)|Not Found|
|[az calendar groupseventscalendar update-multi-value-extended-property](#groups.events.calendarUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersgroups.events.calendarUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar groupseventscalendar update-single-value-extended-property](#groups.events.calendarUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersgroups.events.calendarUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInplaces.place">Commands in `az calendar placesplace` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar placesplace create-place](#places.placeCreatePlace)|CreatePlace|[Parameters](#Parametersplaces.placeCreatePlace)|Not Found|
|[az calendar placesplace delete-place](#places.placeDeletePlace)|DeletePlace|[Parameters](#Parametersplaces.placeDeletePlace)|Not Found|
|[az calendar placesplace list-place](#places.placeListPlace)|ListPlace|[Parameters](#Parametersplaces.placeListPlace)|Not Found|
|[az calendar placesplace show-place](#places.placeGetPlace)|GetPlace|[Parameters](#Parametersplaces.placeGetPlace)|Not Found|
|[az calendar placesplace update-place](#places.placeUpdatePlace)|UpdatePlace|[Parameters](#Parametersplaces.placeUpdatePlace)|Not Found|

### <a name="CommandsInusers">Commands in `az calendar user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar user create-calendar](#usersCreateCalendars)|CreateCalendars|[Parameters](#ParametersusersCreateCalendars)|Not Found|
|[az calendar user create-calendar-group](#usersCreateCalendarGroups)|CreateCalendarGroups|[Parameters](#ParametersusersCreateCalendarGroups)|Not Found|
|[az calendar user create-calendar-view](#usersCreateCalendarView)|CreateCalendarView|[Parameters](#ParametersusersCreateCalendarView)|Not Found|
|[az calendar user create-event](#usersCreateEvents)|CreateEvents|[Parameters](#ParametersusersCreateEvents)|Not Found|
|[az calendar user delete-calendar](#usersDeleteCalendars)|DeleteCalendars|[Parameters](#ParametersusersDeleteCalendars)|Not Found|
|[az calendar user delete-calendar](#usersDeleteCalendar)|DeleteCalendar|[Parameters](#ParametersusersDeleteCalendar)|Not Found|
|[az calendar user delete-calendar-group](#usersDeleteCalendarGroups)|DeleteCalendarGroups|[Parameters](#ParametersusersDeleteCalendarGroups)|Not Found|
|[az calendar user delete-calendar-view](#usersDeleteCalendarView)|DeleteCalendarView|[Parameters](#ParametersusersDeleteCalendarView)|Not Found|
|[az calendar user delete-event](#usersDeleteEvents)|DeleteEvents|[Parameters](#ParametersusersDeleteEvents)|Not Found|
|[az calendar user list-calendar](#usersListCalendars)|ListCalendars|[Parameters](#ParametersusersListCalendars)|Not Found|
|[az calendar user list-calendar-group](#usersListCalendarGroups)|ListCalendarGroups|[Parameters](#ParametersusersListCalendarGroups)|Not Found|
|[az calendar user list-calendar-view](#usersListCalendarView)|ListCalendarView|[Parameters](#ParametersusersListCalendarView)|Not Found|
|[az calendar user list-event](#usersListEvents)|ListEvents|[Parameters](#ParametersusersListEvents)|Not Found|
|[az calendar user show-calendar](#usersGetCalendars)|GetCalendars|[Parameters](#ParametersusersGetCalendars)|Not Found|
|[az calendar user show-calendar](#usersGetCalendar)|GetCalendar|[Parameters](#ParametersusersGetCalendar)|Not Found|
|[az calendar user show-calendar-group](#usersGetCalendarGroups)|GetCalendarGroups|[Parameters](#ParametersusersGetCalendarGroups)|Not Found|
|[az calendar user show-calendar-view](#usersGetCalendarView)|GetCalendarView|[Parameters](#ParametersusersGetCalendarView)|Not Found|
|[az calendar user show-event](#usersGetEvents)|GetEvents|[Parameters](#ParametersusersGetEvents)|Not Found|
|[az calendar user update-calendar](#usersUpdateCalendars)|UpdateCalendars|[Parameters](#ParametersusersUpdateCalendars)|Not Found|
|[az calendar user update-calendar](#usersUpdateCalendar)|UpdateCalendar|[Parameters](#ParametersusersUpdateCalendar)|Not Found|
|[az calendar user update-calendar-group](#usersUpdateCalendarGroups)|UpdateCalendarGroups|[Parameters](#ParametersusersUpdateCalendarGroups)|Not Found|
|[az calendar user update-calendar-view](#usersUpdateCalendarView)|UpdateCalendarView|[Parameters](#ParametersusersUpdateCalendarView)|Not Found|
|[az calendar user update-event](#usersUpdateEvents)|UpdateEvents|[Parameters](#ParametersusersUpdateEvents)|Not Found|

### <a name="CommandsInusers.calendar">Commands in `az calendar userscalendar` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar userscalendar create-calendar-permission](#users.calendarCreateCalendarPermissions)|CreateCalendarPermissions|[Parameters](#Parametersusers.calendarCreateCalendarPermissions)|Not Found|
|[az calendar userscalendar create-calendar-view](#users.calendarCreateCalendarView)|CreateCalendarView|[Parameters](#Parametersusers.calendarCreateCalendarView)|Not Found|
|[az calendar userscalendar create-event](#users.calendarCreateEvents)|CreateEvents|[Parameters](#Parametersusers.calendarCreateEvents)|Not Found|
|[az calendar userscalendar create-multi-value-extended-property](#users.calendarCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarCreateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendar create-single-value-extended-property](#users.calendarCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarCreateSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendar delete-calendar-permission](#users.calendarDeleteCalendarPermissions)|DeleteCalendarPermissions|[Parameters](#Parametersusers.calendarDeleteCalendarPermissions)|Not Found|
|[az calendar userscalendar delete-calendar-view](#users.calendarDeleteCalendarView)|DeleteCalendarView|[Parameters](#Parametersusers.calendarDeleteCalendarView)|Not Found|
|[az calendar userscalendar delete-event](#users.calendarDeleteEvents)|DeleteEvents|[Parameters](#Parametersusers.calendarDeleteEvents)|Not Found|
|[az calendar userscalendar delete-multi-value-extended-property](#users.calendarDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendar delete-single-value-extended-property](#users.calendarDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendar list-calendar-permission](#users.calendarListCalendarPermissions)|ListCalendarPermissions|[Parameters](#Parametersusers.calendarListCalendarPermissions)|Not Found|
|[az calendar userscalendar list-calendar-view](#users.calendarListCalendarView)|ListCalendarView|[Parameters](#Parametersusers.calendarListCalendarView)|Not Found|
|[az calendar userscalendar list-event](#users.calendarListEvents)|ListEvents|[Parameters](#Parametersusers.calendarListEvents)|Not Found|
|[az calendar userscalendar list-multi-value-extended-property](#users.calendarListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarListMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendar list-single-value-extended-property](#users.calendarListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarListSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendar show-calendar-permission](#users.calendarGetCalendarPermissions)|GetCalendarPermissions|[Parameters](#Parametersusers.calendarGetCalendarPermissions)|Not Found|
|[az calendar userscalendar show-calendar-view](#users.calendarGetCalendarView)|GetCalendarView|[Parameters](#Parametersusers.calendarGetCalendarView)|Not Found|
|[az calendar userscalendar show-event](#users.calendarGetEvents)|GetEvents|[Parameters](#Parametersusers.calendarGetEvents)|Not Found|
|[az calendar userscalendar show-multi-value-extended-property](#users.calendarGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGetMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendar show-single-value-extended-property](#users.calendarGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGetSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendar update-calendar-permission](#users.calendarUpdateCalendarPermissions)|UpdateCalendarPermissions|[Parameters](#Parametersusers.calendarUpdateCalendarPermissions)|Not Found|
|[az calendar userscalendar update-calendar-view](#users.calendarUpdateCalendarView)|UpdateCalendarView|[Parameters](#Parametersusers.calendarUpdateCalendarView)|Not Found|
|[az calendar userscalendar update-event](#users.calendarUpdateEvents)|UpdateEvents|[Parameters](#Parametersusers.calendarUpdateEvents)|Not Found|
|[az calendar userscalendar update-multi-value-extended-property](#users.calendarUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendar update-single-value-extended-property](#users.calendarUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.calendars">Commands in `az calendar userscalendar` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar userscalendar create-calendar-permission](#users.calendarsCreateCalendarPermissions)|CreateCalendarPermissions|[Parameters](#Parametersusers.calendarsCreateCalendarPermissions)|Not Found|
|[az calendar userscalendar create-calendar-view](#users.calendarsCreateCalendarView)|CreateCalendarView|[Parameters](#Parametersusers.calendarsCreateCalendarView)|Not Found|
|[az calendar userscalendar create-event](#users.calendarsCreateEvents)|CreateEvents|[Parameters](#Parametersusers.calendarsCreateEvents)|Not Found|
|[az calendar userscalendar create-multi-value-extended-property](#users.calendarsCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarsCreateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendar create-single-value-extended-property](#users.calendarsCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarsCreateSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendar delete-calendar-permission](#users.calendarsDeleteCalendarPermissions)|DeleteCalendarPermissions|[Parameters](#Parametersusers.calendarsDeleteCalendarPermissions)|Not Found|
|[az calendar userscalendar delete-calendar-view](#users.calendarsDeleteCalendarView)|DeleteCalendarView|[Parameters](#Parametersusers.calendarsDeleteCalendarView)|Not Found|
|[az calendar userscalendar delete-event](#users.calendarsDeleteEvents)|DeleteEvents|[Parameters](#Parametersusers.calendarsDeleteEvents)|Not Found|
|[az calendar userscalendar delete-multi-value-extended-property](#users.calendarsDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarsDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendar delete-single-value-extended-property](#users.calendarsDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarsDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendar list-calendar-permission](#users.calendarsListCalendarPermissions)|ListCalendarPermissions|[Parameters](#Parametersusers.calendarsListCalendarPermissions)|Not Found|
|[az calendar userscalendar list-calendar-view](#users.calendarsListCalendarView)|ListCalendarView|[Parameters](#Parametersusers.calendarsListCalendarView)|Not Found|
|[az calendar userscalendar list-event](#users.calendarsListEvents)|ListEvents|[Parameters](#Parametersusers.calendarsListEvents)|Not Found|
|[az calendar userscalendar list-multi-value-extended-property](#users.calendarsListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarsListMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendar list-single-value-extended-property](#users.calendarsListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarsListSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendar show-calendar-permission](#users.calendarsGetCalendarPermissions)|GetCalendarPermissions|[Parameters](#Parametersusers.calendarsGetCalendarPermissions)|Not Found|
|[az calendar userscalendar show-calendar-view](#users.calendarsGetCalendarView)|GetCalendarView|[Parameters](#Parametersusers.calendarsGetCalendarView)|Not Found|
|[az calendar userscalendar show-event](#users.calendarsGetEvents)|GetEvents|[Parameters](#Parametersusers.calendarsGetEvents)|Not Found|
|[az calendar userscalendar show-multi-value-extended-property](#users.calendarsGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarsGetMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendar show-single-value-extended-property](#users.calendarsGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarsGetSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendar update-calendar-permission](#users.calendarsUpdateCalendarPermissions)|UpdateCalendarPermissions|[Parameters](#Parametersusers.calendarsUpdateCalendarPermissions)|Not Found|
|[az calendar userscalendar update-calendar-view](#users.calendarsUpdateCalendarView)|UpdateCalendarView|[Parameters](#Parametersusers.calendarsUpdateCalendarView)|Not Found|
|[az calendar userscalendar update-event](#users.calendarsUpdateEvents)|UpdateEvents|[Parameters](#Parametersusers.calendarsUpdateEvents)|Not Found|
|[az calendar userscalendar update-multi-value-extended-property](#users.calendarsUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarsUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendar update-single-value-extended-property](#users.calendarsUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarsUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.calendar.events">Commands in `az calendar userscalendarevent` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar userscalendarevent create-attachment](#users.calendar.eventsCreateAttachments)|CreateAttachments|[Parameters](#Parametersusers.calendar.eventsCreateAttachments)|Not Found|
|[az calendar userscalendarevent create-extension](#users.calendar.eventsCreateExtensions)|CreateExtensions|[Parameters](#Parametersusers.calendar.eventsCreateExtensions)|Not Found|
|[az calendar userscalendarevent create-instance](#users.calendar.eventsCreateInstances)|CreateInstances|[Parameters](#Parametersusers.calendar.eventsCreateInstances)|Not Found|
|[az calendar userscalendarevent create-multi-value-extended-property](#users.calendar.eventsCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendar.eventsCreateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarevent create-single-value-extended-property](#users.calendar.eventsCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendar.eventsCreateSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarevent delete-attachment](#users.calendar.eventsDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersusers.calendar.eventsDeleteAttachments)|Not Found|
|[az calendar userscalendarevent delete-calendar](#users.calendar.eventsDeleteCalendar)|DeleteCalendar|[Parameters](#Parametersusers.calendar.eventsDeleteCalendar)|Not Found|
|[az calendar userscalendarevent delete-extension](#users.calendar.eventsDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersusers.calendar.eventsDeleteExtensions)|Not Found|
|[az calendar userscalendarevent delete-instance](#users.calendar.eventsDeleteInstances)|DeleteInstances|[Parameters](#Parametersusers.calendar.eventsDeleteInstances)|Not Found|
|[az calendar userscalendarevent delete-multi-value-extended-property](#users.calendar.eventsDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.calendar.eventsDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarevent delete-single-value-extended-property](#users.calendar.eventsDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.calendar.eventsDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarevent list-attachment](#users.calendar.eventsListAttachments)|ListAttachments|[Parameters](#Parametersusers.calendar.eventsListAttachments)|Not Found|
|[az calendar userscalendarevent list-extension](#users.calendar.eventsListExtensions)|ListExtensions|[Parameters](#Parametersusers.calendar.eventsListExtensions)|Not Found|
|[az calendar userscalendarevent list-instance](#users.calendar.eventsListInstances)|ListInstances|[Parameters](#Parametersusers.calendar.eventsListInstances)|Not Found|
|[az calendar userscalendarevent list-multi-value-extended-property](#users.calendar.eventsListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.calendar.eventsListMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarevent list-single-value-extended-property](#users.calendar.eventsListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.calendar.eventsListSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarevent show-attachment](#users.calendar.eventsGetAttachments)|GetAttachments|[Parameters](#Parametersusers.calendar.eventsGetAttachments)|Not Found|
|[az calendar userscalendarevent show-calendar](#users.calendar.eventsGetCalendar)|GetCalendar|[Parameters](#Parametersusers.calendar.eventsGetCalendar)|Not Found|
|[az calendar userscalendarevent show-extension](#users.calendar.eventsGetExtensions)|GetExtensions|[Parameters](#Parametersusers.calendar.eventsGetExtensions)|Not Found|
|[az calendar userscalendarevent show-instance](#users.calendar.eventsGetInstances)|GetInstances|[Parameters](#Parametersusers.calendar.eventsGetInstances)|Not Found|
|[az calendar userscalendarevent show-multi-value-extended-property](#users.calendar.eventsGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.calendar.eventsGetMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarevent show-single-value-extended-property](#users.calendar.eventsGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.calendar.eventsGetSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarevent update-attachment](#users.calendar.eventsUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersusers.calendar.eventsUpdateAttachments)|Not Found|
|[az calendar userscalendarevent update-calendar](#users.calendar.eventsUpdateCalendar)|UpdateCalendar|[Parameters](#Parametersusers.calendar.eventsUpdateCalendar)|Not Found|
|[az calendar userscalendarevent update-extension](#users.calendar.eventsUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersusers.calendar.eventsUpdateExtensions)|Not Found|
|[az calendar userscalendarevent update-instance](#users.calendar.eventsUpdateInstances)|UpdateInstances|[Parameters](#Parametersusers.calendar.eventsUpdateInstances)|Not Found|
|[az calendar userscalendarevent update-multi-value-extended-property](#users.calendar.eventsUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendar.eventsUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarevent update-single-value-extended-property](#users.calendar.eventsUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendar.eventsUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.calendarGroups">Commands in `az calendar userscalendargroup` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar userscalendargroup create-calendar](#users.calendarGroupsCreateCalendars)|CreateCalendars|[Parameters](#Parametersusers.calendarGroupsCreateCalendars)|Not Found|
|[az calendar userscalendargroup delete-calendar](#users.calendarGroupsDeleteCalendars)|DeleteCalendars|[Parameters](#Parametersusers.calendarGroupsDeleteCalendars)|Not Found|
|[az calendar userscalendargroup list-calendar](#users.calendarGroupsListCalendars)|ListCalendars|[Parameters](#Parametersusers.calendarGroupsListCalendars)|Not Found|
|[az calendar userscalendargroup show-calendar](#users.calendarGroupsGetCalendars)|GetCalendars|[Parameters](#Parametersusers.calendarGroupsGetCalendars)|Not Found|
|[az calendar userscalendargroup update-calendar](#users.calendarGroupsUpdateCalendars)|UpdateCalendars|[Parameters](#Parametersusers.calendarGroupsUpdateCalendars)|Not Found|

### <a name="CommandsInusers.calendarGroups.calendars">Commands in `az calendar userscalendargroupscalendar` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar userscalendargroupscalendar create-calendar-permission](#users.calendarGroups.calendarsCreateCalendarPermissions)|CreateCalendarPermissions|[Parameters](#Parametersusers.calendarGroups.calendarsCreateCalendarPermissions)|Not Found|
|[az calendar userscalendargroupscalendar create-calendar-view](#users.calendarGroups.calendarsCreateCalendarView)|CreateCalendarView|[Parameters](#Parametersusers.calendarGroups.calendarsCreateCalendarView)|Not Found|
|[az calendar userscalendargroupscalendar create-event](#users.calendarGroups.calendarsCreateEvents)|CreateEvents|[Parameters](#Parametersusers.calendarGroups.calendarsCreateEvents)|Not Found|
|[az calendar userscalendargroupscalendar create-multi-value-extended-property](#users.calendarGroups.calendarsCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendarsCreateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendar create-single-value-extended-property](#users.calendarGroups.calendarsCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendarsCreateSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendar delete-calendar-permission](#users.calendarGroups.calendarsDeleteCalendarPermissions)|DeleteCalendarPermissions|[Parameters](#Parametersusers.calendarGroups.calendarsDeleteCalendarPermissions)|Not Found|
|[az calendar userscalendargroupscalendar delete-calendar-view](#users.calendarGroups.calendarsDeleteCalendarView)|DeleteCalendarView|[Parameters](#Parametersusers.calendarGroups.calendarsDeleteCalendarView)|Not Found|
|[az calendar userscalendargroupscalendar delete-event](#users.calendarGroups.calendarsDeleteEvents)|DeleteEvents|[Parameters](#Parametersusers.calendarGroups.calendarsDeleteEvents)|Not Found|
|[az calendar userscalendargroupscalendar delete-multi-value-extended-property](#users.calendarGroups.calendarsDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendarsDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendar delete-single-value-extended-property](#users.calendarGroups.calendarsDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendarsDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendar list-calendar-permission](#users.calendarGroups.calendarsListCalendarPermissions)|ListCalendarPermissions|[Parameters](#Parametersusers.calendarGroups.calendarsListCalendarPermissions)|Not Found|
|[az calendar userscalendargroupscalendar list-calendar-view](#users.calendarGroups.calendarsListCalendarView)|ListCalendarView|[Parameters](#Parametersusers.calendarGroups.calendarsListCalendarView)|Not Found|
|[az calendar userscalendargroupscalendar list-event](#users.calendarGroups.calendarsListEvents)|ListEvents|[Parameters](#Parametersusers.calendarGroups.calendarsListEvents)|Not Found|
|[az calendar userscalendargroupscalendar list-multi-value-extended-property](#users.calendarGroups.calendarsListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendarsListMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendar list-single-value-extended-property](#users.calendarGroups.calendarsListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendarsListSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendar show-calendar-permission](#users.calendarGroups.calendarsGetCalendarPermissions)|GetCalendarPermissions|[Parameters](#Parametersusers.calendarGroups.calendarsGetCalendarPermissions)|Not Found|
|[az calendar userscalendargroupscalendar show-calendar-view](#users.calendarGroups.calendarsGetCalendarView)|GetCalendarView|[Parameters](#Parametersusers.calendarGroups.calendarsGetCalendarView)|Not Found|
|[az calendar userscalendargroupscalendar show-event](#users.calendarGroups.calendarsGetEvents)|GetEvents|[Parameters](#Parametersusers.calendarGroups.calendarsGetEvents)|Not Found|
|[az calendar userscalendargroupscalendar show-multi-value-extended-property](#users.calendarGroups.calendarsGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendarsGetMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendar show-single-value-extended-property](#users.calendarGroups.calendarsGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendarsGetSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendar update-calendar-permission](#users.calendarGroups.calendarsUpdateCalendarPermissions)|UpdateCalendarPermissions|[Parameters](#Parametersusers.calendarGroups.calendarsUpdateCalendarPermissions)|Not Found|
|[az calendar userscalendargroupscalendar update-calendar-view](#users.calendarGroups.calendarsUpdateCalendarView)|UpdateCalendarView|[Parameters](#Parametersusers.calendarGroups.calendarsUpdateCalendarView)|Not Found|
|[az calendar userscalendargroupscalendar update-event](#users.calendarGroups.calendarsUpdateEvents)|UpdateEvents|[Parameters](#Parametersusers.calendarGroups.calendarsUpdateEvents)|Not Found|
|[az calendar userscalendargroupscalendar update-multi-value-extended-property](#users.calendarGroups.calendarsUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendarsUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendar update-single-value-extended-property](#users.calendarGroups.calendarsUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendarsUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.calendarGroups.calendars.calendarView">Commands in `az calendar userscalendargroupscalendarscalendarview` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar userscalendargroupscalendarscalendarview create-attachment](#users.calendarGroups.calendars.calendarViewCreateAttachments)|CreateAttachments|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewCreateAttachments)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview create-extension](#users.calendarGroups.calendars.calendarViewCreateExtensions)|CreateExtensions|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewCreateExtensions)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview create-instance](#users.calendarGroups.calendars.calendarViewCreateInstances)|CreateInstances|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewCreateInstances)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview create-multi-value-extended-property](#users.calendarGroups.calendars.calendarViewCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewCreateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview create-single-value-extended-property](#users.calendarGroups.calendars.calendarViewCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewCreateSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview delete-attachment](#users.calendarGroups.calendars.calendarViewDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewDeleteAttachments)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview delete-calendar](#users.calendarGroups.calendars.calendarViewDeleteCalendar)|DeleteCalendar|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewDeleteCalendar)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview delete-extension](#users.calendarGroups.calendars.calendarViewDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewDeleteExtensions)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview delete-instance](#users.calendarGroups.calendars.calendarViewDeleteInstances)|DeleteInstances|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewDeleteInstances)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview delete-multi-value-extended-property](#users.calendarGroups.calendars.calendarViewDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview delete-single-value-extended-property](#users.calendarGroups.calendars.calendarViewDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview list-attachment](#users.calendarGroups.calendars.calendarViewListAttachments)|ListAttachments|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewListAttachments)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview list-extension](#users.calendarGroups.calendars.calendarViewListExtensions)|ListExtensions|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewListExtensions)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview list-instance](#users.calendarGroups.calendars.calendarViewListInstances)|ListInstances|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewListInstances)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview list-multi-value-extended-property](#users.calendarGroups.calendars.calendarViewListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewListMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview list-single-value-extended-property](#users.calendarGroups.calendars.calendarViewListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewListSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview show-attachment](#users.calendarGroups.calendars.calendarViewGetAttachments)|GetAttachments|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewGetAttachments)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview show-calendar](#users.calendarGroups.calendars.calendarViewGetCalendar)|GetCalendar|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewGetCalendar)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview show-extension](#users.calendarGroups.calendars.calendarViewGetExtensions)|GetExtensions|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewGetExtensions)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview show-instance](#users.calendarGroups.calendars.calendarViewGetInstances)|GetInstances|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewGetInstances)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview show-multi-value-extended-property](#users.calendarGroups.calendars.calendarViewGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewGetMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview show-single-value-extended-property](#users.calendarGroups.calendars.calendarViewGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewGetSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview update-attachment](#users.calendarGroups.calendars.calendarViewUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewUpdateAttachments)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview update-calendar](#users.calendarGroups.calendars.calendarViewUpdateCalendar)|UpdateCalendar|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewUpdateCalendar)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview update-extension](#users.calendarGroups.calendars.calendarViewUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewUpdateExtensions)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview update-instance](#users.calendarGroups.calendars.calendarViewUpdateInstances)|UpdateInstances|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewUpdateInstances)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview update-multi-value-extended-property](#users.calendarGroups.calendars.calendarViewUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarscalendarview update-single-value-extended-property](#users.calendarGroups.calendars.calendarViewUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.calendarViewUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.calendarGroups.calendars.events">Commands in `az calendar userscalendargroupscalendarsevent` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar userscalendargroupscalendarsevent create-attachment](#users.calendarGroups.calendars.eventsCreateAttachments)|CreateAttachments|[Parameters](#Parametersusers.calendarGroups.calendars.eventsCreateAttachments)|Not Found|
|[az calendar userscalendargroupscalendarsevent create-extension](#users.calendarGroups.calendars.eventsCreateExtensions)|CreateExtensions|[Parameters](#Parametersusers.calendarGroups.calendars.eventsCreateExtensions)|Not Found|
|[az calendar userscalendargroupscalendarsevent create-instance](#users.calendarGroups.calendars.eventsCreateInstances)|CreateInstances|[Parameters](#Parametersusers.calendarGroups.calendars.eventsCreateInstances)|Not Found|
|[az calendar userscalendargroupscalendarsevent create-multi-value-extended-property](#users.calendarGroups.calendars.eventsCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.eventsCreateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarsevent create-single-value-extended-property](#users.calendarGroups.calendars.eventsCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.eventsCreateSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarsevent delete-attachment](#users.calendarGroups.calendars.eventsDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersusers.calendarGroups.calendars.eventsDeleteAttachments)|Not Found|
|[az calendar userscalendargroupscalendarsevent delete-calendar](#users.calendarGroups.calendars.eventsDeleteCalendar)|DeleteCalendar|[Parameters](#Parametersusers.calendarGroups.calendars.eventsDeleteCalendar)|Not Found|
|[az calendar userscalendargroupscalendarsevent delete-extension](#users.calendarGroups.calendars.eventsDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersusers.calendarGroups.calendars.eventsDeleteExtensions)|Not Found|
|[az calendar userscalendargroupscalendarsevent delete-instance](#users.calendarGroups.calendars.eventsDeleteInstances)|DeleteInstances|[Parameters](#Parametersusers.calendarGroups.calendars.eventsDeleteInstances)|Not Found|
|[az calendar userscalendargroupscalendarsevent delete-multi-value-extended-property](#users.calendarGroups.calendars.eventsDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.eventsDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarsevent delete-single-value-extended-property](#users.calendarGroups.calendars.eventsDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.eventsDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarsevent list-attachment](#users.calendarGroups.calendars.eventsListAttachments)|ListAttachments|[Parameters](#Parametersusers.calendarGroups.calendars.eventsListAttachments)|Not Found|
|[az calendar userscalendargroupscalendarsevent list-extension](#users.calendarGroups.calendars.eventsListExtensions)|ListExtensions|[Parameters](#Parametersusers.calendarGroups.calendars.eventsListExtensions)|Not Found|
|[az calendar userscalendargroupscalendarsevent list-instance](#users.calendarGroups.calendars.eventsListInstances)|ListInstances|[Parameters](#Parametersusers.calendarGroups.calendars.eventsListInstances)|Not Found|
|[az calendar userscalendargroupscalendarsevent list-multi-value-extended-property](#users.calendarGroups.calendars.eventsListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.eventsListMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarsevent list-single-value-extended-property](#users.calendarGroups.calendars.eventsListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.eventsListSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarsevent show-attachment](#users.calendarGroups.calendars.eventsGetAttachments)|GetAttachments|[Parameters](#Parametersusers.calendarGroups.calendars.eventsGetAttachments)|Not Found|
|[az calendar userscalendargroupscalendarsevent show-calendar](#users.calendarGroups.calendars.eventsGetCalendar)|GetCalendar|[Parameters](#Parametersusers.calendarGroups.calendars.eventsGetCalendar)|Not Found|
|[az calendar userscalendargroupscalendarsevent show-extension](#users.calendarGroups.calendars.eventsGetExtensions)|GetExtensions|[Parameters](#Parametersusers.calendarGroups.calendars.eventsGetExtensions)|Not Found|
|[az calendar userscalendargroupscalendarsevent show-instance](#users.calendarGroups.calendars.eventsGetInstances)|GetInstances|[Parameters](#Parametersusers.calendarGroups.calendars.eventsGetInstances)|Not Found|
|[az calendar userscalendargroupscalendarsevent show-multi-value-extended-property](#users.calendarGroups.calendars.eventsGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.eventsGetMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarsevent show-single-value-extended-property](#users.calendarGroups.calendars.eventsGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.eventsGetSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarsevent update-attachment](#users.calendarGroups.calendars.eventsUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersusers.calendarGroups.calendars.eventsUpdateAttachments)|Not Found|
|[az calendar userscalendargroupscalendarsevent update-calendar](#users.calendarGroups.calendars.eventsUpdateCalendar)|UpdateCalendar|[Parameters](#Parametersusers.calendarGroups.calendars.eventsUpdateCalendar)|Not Found|
|[az calendar userscalendargroupscalendarsevent update-extension](#users.calendarGroups.calendars.eventsUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersusers.calendarGroups.calendars.eventsUpdateExtensions)|Not Found|
|[az calendar userscalendargroupscalendarsevent update-instance](#users.calendarGroups.calendars.eventsUpdateInstances)|UpdateInstances|[Parameters](#Parametersusers.calendarGroups.calendars.eventsUpdateInstances)|Not Found|
|[az calendar userscalendargroupscalendarsevent update-multi-value-extended-property](#users.calendarGroups.calendars.eventsUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.eventsUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendargroupscalendarsevent update-single-value-extended-property](#users.calendarGroups.calendars.eventsUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarGroups.calendars.eventsUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.calendars.calendarView">Commands in `az calendar userscalendarscalendarview` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar userscalendarscalendarview create-attachment](#users.calendars.calendarViewCreateAttachments)|CreateAttachments|[Parameters](#Parametersusers.calendars.calendarViewCreateAttachments)|Not Found|
|[az calendar userscalendarscalendarview create-extension](#users.calendars.calendarViewCreateExtensions)|CreateExtensions|[Parameters](#Parametersusers.calendars.calendarViewCreateExtensions)|Not Found|
|[az calendar userscalendarscalendarview create-instance](#users.calendars.calendarViewCreateInstances)|CreateInstances|[Parameters](#Parametersusers.calendars.calendarViewCreateInstances)|Not Found|
|[az calendar userscalendarscalendarview create-multi-value-extended-property](#users.calendars.calendarViewCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendars.calendarViewCreateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarscalendarview create-single-value-extended-property](#users.calendars.calendarViewCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendars.calendarViewCreateSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarscalendarview delete-attachment](#users.calendars.calendarViewDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersusers.calendars.calendarViewDeleteAttachments)|Not Found|
|[az calendar userscalendarscalendarview delete-calendar](#users.calendars.calendarViewDeleteCalendar)|DeleteCalendar|[Parameters](#Parametersusers.calendars.calendarViewDeleteCalendar)|Not Found|
|[az calendar userscalendarscalendarview delete-extension](#users.calendars.calendarViewDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersusers.calendars.calendarViewDeleteExtensions)|Not Found|
|[az calendar userscalendarscalendarview delete-instance](#users.calendars.calendarViewDeleteInstances)|DeleteInstances|[Parameters](#Parametersusers.calendars.calendarViewDeleteInstances)|Not Found|
|[az calendar userscalendarscalendarview delete-multi-value-extended-property](#users.calendars.calendarViewDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.calendars.calendarViewDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarscalendarview delete-single-value-extended-property](#users.calendars.calendarViewDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.calendars.calendarViewDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarscalendarview list-attachment](#users.calendars.calendarViewListAttachments)|ListAttachments|[Parameters](#Parametersusers.calendars.calendarViewListAttachments)|Not Found|
|[az calendar userscalendarscalendarview list-extension](#users.calendars.calendarViewListExtensions)|ListExtensions|[Parameters](#Parametersusers.calendars.calendarViewListExtensions)|Not Found|
|[az calendar userscalendarscalendarview list-instance](#users.calendars.calendarViewListInstances)|ListInstances|[Parameters](#Parametersusers.calendars.calendarViewListInstances)|Not Found|
|[az calendar userscalendarscalendarview list-multi-value-extended-property](#users.calendars.calendarViewListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.calendars.calendarViewListMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarscalendarview list-single-value-extended-property](#users.calendars.calendarViewListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.calendars.calendarViewListSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarscalendarview show-attachment](#users.calendars.calendarViewGetAttachments)|GetAttachments|[Parameters](#Parametersusers.calendars.calendarViewGetAttachments)|Not Found|
|[az calendar userscalendarscalendarview show-calendar](#users.calendars.calendarViewGetCalendar)|GetCalendar|[Parameters](#Parametersusers.calendars.calendarViewGetCalendar)|Not Found|
|[az calendar userscalendarscalendarview show-extension](#users.calendars.calendarViewGetExtensions)|GetExtensions|[Parameters](#Parametersusers.calendars.calendarViewGetExtensions)|Not Found|
|[az calendar userscalendarscalendarview show-instance](#users.calendars.calendarViewGetInstances)|GetInstances|[Parameters](#Parametersusers.calendars.calendarViewGetInstances)|Not Found|
|[az calendar userscalendarscalendarview show-multi-value-extended-property](#users.calendars.calendarViewGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.calendars.calendarViewGetMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarscalendarview show-single-value-extended-property](#users.calendars.calendarViewGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.calendars.calendarViewGetSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarscalendarview update-attachment](#users.calendars.calendarViewUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersusers.calendars.calendarViewUpdateAttachments)|Not Found|
|[az calendar userscalendarscalendarview update-calendar](#users.calendars.calendarViewUpdateCalendar)|UpdateCalendar|[Parameters](#Parametersusers.calendars.calendarViewUpdateCalendar)|Not Found|
|[az calendar userscalendarscalendarview update-extension](#users.calendars.calendarViewUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersusers.calendars.calendarViewUpdateExtensions)|Not Found|
|[az calendar userscalendarscalendarview update-instance](#users.calendars.calendarViewUpdateInstances)|UpdateInstances|[Parameters](#Parametersusers.calendars.calendarViewUpdateInstances)|Not Found|
|[az calendar userscalendarscalendarview update-multi-value-extended-property](#users.calendars.calendarViewUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendars.calendarViewUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarscalendarview update-single-value-extended-property](#users.calendars.calendarViewUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendars.calendarViewUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.calendars.events">Commands in `az calendar userscalendarsevent` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar userscalendarsevent create-attachment](#users.calendars.eventsCreateAttachments)|CreateAttachments|[Parameters](#Parametersusers.calendars.eventsCreateAttachments)|Not Found|
|[az calendar userscalendarsevent create-extension](#users.calendars.eventsCreateExtensions)|CreateExtensions|[Parameters](#Parametersusers.calendars.eventsCreateExtensions)|Not Found|
|[az calendar userscalendarsevent create-instance](#users.calendars.eventsCreateInstances)|CreateInstances|[Parameters](#Parametersusers.calendars.eventsCreateInstances)|Not Found|
|[az calendar userscalendarsevent create-multi-value-extended-property](#users.calendars.eventsCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendars.eventsCreateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarsevent create-single-value-extended-property](#users.calendars.eventsCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendars.eventsCreateSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarsevent delete-attachment](#users.calendars.eventsDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersusers.calendars.eventsDeleteAttachments)|Not Found|
|[az calendar userscalendarsevent delete-calendar](#users.calendars.eventsDeleteCalendar)|DeleteCalendar|[Parameters](#Parametersusers.calendars.eventsDeleteCalendar)|Not Found|
|[az calendar userscalendarsevent delete-extension](#users.calendars.eventsDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersusers.calendars.eventsDeleteExtensions)|Not Found|
|[az calendar userscalendarsevent delete-instance](#users.calendars.eventsDeleteInstances)|DeleteInstances|[Parameters](#Parametersusers.calendars.eventsDeleteInstances)|Not Found|
|[az calendar userscalendarsevent delete-multi-value-extended-property](#users.calendars.eventsDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.calendars.eventsDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarsevent delete-single-value-extended-property](#users.calendars.eventsDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.calendars.eventsDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarsevent list-attachment](#users.calendars.eventsListAttachments)|ListAttachments|[Parameters](#Parametersusers.calendars.eventsListAttachments)|Not Found|
|[az calendar userscalendarsevent list-extension](#users.calendars.eventsListExtensions)|ListExtensions|[Parameters](#Parametersusers.calendars.eventsListExtensions)|Not Found|
|[az calendar userscalendarsevent list-instance](#users.calendars.eventsListInstances)|ListInstances|[Parameters](#Parametersusers.calendars.eventsListInstances)|Not Found|
|[az calendar userscalendarsevent list-multi-value-extended-property](#users.calendars.eventsListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.calendars.eventsListMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarsevent list-single-value-extended-property](#users.calendars.eventsListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.calendars.eventsListSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarsevent show-attachment](#users.calendars.eventsGetAttachments)|GetAttachments|[Parameters](#Parametersusers.calendars.eventsGetAttachments)|Not Found|
|[az calendar userscalendarsevent show-calendar](#users.calendars.eventsGetCalendar)|GetCalendar|[Parameters](#Parametersusers.calendars.eventsGetCalendar)|Not Found|
|[az calendar userscalendarsevent show-extension](#users.calendars.eventsGetExtensions)|GetExtensions|[Parameters](#Parametersusers.calendars.eventsGetExtensions)|Not Found|
|[az calendar userscalendarsevent show-instance](#users.calendars.eventsGetInstances)|GetInstances|[Parameters](#Parametersusers.calendars.eventsGetInstances)|Not Found|
|[az calendar userscalendarsevent show-multi-value-extended-property](#users.calendars.eventsGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.calendars.eventsGetMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarsevent show-single-value-extended-property](#users.calendars.eventsGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.calendars.eventsGetSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarsevent update-attachment](#users.calendars.eventsUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersusers.calendars.eventsUpdateAttachments)|Not Found|
|[az calendar userscalendarsevent update-calendar](#users.calendars.eventsUpdateCalendar)|UpdateCalendar|[Parameters](#Parametersusers.calendars.eventsUpdateCalendar)|Not Found|
|[az calendar userscalendarsevent update-extension](#users.calendars.eventsUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersusers.calendars.eventsUpdateExtensions)|Not Found|
|[az calendar userscalendarsevent update-instance](#users.calendars.eventsUpdateInstances)|UpdateInstances|[Parameters](#Parametersusers.calendars.eventsUpdateInstances)|Not Found|
|[az calendar userscalendarsevent update-multi-value-extended-property](#users.calendars.eventsUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendars.eventsUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarsevent update-single-value-extended-property](#users.calendars.eventsUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendars.eventsUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.calendar.calendarView">Commands in `az calendar userscalendarview` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar userscalendarview create-attachment](#users.calendar.calendarViewCreateAttachments)|CreateAttachments|[Parameters](#Parametersusers.calendar.calendarViewCreateAttachments)|Not Found|
|[az calendar userscalendarview create-extension](#users.calendar.calendarViewCreateExtensions)|CreateExtensions|[Parameters](#Parametersusers.calendar.calendarViewCreateExtensions)|Not Found|
|[az calendar userscalendarview create-instance](#users.calendar.calendarViewCreateInstances)|CreateInstances|[Parameters](#Parametersusers.calendar.calendarViewCreateInstances)|Not Found|
|[az calendar userscalendarview create-multi-value-extended-property](#users.calendar.calendarViewCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendar.calendarViewCreateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarview create-single-value-extended-property](#users.calendar.calendarViewCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendar.calendarViewCreateSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarview delete-attachment](#users.calendar.calendarViewDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersusers.calendar.calendarViewDeleteAttachments)|Not Found|
|[az calendar userscalendarview delete-calendar](#users.calendar.calendarViewDeleteCalendar)|DeleteCalendar|[Parameters](#Parametersusers.calendar.calendarViewDeleteCalendar)|Not Found|
|[az calendar userscalendarview delete-extension](#users.calendar.calendarViewDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersusers.calendar.calendarViewDeleteExtensions)|Not Found|
|[az calendar userscalendarview delete-instance](#users.calendar.calendarViewDeleteInstances)|DeleteInstances|[Parameters](#Parametersusers.calendar.calendarViewDeleteInstances)|Not Found|
|[az calendar userscalendarview delete-multi-value-extended-property](#users.calendar.calendarViewDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.calendar.calendarViewDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarview delete-single-value-extended-property](#users.calendar.calendarViewDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.calendar.calendarViewDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarview list-attachment](#users.calendar.calendarViewListAttachments)|ListAttachments|[Parameters](#Parametersusers.calendar.calendarViewListAttachments)|Not Found|
|[az calendar userscalendarview list-extension](#users.calendar.calendarViewListExtensions)|ListExtensions|[Parameters](#Parametersusers.calendar.calendarViewListExtensions)|Not Found|
|[az calendar userscalendarview list-instance](#users.calendar.calendarViewListInstances)|ListInstances|[Parameters](#Parametersusers.calendar.calendarViewListInstances)|Not Found|
|[az calendar userscalendarview list-multi-value-extended-property](#users.calendar.calendarViewListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.calendar.calendarViewListMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarview list-single-value-extended-property](#users.calendar.calendarViewListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.calendar.calendarViewListSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarview show-attachment](#users.calendar.calendarViewGetAttachments)|GetAttachments|[Parameters](#Parametersusers.calendar.calendarViewGetAttachments)|Not Found|
|[az calendar userscalendarview show-calendar](#users.calendar.calendarViewGetCalendar)|GetCalendar|[Parameters](#Parametersusers.calendar.calendarViewGetCalendar)|Not Found|
|[az calendar userscalendarview show-extension](#users.calendar.calendarViewGetExtensions)|GetExtensions|[Parameters](#Parametersusers.calendar.calendarViewGetExtensions)|Not Found|
|[az calendar userscalendarview show-instance](#users.calendar.calendarViewGetInstances)|GetInstances|[Parameters](#Parametersusers.calendar.calendarViewGetInstances)|Not Found|
|[az calendar userscalendarview show-multi-value-extended-property](#users.calendar.calendarViewGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.calendar.calendarViewGetMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarview show-single-value-extended-property](#users.calendar.calendarViewGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.calendar.calendarViewGetSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarview update-attachment](#users.calendar.calendarViewUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersusers.calendar.calendarViewUpdateAttachments)|Not Found|
|[az calendar userscalendarview update-calendar](#users.calendar.calendarViewUpdateCalendar)|UpdateCalendar|[Parameters](#Parametersusers.calendar.calendarViewUpdateCalendar)|Not Found|
|[az calendar userscalendarview update-extension](#users.calendar.calendarViewUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersusers.calendar.calendarViewUpdateExtensions)|Not Found|
|[az calendar userscalendarview update-instance](#users.calendar.calendarViewUpdateInstances)|UpdateInstances|[Parameters](#Parametersusers.calendar.calendarViewUpdateInstances)|Not Found|
|[az calendar userscalendarview update-multi-value-extended-property](#users.calendar.calendarViewUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendar.calendarViewUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarview update-single-value-extended-property](#users.calendar.calendarViewUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendar.calendarViewUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.calendarView">Commands in `az calendar userscalendarview` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar userscalendarview create-attachment](#users.calendarViewCreateAttachments)|CreateAttachments|[Parameters](#Parametersusers.calendarViewCreateAttachments)|Not Found|
|[az calendar userscalendarview create-extension](#users.calendarViewCreateExtensions)|CreateExtensions|[Parameters](#Parametersusers.calendarViewCreateExtensions)|Not Found|
|[az calendar userscalendarview create-instance](#users.calendarViewCreateInstances)|CreateInstances|[Parameters](#Parametersusers.calendarViewCreateInstances)|Not Found|
|[az calendar userscalendarview create-multi-value-extended-property](#users.calendarViewCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarViewCreateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarview create-single-value-extended-property](#users.calendarViewCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarViewCreateSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarview delete-attachment](#users.calendarViewDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersusers.calendarViewDeleteAttachments)|Not Found|
|[az calendar userscalendarview delete-calendar](#users.calendarViewDeleteCalendar)|DeleteCalendar|[Parameters](#Parametersusers.calendarViewDeleteCalendar)|Not Found|
|[az calendar userscalendarview delete-extension](#users.calendarViewDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersusers.calendarViewDeleteExtensions)|Not Found|
|[az calendar userscalendarview delete-instance](#users.calendarViewDeleteInstances)|DeleteInstances|[Parameters](#Parametersusers.calendarViewDeleteInstances)|Not Found|
|[az calendar userscalendarview delete-multi-value-extended-property](#users.calendarViewDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarViewDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarview delete-single-value-extended-property](#users.calendarViewDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarViewDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarview list-attachment](#users.calendarViewListAttachments)|ListAttachments|[Parameters](#Parametersusers.calendarViewListAttachments)|Not Found|
|[az calendar userscalendarview list-extension](#users.calendarViewListExtensions)|ListExtensions|[Parameters](#Parametersusers.calendarViewListExtensions)|Not Found|
|[az calendar userscalendarview list-instance](#users.calendarViewListInstances)|ListInstances|[Parameters](#Parametersusers.calendarViewListInstances)|Not Found|
|[az calendar userscalendarview list-multi-value-extended-property](#users.calendarViewListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarViewListMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarview list-single-value-extended-property](#users.calendarViewListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarViewListSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarview show-attachment](#users.calendarViewGetAttachments)|GetAttachments|[Parameters](#Parametersusers.calendarViewGetAttachments)|Not Found|
|[az calendar userscalendarview show-calendar](#users.calendarViewGetCalendar)|GetCalendar|[Parameters](#Parametersusers.calendarViewGetCalendar)|Not Found|
|[az calendar userscalendarview show-extension](#users.calendarViewGetExtensions)|GetExtensions|[Parameters](#Parametersusers.calendarViewGetExtensions)|Not Found|
|[az calendar userscalendarview show-instance](#users.calendarViewGetInstances)|GetInstances|[Parameters](#Parametersusers.calendarViewGetInstances)|Not Found|
|[az calendar userscalendarview show-multi-value-extended-property](#users.calendarViewGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarViewGetMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarview show-single-value-extended-property](#users.calendarViewGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarViewGetSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarview update-attachment](#users.calendarViewUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersusers.calendarViewUpdateAttachments)|Not Found|
|[az calendar userscalendarview update-calendar](#users.calendarViewUpdateCalendar)|UpdateCalendar|[Parameters](#Parametersusers.calendarViewUpdateCalendar)|Not Found|
|[az calendar userscalendarview update-extension](#users.calendarViewUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersusers.calendarViewUpdateExtensions)|Not Found|
|[az calendar userscalendarview update-instance](#users.calendarViewUpdateInstances)|UpdateInstances|[Parameters](#Parametersusers.calendarViewUpdateInstances)|Not Found|
|[az calendar userscalendarview update-multi-value-extended-property](#users.calendarViewUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarViewUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarview update-single-value-extended-property](#users.calendarViewUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarViewUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.calendarView.calendar">Commands in `az calendar userscalendarviewcalendar` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar userscalendarviewcalendar create-calendar-permission](#users.calendarView.calendarCreateCalendarPermissions)|CreateCalendarPermissions|[Parameters](#Parametersusers.calendarView.calendarCreateCalendarPermissions)|Not Found|
|[az calendar userscalendarviewcalendar create-calendar-view](#users.calendarView.calendarCreateCalendarView)|CreateCalendarView|[Parameters](#Parametersusers.calendarView.calendarCreateCalendarView)|Not Found|
|[az calendar userscalendarviewcalendar create-event](#users.calendarView.calendarCreateEvents)|CreateEvents|[Parameters](#Parametersusers.calendarView.calendarCreateEvents)|Not Found|
|[az calendar userscalendarviewcalendar create-multi-value-extended-property](#users.calendarView.calendarCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarView.calendarCreateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarviewcalendar create-single-value-extended-property](#users.calendarView.calendarCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarView.calendarCreateSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarviewcalendar delete-calendar-permission](#users.calendarView.calendarDeleteCalendarPermissions)|DeleteCalendarPermissions|[Parameters](#Parametersusers.calendarView.calendarDeleteCalendarPermissions)|Not Found|
|[az calendar userscalendarviewcalendar delete-calendar-view](#users.calendarView.calendarDeleteCalendarView)|DeleteCalendarView|[Parameters](#Parametersusers.calendarView.calendarDeleteCalendarView)|Not Found|
|[az calendar userscalendarviewcalendar delete-event](#users.calendarView.calendarDeleteEvents)|DeleteEvents|[Parameters](#Parametersusers.calendarView.calendarDeleteEvents)|Not Found|
|[az calendar userscalendarviewcalendar delete-multi-value-extended-property](#users.calendarView.calendarDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarView.calendarDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarviewcalendar delete-single-value-extended-property](#users.calendarView.calendarDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarView.calendarDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarviewcalendar list-calendar-permission](#users.calendarView.calendarListCalendarPermissions)|ListCalendarPermissions|[Parameters](#Parametersusers.calendarView.calendarListCalendarPermissions)|Not Found|
|[az calendar userscalendarviewcalendar list-calendar-view](#users.calendarView.calendarListCalendarView)|ListCalendarView|[Parameters](#Parametersusers.calendarView.calendarListCalendarView)|Not Found|
|[az calendar userscalendarviewcalendar list-event](#users.calendarView.calendarListEvents)|ListEvents|[Parameters](#Parametersusers.calendarView.calendarListEvents)|Not Found|
|[az calendar userscalendarviewcalendar list-multi-value-extended-property](#users.calendarView.calendarListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarView.calendarListMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarviewcalendar list-single-value-extended-property](#users.calendarView.calendarListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarView.calendarListSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarviewcalendar show-calendar-permission](#users.calendarView.calendarGetCalendarPermissions)|GetCalendarPermissions|[Parameters](#Parametersusers.calendarView.calendarGetCalendarPermissions)|Not Found|
|[az calendar userscalendarviewcalendar show-calendar-view](#users.calendarView.calendarGetCalendarView)|GetCalendarView|[Parameters](#Parametersusers.calendarView.calendarGetCalendarView)|Not Found|
|[az calendar userscalendarviewcalendar show-event](#users.calendarView.calendarGetEvents)|GetEvents|[Parameters](#Parametersusers.calendarView.calendarGetEvents)|Not Found|
|[az calendar userscalendarviewcalendar show-multi-value-extended-property](#users.calendarView.calendarGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarView.calendarGetMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarviewcalendar show-single-value-extended-property](#users.calendarView.calendarGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarView.calendarGetSingleValueExtendedProperties)|Not Found|
|[az calendar userscalendarviewcalendar update-calendar-permission](#users.calendarView.calendarUpdateCalendarPermissions)|UpdateCalendarPermissions|[Parameters](#Parametersusers.calendarView.calendarUpdateCalendarPermissions)|Not Found|
|[az calendar userscalendarviewcalendar update-calendar-view](#users.calendarView.calendarUpdateCalendarView)|UpdateCalendarView|[Parameters](#Parametersusers.calendarView.calendarUpdateCalendarView)|Not Found|
|[az calendar userscalendarviewcalendar update-event](#users.calendarView.calendarUpdateEvents)|UpdateEvents|[Parameters](#Parametersusers.calendarView.calendarUpdateEvents)|Not Found|
|[az calendar userscalendarviewcalendar update-multi-value-extended-property](#users.calendarView.calendarUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.calendarView.calendarUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar userscalendarviewcalendar update-single-value-extended-property](#users.calendarView.calendarUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.calendarView.calendarUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.events">Commands in `az calendar usersevent` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar usersevent create-attachment](#users.eventsCreateAttachments)|CreateAttachments|[Parameters](#Parametersusers.eventsCreateAttachments)|Not Found|
|[az calendar usersevent create-extension](#users.eventsCreateExtensions)|CreateExtensions|[Parameters](#Parametersusers.eventsCreateExtensions)|Not Found|
|[az calendar usersevent create-instance](#users.eventsCreateInstances)|CreateInstances|[Parameters](#Parametersusers.eventsCreateInstances)|Not Found|
|[az calendar usersevent create-multi-value-extended-property](#users.eventsCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.eventsCreateMultiValueExtendedProperties)|Not Found|
|[az calendar usersevent create-single-value-extended-property](#users.eventsCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.eventsCreateSingleValueExtendedProperties)|Not Found|
|[az calendar usersevent delete-attachment](#users.eventsDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersusers.eventsDeleteAttachments)|Not Found|
|[az calendar usersevent delete-calendar](#users.eventsDeleteCalendar)|DeleteCalendar|[Parameters](#Parametersusers.eventsDeleteCalendar)|Not Found|
|[az calendar usersevent delete-extension](#users.eventsDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersusers.eventsDeleteExtensions)|Not Found|
|[az calendar usersevent delete-instance](#users.eventsDeleteInstances)|DeleteInstances|[Parameters](#Parametersusers.eventsDeleteInstances)|Not Found|
|[az calendar usersevent delete-multi-value-extended-property](#users.eventsDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.eventsDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar usersevent delete-single-value-extended-property](#users.eventsDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.eventsDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar usersevent list-attachment](#users.eventsListAttachments)|ListAttachments|[Parameters](#Parametersusers.eventsListAttachments)|Not Found|
|[az calendar usersevent list-extension](#users.eventsListExtensions)|ListExtensions|[Parameters](#Parametersusers.eventsListExtensions)|Not Found|
|[az calendar usersevent list-instance](#users.eventsListInstances)|ListInstances|[Parameters](#Parametersusers.eventsListInstances)|Not Found|
|[az calendar usersevent list-multi-value-extended-property](#users.eventsListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.eventsListMultiValueExtendedProperties)|Not Found|
|[az calendar usersevent list-single-value-extended-property](#users.eventsListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.eventsListSingleValueExtendedProperties)|Not Found|
|[az calendar usersevent show-attachment](#users.eventsGetAttachments)|GetAttachments|[Parameters](#Parametersusers.eventsGetAttachments)|Not Found|
|[az calendar usersevent show-calendar](#users.eventsGetCalendar)|GetCalendar|[Parameters](#Parametersusers.eventsGetCalendar)|Not Found|
|[az calendar usersevent show-extension](#users.eventsGetExtensions)|GetExtensions|[Parameters](#Parametersusers.eventsGetExtensions)|Not Found|
|[az calendar usersevent show-instance](#users.eventsGetInstances)|GetInstances|[Parameters](#Parametersusers.eventsGetInstances)|Not Found|
|[az calendar usersevent show-multi-value-extended-property](#users.eventsGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.eventsGetMultiValueExtendedProperties)|Not Found|
|[az calendar usersevent show-single-value-extended-property](#users.eventsGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.eventsGetSingleValueExtendedProperties)|Not Found|
|[az calendar usersevent update-attachment](#users.eventsUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersusers.eventsUpdateAttachments)|Not Found|
|[az calendar usersevent update-calendar](#users.eventsUpdateCalendar)|UpdateCalendar|[Parameters](#Parametersusers.eventsUpdateCalendar)|Not Found|
|[az calendar usersevent update-extension](#users.eventsUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersusers.eventsUpdateExtensions)|Not Found|
|[az calendar usersevent update-instance](#users.eventsUpdateInstances)|UpdateInstances|[Parameters](#Parametersusers.eventsUpdateInstances)|Not Found|
|[az calendar usersevent update-multi-value-extended-property](#users.eventsUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.eventsUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar usersevent update-single-value-extended-property](#users.eventsUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.eventsUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsInusers.events.calendar">Commands in `az calendar userseventscalendar` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az calendar userseventscalendar create-calendar-permission](#users.events.calendarCreateCalendarPermissions)|CreateCalendarPermissions|[Parameters](#Parametersusers.events.calendarCreateCalendarPermissions)|Not Found|
|[az calendar userseventscalendar create-calendar-view](#users.events.calendarCreateCalendarView)|CreateCalendarView|[Parameters](#Parametersusers.events.calendarCreateCalendarView)|Not Found|
|[az calendar userseventscalendar create-event](#users.events.calendarCreateEvents)|CreateEvents|[Parameters](#Parametersusers.events.calendarCreateEvents)|Not Found|
|[az calendar userseventscalendar create-multi-value-extended-property](#users.events.calendarCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersusers.events.calendarCreateMultiValueExtendedProperties)|Not Found|
|[az calendar userseventscalendar create-single-value-extended-property](#users.events.calendarCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersusers.events.calendarCreateSingleValueExtendedProperties)|Not Found|
|[az calendar userseventscalendar delete-calendar-permission](#users.events.calendarDeleteCalendarPermissions)|DeleteCalendarPermissions|[Parameters](#Parametersusers.events.calendarDeleteCalendarPermissions)|Not Found|
|[az calendar userseventscalendar delete-calendar-view](#users.events.calendarDeleteCalendarView)|DeleteCalendarView|[Parameters](#Parametersusers.events.calendarDeleteCalendarView)|Not Found|
|[az calendar userseventscalendar delete-event](#users.events.calendarDeleteEvents)|DeleteEvents|[Parameters](#Parametersusers.events.calendarDeleteEvents)|Not Found|
|[az calendar userseventscalendar delete-multi-value-extended-property](#users.events.calendarDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersusers.events.calendarDeleteMultiValueExtendedProperties)|Not Found|
|[az calendar userseventscalendar delete-single-value-extended-property](#users.events.calendarDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersusers.events.calendarDeleteSingleValueExtendedProperties)|Not Found|
|[az calendar userseventscalendar list-calendar-permission](#users.events.calendarListCalendarPermissions)|ListCalendarPermissions|[Parameters](#Parametersusers.events.calendarListCalendarPermissions)|Not Found|
|[az calendar userseventscalendar list-calendar-view](#users.events.calendarListCalendarView)|ListCalendarView|[Parameters](#Parametersusers.events.calendarListCalendarView)|Not Found|
|[az calendar userseventscalendar list-event](#users.events.calendarListEvents)|ListEvents|[Parameters](#Parametersusers.events.calendarListEvents)|Not Found|
|[az calendar userseventscalendar list-multi-value-extended-property](#users.events.calendarListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersusers.events.calendarListMultiValueExtendedProperties)|Not Found|
|[az calendar userseventscalendar list-single-value-extended-property](#users.events.calendarListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersusers.events.calendarListSingleValueExtendedProperties)|Not Found|
|[az calendar userseventscalendar show-calendar-permission](#users.events.calendarGetCalendarPermissions)|GetCalendarPermissions|[Parameters](#Parametersusers.events.calendarGetCalendarPermissions)|Not Found|
|[az calendar userseventscalendar show-calendar-view](#users.events.calendarGetCalendarView)|GetCalendarView|[Parameters](#Parametersusers.events.calendarGetCalendarView)|Not Found|
|[az calendar userseventscalendar show-event](#users.events.calendarGetEvents)|GetEvents|[Parameters](#Parametersusers.events.calendarGetEvents)|Not Found|
|[az calendar userseventscalendar show-multi-value-extended-property](#users.events.calendarGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersusers.events.calendarGetMultiValueExtendedProperties)|Not Found|
|[az calendar userseventscalendar show-single-value-extended-property](#users.events.calendarGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersusers.events.calendarGetSingleValueExtendedProperties)|Not Found|
|[az calendar userseventscalendar update-calendar-permission](#users.events.calendarUpdateCalendarPermissions)|UpdateCalendarPermissions|[Parameters](#Parametersusers.events.calendarUpdateCalendarPermissions)|Not Found|
|[az calendar userseventscalendar update-calendar-view](#users.events.calendarUpdateCalendarView)|UpdateCalendarView|[Parameters](#Parametersusers.events.calendarUpdateCalendarView)|Not Found|
|[az calendar userseventscalendar update-event](#users.events.calendarUpdateEvents)|UpdateEvents|[Parameters](#Parametersusers.events.calendarUpdateEvents)|Not Found|
|[az calendar userseventscalendar update-multi-value-extended-property](#users.events.calendarUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersusers.events.calendarUpdateMultiValueExtendedProperties)|Not Found|
|[az calendar userseventscalendar update-single-value-extended-property](#users.events.calendarUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersusers.events.calendarUpdateSingleValueExtendedProperties)|Not Found|


## COMMAND DETAILS

### group `az calendar group`
#### <a name="groupsCreateCalendarView">Command `az calendar group create-calendar-view`</a>

##### <a name="ParametersgroupsCreateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--body**|object|New navigation property|body|body|

#### <a name="groupsCreateEvents">Command `az calendar group create-event`</a>

##### <a name="ParametersgroupsCreateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--body**|object|New navigation property|body|body|

#### <a name="groupsDeleteCalendar">Command `az calendar group delete-calendar`</a>

##### <a name="ParametersgroupsDeleteCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupsDeleteCalendarView">Command `az calendar group delete-calendar-view`</a>

##### <a name="ParametersgroupsDeleteCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupsDeleteEvents">Command `az calendar group delete-event`</a>

##### <a name="ParametersgroupsDeleteEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupsListCalendarView">Command `az calendar group list-calendar-view`</a>

##### <a name="ParametersgroupsListCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsListEvents">Command `az calendar group list-event`</a>

##### <a name="ParametersgroupsListEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsGetCalendar">Command `az calendar group show-calendar`</a>

##### <a name="ParametersgroupsGetCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsGetCalendarView">Command `az calendar group show-calendar-view`</a>

##### <a name="ParametersgroupsGetCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsGetEvents">Command `az calendar group show-event`</a>

##### <a name="ParametersgroupsGetEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsUpdateCalendar">Command `az calendar group update-calendar`</a>

##### <a name="ParametersgroupsUpdateCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="groupsUpdateCalendarView">Command `az calendar group update-calendar-view`</a>

##### <a name="ParametersgroupsUpdateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="groupsUpdateEvents">Command `az calendar group update-event`</a>

##### <a name="ParametersgroupsUpdateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property values|body|body|

### group `az calendar groupscalendar`
#### <a name="groups.calendarCreateCalendarPermissions">Command `az calendar groupscalendar create-calendar-permission`</a>

##### <a name="Parametersgroups.calendarCreateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="groups.calendarCreateCalendarView">Command `az calendar groupscalendar create-calendar-view`</a>

##### <a name="Parametersgroups.calendarCreateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--body**|object|New navigation property|body|body|

#### <a name="groups.calendarCreateEvents">Command `az calendar groupscalendar create-event`</a>

##### <a name="Parametersgroups.calendarCreateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--body**|object|New navigation property|body|body|

#### <a name="groups.calendarCreateMultiValueExtendedProperties">Command `az calendar groupscalendar create-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendarCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.calendarCreateSingleValueExtendedProperties">Command `az calendar groupscalendar create-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendarCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="groups.calendarDeleteCalendarPermissions">Command `az calendar groupscalendar delete-calendar-permission`</a>

##### <a name="Parametersgroups.calendarDeleteCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarDeleteCalendarView">Command `az calendar groupscalendar delete-calendar-view`</a>

##### <a name="Parametersgroups.calendarDeleteCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarDeleteEvents">Command `az calendar groupscalendar delete-event`</a>

##### <a name="Parametersgroups.calendarDeleteEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarDeleteMultiValueExtendedProperties">Command `az calendar groupscalendar delete-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendarDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarDeleteSingleValueExtendedProperties">Command `az calendar groupscalendar delete-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendarDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarListCalendarPermissions">Command `az calendar groupscalendar list-calendar-permission`</a>

##### <a name="Parametersgroups.calendarListCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarListCalendarView">Command `az calendar groupscalendar list-calendar-view`</a>

##### <a name="Parametersgroups.calendarListCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarListEvents">Command `az calendar groupscalendar list-event`</a>

##### <a name="Parametersgroups.calendarListEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarListMultiValueExtendedProperties">Command `az calendar groupscalendar list-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendarListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarListSingleValueExtendedProperties">Command `az calendar groupscalendar list-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendarListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarGetCalendarPermissions">Command `az calendar groupscalendar show-calendar-permission`</a>

##### <a name="Parametersgroups.calendarGetCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarGetCalendarView">Command `az calendar groupscalendar show-calendar-view`</a>

##### <a name="Parametersgroups.calendarGetCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarGetEvents">Command `az calendar groupscalendar show-event`</a>

##### <a name="Parametersgroups.calendarGetEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarGetMultiValueExtendedProperties">Command `az calendar groupscalendar show-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendarGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarGetSingleValueExtendedProperties">Command `az calendar groupscalendar show-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendarGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarUpdateCalendarPermissions">Command `az calendar groupscalendar update-calendar-permission`</a>

##### <a name="Parametersgroups.calendarUpdateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="groups.calendarUpdateCalendarView">Command `az calendar groupscalendar update-calendar-view`</a>

##### <a name="Parametersgroups.calendarUpdateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="groups.calendarUpdateEvents">Command `az calendar groupscalendar update-event`</a>

##### <a name="Parametersgroups.calendarUpdateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="groups.calendarUpdateMultiValueExtendedProperties">Command `az calendar groupscalendar update-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendarUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.calendarUpdateSingleValueExtendedProperties">Command `az calendar groupscalendar update-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendarUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar groupscalendarevent`
#### <a name="groups.calendar.eventsCreateAttachments">Command `az calendar groupscalendarevent create-attachment`</a>

##### <a name="Parametersgroups.calendar.eventsCreateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="groups.calendar.eventsCreateExtensions">Command `az calendar groupscalendarevent create-extension`</a>

##### <a name="Parametersgroups.calendar.eventsCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

#### <a name="groups.calendar.eventsCreateInstances">Command `az calendar groupscalendarevent create-instance`</a>

##### <a name="Parametersgroups.calendar.eventsCreateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="groups.calendar.eventsCreateMultiValueExtendedProperties">Command `az calendar groupscalendarevent create-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.eventsCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.calendar.eventsCreateSingleValueExtendedProperties">Command `az calendar groupscalendarevent create-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.eventsCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="groups.calendar.eventsDeleteAttachments">Command `az calendar groupscalendarevent delete-attachment`</a>

##### <a name="Parametersgroups.calendar.eventsDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendar.eventsDeleteCalendar">Command `az calendar groupscalendarevent delete-calendar`</a>

##### <a name="Parametersgroups.calendar.eventsDeleteCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendar.eventsDeleteExtensions">Command `az calendar groupscalendarevent delete-extension`</a>

##### <a name="Parametersgroups.calendar.eventsDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendar.eventsDeleteInstances">Command `az calendar groupscalendarevent delete-instance`</a>

##### <a name="Parametersgroups.calendar.eventsDeleteInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendar.eventsDeleteMultiValueExtendedProperties">Command `az calendar groupscalendarevent delete-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.eventsDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendar.eventsDeleteSingleValueExtendedProperties">Command `az calendar groupscalendarevent delete-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.eventsDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendar.eventsListAttachments">Command `az calendar groupscalendarevent list-attachment`</a>

##### <a name="Parametersgroups.calendar.eventsListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.eventsListExtensions">Command `az calendar groupscalendarevent list-extension`</a>

##### <a name="Parametersgroups.calendar.eventsListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.eventsListInstances">Command `az calendar groupscalendarevent list-instance`</a>

##### <a name="Parametersgroups.calendar.eventsListInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.eventsListMultiValueExtendedProperties">Command `az calendar groupscalendarevent list-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.eventsListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.eventsListSingleValueExtendedProperties">Command `az calendar groupscalendarevent list-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.eventsListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.eventsGetAttachments">Command `az calendar groupscalendarevent show-attachment`</a>

##### <a name="Parametersgroups.calendar.eventsGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.eventsGetCalendar">Command `az calendar groupscalendarevent show-calendar`</a>

##### <a name="Parametersgroups.calendar.eventsGetCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.eventsGetExtensions">Command `az calendar groupscalendarevent show-extension`</a>

##### <a name="Parametersgroups.calendar.eventsGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.eventsGetInstances">Command `az calendar groupscalendarevent show-instance`</a>

##### <a name="Parametersgroups.calendar.eventsGetInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.eventsGetMultiValueExtendedProperties">Command `az calendar groupscalendarevent show-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.eventsGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.eventsGetSingleValueExtendedProperties">Command `az calendar groupscalendarevent show-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.eventsGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.eventsUpdateAttachments">Command `az calendar groupscalendarevent update-attachment`</a>

##### <a name="Parametersgroups.calendar.eventsUpdateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="groups.calendar.eventsUpdateCalendar">Command `az calendar groupscalendarevent update-calendar`</a>

##### <a name="Parametersgroups.calendar.eventsUpdateCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="groups.calendar.eventsUpdateExtensions">Command `az calendar groupscalendarevent update-extension`</a>

##### <a name="Parametersgroups.calendar.eventsUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="groups.calendar.eventsUpdateInstances">Command `az calendar groupscalendarevent update-instance`</a>

##### <a name="Parametersgroups.calendar.eventsUpdateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="groups.calendar.eventsUpdateMultiValueExtendedProperties">Command `az calendar groupscalendarevent update-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.eventsUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.calendar.eventsUpdateSingleValueExtendedProperties">Command `az calendar groupscalendarevent update-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.eventsUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar groupscalendarview`
#### <a name="groups.calendar.calendarViewCreateAttachments">Command `az calendar groupscalendarview create-attachment`</a>

##### <a name="Parametersgroups.calendar.calendarViewCreateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="groups.calendar.calendarViewCreateExtensions">Command `az calendar groupscalendarview create-extension`</a>

##### <a name="Parametersgroups.calendar.calendarViewCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

#### <a name="groups.calendar.calendarViewCreateInstances">Command `az calendar groupscalendarview create-instance`</a>

##### <a name="Parametersgroups.calendar.calendarViewCreateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="groups.calendar.calendarViewCreateMultiValueExtendedProperties">Command `az calendar groupscalendarview create-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.calendarViewCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.calendar.calendarViewCreateSingleValueExtendedProperties">Command `az calendar groupscalendarview create-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.calendarViewCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="groups.calendar.calendarViewDeleteAttachments">Command `az calendar groupscalendarview delete-attachment`</a>

##### <a name="Parametersgroups.calendar.calendarViewDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendar.calendarViewDeleteCalendar">Command `az calendar groupscalendarview delete-calendar`</a>

##### <a name="Parametersgroups.calendar.calendarViewDeleteCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendar.calendarViewDeleteExtensions">Command `az calendar groupscalendarview delete-extension`</a>

##### <a name="Parametersgroups.calendar.calendarViewDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendar.calendarViewDeleteInstances">Command `az calendar groupscalendarview delete-instance`</a>

##### <a name="Parametersgroups.calendar.calendarViewDeleteInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendar.calendarViewDeleteMultiValueExtendedProperties">Command `az calendar groupscalendarview delete-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.calendarViewDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendar.calendarViewDeleteSingleValueExtendedProperties">Command `az calendar groupscalendarview delete-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.calendarViewDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendar.calendarViewListAttachments">Command `az calendar groupscalendarview list-attachment`</a>

##### <a name="Parametersgroups.calendar.calendarViewListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.calendarViewListExtensions">Command `az calendar groupscalendarview list-extension`</a>

##### <a name="Parametersgroups.calendar.calendarViewListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.calendarViewListInstances">Command `az calendar groupscalendarview list-instance`</a>

##### <a name="Parametersgroups.calendar.calendarViewListInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.calendarViewListMultiValueExtendedProperties">Command `az calendar groupscalendarview list-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.calendarViewListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.calendarViewListSingleValueExtendedProperties">Command `az calendar groupscalendarview list-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.calendarViewListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.calendarViewGetAttachments">Command `az calendar groupscalendarview show-attachment`</a>

##### <a name="Parametersgroups.calendar.calendarViewGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.calendarViewGetCalendar">Command `az calendar groupscalendarview show-calendar`</a>

##### <a name="Parametersgroups.calendar.calendarViewGetCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.calendarViewGetExtensions">Command `az calendar groupscalendarview show-extension`</a>

##### <a name="Parametersgroups.calendar.calendarViewGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.calendarViewGetInstances">Command `az calendar groupscalendarview show-instance`</a>

##### <a name="Parametersgroups.calendar.calendarViewGetInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.calendarViewGetMultiValueExtendedProperties">Command `az calendar groupscalendarview show-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.calendarViewGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.calendarViewGetSingleValueExtendedProperties">Command `az calendar groupscalendarview show-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.calendarViewGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendar.calendarViewUpdateAttachments">Command `az calendar groupscalendarview update-attachment`</a>

##### <a name="Parametersgroups.calendar.calendarViewUpdateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="groups.calendar.calendarViewUpdateCalendar">Command `az calendar groupscalendarview update-calendar`</a>

##### <a name="Parametersgroups.calendar.calendarViewUpdateCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="groups.calendar.calendarViewUpdateExtensions">Command `az calendar groupscalendarview update-extension`</a>

##### <a name="Parametersgroups.calendar.calendarViewUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="groups.calendar.calendarViewUpdateInstances">Command `az calendar groupscalendarview update-instance`</a>

##### <a name="Parametersgroups.calendar.calendarViewUpdateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="groups.calendar.calendarViewUpdateMultiValueExtendedProperties">Command `az calendar groupscalendarview update-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.calendarViewUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.calendar.calendarViewUpdateSingleValueExtendedProperties">Command `az calendar groupscalendarview update-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendar.calendarViewUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar groupscalendarview`
#### <a name="groups.calendarViewCreateAttachments">Command `az calendar groupscalendarview create-attachment`</a>

##### <a name="Parametersgroups.calendarViewCreateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="groups.calendarViewCreateExtensions">Command `az calendar groupscalendarview create-extension`</a>

##### <a name="Parametersgroups.calendarViewCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

#### <a name="groups.calendarViewCreateInstances">Command `az calendar groupscalendarview create-instance`</a>

##### <a name="Parametersgroups.calendarViewCreateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="groups.calendarViewCreateMultiValueExtendedProperties">Command `az calendar groupscalendarview create-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendarViewCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.calendarViewCreateSingleValueExtendedProperties">Command `az calendar groupscalendarview create-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendarViewCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="groups.calendarViewDeleteAttachments">Command `az calendar groupscalendarview delete-attachment`</a>

##### <a name="Parametersgroups.calendarViewDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarViewDeleteCalendar">Command `az calendar groupscalendarview delete-calendar`</a>

##### <a name="Parametersgroups.calendarViewDeleteCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarViewDeleteExtensions">Command `az calendar groupscalendarview delete-extension`</a>

##### <a name="Parametersgroups.calendarViewDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarViewDeleteInstances">Command `az calendar groupscalendarview delete-instance`</a>

##### <a name="Parametersgroups.calendarViewDeleteInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarViewDeleteMultiValueExtendedProperties">Command `az calendar groupscalendarview delete-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendarViewDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarViewDeleteSingleValueExtendedProperties">Command `az calendar groupscalendarview delete-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendarViewDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarViewListAttachments">Command `az calendar groupscalendarview list-attachment`</a>

##### <a name="Parametersgroups.calendarViewListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarViewListExtensions">Command `az calendar groupscalendarview list-extension`</a>

##### <a name="Parametersgroups.calendarViewListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarViewListInstances">Command `az calendar groupscalendarview list-instance`</a>

##### <a name="Parametersgroups.calendarViewListInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarViewListMultiValueExtendedProperties">Command `az calendar groupscalendarview list-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendarViewListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarViewListSingleValueExtendedProperties">Command `az calendar groupscalendarview list-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendarViewListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarViewGetAttachments">Command `az calendar groupscalendarview show-attachment`</a>

##### <a name="Parametersgroups.calendarViewGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarViewGetCalendar">Command `az calendar groupscalendarview show-calendar`</a>

##### <a name="Parametersgroups.calendarViewGetCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarViewGetExtensions">Command `az calendar groupscalendarview show-extension`</a>

##### <a name="Parametersgroups.calendarViewGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarViewGetInstances">Command `az calendar groupscalendarview show-instance`</a>

##### <a name="Parametersgroups.calendarViewGetInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarViewGetMultiValueExtendedProperties">Command `az calendar groupscalendarview show-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendarViewGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarViewGetSingleValueExtendedProperties">Command `az calendar groupscalendarview show-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendarViewGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarViewUpdateAttachments">Command `az calendar groupscalendarview update-attachment`</a>

##### <a name="Parametersgroups.calendarViewUpdateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="groups.calendarViewUpdateCalendar">Command `az calendar groupscalendarview update-calendar`</a>

##### <a name="Parametersgroups.calendarViewUpdateCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="groups.calendarViewUpdateExtensions">Command `az calendar groupscalendarview update-extension`</a>

##### <a name="Parametersgroups.calendarViewUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="groups.calendarViewUpdateInstances">Command `az calendar groupscalendarview update-instance`</a>

##### <a name="Parametersgroups.calendarViewUpdateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="groups.calendarViewUpdateMultiValueExtendedProperties">Command `az calendar groupscalendarview update-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendarViewUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.calendarViewUpdateSingleValueExtendedProperties">Command `az calendar groupscalendarview update-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendarViewUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar groupscalendarviewcalendar`
#### <a name="groups.calendarView.calendarCreateCalendarPermissions">Command `az calendar groupscalendarviewcalendar create-calendar-permission`</a>

##### <a name="Parametersgroups.calendarView.calendarCreateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="groups.calendarView.calendarCreateCalendarView">Command `az calendar groupscalendarviewcalendar create-calendar-view`</a>

##### <a name="Parametersgroups.calendarView.calendarCreateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="groups.calendarView.calendarCreateEvents">Command `az calendar groupscalendarviewcalendar create-event`</a>

##### <a name="Parametersgroups.calendarView.calendarCreateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="groups.calendarView.calendarCreateMultiValueExtendedProperties">Command `az calendar groupscalendarviewcalendar create-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendarView.calendarCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.calendarView.calendarCreateSingleValueExtendedProperties">Command `az calendar groupscalendarviewcalendar create-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendarView.calendarCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="groups.calendarView.calendarDeleteCalendarPermissions">Command `az calendar groupscalendarviewcalendar delete-calendar-permission`</a>

##### <a name="Parametersgroups.calendarView.calendarDeleteCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarView.calendarDeleteCalendarView">Command `az calendar groupscalendarviewcalendar delete-calendar-view`</a>

##### <a name="Parametersgroups.calendarView.calendarDeleteCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarView.calendarDeleteEvents">Command `az calendar groupscalendarviewcalendar delete-event`</a>

##### <a name="Parametersgroups.calendarView.calendarDeleteEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarView.calendarDeleteMultiValueExtendedProperties">Command `az calendar groupscalendarviewcalendar delete-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendarView.calendarDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarView.calendarDeleteSingleValueExtendedProperties">Command `az calendar groupscalendarviewcalendar delete-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendarView.calendarDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.calendarView.calendarListCalendarPermissions">Command `az calendar groupscalendarviewcalendar list-calendar-permission`</a>

##### <a name="Parametersgroups.calendarView.calendarListCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarView.calendarListCalendarView">Command `az calendar groupscalendarviewcalendar list-calendar-view`</a>

##### <a name="Parametersgroups.calendarView.calendarListCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarView.calendarListEvents">Command `az calendar groupscalendarviewcalendar list-event`</a>

##### <a name="Parametersgroups.calendarView.calendarListEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarView.calendarListMultiValueExtendedProperties">Command `az calendar groupscalendarviewcalendar list-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendarView.calendarListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarView.calendarListSingleValueExtendedProperties">Command `az calendar groupscalendarviewcalendar list-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendarView.calendarListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarView.calendarGetCalendarPermissions">Command `az calendar groupscalendarviewcalendar show-calendar-permission`</a>

##### <a name="Parametersgroups.calendarView.calendarGetCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarView.calendarGetCalendarView">Command `az calendar groupscalendarviewcalendar show-calendar-view`</a>

##### <a name="Parametersgroups.calendarView.calendarGetCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarView.calendarGetEvents">Command `az calendar groupscalendarviewcalendar show-event`</a>

##### <a name="Parametersgroups.calendarView.calendarGetEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarView.calendarGetMultiValueExtendedProperties">Command `az calendar groupscalendarviewcalendar show-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendarView.calendarGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarView.calendarGetSingleValueExtendedProperties">Command `az calendar groupscalendarviewcalendar show-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendarView.calendarGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.calendarView.calendarUpdateCalendarPermissions">Command `az calendar groupscalendarviewcalendar update-calendar-permission`</a>

##### <a name="Parametersgroups.calendarView.calendarUpdateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="groups.calendarView.calendarUpdateCalendarView">Command `az calendar groupscalendarviewcalendar update-calendar-view`</a>

##### <a name="Parametersgroups.calendarView.calendarUpdateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="groups.calendarView.calendarUpdateEvents">Command `az calendar groupscalendarviewcalendar update-event`</a>

##### <a name="Parametersgroups.calendarView.calendarUpdateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="groups.calendarView.calendarUpdateMultiValueExtendedProperties">Command `az calendar groupscalendarviewcalendar update-multi-value-extended-property`</a>

##### <a name="Parametersgroups.calendarView.calendarUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.calendarView.calendarUpdateSingleValueExtendedProperties">Command `az calendar groupscalendarviewcalendar update-single-value-extended-property`</a>

##### <a name="Parametersgroups.calendarView.calendarUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar groupsevent`
#### <a name="groups.eventsCreateAttachments">Command `az calendar groupsevent create-attachment`</a>

##### <a name="Parametersgroups.eventsCreateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="groups.eventsCreateExtensions">Command `az calendar groupsevent create-extension`</a>

##### <a name="Parametersgroups.eventsCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

#### <a name="groups.eventsCreateInstances">Command `az calendar groupsevent create-instance`</a>

##### <a name="Parametersgroups.eventsCreateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="groups.eventsCreateMultiValueExtendedProperties">Command `az calendar groupsevent create-multi-value-extended-property`</a>

##### <a name="Parametersgroups.eventsCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.eventsCreateSingleValueExtendedProperties">Command `az calendar groupsevent create-single-value-extended-property`</a>

##### <a name="Parametersgroups.eventsCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="groups.eventsDeleteAttachments">Command `az calendar groupsevent delete-attachment`</a>

##### <a name="Parametersgroups.eventsDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.eventsDeleteCalendar">Command `az calendar groupsevent delete-calendar`</a>

##### <a name="Parametersgroups.eventsDeleteCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.eventsDeleteExtensions">Command `az calendar groupsevent delete-extension`</a>

##### <a name="Parametersgroups.eventsDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.eventsDeleteInstances">Command `az calendar groupsevent delete-instance`</a>

##### <a name="Parametersgroups.eventsDeleteInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.eventsDeleteMultiValueExtendedProperties">Command `az calendar groupsevent delete-multi-value-extended-property`</a>

##### <a name="Parametersgroups.eventsDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.eventsDeleteSingleValueExtendedProperties">Command `az calendar groupsevent delete-single-value-extended-property`</a>

##### <a name="Parametersgroups.eventsDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.eventsListAttachments">Command `az calendar groupsevent list-attachment`</a>

##### <a name="Parametersgroups.eventsListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.eventsListExtensions">Command `az calendar groupsevent list-extension`</a>

##### <a name="Parametersgroups.eventsListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.eventsListInstances">Command `az calendar groupsevent list-instance`</a>

##### <a name="Parametersgroups.eventsListInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.eventsListMultiValueExtendedProperties">Command `az calendar groupsevent list-multi-value-extended-property`</a>

##### <a name="Parametersgroups.eventsListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.eventsListSingleValueExtendedProperties">Command `az calendar groupsevent list-single-value-extended-property`</a>

##### <a name="Parametersgroups.eventsListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.eventsGetAttachments">Command `az calendar groupsevent show-attachment`</a>

##### <a name="Parametersgroups.eventsGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.eventsGetCalendar">Command `az calendar groupsevent show-calendar`</a>

##### <a name="Parametersgroups.eventsGetCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.eventsGetExtensions">Command `az calendar groupsevent show-extension`</a>

##### <a name="Parametersgroups.eventsGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.eventsGetInstances">Command `az calendar groupsevent show-instance`</a>

##### <a name="Parametersgroups.eventsGetInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.eventsGetMultiValueExtendedProperties">Command `az calendar groupsevent show-multi-value-extended-property`</a>

##### <a name="Parametersgroups.eventsGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.eventsGetSingleValueExtendedProperties">Command `az calendar groupsevent show-single-value-extended-property`</a>

##### <a name="Parametersgroups.eventsGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.eventsUpdateAttachments">Command `az calendar groupsevent update-attachment`</a>

##### <a name="Parametersgroups.eventsUpdateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="groups.eventsUpdateCalendar">Command `az calendar groupsevent update-calendar`</a>

##### <a name="Parametersgroups.eventsUpdateCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="groups.eventsUpdateExtensions">Command `az calendar groupsevent update-extension`</a>

##### <a name="Parametersgroups.eventsUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="groups.eventsUpdateInstances">Command `az calendar groupsevent update-instance`</a>

##### <a name="Parametersgroups.eventsUpdateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="groups.eventsUpdateMultiValueExtendedProperties">Command `az calendar groupsevent update-multi-value-extended-property`</a>

##### <a name="Parametersgroups.eventsUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.eventsUpdateSingleValueExtendedProperties">Command `az calendar groupsevent update-single-value-extended-property`</a>

##### <a name="Parametersgroups.eventsUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar groupseventscalendar`
#### <a name="groups.events.calendarCreateCalendarPermissions">Command `az calendar groupseventscalendar create-calendar-permission`</a>

##### <a name="Parametersgroups.events.calendarCreateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="groups.events.calendarCreateCalendarView">Command `az calendar groupseventscalendar create-calendar-view`</a>

##### <a name="Parametersgroups.events.calendarCreateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="groups.events.calendarCreateEvents">Command `az calendar groupseventscalendar create-event`</a>

##### <a name="Parametersgroups.events.calendarCreateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="groups.events.calendarCreateMultiValueExtendedProperties">Command `az calendar groupseventscalendar create-multi-value-extended-property`</a>

##### <a name="Parametersgroups.events.calendarCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.events.calendarCreateSingleValueExtendedProperties">Command `az calendar groupseventscalendar create-single-value-extended-property`</a>

##### <a name="Parametersgroups.events.calendarCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="groups.events.calendarDeleteCalendarPermissions">Command `az calendar groupseventscalendar delete-calendar-permission`</a>

##### <a name="Parametersgroups.events.calendarDeleteCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.events.calendarDeleteCalendarView">Command `az calendar groupseventscalendar delete-calendar-view`</a>

##### <a name="Parametersgroups.events.calendarDeleteCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.events.calendarDeleteEvents">Command `az calendar groupseventscalendar delete-event`</a>

##### <a name="Parametersgroups.events.calendarDeleteEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.events.calendarDeleteMultiValueExtendedProperties">Command `az calendar groupseventscalendar delete-multi-value-extended-property`</a>

##### <a name="Parametersgroups.events.calendarDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.events.calendarDeleteSingleValueExtendedProperties">Command `az calendar groupseventscalendar delete-single-value-extended-property`</a>

##### <a name="Parametersgroups.events.calendarDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.events.calendarListCalendarPermissions">Command `az calendar groupseventscalendar list-calendar-permission`</a>

##### <a name="Parametersgroups.events.calendarListCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.events.calendarListCalendarView">Command `az calendar groupseventscalendar list-calendar-view`</a>

##### <a name="Parametersgroups.events.calendarListCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.events.calendarListEvents">Command `az calendar groupseventscalendar list-event`</a>

##### <a name="Parametersgroups.events.calendarListEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.events.calendarListMultiValueExtendedProperties">Command `az calendar groupseventscalendar list-multi-value-extended-property`</a>

##### <a name="Parametersgroups.events.calendarListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.events.calendarListSingleValueExtendedProperties">Command `az calendar groupseventscalendar list-single-value-extended-property`</a>

##### <a name="Parametersgroups.events.calendarListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.events.calendarGetCalendarPermissions">Command `az calendar groupseventscalendar show-calendar-permission`</a>

##### <a name="Parametersgroups.events.calendarGetCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.events.calendarGetCalendarView">Command `az calendar groupseventscalendar show-calendar-view`</a>

##### <a name="Parametersgroups.events.calendarGetCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.events.calendarGetEvents">Command `az calendar groupseventscalendar show-event`</a>

##### <a name="Parametersgroups.events.calendarGetEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.events.calendarGetMultiValueExtendedProperties">Command `az calendar groupseventscalendar show-multi-value-extended-property`</a>

##### <a name="Parametersgroups.events.calendarGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.events.calendarGetSingleValueExtendedProperties">Command `az calendar groupseventscalendar show-single-value-extended-property`</a>

##### <a name="Parametersgroups.events.calendarGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.events.calendarUpdateCalendarPermissions">Command `az calendar groupseventscalendar update-calendar-permission`</a>

##### <a name="Parametersgroups.events.calendarUpdateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="groups.events.calendarUpdateCalendarView">Command `az calendar groupseventscalendar update-calendar-view`</a>

##### <a name="Parametersgroups.events.calendarUpdateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="groups.events.calendarUpdateEvents">Command `az calendar groupseventscalendar update-event`</a>

##### <a name="Parametersgroups.events.calendarUpdateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="groups.events.calendarUpdateMultiValueExtendedProperties">Command `az calendar groupseventscalendar update-multi-value-extended-property`</a>

##### <a name="Parametersgroups.events.calendarUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.events.calendarUpdateSingleValueExtendedProperties">Command `az calendar groupseventscalendar update-single-value-extended-property`</a>

##### <a name="Parametersgroups.events.calendarUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar placesplace`
#### <a name="places.placeCreatePlace">Command `az calendar placesplace create-place`</a>

##### <a name="Parametersplaces.placeCreatePlace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--address**|object|physicalAddress|address|address|
|**--display-name**|string|The name associated with the place.|display_name|displayName|
|**--geo-coordinates**|object|outlookGeoCoordinates|geo_coordinates|geoCoordinates|
|**--phone**|string|The phone number of the place.|phone|phone|

#### <a name="places.placeDeletePlace">Command `az calendar placesplace delete-place`</a>

##### <a name="Parametersplaces.placeDeletePlace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--place-id**|string|key: id of place|place_id|place-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="places.placeListPlace">Command `az calendar placesplace list-place`</a>

##### <a name="Parametersplaces.placeListPlace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="places.placeGetPlace">Command `az calendar placesplace show-place`</a>

##### <a name="Parametersplaces.placeGetPlace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--place-id**|string|key: id of place|place_id|place-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="places.placeUpdatePlace">Command `az calendar placesplace update-place`</a>

##### <a name="Parametersplaces.placeUpdatePlace">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--place-id**|string|key: id of place|place_id|place-id|
|**--id**|string|Read-only.|id|id|
|**--address**|object|physicalAddress|address|address|
|**--display-name**|string|The name associated with the place.|display_name|displayName|
|**--geo-coordinates**|object|outlookGeoCoordinates|geo_coordinates|geoCoordinates|
|**--phone**|string|The phone number of the place.|phone|phone|

### group `az calendar user`
#### <a name="usersCreateCalendars">Command `az calendar user create-calendar`</a>

##### <a name="ParametersusersCreateCalendars">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="usersCreateCalendarGroups">Command `az calendar user create-calendar-group`</a>

##### <a name="ParametersusersCreateCalendarGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string|Identifies the version of the calendar group. Every time the calendar group is changed, ChangeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--class-id**|uuid|The class identifier. Read-only.|class_id|classId|
|**--name**|string|The group name.|name|name|
|**--calendars**|array|The calendars in the calendar group. Navigation property. Read-only. Nullable.|calendars|calendars|

#### <a name="usersCreateCalendarView">Command `az calendar user create-calendar-view`</a>

##### <a name="ParametersusersCreateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|object|New navigation property|body|body|

#### <a name="usersCreateEvents">Command `az calendar user create-event`</a>

##### <a name="ParametersusersCreateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|object|New navigation property|body|body|

#### <a name="usersDeleteCalendars">Command `az calendar user delete-calendar`</a>

##### <a name="ParametersusersDeleteCalendars">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteCalendar">Command `az calendar user delete-calendar`</a>

##### <a name="ParametersusersDeleteCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="usersDeleteCalendarGroups">Command `az calendar user delete-calendar-group`</a>

##### <a name="ParametersusersDeleteCalendarGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteCalendarView">Command `az calendar user delete-calendar-view`</a>

##### <a name="ParametersusersDeleteCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteEvents">Command `az calendar user delete-event`</a>

##### <a name="ParametersusersDeleteEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersListCalendars">Command `az calendar user list-calendar`</a>

##### <a name="ParametersusersListCalendars">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListCalendarGroups">Command `az calendar user list-calendar-group`</a>

##### <a name="ParametersusersListCalendarGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListCalendarView">Command `az calendar user list-calendar-view`</a>

##### <a name="ParametersusersListCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersListEvents">Command `az calendar user list-event`</a>

##### <a name="ParametersusersListEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetCalendars">Command `az calendar user show-calendar`</a>

##### <a name="ParametersusersGetCalendars">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetCalendar">Command `az calendar user show-calendar`</a>

##### <a name="ParametersusersGetCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="usersGetCalendarGroups">Command `az calendar user show-calendar-group`</a>

##### <a name="ParametersusersGetCalendarGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetCalendarView">Command `az calendar user show-calendar-view`</a>

##### <a name="ParametersusersGetCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetEvents">Command `az calendar user show-event`</a>

##### <a name="ParametersusersGetEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateCalendars">Command `az calendar user update-calendar`</a>

##### <a name="ParametersusersUpdateCalendars">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="usersUpdateCalendar">Command `az calendar user update-calendar`</a>

##### <a name="ParametersusersUpdateCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="usersUpdateCalendarGroups">Command `az calendar user update-calendar-group`</a>

##### <a name="ParametersusersUpdateCalendarGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--id**|string|Read-only.|id|id|
|**--change-key**|string|Identifies the version of the calendar group. Every time the calendar group is changed, ChangeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--class-id**|uuid|The class identifier. Read-only.|class_id|classId|
|**--name**|string|The group name.|name|name|
|**--calendars**|array|The calendars in the calendar group. Navigation property. Read-only. Nullable.|calendars|calendars|

#### <a name="usersUpdateCalendarView">Command `az calendar user update-calendar-view`</a>

##### <a name="ParametersusersUpdateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="usersUpdateEvents">Command `az calendar user update-event`</a>

##### <a name="ParametersusersUpdateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property values|body|body|

### group `az calendar userscalendar`
#### <a name="users.calendarCreateCalendarPermissions">Command `az calendar userscalendar create-calendar-permission`</a>

##### <a name="Parametersusers.calendarCreateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="users.calendarCreateCalendarView">Command `az calendar userscalendar create-calendar-view`</a>

##### <a name="Parametersusers.calendarCreateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.calendarCreateEvents">Command `az calendar userscalendar create-event`</a>

##### <a name="Parametersusers.calendarCreateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.calendarCreateMultiValueExtendedProperties">Command `az calendar userscalendar create-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendarCreateSingleValueExtendedProperties">Command `az calendar userscalendar create-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.calendarDeleteCalendarPermissions">Command `az calendar userscalendar delete-calendar-permission`</a>

##### <a name="Parametersusers.calendarDeleteCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarDeleteCalendarView">Command `az calendar userscalendar delete-calendar-view`</a>

##### <a name="Parametersusers.calendarDeleteCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarDeleteEvents">Command `az calendar userscalendar delete-event`</a>

##### <a name="Parametersusers.calendarDeleteEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarDeleteMultiValueExtendedProperties">Command `az calendar userscalendar delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarDeleteSingleValueExtendedProperties">Command `az calendar userscalendar delete-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarListCalendarPermissions">Command `az calendar userscalendar list-calendar-permission`</a>

##### <a name="Parametersusers.calendarListCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarListCalendarView">Command `az calendar userscalendar list-calendar-view`</a>

##### <a name="Parametersusers.calendarListCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarListEvents">Command `az calendar userscalendar list-event`</a>

##### <a name="Parametersusers.calendarListEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarListMultiValueExtendedProperties">Command `az calendar userscalendar list-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarListSingleValueExtendedProperties">Command `az calendar userscalendar list-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGetCalendarPermissions">Command `az calendar userscalendar show-calendar-permission`</a>

##### <a name="Parametersusers.calendarGetCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGetCalendarView">Command `az calendar userscalendar show-calendar-view`</a>

##### <a name="Parametersusers.calendarGetCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGetEvents">Command `az calendar userscalendar show-event`</a>

##### <a name="Parametersusers.calendarGetEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGetMultiValueExtendedProperties">Command `az calendar userscalendar show-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGetSingleValueExtendedProperties">Command `az calendar userscalendar show-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarUpdateCalendarPermissions">Command `az calendar userscalendar update-calendar-permission`</a>

##### <a name="Parametersusers.calendarUpdateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="users.calendarUpdateCalendarView">Command `az calendar userscalendar update-calendar-view`</a>

##### <a name="Parametersusers.calendarUpdateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.calendarUpdateEvents">Command `az calendar userscalendar update-event`</a>

##### <a name="Parametersusers.calendarUpdateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.calendarUpdateMultiValueExtendedProperties">Command `az calendar userscalendar update-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendarUpdateSingleValueExtendedProperties">Command `az calendar userscalendar update-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar userscalendar`
#### <a name="users.calendarsCreateCalendarPermissions">Command `az calendar userscalendar create-calendar-permission`</a>

##### <a name="Parametersusers.calendarsCreateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="users.calendarsCreateCalendarView">Command `az calendar userscalendar create-calendar-view`</a>

##### <a name="Parametersusers.calendarsCreateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.calendarsCreateEvents">Command `az calendar userscalendar create-event`</a>

##### <a name="Parametersusers.calendarsCreateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.calendarsCreateMultiValueExtendedProperties">Command `az calendar userscalendar create-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarsCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendarsCreateSingleValueExtendedProperties">Command `az calendar userscalendar create-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarsCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.calendarsDeleteCalendarPermissions">Command `az calendar userscalendar delete-calendar-permission`</a>

##### <a name="Parametersusers.calendarsDeleteCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarsDeleteCalendarView">Command `az calendar userscalendar delete-calendar-view`</a>

##### <a name="Parametersusers.calendarsDeleteCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarsDeleteEvents">Command `az calendar userscalendar delete-event`</a>

##### <a name="Parametersusers.calendarsDeleteEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarsDeleteMultiValueExtendedProperties">Command `az calendar userscalendar delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarsDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarsDeleteSingleValueExtendedProperties">Command `az calendar userscalendar delete-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarsDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarsListCalendarPermissions">Command `az calendar userscalendar list-calendar-permission`</a>

##### <a name="Parametersusers.calendarsListCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarsListCalendarView">Command `az calendar userscalendar list-calendar-view`</a>

##### <a name="Parametersusers.calendarsListCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarsListEvents">Command `az calendar userscalendar list-event`</a>

##### <a name="Parametersusers.calendarsListEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarsListMultiValueExtendedProperties">Command `az calendar userscalendar list-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarsListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarsListSingleValueExtendedProperties">Command `az calendar userscalendar list-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarsListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarsGetCalendarPermissions">Command `az calendar userscalendar show-calendar-permission`</a>

##### <a name="Parametersusers.calendarsGetCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarsGetCalendarView">Command `az calendar userscalendar show-calendar-view`</a>

##### <a name="Parametersusers.calendarsGetCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--start-date-time**|string|The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00|start_date_time|startDateTime|
|**--end-date-time**|string|The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00|end_date_time|endDateTime|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarsGetEvents">Command `az calendar userscalendar show-event`</a>

##### <a name="Parametersusers.calendarsGetEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarsGetMultiValueExtendedProperties">Command `az calendar userscalendar show-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarsGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarsGetSingleValueExtendedProperties">Command `az calendar userscalendar show-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarsGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarsUpdateCalendarPermissions">Command `az calendar userscalendar update-calendar-permission`</a>

##### <a name="Parametersusers.calendarsUpdateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="users.calendarsUpdateCalendarView">Command `az calendar userscalendar update-calendar-view`</a>

##### <a name="Parametersusers.calendarsUpdateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.calendarsUpdateEvents">Command `az calendar userscalendar update-event`</a>

##### <a name="Parametersusers.calendarsUpdateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.calendarsUpdateMultiValueExtendedProperties">Command `az calendar userscalendar update-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarsUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendarsUpdateSingleValueExtendedProperties">Command `az calendar userscalendar update-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarsUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar userscalendarevent`
#### <a name="users.calendar.eventsCreateAttachments">Command `az calendar userscalendarevent create-attachment`</a>

##### <a name="Parametersusers.calendar.eventsCreateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.calendar.eventsCreateExtensions">Command `az calendar userscalendarevent create-extension`</a>

##### <a name="Parametersusers.calendar.eventsCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.calendar.eventsCreateInstances">Command `az calendar userscalendarevent create-instance`</a>

##### <a name="Parametersusers.calendar.eventsCreateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.calendar.eventsCreateMultiValueExtendedProperties">Command `az calendar userscalendarevent create-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendar.eventsCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendar.eventsCreateSingleValueExtendedProperties">Command `az calendar userscalendarevent create-single-value-extended-property`</a>

##### <a name="Parametersusers.calendar.eventsCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.calendar.eventsDeleteAttachments">Command `az calendar userscalendarevent delete-attachment`</a>

##### <a name="Parametersusers.calendar.eventsDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendar.eventsDeleteCalendar">Command `az calendar userscalendarevent delete-calendar`</a>

##### <a name="Parametersusers.calendar.eventsDeleteCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendar.eventsDeleteExtensions">Command `az calendar userscalendarevent delete-extension`</a>

##### <a name="Parametersusers.calendar.eventsDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendar.eventsDeleteInstances">Command `az calendar userscalendarevent delete-instance`</a>

##### <a name="Parametersusers.calendar.eventsDeleteInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendar.eventsDeleteMultiValueExtendedProperties">Command `az calendar userscalendarevent delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendar.eventsDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendar.eventsDeleteSingleValueExtendedProperties">Command `az calendar userscalendarevent delete-single-value-extended-property`</a>

##### <a name="Parametersusers.calendar.eventsDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendar.eventsListAttachments">Command `az calendar userscalendarevent list-attachment`</a>

##### <a name="Parametersusers.calendar.eventsListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.eventsListExtensions">Command `az calendar userscalendarevent list-extension`</a>

##### <a name="Parametersusers.calendar.eventsListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.eventsListInstances">Command `az calendar userscalendarevent list-instance`</a>

##### <a name="Parametersusers.calendar.eventsListInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.eventsListMultiValueExtendedProperties">Command `az calendar userscalendarevent list-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendar.eventsListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.eventsListSingleValueExtendedProperties">Command `az calendar userscalendarevent list-single-value-extended-property`</a>

##### <a name="Parametersusers.calendar.eventsListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.eventsGetAttachments">Command `az calendar userscalendarevent show-attachment`</a>

##### <a name="Parametersusers.calendar.eventsGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.eventsGetCalendar">Command `az calendar userscalendarevent show-calendar`</a>

##### <a name="Parametersusers.calendar.eventsGetCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.eventsGetExtensions">Command `az calendar userscalendarevent show-extension`</a>

##### <a name="Parametersusers.calendar.eventsGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.eventsGetInstances">Command `az calendar userscalendarevent show-instance`</a>

##### <a name="Parametersusers.calendar.eventsGetInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.eventsGetMultiValueExtendedProperties">Command `az calendar userscalendarevent show-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendar.eventsGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.eventsGetSingleValueExtendedProperties">Command `az calendar userscalendarevent show-single-value-extended-property`</a>

##### <a name="Parametersusers.calendar.eventsGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.eventsUpdateAttachments">Command `az calendar userscalendarevent update-attachment`</a>

##### <a name="Parametersusers.calendar.eventsUpdateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.calendar.eventsUpdateCalendar">Command `az calendar userscalendarevent update-calendar`</a>

##### <a name="Parametersusers.calendar.eventsUpdateCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="users.calendar.eventsUpdateExtensions">Command `az calendar userscalendarevent update-extension`</a>

##### <a name="Parametersusers.calendar.eventsUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.calendar.eventsUpdateInstances">Command `az calendar userscalendarevent update-instance`</a>

##### <a name="Parametersusers.calendar.eventsUpdateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.calendar.eventsUpdateMultiValueExtendedProperties">Command `az calendar userscalendarevent update-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendar.eventsUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendar.eventsUpdateSingleValueExtendedProperties">Command `az calendar userscalendarevent update-single-value-extended-property`</a>

##### <a name="Parametersusers.calendar.eventsUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar userscalendargroup`
#### <a name="users.calendarGroupsCreateCalendars">Command `az calendar userscalendargroup create-calendar`</a>

##### <a name="Parametersusers.calendarGroupsCreateCalendars">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="users.calendarGroupsDeleteCalendars">Command `az calendar userscalendargroup delete-calendar`</a>

##### <a name="Parametersusers.calendarGroupsDeleteCalendars">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroupsListCalendars">Command `az calendar userscalendargroup list-calendar`</a>

##### <a name="Parametersusers.calendarGroupsListCalendars">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroupsGetCalendars">Command `az calendar userscalendargroup show-calendar`</a>

##### <a name="Parametersusers.calendarGroupsGetCalendars">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroupsUpdateCalendars">Command `az calendar userscalendargroup update-calendar`</a>

##### <a name="Parametersusers.calendarGroupsUpdateCalendars">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### group `az calendar userscalendargroupscalendar`
#### <a name="users.calendarGroups.calendarsCreateCalendarPermissions">Command `az calendar userscalendargroupscalendar create-calendar-permission`</a>

##### <a name="Parametersusers.calendarGroups.calendarsCreateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="users.calendarGroups.calendarsCreateCalendarView">Command `az calendar userscalendargroupscalendar create-calendar-view`</a>

##### <a name="Parametersusers.calendarGroups.calendarsCreateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.calendarGroups.calendarsCreateEvents">Command `az calendar userscalendargroupscalendar create-event`</a>

##### <a name="Parametersusers.calendarGroups.calendarsCreateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.calendarGroups.calendarsCreateMultiValueExtendedProperties">Command `az calendar userscalendargroupscalendar create-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendarsCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendarGroups.calendarsCreateSingleValueExtendedProperties">Command `az calendar userscalendargroupscalendar create-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendarsCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.calendarGroups.calendarsDeleteCalendarPermissions">Command `az calendar userscalendargroupscalendar delete-calendar-permission`</a>

##### <a name="Parametersusers.calendarGroups.calendarsDeleteCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendarsDeleteCalendarView">Command `az calendar userscalendargroupscalendar delete-calendar-view`</a>

##### <a name="Parametersusers.calendarGroups.calendarsDeleteCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendarsDeleteEvents">Command `az calendar userscalendargroupscalendar delete-event`</a>

##### <a name="Parametersusers.calendarGroups.calendarsDeleteEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendarsDeleteMultiValueExtendedProperties">Command `az calendar userscalendargroupscalendar delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendarsDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendarsDeleteSingleValueExtendedProperties">Command `az calendar userscalendargroupscalendar delete-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendarsDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendarsListCalendarPermissions">Command `az calendar userscalendargroupscalendar list-calendar-permission`</a>

##### <a name="Parametersusers.calendarGroups.calendarsListCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendarsListCalendarView">Command `az calendar userscalendargroupscalendar list-calendar-view`</a>

##### <a name="Parametersusers.calendarGroups.calendarsListCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendarsListEvents">Command `az calendar userscalendargroupscalendar list-event`</a>

##### <a name="Parametersusers.calendarGroups.calendarsListEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendarsListMultiValueExtendedProperties">Command `az calendar userscalendargroupscalendar list-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendarsListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendarsListSingleValueExtendedProperties">Command `az calendar userscalendargroupscalendar list-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendarsListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendarsGetCalendarPermissions">Command `az calendar userscalendargroupscalendar show-calendar-permission`</a>

##### <a name="Parametersusers.calendarGroups.calendarsGetCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendarsGetCalendarView">Command `az calendar userscalendargroupscalendar show-calendar-view`</a>

##### <a name="Parametersusers.calendarGroups.calendarsGetCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendarsGetEvents">Command `az calendar userscalendargroupscalendar show-event`</a>

##### <a name="Parametersusers.calendarGroups.calendarsGetEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendarsGetMultiValueExtendedProperties">Command `az calendar userscalendargroupscalendar show-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendarsGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendarsGetSingleValueExtendedProperties">Command `az calendar userscalendargroupscalendar show-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendarsGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendarsUpdateCalendarPermissions">Command `az calendar userscalendargroupscalendar update-calendar-permission`</a>

##### <a name="Parametersusers.calendarGroups.calendarsUpdateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="users.calendarGroups.calendarsUpdateCalendarView">Command `az calendar userscalendargroupscalendar update-calendar-view`</a>

##### <a name="Parametersusers.calendarGroups.calendarsUpdateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.calendarGroups.calendarsUpdateEvents">Command `az calendar userscalendargroupscalendar update-event`</a>

##### <a name="Parametersusers.calendarGroups.calendarsUpdateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.calendarGroups.calendarsUpdateMultiValueExtendedProperties">Command `az calendar userscalendargroupscalendar update-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendarsUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendarGroups.calendarsUpdateSingleValueExtendedProperties">Command `az calendar userscalendargroupscalendar update-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendarsUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar userscalendargroupscalendarscalendarview`
#### <a name="users.calendarGroups.calendars.calendarViewCreateAttachments">Command `az calendar userscalendargroupscalendarscalendarview create-attachment`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewCreateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.calendarGroups.calendars.calendarViewCreateExtensions">Command `az calendar userscalendargroupscalendarscalendarview create-extension`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.calendarGroups.calendars.calendarViewCreateInstances">Command `az calendar userscalendargroupscalendarscalendarview create-instance`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewCreateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.calendarGroups.calendars.calendarViewCreateMultiValueExtendedProperties">Command `az calendar userscalendargroupscalendarscalendarview create-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendarGroups.calendars.calendarViewCreateSingleValueExtendedProperties">Command `az calendar userscalendargroupscalendarscalendarview create-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.calendarGroups.calendars.calendarViewDeleteAttachments">Command `az calendar userscalendargroupscalendarscalendarview delete-attachment`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendars.calendarViewDeleteCalendar">Command `az calendar userscalendargroupscalendarscalendarview delete-calendar`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewDeleteCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendars.calendarViewDeleteExtensions">Command `az calendar userscalendargroupscalendarscalendarview delete-extension`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendars.calendarViewDeleteInstances">Command `az calendar userscalendargroupscalendarscalendarview delete-instance`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewDeleteInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendars.calendarViewDeleteMultiValueExtendedProperties">Command `az calendar userscalendargroupscalendarscalendarview delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendars.calendarViewDeleteSingleValueExtendedProperties">Command `az calendar userscalendargroupscalendarscalendarview delete-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendars.calendarViewListAttachments">Command `az calendar userscalendargroupscalendarscalendarview list-attachment`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.calendarViewListExtensions">Command `az calendar userscalendargroupscalendarscalendarview list-extension`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.calendarViewListInstances">Command `az calendar userscalendargroupscalendarscalendarview list-instance`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewListInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.calendarViewListMultiValueExtendedProperties">Command `az calendar userscalendargroupscalendarscalendarview list-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.calendarViewListSingleValueExtendedProperties">Command `az calendar userscalendargroupscalendarscalendarview list-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.calendarViewGetAttachments">Command `az calendar userscalendargroupscalendarscalendarview show-attachment`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.calendarViewGetCalendar">Command `az calendar userscalendargroupscalendarscalendarview show-calendar`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewGetCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.calendarViewGetExtensions">Command `az calendar userscalendargroupscalendarscalendarview show-extension`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.calendarViewGetInstances">Command `az calendar userscalendargroupscalendarscalendarview show-instance`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewGetInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.calendarViewGetMultiValueExtendedProperties">Command `az calendar userscalendargroupscalendarscalendarview show-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.calendarViewGetSingleValueExtendedProperties">Command `az calendar userscalendargroupscalendarscalendarview show-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.calendarViewUpdateAttachments">Command `az calendar userscalendargroupscalendarscalendarview update-attachment`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewUpdateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.calendarGroups.calendars.calendarViewUpdateCalendar">Command `az calendar userscalendargroupscalendarscalendarview update-calendar`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewUpdateCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="users.calendarGroups.calendars.calendarViewUpdateExtensions">Command `az calendar userscalendargroupscalendarscalendarview update-extension`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.calendarGroups.calendars.calendarViewUpdateInstances">Command `az calendar userscalendargroupscalendarscalendarview update-instance`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewUpdateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.calendarGroups.calendars.calendarViewUpdateMultiValueExtendedProperties">Command `az calendar userscalendargroupscalendarscalendarview update-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendarGroups.calendars.calendarViewUpdateSingleValueExtendedProperties">Command `az calendar userscalendargroupscalendarscalendarview update-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.calendarViewUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar userscalendargroupscalendarsevent`
#### <a name="users.calendarGroups.calendars.eventsCreateAttachments">Command `az calendar userscalendargroupscalendarsevent create-attachment`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsCreateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.calendarGroups.calendars.eventsCreateExtensions">Command `az calendar userscalendargroupscalendarsevent create-extension`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.calendarGroups.calendars.eventsCreateInstances">Command `az calendar userscalendargroupscalendarsevent create-instance`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsCreateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.calendarGroups.calendars.eventsCreateMultiValueExtendedProperties">Command `az calendar userscalendargroupscalendarsevent create-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendarGroups.calendars.eventsCreateSingleValueExtendedProperties">Command `az calendar userscalendargroupscalendarsevent create-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.calendarGroups.calendars.eventsDeleteAttachments">Command `az calendar userscalendargroupscalendarsevent delete-attachment`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendars.eventsDeleteCalendar">Command `az calendar userscalendargroupscalendarsevent delete-calendar`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsDeleteCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendars.eventsDeleteExtensions">Command `az calendar userscalendargroupscalendarsevent delete-extension`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendars.eventsDeleteInstances">Command `az calendar userscalendargroupscalendarsevent delete-instance`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsDeleteInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendars.eventsDeleteMultiValueExtendedProperties">Command `az calendar userscalendargroupscalendarsevent delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendars.eventsDeleteSingleValueExtendedProperties">Command `az calendar userscalendargroupscalendarsevent delete-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarGroups.calendars.eventsListAttachments">Command `az calendar userscalendargroupscalendarsevent list-attachment`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.eventsListExtensions">Command `az calendar userscalendargroupscalendarsevent list-extension`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.eventsListInstances">Command `az calendar userscalendargroupscalendarsevent list-instance`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsListInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.eventsListMultiValueExtendedProperties">Command `az calendar userscalendargroupscalendarsevent list-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.eventsListSingleValueExtendedProperties">Command `az calendar userscalendargroupscalendarsevent list-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.eventsGetAttachments">Command `az calendar userscalendargroupscalendarsevent show-attachment`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.eventsGetCalendar">Command `az calendar userscalendargroupscalendarsevent show-calendar`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsGetCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.eventsGetExtensions">Command `az calendar userscalendargroupscalendarsevent show-extension`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.eventsGetInstances">Command `az calendar userscalendargroupscalendarsevent show-instance`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsGetInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.eventsGetMultiValueExtendedProperties">Command `az calendar userscalendargroupscalendarsevent show-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.eventsGetSingleValueExtendedProperties">Command `az calendar userscalendargroupscalendarsevent show-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarGroups.calendars.eventsUpdateAttachments">Command `az calendar userscalendargroupscalendarsevent update-attachment`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsUpdateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.calendarGroups.calendars.eventsUpdateCalendar">Command `az calendar userscalendargroupscalendarsevent update-calendar`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsUpdateCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="users.calendarGroups.calendars.eventsUpdateExtensions">Command `az calendar userscalendargroupscalendarsevent update-extension`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.calendarGroups.calendars.eventsUpdateInstances">Command `az calendar userscalendargroupscalendarsevent update-instance`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsUpdateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.calendarGroups.calendars.eventsUpdateMultiValueExtendedProperties">Command `az calendar userscalendargroupscalendarsevent update-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendarGroups.calendars.eventsUpdateSingleValueExtendedProperties">Command `az calendar userscalendargroupscalendarsevent update-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarGroups.calendars.eventsUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-group-id**|string|key: id of calendarGroup|calendar_group_id|calendarGroup-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar userscalendarscalendarview`
#### <a name="users.calendars.calendarViewCreateAttachments">Command `az calendar userscalendarscalendarview create-attachment`</a>

##### <a name="Parametersusers.calendars.calendarViewCreateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.calendars.calendarViewCreateExtensions">Command `az calendar userscalendarscalendarview create-extension`</a>

##### <a name="Parametersusers.calendars.calendarViewCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.calendars.calendarViewCreateInstances">Command `az calendar userscalendarscalendarview create-instance`</a>

##### <a name="Parametersusers.calendars.calendarViewCreateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.calendars.calendarViewCreateMultiValueExtendedProperties">Command `az calendar userscalendarscalendarview create-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendars.calendarViewCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendars.calendarViewCreateSingleValueExtendedProperties">Command `az calendar userscalendarscalendarview create-single-value-extended-property`</a>

##### <a name="Parametersusers.calendars.calendarViewCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.calendars.calendarViewDeleteAttachments">Command `az calendar userscalendarscalendarview delete-attachment`</a>

##### <a name="Parametersusers.calendars.calendarViewDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendars.calendarViewDeleteCalendar">Command `az calendar userscalendarscalendarview delete-calendar`</a>

##### <a name="Parametersusers.calendars.calendarViewDeleteCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendars.calendarViewDeleteExtensions">Command `az calendar userscalendarscalendarview delete-extension`</a>

##### <a name="Parametersusers.calendars.calendarViewDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendars.calendarViewDeleteInstances">Command `az calendar userscalendarscalendarview delete-instance`</a>

##### <a name="Parametersusers.calendars.calendarViewDeleteInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendars.calendarViewDeleteMultiValueExtendedProperties">Command `az calendar userscalendarscalendarview delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendars.calendarViewDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendars.calendarViewDeleteSingleValueExtendedProperties">Command `az calendar userscalendarscalendarview delete-single-value-extended-property`</a>

##### <a name="Parametersusers.calendars.calendarViewDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendars.calendarViewListAttachments">Command `az calendar userscalendarscalendarview list-attachment`</a>

##### <a name="Parametersusers.calendars.calendarViewListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.calendarViewListExtensions">Command `az calendar userscalendarscalendarview list-extension`</a>

##### <a name="Parametersusers.calendars.calendarViewListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.calendarViewListInstances">Command `az calendar userscalendarscalendarview list-instance`</a>

##### <a name="Parametersusers.calendars.calendarViewListInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.calendarViewListMultiValueExtendedProperties">Command `az calendar userscalendarscalendarview list-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendars.calendarViewListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.calendarViewListSingleValueExtendedProperties">Command `az calendar userscalendarscalendarview list-single-value-extended-property`</a>

##### <a name="Parametersusers.calendars.calendarViewListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.calendarViewGetAttachments">Command `az calendar userscalendarscalendarview show-attachment`</a>

##### <a name="Parametersusers.calendars.calendarViewGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.calendarViewGetCalendar">Command `az calendar userscalendarscalendarview show-calendar`</a>

##### <a name="Parametersusers.calendars.calendarViewGetCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.calendarViewGetExtensions">Command `az calendar userscalendarscalendarview show-extension`</a>

##### <a name="Parametersusers.calendars.calendarViewGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.calendarViewGetInstances">Command `az calendar userscalendarscalendarview show-instance`</a>

##### <a name="Parametersusers.calendars.calendarViewGetInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.calendarViewGetMultiValueExtendedProperties">Command `az calendar userscalendarscalendarview show-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendars.calendarViewGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.calendarViewGetSingleValueExtendedProperties">Command `az calendar userscalendarscalendarview show-single-value-extended-property`</a>

##### <a name="Parametersusers.calendars.calendarViewGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.calendarViewUpdateAttachments">Command `az calendar userscalendarscalendarview update-attachment`</a>

##### <a name="Parametersusers.calendars.calendarViewUpdateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.calendars.calendarViewUpdateCalendar">Command `az calendar userscalendarscalendarview update-calendar`</a>

##### <a name="Parametersusers.calendars.calendarViewUpdateCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="users.calendars.calendarViewUpdateExtensions">Command `az calendar userscalendarscalendarview update-extension`</a>

##### <a name="Parametersusers.calendars.calendarViewUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.calendars.calendarViewUpdateInstances">Command `az calendar userscalendarscalendarview update-instance`</a>

##### <a name="Parametersusers.calendars.calendarViewUpdateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.calendars.calendarViewUpdateMultiValueExtendedProperties">Command `az calendar userscalendarscalendarview update-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendars.calendarViewUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendars.calendarViewUpdateSingleValueExtendedProperties">Command `az calendar userscalendarscalendarview update-single-value-extended-property`</a>

##### <a name="Parametersusers.calendars.calendarViewUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar userscalendarsevent`
#### <a name="users.calendars.eventsCreateAttachments">Command `az calendar userscalendarsevent create-attachment`</a>

##### <a name="Parametersusers.calendars.eventsCreateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.calendars.eventsCreateExtensions">Command `az calendar userscalendarsevent create-extension`</a>

##### <a name="Parametersusers.calendars.eventsCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.calendars.eventsCreateInstances">Command `az calendar userscalendarsevent create-instance`</a>

##### <a name="Parametersusers.calendars.eventsCreateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.calendars.eventsCreateMultiValueExtendedProperties">Command `az calendar userscalendarsevent create-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendars.eventsCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendars.eventsCreateSingleValueExtendedProperties">Command `az calendar userscalendarsevent create-single-value-extended-property`</a>

##### <a name="Parametersusers.calendars.eventsCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.calendars.eventsDeleteAttachments">Command `az calendar userscalendarsevent delete-attachment`</a>

##### <a name="Parametersusers.calendars.eventsDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendars.eventsDeleteCalendar">Command `az calendar userscalendarsevent delete-calendar`</a>

##### <a name="Parametersusers.calendars.eventsDeleteCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendars.eventsDeleteExtensions">Command `az calendar userscalendarsevent delete-extension`</a>

##### <a name="Parametersusers.calendars.eventsDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendars.eventsDeleteInstances">Command `az calendar userscalendarsevent delete-instance`</a>

##### <a name="Parametersusers.calendars.eventsDeleteInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendars.eventsDeleteMultiValueExtendedProperties">Command `az calendar userscalendarsevent delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendars.eventsDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendars.eventsDeleteSingleValueExtendedProperties">Command `az calendar userscalendarsevent delete-single-value-extended-property`</a>

##### <a name="Parametersusers.calendars.eventsDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendars.eventsListAttachments">Command `az calendar userscalendarsevent list-attachment`</a>

##### <a name="Parametersusers.calendars.eventsListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.eventsListExtensions">Command `az calendar userscalendarsevent list-extension`</a>

##### <a name="Parametersusers.calendars.eventsListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.eventsListInstances">Command `az calendar userscalendarsevent list-instance`</a>

##### <a name="Parametersusers.calendars.eventsListInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.eventsListMultiValueExtendedProperties">Command `az calendar userscalendarsevent list-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendars.eventsListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.eventsListSingleValueExtendedProperties">Command `az calendar userscalendarsevent list-single-value-extended-property`</a>

##### <a name="Parametersusers.calendars.eventsListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.eventsGetAttachments">Command `az calendar userscalendarsevent show-attachment`</a>

##### <a name="Parametersusers.calendars.eventsGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.eventsGetCalendar">Command `az calendar userscalendarsevent show-calendar`</a>

##### <a name="Parametersusers.calendars.eventsGetCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.eventsGetExtensions">Command `az calendar userscalendarsevent show-extension`</a>

##### <a name="Parametersusers.calendars.eventsGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.eventsGetInstances">Command `az calendar userscalendarsevent show-instance`</a>

##### <a name="Parametersusers.calendars.eventsGetInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.eventsGetMultiValueExtendedProperties">Command `az calendar userscalendarsevent show-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendars.eventsGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.eventsGetSingleValueExtendedProperties">Command `az calendar userscalendarsevent show-single-value-extended-property`</a>

##### <a name="Parametersusers.calendars.eventsGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendars.eventsUpdateAttachments">Command `az calendar userscalendarsevent update-attachment`</a>

##### <a name="Parametersusers.calendars.eventsUpdateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.calendars.eventsUpdateCalendar">Command `az calendar userscalendarsevent update-calendar`</a>

##### <a name="Parametersusers.calendars.eventsUpdateCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="users.calendars.eventsUpdateExtensions">Command `az calendar userscalendarsevent update-extension`</a>

##### <a name="Parametersusers.calendars.eventsUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.calendars.eventsUpdateInstances">Command `az calendar userscalendarsevent update-instance`</a>

##### <a name="Parametersusers.calendars.eventsUpdateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.calendars.eventsUpdateMultiValueExtendedProperties">Command `az calendar userscalendarsevent update-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendars.eventsUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendars.eventsUpdateSingleValueExtendedProperties">Command `az calendar userscalendarsevent update-single-value-extended-property`</a>

##### <a name="Parametersusers.calendars.eventsUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--calendar-id**|string|key: id of calendar|calendar_id|calendar-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar userscalendarview`
#### <a name="users.calendar.calendarViewCreateAttachments">Command `az calendar userscalendarview create-attachment`</a>

##### <a name="Parametersusers.calendar.calendarViewCreateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.calendar.calendarViewCreateExtensions">Command `az calendar userscalendarview create-extension`</a>

##### <a name="Parametersusers.calendar.calendarViewCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.calendar.calendarViewCreateInstances">Command `az calendar userscalendarview create-instance`</a>

##### <a name="Parametersusers.calendar.calendarViewCreateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.calendar.calendarViewCreateMultiValueExtendedProperties">Command `az calendar userscalendarview create-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendar.calendarViewCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendar.calendarViewCreateSingleValueExtendedProperties">Command `az calendar userscalendarview create-single-value-extended-property`</a>

##### <a name="Parametersusers.calendar.calendarViewCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.calendar.calendarViewDeleteAttachments">Command `az calendar userscalendarview delete-attachment`</a>

##### <a name="Parametersusers.calendar.calendarViewDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendar.calendarViewDeleteCalendar">Command `az calendar userscalendarview delete-calendar`</a>

##### <a name="Parametersusers.calendar.calendarViewDeleteCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendar.calendarViewDeleteExtensions">Command `az calendar userscalendarview delete-extension`</a>

##### <a name="Parametersusers.calendar.calendarViewDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendar.calendarViewDeleteInstances">Command `az calendar userscalendarview delete-instance`</a>

##### <a name="Parametersusers.calendar.calendarViewDeleteInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendar.calendarViewDeleteMultiValueExtendedProperties">Command `az calendar userscalendarview delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendar.calendarViewDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendar.calendarViewDeleteSingleValueExtendedProperties">Command `az calendar userscalendarview delete-single-value-extended-property`</a>

##### <a name="Parametersusers.calendar.calendarViewDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendar.calendarViewListAttachments">Command `az calendar userscalendarview list-attachment`</a>

##### <a name="Parametersusers.calendar.calendarViewListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.calendarViewListExtensions">Command `az calendar userscalendarview list-extension`</a>

##### <a name="Parametersusers.calendar.calendarViewListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.calendarViewListInstances">Command `az calendar userscalendarview list-instance`</a>

##### <a name="Parametersusers.calendar.calendarViewListInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.calendarViewListMultiValueExtendedProperties">Command `az calendar userscalendarview list-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendar.calendarViewListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.calendarViewListSingleValueExtendedProperties">Command `az calendar userscalendarview list-single-value-extended-property`</a>

##### <a name="Parametersusers.calendar.calendarViewListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.calendarViewGetAttachments">Command `az calendar userscalendarview show-attachment`</a>

##### <a name="Parametersusers.calendar.calendarViewGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.calendarViewGetCalendar">Command `az calendar userscalendarview show-calendar`</a>

##### <a name="Parametersusers.calendar.calendarViewGetCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.calendarViewGetExtensions">Command `az calendar userscalendarview show-extension`</a>

##### <a name="Parametersusers.calendar.calendarViewGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.calendarViewGetInstances">Command `az calendar userscalendarview show-instance`</a>

##### <a name="Parametersusers.calendar.calendarViewGetInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.calendarViewGetMultiValueExtendedProperties">Command `az calendar userscalendarview show-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendar.calendarViewGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.calendarViewGetSingleValueExtendedProperties">Command `az calendar userscalendarview show-single-value-extended-property`</a>

##### <a name="Parametersusers.calendar.calendarViewGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendar.calendarViewUpdateAttachments">Command `az calendar userscalendarview update-attachment`</a>

##### <a name="Parametersusers.calendar.calendarViewUpdateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.calendar.calendarViewUpdateCalendar">Command `az calendar userscalendarview update-calendar`</a>

##### <a name="Parametersusers.calendar.calendarViewUpdateCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="users.calendar.calendarViewUpdateExtensions">Command `az calendar userscalendarview update-extension`</a>

##### <a name="Parametersusers.calendar.calendarViewUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.calendar.calendarViewUpdateInstances">Command `az calendar userscalendarview update-instance`</a>

##### <a name="Parametersusers.calendar.calendarViewUpdateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.calendar.calendarViewUpdateMultiValueExtendedProperties">Command `az calendar userscalendarview update-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendar.calendarViewUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendar.calendarViewUpdateSingleValueExtendedProperties">Command `az calendar userscalendarview update-single-value-extended-property`</a>

##### <a name="Parametersusers.calendar.calendarViewUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar userscalendarview`
#### <a name="users.calendarViewCreateAttachments">Command `az calendar userscalendarview create-attachment`</a>

##### <a name="Parametersusers.calendarViewCreateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.calendarViewCreateExtensions">Command `az calendar userscalendarview create-extension`</a>

##### <a name="Parametersusers.calendarViewCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.calendarViewCreateInstances">Command `az calendar userscalendarview create-instance`</a>

##### <a name="Parametersusers.calendarViewCreateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.calendarViewCreateMultiValueExtendedProperties">Command `az calendar userscalendarview create-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarViewCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendarViewCreateSingleValueExtendedProperties">Command `az calendar userscalendarview create-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarViewCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.calendarViewDeleteAttachments">Command `az calendar userscalendarview delete-attachment`</a>

##### <a name="Parametersusers.calendarViewDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarViewDeleteCalendar">Command `az calendar userscalendarview delete-calendar`</a>

##### <a name="Parametersusers.calendarViewDeleteCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarViewDeleteExtensions">Command `az calendar userscalendarview delete-extension`</a>

##### <a name="Parametersusers.calendarViewDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarViewDeleteInstances">Command `az calendar userscalendarview delete-instance`</a>

##### <a name="Parametersusers.calendarViewDeleteInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarViewDeleteMultiValueExtendedProperties">Command `az calendar userscalendarview delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarViewDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarViewDeleteSingleValueExtendedProperties">Command `az calendar userscalendarview delete-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarViewDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarViewListAttachments">Command `az calendar userscalendarview list-attachment`</a>

##### <a name="Parametersusers.calendarViewListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarViewListExtensions">Command `az calendar userscalendarview list-extension`</a>

##### <a name="Parametersusers.calendarViewListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarViewListInstances">Command `az calendar userscalendarview list-instance`</a>

##### <a name="Parametersusers.calendarViewListInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarViewListMultiValueExtendedProperties">Command `az calendar userscalendarview list-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarViewListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarViewListSingleValueExtendedProperties">Command `az calendar userscalendarview list-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarViewListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarViewGetAttachments">Command `az calendar userscalendarview show-attachment`</a>

##### <a name="Parametersusers.calendarViewGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarViewGetCalendar">Command `az calendar userscalendarview show-calendar`</a>

##### <a name="Parametersusers.calendarViewGetCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarViewGetExtensions">Command `az calendar userscalendarview show-extension`</a>

##### <a name="Parametersusers.calendarViewGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarViewGetInstances">Command `az calendar userscalendarview show-instance`</a>

##### <a name="Parametersusers.calendarViewGetInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarViewGetMultiValueExtendedProperties">Command `az calendar userscalendarview show-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarViewGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarViewGetSingleValueExtendedProperties">Command `az calendar userscalendarview show-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarViewGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarViewUpdateAttachments">Command `az calendar userscalendarview update-attachment`</a>

##### <a name="Parametersusers.calendarViewUpdateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.calendarViewUpdateCalendar">Command `az calendar userscalendarview update-calendar`</a>

##### <a name="Parametersusers.calendarViewUpdateCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="users.calendarViewUpdateExtensions">Command `az calendar userscalendarview update-extension`</a>

##### <a name="Parametersusers.calendarViewUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.calendarViewUpdateInstances">Command `az calendar userscalendarview update-instance`</a>

##### <a name="Parametersusers.calendarViewUpdateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.calendarViewUpdateMultiValueExtendedProperties">Command `az calendar userscalendarview update-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarViewUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendarViewUpdateSingleValueExtendedProperties">Command `az calendar userscalendarview update-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarViewUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar userscalendarviewcalendar`
#### <a name="users.calendarView.calendarCreateCalendarPermissions">Command `az calendar userscalendarviewcalendar create-calendar-permission`</a>

##### <a name="Parametersusers.calendarView.calendarCreateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="users.calendarView.calendarCreateCalendarView">Command `az calendar userscalendarviewcalendar create-calendar-view`</a>

##### <a name="Parametersusers.calendarView.calendarCreateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.calendarView.calendarCreateEvents">Command `az calendar userscalendarviewcalendar create-event`</a>

##### <a name="Parametersusers.calendarView.calendarCreateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.calendarView.calendarCreateMultiValueExtendedProperties">Command `az calendar userscalendarviewcalendar create-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarView.calendarCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendarView.calendarCreateSingleValueExtendedProperties">Command `az calendar userscalendarviewcalendar create-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarView.calendarCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.calendarView.calendarDeleteCalendarPermissions">Command `az calendar userscalendarviewcalendar delete-calendar-permission`</a>

##### <a name="Parametersusers.calendarView.calendarDeleteCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarView.calendarDeleteCalendarView">Command `az calendar userscalendarviewcalendar delete-calendar-view`</a>

##### <a name="Parametersusers.calendarView.calendarDeleteCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarView.calendarDeleteEvents">Command `az calendar userscalendarviewcalendar delete-event`</a>

##### <a name="Parametersusers.calendarView.calendarDeleteEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarView.calendarDeleteMultiValueExtendedProperties">Command `az calendar userscalendarviewcalendar delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarView.calendarDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarView.calendarDeleteSingleValueExtendedProperties">Command `az calendar userscalendarviewcalendar delete-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarView.calendarDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.calendarView.calendarListCalendarPermissions">Command `az calendar userscalendarviewcalendar list-calendar-permission`</a>

##### <a name="Parametersusers.calendarView.calendarListCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarView.calendarListCalendarView">Command `az calendar userscalendarviewcalendar list-calendar-view`</a>

##### <a name="Parametersusers.calendarView.calendarListCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarView.calendarListEvents">Command `az calendar userscalendarviewcalendar list-event`</a>

##### <a name="Parametersusers.calendarView.calendarListEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarView.calendarListMultiValueExtendedProperties">Command `az calendar userscalendarviewcalendar list-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarView.calendarListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarView.calendarListSingleValueExtendedProperties">Command `az calendar userscalendarviewcalendar list-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarView.calendarListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarView.calendarGetCalendarPermissions">Command `az calendar userscalendarviewcalendar show-calendar-permission`</a>

##### <a name="Parametersusers.calendarView.calendarGetCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarView.calendarGetCalendarView">Command `az calendar userscalendarviewcalendar show-calendar-view`</a>

##### <a name="Parametersusers.calendarView.calendarGetCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarView.calendarGetEvents">Command `az calendar userscalendarviewcalendar show-event`</a>

##### <a name="Parametersusers.calendarView.calendarGetEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarView.calendarGetMultiValueExtendedProperties">Command `az calendar userscalendarviewcalendar show-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarView.calendarGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarView.calendarGetSingleValueExtendedProperties">Command `az calendar userscalendarviewcalendar show-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarView.calendarGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.calendarView.calendarUpdateCalendarPermissions">Command `az calendar userscalendarviewcalendar update-calendar-permission`</a>

##### <a name="Parametersusers.calendarView.calendarUpdateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="users.calendarView.calendarUpdateCalendarView">Command `az calendar userscalendarviewcalendar update-calendar-view`</a>

##### <a name="Parametersusers.calendarView.calendarUpdateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.calendarView.calendarUpdateEvents">Command `az calendar userscalendarviewcalendar update-event`</a>

##### <a name="Parametersusers.calendarView.calendarUpdateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.calendarView.calendarUpdateMultiValueExtendedProperties">Command `az calendar userscalendarviewcalendar update-multi-value-extended-property`</a>

##### <a name="Parametersusers.calendarView.calendarUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.calendarView.calendarUpdateSingleValueExtendedProperties">Command `az calendar userscalendarviewcalendar update-single-value-extended-property`</a>

##### <a name="Parametersusers.calendarView.calendarUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar usersevent`
#### <a name="users.eventsCreateAttachments">Command `az calendar usersevent create-attachment`</a>

##### <a name="Parametersusers.eventsCreateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.eventsCreateExtensions">Command `az calendar usersevent create-extension`</a>

##### <a name="Parametersusers.eventsCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.eventsCreateInstances">Command `az calendar usersevent create-instance`</a>

##### <a name="Parametersusers.eventsCreateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.eventsCreateMultiValueExtendedProperties">Command `az calendar usersevent create-multi-value-extended-property`</a>

##### <a name="Parametersusers.eventsCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.eventsCreateSingleValueExtendedProperties">Command `az calendar usersevent create-single-value-extended-property`</a>

##### <a name="Parametersusers.eventsCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.eventsDeleteAttachments">Command `az calendar usersevent delete-attachment`</a>

##### <a name="Parametersusers.eventsDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.eventsDeleteCalendar">Command `az calendar usersevent delete-calendar`</a>

##### <a name="Parametersusers.eventsDeleteCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.eventsDeleteExtensions">Command `az calendar usersevent delete-extension`</a>

##### <a name="Parametersusers.eventsDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.eventsDeleteInstances">Command `az calendar usersevent delete-instance`</a>

##### <a name="Parametersusers.eventsDeleteInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.eventsDeleteMultiValueExtendedProperties">Command `az calendar usersevent delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.eventsDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.eventsDeleteSingleValueExtendedProperties">Command `az calendar usersevent delete-single-value-extended-property`</a>

##### <a name="Parametersusers.eventsDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.eventsListAttachments">Command `az calendar usersevent list-attachment`</a>

##### <a name="Parametersusers.eventsListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.eventsListExtensions">Command `az calendar usersevent list-extension`</a>

##### <a name="Parametersusers.eventsListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.eventsListInstances">Command `az calendar usersevent list-instance`</a>

##### <a name="Parametersusers.eventsListInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.eventsListMultiValueExtendedProperties">Command `az calendar usersevent list-multi-value-extended-property`</a>

##### <a name="Parametersusers.eventsListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.eventsListSingleValueExtendedProperties">Command `az calendar usersevent list-single-value-extended-property`</a>

##### <a name="Parametersusers.eventsListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.eventsGetAttachments">Command `az calendar usersevent show-attachment`</a>

##### <a name="Parametersusers.eventsGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.eventsGetCalendar">Command `az calendar usersevent show-calendar`</a>

##### <a name="Parametersusers.eventsGetCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.eventsGetExtensions">Command `az calendar usersevent show-extension`</a>

##### <a name="Parametersusers.eventsGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.eventsGetInstances">Command `az calendar usersevent show-instance`</a>

##### <a name="Parametersusers.eventsGetInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.eventsGetMultiValueExtendedProperties">Command `az calendar usersevent show-multi-value-extended-property`</a>

##### <a name="Parametersusers.eventsGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.eventsGetSingleValueExtendedProperties">Command `az calendar usersevent show-single-value-extended-property`</a>

##### <a name="Parametersusers.eventsGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.eventsUpdateAttachments">Command `az calendar usersevent update-attachment`</a>

##### <a name="Parametersusers.eventsUpdateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The attachment's file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="users.eventsUpdateCalendar">Command `az calendar usersevent update-calendar`</a>

##### <a name="Parametersusers.eventsUpdateCalendar">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-online-meeting-providers**|array|Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.|allowed_online_meeting_providers|allowedOnlineMeetingProviders|
|**--can-edit**|boolean|True if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who has been shared a calendar and granted write access.|can_edit|canEdit|
|**--can-share**|boolean|True if the user has the permission to share the calendar, false otherwise. Only the user who created the calendar can share it.|can_share|canShare|
|**--can-view-private-items**|boolean|True if the user can read calendar items that have been marked private, false otherwise.|can_view_private_items|canViewPrivateItems|
|**--change-key**|string|Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--color**|choice||color|color|
|**--default-online-meeting-provider**|choice||default_online_meeting_provider|defaultOnlineMeetingProvider|
|**--is-removable**|boolean|Indicates whether this user calendar can be deleted from the user mailbox.|is_removable|isRemovable|
|**--is-tallying-responses**|boolean|Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.|is_tallying_responses|isTallyingResponses|
|**--name**|string|The calendar name.|name|name|
|**--owner**|object|emailAddress|owner|owner|
|**--calendar-permissions**|array|The permissions of the users with whom the calendar is shared.|calendar_permissions|calendarPermissions|
|**--calendar-view**|array|The calendar view for the calendar. Navigation property. Read-only.|calendar_view|calendarView|
|**--events**|array|The events in the calendar. Navigation property. Read-only.|events|events|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the calendar. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

#### <a name="users.eventsUpdateExtensions">Command `az calendar usersevent update-extension`</a>

##### <a name="Parametersusers.eventsUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="users.eventsUpdateInstances">Command `az calendar usersevent update-instance`</a>

##### <a name="Parametersusers.eventsUpdateInstances">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.eventsUpdateMultiValueExtendedProperties">Command `az calendar usersevent update-multi-value-extended-property`</a>

##### <a name="Parametersusers.eventsUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.eventsUpdateSingleValueExtendedProperties">Command `az calendar usersevent update-single-value-extended-property`</a>

##### <a name="Parametersusers.eventsUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az calendar userseventscalendar`
#### <a name="users.events.calendarCreateCalendarPermissions">Command `az calendar userseventscalendar create-calendar-permission`</a>

##### <a name="Parametersusers.events.calendarCreateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="users.events.calendarCreateCalendarView">Command `az calendar userseventscalendar create-calendar-view`</a>

##### <a name="Parametersusers.events.calendarCreateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.events.calendarCreateEvents">Command `az calendar userseventscalendar create-event`</a>

##### <a name="Parametersusers.events.calendarCreateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--body**|object|New navigation property|body|body|

#### <a name="users.events.calendarCreateMultiValueExtendedProperties">Command `az calendar userseventscalendar create-multi-value-extended-property`</a>

##### <a name="Parametersusers.events.calendarCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.events.calendarCreateSingleValueExtendedProperties">Command `az calendar userseventscalendar create-single-value-extended-property`</a>

##### <a name="Parametersusers.events.calendarCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="users.events.calendarDeleteCalendarPermissions">Command `az calendar userseventscalendar delete-calendar-permission`</a>

##### <a name="Parametersusers.events.calendarDeleteCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.events.calendarDeleteCalendarView">Command `az calendar userseventscalendar delete-calendar-view`</a>

##### <a name="Parametersusers.events.calendarDeleteCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.events.calendarDeleteEvents">Command `az calendar userseventscalendar delete-event`</a>

##### <a name="Parametersusers.events.calendarDeleteEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.events.calendarDeleteMultiValueExtendedProperties">Command `az calendar userseventscalendar delete-multi-value-extended-property`</a>

##### <a name="Parametersusers.events.calendarDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.events.calendarDeleteSingleValueExtendedProperties">Command `az calendar userseventscalendar delete-single-value-extended-property`</a>

##### <a name="Parametersusers.events.calendarDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="users.events.calendarListCalendarPermissions">Command `az calendar userseventscalendar list-calendar-permission`</a>

##### <a name="Parametersusers.events.calendarListCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.events.calendarListCalendarView">Command `az calendar userseventscalendar list-calendar-view`</a>

##### <a name="Parametersusers.events.calendarListCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.events.calendarListEvents">Command `az calendar userseventscalendar list-event`</a>

##### <a name="Parametersusers.events.calendarListEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.events.calendarListMultiValueExtendedProperties">Command `az calendar userseventscalendar list-multi-value-extended-property`</a>

##### <a name="Parametersusers.events.calendarListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.events.calendarListSingleValueExtendedProperties">Command `az calendar userseventscalendar list-single-value-extended-property`</a>

##### <a name="Parametersusers.events.calendarListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.events.calendarGetCalendarPermissions">Command `az calendar userseventscalendar show-calendar-permission`</a>

##### <a name="Parametersusers.events.calendarGetCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.events.calendarGetCalendarView">Command `az calendar userseventscalendar show-calendar-view`</a>

##### <a name="Parametersusers.events.calendarGetCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.events.calendarGetEvents">Command `az calendar userseventscalendar show-event`</a>

##### <a name="Parametersusers.events.calendarGetEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.events.calendarGetMultiValueExtendedProperties">Command `az calendar userseventscalendar show-multi-value-extended-property`</a>

##### <a name="Parametersusers.events.calendarGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.events.calendarGetSingleValueExtendedProperties">Command `az calendar userseventscalendar show-single-value-extended-property`</a>

##### <a name="Parametersusers.events.calendarGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="users.events.calendarUpdateCalendarPermissions">Command `az calendar userseventscalendar update-calendar-permission`</a>

##### <a name="Parametersusers.events.calendarUpdateCalendarPermissions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--calendar-permission-id**|string|key: id of calendarPermission|calendar_permission_id|calendarPermission-id|
|**--id**|string|Read-only.|id|id|
|**--allowed-roles**|array|List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.|allowed_roles|allowedRoles|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--is-inside-organization**|boolean|True if the user in context (sharee or delegate) is inside the same organization as the calendar owner.|is_inside_organization|isInsideOrganization|
|**--is-removable**|boolean|True if the user can be removed from the list of sharees or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You cannot remove 'My organization' as a sharee to a calendar.|is_removable|isRemovable|
|**--role**|choice||role|role|

#### <a name="users.events.calendarUpdateCalendarView">Command `az calendar userseventscalendar update-calendar-view`</a>

##### <a name="Parametersusers.events.calendarUpdateCalendarView">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.events.calendarUpdateEvents">Command `az calendar userseventscalendar update-event`</a>

##### <a name="Parametersusers.events.calendarUpdateEvents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--body**|object|New navigation property values|body|body|

#### <a name="users.events.calendarUpdateMultiValueExtendedProperties">Command `az calendar userseventscalendar update-multi-value-extended-property`</a>

##### <a name="Parametersusers.events.calendarUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="users.events.calendarUpdateSingleValueExtendedProperties">Command `az calendar userseventscalendar update-single-value-extended-property`</a>

##### <a name="Parametersusers.events.calendarUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|
