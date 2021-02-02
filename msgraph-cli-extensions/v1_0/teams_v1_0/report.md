# Azure CLI Module Creation Report

### teams chat get-all-message

get-all-message a teams chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams chat|chats|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-all-message|getAllMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### teams chat-chat create-chat

create-chat a teams chat-chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams chat-chat|chats.chat|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-chat|CreateChat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|

### teams chat-chat delete

delete a teams chat-chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams chat-chat|chats.chat|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteChat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--if-match**|string|ETag|if_match|If-Match|

### teams chat-chat get-chat

get-chat a teams chat-chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams chat-chat|chats.chat|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-chat|GetChat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams chat-chat list-chat

list-chat a teams chat-chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams chat-chat|chats.chat|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-chat|ListChat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams chat-chat update-chat

update-chat a teams chat-chat.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams chat-chat|chats.chat|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-chat|UpdateChat|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--id**|string|Read-only.|id|id|

### teams group delete

delete a teams group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteTeam|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--if-match**|string|ETag|if_match|If-Match|

### teams group get

get a teams group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetTeam|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams group update

update a teams group.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams group|groups|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateTeam|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--classification**|string|An optional label. Typically describes the data or business sensitivity of the team. Must match one of a pre-configured set in the tenant's directory.|classification|classification|
|**--description**|string|An optional description for the team.|description|description|
|**--display-name**|string|The name of the team.|display_name|displayName|
|**--fun-settings**|object|teamFunSettings|fun_settings|funSettings|
|**--guest-settings**|object|teamGuestSettings|guest_settings|guestSettings|
|**--internal-id**|string|A unique ID for the team that has been used in a few places such as the audit log/Office 365 Management Activity API.|internal_id|internalId|
|**--is-archived**|boolean|Whether this team is in read-only mode.|is_archived|isArchived|
|**--member-settings**|object|teamMemberSettings|member_settings|memberSettings|
|**--messaging-settings**|object|teamMessagingSettings|messaging_settings|messagingSettings|
|**--specialization**|choice||specialization|specialization|
|**--visibility**|choice||visibility|visibility|
|**--web-url**|string|A hyperlink that will go to the team in the Microsoft Teams client. This is the URL that you get when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.|web_url|webUrl|
|**--channels**|array|The collection of channels & messages associated with the team.|channels|channels|
|**--installed-apps**|array|The apps installed in this team.|installed_apps|installedApps|
|**--members**|array|Members and owners of the team.|members|members|
|**--operations**|array|The async operations that ran or are running on this team.|operations|operations|
|**--primary-channel**|object|channel|primary_channel|primaryChannel|
|**--template-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--id1**|string|Read-only.|id1|id|
|**--group-deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--group-assigned-labels**|array|The list of sensitivity label pairs (label ID, label name) associated with an Microsoft 365 group. Returned only on $select. Read-only.|assigned_labels|assignedLabels|
|**--group-assigned-licenses**|array|The licenses that are assigned to the group. Returned only on $select. Read-only.|assigned_licenses|assignedLicenses|
|**--group-classification**|string|Describes a classification for the group (such as low, medium or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default.|microsoft_graph_group_classification|classification|
|**--group-created-date-time**|date-time|Timestamp of when the group was created. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|created_date_time|createdDateTime|
|**--group-description**|string|An optional description for the group. Returned by default.|microsoft_graph_group_description|description|
|**--group-display-name**|string|The display name for the group. This property is required when a group is created and cannot be cleared during updates. Returned by default. Supports $filter and $orderby.|microsoft_graph_group_display_name|displayName|
|**--group-expiration-date-time**|date-time|Timestamp of when the group is set to expire. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|expiration_date_time|expirationDateTime|
|**--group-group-types**|array|Specifies the group type and its membership.  If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static.  Returned by default. Supports $filter.|group_types|groupTypes|
|**--group-has-members-with-license-errors**|boolean|Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an example.|has_members_with_license_errors|hasMembersWithLicenseErrors|
|**--group-license-processing-state**|object|licenseProcessingState|license_processing_state|licenseProcessingState|
|**--group-mail**|string|The SMTP address for the group, for example, 'serviceadmins@contoso.onmicrosoft.com'. Returned by default. Read-only. Supports $filter.|mail|mail|
|**--group-mail-enabled**|boolean|Specifies whether the group is mail-enabled. Returned by default.|mail_enabled|mailEnabled|
|**--group-mail-nickname**|string|The mail alias for the group, unique in the organization. This property must be specified when a group is created. Returned by default. Supports $filter.|mail_nickname|mailNickname|
|**--group-membership-rule**|string|The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default.|membership_rule|membershipRule|
|**--group-membership-rule-processing-state**|string|Indicates whether the dynamic membership processing is on or paused. Possible values are 'On' or 'Paused'. Returned by default.|membership_rule_processing_state|membershipRuleProcessingState|
|**--group-on-premises-domain-name**|string|Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_domain_name|onPremisesDomainName|
|**--group-on-premises-last-sync-date-time**|date-time|Indicates the last time at which the group was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only. Supports $filter.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--group-on-premises-net-bios-name**|string|Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_net_bios_name|onPremisesNetBiosName|
|**--group-on-premises-provisioning-errors**|array|Errors when using Microsoft synchronization product during provisioning. Returned by default.|on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--group-on-premises-sam-account-name**|string|Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_sam_account_name|onPremisesSamAccountName|
|**--group-on-premises-security-identifier**|string|Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Returned by default. Read-only.|on_premises_security_identifier|onPremisesSecurityIdentifier|
|**--group-on-premises-sync-enabled**|boolean|true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--group-preferred-data-location**|string|The preferred data location for the group. For more information, see  OneDrive Online Multi-Geo. Returned by default.|preferred_data_location|preferredDataLocation|
|**--group-preferred-language**|string|The preferred language for an Microsoft 365 group. Should follow ISO 639-1 Code; for example 'en-US'. Returned by default.|preferred_language|preferredLanguage|
|**--group-proxy-addresses**|array|Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter.|proxy_addresses|proxyAddresses|
|**--group-renewed-date-time**|date-time|Timestamp of when the group was last renewed. This cannot be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|renewed_date_time|renewedDateTime|
|**--group-security-enabled**|boolean|Specifies whether the group is a security group. Returned by default. Supports $filter.|security_enabled|securityEnabled|
|**--group-security-identifier**|string|Security identifier of the group, used in Windows scenarios. Returned by default.|security_identifier|securityIdentifier|
|**--group-theme**|string|Specifies an Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange or Red. Returned by default.|theme|theme|
|**--group-visibility**|string|Specifies the visibility of a Microsoft 365 group. Possible values are: Private, Public, or Hiddenmembership; blank values are treated as public.  See group visibility options to learn more.Visibility can be set only when a group is created; it is not editable.Visibility is supported only for unified groups; it is not supported for security groups. Returned by default.|microsoft_graph_group_visibility|visibility|
|**--group-allow-external-senders**|boolean|Indicates if people external to the organization can send messages to the group. Default value is false. Returned only on $select.|allow_external_senders|allowExternalSenders|
|**--group-auto-subscribe-new-members**|boolean|Indicates if new members added to the group will be auto-subscribed to receive email notifications. You can set this property in a PATCH request for the group; do not set it in the initial POST request that creates the group. Default value is false. Returned only on $select.|auto_subscribe_new_members|autoSubscribeNewMembers|
|**--group-hide-from-address-lists**|boolean|True if the group is not displayed in certain parts of the Outlook UI: the Address Book, address lists for selecting message recipients, and the Browse Groups dialog for searching groups; otherwise, false. Default value is false. Returned only on $select.|hide_from_address_lists|hideFromAddressLists|
|**--group-hide-from-outlook-clients**|boolean|True if the group is not displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. Default value is false. Returned only on $select.|hide_from_outlook_clients|hideFromOutlookClients|
|**--group-is-subscribed-by-mail**|boolean|Indicates whether the signed-in user is subscribed to receive email conversations. Default value is true. Returned only on $select.|is_subscribed_by_mail|isSubscribedByMail|
|**--group-unseen-count**|integer|Count of conversations that have received new posts since the signed-in user last visited the group. Returned only on $select.|unseen_count|unseenCount|
|**--group-is-archived**|boolean||is_archived|isArchived|
|**--group-app-role-assignments**|array||app_role_assignments|appRoleAssignments|
|**--group-created-on-behalf-of**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|created_on_behalf_of|createdOnBehalfOf|
|**--group-member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--group-members**|array|Users and groups that are members of this group. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups) Nullable.|microsoft_graph_group_members|members|
|**--group-members-with-license-errors**|array|A list of group members with license errors from this group-based license assignment. Read-only.|members_with_license_errors|membersWithLicenseErrors|
|**--group-owners**|array|The owners of the group. The owners are a set of non-admin users who are allowed to modify this object. Limited to 100 owners. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups). Nullable.|owners|owners|
|**--group-settings**|array|Read-only. Nullable.|settings|settings|
|**--group-transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--group-transitive-members**|array||transitive_members|transitiveMembers|
|**--group-accepted-senders**|array|The list of users or groups that are allowed to create post's or calendar events in this group. If this list is non-empty then only users or groups listed here are allowed to post.|accepted_senders|acceptedSenders|
|**--group-calendar**|object|calendar|calendar|calendar|
|**--group-calendar-view**|array|The calendar view for the calendar. Read-only.|calendar_view|calendarView|
|**--group-conversations**|array|The group's conversations.|conversations|conversations|
|**--group-events**|array|The group's calendar events.|events|events|
|**--group-photo**|object|profilePhoto|photo|photo|
|**--group-photos**|array|The profile photos owned by the group. Read-only. Nullable.|photos|photos|
|**--group-rejected-senders**|array|The list of users or groups that are not allowed to create posts or calendar events in this group. Nullable|rejected_senders|rejectedSenders|
|**--group-threads**|array|The group's conversation threads. Nullable.|threads|threads|
|**--group-drive**|object|drive|drive|drive|
|**--group-drives**|array|The group's drives. Read-only.|drives|drives|
|**--group-sites**|array|The list of SharePoint sites in this group. Access the default site with /sites/root.|sites|sites|
|**--group-extensions**|array|The collection of open extensions defined for the group. Read-only. Nullable.|extensions|extensions|
|**--group-group-lifecycle-policies**|array|The collection of lifecycle policies for this group. Read-only. Nullable.|group_lifecycle_policies|groupLifecyclePolicies|
|**--group-planner**|object|plannerGroup|planner|planner|
|**--group-onenote**|object|onenote|onenote|onenote|
|**--group-team**|object|team|team|team|
|**--schedule-id**|string|Read-only.|id2|id|
|**--schedule-enabled**|boolean|Indicates whether the schedule is enabled for the team. Required.|enabled|enabled|
|**--schedule-offer-shift-requests-enabled**|boolean|Indicates whether offer shift requests are enabled for the schedule.|offer_shift_requests_enabled|offerShiftRequestsEnabled|
|**--schedule-open-shifts-enabled**|boolean|Indicates whether open shifts are enabled for the schedule.|open_shifts_enabled|openShiftsEnabled|
|**--schedule-provision-status**|choice||provision_status|provisionStatus|
|**--schedule-provision-status-code**|string|Additional information about why schedule provisioning failed.|provision_status_code|provisionStatusCode|
|**--schedule-swap-shifts-requests-enabled**|boolean|Indicates whether swap shifts requests are enabled for the schedule.|swap_shifts_requests_enabled|swapShiftsRequestsEnabled|
|**--schedule-time-clock-enabled**|boolean|Indicates whether time clock is enabled for the schedule.|time_clock_enabled|timeClockEnabled|
|**--schedule-time-off-requests-enabled**|boolean|Indicates whether time off requests are enabled for the schedule.|time_off_requests_enabled|timeOffRequestsEnabled|
|**--schedule-time-zone**|string|Indicates the time zone of the schedule team using tz database format. Required.|time_zone|timeZone|
|**--schedule-workforce-integration-ids**|array||workforce_integration_ids|workforceIntegrationIds|
|**--schedule-offer-shift-requests**|array||offer_shift_requests|offerShiftRequests|
|**--schedule-open-shift-change-requests**|array||open_shift_change_requests|openShiftChangeRequests|
|**--schedule-open-shifts**|array||open_shifts|openShifts|
|**--schedule-scheduling-groups**|array|The logical grouping of users in the schedule (usually by role).|scheduling_groups|schedulingGroups|
|**--schedule-shifts**|array|The shifts in the schedule.|shifts|shifts|
|**--schedule-swap-shifts-change-requests**|array||swap_shifts_change_requests|swapShiftsChangeRequests|
|**--schedule-time-off-reasons**|array|The set of reasons for a time off in the schedule.|time_off_reasons|timeOffReasons|
|**--schedule-time-off-requests**|array||time_off_requests|timeOffRequests|
|**--schedule-times-off**|array|The instances of times off in the schedule.|times_off|timesOff|

### teams team archive

archive a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|archive|archive|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--should-set-spo-site-read-only-for-members**|boolean||should_set_spo_site_read_only_for_members|shouldSetSpoSiteReadOnlyForMembers|

### teams team clone

clone a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|clone|clone|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--display-name**|string||display_name|displayName|
|**--description**|string||description|description|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--classification**|string||classification|classification|
|**--visibility**|choice||visibility|visibility|
|**--parts-to-clone**|choice||parts_to_clone|partsToClone|

### teams team create

