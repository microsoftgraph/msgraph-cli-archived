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


def security_security_create(client,
                             id_=None,
                             alerts=None,
                             secure_score_control_profiles=None,
                             secure_scores=None):
    body = {}
    body['id'] = id_
    body['alerts'] = alerts
    body['secure_score_control_profiles'] = secure_score_control_profiles
    body['secure_scores'] = secure_scores
    return client.update_security(body=body)


def security_security_show_security(client,
                                    select=None,
                                    expand=None):
    return client.get_security(select=select,
                               expand=expand)


def security_create_alert(client,
                          id_=None,
                          activity_group_name=None,
                          assigned_to=None,
                          azure_subscription_id=None,
                          azure_tenant_id=None,
                          category=None,
                          closed_date_time=None,
                          cloud_app_states=None,
                          comments=None,
                          confidence=None,
                          created_date_time=None,
                          description=None,
                          detection_ids=None,
                          event_date_time=None,
                          feedback=None,
                          file_states=None,
                          history_states=None,
                          host_states=None,
                          incident_ids=None,
                          last_modified_date_time=None,
                          malware_states=None,
                          network_connections=None,
                          processes=None,
                          recommended_actions=None,
                          registry_key_states=None,
                          security_resources=None,
                          severity=None,
                          source_materials=None,
                          status=None,
                          tags=None,
                          title=None,
                          triggers=None,
                          user_states=None,
                          vendor_information=None,
                          vulnerability_states=None):
    body = {}
    body['id'] = id_
    body['activity_group_name'] = activity_group_name
    body['assigned_to'] = assigned_to
    body['azure_subscription_id'] = azure_subscription_id
    body['azure_tenant_id'] = azure_tenant_id
    body['category'] = category
    body['closed_date_time'] = closed_date_time
    body['cloud_app_states'] = cloud_app_states
    body['comments'] = comments
    body['confidence'] = confidence
    body['created_date_time'] = created_date_time
    body['description'] = description
    body['detection_ids'] = detection_ids
    body['event_date_time'] = event_date_time
    body['feedback'] = feedback
    body['file_states'] = file_states
    body['history_states'] = history_states
    body['host_states'] = host_states
    body['incident_ids'] = incident_ids
    body['last_modified_date_time'] = last_modified_date_time
    body['malware_states'] = malware_states
    body['network_connections'] = network_connections
    body['processes'] = processes
    body['recommended_actions'] = recommended_actions
    body['registry_key_states'] = registry_key_states
    body['security_resources'] = security_resources
    body['severity'] = severity
    body['source_materials'] = source_materials
    body['status'] = status
    body['tags'] = tags
    body['title'] = title
    body['triggers'] = triggers
    body['user_states'] = user_states
    body['vendor_information'] = vendor_information
    body['vulnerability_states'] = vulnerability_states
    return client.create_alerts(body=body)


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
    body = {}
    body['id'] = id_
    body['active_user_count'] = active_user_count
    body['average_comparative_scores'] = average_comparative_scores
    body['azure_tenant_id'] = azure_tenant_id
    body['control_scores'] = control_scores
    body['created_date_time'] = created_date_time
    body['current_score'] = current_score
    body['enabled_services'] = enabled_services
    body['licensed_user_count'] = licensed_user_count
    body['max_score'] = max_score
    body['vendor_information'] = vendor_information
    return client.create_secure_scores(body=body)


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
    body = {}
    body['id'] = id_
    body['action_type'] = action_type
    body['action_url'] = action_url
    body['azure_tenant_id'] = azure_tenant_id
    body['compliance_information'] = compliance_information
    body['control_category'] = control_category
    body['control_state_updates'] = control_state_updates
    body['deprecated'] = deprecated
    body['implementation_cost'] = implementation_cost
    body['last_modified_date_time'] = last_modified_date_time
    body['max_score'] = max_score
    body['rank'] = rank
    body['remediation'] = remediation
    body['remediation_impact'] = remediation_impact
    body['service'] = service
    body['threats'] = threats
    body['tier'] = tier
    body['title'] = title
    body['user_impact'] = user_impact
    body['vendor_information'] = vendor_information
    return client.create_secure_score_control_profiles(body=body)


def security_delete_alert(client,
                          alert_id,
                          if_match=None):
    return client.delete_alerts(alert_id=alert_id,
                                if_match=if_match)


def security_delete_secure_score(client,
                                 secure_score_id,
                                 if_match=None):
    return client.delete_secure_scores(secure_score_id=secure_score_id,
                                       if_match=if_match)


def security_delete_secure_score_control_profile(client,
                                                 secure_score_control_profile_id,
                                                 if_match=None):
    return client.delete_secure_score_control_profiles(secure_score_control_profile_id=secure_score_control_profile_id,
                                                       if_match=if_match)


def security_list_alert(client,
                        orderby=None,
                        select=None,
                        expand=None):
    return client.list_alerts(orderby=orderby,
                              select=select,
                              expand=expand)


