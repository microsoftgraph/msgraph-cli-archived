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


def crossdeviceexperiences_user_create_activity(client,
                                                user_id,
                                                id_=None,
                                                activation_url=None,
                                                activity_source_host=None,
                                                app_activity_id=None,
                                                app_display_name=None,
                                                content_info=None,
                                                content_url=None,
                                                created_date_time=None,
                                                expiration_date_time=None,
                                                fallback_url=None,
                                                last_modified_date_time=None,
                                                status=None,
                                                user_timezone=None,
                                                history_items=None,
                                                attribution=None,
                                                background_color=None,
                                                content=None,
                                                description=None,
                                                display_text=None):
    body = {}
    if id_ is not None:
        body['id'] = id_
    if activation_url is not None:
        body['activation_url'] = activation_url
    if activity_source_host is not None:
        body['activity_source_host'] = activity_source_host
    if app_activity_id is not None:
        body['app_activity_id'] = app_activity_id
    if app_display_name is not None:
        body['app_display_name'] = app_display_name
    if content_info is not None:
        body['content_info'] = content_info
    if content_url is not None:
        body['content_url'] = content_url
    if created_date_time is not None:
        body['created_date_time'] = created_date_time
    if expiration_date_time is not None:
        body['expiration_date_time'] = expiration_date_time
    if fallback_url is not None:
        body['fallback_url'] = fallback_url
    if last_modified_date_time is not None:
        body['last_modified_date_time'] = last_modified_date_time
    if status is not None:
        body['status'] = status
    if user_timezone is not None:
        body['user_timezone'] = user_timezone
    if history_items is not None:
        body['history_items'] = history_items
    body['visual_elements'] = {}
    if attribution is not None:
        body['visual_elements']['attribution'] = attribution
    if background_color is not None:
        body['visual_elements']['background_color'] = background_color
    if content is not None:
        body['visual_elements']['content'] = content
    if description is not None:
        body['visual_elements']['description'] = description
    if display_text is not None:
        body['visual_elements']['display_text'] = display_text
    if len(body['visual_elements']) == 0:
        del body['visual_elements']
    return client.create_activities(user_id=user_id,
                                    body=body)


def crossdeviceexperiences_user_delete_activity(client,
                                                user_id,
                                                user_activity_id,
                                                if_match=None):
    return client.delete_activities(user_id=user_id,
                                    user_activity_id=user_activity_id,
                                    if_match=if_match)


def crossdeviceexperiences_user_list_activity(client,
                                              user_id,
                                              orderby=None,
                                              select=None,
                                              expand=None):
    return client.list_activities(user_id=user_id,
                                  orderby=orderby,
                                  select=select,
                                  expand=expand)


def crossdeviceexperiences_user_show_activity(client,
                                              user_id,
                                              user_activity_id,
                                              select=None,
                                              expand=None):
    return client.get_activities(user_id=user_id,
                                 user_activity_id=user_activity_id,
                                 select=select,
                                 expand=expand)


def crossdeviceexperiences_user_update_activity(client,
                                                user_id,
                                                user_activity_id,
                                                id_=None,
                                                activation_url=None,
                                                activity_source_host=None,
                                                app_activity_id=None,
                                                app_display_name=None,
                                                content_info=None,
                                                content_url=None,
                                                created_date_time=None,
                                                expiration_date_time=None,
                                                fallback_url=None,
                                                last_modified_date_time=None,
                                                status=None,
                                                user_timezone=None,
                                                history_items=None,
                                                attribution=None,
                                                background_color=None,
                                                content=None,
                                                description=None,
                                                display_text=None):
    body = {}
    if id_ is not None:
        body['id'] = id_
    if activation_url is not None:
        body['activation_url'] = activation_url
    if activity_source_host is not None:
        body['activity_source_host'] = activity_source_host
    if app_activity_id is not None:
        body['app_activity_id'] = app_activity_id
    if app_display_name is not None:
        body['app_display_name'] = app_display_name
    if content_info is not None:
        body['content_info'] = content_info
    if content_url is not None:
        body['content_url'] = content_url
    if created_date_time is not None:
        body['created_date_time'] = created_date_time
    if expiration_date_time is not None:
        body['expiration_date_time'] = expiration_date_time
    if fallback_url is not None:
        body['fallback_url'] = fallback_url
    if last_modified_date_time is not None:
        body['last_modified_date_time'] = last_modified_date_time
    if status is not None:
        body['status'] = status
    if user_timezone is not None:
        body['user_timezone'] = user_timezone
    if history_items is not None:
        body['history_items'] = history_items
    body['visual_elements'] = {}
    if attribution is not None:
        body['visual_elements']['attribution'] = attribution
    if background_color is not None:
        body['visual_elements']['background_color'] = background_color
    if content is not None:
        body['visual_elements']['content'] = content
    if description is not None:
        body['visual_elements']['description'] = description
    if display_text is not None:
        body['visual_elements']['display_text'] = display_text
    if len(body['visual_elements']) == 0:
        del body['visual_elements']
    return client.update_activities(user_id=user_id,
                                    user_activity_id=user_activity_id,
                                    body=body)


