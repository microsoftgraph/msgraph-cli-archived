# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_usersactions_v1_0_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_usersactions_v1_0.vendored_sdks.usersactions import UsersActions
    return get_mgmt_service_client(cli_ctx,
                                   UsersActions,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_userscalendarviewattachment(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarcalendarviewattachments


def cf_userscalendarviewcalendar(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarcalendarviewcalendar


def cf_userscalendarviewinstance(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarcalendarviewinstances


def cf_userscalendarview(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarcalendarview


def cf_userscalendareventsattachment(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendareventsattachments


def cf_userscalendareventscalendar(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendareventscalendar


def cf_userscalendareventsinstance(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendareventsinstances


def cf_userscalendarevent(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarevents


def cf_userscalendar(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendar


def cf_userscalendargroupscalendarscalendarviewattachment(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendargroupscalendarscalendarviewattachments


def cf_userscalendargroupscalendarscalendarviewcalendar(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendargroupscalendarscalendarviewcalendar


def cf_userscalendargroupscalendarscalendarviewinstance(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendargroupscalendarscalendarviewinstances


def cf_userscalendargroupscalendarscalendarview(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendargroupscalendarscalendarview


def cf_userscalendargroupscalendarseventsattachment(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendargroupscalendarseventsattachments


def cf_userscalendargroupscalendarseventscalendar(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendargroupscalendarseventscalendar


def cf_userscalendargroupscalendarseventsinstance(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendargroupscalendarseventsinstances


def cf_userscalendargroupscalendarsevent(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendargroupscalendarsevents


def cf_userscalendargroupscalendar(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendargroupscalendars


def cf_userscalendarscalendarviewattachment(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarscalendarviewattachments


def cf_userscalendarscalendarviewcalendar(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarscalendarviewcalendar


def cf_userscalendarscalendarviewinstance(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarscalendarviewinstances


def cf_userscalendarscalendarview(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarscalendarview


def cf_userscalendarseventsattachment(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarseventsattachments


def cf_userscalendarseventscalendar(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarseventscalendar


def cf_userscalendarseventsinstance(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarseventsinstances


def cf_userscalendarsevent(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarsevents


def cf_userscalendar(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendars


def cf_userscalendarviewattachment(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarviewattachments


def cf_userscalendarviewcalendarview(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarviewcalendarcalendarview


def cf_userscalendarviewcalendarevent(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarviewcalendarevents


def cf_userscalendarviewcalendar(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarviewcalendar


def cf_userscalendarviewinstance(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarviewinstances


def cf_userscalendarview(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userscalendarview


def cf_userseventsattachment(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userseventsattachments


def cf_userseventscalendarview(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userseventscalendarcalendarview


def cf_userseventscalendarevent(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userseventscalendarevents


def cf_userseventscalendar(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userseventscalendar


def cf_userseventsinstance(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).userseventsinstances


def cf_usersevent(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersevents


def cf_usersmailfolderschildfolder(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersmailfolderschildfolders


def cf_usersmailfoldersmessagesattachment(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersmailfoldersmessagesattachments


def cf_usersmailfoldersmessage(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersmailfoldersmessages


def cf_usersmailfolder(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersmailfolders


def cf_usersmanageddevice(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersmanageddevices


def cf_usersmessagesattachment(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersmessagesattachments


def cf_usersmessage(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersmessages


def cf_user(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).users


def cf_usersonenotenotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotenotebooks


def cf_usersonenotenotebookssectiongroupsparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotenotebookssectiongroupsparentnotebook


def cf_usersonenotenotebookssectiongroupssection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotenotebookssectiongroupssections


def cf_usersonenotenotebookssectiongroupssectionspage(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotenotebookssectiongroupssectionspages


def cf_usersonenotenotebookssectiongroupssectionspagesparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotenotebookssectiongroupssectionspagesparentnotebook


def cf_usersonenotenotebookssectiongroupssectionspagesparentsection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotenotebookssectiongroupssectionspagesparentsection


def cf_usersonenotenotebookssectiongroupssectionsparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotenotebookssectiongroupssectionsparentnotebook


def cf_usersonenotenotebookssection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotenotebookssections


def cf_usersonenotenotebookssectionspage(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotenotebookssectionspages


def cf_usersonenotenotebookssectionspagesparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotenotebookssectionspagesparentnotebook


def cf_usersonenotenotebookssectionspagesparentsection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotenotebookssectionspagesparentsection


def cf_usersonenotenotebookssectionsparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotenotebookssectionsparentnotebook


def cf_usersonenotenotebookssectionsparentsectiongroupparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotenotebookssectionsparentsectiongroupparentnotebook


def cf_usersonenotenotebookssectionsparentsectiongroupsection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotenotebookssectionsparentsectiongroupsections


def cf_usersonenotepage(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepages


def cf_usersonenotepagesparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentnotebook


def cf_usersonenotepagesparentnotebooksectiongroupsparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentnotebooksectiongroupsparentnotebook


def cf_usersonenotepagesparentnotebooksectiongroupssection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentnotebooksectiongroupssections


def cf_usersonenotepagesparentnotebooksectiongroupssectionspage(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentnotebooksectiongroupssectionspages


def cf_usersonenotepagesparentnotebooksectiongroupssectionsparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentnotebooksectiongroupssectionsparentnotebook


def cf_usersonenotepagesparentnotebooksection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentnotebooksections


def cf_usersonenotepagesparentnotebooksectionspage(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentnotebooksectionspages


def cf_usersonenotepagesparentnotebooksectionsparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentnotebooksectionsparentnotebook


def cf_usersonenotepagesparentnotebooksectionsparentsectiongroupparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentnotebooksectionsparentsectiongroupparentnotebook


def cf_usersonenotepagesparentnotebooksectionsparentsectiongroupsection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentnotebooksectionsparentsectiongroupsections


def cf_usersonenotepagesparentsection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentsection


def cf_usersonenotepagesparentsectionpage(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentsectionpages


def cf_usersonenotepagesparentsectionparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentsectionparentnotebook


def cf_usersonenotepagesparentsectionparentnotebooksectiongroupsparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentsectionparentnotebooksectiongroupsparentnotebook


def cf_usersonenotepagesparentsectionparentnotebooksectiongroupssection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentsectionparentnotebooksectiongroupssections


def cf_usersonenotepagesparentsectionparentnotebooksection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentsectionparentnotebooksections


def cf_usersonenotepagesparentsectiongroupparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentsectionparentsectiongroupparentnotebook


def cf_usersonenotepagesparentsectiongroupparentnotebooksection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentsectionparentsectiongroupparentnotebooksections


def cf_usersonenotepagesparentsectiongroupsection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotepagesparentsectionparentsectiongroupsections


def cf_usersonenotesectiongroupsparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectiongroupsparentnotebook


def cf_usersonenotesectiongroupsparentnotebooksection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectiongroupsparentnotebooksections


def cf_usersonenotesectiongroupsparentnotebooksectionspage(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectiongroupsparentnotebooksectionspages


def cf_usersonenotesectiongroupsparentnotebooksectionspagesparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectiongroupsparentnotebooksectionspagesparentnotebook


def cf_usersonenotesectiongroupsparentnotebooksectionspagesparentsection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectiongroupsparentnotebooksectionspagesparentsection


def cf_usersonenotesectiongroupsparentnotebooksectionsparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectiongroupsparentnotebooksectionsparentnotebook


def cf_usersonenotesectiongroupssection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectiongroupssections


def cf_usersonenotesectiongroupssectionspage(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectiongroupssectionspages


def cf_usersonenotesectiongroupssectionspagesparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectiongroupssectionspagesparentnotebook


def cf_usersonenotesectiongroupssectionspagesparentnotebooksection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectiongroupssectionspagesparentnotebooksections


def cf_usersonenotesectiongroupssectionspagesparentsection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectiongroupssectionspagesparentsection


def cf_usersonenotesectiongroupssectionsparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectiongroupssectionsparentnotebook


def cf_usersonenotesectiongroupssectionsparentnotebooksection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectiongroupssectionsparentnotebooksections


def cf_usersonenotesection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesections


def cf_usersonenotesectionspage(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectionspages


def cf_usersonenotesectionspagesparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectionspagesparentnotebook


def cf_usersonenotesectionspagesparentnotebooksectiongroupsparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectionspagesparentnotebooksectiongroupsparentnotebook


def cf_usersonenotesectionspagesparentnotebooksectiongroupssection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectionspagesparentnotebooksectiongroupssections


def cf_usersonenotesectionspagesparentnotebooksection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectionspagesparentnotebooksections


def cf_usersonenotesectionspagesparentsection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectionspagesparentsection


def cf_usersonenotesectionsparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectionsparentnotebook


def cf_usersonenotesectionsparentnotebooksectiongroupsparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectionsparentnotebooksectiongroupsparentnotebook


def cf_usersonenotesectionsparentnotebooksectiongroupssection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectionsparentnotebooksectiongroupssections


def cf_usersonenotesectionsparentnotebooksection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectionsparentnotebooksections


def cf_usersonenotesectionsparentsectiongroupparentnotebook(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectionsparentsectiongroupparentnotebook


def cf_usersonenotesectionsparentsectiongroupparentnotebooksection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectionsparentsectiongroupparentnotebooksections


def cf_usersonenotesectionsparentsectiongroupsection(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonenotesectionsparentsectiongroupsections


def cf_usersonlinemeeting(cli_ctx, *_):
    return cf_usersactions_v1_0_cl(cli_ctx).usersonlinemeetings