create a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams.team|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|CreateTeam|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--classification**|string|An optional label. Typically describes the data or business sensitivity of the team. Must match one of a pre-configured set in the tenant's directory.|classification|classification|
|**--description**|string|An optional description for the team.|description|description|
|**--display-name**|string|The name of the team.|display_name|displayName|
|**--fun-settings**|object|teamFunSettings|fun_settings|funSettings|
|**--guest-settings**|object|teamGuestSettings|guest_settings|guestSettings|
|**--internal-id**|string|A unique ID for the team that has been used in a few places such as the audit log/Office 365 Management Activity API.|internal_id|internalId|
|**--is-archived**|boolean|Whether this team is in read-only mode.|is_archived|isArchived|
|**--member-settings**|object|teamMemberSettings|member_settings|memberSettings|
|**--messaging-settings**|object|teamMessagingSettings|messaging_settings|messagingSettings|
|**--specialization**|choice||specialization|specialization|
|**--visibility**|choice||visibility|visibility|
|**--web-url**|string|A hyperlink that will go to the team in the Microsoft Teams client. This is the URL that you get when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.|web_url|webUrl|
|**--channels**|array|The collection of channels & messages associated with the team.|channels|channels|
|**--installed-apps**|array|The apps installed in this team.|installed_apps|installedApps|
|**--members**|array|Members and owners of the team.|members|members|
|**--operations**|array|The async operations that ran or are running on this team.|operations|operations|
|**--primary-channel**|object|channel|primary_channel|primaryChannel|
|**--template-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--group-id**|string|Read-only.|id1|id|
|**--group-deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--group-assigned-labels**|array|The list of sensitivity label pairs (label ID, label name) associated with an Microsoft 365 group. Returned only on $select. Read-only.|assigned_labels|assignedLabels|
|**--group-assigned-licenses**|array|The licenses that are assigned to the group. Returned only on $select. Read-only.|assigned_licenses|assignedLicenses|
|**--group-classification**|string|Describes a classification for the group (such as low, medium or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default.|microsoft_graph_group_classification|classification|
|**--group-created-date-time**|date-time|Timestamp of when the group was created. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|created_date_time|createdDateTime|
|**--group-description**|string|An optional description for the group. Returned by default.|microsoft_graph_group_description|description|
|**--group-display-name**|string|The display name for the group. This property is required when a group is created and cannot be cleared during updates. Returned by default. Supports $filter and $orderby.|microsoft_graph_group_display_name|displayName|
|**--group-expiration-date-time**|date-time|Timestamp of when the group is set to expire. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|expiration_date_time|expirationDateTime|
|**--group-group-types**|array|Specifies the group type and its membership.  If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static.  Returned by default. Supports $filter.|group_types|groupTypes|
|**--group-has-members-with-license-errors**|boolean|Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an example.|has_members_with_license_errors|hasMembersWithLicenseErrors|
|**--group-license-processing-state**|object|licenseProcessingState|license_processing_state|licenseProcessingState|
|**--group-mail**|string|The SMTP address for the group, for example, 'serviceadmins@contoso.onmicrosoft.com'. Returned by default. Read-only. Supports $filter.|mail|mail|
|**--group-mail-enabled**|boolean|Specifies whether the group is mail-enabled. Returned by default.|mail_enabled|mailEnabled|
|**--group-mail-nickname**|string|The mail alias for the group, unique in the organization. This property must be specified when a group is created. Returned by default. Supports $filter.|mail_nickname|mailNickname|
|**--group-membership-rule**|string|The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default.|membership_rule|membershipRule|
|**--group-membership-rule-processing-state**|string|Indicates whether the dynamic membership processing is on or paused. Possible values are 'On' or 'Paused'. Returned by default.|membership_rule_processing_state|membershipRuleProcessingState|
|**--group-on-premises-domain-name**|string|Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_domain_name|onPremisesDomainName|
|**--group-on-premises-last-sync-date-time**|date-time|Indicates the last time at which the group was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only. Supports $filter.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--group-on-premises-net-bios-name**|string|Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_net_bios_name|onPremisesNetBiosName|
|**--group-on-premises-provisioning-errors**|array|Errors when using Microsoft synchronization product during provisioning. Returned by default.|on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--group-on-premises-sam-account-name**|string|Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_sam_account_name|onPremisesSamAccountName|
|**--group-on-premises-security-identifier**|string|Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Returned by default. Read-only.|on_premises_security_identifier|onPremisesSecurityIdentifier|
|**--group-on-premises-sync-enabled**|boolean|true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--group-preferred-data-location**|string|The preferred data location for the group. For more information, see  OneDrive Online Multi-Geo. Returned by default.|preferred_data_location|preferredDataLocation|
|**--group-preferred-language**|string|The preferred language for an Microsoft 365 group. Should follow ISO 639-1 Code; for example 'en-US'. Returned by default.|preferred_language|preferredLanguage|
|**--group-proxy-addresses**|array|Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter.|proxy_addresses|proxyAddresses|
|**--group-renewed-date-time**|date-time|Timestamp of when the group was last renewed. This cannot be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|renewed_date_time|renewedDateTime|
|**--group-security-enabled**|boolean|Specifies whether the group is a security group. Returned by default. Supports $filter.|security_enabled|securityEnabled|
|**--group-security-identifier**|string|Security identifier of the group, used in Windows scenarios. Returned by default.|security_identifier|securityIdentifier|
|**--group-theme**|string|Specifies an Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange or Red. Returned by default.|theme|theme|
|**--group-visibility**|string|Specifies the visibility of a Microsoft 365 group. Possible values are: Private, Public, or Hiddenmembership; blank values are treated as public.  See group visibility options to learn more.Visibility can be set only when a group is created; it is not editable.Visibility is supported only for unified groups; it is not supported for security groups. Returned by default.|microsoft_graph_group_visibility|visibility|
|**--group-allow-external-senders**|boolean|Indicates if people external to the organization can send messages to the group. Default value is false. Returned only on $select.|allow_external_senders|allowExternalSenders|
|**--group-auto-subscribe-new-members**|boolean|Indicates if new members added to the group will be auto-subscribed to receive email notifications. You can set this property in a PATCH request for the group; do not set it in the initial POST request that creates the group. Default value is false. Returned only on $select.|auto_subscribe_new_members|autoSubscribeNewMembers|
|**--group-hide-from-address-lists**|boolean|True if the group is not displayed in certain parts of the Outlook UI: the Address Book, address lists for selecting message recipients, and the Browse Groups dialog for searching groups; otherwise, false. Default value is false. Returned only on $select.|hide_from_address_lists|hideFromAddressLists|
|**--group-hide-from-outlook-clients**|boolean|True if the group is not displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. Default value is false. Returned only on $select.|hide_from_outlook_clients|hideFromOutlookClients|
|**--group-is-subscribed-by-mail**|boolean|Indicates whether the signed-in user is subscribed to receive email conversations. Default value is true. Returned only on $select.|is_subscribed_by_mail|isSubscribedByMail|
|**--group-unseen-count**|integer|Count of conversations that have received new posts since the signed-in user last visited the group. Returned only on $select.|unseen_count|unseenCount|
|**--group-is-archived**|boolean||is_archived|isArchived|
|**--group-app-role-assignments**|array||app_role_assignments|appRoleAssignments|
|**--group-created-on-behalf-of**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|created_on_behalf_of|createdOnBehalfOf|
|**--group-member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--group-members**|array|Users and groups that are members of this group. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups) Nullable.|microsoft_graph_group_members|members|
|**--group-members-with-license-errors**|array|A list of group members with license errors from this group-based license assignment. Read-only.|members_with_license_errors|membersWithLicenseErrors|
|**--group-owners**|array|The owners of the group. The owners are a set of non-admin users who are allowed to modify this object. Limited to 100 owners. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups). Nullable.|owners|owners|
|**--group-settings**|array|Read-only. Nullable.|settings|settings|
|**--group-transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--group-transitive-members**|array||transitive_members|transitiveMembers|
|**--group-accepted-senders**|array|The list of users or groups that are allowed to create post's or calendar events in this group. If this list is non-empty then only users or groups listed here are allowed to post.|accepted_senders|acceptedSenders|
|**--group-calendar**|object|calendar|calendar|calendar|
|**--group-calendar-view**|array|The calendar view for the calendar. Read-only.|calendar_view|calendarView|
|**--group-conversations**|array|The group's conversations.|conversations|conversations|
|**--group-events**|array|The group's calendar events.|events|events|
|**--group-photo**|object|profilePhoto|photo|photo|
|**--group-photos**|array|The profile photos owned by the group. Read-only. Nullable.|photos|photos|
|**--group-rejected-senders**|array|The list of users or groups that are not allowed to create posts or calendar events in this group. Nullable|rejected_senders|rejectedSenders|
|**--group-threads**|array|The group's conversation threads. Nullable.|threads|threads|
|**--group-drive**|object|drive|drive|drive|
|**--group-drives**|array|The group's drives. Read-only.|drives|drives|
|**--group-sites**|array|The list of SharePoint sites in this group. Access the default site with /sites/root.|sites|sites|
|**--group-extensions**|array|The collection of open extensions defined for the group. Read-only. Nullable.|extensions|extensions|
|**--group-group-lifecycle-policies**|array|The collection of lifecycle policies for this group. Read-only. Nullable.|group_lifecycle_policies|groupLifecyclePolicies|
|**--group-planner**|object|plannerGroup|planner|planner|
|**--group-onenote**|object|onenote|onenote|onenote|
|**--group-team**|object|team|team|team|
|**--schedule-id**|string|Read-only.|id2|id|
|**--schedule-enabled**|boolean|Indicates whether the schedule is enabled for the team. Required.|enabled|enabled|
|**--schedule-offer-shift-requests-enabled**|boolean|Indicates whether offer shift requests are enabled for the schedule.|offer_shift_requests_enabled|offerShiftRequestsEnabled|
|**--schedule-open-shifts-enabled**|boolean|Indicates whether open shifts are enabled for the schedule.|open_shifts_enabled|openShiftsEnabled|
|**--schedule-provision-status**|choice||provision_status|provisionStatus|
|**--schedule-provision-status-code**|string|Additional information about why schedule provisioning failed.|provision_status_code|provisionStatusCode|
|**--schedule-swap-shifts-requests-enabled**|boolean|Indicates whether swap shifts requests are enabled for the schedule.|swap_shifts_requests_enabled|swapShiftsRequestsEnabled|
|**--schedule-time-clock-enabled**|boolean|Indicates whether time clock is enabled for the schedule.|time_clock_enabled|timeClockEnabled|
|**--schedule-time-off-requests-enabled**|boolean|Indicates whether time off requests are enabled for the schedule.|time_off_requests_enabled|timeOffRequestsEnabled|
|**--schedule-time-zone**|string|Indicates the time zone of the schedule team using tz database format. Required.|time_zone|timeZone|
|**--schedule-workforce-integration-ids**|array||workforce_integration_ids|workforceIntegrationIds|
|**--schedule-offer-shift-requests**|array||offer_shift_requests|offerShiftRequests|
|**--schedule-open-shift-change-requests**|array||open_shift_change_requests|openShiftChangeRequests|
|**--schedule-open-shifts**|array||open_shifts|openShifts|
|**--schedule-scheduling-groups**|array|The logical grouping of users in the schedule (usually by role).|scheduling_groups|schedulingGroups|
|**--schedule-shifts**|array|The shifts in the schedule.|shifts|shifts|
|**--schedule-swap-shifts-change-requests**|array||swap_shifts_change_requests|swapShiftsChangeRequests|
|**--schedule-time-off-reasons**|array|The set of reasons for a time off in the schedule.|time_off_reasons|timeOffReasons|
|**--schedule-time-off-requests**|array||time_off_requests|timeOffRequests|
|**--schedule-times-off**|array|The instances of times off in the schedule.|times_off|timesOff|

### teams team create-channel

create-channel a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-channel|CreateChannels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string|Optional textual description for the channel.|description|description|
|**--display-name**|string|Channel name as it will appear to the user in Microsoft Teams.|display_name|displayName|
|**--email**|string|The email address for sending messages to the channel. Read-only.|email|email|
|**--membership-type**|choice||membership_type|membershipType|
|**--web-url**|string|A hyperlink that will navigate to the channel in Microsoft Teams. This is the URL that you get when you right-click a channel in Microsoft Teams and select Get link to channel. This URL should be treated as an opaque blob, and not parsed. Read-only.|web_url|webUrl|
|**--files-folder**|object|driveItem|files_folder|filesFolder|
|**--members**|array||members|members|
|**--messages**|array|A collection of all the messages in the channel. A navigation property. Nullable.|messages|messages|
|**--tabs**|array|A collection of all the tabs in the channel. A navigation property.|tabs|tabs|

### teams team create-installed-app

create-installed-app a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-installed-app|CreateInstalledApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--teams-app-definition**|object|teamsAppDefinition|teams_app_definition|teamsAppDefinition|
|**--teams-app-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|display_name|displayName|
|**--teams-app-distribution-method**|choice||distribution_method|distributionMethod|
|**--teams-app-external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--teams-app-app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

### teams team create-member

create-member a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-member|CreateMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

### teams team create-operation

create-operation a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-operation|CreateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--attempts-count**|integer|Number of times the operation was attempted before being marked successful or failed.|attempts_count|attemptsCount|
|**--created-date-time**|date-time|Time when the operation was created.|created_date_time|createdDateTime|
|**--error**|object|operationError|error|error|
|**--last-action-date-time**|date-time|Time when the async operation was last updated.|last_action_date_time|lastActionDateTime|
|**--operation-type**|choice||operation_type|operationType|
|**--status**|choice||status|status|
|**--target-resource-id**|string|The ID of the object that's created or modified as result of this async operation, typically a team.|target_resource_id|targetResourceId|
|**--target-resource-location**|string|The location of the object that's created or modified as result of this async operation. This URL should be treated as an opaque value and not parsed into its component paths.|target_resource_location|targetResourceLocation|

### teams team delete

delete a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteChannels|
|delete|DeleteInstalledApps|
|delete|DeleteMembers|
|delete|DeleteOperations|
|delete|DeleteRefGroup|
|delete|DeletePrimaryChannel|
|delete|DeleteSchedule|
|delete|DeleteRefTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--teams-async-operation-id**|string|key: id of teamsAsyncOperation|teams_async_operation_id|teamsAsyncOperation-id|
|**--if-match**|string|ETag|if_match|If-Match|

### teams team get

get a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams.team|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get|GetTeam|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team get-all-message

get-all-message a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-all-message|getAllMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

### teams team get-channel

get-channel a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-channel|GetChannels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team get-group

get-group a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-group|GetGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team get-installed-app

get-installed-app a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-installed-app|GetInstalledApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team get-member

get-member a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member|GetMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team get-operation

get-operation a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-operation|GetOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-async-operation-id**|string|key: id of teamsAsyncOperation|teams_async_operation_id|teamsAsyncOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team get-primary-channel

get-primary-channel a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-primary-channel|GetPrimaryChannel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team get-ref-group

get-ref-group a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-group|GetRefGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|

### teams team get-ref-template

get-ref-template a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-template|GetRefTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|

### teams team get-schedule

get-schedule a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-schedule|GetSchedule|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team get-template

get-template a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-template|GetTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team list

list a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams.team|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list|ListTeam|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team list-channel

list-channel a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-channel|ListChannels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team list-installed-app

list-installed-app a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-installed-app|ListInstalledApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team list-member

list-member a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member|ListMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team list-operation

list-operation a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-operation|ListOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team set-ref-group

set-ref-group a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-group|SetRefGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### teams team set-ref-template

set-ref-template a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-template|SetRefTemplate|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### teams team unarchive

unarchive a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|unarchive|unarchive|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|

