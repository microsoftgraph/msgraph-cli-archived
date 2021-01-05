# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines


def security_get_security(client,
                          select=None,
                          expand=None):
    return client.get_security(select=select,
                               expand=expand)


def security_update_security(client,
                             id_=None,
                             alerts=None,
                             secure_score_control_profiles=None,
                             secure_scores=None):
    return client.update_security(id=id_,
                                  alerts=alerts,
                                  secure_score_control_profiles=secure_score_control_profiles,
                                  secure_scores=secure_scores)


def security_delete(client,
                    alert_id=None,
                    if_match=None,
                    secure_score_control_profile_id=None,
                    secure_score_id=None):
    if alert_id is not None:
        return client.delete_alert(alert_id=alert_id,
                                   if_match=if_match)
    elif secure_score_control_profile_id is not None:
        return client.delete_secure_score_control_profile(secure_score_control_profile_id=secure_score_control_profile_id,
                                                          if_match=if_match)
    return client.delete_secure_score(secure_score_id=secure_score_id,
                                      if_match=if_match)


def security_create_alert(client,
                          body):
    return client.create_alert(body=body)


def security_create_secure_score(client,
                                 id_=None,
                                 active_user_count=None,
                                 average_comparative_scores=None,
                                 azure_tenant_id=None,
                                 control_scores=None,
                                 created_date_time=None,
                                 current_score=None,
                                 enabled_services=None,
                                 licensed_user_count=None,
                                 max_score=None,
                                 vendor_information=None):
    return client.create_secure_score(id=id_,
                                      active_user_count=active_user_count,
                                      average_comparative_scores=average_comparative_scores,
                                      azure_tenant_id=azure_tenant_id,
                                      control_scores=control_scores,
                                      created_date_time=created_date_time,
                                      current_score=current_score,
                                      enabled_services=enabled_services,
                                      licensed_user_count=licensed_user_count,
                                      max_score=max_score,
                                      vendor_information=vendor_information)


def security_create_secure_score_control_profile(client,
                                                 id_=None,
                                                 action_type=None,
                                                 action_url=None,
                                                 azure_tenant_id=None,
                                                 compliance_information=None,
                                                 control_category=None,
                                                 control_state_updates=None,
                                                 deprecated=None,
                                                 implementation_cost=None,
                                                 last_modified_date_time=None,
                                                 max_score=None,
                                                 rank=None,
                                                 remediation=None,
                                                 remediation_impact=None,
                                                 service=None,
                                                 threats=None,
                                                 tier=None,
                                                 title=None,
                                                 user_impact=None,
                                                 vendor_information=None):
    return client.create_secure_score_control_profile(id=id_,
                                                      action_type=action_type,
                                                      action_url=action_url,
                                                      azure_tenant_id=azure_tenant_id,
                                                      compliance_information=compliance_information,
                                                      control_category=control_category,
                                                      control_state_updates=control_state_updates,
                                                      deprecated=deprecated,
                                                      implementation_cost=implementation_cost,
                                                      last_modified_date_time=last_modified_date_time,
                                                      max_score=max_score,
                                                      rank=rank,
                                                      remediation=remediation,
                                                      remediation_impact=remediation_impact,
                                                      service=service,
                                                      threats=threats,
                                                      tier=tier,
                                                      title=title,
                                                      user_impact=user_impact,
                                                      vendor_information=vendor_information)


def security_get_alert(client,
                       alert_id,
                       select=None,
                       expand=None):
    return client.get_alert(alert_id=alert_id,
                            select=select,
                            expand=expand)


def security_get_secure_score(client,
                              secure_score_id,
                              select=None,
                              expand=None):
    return client.get_secure_score(secure_score_id=secure_score_id,
                                   select=select,
                                   expand=expand)


def security_get_secure_score_control_profile(client,
                                              secure_score_control_profile_id,
                                              select=None,
                                              expand=None):
    return client.get_secure_score_control_profile(secure_score_control_profile_id=secure_score_control_profile_id,
                                                   select=select,
                                                   expand=expand)


def security_list_alert(client,
                        orderby=None,
                        select=None,
                        expand=None):
    return client.list_alert(orderby=orderby,
                             select=select,
                             expand=expand)


def security_list_secure_score(client,
                               orderby=None,
                               select=None,
                               expand=None):
    return client.list_secure_score(orderby=orderby,
                                    select=select,
                                    expand=expand)


def security_list_secure_score_control_profile(client,
                                               orderby=None,
                                               select=None,
                                               expand=None):
    return client.list_secure_score_control_profile(orderby=orderby,
                                                    select=select,
                                                    expand=expand)


def security_update_alert(client,
                          alert_id,
                          body):
    return client.update_alert(alert_id=alert_id,
                               body=body)


def security_update_secure_score(client,
                                 secure_score_id,
                                 id_=None,
                                 active_user_count=None,
                                 average_comparative_scores=None,
                                 azure_tenant_id=None,
                                 control_scores=None,
                                 created_date_time=None,
                                 current_score=None,
                                 enabled_services=None,
                                 licensed_user_count=None,
                                 max_score=None,
                                 vendor_information=None):
    return client.update_secure_score(secure_score_id=secure_score_id,
                                      id=id_,
                                      active_user_count=active_user_count,
                                      average_comparative_scores=average_comparative_scores,
                                      azure_tenant_id=azure_tenant_id,
                                      control_scores=control_scores,
                                      created_date_time=created_date_time,
                                      current_score=current_score,
                                      enabled_services=enabled_services,
                                      licensed_user_count=licensed_user_count,
                                      max_score=max_score,
                                      vendor_information=vendor_information)


def security_update_secure_score_control_profile(client,
                                                 secure_score_control_profile_id,
                                                 id_=None,
                                                 action_type=None,
                                                 action_url=None,
                                                 azure_tenant_id=None,
                                                 compliance_information=None,
                                                 control_category=None,
                                                 control_state_updates=None,
                                                 deprecated=None,
                                                 implementation_cost=None,
                                                 last_modified_date_time=None,
                                                 max_score=None,
                                                 rank=None,
                                                 remediation=None,
                                                 remediation_impact=None,
                                                 service=None,
                                                 threats=None,
                                                 tier=None,
                                                 title=None,
                                                 user_impact=None,
                                                 vendor_information=None):
    return client.update_secure_score_control_profile(secure_score_control_profile_id=secure_score_control_profile_id,
                                                      id=id_,
                                                      action_type=action_type,
                                                      action_url=action_url,
                                                      azure_tenant_id=azure_tenant_id,
                                                      compliance_information=compliance_information,
                                                      control_category=control_category,
                                                      control_state_updates=control_state_updates,
                                                      deprecated=deprecated,
                                                      implementation_cost=implementation_cost,
                                                      last_modified_date_time=last_modified_date_time,
                                                      max_score=max_score,
                                                      rank=rank,
                                                      remediation=remediation,
                                                      remediation_impact=remediation_impact,
                                                      service=service,
                                                      threats=threats,
                                                      tier=tier,
                                                      title=title,
                                                      user_impact=user_impact,
                                                      vendor_information=vendor_information)