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


def people_user_delete(client,
                       user_id,
                       person_id=None,
                       if_match=None):
    if user_id is not None and person_id is not None:
        return client.delete_person(user_id=user_id,
                                    person_id=person_id,
                                    if_match=if_match)
    return client.delete_insight(user_id=user_id,
                                 if_match=if_match)


def people_user_create_person(client,
                              user_id,
                              id_=None,
                              birthday=None,
                              company_name=None,
                              department=None,
                              display_name=None,
                              given_name=None,
                              im_address=None,
                              is_favorite=None,
                              job_title=None,
                              office_location=None,
                              person_notes=None,
                              person_type=None,
                              phones=None,
                              postal_addresses=None,
                              profession=None,
                              scored_email_addresses=None,
                              surname=None,
                              user_principal_name=None,
                              websites=None,
                              yomi_company=None):
    return client.create_person(user_id=user_id,
                                id=id_,
                                birthday=birthday,
                                company_name=company_name,
                                department=department,
                                display_name=display_name,
                                given_name=given_name,
                                im_address=im_address,
                                is_favorite=is_favorite,
                                job_title=job_title,
                                office_location=office_location,
                                person_notes=person_notes,
                                person_type=person_type,
                                phones=phones,
                                postal_addresses=postal_addresses,
                                profession=profession,
                                scored_email_addresses=scored_email_addresses,
                                surname=surname,
                                user_principal_name=user_principal_name,
                                websites=websites,
                                yomi_company=yomi_company)


def people_user_list_person(client,
                            user_id,
                            orderby=None,
                            select=None,
                            expand=None):
    return client.list_person(user_id=user_id,
                              orderby=orderby,
                              select=select,
                              expand=expand)


def people_user_show_insight(client,
                             user_id,
                             select=None,
                             expand=None):
    return client.get_insight(user_id=user_id,
                              select=select,
                              expand=expand)


def people_user_show_person(client,
                            user_id,
                            person_id,
                            select=None,
                            expand=None):
    return client.get_person(user_id=user_id,
                             person_id=person_id,
                             select=select,
                             expand=expand)


def people_user_update_insight(client,
                               user_id,
                               id_=None,
                               shared=None,
                               trending=None,
                               used=None):
    return client.update_insight(user_id=user_id,
                                 id=id_,
                                 shared=shared,
                                 trending=trending,
                                 used=used)


def people_user_update_person(client,
                              user_id,
                              person_id,
                              id_=None,
                              birthday=None,
                              company_name=None,
                              department=None,
                              display_name=None,
                              given_name=None,
                              im_address=None,
                              is_favorite=None,
                              job_title=None,
                              office_location=None,
                              person_notes=None,
                              person_type=None,
                              phones=None,
                              postal_addresses=None,
                              profession=None,
                              scored_email_addresses=None,
                              surname=None,
                              user_principal_name=None,
                              websites=None,
                              yomi_company=None):
    return client.update_person(user_id=user_id,
                                person_id=person_id,
                                id=id_,
                                birthday=birthday,
                                company_name=company_name,
                                department=department,
                                display_name=display_name,
                                given_name=given_name,
                                im_address=im_address,
                                is_favorite=is_favorite,
                                job_title=job_title,
                                office_location=office_location,
                                person_notes=person_notes,
                                person_type=person_type,
                                phones=phones,
                                postal_addresses=postal_addresses,
                                profession=profession,
                                scored_email_addresses=scored_email_addresses,
                                surname=surname,
                                user_principal_name=user_principal_name,
                                websites=websites,
                                yomi_company=yomi_company)


def people_user_insight_delete(client,
                               user_id,
                               shared_insight_id=None,
                               if_match=None,
                               trending_id=None,
                               used_insight_id=None):
    if user_id is not None and shared_insight_id is not None:
        return client.delete_shared(user_id=user_id,
                                    shared_insight_id=shared_insight_id,
                                    if_match=if_match)
    elif user_id is not None and trending_id is not None:
        return client.delete_trending(user_id=user_id,
                                      trending_id=trending_id,
                                      if_match=if_match)
    return client.delete_used(user_id=user_id,
                              used_insight_id=used_insight_id,
                              if_match=if_match)