### teams team update

update a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams.team|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update|UpdateTeam|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--classification**|string|An optional label. Typically describes the data or business sensitivity of the team. Must match one of a pre-configured set in the tenant's directory.|classification|classification|
|**--description**|string|An optional description for the team.|description|description|
|**--display-name**|string|The name of the team.|display_name|displayName|
|**--fun-settings**|object|teamFunSettings|fun_settings|funSettings|
|**--guest-settings**|object|teamGuestSettings|guest_settings|guestSettings|
|**--internal-id**|string|A unique ID for the team that has been used in a few places such as the audit log/Office 365 Management Activity API.|internal_id|internalId|
|**--is-archived**|boolean|Whether this team is in read-only mode.|is_archived|isArchived|
|**--member-settings**|object|teamMemberSettings|member_settings|memberSettings|
|**--messaging-settings**|object|teamMessagingSettings|messaging_settings|messagingSettings|
|**--specialization**|choice||specialization|specialization|
|**--visibility**|choice||visibility|visibility|
|**--web-url**|string|A hyperlink that will go to the team in the Microsoft Teams client. This is the URL that you get when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.|web_url|webUrl|
|**--channels**|array|The collection of channels & messages associated with the team.|channels|channels|
|**--installed-apps**|array|The apps installed in this team.|installed_apps|installedApps|
|**--members**|array|Members and owners of the team.|members|members|
|**--operations**|array|The async operations that ran or are running on this team.|operations|operations|
|**--primary-channel**|object|channel|primary_channel|primaryChannel|
|**--template-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--group-id**|string|Read-only.|id1|id|
|**--group-deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--group-assigned-labels**|array|The list of sensitivity label pairs (label ID, label name) associated with an Microsoft 365 group. Returned only on $select. Read-only.|assigned_labels|assignedLabels|
|**--group-assigned-licenses**|array|The licenses that are assigned to the group. Returned only on $select. Read-only.|assigned_licenses|assignedLicenses|
|**--group-classification**|string|Describes a classification for the group (such as low, medium or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default.|microsoft_graph_group_classification|classification|
|**--group-created-date-time**|date-time|Timestamp of when the group was created. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|created_date_time|createdDateTime|
|**--group-description**|string|An optional description for the group. Returned by default.|microsoft_graph_group_description|description|
|**--group-display-name**|string|The display name for the group. This property is required when a group is created and cannot be cleared during updates. Returned by default. Supports $filter and $orderby.|microsoft_graph_group_display_name|displayName|
|**--group-expiration-date-time**|date-time|Timestamp of when the group is set to expire. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|expiration_date_time|expirationDateTime|
|**--group-group-types**|array|Specifies the group type and its membership.  If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static.  Returned by default. Supports $filter.|group_types|groupTypes|
|**--group-has-members-with-license-errors**|boolean|Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an example.|has_members_with_license_errors|hasMembersWithLicenseErrors|
|**--group-license-processing-state**|object|licenseProcessingState|license_processing_state|licenseProcessingState|
|**--group-mail**|string|The SMTP address for the group, for example, 'serviceadmins@contoso.onmicrosoft.com'. Returned by default. Read-only. Supports $filter.|mail|mail|
|**--group-mail-enabled**|boolean|Specifies whether the group is mail-enabled. Returned by default.|mail_enabled|mailEnabled|
|**--group-mail-nickname**|string|The mail alias for the group, unique in the organization. This property must be specified when a group is created. Returned by default. Supports $filter.|mail_nickname|mailNickname|
|**--group-membership-rule**|string|The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default.|membership_rule|membershipRule|
|**--group-membership-rule-processing-state**|string|Indicates whether the dynamic membership processing is on or paused. Possible values are 'On' or 'Paused'. Returned by default.|membership_rule_processing_state|membershipRuleProcessingState|
|**--group-on-premises-domain-name**|string|Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_domain_name|onPremisesDomainName|
|**--group-on-premises-last-sync-date-time**|date-time|Indicates the last time at which the group was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only. Supports $filter.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--group-on-premises-net-bios-name**|string|Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_net_bios_name|onPremisesNetBiosName|
|**--group-on-premises-provisioning-errors**|array|Errors when using Microsoft synchronization product during provisioning. Returned by default.|on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--group-on-premises-sam-account-name**|string|Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_sam_account_name|onPremisesSamAccountName|
|**--group-on-premises-security-identifier**|string|Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Returned by default. Read-only.|on_premises_security_identifier|onPremisesSecurityIdentifier|
|**--group-on-premises-sync-enabled**|boolean|true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--group-preferred-data-location**|string|The preferred data location for the group. For more information, see  OneDrive Online Multi-Geo. Returned by default.|preferred_data_location|preferredDataLocation|
|**--group-preferred-language**|string|The preferred language for an Microsoft 365 group. Should follow ISO 639-1 Code; for example 'en-US'. Returned by default.|preferred_language|preferredLanguage|
|**--group-proxy-addresses**|array|Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter.|proxy_addresses|proxyAddresses|
|**--group-renewed-date-time**|date-time|Timestamp of when the group was last renewed. This cannot be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|renewed_date_time|renewedDateTime|
|**--group-security-enabled**|boolean|Specifies whether the group is a security group. Returned by default. Supports $filter.|security_enabled|securityEnabled|
|**--group-security-identifier**|string|Security identifier of the group, used in Windows scenarios. Returned by default.|security_identifier|securityIdentifier|
|**--group-theme**|string|Specifies an Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange or Red. Returned by default.|theme|theme|
|**--group-visibility**|string|Specifies the visibility of a Microsoft 365 group. Possible values are: Private, Public, or Hiddenmembership; blank values are treated as public.  See group visibility options to learn more.Visibility can be set only when a group is created; it is not editable.Visibility is supported only for unified groups; it is not supported for security groups. Returned by default.|microsoft_graph_group_visibility|visibility|
|**--group-allow-external-senders**|boolean|Indicates if people external to the organization can send messages to the group. Default value is false. Returned only on $select.|allow_external_senders|allowExternalSenders|
|**--group-auto-subscribe-new-members**|boolean|Indicates if new members added to the group will be auto-subscribed to receive email notifications. You can set this property in a PATCH request for the group; do not set it in the initial POST request that creates the group. Default value is false. Returned only on $select.|auto_subscribe_new_members|autoSubscribeNewMembers|
|**--group-hide-from-address-lists**|boolean|True if the group is not displayed in certain parts of the Outlook UI: the Address Book, address lists for selecting message recipients, and the Browse Groups dialog for searching groups; otherwise, false. Default value is false. Returned only on $select.|hide_from_address_lists|hideFromAddressLists|
|**--group-hide-from-outlook-clients**|boolean|True if the group is not displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. Default value is false. Returned only on $select.|hide_from_outlook_clients|hideFromOutlookClients|
|**--group-is-subscribed-by-mail**|boolean|Indicates whether the signed-in user is subscribed to receive email conversations. Default value is true. Returned only on $select.|is_subscribed_by_mail|isSubscribedByMail|
|**--group-unseen-count**|integer|Count of conversations that have received new posts since the signed-in user last visited the group. Returned only on $select.|unseen_count|unseenCount|
|**--group-is-archived**|boolean||is_archived|isArchived|
|**--group-app-role-assignments**|array||app_role_assignments|appRoleAssignments|
|**--group-created-on-behalf-of**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|created_on_behalf_of|createdOnBehalfOf|
|**--group-member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--group-members**|array|Users and groups that are members of this group. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups) Nullable.|microsoft_graph_group_members|members|
|**--group-members-with-license-errors**|array|A list of group members with license errors from this group-based license assignment. Read-only.|members_with_license_errors|membersWithLicenseErrors|
|**--group-owners**|array|The owners of the group. The owners are a set of non-admin users who are allowed to modify this object. Limited to 100 owners. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups). Nullable.|owners|owners|
|**--group-settings**|array|Read-only. Nullable.|settings|settings|
|**--group-transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--group-transitive-members**|array||transitive_members|transitiveMembers|
|**--group-accepted-senders**|array|The list of users or groups that are allowed to create post's or calendar events in this group. If this list is non-empty then only users or groups listed here are allowed to post.|accepted_senders|acceptedSenders|
|**--group-calendar**|object|calendar|calendar|calendar|
|**--group-calendar-view**|array|The calendar view for the calendar. Read-only.|calendar_view|calendarView|
|**--group-conversations**|array|The group's conversations.|conversations|conversations|
|**--group-events**|array|The group's calendar events.|events|events|
|**--group-photo**|object|profilePhoto|photo|photo|
|**--group-photos**|array|The profile photos owned by the group. Read-only. Nullable.|photos|photos|
|**--group-rejected-senders**|array|The list of users or groups that are not allowed to create posts or calendar events in this group. Nullable|rejected_senders|rejectedSenders|
|**--group-threads**|array|The group's conversation threads. Nullable.|threads|threads|
|**--group-drive**|object|drive|drive|drive|
|**--group-drives**|array|The group's drives. Read-only.|drives|drives|
|**--group-sites**|array|The list of SharePoint sites in this group. Access the default site with /sites/root.|sites|sites|
|**--group-extensions**|array|The collection of open extensions defined for the group. Read-only. Nullable.|extensions|extensions|
|**--group-group-lifecycle-policies**|array|The collection of lifecycle policies for this group. Read-only. Nullable.|group_lifecycle_policies|groupLifecyclePolicies|
|**--group-planner**|object|plannerGroup|planner|planner|
|**--group-onenote**|object|onenote|onenote|onenote|
|**--group-team**|object|team|team|team|
|**--schedule-id**|string|Read-only.|id2|id|
|**--schedule-enabled**|boolean|Indicates whether the schedule is enabled for the team. Required.|enabled|enabled|
|**--schedule-offer-shift-requests-enabled**|boolean|Indicates whether offer shift requests are enabled for the schedule.|offer_shift_requests_enabled|offerShiftRequestsEnabled|
|**--schedule-open-shifts-enabled**|boolean|Indicates whether open shifts are enabled for the schedule.|open_shifts_enabled|openShiftsEnabled|
|**--schedule-provision-status**|choice||provision_status|provisionStatus|
|**--schedule-provision-status-code**|string|Additional information about why schedule provisioning failed.|provision_status_code|provisionStatusCode|
|**--schedule-swap-shifts-requests-enabled**|boolean|Indicates whether swap shifts requests are enabled for the schedule.|swap_shifts_requests_enabled|swapShiftsRequestsEnabled|
|**--schedule-time-clock-enabled**|boolean|Indicates whether time clock is enabled for the schedule.|time_clock_enabled|timeClockEnabled|
|**--schedule-time-off-requests-enabled**|boolean|Indicates whether time off requests are enabled for the schedule.|time_off_requests_enabled|timeOffRequestsEnabled|
|**--schedule-time-zone**|string|Indicates the time zone of the schedule team using tz database format. Required.|time_zone|timeZone|
|**--schedule-workforce-integration-ids**|array||workforce_integration_ids|workforceIntegrationIds|
|**--schedule-offer-shift-requests**|array||offer_shift_requests|offerShiftRequests|
|**--schedule-open-shift-change-requests**|array||open_shift_change_requests|openShiftChangeRequests|
|**--schedule-open-shifts**|array||open_shifts|openShifts|
|**--schedule-scheduling-groups**|array|The logical grouping of users in the schedule (usually by role).|scheduling_groups|schedulingGroups|
|**--schedule-shifts**|array|The shifts in the schedule.|shifts|shifts|
|**--schedule-swap-shifts-change-requests**|array||swap_shifts_change_requests|swapShiftsChangeRequests|
|**--schedule-time-off-reasons**|array|The set of reasons for a time off in the schedule.|time_off_reasons|timeOffReasons|
|**--schedule-time-off-requests**|array||time_off_requests|timeOffRequests|
|**--schedule-times-off**|array|The instances of times off in the schedule.|times_off|timesOff|

### teams team update-channel

update-channel a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-channel|UpdateChannels|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string|Optional textual description for the channel.|description|description|
|**--display-name**|string|Channel name as it will appear to the user in Microsoft Teams.|display_name|displayName|
|**--email**|string|The email address for sending messages to the channel. Read-only.|email|email|
|**--membership-type**|choice||membership_type|membershipType|
|**--web-url**|string|A hyperlink that will navigate to the channel in Microsoft Teams. This is the URL that you get when you right-click a channel in Microsoft Teams and select Get link to channel. This URL should be treated as an opaque blob, and not parsed. Read-only.|web_url|webUrl|
|**--files-folder**|object|driveItem|files_folder|filesFolder|
|**--members**|array||members|members|
|**--messages**|array|A collection of all the messages in the channel. A navigation property. Nullable.|messages|messages|
|**--tabs**|array|A collection of all the tabs in the channel. A navigation property.|tabs|tabs|

### teams team update-installed-app

update-installed-app a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-installed-app|UpdateInstalledApps|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--id**|string|Read-only.|id|id|
|**--teams-app-definition**|object|teamsAppDefinition|teams_app_definition|teamsAppDefinition|
|**--teams-app-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|display_name|displayName|
|**--teams-app-distribution-method**|choice||distribution_method|distributionMethod|
|**--teams-app-external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--teams-app-app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

### teams team update-member

update-member a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-member|UpdateMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

### teams team update-operation

update-operation a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-operation|UpdateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-async-operation-id**|string|key: id of teamsAsyncOperation|teams_async_operation_id|teamsAsyncOperation-id|
|**--id**|string|Read-only.|id|id|
|**--attempts-count**|integer|Number of times the operation was attempted before being marked successful or failed.|attempts_count|attemptsCount|
|**--created-date-time**|date-time|Time when the operation was created.|created_date_time|createdDateTime|
|**--error**|object|operationError|error|error|
|**--last-action-date-time**|date-time|Time when the async operation was last updated.|last_action_date_time|lastActionDateTime|
|**--operation-type**|choice||operation_type|operationType|
|**--status**|choice||status|status|
|**--target-resource-id**|string|The ID of the object that's created or modified as result of this async operation, typically a team.|target_resource_id|targetResourceId|
|**--target-resource-location**|string|The location of the object that's created or modified as result of this async operation. This URL should be treated as an opaque value and not parsed into its component paths.|target_resource_location|targetResourceLocation|

### teams team update-primary-channel