def crossdeviceexperiences_usersactivity_create_history_item(client,
                                                             user_id,
                                                             user_activity_id,
                                                             id_=None,
                                                             active_duration_seconds=None,
                                                             created_date_time=None,
                                                             expiration_date_time=None,
                                                             last_active_date_time=None,
                                                             last_modified_date_time=None,
                                                             started_date_time=None,
                                                             status=None,
                                                             user_timezone=None,
                                                             activity=None):
    body = {}
    if id_ is not None:
        body['id'] = id_
    if active_duration_seconds is not None:
        body['active_duration_seconds'] = active_duration_seconds
    if created_date_time is not None:
        body['created_date_time'] = created_date_time
    if expiration_date_time is not None:
        body['expiration_date_time'] = expiration_date_time
    if last_active_date_time is not None:
        body['last_active_date_time'] = last_active_date_time
    if last_modified_date_time is not None:
        body['last_modified_date_time'] = last_modified_date_time
    if started_date_time is not None:
        body['started_date_time'] = started_date_time
    if status is not None:
        body['status'] = status
    if user_timezone is not None:
        body['user_timezone'] = user_timezone
    if activity is not None:
        body['activity'] = activity
    return client.create_history_items(user_id=user_id,
                                       user_activity_id=user_activity_id,
                                       body=body)


def crossdeviceexperiences_usersactivity_delete_history_item(client,
                                                             user_id,
                                                             user_activity_id,
                                                             activity_history_item_id,
                                                             if_match=None):
    return client.delete_history_items(user_id=user_id,
                                       user_activity_id=user_activity_id,
                                       activity_history_item_id=activity_history_item_id,
                                       if_match=if_match)


def crossdeviceexperiences_usersactivity_list_history_item(client,
                                                           user_id,
                                                           user_activity_id,
                                                           orderby=None,
                                                           select=None,
                                                           expand=None):
    return client.list_history_items(user_id=user_id,
                                     user_activity_id=user_activity_id,
                                     orderby=orderby,
                                     select=select,
                                     expand=expand)


def crossdeviceexperiences_usersactivity_show_history_item(client,
                                                           user_id,
                                                           user_activity_id,
                                                           activity_history_item_id,
                                                           select=None,
                                                           expand=None):
    return client.get_history_items(user_id=user_id,
                                    user_activity_id=user_activity_id,
                                    activity_history_item_id=activity_history_item_id,
                                    select=select,
                                    expand=expand)


def crossdeviceexperiences_usersactivity_update_history_item(client,
                                                             user_id,
                                                             user_activity_id,
                                                             activity_history_item_id,
                                                             id_=None,
                                                             active_duration_seconds=None,
                                                             created_date_time=None,
                                                             expiration_date_time=None,
                                                             last_active_date_time=None,
                                                             last_modified_date_time=None,
                                                             started_date_time=None,
                                                             status=None,
                                                             user_timezone=None,
                                                             activity=None):
    body = {}
    if id_ is not None:
        body['id'] = id_
    if active_duration_seconds is not None:
        body['active_duration_seconds'] = active_duration_seconds
    if created_date_time is not None:
        body['created_date_time'] = created_date_time
    if expiration_date_time is not None:
        body['expiration_date_time'] = expiration_date_time
    if last_active_date_time is not None:
        body['last_active_date_time'] = last_active_date_time
    if last_modified_date_time is not None:
        body['last_modified_date_time'] = last_modified_date_time
    if started_date_time is not None:
        body['started_date_time'] = started_date_time
    if status is not None:
        body['status'] = status
    if user_timezone is not None:
        body['user_timezone'] = user_timezone
    if activity is not None:
        body['activity'] = activity
    return client.update_history_items(user_id=user_id,
                                       user_activity_id=user_activity_id,
                                       activity_history_item_id=activity_history_item_id,
                                       body=body)


def crossdeviceexperiences_usersactivitieshistoryitem_delete_ref_activity(client,
                                                                          user_id,
                                                                          user_activity_id,
                                                                          activity_history_item_id,
                                                                          if_match=None):
    return client.delete_ref_activity(user_id=user_id,
                                      user_activity_id=user_activity_id,
                                      activity_history_item_id=activity_history_item_id,
                                      if_match=if_match)


def crossdeviceexperiences_usersactivitieshistoryitem_set_ref_activity(client,
                                                                       user_id,
                                                                       user_activity_id,
                                                                       activity_history_item_id,
                                                                       body):
    return client.set_ref_activity(user_id=user_id,
                                   user_activity_id=user_activity_id,
                                   activity_history_item_id=activity_history_item_id,
                                   body=body)


def crossdeviceexperiences_usersactivitieshistoryitem_show_activity(client,
                                                                    user_id,
                                                                    user_activity_id,
                                                                    activity_history_item_id,
                                                                    select=None,
                                                                    expand=None):
    return client.get_activity(user_id=user_id,
                               user_activity_id=user_activity_id,
                               activity_history_item_id=activity_history_item_id,
                               select=select,
                               expand=expand)


def crossdeviceexperiences_usersactivitieshistoryitem_show_ref_activity(client,
                                                                        user_id,
                                                                        user_activity_id,
                                                                        activity_history_item_id):
    return client.get_ref_activity(user_id=user_id,
                                   user_activity_id=user_activity_id,
                                   activity_history_item_id=activity_history_item_id)