def people_user_insight_create_shared(client,
                                      user_id,
                                      id_=None,
                                      resource_reference=None,
                                      resource_visualization=None,
                                      sharing_history=None,
                                      microsoft_graph_entity_id=None,
                                      id1=None,
                                      shared_by=None,
                                      shared_date_time=None,
                                      sharing_reference=None,
                                      sharing_subject=None,
                                      sharing_type=None):
    return client.create_shared(user_id=user_id,
                                id=id_,
                                resource_reference=resource_reference,
                                resource_visualization=resource_visualization,
                                sharing_history=sharing_history,
                                microsoft_graph_entity_id=microsoft_graph_entity_id,
                                id1=id1,
                                shared_by=shared_by,
                                shared_date_time=shared_date_time,
                                sharing_reference=sharing_reference,
                                sharing_subject=sharing_subject,
                                sharing_type=sharing_type)


def people_user_insight_create_trending(client,
                                        user_id,
                                        id_=None,
                                        last_modified_date_time=None,
                                        resource_reference=None,
                                        resource_visualization=None,
                                        weight=None,
                                        microsoft_graph_entity_id=None):
    return client.create_trending(user_id=user_id,
                                  id=id_,
                                  last_modified_date_time=last_modified_date_time,
                                  resource_reference=resource_reference,
                                  resource_visualization=resource_visualization,
                                  weight=weight,
                                  microsoft_graph_entity_id=microsoft_graph_entity_id)


def people_user_insight_create_used(client,
                                    user_id,
                                    id_=None,
                                    last_used=None,
                                    resource_reference=None,
                                    resource_visualization=None,
                                    microsoft_graph_entity_id=None):
    return client.create_used(user_id=user_id,
                              id=id_,
                              last_used=last_used,
                              resource_reference=resource_reference,
                              resource_visualization=resource_visualization,
                              microsoft_graph_entity_id=microsoft_graph_entity_id)


def people_user_insight_list_shared(client,
                                    user_id,
                                    orderby=None,
                                    select=None,
                                    expand=None):
    return client.list_shared(user_id=user_id,
                              orderby=orderby,
                              select=select,
                              expand=expand)


def people_user_insight_list_trending(client,
                                      user_id,
                                      orderby=None,
                                      select=None,
                                      expand=None):
    return client.list_trending(user_id=user_id,
                                orderby=orderby,
                                select=select,
                                expand=expand)


def people_user_insight_list_used(client,
                                  user_id,
                                  orderby=None,
                                  select=None,
                                  expand=None):
    return client.list_used(user_id=user_id,
                            orderby=orderby,
                            select=select,
                            expand=expand)


def people_user_insight_show_shared(client,
                                    user_id,
                                    shared_insight_id,
                                    select=None,
                                    expand=None):
    return client.get_shared(user_id=user_id,
                             shared_insight_id=shared_insight_id,
                             select=select,
                             expand=expand)


def people_user_insight_show_trending(client,
                                      user_id,
                                      trending_id,
                                      select=None,
                                      expand=None):
    return client.get_trending(user_id=user_id,
                               trending_id=trending_id,
                               select=select,
                               expand=expand)


def people_user_insight_show_used(client,
                                  user_id,
                                  used_insight_id,
                                  select=None,
                                  expand=None):
    return client.get_used(user_id=user_id,
                           used_insight_id=used_insight_id,
                           select=select,
                           expand=expand)


def people_user_insight_update_shared(client,
                                      user_id,
                                      shared_insight_id,
                                      id_=None,
                                      resource_reference=None,
                                      resource_visualization=None,
                                      sharing_history=None,
                                      microsoft_graph_entity_id=None,
                                      id1=None,
                                      shared_by=None,
                                      shared_date_time=None,
                                      sharing_reference=None,
                                      sharing_subject=None,
                                      sharing_type=None):
    return client.update_shared(user_id=user_id,
                                shared_insight_id=shared_insight_id,
                                id=id_,
                                resource_reference=resource_reference,
                                resource_visualization=resource_visualization,
                                sharing_history=sharing_history,
                                microsoft_graph_entity_id=microsoft_graph_entity_id,
                                id1=id1,
                                shared_by=shared_by,
                                shared_date_time=shared_date_time,
                                sharing_reference=sharing_reference,
                                sharing_subject=sharing_subject,
                                sharing_type=sharing_type)


def people_user_insight_update_trending(client,
                                        user_id,
                                        trending_id,
                                        id_=None,
                                        last_modified_date_time=None,
                                        resource_reference=None,
                                        resource_visualization=None,
                                        weight=None,
                                        microsoft_graph_entity_id=None):
    return client.update_trending(user_id=user_id,
                                  trending_id=trending_id,
                                  id=id_,
                                  last_modified_date_time=last_modified_date_time,
                                  resource_reference=resource_reference,
                                  resource_visualization=resource_visualization,
                                  weight=weight,
                                  microsoft_graph_entity_id=microsoft_graph_entity_id)