update-primary-channel a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-primary-channel|UpdatePrimaryChannel|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string|Optional textual description for the channel.|description|description|
|**--display-name**|string|Channel name as it will appear to the user in Microsoft Teams.|display_name|displayName|
|**--email**|string|The email address for sending messages to the channel. Read-only.|email|email|
|**--membership-type**|choice||membership_type|membershipType|
|**--web-url**|string|A hyperlink that will navigate to the channel in Microsoft Teams. This is the URL that you get when you right-click a channel in Microsoft Teams and select Get link to channel. This URL should be treated as an opaque blob, and not parsed. Read-only.|web_url|webUrl|
|**--files-folder**|object|driveItem|files_folder|filesFolder|
|**--members**|array||members|members|
|**--messages**|array|A collection of all the messages in the channel. A navigation property. Nullable.|messages|messages|
|**--tabs**|array|A collection of all the tabs in the channel. A navigation property.|tabs|tabs|

### teams team update-schedule

update-schedule a teams team.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team|teams|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-schedule|UpdateSchedule|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--enabled**|boolean|Indicates whether the schedule is enabled for the team. Required.|enabled|enabled|
|**--offer-shift-requests-enabled**|boolean|Indicates whether offer shift requests are enabled for the schedule.|offer_shift_requests_enabled|offerShiftRequestsEnabled|
|**--open-shifts-enabled**|boolean|Indicates whether open shifts are enabled for the schedule.|open_shifts_enabled|openShiftsEnabled|
|**--provision-status**|choice||provision_status|provisionStatus|
|**--provision-status-code**|string|Additional information about why schedule provisioning failed.|provision_status_code|provisionStatusCode|
|**--swap-shifts-requests-enabled**|boolean|Indicates whether swap shifts requests are enabled for the schedule.|swap_shifts_requests_enabled|swapShiftsRequestsEnabled|
|**--time-clock-enabled**|boolean|Indicates whether time clock is enabled for the schedule.|time_clock_enabled|timeClockEnabled|
|**--time-off-requests-enabled**|boolean|Indicates whether time off requests are enabled for the schedule.|time_off_requests_enabled|timeOffRequestsEnabled|
|**--time-zone**|string|Indicates the time zone of the schedule team using tz database format. Required.|time_zone|timeZone|
|**--workforce-integration-ids**|array||workforce_integration_ids|workforceIntegrationIds|
|**--offer-shift-requests**|array||offer_shift_requests|offerShiftRequests|
|**--open-shift-change-requests**|array||open_shift_change_requests|openShiftChangeRequests|
|**--open-shifts**|array||open_shifts|openShifts|
|**--scheduling-groups**|array|The logical grouping of users in the schedule (usually by role).|scheduling_groups|schedulingGroups|
|**--shifts**|array|The shifts in the schedule.|shifts|shifts|
|**--swap-shifts-change-requests**|array||swap_shifts_change_requests|swapShiftsChangeRequests|
|**--time-off-reasons**|array|The set of reasons for a time off in the schedule.|time_off_reasons|timeOffReasons|
|**--time-off-requests**|array||time_off_requests|timeOffRequests|
|**--times-off**|array|The instances of times off in the schedule.|times_off|timesOff|

### teams team-channel create-member

create-member a teams team-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel|teams.channels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-member|CreateMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

### teams team-channel create-message

create-message a teams team-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel|teams.channels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-message|CreateMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--policy-violation-dlp-action**|choice||dlp_action|dlpAction|
|**--policy-violation-justification-text**|string||justification_text|justificationText|
|**--policy-violation-policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--policy-violation-user-action**|choice||user_action|userAction|
|**--policy-violation-verdict-details**|choice||verdict_details|verdictDetails|
|**--from-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--from-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--from-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--from-device-id**|string|Unique identifier for the identity.|id1|id|
|**--from-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--from-application-id**|string|Unique identifier for the identity.|id2|id|

### teams team-channel create-tab

create-tab a teams team-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel|teams.channels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-tab|CreateTabs|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|teamsTabConfiguration|configuration|configuration|
|**--display-name**|string|Name of the tab.|display_name|displayName|
|**--web-url**|string|Deep link URL of the tab instance. Read only.|web_url|webUrl|
|**--teams-app-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--teams-app-distribution-method**|choice||distribution_method|distributionMethod|
|**--teams-app-external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--teams-app-app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

### teams team-channel delete

delete a teams team-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel|teams.channels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteMembers|
|delete|DeleteMessages|
|delete|DeleteTabs|
|delete|DeleteFilesFolder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--if-match**|string|ETag|if_match|If-Match|

### teams team-channel get-file-folder

get-file-folder a teams team-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel|teams.channels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-file-folder|GetFilesFolder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-channel get-member

get-member a teams team-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel|teams.channels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member|GetMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-channel get-message

get-message a teams team-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel|teams.channels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-message|GetMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-channel get-tab

get-tab a teams team-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel|teams.channels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-tab|GetTabs|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-channel list-member

list-member a teams team-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel|teams.channels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member|ListMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-channel list-message

list-message a teams team-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel|teams.channels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-message|ListMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-channel list-tab

list-tab a teams team-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel|teams.channels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-tab|ListTabs|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-channel update-file-folder

update-file-folder a teams team-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel|teams.channels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-file-folder|UpdateFilesFolder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--parent-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--parent-reference-site-id**|string||site_id|siteId|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--audio**|object|audio|audio|audio|
|**--content**|byte-array|The content stream, if the item represents a file.|content|content|
|**--c-tag**|string|An eTag for the content of the item. This eTag is not changed if only the metadata is changed. Note This property is not returned if the item is a folder. Read-only.|c_tag|cTag|
|**--file-system-info**|object|fileSystemInfo|file_system_info|fileSystemInfo|
|**--image**|object|image|image|image|
|**--location**|object|geoCoordinates|location|location|
|**--photo**|object|photo|photo|photo|
|**--publication**|object|publicationFacet|publication|publication|
|**--root**|dictionary|root|root|root|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--size**|integer|Size of the item in bytes. Read-only.|size|size|
|**--video**|object|video|video|video|
|**--web-dav-url**|string|WebDAV compatible URL for the item.|web_dav_url|webDavUrl|
|**--children**|array|Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.|children|children|
|**--permissions**|array|The set of permissions for the item. Read-only. Nullable.|permissions|permissions|
|**--subscriptions**|array|The set of subscriptions on the item. Only supported on the root of a drive.|subscriptions|subscriptions|
|**--thumbnails**|array|Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.|thumbnails|thumbnails|
|**--versions**|array|The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.|versions|versions|
|**--list-item-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--list-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--list-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--list-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--list-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--list-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--list-item-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--list-item-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--list-item-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--list-item-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--list-item-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|id6|id|
|**--list-item-parent-reference-name**|string|The name of the item being referenced. Read-only.|name1|name|
|**--list-item-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--list-item-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--list-item-parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--list-item-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-item-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--list-item-last-modified-by-user-id**|string|Unique identifier for the identity.|id7|id|
|**--list-item-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--list-item-last-modified-by-device-id**|string|Unique identifier for the identity.|id8|id|
|**--list-item-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--list-item-last-modified-by-application-id**|string|Unique identifier for the identity.|id9|id|
|**--list-item-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--list-item-created-by-user-id**|string|Unique identifier for the identity.|id10|id|
|**--list-item-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--list-item-created-by-device-id**|string|Unique identifier for the identity.|id11|id|
|**--list-item-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|
|**--list-item-created-by-application-id**|string|Unique identifier for the identity.|id12|id|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids2|sharepointIds|
|**--list-item-analytics**|object|itemAnalytics|analytics|analytics|
|**--list-item-drive-item**|object|driveItem|drive_item|driveItem|
|**--list-item-fields**|object|fieldValueSet|fields|fields|
|**--list-item-versions**|array|The list of previous versions of the list item.|microsoft_graph_list_item_versions|versions|
|**--analytics-id**|string|Read-only.|id13|id|
|**--analytics-all-time**|object|itemActivityStat|all_time|allTime|
|**--analytics-item-activity-stats**|array||item_activity_stats|itemActivityStats|
|**--analytics-last-seven-days**|object|itemActivityStat|last_seven_days|lastSevenDays|
|**--workbook-id**|string|Read-only.|id14|id|
|**--workbook-application**|object|workbookApplication|application|application|
|**--workbook-comments**|array||comments|comments|
|**--workbook-functions**|object|workbookFunctions|functions|functions|
|**--workbook-names**|array|Represents a collection of workbook scoped named items (named ranges and constants). Read-only.|names|names|
|**--workbook-operations**|array|The status of workbook operations. Getting an operation collection is not supported, but you can get the status of a long-running operation if the Location header is returned in the response. Read-only.|operations|operations|
|**--workbook-tables**|array|Represents a collection of tables associated with the workbook. Read-only.|tables|tables|
|**--workbook-worksheets**|array|Represents a collection of worksheets associated with the workbook. Read-only.|worksheets|worksheets|
|**--special-folder-name**|string|The unique identifier for this item in the /drive/special collection|microsoft_graph_special_folder_name|name|
|**--shared-owner**|object|identitySet|owner|owner|
|**--shared-scope**|string|Indicates the scope of how the item is shared: anonymous, organization, or users. Read-only.|scope|scope|
|**--shared-shared-by**|object|identitySet|shared_by|sharedBy|
|**--shared-shared-date-time**|date-time|The UTC date and time when the item was shared. Read-only.|shared_date_time|sharedDateTime|
|**--search-result-on-click-telemetry-url**|string|A callback URL that can be used to record telemetry information. The application should issue a GET on this URL if the user interacts with this item to improve the quality of results.|on_click_telemetry_url|onClickTelemetryUrl|
|**--remote-item-created-by**|object|identitySet|created_by|createdBy|
|**--remote-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_remote_item_created_date_time_created_date_time|createdDateTime|
|**--remote-item-file**|object|file|file|file|
|**--remote-item-file-system-info**|object|fileSystemInfo|microsoft_graph_file_system_info_file_system_info|fileSystemInfo|
|**--remote-item-folder**|object|folder|folder|folder|
|**--remote-item-id**|string|Unique identifier for the remote item in its drive. Read-only.|microsoft_graph_remote_item_id|id|
|**--remote-item-image**|object|image|microsoft_graph_image|image|
|**--remote-item-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--remote-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_remote_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--remote-item-name**|string|Optional. Filename of the remote item. Read-only.|microsoft_graph_remote_item_name|name|
|**--remote-item-package**|object|package|package|package|
|**--remote-item-parent-reference**|object|itemReference|parent_reference|parentReference|
|**--remote-item-shared**|object|shared|shared|shared|
|**--remote-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids3|sharepointIds|
|**--remote-item-size**|integer|Size of the remote item. Read-only.|integer_size|size|
|**--remote-item-special-folder**|object|specialFolder|special_folder|specialFolder|
|**--remote-item-video**|object|video|microsoft_graph_video|video|
|**--remote-item-web-dav-url**|string|DAV compatible URL for the item.|microsoft_graph_remote_item_web_dav_url_web_dav_url|webDavUrl|
|**--remote-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_remote_item_web_url|webUrl|
|**--pending-operations-pending-content-update-queued-date-time**|date-time|Date and time the pending binary operation was queued in UTC time. Read-only.|queued_date_time|queuedDateTime|
|**--package-type**|string|A string indicating the type of package. While oneNote is the only currently defined value, you should expect other package types to be returned and handle them accordingly.|type|type|
|**--folder-child-count**|integer|Number of children contained immediately within this container.|child_count|childCount|
|**--folder-view**|object|folderView|view|view|
|**--file-hashes**|object|hashes|hashes|hashes|
|**--file-mime-type**|string|The MIME type for the file. This is determined by logic on the server and might not be the value provided when the file was uploaded. Read-only.|mime_type|mimeType|
|**--file-processing-metadata**|boolean||processing_metadata|processingMetadata|
|**--deleted-state**|string|Represents the state of the deleted item.|state|state|

### teams team-channel update-member

update-member a teams team-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel|teams.channels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-member|UpdateMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

### teams team-channel update-message

update-message a teams team-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel|teams.channels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-message|UpdateMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--policy-violation-dlp-action**|choice||dlp_action|dlpAction|
|**--policy-violation-justification-text**|string||justification_text|justificationText|
|**--policy-violation-policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--policy-violation-user-action**|choice||user_action|userAction|
|**--policy-violation-verdict-details**|choice||verdict_details|verdictDetails|
|**--from-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--from-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--from-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--from-device-id**|string|Unique identifier for the identity.|id1|id|
|**--from-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--from-application-id**|string|Unique identifier for the identity.|id2|id|

### teams team-channel update-tab

update-tab a teams team-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel|teams.channels|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-tab|UpdateTabs|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|teamsTabConfiguration|configuration|configuration|
|**--display-name**|string|Name of the tab.|display_name|displayName|
|**--web-url**|string|Deep link URL of the tab instance. Read only.|web_url|webUrl|
|**--teams-app-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--teams-app-distribution-method**|choice||distribution_method|distributionMethod|
|**--teams-app-external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--teams-app-app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

### teams team-channel-message create-hosted-content

create-hosted-content a teams team-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel-message|teams.channels.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-hosted-content|CreateHostedContents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|

### teams team-channel-message create-reply

create-reply a teams team-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel-message|teams.channels.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-reply|CreateReplies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--policy-violation-dlp-action**|choice||dlp_action|dlpAction|
|**--policy-violation-justification-text**|string||justification_text|justificationText|
|**--policy-violation-policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--policy-violation-user-action**|choice||user_action|userAction|
|**--policy-violation-verdict-details**|choice||verdict_details|verdictDetails|
|**--from-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--from-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--from-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--from-device-id**|string|Unique identifier for the identity.|id1|id|
|**--from-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--from-application-id**|string|Unique identifier for the identity.|id2|id|

### teams team-channel-message delete

delete a teams team-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel-message|teams.channels.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteHostedContents|
|delete|DeleteReplies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--if-match**|string|ETag|if_match|If-Match|

### teams team-channel-message get-hosted-content

get-hosted-content a teams team-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel-message|teams.channels.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-hosted-content|GetHostedContents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-channel-message get-reply

get-reply a teams team-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel-message|teams.channels.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-reply|GetReplies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-channel-message list-hosted-content

list-hosted-content a teams team-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel-message|teams.channels.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-hosted-content|ListHostedContents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-channel-message list-reply

list-reply a teams team-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel-message|teams.channels.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-reply|ListReplies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-channel-message update-hosted-content

update-hosted-content a teams team-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel-message|teams.channels.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-hosted-content|UpdateHostedContents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--id**|string|Read-only.|id|id|

### teams team-channel-message update-reply