def security_list_secure_score(client,
                               orderby=None,
                               select=None,
                               expand=None):
    return client.list_secure_scores(orderby=orderby,
                                     select=select,
                                     expand=expand)


def security_list_secure_score_control_profile(client,
                                               orderby=None,
                                               select=None,
                                               expand=None):
    return client.list_secure_score_control_profiles(orderby=orderby,
                                                     select=select,
                                                     expand=expand)


def security_show_alert(client,
                        alert_id,
                        select=None,
                        expand=None):
    return client.get_alerts(alert_id=alert_id,
                             select=select,
                             expand=expand)


def security_show_secure_score(client,
                               secure_score_id,
                               select=None,
                               expand=None):
    return client.get_secure_scores(secure_score_id=secure_score_id,
                                    select=select,
                                    expand=expand)


def security_show_secure_score_control_profile(client,
                                               secure_score_control_profile_id,
                                               select=None,
                                               expand=None):
    return client.get_secure_score_control_profiles(secure_score_control_profile_id=secure_score_control_profile_id,
                                                    select=select,
                                                    expand=expand)


def security_update_alert(client,
                          alert_id,
                          id_=None,
                          activity_group_name=None,
                          assigned_to=None,
                          azure_subscription_id=None,
                          azure_tenant_id=None,
                          category=None,
                          closed_date_time=None,
                          cloud_app_states=None,
                          comments=None,
                          confidence=None,
                          created_date_time=None,
                          description=None,
                          detection_ids=None,
                          event_date_time=None,
                          feedback=None,
                          file_states=None,
                          history_states=None,
                          host_states=None,
                          incident_ids=None,
                          last_modified_date_time=None,
                          malware_states=None,
                          network_connections=None,
                          processes=None,
                          recommended_actions=None,
                          registry_key_states=None,
                          security_resources=None,
                          severity=None,
                          source_materials=None,
                          status=None,
                          tags=None,
                          title=None,
                          triggers=None,
                          user_states=None,
                          vendor_information=None,
                          vulnerability_states=None):
    body = {}
    body['id'] = id_
    body['activity_group_name'] = activity_group_name
    body['assigned_to'] = assigned_to
    body['azure_subscription_id'] = azure_subscription_id
    body['azure_tenant_id'] = azure_tenant_id
    body['category'] = category
    body['closed_date_time'] = closed_date_time
    body['cloud_app_states'] = cloud_app_states
    body['comments'] = comments
    body['confidence'] = confidence
    body['created_date_time'] = created_date_time
    body['description'] = description
    body['detection_ids'] = detection_ids
    body['event_date_time'] = event_date_time
    body['feedback'] = feedback
    body['file_states'] = file_states
    body['history_states'] = history_states
    body['host_states'] = host_states
    body['incident_ids'] = incident_ids
    body['last_modified_date_time'] = last_modified_date_time
    body['malware_states'] = malware_states
    body['network_connections'] = network_connections
    body['processes'] = processes
    body['recommended_actions'] = recommended_actions
    body['registry_key_states'] = registry_key_states
    body['security_resources'] = security_resources
    body['severity'] = severity
    body['source_materials'] = source_materials
    body['status'] = status
    body['tags'] = tags
    body['title'] = title
    body['triggers'] = triggers
    body['user_states'] = user_states
    body['vendor_information'] = vendor_information
    body['vulnerability_states'] = vulnerability_states
    return client.update_alerts(alert_id=alert_id,
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
    body = {}
    body['id'] = id_
    body['active_user_count'] = active_user_count
    body['average_comparative_scores'] = average_comparative_scores
    body['azure_tenant_id'] = azure_tenant_id
    body['control_scores'] = control_scores
    body['created_date_time'] = created_date_time
    body['current_score'] = current_score
    body['enabled_services'] = enabled_services
    body['licensed_user_count'] = licensed_user_count
    body['max_score'] = max_score
    body['vendor_information'] = vendor_information
    return client.update_secure_scores(secure_score_id=secure_score_id,
                                       body=body)


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
    body = {}
    body['id'] = id_
    body['action_type'] = action_type
    body['action_url'] = action_url
    body['azure_tenant_id'] = azure_tenant_id
    body['compliance_information'] = compliance_information
    body['control_category'] = control_category
    body['control_state_updates'] = control_state_updates
    body['deprecated'] = deprecated
    body['implementation_cost'] = implementation_cost
    body['last_modified_date_time'] = last_modified_date_time
    body['max_score'] = max_score
    body['rank'] = rank
    body['remediation'] = remediation
    body['remediation_impact'] = remediation_impact
    body['service'] = service
    body['threats'] = threats
    body['tier'] = tier
    body['title'] = title
    body['user_impact'] = user_impact
    body['vendor_information'] = vendor_information
    return client.update_secure_score_control_profiles(secure_score_control_profile_id=secure_score_control_profile_id,
                                                       body=body)