def people_user_insight_update_used(client,
                                    user_id,
                                    used_insight_id,
                                    id_=None,
                                    last_used=None,
                                    resource_reference=None,
                                    resource_visualization=None,
                                    microsoft_graph_entity_id=None):
    return client.update_used(user_id=user_id,
                              used_insight_id=used_insight_id,
                              id=id_,
                              last_used=last_used,
                              resource_reference=resource_reference,
                              resource_visualization=resource_visualization,
                              microsoft_graph_entity_id=microsoft_graph_entity_id)


def people_user_insight_shared_delete(client,
                                      user_id,
                                      shared_insight_id,
                                      if_match=None):
    if user_id is not None and shared_insight_id is not None:
        return client.delete_ref_last_shared_method(user_id=user_id,
                                                    shared_insight_id=shared_insight_id,
                                                    if_match=if_match)
    return client.delete_ref_resource(user_id=user_id,
                                      shared_insight_id=shared_insight_id,
                                      if_match=if_match)


def people_user_insight_shared_set_ref_last_shared_method(client,
                                                          user_id,
                                                          shared_insight_id,
                                                          body):
    return client.set_ref_last_shared_method(user_id=user_id,
                                             shared_insight_id=shared_insight_id,
                                             body=body)


def people_user_insight_shared_set_ref_resource(client,
                                                user_id,
                                                shared_insight_id,
                                                body):
    return client.set_ref_resource(user_id=user_id,
                                   shared_insight_id=shared_insight_id,
                                   body=body)


def people_user_insight_shared_show_last_shared_method(client,
                                                       user_id,
                                                       shared_insight_id,
                                                       select=None,
                                                       expand=None):
    return client.get_last_shared_method(user_id=user_id,
                                         shared_insight_id=shared_insight_id,
                                         select=select,
                                         expand=expand)


def people_user_insight_shared_show_ref_last_shared_method(client,
                                                           user_id,
                                                           shared_insight_id):
    return client.get_ref_last_shared_method(user_id=user_id,
                                             shared_insight_id=shared_insight_id)


def people_user_insight_shared_show_ref_resource(client,
                                                 user_id,
                                                 shared_insight_id):
    return client.get_ref_resource(user_id=user_id,
                                   shared_insight_id=shared_insight_id)


def people_user_insight_shared_show_resource(client,
                                             user_id,
                                             shared_insight_id,
                                             select=None,
                                             expand=None):
    return client.get_resource(user_id=user_id,
                               shared_insight_id=shared_insight_id,
                               select=select,
                               expand=expand)


def people_user_insight_trending_delete(client,
                                        user_id,
                                        trending_id,
                                        if_match=None):
    return client.delete_ref_resource(user_id=user_id,
                                      trending_id=trending_id,
                                      if_match=if_match)


def people_user_insight_trending_set_ref_resource(client,
                                                  user_id,
                                                  trending_id,
                                                  body):
    return client.set_ref_resource(user_id=user_id,
                                   trending_id=trending_id,
                                   body=body)


def people_user_insight_trending_show_ref_resource(client,
                                                   user_id,
                                                   trending_id):
    return client.get_ref_resource(user_id=user_id,
                                   trending_id=trending_id)


def people_user_insight_trending_show_resource(client,
                                               user_id,
                                               trending_id,
                                               select=None,
                                               expand=None):
    return client.get_resource(user_id=user_id,
                               trending_id=trending_id,
                               select=select,
                               expand=expand)


def people_user_insight_used_delete(client,
                                    user_id,
                                    used_insight_id,
                                    if_match=None):
    return client.delete_ref_resource(user_id=user_id,
                                      used_insight_id=used_insight_id,
                                      if_match=if_match)


def people_user_insight_used_set_ref_resource(client,
                                              user_id,
                                              used_insight_id,
                                              body):
    return client.set_ref_resource(user_id=user_id,
                                   used_insight_id=used_insight_id,
                                   body=body)


def people_user_insight_used_show_ref_resource(client,
                                               user_id,
                                               used_insight_id):
    return client.get_ref_resource(user_id=user_id,
                                   used_insight_id=used_insight_id)


def people_user_insight_used_show_resource(client,
                                           user_id,
                                           used_insight_id,
                                           select=None,
                                           expand=None):
    return client.get_resource(user_id=user_id,
                               used_insight_id=used_insight_id,
                               select=select,
                               expand=expand)