update-reply a teams team-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel-message|teams.channels.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-reply|UpdateReplies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--policy-violation-dlp-action**|choice||dlp_action|dlpAction|
|**--policy-violation-justification-text**|string||justification_text|justificationText|
|**--policy-violation-policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--policy-violation-user-action**|choice||user_action|userAction|
|**--policy-violation-verdict-details**|choice||verdict_details|verdictDetails|
|**--from-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--from-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--from-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--from-device-id**|string|Unique identifier for the identity.|id1|id|
|**--from-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--from-application-id**|string|Unique identifier for the identity.|id2|id|

### teams team-channel-tab delete

delete a teams team-channel-tab.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel-tab|teams.channels.tabs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRefTeamsApp|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--if-match**|string|ETag|if_match|If-Match|

### teams team-channel-tab get-app

get-app a teams team-channel-tab.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel-tab|teams.channels.tabs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-app|GetTeamsApp|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-channel-tab get-ref-team-app

get-ref-team-app a teams team-channel-tab.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel-tab|teams.channels.tabs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-team-app|GetRefTeamsApp|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|

### teams team-channel-tab set-ref-team-app

set-ref-team-app a teams team-channel-tab.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-channel-tab|teams.channels.tabs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-team-app|SetRefTeamsApp|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### teams team-installed-app delete

delete a teams team-installed-app.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-installed-app|teams.installedApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRefTeamsApp|
|delete|DeleteRefTeamsAppDefinition|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--if-match**|string|ETag|if_match|If-Match|

### teams team-installed-app get-app

get-app a teams team-installed-app.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-installed-app|teams.installedApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-app|GetTeamsApp|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-installed-app get-app-definition

get-app-definition a teams team-installed-app.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-installed-app|teams.installedApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-app-definition|GetTeamsAppDefinition|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-installed-app get-ref-team-app

get-ref-team-app a teams team-installed-app.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-installed-app|teams.installedApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-team-app|GetRefTeamsApp|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|

### teams team-installed-app get-ref-team-app-definition

get-ref-team-app-definition a teams team-installed-app.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-installed-app|teams.installedApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-team-app-definition|GetRefTeamsAppDefinition|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|

### teams team-installed-app set-ref-team-app

set-ref-team-app a teams team-installed-app.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-installed-app|teams.installedApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-team-app|SetRefTeamsApp|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### teams team-installed-app set-ref-team-app-definition

set-ref-team-app-definition a teams team-installed-app.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-installed-app|teams.installedApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-team-app-definition|SetRefTeamsAppDefinition|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### teams team-installed-app upgrade

upgrade a teams team-installed-app.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-installed-app|teams.installedApps|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|upgrade|upgrade|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|

### teams team-primary-channel create-member

create-member a teams team-primary-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel|teams.primaryChannel|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-member|CreateMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

### teams team-primary-channel create-message

create-message a teams team-primary-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel|teams.primaryChannel|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-message|CreateMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--policy-violation-dlp-action**|choice||dlp_action|dlpAction|
|**--policy-violation-justification-text**|string||justification_text|justificationText|
|**--policy-violation-policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--policy-violation-user-action**|choice||user_action|userAction|
|**--policy-violation-verdict-details**|choice||verdict_details|verdictDetails|
|**--from-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--from-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--from-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--from-device-id**|string|Unique identifier for the identity.|id1|id|
|**--from-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--from-application-id**|string|Unique identifier for the identity.|id2|id|

### teams team-primary-channel create-tab

create-tab a teams team-primary-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel|teams.primaryChannel|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-tab|CreateTabs|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|teamsTabConfiguration|configuration|configuration|
|**--display-name**|string|Name of the tab.|display_name|displayName|
|**--web-url**|string|Deep link URL of the tab instance. Read only.|web_url|webUrl|
|**--teams-app-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--teams-app-distribution-method**|choice||distribution_method|distributionMethod|
|**--teams-app-external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--teams-app-app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

### teams team-primary-channel delete

delete a teams team-primary-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel|teams.primaryChannel|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteMembers|
|delete|DeleteMessages|
|delete|DeleteTabs|
|delete|DeleteFilesFolder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--if-match**|string|ETag|if_match|If-Match|

### teams team-primary-channel get-file-folder

get-file-folder a teams team-primary-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel|teams.primaryChannel|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-file-folder|GetFilesFolder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-primary-channel get-member

get-member a teams team-primary-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel|teams.primaryChannel|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member|GetMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-primary-channel get-message

get-message a teams team-primary-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel|teams.primaryChannel|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-message|GetMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-primary-channel get-tab

get-tab a teams team-primary-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel|teams.primaryChannel|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-tab|GetTabs|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-primary-channel list-member

list-member a teams team-primary-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel|teams.primaryChannel|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-member|ListMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-primary-channel list-message

list-message a teams team-primary-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel|teams.primaryChannel|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-message|ListMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-primary-channel list-tab

list-tab a teams team-primary-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel|teams.primaryChannel|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-tab|ListTabs|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-primary-channel update-file-folder

update-file-folder a teams team-primary-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel|teams.primaryChannel|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-file-folder|UpdateFilesFolder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--parent-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--parent-reference-site-id**|string||site_id|siteId|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name2|displayName|
|**--created-by-user-id**|string|Unique identifier for the identity.|id3|id|
|**--created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name3|displayName|
|**--created-by-device-id**|string|Unique identifier for the identity.|id4|id|
|**--created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name4|displayName|
|**--created-by-application-id**|string|Unique identifier for the identity.|id5|id|
|**--audio**|object|audio|audio|audio|
|**--content**|byte-array|The content stream, if the item represents a file.|content|content|
|**--c-tag**|string|An eTag for the content of the item. This eTag is not changed if only the metadata is changed. Note This property is not returned if the item is a folder. Read-only.|c_tag|cTag|
|**--file-system-info**|object|fileSystemInfo|file_system_info|fileSystemInfo|
|**--image**|object|image|image|image|
|**--location**|object|geoCoordinates|location|location|
|**--photo**|object|photo|photo|photo|
|**--publication**|object|publicationFacet|publication|publication|
|**--root**|dictionary|root|root|root|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--size**|integer|Size of the item in bytes. Read-only.|size|size|
|**--video**|object|video|video|video|
|**--web-dav-url**|string|WebDAV compatible URL for the item.|web_dav_url|webDavUrl|
|**--children**|array|Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.|children|children|
|**--permissions**|array|The set of permissions for the item. Read-only. Nullable.|permissions|permissions|
|**--subscriptions**|array|The set of subscriptions on the item. Only supported on the root of a drive.|subscriptions|subscriptions|
|**--thumbnails**|array|Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.|thumbnails|thumbnails|
|**--versions**|array|The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.|versions|versions|
|**--list-item-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--list-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--list-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--list-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--list-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--list-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--list-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--list-item-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--list-item-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--list-item-parent-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--list-item-parent-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--list-item-parent-reference-id**|string|Unique identifier of the item in the drive. Read-only.|id6|id|
|**--list-item-parent-reference-name**|string|The name of the item being referenced. Read-only.|name1|name|
|**--list-item-parent-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--list-item-parent-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--list-item-parent-reference-sharepoint-ids**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--list-item-parent-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--list-item-last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name5|displayName|
|**--list-item-last-modified-by-user-id**|string|Unique identifier for the identity.|id7|id|
|**--list-item-last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name6|displayName|
|**--list-item-last-modified-by-device-id**|string|Unique identifier for the identity.|id8|id|
|**--list-item-last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name7|displayName|
|**--list-item-last-modified-by-application-id**|string|Unique identifier for the identity.|id9|id|
|**--list-item-created-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name8|displayName|
|**--list-item-created-by-user-id**|string|Unique identifier for the identity.|id10|id|
|**--list-item-created-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name9|displayName|
|**--list-item-created-by-device-id**|string|Unique identifier for the identity.|id11|id|
|**--list-item-created-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name10|displayName|
|**--list-item-created-by-application-id**|string|Unique identifier for the identity.|id12|id|
|**--list-item-content-type**|object|contentTypeInfo|content_type|contentType|
|**--list-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids2|sharepointIds|
|**--list-item-analytics**|object|itemAnalytics|analytics|analytics|
|**--list-item-drive-item**|object|driveItem|drive_item|driveItem|
|**--list-item-fields**|object|fieldValueSet|fields|fields|
|**--list-item-versions**|array|The list of previous versions of the list item.|microsoft_graph_list_item_versions|versions|
|**--analytics-id**|string|Read-only.|id13|id|
|**--analytics-all-time**|object|itemActivityStat|all_time|allTime|
|**--analytics-item-activity-stats**|array||item_activity_stats|itemActivityStats|
|**--analytics-last-seven-days**|object|itemActivityStat|last_seven_days|lastSevenDays|
|**--workbook-id**|string|Read-only.|id14|id|
|**--workbook-application**|object|workbookApplication|application|application|
|**--workbook-comments**|array||comments|comments|
|**--workbook-functions**|object|workbookFunctions|functions|functions|
|**--workbook-names**|array|Represents a collection of workbook scoped named items (named ranges and constants). Read-only.|names|names|
|**--workbook-operations**|array|The status of workbook operations. Getting an operation collection is not supported, but you can get the status of a long-running operation if the Location header is returned in the response. Read-only.|operations|operations|
|**--workbook-tables**|array|Represents a collection of tables associated with the workbook. Read-only.|tables|tables|
|**--workbook-worksheets**|array|Represents a collection of worksheets associated with the workbook. Read-only.|worksheets|worksheets|
|**--special-folder-name**|string|The unique identifier for this item in the /drive/special collection|microsoft_graph_special_folder_name|name|
|**--shared-owner**|object|identitySet|owner|owner|
|**--shared-scope**|string|Indicates the scope of how the item is shared: anonymous, organization, or users. Read-only.|scope|scope|
|**--shared-shared-by**|object|identitySet|shared_by|sharedBy|
|**--shared-shared-date-time**|date-time|The UTC date and time when the item was shared. Read-only.|shared_date_time|sharedDateTime|
|**--search-result-on-click-telemetry-url**|string|A callback URL that can be used to record telemetry information. The application should issue a GET on this URL if the user interacts with this item to improve the quality of results.|on_click_telemetry_url|onClickTelemetryUrl|
|**--remote-item-created-by**|object|identitySet|created_by|createdBy|
|**--remote-item-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_remote_item_created_date_time_created_date_time|createdDateTime|
|**--remote-item-file**|object|file|file|file|
|**--remote-item-file-system-info**|object|fileSystemInfo|microsoft_graph_file_system_info_file_system_info|fileSystemInfo|
|**--remote-item-folder**|object|folder|folder|folder|
|**--remote-item-id**|string|Unique identifier for the remote item in its drive. Read-only.|microsoft_graph_remote_item_id|id|
|**--remote-item-image**|object|image|microsoft_graph_image|image|
|**--remote-item-last-modified-by**|object|identitySet|last_modified_by|lastModifiedBy|
|**--remote-item-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_remote_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--remote-item-name**|string|Optional. Filename of the remote item. Read-only.|microsoft_graph_remote_item_name|name|
|**--remote-item-package**|object|package|package|package|
|**--remote-item-parent-reference**|object|itemReference|parent_reference|parentReference|
|**--remote-item-shared**|object|shared|shared|shared|
|**--remote-item-sharepoint-ids**|object|sharepointIds|sharepoint_ids3|sharepointIds|
|**--remote-item-size**|integer|Size of the remote item. Read-only.|integer_size|size|
|**--remote-item-special-folder**|object|specialFolder|special_folder|specialFolder|
|**--remote-item-video**|object|video|microsoft_graph_video|video|
|**--remote-item-web-dav-url**|string|DAV compatible URL for the item.|microsoft_graph_remote_item_web_dav_url_web_dav_url|webDavUrl|
|**--remote-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_remote_item_web_url|webUrl|
|**--pending-operations-pending-content-update-queued-date-time**|date-time|Date and time the pending binary operation was queued in UTC time. Read-only.|queued_date_time|queuedDateTime|
|**--package-type**|string|A string indicating the type of package. While oneNote is the only currently defined value, you should expect other package types to be returned and handle them accordingly.|type|type|
|**--folder-child-count**|integer|Number of children contained immediately within this container.|child_count|childCount|
|**--folder-view**|object|folderView|view|view|
|**--file-hashes**|object|hashes|hashes|hashes|
|**--file-mime-type**|string|The MIME type for the file. This is determined by logic on the server and might not be the value provided when the file was uploaded. Read-only.|mime_type|mimeType|
|**--file-processing-metadata**|boolean||processing_metadata|processingMetadata|
|**--deleted-state**|string|Represents the state of the deleted item.|state|state|

### teams team-primary-channel update-member

update-member a teams team-primary-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel|teams.primaryChannel|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-member|UpdateMembers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

### teams team-primary-channel update-message

update-message a teams team-primary-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel|teams.primaryChannel|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-message|UpdateMessages|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--policy-violation-dlp-action**|choice||dlp_action|dlpAction|
|**--policy-violation-justification-text**|string||justification_text|justificationText|
|**--policy-violation-policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--policy-violation-user-action**|choice||user_action|userAction|
|**--policy-violation-verdict-details**|choice||verdict_details|verdictDetails|
|**--from-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--from-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--from-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--from-device-id**|string|Unique identifier for the identity.|id1|id|
|**--from-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--from-application-id**|string|Unique identifier for the identity.|id2|id|

### teams team-primary-channel update-tab

update-tab a teams team-primary-channel.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel|teams.primaryChannel|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-tab|UpdateTabs|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|teamsTabConfiguration|configuration|configuration|
|**--display-name**|string|Name of the tab.|display_name|displayName|
|**--web-url**|string|Deep link URL of the tab instance. Read only.|web_url|webUrl|
|**--teams-app-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--teams-app-distribution-method**|choice||distribution_method|distributionMethod|
|**--teams-app-external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--teams-app-app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

### teams team-primary-channel-message create-hosted-content

create-hosted-content a teams team-primary-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel-message|teams.primaryChannel.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-hosted-content|CreateHostedContents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|

### teams team-primary-channel-message create-reply

create-reply a teams team-primary-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel-message|teams.primaryChannel.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-reply|CreateReplies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--policy-violation-dlp-action**|choice||dlp_action|dlpAction|
|**--policy-violation-justification-text**|string||justification_text|justificationText|
|**--policy-violation-policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--policy-violation-user-action**|choice||user_action|userAction|
|**--policy-violation-verdict-details**|choice||verdict_details|verdictDetails|
|**--from-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--from-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--from-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--from-device-id**|string|Unique identifier for the identity.|id1|id|
|**--from-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--from-application-id**|string|Unique identifier for the identity.|id2|id|

### teams team-primary-channel-message delete

delete a teams team-primary-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel-message|teams.primaryChannel.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteHostedContents|
|delete|DeleteReplies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--if-match**|string|ETag|if_match|If-Match|

### teams team-primary-channel-message get-hosted-content

get-hosted-content a teams team-primary-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel-message|teams.primaryChannel.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-hosted-content|GetHostedContents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-primary-channel-message get-reply

get-reply a teams team-primary-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel-message|teams.primaryChannel.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-reply|GetReplies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-primary-channel-message list-hosted-content

list-hosted-content a teams team-primary-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel-message|teams.primaryChannel.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-hosted-content|ListHostedContents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-primary-channel-message list-reply

list-reply a teams team-primary-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel-message|teams.primaryChannel.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-reply|ListReplies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-primary-channel-message update-hosted-content

update-hosted-content a teams team-primary-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel-message|teams.primaryChannel.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-hosted-content|UpdateHostedContents|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--id**|string|Read-only.|id|id|

### teams team-primary-channel-message update-reply

update-reply a teams team-primary-channel-message.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel-message|teams.primaryChannel.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-reply|UpdateReplies|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--id**|string|Read-only.|id|id|
|**--attachments**|array|Attached files. Attachments are currently read-only – sending attachments is not supported.|attachments|attachments|
|**--body**|object|itemBody|body|body|
|**--created-date-time**|date-time|Read only. Timestamp of when the chat message was created.|created_date_time|createdDateTime|
|**--deleted-date-time**|date-time|Read only. Timestamp at which the chat message was deleted, or null if not deleted.|deleted_date_time|deletedDateTime|
|**--etag**|string|Read-only. Version number of the chat message.|etag|etag|
|**--importance**|choice||importance|importance|
|**--last-edited-date-time**|date-time|Read only. Timestamp when edits to the chat message were made. Triggers an 'Edited' flag in the Microsoft Teams UI. If no edits are made the value is null.|last_edited_date_time|lastEditedDateTime|
|**--last-modified-date-time**|date-time|Read only. Timestamp when the chat message is created (initial setting) or edited, including when a reaction is added or removed.|last_modified_date_time|lastModifiedDateTime|
|**--locale**|string|Locale of the chat message set by the client.|locale|locale|
|**--mentions**|array|List of entities mentioned in the chat message. Currently supports user, bot, team, channel.|mentions|mentions|
|**--message-type**|choice||message_type|messageType|
|**--reactions**|array||reactions|reactions|
|**--reply-to-id**|string|Read-only. Id of the parent chat message or root chat message of the thread. (Only applies to chat messages in channels not chats)|reply_to_id|replyToId|
|**--subject**|string|The subject of the chat message, in plaintext.|subject|subject|
|**--summary**|string|Summary text of the chat message that could be used for push notifications and summary views or fall back views. Only applies to channel chat messages, not chat messages in a chat.|summary|summary|
|**--web-url**|string||web_url|webUrl|
|**--hosted-contents**|array||hosted_contents|hostedContents|
|**--replies**|array||replies|replies|
|**--policy-violation-dlp-action**|choice||dlp_action|dlpAction|
|**--policy-violation-justification-text**|string||justification_text|justificationText|
|**--policy-violation-policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--policy-violation-user-action**|choice||user_action|userAction|
|**--policy-violation-verdict-details**|choice||verdict_details|verdictDetails|
|**--from-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--from-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--from-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--from-device-id**|string|Unique identifier for the identity.|id1|id|
|**--from-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--from-application-id**|string|Unique identifier for the identity.|id2|id|

### teams team-primary-channel-tab delete

delete a teams team-primary-channel-tab.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel-tab|teams.primaryChannel.tabs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRefTeamsApp|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--if-match**|string|ETag|if_match|If-Match|

### teams team-primary-channel-tab get-app

get-app a teams team-primary-channel-tab.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel-tab|teams.primaryChannel.tabs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-app|GetTeamsApp|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-primary-channel-tab get-ref-team-app

get-ref-team-app a teams team-primary-channel-tab.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel-tab|teams.primaryChannel.tabs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-team-app|GetRefTeamsApp|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|

### teams team-primary-channel-tab set-ref-team-app

set-ref-team-app a teams team-primary-channel-tab.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-primary-channel-tab|teams.primaryChannel.tabs|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-team-app|SetRefTeamsApp|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### teams team-schedule create-offer-shift-request

create-offer-shift-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-offer-shift-request|CreateOfferShiftRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--recipient-action-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|recipient_action_date_time|recipientActionDateTime|
|**--recipient-action-message**|string|Custom message sent by recipient of the offer shift request.|recipient_action_message|recipientActionMessage|
|**--recipient-user-id**|string|User ID of the recipient of the offer shift request.|recipient_user_id|recipientUserId|
|**--sender-shift-id**|string|User ID of the sender of the offer shift request.|sender_shift_id|senderShiftId|

### teams team-schedule create-open-shift

create-open-shift a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-open-shift|CreateOpenShifts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--draft-open-shift**|object|openShiftItem|draft_open_shift|draftOpenShift|
|**--scheduling-group-id**|string|ID for the scheduling group that the open shift belongs to.|scheduling_group_id|schedulingGroupId|
|**--shared-open-shift**|object|openShiftItem|shared_open_shift|sharedOpenShift|

### teams team-schedule create-open-shift-change-request

create-open-shift-change-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-open-shift-change-request|CreateOpenShiftChangeRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--open-shift-id**|string|ID for the open shift.|open_shift_id|openShiftId|

### teams team-schedule create-scheduling-group

create-scheduling-group a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-scheduling-group|CreateSchedulingGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--microsoft-graph-scheduling-group-display-name**|string|The display name for the schedulingGroup. Required.|microsoft_graph_scheduling_group_display_name|displayName|
|**--is-active**|boolean|Indicates whether the schedulingGroup can be used when creating new entities or updating existing ones. Required.|is_active|isActive|
|**--user-ids**|array|The list of user IDs that are a member of the schedulingGroup. Required.|user_ids|userIds|

### teams team-schedule create-shift

create-shift a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-shift|CreateShifts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--body**|object|New navigation property|body|body|

### teams team-schedule create-swap-shift-change-request

create-swap-shift-change-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-swap-shift-change-request|CreateSwapShiftsChangeRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--recipient-action-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|recipient_action_date_time|recipientActionDateTime|
|**--recipient-action-message**|string|Custom message sent by recipient of the offer shift request.|recipient_action_message|recipientActionMessage|
|**--recipient-user-id**|string|User ID of the recipient of the offer shift request.|recipient_user_id|recipientUserId|
|**--sender-shift-id**|string|User ID of the sender of the offer shift request.|sender_shift_id|senderShiftId|
|**--recipient-shift-id**|string|ShiftId for the recipient user with whom the request is to swap.|recipient_shift_id|recipientShiftId|

### teams team-schedule create-time-off

create-time-off a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-time-off|CreateTimesOff|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--draft-time-off**|object|timeOffItem|draft_time_off|draftTimeOff|
|**--shared-time-off**|object|timeOffItem|shared_time_off|sharedTimeOff|
|**--user-id**|string|ID of the user assigned to the timeOff. Required.|user_id|userId|

### teams team-schedule create-time-off-reason

create-time-off-reason a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-time-off-reason|CreateTimeOffReasons|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--microsoft-graph-time-off-reason-display-name**|string|The name of the timeOffReason. Required.|microsoft_graph_time_off_reason_display_name|displayName|
|**--icon-type**|choice||icon_type|iconType|
|**--is-active**|boolean|Indicates whether the timeOffReason can be used when creating new entities or updating existing ones. Required.|is_active|isActive|

### teams team-schedule create-time-off-request

create-time-off-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-time-off-request|CreateTimeOffRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--end-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|end_date_time|endDateTime|
|**--start-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--time-off-reason-id**|string|The reason for the time off.|time_off_reason_id|timeOffReasonId|

### teams team-schedule delete

delete a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteOfferShiftRequests|
|delete|DeleteOpenShiftChangeRequests|
|delete|DeleteOpenShifts|
|delete|DeleteSchedulingGroups|
|delete|DeleteShifts|
|delete|DeleteSwapShiftsChangeRequests|
|delete|DeleteTimeOffReasons|
|delete|DeleteTimeOffRequests|
|delete|DeleteTimesOff|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--offer-shift-request-id**|string|key: id of offerShiftRequest|offer_shift_request_id|offerShiftRequest-id|
|**--open-shift-change-request-id**|string|key: id of openShiftChangeRequest|open_shift_change_request_id|openShiftChangeRequest-id|
|**--open-shift-id**|string|key: id of openShift|open_shift_id|openShift-id|
|**--scheduling-group-id**|string|key: id of schedulingGroup|scheduling_group_id|schedulingGroup-id|
|**--shift-id**|string|key: id of shift|shift_id|shift-id|
|**--swap-shifts-change-request-id**|string|key: id of swapShiftsChangeRequest|swap_shifts_change_request_id|swapShiftsChangeRequest-id|
|**--time-off-reason-id**|string|key: id of timeOffReason|time_off_reason_id|timeOffReason-id|
|**--time-off-request-id**|string|key: id of timeOffRequest|time_off_request_id|timeOffRequest-id|
|**--time-off-id**|string|key: id of timeOff|time_off_id|timeOff-id|
|**--if-match**|string|ETag|if_match|If-Match|

### teams team-schedule get-offer-shift-request

get-offer-shift-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-offer-shift-request|GetOfferShiftRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--offer-shift-request-id**|string|key: id of offerShiftRequest|offer_shift_request_id|offerShiftRequest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule get-open-shift

get-open-shift a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-open-shift|GetOpenShifts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-id**|string|key: id of openShift|open_shift_id|openShift-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule get-open-shift-change-request

get-open-shift-change-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-open-shift-change-request|GetOpenShiftChangeRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-change-request-id**|string|key: id of openShiftChangeRequest|open_shift_change_request_id|openShiftChangeRequest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule get-scheduling-group

get-scheduling-group a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-scheduling-group|GetSchedulingGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--scheduling-group-id**|string|key: id of schedulingGroup|scheduling_group_id|schedulingGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule get-shift

get-shift a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-shift|GetShifts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--shift-id**|string|key: id of shift|shift_id|shift-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule get-swap-shift-change-request

get-swap-shift-change-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-swap-shift-change-request|GetSwapShiftsChangeRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--swap-shifts-change-request-id**|string|key: id of swapShiftsChangeRequest|swap_shifts_change_request_id|swapShiftsChangeRequest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule get-time-off

get-time-off a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-time-off|GetTimesOff|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-id**|string|key: id of timeOff|time_off_id|timeOff-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule get-time-off-reason

get-time-off-reason a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-time-off-reason|GetTimeOffReasons|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-reason-id**|string|key: id of timeOffReason|time_off_reason_id|timeOffReason-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule get-time-off-request

get-time-off-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-time-off-request|GetTimeOffRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-request-id**|string|key: id of timeOffRequest|time_off_request_id|timeOffRequest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule list-offer-shift-request

list-offer-shift-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-offer-shift-request|ListOfferShiftRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule list-open-shift

list-open-shift a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-open-shift|ListOpenShifts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule list-open-shift-change-request

list-open-shift-change-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-open-shift-change-request|ListOpenShiftChangeRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule list-scheduling-group

list-scheduling-group a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-scheduling-group|ListSchedulingGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule list-shift

list-shift a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-shift|ListShifts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule list-swap-shift-change-request

list-swap-shift-change-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-swap-shift-change-request|ListSwapShiftsChangeRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule list-time-off

list-time-off a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-time-off|ListTimesOff|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule list-time-off-reason

list-time-off-reason a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-time-off-reason|ListTimeOffReasons|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule list-time-off-request

list-time-off-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-time-off-request|ListTimeOffRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams team-schedule share

share a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|share|share|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--notify-team**|boolean||notify_team|notifyTeam|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--end-date-time**|date-time||end_date_time|endDateTime|

### teams team-schedule update-offer-shift-request

update-offer-shift-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-offer-shift-request|UpdateOfferShiftRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--offer-shift-request-id**|string|key: id of offerShiftRequest|offer_shift_request_id|offerShiftRequest-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--recipient-action-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|recipient_action_date_time|recipientActionDateTime|
|**--recipient-action-message**|string|Custom message sent by recipient of the offer shift request.|recipient_action_message|recipientActionMessage|
|**--recipient-user-id**|string|User ID of the recipient of the offer shift request.|recipient_user_id|recipientUserId|
|**--sender-shift-id**|string|User ID of the sender of the offer shift request.|sender_shift_id|senderShiftId|

### teams team-schedule update-open-shift

update-open-shift a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-open-shift|UpdateOpenShifts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-id**|string|key: id of openShift|open_shift_id|openShift-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--draft-open-shift**|object|openShiftItem|draft_open_shift|draftOpenShift|
|**--scheduling-group-id**|string|ID for the scheduling group that the open shift belongs to.|scheduling_group_id|schedulingGroupId|
|**--shared-open-shift**|object|openShiftItem|shared_open_shift|sharedOpenShift|

### teams team-schedule update-open-shift-change-request

update-open-shift-change-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-open-shift-change-request|UpdateOpenShiftChangeRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-change-request-id**|string|key: id of openShiftChangeRequest|open_shift_change_request_id|openShiftChangeRequest-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--open-shift-id**|string|ID for the open shift.|open_shift_id|openShiftId|

### teams team-schedule update-scheduling-group

update-scheduling-group a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-scheduling-group|UpdateSchedulingGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--scheduling-group-id**|string|key: id of schedulingGroup|scheduling_group_id|schedulingGroup-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--microsoft-graph-scheduling-group-display-name**|string|The display name for the schedulingGroup. Required.|microsoft_graph_scheduling_group_display_name|displayName|
|**--is-active**|boolean|Indicates whether the schedulingGroup can be used when creating new entities or updating existing ones. Required.|is_active|isActive|
|**--user-ids**|array|The list of user IDs that are a member of the schedulingGroup. Required.|user_ids|userIds|

### teams team-schedule update-shift

update-shift a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-shift|UpdateShifts|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--shift-id**|string|key: id of shift|shift_id|shift-id|
|**--body**|object|New navigation property values|body|body|

### teams team-schedule update-swap-shift-change-request

update-swap-shift-change-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-swap-shift-change-request|UpdateSwapShiftsChangeRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--swap-shifts-change-request-id**|string|key: id of swapShiftsChangeRequest|swap_shifts_change_request_id|swapShiftsChangeRequest-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--recipient-action-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|recipient_action_date_time|recipientActionDateTime|
|**--recipient-action-message**|string|Custom message sent by recipient of the offer shift request.|recipient_action_message|recipientActionMessage|
|**--recipient-user-id**|string|User ID of the recipient of the offer shift request.|recipient_user_id|recipientUserId|
|**--sender-shift-id**|string|User ID of the sender of the offer shift request.|sender_shift_id|senderShiftId|
|**--recipient-shift-id**|string|ShiftId for the recipient user with whom the request is to swap.|recipient_shift_id|recipientShiftId|

### teams team-schedule update-time-off

update-time-off a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-time-off|UpdateTimesOff|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-id**|string|key: id of timeOff|time_off_id|timeOff-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--draft-time-off**|object|timeOffItem|draft_time_off|draftTimeOff|
|**--shared-time-off**|object|timeOffItem|shared_time_off|sharedTimeOff|
|**--user-id**|string|ID of the user assigned to the timeOff. Required.|user_id|userId|

### teams team-schedule update-time-off-reason

update-time-off-reason a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-time-off-reason|UpdateTimeOffReasons|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-reason-id**|string|key: id of timeOffReason|time_off_reason_id|timeOffReason-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--microsoft-graph-time-off-reason-display-name**|string|The name of the timeOffReason. Required.|microsoft_graph_time_off_reason_display_name|displayName|
|**--icon-type**|choice||icon_type|iconType|
|**--is-active**|boolean|Indicates whether the timeOffReason can be used when creating new entities or updating existing ones. Required.|is_active|isActive|

### teams team-schedule update-time-off-request

update-time-off-request a teams team-schedule.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams team-schedule|teams.schedule|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-time-off-request|UpdateTimeOffRequests|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-request-id**|string|key: id of timeOffRequest|time_off_request_id|timeOffRequest-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--end-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|end_date_time|endDateTime|
|**--start-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|start_date_time|startDateTime|
|**--time-off-reason-id**|string|The reason for the time off.|time_off_reason_id|timeOffReasonId|

### teams teamwork create-workforce-integration

create-workforce-integration a teams teamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams teamwork|teamwork|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-workforce-integration|CreateWorkforceIntegrations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--api-version**|integer|API version for the call back URL. Start with 1.|api_version|apiVersion|
|**--microsoft-graph-workforce-integration-display-name**|string|Name of the workforce integration.|microsoft_graph_workforce_integration_display_name|displayName|
|**--encryption**|object|workforceIntegrationEncryption|encryption|encryption|
|**--is-active**|boolean|Indicates whether this workforce integration is currently active and available.|is_active|isActive|
|**--supported-entities**|choice||supported_entities|supportedEntities|
|**--url**|string|Workforce Integration URL for callbacks from the Shifts service.|url|url|

### teams teamwork delete

delete a teams teamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams teamwork|teamwork|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteWorkforceIntegrations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--workforce-integration-id**|string|key: id of workforceIntegration|workforce_integration_id|workforceIntegration-id|
|**--if-match**|string|ETag|if_match|If-Match|

### teams teamwork get-workforce-integration

get-workforce-integration a teams teamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams teamwork|teamwork|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-workforce-integration|GetWorkforceIntegrations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--workforce-integration-id**|string|key: id of workforceIntegration|workforce_integration_id|workforceIntegration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams teamwork list-workforce-integration

list-workforce-integration a teams teamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams teamwork|teamwork|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-workforce-integration|ListWorkforceIntegrations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams teamwork update-workforce-integration

update-workforce-integration a teams teamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams teamwork|teamwork|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-workforce-integration|UpdateWorkforceIntegrations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--workforce-integration-id**|string|key: id of workforceIntegration|workforce_integration_id|workforceIntegration-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--last-modified-by-user-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name|displayName|
|**--last-modified-by-user-id**|string|Unique identifier for the identity.|microsoft_graph_identity_id|id|
|**--last-modified-by-device-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|microsoft_graph_identity_display_name|displayName|
|**--last-modified-by-device-id**|string|Unique identifier for the identity.|id1|id|
|**--last-modified-by-application-display-name**|string|The identity's display name. Note that this may not always be available or up to date. For example, if a user changes their display name, the API may show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.|display_name1|displayName|
|**--last-modified-by-application-id**|string|Unique identifier for the identity.|id2|id|
|**--api-version**|integer|API version for the call back URL. Start with 1.|api_version|apiVersion|
|**--microsoft-graph-workforce-integration-display-name**|string|Name of the workforce integration.|microsoft_graph_workforce_integration_display_name|displayName|
|**--encryption**|object|workforceIntegrationEncryption|encryption|encryption|
|**--is-active**|boolean|Indicates whether this workforce integration is currently active and available.|is_active|isActive|
|**--supported-entities**|choice||supported_entities|supportedEntities|
|**--url**|string|Workforce Integration URL for callbacks from the Shifts service.|url|url|

### teams teamwork-teamwork getwork

getwork a teams teamwork-teamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams teamwork-teamwork|teamwork.teamwork|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|getwork|GetTeamwork|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams teamwork-teamwork updatework

updatework a teams teamwork-teamwork.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams teamwork-teamwork|teamwork.teamwork|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|updatework|UpdateTeamwork|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--workforce-integrations**|array||workforce_integrations|workforceIntegrations|

### teams user create-joined-team

create-joined-team a teams user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-joined-team|CreateJoinedTeams|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--classification**|string|An optional label. Typically describes the data or business sensitivity of the team. Must match one of a pre-configured set in the tenant's directory.|classification|classification|
|**--description**|string|An optional description for the team.|description|description|
|**--display-name**|string|The name of the team.|display_name|displayName|
|**--fun-settings**|object|teamFunSettings|fun_settings|funSettings|
|**--guest-settings**|object|teamGuestSettings|guest_settings|guestSettings|
|**--internal-id**|string|A unique ID for the team that has been used in a few places such as the audit log/Office 365 Management Activity API.|internal_id|internalId|
|**--is-archived**|boolean|Whether this team is in read-only mode.|is_archived|isArchived|
|**--member-settings**|object|teamMemberSettings|member_settings|memberSettings|
|**--messaging-settings**|object|teamMessagingSettings|messaging_settings|messagingSettings|
|**--specialization**|choice||specialization|specialization|
|**--visibility**|choice||visibility|visibility|
|**--web-url**|string|A hyperlink that will go to the team in the Microsoft Teams client. This is the URL that you get when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.|web_url|webUrl|
|**--channels**|array|The collection of channels & messages associated with the team.|channels|channels|
|**--installed-apps**|array|The apps installed in this team.|installed_apps|installedApps|
|**--members**|array|Members and owners of the team.|members|members|
|**--operations**|array|The async operations that ran or are running on this team.|operations|operations|
|**--primary-channel**|object|channel|primary_channel|primaryChannel|
|**--template-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--group-id**|string|Read-only.|id1|id|
|**--group-deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--group-assigned-labels**|array|The list of sensitivity label pairs (label ID, label name) associated with an Microsoft 365 group. Returned only on $select. Read-only.|assigned_labels|assignedLabels|
|**--group-assigned-licenses**|array|The licenses that are assigned to the group. Returned only on $select. Read-only.|assigned_licenses|assignedLicenses|
|**--group-classification**|string|Describes a classification for the group (such as low, medium or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default.|microsoft_graph_group_classification|classification|
|**--group-created-date-time**|date-time|Timestamp of when the group was created. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|created_date_time|createdDateTime|
|**--group-description**|string|An optional description for the group. Returned by default.|microsoft_graph_group_description|description|
|**--group-display-name**|string|The display name for the group. This property is required when a group is created and cannot be cleared during updates. Returned by default. Supports $filter and $orderby.|microsoft_graph_group_display_name|displayName|
|**--group-expiration-date-time**|date-time|Timestamp of when the group is set to expire. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|expiration_date_time|expirationDateTime|
|**--group-group-types**|array|Specifies the group type and its membership.  If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static.  Returned by default. Supports $filter.|group_types|groupTypes|
|**--group-has-members-with-license-errors**|boolean|Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an example.|has_members_with_license_errors|hasMembersWithLicenseErrors|
|**--group-license-processing-state**|object|licenseProcessingState|license_processing_state|licenseProcessingState|
|**--group-mail**|string|The SMTP address for the group, for example, 'serviceadmins@contoso.onmicrosoft.com'. Returned by default. Read-only. Supports $filter.|mail|mail|
|**--group-mail-enabled**|boolean|Specifies whether the group is mail-enabled. Returned by default.|mail_enabled|mailEnabled|
|**--group-mail-nickname**|string|The mail alias for the group, unique in the organization. This property must be specified when a group is created. Returned by default. Supports $filter.|mail_nickname|mailNickname|
|**--group-membership-rule**|string|The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default.|membership_rule|membershipRule|
|**--group-membership-rule-processing-state**|string|Indicates whether the dynamic membership processing is on or paused. Possible values are 'On' or 'Paused'. Returned by default.|membership_rule_processing_state|membershipRuleProcessingState|
|**--group-on-premises-domain-name**|string|Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_domain_name|onPremisesDomainName|
|**--group-on-premises-last-sync-date-time**|date-time|Indicates the last time at which the group was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only. Supports $filter.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--group-on-premises-net-bios-name**|string|Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_net_bios_name|onPremisesNetBiosName|
|**--group-on-premises-provisioning-errors**|array|Errors when using Microsoft synchronization product during provisioning. Returned by default.|on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--group-on-premises-sam-account-name**|string|Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_sam_account_name|onPremisesSamAccountName|
|**--group-on-premises-security-identifier**|string|Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Returned by default. Read-only.|on_premises_security_identifier|onPremisesSecurityIdentifier|
|**--group-on-premises-sync-enabled**|boolean|true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--group-preferred-data-location**|string|The preferred data location for the group. For more information, see  OneDrive Online Multi-Geo. Returned by default.|preferred_data_location|preferredDataLocation|
|**--group-preferred-language**|string|The preferred language for an Microsoft 365 group. Should follow ISO 639-1 Code; for example 'en-US'. Returned by default.|preferred_language|preferredLanguage|
|**--group-proxy-addresses**|array|Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter.|proxy_addresses|proxyAddresses|
|**--group-renewed-date-time**|date-time|Timestamp of when the group was last renewed. This cannot be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|renewed_date_time|renewedDateTime|
|**--group-security-enabled**|boolean|Specifies whether the group is a security group. Returned by default. Supports $filter.|security_enabled|securityEnabled|
|**--group-security-identifier**|string|Security identifier of the group, used in Windows scenarios. Returned by default.|security_identifier|securityIdentifier|
|**--group-theme**|string|Specifies an Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange or Red. Returned by default.|theme|theme|
|**--group-visibility**|string|Specifies the visibility of a Microsoft 365 group. Possible values are: Private, Public, or Hiddenmembership; blank values are treated as public.  See group visibility options to learn more.Visibility can be set only when a group is created; it is not editable.Visibility is supported only for unified groups; it is not supported for security groups. Returned by default.|microsoft_graph_group_visibility|visibility|
|**--group-allow-external-senders**|boolean|Indicates if people external to the organization can send messages to the group. Default value is false. Returned only on $select.|allow_external_senders|allowExternalSenders|
|**--group-auto-subscribe-new-members**|boolean|Indicates if new members added to the group will be auto-subscribed to receive email notifications. You can set this property in a PATCH request for the group; do not set it in the initial POST request that creates the group. Default value is false. Returned only on $select.|auto_subscribe_new_members|autoSubscribeNewMembers|
|**--group-hide-from-address-lists**|boolean|True if the group is not displayed in certain parts of the Outlook UI: the Address Book, address lists for selecting message recipients, and the Browse Groups dialog for searching groups; otherwise, false. Default value is false. Returned only on $select.|hide_from_address_lists|hideFromAddressLists|
|**--group-hide-from-outlook-clients**|boolean|True if the group is not displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. Default value is false. Returned only on $select.|hide_from_outlook_clients|hideFromOutlookClients|
|**--group-is-subscribed-by-mail**|boolean|Indicates whether the signed-in user is subscribed to receive email conversations. Default value is true. Returned only on $select.|is_subscribed_by_mail|isSubscribedByMail|
|**--group-unseen-count**|integer|Count of conversations that have received new posts since the signed-in user last visited the group. Returned only on $select.|unseen_count|unseenCount|
|**--group-is-archived**|boolean||is_archived|isArchived|
|**--group-app-role-assignments**|array||app_role_assignments|appRoleAssignments|
|**--group-created-on-behalf-of**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|created_on_behalf_of|createdOnBehalfOf|
|**--group-member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--group-members**|array|Users and groups that are members of this group. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups) Nullable.|microsoft_graph_group_members|members|
|**--group-members-with-license-errors**|array|A list of group members with license errors from this group-based license assignment. Read-only.|members_with_license_errors|membersWithLicenseErrors|
|**--group-owners**|array|The owners of the group. The owners are a set of non-admin users who are allowed to modify this object. Limited to 100 owners. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups). Nullable.|owners|owners|
|**--group-settings**|array|Read-only. Nullable.|settings|settings|
|**--group-transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--group-transitive-members**|array||transitive_members|transitiveMembers|
|**--group-accepted-senders**|array|The list of users or groups that are allowed to create post's or calendar events in this group. If this list is non-empty then only users or groups listed here are allowed to post.|accepted_senders|acceptedSenders|
|**--group-calendar**|object|calendar|calendar|calendar|
|**--group-calendar-view**|array|The calendar view for the calendar. Read-only.|calendar_view|calendarView|
|**--group-conversations**|array|The group's conversations.|conversations|conversations|
|**--group-events**|array|The group's calendar events.|events|events|
|**--group-photo**|object|profilePhoto|photo|photo|
|**--group-photos**|array|The profile photos owned by the group. Read-only. Nullable.|photos|photos|
|**--group-rejected-senders**|array|The list of users or groups that are not allowed to create posts or calendar events in this group. Nullable|rejected_senders|rejectedSenders|
|**--group-threads**|array|The group's conversation threads. Nullable.|threads|threads|
|**--group-drive**|object|drive|drive|drive|
|**--group-drives**|array|The group's drives. Read-only.|drives|drives|
|**--group-sites**|array|The list of SharePoint sites in this group. Access the default site with /sites/root.|sites|sites|
|**--group-extensions**|array|The collection of open extensions defined for the group. Read-only. Nullable.|extensions|extensions|
|**--group-group-lifecycle-policies**|array|The collection of lifecycle policies for this group. Read-only. Nullable.|group_lifecycle_policies|groupLifecyclePolicies|
|**--group-planner**|object|plannerGroup|planner|planner|
|**--group-onenote**|object|onenote|onenote|onenote|
|**--group-team**|object|team|team|team|
|**--schedule-id**|string|Read-only.|id2|id|
|**--schedule-enabled**|boolean|Indicates whether the schedule is enabled for the team. Required.|enabled|enabled|
|**--schedule-offer-shift-requests-enabled**|boolean|Indicates whether offer shift requests are enabled for the schedule.|offer_shift_requests_enabled|offerShiftRequestsEnabled|
|**--schedule-open-shifts-enabled**|boolean|Indicates whether open shifts are enabled for the schedule.|open_shifts_enabled|openShiftsEnabled|
|**--schedule-provision-status**|choice||provision_status|provisionStatus|
|**--schedule-provision-status-code**|string|Additional information about why schedule provisioning failed.|provision_status_code|provisionStatusCode|
|**--schedule-swap-shifts-requests-enabled**|boolean|Indicates whether swap shifts requests are enabled for the schedule.|swap_shifts_requests_enabled|swapShiftsRequestsEnabled|
|**--schedule-time-clock-enabled**|boolean|Indicates whether time clock is enabled for the schedule.|time_clock_enabled|timeClockEnabled|
|**--schedule-time-off-requests-enabled**|boolean|Indicates whether time off requests are enabled for the schedule.|time_off_requests_enabled|timeOffRequestsEnabled|
|**--schedule-time-zone**|string|Indicates the time zone of the schedule team using tz database format. Required.|time_zone|timeZone|
|**--schedule-workforce-integration-ids**|array||workforce_integration_ids|workforceIntegrationIds|
|**--schedule-offer-shift-requests**|array||offer_shift_requests|offerShiftRequests|
|**--schedule-open-shift-change-requests**|array||open_shift_change_requests|openShiftChangeRequests|
|**--schedule-open-shifts**|array||open_shifts|openShifts|
|**--schedule-scheduling-groups**|array|The logical grouping of users in the schedule (usually by role).|scheduling_groups|schedulingGroups|
|**--schedule-shifts**|array|The shifts in the schedule.|shifts|shifts|
|**--schedule-swap-shifts-change-requests**|array||swap_shifts_change_requests|swapShiftsChangeRequests|
|**--schedule-time-off-reasons**|array|The set of reasons for a time off in the schedule.|time_off_reasons|timeOffReasons|
|**--schedule-time-off-requests**|array||time_off_requests|timeOffRequests|
|**--schedule-times-off**|array|The instances of times off in the schedule.|times_off|timesOff|

### teams user delete

delete a teams user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteJoinedTeams|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

### teams user get-joined-team

get-joined-team a teams user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-joined-team|GetJoinedTeams|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams user list-joined-team

list-joined-team a teams user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-joined-team|ListJoinedTeams|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### teams user update-joined-team

update-joined-team a teams user.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|teams user|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-joined-team|UpdateJoinedTeams|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--classification**|string|An optional label. Typically describes the data or business sensitivity of the team. Must match one of a pre-configured set in the tenant's directory.|classification|classification|
|**--description**|string|An optional description for the team.|description|description|
|**--display-name**|string|The name of the team.|display_name|displayName|
|**--fun-settings**|object|teamFunSettings|fun_settings|funSettings|
|**--guest-settings**|object|teamGuestSettings|guest_settings|guestSettings|
|**--internal-id**|string|A unique ID for the team that has been used in a few places such as the audit log/Office 365 Management Activity API.|internal_id|internalId|
|**--is-archived**|boolean|Whether this team is in read-only mode.|is_archived|isArchived|
|**--member-settings**|object|teamMemberSettings|member_settings|memberSettings|
|**--messaging-settings**|object|teamMessagingSettings|messaging_settings|messagingSettings|
|**--specialization**|choice||specialization|specialization|
|**--visibility**|choice||visibility|visibility|
|**--web-url**|string|A hyperlink that will go to the team in the Microsoft Teams client. This is the URL that you get when you right-click a team in the Microsoft Teams client and select Get link to team. This URL should be treated as an opaque blob, and not parsed.|web_url|webUrl|
|**--channels**|array|The collection of channels & messages associated with the team.|channels|channels|
|**--installed-apps**|array|The apps installed in this team.|installed_apps|installedApps|
|**--members**|array|Members and owners of the team.|members|members|
|**--operations**|array|The async operations that ran or are running on this team.|operations|operations|
|**--primary-channel**|object|channel|primary_channel|primaryChannel|
|**--template-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--group-id**|string|Read-only.|id1|id|
|**--group-deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--group-assigned-labels**|array|The list of sensitivity label pairs (label ID, label name) associated with an Microsoft 365 group. Returned only on $select. Read-only.|assigned_labels|assignedLabels|
|**--group-assigned-licenses**|array|The licenses that are assigned to the group. Returned only on $select. Read-only.|assigned_licenses|assignedLicenses|
|**--group-classification**|string|Describes a classification for the group (such as low, medium or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default.|microsoft_graph_group_classification|classification|
|**--group-created-date-time**|date-time|Timestamp of when the group was created. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|created_date_time|createdDateTime|
|**--group-description**|string|An optional description for the group. Returned by default.|microsoft_graph_group_description|description|
|**--group-display-name**|string|The display name for the group. This property is required when a group is created and cannot be cleared during updates. Returned by default. Supports $filter and $orderby.|microsoft_graph_group_display_name|displayName|
|**--group-expiration-date-time**|date-time|Timestamp of when the group is set to expire. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|expiration_date_time|expirationDateTime|
|**--group-group-types**|array|Specifies the group type and its membership.  If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static.  Returned by default. Supports $filter.|group_types|groupTypes|
|**--group-has-members-with-license-errors**|boolean|Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an example.|has_members_with_license_errors|hasMembersWithLicenseErrors|
|**--group-license-processing-state**|object|licenseProcessingState|license_processing_state|licenseProcessingState|
|**--group-mail**|string|The SMTP address for the group, for example, 'serviceadmins@contoso.onmicrosoft.com'. Returned by default. Read-only. Supports $filter.|mail|mail|
|**--group-mail-enabled**|boolean|Specifies whether the group is mail-enabled. Returned by default.|mail_enabled|mailEnabled|
|**--group-mail-nickname**|string|The mail alias for the group, unique in the organization. This property must be specified when a group is created. Returned by default. Supports $filter.|mail_nickname|mailNickname|
|**--group-membership-rule**|string|The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default.|membership_rule|membershipRule|
|**--group-membership-rule-processing-state**|string|Indicates whether the dynamic membership processing is on or paused. Possible values are 'On' or 'Paused'. Returned by default.|membership_rule_processing_state|membershipRuleProcessingState|
|**--group-on-premises-domain-name**|string|Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_domain_name|onPremisesDomainName|
|**--group-on-premises-last-sync-date-time**|date-time|Indicates the last time at which the group was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only. Supports $filter.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--group-on-premises-net-bios-name**|string|Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_net_bios_name|onPremisesNetBiosName|
|**--group-on-premises-provisioning-errors**|array|Errors when using Microsoft synchronization product during provisioning. Returned by default.|on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--group-on-premises-sam-account-name**|string|Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_sam_account_name|onPremisesSamAccountName|
|**--group-on-premises-security-identifier**|string|Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Returned by default. Read-only.|on_premises_security_identifier|onPremisesSecurityIdentifier|
|**--group-on-premises-sync-enabled**|boolean|true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--group-preferred-data-location**|string|The preferred data location for the group. For more information, see  OneDrive Online Multi-Geo. Returned by default.|preferred_data_location|preferredDataLocation|
|**--group-preferred-language**|string|The preferred language for an Microsoft 365 group. Should follow ISO 639-1 Code; for example 'en-US'. Returned by default.|preferred_language|preferredLanguage|
|**--group-proxy-addresses**|array|Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter.|proxy_addresses|proxyAddresses|
|**--group-renewed-date-time**|date-time|Timestamp of when the group was last renewed. This cannot be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|renewed_date_time|renewedDateTime|
|**--group-security-enabled**|boolean|Specifies whether the group is a security group. Returned by default. Supports $filter.|security_enabled|securityEnabled|
|**--group-security-identifier**|string|Security identifier of the group, used in Windows scenarios. Returned by default.|security_identifier|securityIdentifier|
|**--group-theme**|string|Specifies an Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange or Red. Returned by default.|theme|theme|
|**--group-visibility**|string|Specifies the visibility of a Microsoft 365 group. Possible values are: Private, Public, or Hiddenmembership; blank values are treated as public.  See group visibility options to learn more.Visibility can be set only when a group is created; it is not editable.Visibility is supported only for unified groups; it is not supported for security groups. Returned by default.|microsoft_graph_group_visibility|visibility|
|**--group-allow-external-senders**|boolean|Indicates if people external to the organization can send messages to the group. Default value is false. Returned only on $select.|allow_external_senders|allowExternalSenders|
|**--group-auto-subscribe-new-members**|boolean|Indicates if new members added to the group will be auto-subscribed to receive email notifications. You can set this property in a PATCH request for the group; do not set it in the initial POST request that creates the group. Default value is false. Returned only on $select.|auto_subscribe_new_members|autoSubscribeNewMembers|
|**--group-hide-from-address-lists**|boolean|True if the group is not displayed in certain parts of the Outlook UI: the Address Book, address lists for selecting message recipients, and the Browse Groups dialog for searching groups; otherwise, false. Default value is false. Returned only on $select.|hide_from_address_lists|hideFromAddressLists|
|**--group-hide-from-outlook-clients**|boolean|True if the group is not displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. Default value is false. Returned only on $select.|hide_from_outlook_clients|hideFromOutlookClients|
|**--group-is-subscribed-by-mail**|boolean|Indicates whether the signed-in user is subscribed to receive email conversations. Default value is true. Returned only on $select.|is_subscribed_by_mail|isSubscribedByMail|
|**--group-unseen-count**|integer|Count of conversations that have received new posts since the signed-in user last visited the group. Returned only on $select.|unseen_count|unseenCount|
|**--group-is-archived**|boolean||is_archived|isArchived|
|**--group-app-role-assignments**|array||app_role_assignments|appRoleAssignments|
|**--group-created-on-behalf-of**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|created_on_behalf_of|createdOnBehalfOf|
|**--group-member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--group-members**|array|Users and groups that are members of this group. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups) Nullable.|microsoft_graph_group_members|members|
|**--group-members-with-license-errors**|array|A list of group members with license errors from this group-based license assignment. Read-only.|members_with_license_errors|membersWithLicenseErrors|
|**--group-owners**|array|The owners of the group. The owners are a set of non-admin users who are allowed to modify this object. Limited to 100 owners. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups). Nullable.|owners|owners|
|**--group-settings**|array|Read-only. Nullable.|settings|settings|
|**--group-transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--group-transitive-members**|array||transitive_members|transitiveMembers|
|**--group-accepted-senders**|array|The list of users or groups that are allowed to create post's or calendar events in this group. If this list is non-empty then only users or groups listed here are allowed to post.|accepted_senders|acceptedSenders|
|**--group-calendar**|object|calendar|calendar|calendar|
|**--group-calendar-view**|array|The calendar view for the calendar. Read-only.|calendar_view|calendarView|
|**--group-conversations**|array|The group's conversations.|conversations|conversations|
|**--group-events**|array|The group's calendar events.|events|events|
|**--group-photo**|object|profilePhoto|photo|photo|
|**--group-photos**|array|The profile photos owned by the group. Read-only. Nullable.|photos|photos|
|**--group-rejected-senders**|array|The list of users or groups that are not allowed to create posts or calendar events in this group. Nullable|rejected_senders|rejectedSenders|
|**--group-threads**|array|The group's conversation threads. Nullable.|threads|threads|
|**--group-drive**|object|drive|drive|drive|
|**--group-drives**|array|The group's drives. Read-only.|drives|drives|
|**--group-sites**|array|The list of SharePoint sites in this group. Access the default site with /sites/root.|sites|sites|
|**--group-extensions**|array|The collection of open extensions defined for the group. Read-only. Nullable.|extensions|extensions|
|**--group-group-lifecycle-policies**|array|The collection of lifecycle policies for this group. Read-only. Nullable.|group_lifecycle_policies|groupLifecyclePolicies|
|**--group-planner**|object|plannerGroup|planner|planner|
|**--group-onenote**|object|onenote|onenote|onenote|
|**--group-team**|object|team|team|team|
|**--schedule-id**|string|Read-only.|id2|id|
|**--schedule-enabled**|boolean|Indicates whether the schedule is enabled for the team. Required.|enabled|enabled|
|**--schedule-offer-shift-requests-enabled**|boolean|Indicates whether offer shift requests are enabled for the schedule.|offer_shift_requests_enabled|offerShiftRequestsEnabled|
|**--schedule-open-shifts-enabled**|boolean|Indicates whether open shifts are enabled for the schedule.|open_shifts_enabled|openShiftsEnabled|
|**--schedule-provision-status**|choice||provision_status|provisionStatus|
|**--schedule-provision-status-code**|string|Additional information about why schedule provisioning failed.|provision_status_code|provisionStatusCode|
|**--schedule-swap-shifts-requests-enabled**|boolean|Indicates whether swap shifts requests are enabled for the schedule.|swap_shifts_requests_enabled|swapShiftsRequestsEnabled|
|**--schedule-time-clock-enabled**|boolean|Indicates whether time clock is enabled for the schedule.|time_clock_enabled|timeClockEnabled|
|**--schedule-time-off-requests-enabled**|boolean|Indicates whether time off requests are enabled for the schedule.|time_off_requests_enabled|timeOffRequestsEnabled|
|**--schedule-time-zone**|string|Indicates the time zone of the schedule team using tz database format. Required.|time_zone|timeZone|
|**--schedule-workforce-integration-ids**|array||workforce_integration_ids|workforceIntegrationIds|
|**--schedule-offer-shift-requests**|array||offer_shift_requests|offerShiftRequests|
|**--schedule-open-shift-change-requests**|array||open_shift_change_requests|openShiftChangeRequests|
|**--schedule-open-shifts**|array||open_shifts|openShifts|
|**--schedule-scheduling-groups**|array|The logical grouping of users in the schedule (usually by role).|scheduling_groups|schedulingGroups|
|**--schedule-shifts**|array|The shifts in the schedule.|shifts|shifts|
|**--schedule-swap-shifts-change-requests**|array||swap_shifts_change_requests|swapShiftsChangeRequests|
|**--schedule-time-off-reasons**|array|The set of reasons for a time off in the schedule.|time_off_reasons|timeOffReasons|
|**--schedule-time-off-requests**|array||time_off_requests|timeOffRequests|
|**--schedule-times-off**|array|The instances of times off in the schedule.|times_off|timesOff|
