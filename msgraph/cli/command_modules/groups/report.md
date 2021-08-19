# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az groups|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az groups` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az groups group|groups|[commands](#CommandsIngroups)|
|az groups group-calendar|groups.calendar|[commands](#CommandsIngroups.calendar)|
|az groups group-calendar-calendar-view|groups.calendar.calendarView|[commands](#CommandsIngroups.calendar.calendarView)|
|az groups group-calendar-calendar-view-attachment|groups.calendar.calendarView.attachments|[commands](#CommandsIngroups.calendar.calendarView.attachments)|
|az groups group-calendar-calendar-view-calendar|groups.calendar.calendarView.calendar|[commands](#CommandsIngroups.calendar.calendarView.calendar)|
|az groups group-calendar-calendar-view-instance|groups.calendar.calendarView.instances|[commands](#CommandsIngroups.calendar.calendarView.instances)|
|az groups group-calendar-event|groups.calendar.events|[commands](#CommandsIngroups.calendar.events)|
|az groups group-calendar-event-attachment|groups.calendar.events.attachments|[commands](#CommandsIngroups.calendar.events.attachments)|
|az groups group-calendar-event-calendar|groups.calendar.events.calendar|[commands](#CommandsIngroups.calendar.events.calendar)|
|az groups group-calendar-event-instance|groups.calendar.events.instances|[commands](#CommandsIngroups.calendar.events.instances)|
|az groups group-calendar-view|groups.calendarView|[commands](#CommandsIngroups.calendarView)|
|az groups group-calendar-view-attachment|groups.calendarView.attachments|[commands](#CommandsIngroups.calendarView.attachments)|
|az groups group-calendar-view-calendar|groups.calendarView.calendar|[commands](#CommandsIngroups.calendarView.calendar)|
|az groups group-calendar-view-calendar-calendar-view|groups.calendarView.calendar.calendarView|[commands](#CommandsIngroups.calendarView.calendar.calendarView)|
|az groups group-calendar-view-calendar-event|groups.calendarView.calendar.events|[commands](#CommandsIngroups.calendarView.calendar.events)|
|az groups group-calendar-view-instance|groups.calendarView.instances|[commands](#CommandsIngroups.calendarView.instances)|
|az groups group-conversation|groups.conversations|[commands](#CommandsIngroups.conversations)|
|az groups group-conversation-thread|groups.conversations.threads|[commands](#CommandsIngroups.conversations.threads)|
|az groups group-conversation-thread-post|groups.conversations.threads.posts|[commands](#CommandsIngroups.conversations.threads.posts)|
|az groups group-conversation-thread-post-attachment|groups.conversations.threads.posts.attachments|[commands](#CommandsIngroups.conversations.threads.posts.attachments)|
|az groups group-conversation-thread-post-in-reply-to|groups.conversations.threads.posts.inReplyTo|[commands](#CommandsIngroups.conversations.threads.posts.inReplyTo)|
|az groups group-event|groups.events|[commands](#CommandsIngroups.events)|
|az groups group-event-attachment|groups.events.attachments|[commands](#CommandsIngroups.events.attachments)|
|az groups group-event-calendar|groups.events.calendar|[commands](#CommandsIngroups.events.calendar)|
|az groups group-event-calendar-calendar-view|groups.events.calendar.calendarView|[commands](#CommandsIngroups.events.calendar.calendarView)|
|az groups group-event-calendar-event|groups.events.calendar.events|[commands](#CommandsIngroups.events.calendar.events)|
|az groups group-event-instance|groups.events.instances|[commands](#CommandsIngroups.events.instances)|
|az groups group-group|groups.group|[commands](#CommandsIngroups.group)|
|az groups group-lifecycle-policy|groupLifecyclePolicies|[commands](#CommandsIngroupLifecyclePolicies)|
|az groups group-lifecycle-policy-group-lifecycle-policy|groupLifecyclePolicies.groupLifecyclePolicy|[commands](#CommandsIngroupLifecyclePolicies.groupLifecyclePolicy)|
|az groups group-onenote-notebook|groups.onenote.notebooks|[commands](#CommandsIngroups.onenote.notebooks)|
|az groups group-onenote-notebook-section|groups.onenote.notebooks.sections|[commands](#CommandsIngroups.onenote.notebooks.sections)|
|az groups group-onenote-notebook-section-group-parent-notebook|groups.onenote.notebooks.sectionGroups.parentNotebook|[commands](#CommandsIngroups.onenote.notebooks.sectionGroups.parentNotebook)|
|az groups group-onenote-notebook-section-group-section|groups.onenote.notebooks.sectionGroups.sections|[commands](#CommandsIngroups.onenote.notebooks.sectionGroups.sections)|
|az groups group-onenote-notebook-section-group-section-page|groups.onenote.notebooks.sectionGroups.sections.pages|[commands](#CommandsIngroups.onenote.notebooks.sectionGroups.sections.pages)|
|az groups group-onenote-notebook-section-group-section-page-parent-notebook|groups.onenote.notebooks.sectionGroups.sections.pages.parentNotebook|[commands](#CommandsIngroups.onenote.notebooks.sectionGroups.sections.pages.parentNotebook)|
|az groups group-onenote-notebook-section-group-section-page-parent-section|groups.onenote.notebooks.sectionGroups.sections.pages.parentSection|[commands](#CommandsIngroups.onenote.notebooks.sectionGroups.sections.pages.parentSection)|
|az groups group-onenote-notebook-section-group-section-parent-notebook|groups.onenote.notebooks.sectionGroups.sections.parentNotebook|[commands](#CommandsIngroups.onenote.notebooks.sectionGroups.sections.parentNotebook)|
|az groups group-onenote-notebook-section-page|groups.onenote.notebooks.sections.pages|[commands](#CommandsIngroups.onenote.notebooks.sections.pages)|
|az groups group-onenote-notebook-section-page-parent-notebook|groups.onenote.notebooks.sections.pages.parentNotebook|[commands](#CommandsIngroups.onenote.notebooks.sections.pages.parentNotebook)|
|az groups group-onenote-notebook-section-page-parent-section|groups.onenote.notebooks.sections.pages.parentSection|[commands](#CommandsIngroups.onenote.notebooks.sections.pages.parentSection)|
|az groups group-onenote-notebook-section-parent-notebook|groups.onenote.notebooks.sections.parentNotebook|[commands](#CommandsIngroups.onenote.notebooks.sections.parentNotebook)|
|az groups group-onenote-notebook-section-parent-section-group-parent-notebook|groups.onenote.notebooks.sections.parentSectionGroup.parentNotebook|[commands](#CommandsIngroups.onenote.notebooks.sections.parentSectionGroup.parentNotebook)|
|az groups group-onenote-notebook-section-parent-section-group-section|groups.onenote.notebooks.sections.parentSectionGroup.sections|[commands](#CommandsIngroups.onenote.notebooks.sections.parentSectionGroup.sections)|
|az groups group-onenote-page|groups.onenote.pages|[commands](#CommandsIngroups.onenote.pages)|
|az groups group-onenote-page-parent-notebook|groups.onenote.pages.parentNotebook|[commands](#CommandsIngroups.onenote.pages.parentNotebook)|
|az groups group-onenote-page-parent-notebook-section|groups.onenote.pages.parentNotebook.sections|[commands](#CommandsIngroups.onenote.pages.parentNotebook.sections)|
|az groups group-onenote-page-parent-notebook-section-group-parent-notebook|groups.onenote.pages.parentNotebook.sectionGroups.parentNotebook|[commands](#CommandsIngroups.onenote.pages.parentNotebook.sectionGroups.parentNotebook)|
|az groups group-onenote-page-parent-notebook-section-group-section|groups.onenote.pages.parentNotebook.sectionGroups.sections|[commands](#CommandsIngroups.onenote.pages.parentNotebook.sectionGroups.sections)|
|az groups group-onenote-page-parent-notebook-section-group-section-page|groups.onenote.pages.parentNotebook.sectionGroups.sections.pages|[commands](#CommandsIngroups.onenote.pages.parentNotebook.sectionGroups.sections.pages)|
|az groups group-onenote-page-parent-notebook-section-group-section-parent-notebook|groups.onenote.pages.parentNotebook.sectionGroups.sections.parentNotebook|[commands](#CommandsIngroups.onenote.pages.parentNotebook.sectionGroups.sections.parentNotebook)|
|az groups group-onenote-page-parent-notebook-section-page|groups.onenote.pages.parentNotebook.sections.pages|[commands](#CommandsIngroups.onenote.pages.parentNotebook.sections.pages)|
|az groups group-onenote-page-parent-notebook-section-parent-notebook|groups.onenote.pages.parentNotebook.sections.parentNotebook|[commands](#CommandsIngroups.onenote.pages.parentNotebook.sections.parentNotebook)|
|az groups group-onenote-page-parent-notebook-section-parent-section-group-parent-notebook|groups.onenote.pages.parentNotebook.sections.parentSectionGroup.parentNotebook|[commands](#CommandsIngroups.onenote.pages.parentNotebook.sections.parentSectionGroup.parentNotebook)|
|az groups group-onenote-page-parent-notebook-section-parent-section-group-section|groups.onenote.pages.parentNotebook.sections.parentSectionGroup.sections|[commands](#CommandsIngroups.onenote.pages.parentNotebook.sections.parentSectionGroup.sections)|
|az groups group-onenote-page-parent-section|groups.onenote.pages.parentSection|[commands](#CommandsIngroups.onenote.pages.parentSection)|
|az groups group-onenote-page-parent-section-page|groups.onenote.pages.parentSection.pages|[commands](#CommandsIngroups.onenote.pages.parentSection.pages)|
|az groups group-onenote-page-parent-section-parent-notebook|groups.onenote.pages.parentSection.parentNotebook|[commands](#CommandsIngroups.onenote.pages.parentSection.parentNotebook)|
|az groups group-onenote-page-parent-section-parent-notebook-section|groups.onenote.pages.parentSection.parentNotebook.sections|[commands](#CommandsIngroups.onenote.pages.parentSection.parentNotebook.sections)|
|az groups group-onenote-page-parent-section-parent-notebook-section-group-parent-notebook|groups.onenote.pages.parentSection.parentNotebook.sectionGroups.parentNotebook|[commands](#CommandsIngroups.onenote.pages.parentSection.parentNotebook.sectionGroups.parentNotebook)|
|az groups group-onenote-page-parent-section-parent-notebook-section-group-section|groups.onenote.pages.parentSection.parentNotebook.sectionGroups.sections|[commands](#CommandsIngroups.onenote.pages.parentSection.parentNotebook.sectionGroups.sections)|
|az groups group-onenote-page-parent-section-parent-section-group-parent-notebook|groups.onenote.pages.parentSection.parentSectionGroup.parentNotebook|[commands](#CommandsIngroups.onenote.pages.parentSection.parentSectionGroup.parentNotebook)|
|az groups group-onenote-page-parent-section-parent-section-group-parent-notebook-section|groups.onenote.pages.parentSection.parentSectionGroup.parentNotebook.sections|[commands](#CommandsIngroups.onenote.pages.parentSection.parentSectionGroup.parentNotebook.sections)|
|az groups group-onenote-page-parent-section-parent-section-group-section|groups.onenote.pages.parentSection.parentSectionGroup.sections|[commands](#CommandsIngroups.onenote.pages.parentSection.parentSectionGroup.sections)|
|az groups group-onenote-section|groups.onenote.sections|[commands](#CommandsIngroups.onenote.sections)|
|az groups group-onenote-section-group-parent-notebook|groups.onenote.sectionGroups.parentNotebook|[commands](#CommandsIngroups.onenote.sectionGroups.parentNotebook)|
|az groups group-onenote-section-group-parent-notebook-section|groups.onenote.sectionGroups.parentNotebook.sections|[commands](#CommandsIngroups.onenote.sectionGroups.parentNotebook.sections)|
|az groups group-onenote-section-group-parent-notebook-section-page|groups.onenote.sectionGroups.parentNotebook.sections.pages|[commands](#CommandsIngroups.onenote.sectionGroups.parentNotebook.sections.pages)|
|az groups group-onenote-section-group-parent-notebook-section-page-parent-notebook|groups.onenote.sectionGroups.parentNotebook.sections.pages.parentNotebook|[commands](#CommandsIngroups.onenote.sectionGroups.parentNotebook.sections.pages.parentNotebook)|
|az groups group-onenote-section-group-parent-notebook-section-page-parent-section|groups.onenote.sectionGroups.parentNotebook.sections.pages.parentSection|[commands](#CommandsIngroups.onenote.sectionGroups.parentNotebook.sections.pages.parentSection)|
|az groups group-onenote-section-group-parent-notebook-section-parent-notebook|groups.onenote.sectionGroups.parentNotebook.sections.parentNotebook|[commands](#CommandsIngroups.onenote.sectionGroups.parentNotebook.sections.parentNotebook)|
|az groups group-onenote-section-group-section|groups.onenote.sectionGroups.sections|[commands](#CommandsIngroups.onenote.sectionGroups.sections)|
|az groups group-onenote-section-group-section-page|groups.onenote.sectionGroups.sections.pages|[commands](#CommandsIngroups.onenote.sectionGroups.sections.pages)|
|az groups group-onenote-section-group-section-page-parent-notebook|groups.onenote.sectionGroups.sections.pages.parentNotebook|[commands](#CommandsIngroups.onenote.sectionGroups.sections.pages.parentNotebook)|
|az groups group-onenote-section-group-section-page-parent-notebook-section|groups.onenote.sectionGroups.sections.pages.parentNotebook.sections|[commands](#CommandsIngroups.onenote.sectionGroups.sections.pages.parentNotebook.sections)|
|az groups group-onenote-section-group-section-page-parent-section|groups.onenote.sectionGroups.sections.pages.parentSection|[commands](#CommandsIngroups.onenote.sectionGroups.sections.pages.parentSection)|
|az groups group-onenote-section-group-section-parent-notebook|groups.onenote.sectionGroups.sections.parentNotebook|[commands](#CommandsIngroups.onenote.sectionGroups.sections.parentNotebook)|
|az groups group-onenote-section-group-section-parent-notebook-section|groups.onenote.sectionGroups.sections.parentNotebook.sections|[commands](#CommandsIngroups.onenote.sectionGroups.sections.parentNotebook.sections)|
|az groups group-onenote-section-page|groups.onenote.sections.pages|[commands](#CommandsIngroups.onenote.sections.pages)|
|az groups group-onenote-section-page-parent-notebook|groups.onenote.sections.pages.parentNotebook|[commands](#CommandsIngroups.onenote.sections.pages.parentNotebook)|
|az groups group-onenote-section-page-parent-notebook-section|groups.onenote.sections.pages.parentNotebook.sections|[commands](#CommandsIngroups.onenote.sections.pages.parentNotebook.sections)|
|az groups group-onenote-section-page-parent-notebook-section-group-parent-notebook|groups.onenote.sections.pages.parentNotebook.sectionGroups.parentNotebook|[commands](#CommandsIngroups.onenote.sections.pages.parentNotebook.sectionGroups.parentNotebook)|
|az groups group-onenote-section-page-parent-notebook-section-group-section|groups.onenote.sections.pages.parentNotebook.sectionGroups.sections|[commands](#CommandsIngroups.onenote.sections.pages.parentNotebook.sectionGroups.sections)|
|az groups group-onenote-section-page-parent-section|groups.onenote.sections.pages.parentSection|[commands](#CommandsIngroups.onenote.sections.pages.parentSection)|
|az groups group-onenote-section-parent-notebook|groups.onenote.sections.parentNotebook|[commands](#CommandsIngroups.onenote.sections.parentNotebook)|
|az groups group-onenote-section-parent-notebook-section|groups.onenote.sections.parentNotebook.sections|[commands](#CommandsIngroups.onenote.sections.parentNotebook.sections)|
|az groups group-onenote-section-parent-notebook-section-group-parent-notebook|groups.onenote.sections.parentNotebook.sectionGroups.parentNotebook|[commands](#CommandsIngroups.onenote.sections.parentNotebook.sectionGroups.parentNotebook)|
|az groups group-onenote-section-parent-notebook-section-group-section|groups.onenote.sections.parentNotebook.sectionGroups.sections|[commands](#CommandsIngroups.onenote.sections.parentNotebook.sectionGroups.sections)|
|az groups group-onenote-section-parent-section-group-parent-notebook|groups.onenote.sections.parentSectionGroup.parentNotebook|[commands](#CommandsIngroups.onenote.sections.parentSectionGroup.parentNotebook)|
|az groups group-onenote-section-parent-section-group-parent-notebook-section|groups.onenote.sections.parentSectionGroup.parentNotebook.sections|[commands](#CommandsIngroups.onenote.sections.parentSectionGroup.parentNotebook.sections)|
|az groups group-onenote-section-parent-section-group-section|groups.onenote.sections.parentSectionGroup.sections|[commands](#CommandsIngroups.onenote.sections.parentSectionGroup.sections)|
|az groups group-thread|groups.threads|[commands](#CommandsIngroups.threads)|
|az groups group-thread-post|groups.threads.posts|[commands](#CommandsIngroups.threads.posts)|
|az groups group-thread-post-attachment|groups.threads.posts.attachments|[commands](#CommandsIngroups.threads.posts.attachments)|
|az groups group-thread-post-in-reply-to|groups.threads.posts.inReplyTo|[commands](#CommandsIngroups.threads.posts.inReplyTo)|

## COMMANDS
### <a name="CommandsIngroups">Commands in `az groups group` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group add-favorite](#groupsaddFavorite)|addFavorite|[Parameters](#ParametersgroupsaddFavorite)|Not Found|
|[az groups group assign-license](#groupsassignLicense)|assignLicense|[Parameters](#ParametersgroupsassignLicense)|Not Found|
|[az groups group check-granted-permission-for-app](#groupscheckGrantedPermissionsForApp)|checkGrantedPermissionsForApp|[Parameters](#ParametersgroupscheckGrantedPermissionsForApp)|Not Found|
|[az groups group check-member-group](#groupscheckMemberGroups)|checkMemberGroups|[Parameters](#ParametersgroupscheckMemberGroups)|Not Found|
|[az groups group check-member-object](#groupscheckMemberObjects)|checkMemberObjects|[Parameters](#ParametersgroupscheckMemberObjects)|Not Found|
|[az groups group create-conversation](#groupsCreateConversations)|CreateConversations|[Parameters](#ParametersgroupsCreateConversations)|Not Found|
|[az groups group create-extension](#groupsCreateExtensions)|CreateExtensions|[Parameters](#ParametersgroupsCreateExtensions)|Not Found|
|[az groups group create-permission-grant](#groupsCreatePermissionGrants)|CreatePermissionGrants|[Parameters](#ParametersgroupsCreatePermissionGrants)|Not Found|
|[az groups group create-photo](#groupsCreatePhotos)|CreatePhotos|[Parameters](#ParametersgroupsCreatePhotos)|Not Found|
|[az groups group create-ref-accepted-sender](#groupsCreateRefAcceptedSenders)|CreateRefAcceptedSenders|[Parameters](#ParametersgroupsCreateRefAcceptedSenders)|Not Found|
|[az groups group create-ref-member](#groupsCreateRefMembers)|CreateRefMembers|[Parameters](#ParametersgroupsCreateRefMembers)|Not Found|
|[az groups group create-ref-member-of](#groupsCreateRefMemberOf)|CreateRefMemberOf|[Parameters](#ParametersgroupsCreateRefMemberOf)|Not Found|
|[az groups group create-ref-member-with-license-error](#groupsCreateRefMembersWithLicenseErrors)|CreateRefMembersWithLicenseErrors|[Parameters](#ParametersgroupsCreateRefMembersWithLicenseErrors)|Not Found|
|[az groups group create-ref-owner](#groupsCreateRefOwners)|CreateRefOwners|[Parameters](#ParametersgroupsCreateRefOwners)|Not Found|
|[az groups group create-ref-rejected-sender](#groupsCreateRefRejectedSenders)|CreateRefRejectedSenders|[Parameters](#ParametersgroupsCreateRefRejectedSenders)|Not Found|
|[az groups group create-ref-transitive-member](#groupsCreateRefTransitiveMembers)|CreateRefTransitiveMembers|[Parameters](#ParametersgroupsCreateRefTransitiveMembers)|Not Found|
|[az groups group create-ref-transitive-member-of](#groupsCreateRefTransitiveMemberOf)|CreateRefTransitiveMemberOf|[Parameters](#ParametersgroupsCreateRefTransitiveMemberOf)|Not Found|
|[az groups group create-thread](#groupsCreateThreads)|CreateThreads|[Parameters](#ParametersgroupsCreateThreads)|Not Found|
|[az groups group delete-conversation](#groupsDeleteConversations)|DeleteConversations|[Parameters](#ParametersgroupsDeleteConversations)|Not Found|
|[az groups group delete-extension](#groupsDeleteExtensions)|DeleteExtensions|[Parameters](#ParametersgroupsDeleteExtensions)|Not Found|
|[az groups group delete-permission-grant](#groupsDeletePermissionGrants)|DeletePermissionGrants|[Parameters](#ParametersgroupsDeletePermissionGrants)|Not Found|
|[az groups group delete-photo](#groupsDeletePhotos)|DeletePhotos|[Parameters](#ParametersgroupsDeletePhotos)|Not Found|
|[az groups group delete-photo](#groupsDeletePhoto)|DeletePhoto|[Parameters](#ParametersgroupsDeletePhoto)|Not Found|
|[az groups group delete-ref-created-on-behalf-of](#groupsDeleteRefCreatedOnBehalfOf)|DeleteRefCreatedOnBehalfOf|[Parameters](#ParametersgroupsDeleteRefCreatedOnBehalfOf)|Not Found|
|[az groups group delete-thread](#groupsDeleteThreads)|DeleteThreads|[Parameters](#ParametersgroupsDeleteThreads)|Not Found|
|[az groups group delta](#groupsdelta)|delta|[Parameters](#Parametersgroupsdelta)|Not Found|
|[az groups group get-available-extension-property](#groupsgetAvailableExtensionProperties)|getAvailableExtensionProperties|[Parameters](#ParametersgroupsgetAvailableExtensionProperties)|Not Found|
|[az groups group get-by-id](#groupsgetByIds)|getByIds|[Parameters](#ParametersgroupsgetByIds)|Not Found|
|[az groups group get-member-group](#groupsgetMemberGroups)|getMemberGroups|[Parameters](#ParametersgroupsgetMemberGroups)|Not Found|
|[az groups group get-member-object](#groupsgetMemberObjects)|getMemberObjects|[Parameters](#ParametersgroupsgetMemberObjects)|Not Found|
|[az groups group list-accepted-sender](#groupsListAcceptedSenders)|ListAcceptedSenders|[Parameters](#ParametersgroupsListAcceptedSenders)|Not Found|
|[az groups group list-conversation](#groupsListConversations)|ListConversations|[Parameters](#ParametersgroupsListConversations)|Not Found|
|[az groups group list-extension](#groupsListExtensions)|ListExtensions|[Parameters](#ParametersgroupsListExtensions)|Not Found|
|[az groups group list-member](#groupsListMembers)|ListMembers|[Parameters](#ParametersgroupsListMembers)|Not Found|
|[az groups group list-member-of](#groupsListMemberOf)|ListMemberOf|[Parameters](#ParametersgroupsListMemberOf)|Not Found|
|[az groups group list-member-with-license-error](#groupsListMembersWithLicenseErrors)|ListMembersWithLicenseErrors|[Parameters](#ParametersgroupsListMembersWithLicenseErrors)|Not Found|
|[az groups group list-owner](#groupsListOwners)|ListOwners|[Parameters](#ParametersgroupsListOwners)|Not Found|
|[az groups group list-permission-grant](#groupsListPermissionGrants)|ListPermissionGrants|[Parameters](#ParametersgroupsListPermissionGrants)|Not Found|
|[az groups group list-photo](#groupsListPhotos)|ListPhotos|[Parameters](#ParametersgroupsListPhotos)|Not Found|
|[az groups group list-ref-accepted-sender](#groupsListRefAcceptedSenders)|ListRefAcceptedSenders|[Parameters](#ParametersgroupsListRefAcceptedSenders)|Not Found|
|[az groups group list-ref-member](#groupsListRefMembers)|ListRefMembers|[Parameters](#ParametersgroupsListRefMembers)|Not Found|
|[az groups group list-ref-member-of](#groupsListRefMemberOf)|ListRefMemberOf|[Parameters](#ParametersgroupsListRefMemberOf)|Not Found|
|[az groups group list-ref-member-with-license-error](#groupsListRefMembersWithLicenseErrors)|ListRefMembersWithLicenseErrors|[Parameters](#ParametersgroupsListRefMembersWithLicenseErrors)|Not Found|
|[az groups group list-ref-owner](#groupsListRefOwners)|ListRefOwners|[Parameters](#ParametersgroupsListRefOwners)|Not Found|
|[az groups group list-ref-rejected-sender](#groupsListRefRejectedSenders)|ListRefRejectedSenders|[Parameters](#ParametersgroupsListRefRejectedSenders)|Not Found|
|[az groups group list-ref-transitive-member](#groupsListRefTransitiveMembers)|ListRefTransitiveMembers|[Parameters](#ParametersgroupsListRefTransitiveMembers)|Not Found|
|[az groups group list-ref-transitive-member-of](#groupsListRefTransitiveMemberOf)|ListRefTransitiveMemberOf|[Parameters](#ParametersgroupsListRefTransitiveMemberOf)|Not Found|
|[az groups group list-rejected-sender](#groupsListRejectedSenders)|ListRejectedSenders|[Parameters](#ParametersgroupsListRejectedSenders)|Not Found|
|[az groups group list-thread](#groupsListThreads)|ListThreads|[Parameters](#ParametersgroupsListThreads)|Not Found|
|[az groups group list-transitive-member](#groupsListTransitiveMembers)|ListTransitiveMembers|[Parameters](#ParametersgroupsListTransitiveMembers)|Not Found|
|[az groups group list-transitive-member-of](#groupsListTransitiveMemberOf)|ListTransitiveMemberOf|[Parameters](#ParametersgroupsListTransitiveMemberOf)|Not Found|
|[az groups group remove-favorite](#groupsremoveFavorite)|removeFavorite|[Parameters](#ParametersgroupsremoveFavorite)|Not Found|
|[az groups group renew](#groupsrenew)|renew|[Parameters](#Parametersgroupsrenew)|Not Found|
|[az groups group reset-unseen-count](#groupsresetUnseenCount)|resetUnseenCount|[Parameters](#ParametersgroupsresetUnseenCount)|Not Found|
|[az groups group restore](#groupsrestore)|restore|[Parameters](#Parametersgroupsrestore)|Not Found|
|[az groups group set-photo-content](#groupsSetPhotosContent)|SetPhotosContent|[Parameters](#ParametersgroupsSetPhotosContent)|Not Found|
|[az groups group set-photo-content](#groupsSetPhotoContent)|SetPhotoContent|[Parameters](#ParametersgroupsSetPhotoContent)|Not Found|
|[az groups group set-ref-created-on-behalf-of](#groupsSetRefCreatedOnBehalfOf)|SetRefCreatedOnBehalfOf|[Parameters](#ParametersgroupsSetRefCreatedOnBehalfOf)|Not Found|
|[az groups group show-conversation](#groupsGetConversations)|GetConversations|[Parameters](#ParametersgroupsGetConversations)|Not Found|
|[az groups group show-created-on-behalf-of](#groupsGetCreatedOnBehalfOf)|GetCreatedOnBehalfOf|[Parameters](#ParametersgroupsGetCreatedOnBehalfOf)|Not Found|
|[az groups group show-extension](#groupsGetExtensions)|GetExtensions|[Parameters](#ParametersgroupsGetExtensions)|Not Found|
|[az groups group show-permission-grant](#groupsGetPermissionGrants)|GetPermissionGrants|[Parameters](#ParametersgroupsGetPermissionGrants)|Not Found|
|[az groups group show-photo](#groupsGetPhotos)|GetPhotos|[Parameters](#ParametersgroupsGetPhotos)|Not Found|
|[az groups group show-photo](#groupsGetPhoto)|GetPhoto|[Parameters](#ParametersgroupsGetPhoto)|Not Found|
|[az groups group show-photo-content](#groupsGetPhotosContent)|GetPhotosContent|[Parameters](#ParametersgroupsGetPhotosContent)|Not Found|
|[az groups group show-photo-content](#groupsGetPhotoContent)|GetPhotoContent|[Parameters](#ParametersgroupsGetPhotoContent)|Not Found|
|[az groups group show-ref-created-on-behalf-of](#groupsGetRefCreatedOnBehalfOf)|GetRefCreatedOnBehalfOf|[Parameters](#ParametersgroupsGetRefCreatedOnBehalfOf)|Not Found|
|[az groups group show-thread](#groupsGetThreads)|GetThreads|[Parameters](#ParametersgroupsGetThreads)|Not Found|
|[az groups group subscribe-by-mail](#groupssubscribeByMail)|subscribeByMail|[Parameters](#ParametersgroupssubscribeByMail)|Not Found|
|[az groups group unsubscribe-by-mail](#groupsunsubscribeByMail)|unsubscribeByMail|[Parameters](#ParametersgroupsunsubscribeByMail)|Not Found|
|[az groups group update-conversation](#groupsUpdateConversations)|UpdateConversations|[Parameters](#ParametersgroupsUpdateConversations)|Not Found|
|[az groups group update-extension](#groupsUpdateExtensions)|UpdateExtensions|[Parameters](#ParametersgroupsUpdateExtensions)|Not Found|
|[az groups group update-permission-grant](#groupsUpdatePermissionGrants)|UpdatePermissionGrants|[Parameters](#ParametersgroupsUpdatePermissionGrants)|Not Found|
|[az groups group update-photo](#groupsUpdatePhotos)|UpdatePhotos|[Parameters](#ParametersgroupsUpdatePhotos)|Not Found|
|[az groups group update-photo](#groupsUpdatePhoto)|UpdatePhoto|[Parameters](#ParametersgroupsUpdatePhoto)|Not Found|
|[az groups group update-thread](#groupsUpdateThreads)|UpdateThreads|[Parameters](#ParametersgroupsUpdateThreads)|Not Found|
|[az groups group validate-property](#groupsvalidateProperties)|validateProperties|[Parameters](#ParametersgroupsvalidateProperties)|Not Found|

### <a name="CommandsIngroups.calendar">Commands in `az groups group-calendar` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-calendar allowed-calendar-sharing-role](#groups.calendarallowedCalendarSharingRoles)|allowedCalendarSharingRoles|[Parameters](#Parametersgroups.calendarallowedCalendarSharingRoles)|Not Found|
|[az groups group-calendar get-schedule](#groups.calendargetSchedule)|getSchedule|[Parameters](#Parametersgroups.calendargetSchedule)|Not Found|

### <a name="CommandsIngroups.calendar.calendarView">Commands in `az groups group-calendar-calendar-view` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-calendar-calendar-view accept](#groups.calendar.calendarViewaccept)|accept|[Parameters](#Parametersgroups.calendar.calendarViewaccept)|Not Found|
|[az groups group-calendar-calendar-view cancel](#groups.calendar.calendarViewcancel)|cancel|[Parameters](#Parametersgroups.calendar.calendarViewcancel)|Not Found|
|[az groups group-calendar-calendar-view decline](#groups.calendar.calendarViewdecline)|decline|[Parameters](#Parametersgroups.calendar.calendarViewdecline)|Not Found|
|[az groups group-calendar-calendar-view delta](#groups.calendar.calendarViewdelta)|delta|[Parameters](#Parametersgroups.calendar.calendarViewdelta)|Not Found|
|[az groups group-calendar-calendar-view dismiss-reminder](#groups.calendar.calendarViewdismissReminder)|dismissReminder|[Parameters](#Parametersgroups.calendar.calendarViewdismissReminder)|Not Found|
|[az groups group-calendar-calendar-view forward](#groups.calendar.calendarViewforward)|forward|[Parameters](#Parametersgroups.calendar.calendarViewforward)|Not Found|
|[az groups group-calendar-calendar-view snooze-reminder](#groups.calendar.calendarViewsnoozeReminder)|snoozeReminder|[Parameters](#Parametersgroups.calendar.calendarViewsnoozeReminder)|Not Found|
|[az groups group-calendar-calendar-view tentatively-accept](#groups.calendar.calendarViewtentativelyAccept)|tentativelyAccept|[Parameters](#Parametersgroups.calendar.calendarViewtentativelyAccept)|Not Found|

### <a name="CommandsIngroups.calendar.calendarView.attachments">Commands in `az groups group-calendar-calendar-view-attachment` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-calendar-calendar-view-attachment create-upload-session](#groups.calendar.calendarView.attachmentscreateUploadSession)|createUploadSession|[Parameters](#Parametersgroups.calendar.calendarView.attachmentscreateUploadSession)|Not Found|

### <a name="CommandsIngroups.calendar.calendarView.calendar">Commands in `az groups group-calendar-calendar-view-calendar` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-calendar-calendar-view-calendar allowed-calendar-sharing-role](#groups.calendar.calendarView.calendarallowedCalendarSharingRoles)|allowedCalendarSharingRoles|[Parameters](#Parametersgroups.calendar.calendarView.calendarallowedCalendarSharingRoles)|Not Found|
|[az groups group-calendar-calendar-view-calendar get-schedule](#groups.calendar.calendarView.calendargetSchedule)|getSchedule|[Parameters](#Parametersgroups.calendar.calendarView.calendargetSchedule)|Not Found|

### <a name="CommandsIngroups.calendar.calendarView.instances">Commands in `az groups group-calendar-calendar-view-instance` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-calendar-calendar-view-instance accept](#groups.calendar.calendarView.instancesaccept)|accept|[Parameters](#Parametersgroups.calendar.calendarView.instancesaccept)|Not Found|
|[az groups group-calendar-calendar-view-instance cancel](#groups.calendar.calendarView.instancescancel)|cancel|[Parameters](#Parametersgroups.calendar.calendarView.instancescancel)|Not Found|
|[az groups group-calendar-calendar-view-instance decline](#groups.calendar.calendarView.instancesdecline)|decline|[Parameters](#Parametersgroups.calendar.calendarView.instancesdecline)|Not Found|
|[az groups group-calendar-calendar-view-instance delta](#groups.calendar.calendarView.instancesdelta)|delta|[Parameters](#Parametersgroups.calendar.calendarView.instancesdelta)|Not Found|
|[az groups group-calendar-calendar-view-instance dismiss-reminder](#groups.calendar.calendarView.instancesdismissReminder)|dismissReminder|[Parameters](#Parametersgroups.calendar.calendarView.instancesdismissReminder)|Not Found|
|[az groups group-calendar-calendar-view-instance forward](#groups.calendar.calendarView.instancesforward)|forward|[Parameters](#Parametersgroups.calendar.calendarView.instancesforward)|Not Found|
|[az groups group-calendar-calendar-view-instance snooze-reminder](#groups.calendar.calendarView.instancessnoozeReminder)|snoozeReminder|[Parameters](#Parametersgroups.calendar.calendarView.instancessnoozeReminder)|Not Found|
|[az groups group-calendar-calendar-view-instance tentatively-accept](#groups.calendar.calendarView.instancestentativelyAccept)|tentativelyAccept|[Parameters](#Parametersgroups.calendar.calendarView.instancestentativelyAccept)|Not Found|

### <a name="CommandsIngroups.calendar.events">Commands in `az groups group-calendar-event` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-calendar-event accept](#groups.calendar.eventsaccept)|accept|[Parameters](#Parametersgroups.calendar.eventsaccept)|Not Found|
|[az groups group-calendar-event cancel](#groups.calendar.eventscancel)|cancel|[Parameters](#Parametersgroups.calendar.eventscancel)|Not Found|
|[az groups group-calendar-event decline](#groups.calendar.eventsdecline)|decline|[Parameters](#Parametersgroups.calendar.eventsdecline)|Not Found|
|[az groups group-calendar-event delta](#groups.calendar.eventsdelta)|delta|[Parameters](#Parametersgroups.calendar.eventsdelta)|Not Found|
|[az groups group-calendar-event dismiss-reminder](#groups.calendar.eventsdismissReminder)|dismissReminder|[Parameters](#Parametersgroups.calendar.eventsdismissReminder)|Not Found|
|[az groups group-calendar-event forward](#groups.calendar.eventsforward)|forward|[Parameters](#Parametersgroups.calendar.eventsforward)|Not Found|
|[az groups group-calendar-event snooze-reminder](#groups.calendar.eventssnoozeReminder)|snoozeReminder|[Parameters](#Parametersgroups.calendar.eventssnoozeReminder)|Not Found|
|[az groups group-calendar-event tentatively-accept](#groups.calendar.eventstentativelyAccept)|tentativelyAccept|[Parameters](#Parametersgroups.calendar.eventstentativelyAccept)|Not Found|

### <a name="CommandsIngroups.calendar.events.attachments">Commands in `az groups group-calendar-event-attachment` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-calendar-event-attachment create-upload-session](#groups.calendar.events.attachmentscreateUploadSession)|createUploadSession|[Parameters](#Parametersgroups.calendar.events.attachmentscreateUploadSession)|Not Found|

### <a name="CommandsIngroups.calendar.events.calendar">Commands in `az groups group-calendar-event-calendar` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-calendar-event-calendar allowed-calendar-sharing-role](#groups.calendar.events.calendarallowedCalendarSharingRoles)|allowedCalendarSharingRoles|[Parameters](#Parametersgroups.calendar.events.calendarallowedCalendarSharingRoles)|Not Found|
|[az groups group-calendar-event-calendar get-schedule](#groups.calendar.events.calendargetSchedule)|getSchedule|[Parameters](#Parametersgroups.calendar.events.calendargetSchedule)|Not Found|

### <a name="CommandsIngroups.calendar.events.instances">Commands in `az groups group-calendar-event-instance` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-calendar-event-instance accept](#groups.calendar.events.instancesaccept)|accept|[Parameters](#Parametersgroups.calendar.events.instancesaccept)|Not Found|
|[az groups group-calendar-event-instance cancel](#groups.calendar.events.instancescancel)|cancel|[Parameters](#Parametersgroups.calendar.events.instancescancel)|Not Found|
|[az groups group-calendar-event-instance decline](#groups.calendar.events.instancesdecline)|decline|[Parameters](#Parametersgroups.calendar.events.instancesdecline)|Not Found|
|[az groups group-calendar-event-instance delta](#groups.calendar.events.instancesdelta)|delta|[Parameters](#Parametersgroups.calendar.events.instancesdelta)|Not Found|
|[az groups group-calendar-event-instance dismiss-reminder](#groups.calendar.events.instancesdismissReminder)|dismissReminder|[Parameters](#Parametersgroups.calendar.events.instancesdismissReminder)|Not Found|
|[az groups group-calendar-event-instance forward](#groups.calendar.events.instancesforward)|forward|[Parameters](#Parametersgroups.calendar.events.instancesforward)|Not Found|
|[az groups group-calendar-event-instance snooze-reminder](#groups.calendar.events.instancessnoozeReminder)|snoozeReminder|[Parameters](#Parametersgroups.calendar.events.instancessnoozeReminder)|Not Found|
|[az groups group-calendar-event-instance tentatively-accept](#groups.calendar.events.instancestentativelyAccept)|tentativelyAccept|[Parameters](#Parametersgroups.calendar.events.instancestentativelyAccept)|Not Found|

### <a name="CommandsIngroups.calendarView">Commands in `az groups group-calendar-view` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-calendar-view accept](#groups.calendarViewaccept)|accept|[Parameters](#Parametersgroups.calendarViewaccept)|Not Found|
|[az groups group-calendar-view cancel](#groups.calendarViewcancel)|cancel|[Parameters](#Parametersgroups.calendarViewcancel)|Not Found|
|[az groups group-calendar-view decline](#groups.calendarViewdecline)|decline|[Parameters](#Parametersgroups.calendarViewdecline)|Not Found|
|[az groups group-calendar-view delta](#groups.calendarViewdelta)|delta|[Parameters](#Parametersgroups.calendarViewdelta)|Not Found|
|[az groups group-calendar-view dismiss-reminder](#groups.calendarViewdismissReminder)|dismissReminder|[Parameters](#Parametersgroups.calendarViewdismissReminder)|Not Found|
|[az groups group-calendar-view forward](#groups.calendarViewforward)|forward|[Parameters](#Parametersgroups.calendarViewforward)|Not Found|
|[az groups group-calendar-view snooze-reminder](#groups.calendarViewsnoozeReminder)|snoozeReminder|[Parameters](#Parametersgroups.calendarViewsnoozeReminder)|Not Found|
|[az groups group-calendar-view tentatively-accept](#groups.calendarViewtentativelyAccept)|tentativelyAccept|[Parameters](#Parametersgroups.calendarViewtentativelyAccept)|Not Found|

### <a name="CommandsIngroups.calendarView.attachments">Commands in `az groups group-calendar-view-attachment` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-calendar-view-attachment create-upload-session](#groups.calendarView.attachmentscreateUploadSession)|createUploadSession|[Parameters](#Parametersgroups.calendarView.attachmentscreateUploadSession)|Not Found|

### <a name="CommandsIngroups.calendarView.calendar">Commands in `az groups group-calendar-view-calendar` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-calendar-view-calendar allowed-calendar-sharing-role](#groups.calendarView.calendarallowedCalendarSharingRoles)|allowedCalendarSharingRoles|[Parameters](#Parametersgroups.calendarView.calendarallowedCalendarSharingRoles)|Not Found|
|[az groups group-calendar-view-calendar get-schedule](#groups.calendarView.calendargetSchedule)|getSchedule|[Parameters](#Parametersgroups.calendarView.calendargetSchedule)|Not Found|

### <a name="CommandsIngroups.calendarView.calendar.calendarView">Commands in `az groups group-calendar-view-calendar-calendar-view` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-calendar-view-calendar-calendar-view accept](#groups.calendarView.calendar.calendarViewaccept)|accept|[Parameters](#Parametersgroups.calendarView.calendar.calendarViewaccept)|Not Found|
|[az groups group-calendar-view-calendar-calendar-view cancel](#groups.calendarView.calendar.calendarViewcancel)|cancel|[Parameters](#Parametersgroups.calendarView.calendar.calendarViewcancel)|Not Found|
|[az groups group-calendar-view-calendar-calendar-view decline](#groups.calendarView.calendar.calendarViewdecline)|decline|[Parameters](#Parametersgroups.calendarView.calendar.calendarViewdecline)|Not Found|
|[az groups group-calendar-view-calendar-calendar-view delta](#groups.calendarView.calendar.calendarViewdelta)|delta|[Parameters](#Parametersgroups.calendarView.calendar.calendarViewdelta)|Not Found|
|[az groups group-calendar-view-calendar-calendar-view dismiss-reminder](#groups.calendarView.calendar.calendarViewdismissReminder)|dismissReminder|[Parameters](#Parametersgroups.calendarView.calendar.calendarViewdismissReminder)|Not Found|
|[az groups group-calendar-view-calendar-calendar-view forward](#groups.calendarView.calendar.calendarViewforward)|forward|[Parameters](#Parametersgroups.calendarView.calendar.calendarViewforward)|Not Found|
|[az groups group-calendar-view-calendar-calendar-view snooze-reminder](#groups.calendarView.calendar.calendarViewsnoozeReminder)|snoozeReminder|[Parameters](#Parametersgroups.calendarView.calendar.calendarViewsnoozeReminder)|Not Found|
|[az groups group-calendar-view-calendar-calendar-view tentatively-accept](#groups.calendarView.calendar.calendarViewtentativelyAccept)|tentativelyAccept|[Parameters](#Parametersgroups.calendarView.calendar.calendarViewtentativelyAccept)|Not Found|

### <a name="CommandsIngroups.calendarView.calendar.events">Commands in `az groups group-calendar-view-calendar-event` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-calendar-view-calendar-event accept](#groups.calendarView.calendar.eventsaccept)|accept|[Parameters](#Parametersgroups.calendarView.calendar.eventsaccept)|Not Found|
|[az groups group-calendar-view-calendar-event cancel](#groups.calendarView.calendar.eventscancel)|cancel|[Parameters](#Parametersgroups.calendarView.calendar.eventscancel)|Not Found|
|[az groups group-calendar-view-calendar-event decline](#groups.calendarView.calendar.eventsdecline)|decline|[Parameters](#Parametersgroups.calendarView.calendar.eventsdecline)|Not Found|
|[az groups group-calendar-view-calendar-event delta](#groups.calendarView.calendar.eventsdelta)|delta|[Parameters](#Parametersgroups.calendarView.calendar.eventsdelta)|Not Found|
|[az groups group-calendar-view-calendar-event dismiss-reminder](#groups.calendarView.calendar.eventsdismissReminder)|dismissReminder|[Parameters](#Parametersgroups.calendarView.calendar.eventsdismissReminder)|Not Found|
|[az groups group-calendar-view-calendar-event forward](#groups.calendarView.calendar.eventsforward)|forward|[Parameters](#Parametersgroups.calendarView.calendar.eventsforward)|Not Found|
|[az groups group-calendar-view-calendar-event snooze-reminder](#groups.calendarView.calendar.eventssnoozeReminder)|snoozeReminder|[Parameters](#Parametersgroups.calendarView.calendar.eventssnoozeReminder)|Not Found|
|[az groups group-calendar-view-calendar-event tentatively-accept](#groups.calendarView.calendar.eventstentativelyAccept)|tentativelyAccept|[Parameters](#Parametersgroups.calendarView.calendar.eventstentativelyAccept)|Not Found|

### <a name="CommandsIngroups.calendarView.instances">Commands in `az groups group-calendar-view-instance` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-calendar-view-instance accept](#groups.calendarView.instancesaccept)|accept|[Parameters](#Parametersgroups.calendarView.instancesaccept)|Not Found|
|[az groups group-calendar-view-instance cancel](#groups.calendarView.instancescancel)|cancel|[Parameters](#Parametersgroups.calendarView.instancescancel)|Not Found|
|[az groups group-calendar-view-instance decline](#groups.calendarView.instancesdecline)|decline|[Parameters](#Parametersgroups.calendarView.instancesdecline)|Not Found|
|[az groups group-calendar-view-instance delta](#groups.calendarView.instancesdelta)|delta|[Parameters](#Parametersgroups.calendarView.instancesdelta)|Not Found|
|[az groups group-calendar-view-instance dismiss-reminder](#groups.calendarView.instancesdismissReminder)|dismissReminder|[Parameters](#Parametersgroups.calendarView.instancesdismissReminder)|Not Found|
|[az groups group-calendar-view-instance forward](#groups.calendarView.instancesforward)|forward|[Parameters](#Parametersgroups.calendarView.instancesforward)|Not Found|
|[az groups group-calendar-view-instance snooze-reminder](#groups.calendarView.instancessnoozeReminder)|snoozeReminder|[Parameters](#Parametersgroups.calendarView.instancessnoozeReminder)|Not Found|
|[az groups group-calendar-view-instance tentatively-accept](#groups.calendarView.instancestentativelyAccept)|tentativelyAccept|[Parameters](#Parametersgroups.calendarView.instancestentativelyAccept)|Not Found|

### <a name="CommandsIngroups.conversations">Commands in `az groups group-conversation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-conversation create-thread](#groups.conversationsCreateThreads)|CreateThreads|[Parameters](#Parametersgroups.conversationsCreateThreads)|Not Found|
|[az groups group-conversation delete-thread](#groups.conversationsDeleteThreads)|DeleteThreads|[Parameters](#Parametersgroups.conversationsDeleteThreads)|Not Found|
|[az groups group-conversation list-thread](#groups.conversationsListThreads)|ListThreads|[Parameters](#Parametersgroups.conversationsListThreads)|Not Found|
|[az groups group-conversation show-thread](#groups.conversationsGetThreads)|GetThreads|[Parameters](#Parametersgroups.conversationsGetThreads)|Not Found|
|[az groups group-conversation update-thread](#groups.conversationsUpdateThreads)|UpdateThreads|[Parameters](#Parametersgroups.conversationsUpdateThreads)|Not Found|

### <a name="CommandsIngroups.conversations.threads">Commands in `az groups group-conversation-thread` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-conversation-thread create-post](#groups.conversations.threadsCreatePosts)|CreatePosts|[Parameters](#Parametersgroups.conversations.threadsCreatePosts)|Not Found|
|[az groups group-conversation-thread delete-post](#groups.conversations.threadsDeletePosts)|DeletePosts|[Parameters](#Parametersgroups.conversations.threadsDeletePosts)|Not Found|
|[az groups group-conversation-thread list-post](#groups.conversations.threadsListPosts)|ListPosts|[Parameters](#Parametersgroups.conversations.threadsListPosts)|Not Found|
|[az groups group-conversation-thread reply](#groups.conversations.threadsreply)|reply|[Parameters](#Parametersgroups.conversations.threadsreply)|Not Found|
|[az groups group-conversation-thread show-post](#groups.conversations.threadsGetPosts)|GetPosts|[Parameters](#Parametersgroups.conversations.threadsGetPosts)|Not Found|
|[az groups group-conversation-thread update-post](#groups.conversations.threadsUpdatePosts)|UpdatePosts|[Parameters](#Parametersgroups.conversations.threadsUpdatePosts)|Not Found|

### <a name="CommandsIngroups.conversations.threads.posts">Commands in `az groups group-conversation-thread-post` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-conversation-thread-post create-attachment](#groups.conversations.threads.postsCreateAttachments)|CreateAttachments|[Parameters](#Parametersgroups.conversations.threads.postsCreateAttachments)|Not Found|
|[az groups group-conversation-thread-post create-extension](#groups.conversations.threads.postsCreateExtensions)|CreateExtensions|[Parameters](#Parametersgroups.conversations.threads.postsCreateExtensions)|Not Found|
|[az groups group-conversation-thread-post create-multi-value-extended-property](#groups.conversations.threads.postsCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersgroups.conversations.threads.postsCreateMultiValueExtendedProperties)|Not Found|
|[az groups group-conversation-thread-post create-single-value-extended-property](#groups.conversations.threads.postsCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersgroups.conversations.threads.postsCreateSingleValueExtendedProperties)|Not Found|
|[az groups group-conversation-thread-post delete-attachment](#groups.conversations.threads.postsDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersgroups.conversations.threads.postsDeleteAttachments)|Not Found|
|[az groups group-conversation-thread-post delete-extension](#groups.conversations.threads.postsDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersgroups.conversations.threads.postsDeleteExtensions)|Not Found|
|[az groups group-conversation-thread-post delete-in-reply-to](#groups.conversations.threads.postsDeleteInReplyTo)|DeleteInReplyTo|[Parameters](#Parametersgroups.conversations.threads.postsDeleteInReplyTo)|Not Found|
|[az groups group-conversation-thread-post delete-multi-value-extended-property](#groups.conversations.threads.postsDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersgroups.conversations.threads.postsDeleteMultiValueExtendedProperties)|Not Found|
|[az groups group-conversation-thread-post delete-single-value-extended-property](#groups.conversations.threads.postsDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersgroups.conversations.threads.postsDeleteSingleValueExtendedProperties)|Not Found|
|[az groups group-conversation-thread-post forward](#groups.conversations.threads.postsforward)|forward|[Parameters](#Parametersgroups.conversations.threads.postsforward)|Not Found|
|[az groups group-conversation-thread-post list-attachment](#groups.conversations.threads.postsListAttachments)|ListAttachments|[Parameters](#Parametersgroups.conversations.threads.postsListAttachments)|Not Found|
|[az groups group-conversation-thread-post list-extension](#groups.conversations.threads.postsListExtensions)|ListExtensions|[Parameters](#Parametersgroups.conversations.threads.postsListExtensions)|Not Found|
|[az groups group-conversation-thread-post list-multi-value-extended-property](#groups.conversations.threads.postsListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersgroups.conversations.threads.postsListMultiValueExtendedProperties)|Not Found|
|[az groups group-conversation-thread-post list-single-value-extended-property](#groups.conversations.threads.postsListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersgroups.conversations.threads.postsListSingleValueExtendedProperties)|Not Found|
|[az groups group-conversation-thread-post reply](#groups.conversations.threads.postsreply)|reply|[Parameters](#Parametersgroups.conversations.threads.postsreply)|Not Found|
|[az groups group-conversation-thread-post show-attachment](#groups.conversations.threads.postsGetAttachments)|GetAttachments|[Parameters](#Parametersgroups.conversations.threads.postsGetAttachments)|Not Found|
|[az groups group-conversation-thread-post show-extension](#groups.conversations.threads.postsGetExtensions)|GetExtensions|[Parameters](#Parametersgroups.conversations.threads.postsGetExtensions)|Not Found|
|[az groups group-conversation-thread-post show-in-reply-to](#groups.conversations.threads.postsGetInReplyTo)|GetInReplyTo|[Parameters](#Parametersgroups.conversations.threads.postsGetInReplyTo)|Not Found|
|[az groups group-conversation-thread-post show-multi-value-extended-property](#groups.conversations.threads.postsGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersgroups.conversations.threads.postsGetMultiValueExtendedProperties)|Not Found|
|[az groups group-conversation-thread-post show-single-value-extended-property](#groups.conversations.threads.postsGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersgroups.conversations.threads.postsGetSingleValueExtendedProperties)|Not Found|
|[az groups group-conversation-thread-post update-attachment](#groups.conversations.threads.postsUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersgroups.conversations.threads.postsUpdateAttachments)|Not Found|
|[az groups group-conversation-thread-post update-extension](#groups.conversations.threads.postsUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersgroups.conversations.threads.postsUpdateExtensions)|Not Found|
|[az groups group-conversation-thread-post update-in-reply-to](#groups.conversations.threads.postsUpdateInReplyTo)|UpdateInReplyTo|[Parameters](#Parametersgroups.conversations.threads.postsUpdateInReplyTo)|Not Found|
|[az groups group-conversation-thread-post update-multi-value-extended-property](#groups.conversations.threads.postsUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersgroups.conversations.threads.postsUpdateMultiValueExtendedProperties)|Not Found|
|[az groups group-conversation-thread-post update-single-value-extended-property](#groups.conversations.threads.postsUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersgroups.conversations.threads.postsUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsIngroups.conversations.threads.posts.attachments">Commands in `az groups group-conversation-thread-post-attachment` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-conversation-thread-post-attachment create-upload-session](#groups.conversations.threads.posts.attachmentscreateUploadSession)|createUploadSession|[Parameters](#Parametersgroups.conversations.threads.posts.attachmentscreateUploadSession)|Not Found|

### <a name="CommandsIngroups.conversations.threads.posts.inReplyTo">Commands in `az groups group-conversation-thread-post-in-reply-to` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-conversation-thread-post-in-reply-to forward](#groups.conversations.threads.posts.inReplyToforward)|forward|[Parameters](#Parametersgroups.conversations.threads.posts.inReplyToforward)|Not Found|
|[az groups group-conversation-thread-post-in-reply-to reply](#groups.conversations.threads.posts.inReplyToreply)|reply|[Parameters](#Parametersgroups.conversations.threads.posts.inReplyToreply)|Not Found|

### <a name="CommandsIngroups.events">Commands in `az groups group-event` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-event accept](#groups.eventsaccept)|accept|[Parameters](#Parametersgroups.eventsaccept)|Not Found|
|[az groups group-event cancel](#groups.eventscancel)|cancel|[Parameters](#Parametersgroups.eventscancel)|Not Found|
|[az groups group-event decline](#groups.eventsdecline)|decline|[Parameters](#Parametersgroups.eventsdecline)|Not Found|
|[az groups group-event delta](#groups.eventsdelta)|delta|[Parameters](#Parametersgroups.eventsdelta)|Not Found|
|[az groups group-event dismiss-reminder](#groups.eventsdismissReminder)|dismissReminder|[Parameters](#Parametersgroups.eventsdismissReminder)|Not Found|
|[az groups group-event forward](#groups.eventsforward)|forward|[Parameters](#Parametersgroups.eventsforward)|Not Found|
|[az groups group-event snooze-reminder](#groups.eventssnoozeReminder)|snoozeReminder|[Parameters](#Parametersgroups.eventssnoozeReminder)|Not Found|
|[az groups group-event tentatively-accept](#groups.eventstentativelyAccept)|tentativelyAccept|[Parameters](#Parametersgroups.eventstentativelyAccept)|Not Found|

### <a name="CommandsIngroups.events.attachments">Commands in `az groups group-event-attachment` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-event-attachment create-upload-session](#groups.events.attachmentscreateUploadSession)|createUploadSession|[Parameters](#Parametersgroups.events.attachmentscreateUploadSession)|Not Found|

### <a name="CommandsIngroups.events.calendar">Commands in `az groups group-event-calendar` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-event-calendar allowed-calendar-sharing-role](#groups.events.calendarallowedCalendarSharingRoles)|allowedCalendarSharingRoles|[Parameters](#Parametersgroups.events.calendarallowedCalendarSharingRoles)|Not Found|
|[az groups group-event-calendar get-schedule](#groups.events.calendargetSchedule)|getSchedule|[Parameters](#Parametersgroups.events.calendargetSchedule)|Not Found|

### <a name="CommandsIngroups.events.calendar.calendarView">Commands in `az groups group-event-calendar-calendar-view` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-event-calendar-calendar-view accept](#groups.events.calendar.calendarViewaccept)|accept|[Parameters](#Parametersgroups.events.calendar.calendarViewaccept)|Not Found|
|[az groups group-event-calendar-calendar-view cancel](#groups.events.calendar.calendarViewcancel)|cancel|[Parameters](#Parametersgroups.events.calendar.calendarViewcancel)|Not Found|
|[az groups group-event-calendar-calendar-view decline](#groups.events.calendar.calendarViewdecline)|decline|[Parameters](#Parametersgroups.events.calendar.calendarViewdecline)|Not Found|
|[az groups group-event-calendar-calendar-view delta](#groups.events.calendar.calendarViewdelta)|delta|[Parameters](#Parametersgroups.events.calendar.calendarViewdelta)|Not Found|
|[az groups group-event-calendar-calendar-view dismiss-reminder](#groups.events.calendar.calendarViewdismissReminder)|dismissReminder|[Parameters](#Parametersgroups.events.calendar.calendarViewdismissReminder)|Not Found|
|[az groups group-event-calendar-calendar-view forward](#groups.events.calendar.calendarViewforward)|forward|[Parameters](#Parametersgroups.events.calendar.calendarViewforward)|Not Found|
|[az groups group-event-calendar-calendar-view snooze-reminder](#groups.events.calendar.calendarViewsnoozeReminder)|snoozeReminder|[Parameters](#Parametersgroups.events.calendar.calendarViewsnoozeReminder)|Not Found|
|[az groups group-event-calendar-calendar-view tentatively-accept](#groups.events.calendar.calendarViewtentativelyAccept)|tentativelyAccept|[Parameters](#Parametersgroups.events.calendar.calendarViewtentativelyAccept)|Not Found|

### <a name="CommandsIngroups.events.calendar.events">Commands in `az groups group-event-calendar-event` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-event-calendar-event accept](#groups.events.calendar.eventsaccept)|accept|[Parameters](#Parametersgroups.events.calendar.eventsaccept)|Not Found|
|[az groups group-event-calendar-event cancel](#groups.events.calendar.eventscancel)|cancel|[Parameters](#Parametersgroups.events.calendar.eventscancel)|Not Found|
|[az groups group-event-calendar-event decline](#groups.events.calendar.eventsdecline)|decline|[Parameters](#Parametersgroups.events.calendar.eventsdecline)|Not Found|
|[az groups group-event-calendar-event delta](#groups.events.calendar.eventsdelta)|delta|[Parameters](#Parametersgroups.events.calendar.eventsdelta)|Not Found|
|[az groups group-event-calendar-event dismiss-reminder](#groups.events.calendar.eventsdismissReminder)|dismissReminder|[Parameters](#Parametersgroups.events.calendar.eventsdismissReminder)|Not Found|
|[az groups group-event-calendar-event forward](#groups.events.calendar.eventsforward)|forward|[Parameters](#Parametersgroups.events.calendar.eventsforward)|Not Found|
|[az groups group-event-calendar-event snooze-reminder](#groups.events.calendar.eventssnoozeReminder)|snoozeReminder|[Parameters](#Parametersgroups.events.calendar.eventssnoozeReminder)|Not Found|
|[az groups group-event-calendar-event tentatively-accept](#groups.events.calendar.eventstentativelyAccept)|tentativelyAccept|[Parameters](#Parametersgroups.events.calendar.eventstentativelyAccept)|Not Found|

### <a name="CommandsIngroups.events.instances">Commands in `az groups group-event-instance` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-event-instance accept](#groups.events.instancesaccept)|accept|[Parameters](#Parametersgroups.events.instancesaccept)|Not Found|
|[az groups group-event-instance cancel](#groups.events.instancescancel)|cancel|[Parameters](#Parametersgroups.events.instancescancel)|Not Found|
|[az groups group-event-instance decline](#groups.events.instancesdecline)|decline|[Parameters](#Parametersgroups.events.instancesdecline)|Not Found|
|[az groups group-event-instance delta](#groups.events.instancesdelta)|delta|[Parameters](#Parametersgroups.events.instancesdelta)|Not Found|
|[az groups group-event-instance dismiss-reminder](#groups.events.instancesdismissReminder)|dismissReminder|[Parameters](#Parametersgroups.events.instancesdismissReminder)|Not Found|
|[az groups group-event-instance forward](#groups.events.instancesforward)|forward|[Parameters](#Parametersgroups.events.instancesforward)|Not Found|
|[az groups group-event-instance snooze-reminder](#groups.events.instancessnoozeReminder)|snoozeReminder|[Parameters](#Parametersgroups.events.instancessnoozeReminder)|Not Found|
|[az groups group-event-instance tentatively-accept](#groups.events.instancestentativelyAccept)|tentativelyAccept|[Parameters](#Parametersgroups.events.instancestentativelyAccept)|Not Found|

### <a name="CommandsIngroups.group">Commands in `az groups group-group` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-group create-group](#groups.groupCreateGroup)|CreateGroup|[Parameters](#Parametersgroups.groupCreateGroup)|Not Found|
|[az groups group-group delete-group](#groups.groupDeleteGroup)|DeleteGroup|[Parameters](#Parametersgroups.groupDeleteGroup)|Not Found|
|[az groups group-group list-group](#groups.groupListGroup)|ListGroup|[Parameters](#Parametersgroups.groupListGroup)|Not Found|
|[az groups group-group show-group](#groups.groupGetGroup)|GetGroup|[Parameters](#Parametersgroups.groupGetGroup)|Not Found|
|[az groups group-group update-group](#groups.groupUpdateGroup)|UpdateGroup|[Parameters](#Parametersgroups.groupUpdateGroup)|Not Found|

### <a name="CommandsIngroupLifecyclePolicies">Commands in `az groups group-lifecycle-policy` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-lifecycle-policy add-group](#groupLifecyclePoliciesaddGroup)|addGroup|[Parameters](#ParametersgroupLifecyclePoliciesaddGroup)|Not Found|
|[az groups group-lifecycle-policy remove-group](#groupLifecyclePoliciesremoveGroup)|removeGroup|[Parameters](#ParametersgroupLifecyclePoliciesremoveGroup)|Not Found|

### <a name="CommandsIngroupLifecyclePolicies.groupLifecyclePolicy">Commands in `az groups group-lifecycle-policy-group-lifecycle-policy` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-lifecycle-policy-group-lifecycle-policy create-group-lifecycle-policy](#groupLifecyclePolicies.groupLifecyclePolicyCreateGroupLifecyclePolicy)|CreateGroupLifecyclePolicy|[Parameters](#ParametersgroupLifecyclePolicies.groupLifecyclePolicyCreateGroupLifecyclePolicy)|Not Found|
|[az groups group-lifecycle-policy-group-lifecycle-policy delete-group-lifecycle-policy](#groupLifecyclePolicies.groupLifecyclePolicyDeleteGroupLifecyclePolicy)|DeleteGroupLifecyclePolicy|[Parameters](#ParametersgroupLifecyclePolicies.groupLifecyclePolicyDeleteGroupLifecyclePolicy)|Not Found|
|[az groups group-lifecycle-policy-group-lifecycle-policy list-group-lifecycle-policy](#groupLifecyclePolicies.groupLifecyclePolicyListGroupLifecyclePolicy)|ListGroupLifecyclePolicy|[Parameters](#ParametersgroupLifecyclePolicies.groupLifecyclePolicyListGroupLifecyclePolicy)|Not Found|
|[az groups group-lifecycle-policy-group-lifecycle-policy show-group-lifecycle-policy](#groupLifecyclePolicies.groupLifecyclePolicyGetGroupLifecyclePolicy)|GetGroupLifecyclePolicy|[Parameters](#ParametersgroupLifecyclePolicies.groupLifecyclePolicyGetGroupLifecyclePolicy)|Not Found|
|[az groups group-lifecycle-policy-group-lifecycle-policy update-group-lifecycle-policy](#groupLifecyclePolicies.groupLifecyclePolicyUpdateGroupLifecyclePolicy)|UpdateGroupLifecyclePolicy|[Parameters](#ParametersgroupLifecyclePolicies.groupLifecyclePolicyUpdateGroupLifecyclePolicy)|Not Found|

### <a name="CommandsIngroups.onenote.notebooks">Commands in `az groups group-onenote-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-notebook copy-notebook](#groups.onenote.notebookscopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.notebookscopyNotebook)|Not Found|
|[az groups group-onenote-notebook get-notebook-from-web-url](#groups.onenote.notebooksgetNotebookFromWebUrl)|getNotebookFromWebUrl|[Parameters](#Parametersgroups.onenote.notebooksgetNotebookFromWebUrl)|Not Found|
|[az groups group-onenote-notebook show-recent-notebook](#groups.onenote.notebooksgetRecentNotebooks)|getRecentNotebooks|[Parameters](#Parametersgroups.onenote.notebooksgetRecentNotebooks)|Not Found|

### <a name="CommandsIngroups.onenote.notebooks.sections">Commands in `az groups group-onenote-notebook-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-notebook-section copy-to-notebook](#groups.onenote.notebooks.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.notebooks.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-notebook-section copy-to-section-group](#groups.onenote.notebooks.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.notebooks.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.notebooks.sectionGroups.parentNotebook">Commands in `az groups group-onenote-notebook-section-group-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-notebook-section-group-parent-notebook copy-notebook](#groups.onenote.notebooks.sectionGroups.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.notebooks.sectionGroups.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.notebooks.sectionGroups.sections">Commands in `az groups group-onenote-notebook-section-group-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-notebook-section-group-section copy-to-notebook](#groups.onenote.notebooks.sectionGroups.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.notebooks.sectionGroups.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-notebook-section-group-section copy-to-section-group](#groups.onenote.notebooks.sectionGroups.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.notebooks.sectionGroups.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.notebooks.sectionGroups.sections.pages">Commands in `az groups group-onenote-notebook-section-group-section-page` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-notebook-section-group-section-page copy-to-section](#groups.onenote.notebooks.sectionGroups.sections.pagescopyToSection)|copyToSection|[Parameters](#Parametersgroups.onenote.notebooks.sectionGroups.sections.pagescopyToSection)|Not Found|
|[az groups group-onenote-notebook-section-group-section-page onenote-patch-content](#groups.onenote.notebooks.sectionGroups.sections.pagesonenotePatchContent)|onenotePatchContent|[Parameters](#Parametersgroups.onenote.notebooks.sectionGroups.sections.pagesonenotePatchContent)|Not Found|
|[az groups group-onenote-notebook-section-group-section-page preview](#groups.onenote.notebooks.sectionGroups.sections.pagespreview)|preview|[Parameters](#Parametersgroups.onenote.notebooks.sectionGroups.sections.pagespreview)|Not Found|

### <a name="CommandsIngroups.onenote.notebooks.sectionGroups.sections.pages.parentNotebook">Commands in `az groups group-onenote-notebook-section-group-section-page-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-notebook-section-group-section-page-parent-notebook copy-notebook](#groups.onenote.notebooks.sectionGroups.sections.pages.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.notebooks.sectionGroups.sections.pages.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.notebooks.sectionGroups.sections.pages.parentSection">Commands in `az groups group-onenote-notebook-section-group-section-page-parent-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-notebook-section-group-section-page-parent-section copy-to-notebook](#groups.onenote.notebooks.sectionGroups.sections.pages.parentSectioncopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.notebooks.sectionGroups.sections.pages.parentSectioncopyToNotebook)|Not Found|
|[az groups group-onenote-notebook-section-group-section-page-parent-section copy-to-section-group](#groups.onenote.notebooks.sectionGroups.sections.pages.parentSectioncopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.notebooks.sectionGroups.sections.pages.parentSectioncopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.notebooks.sectionGroups.sections.parentNotebook">Commands in `az groups group-onenote-notebook-section-group-section-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-notebook-section-group-section-parent-notebook copy-notebook](#groups.onenote.notebooks.sectionGroups.sections.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.notebooks.sectionGroups.sections.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.notebooks.sections.pages">Commands in `az groups group-onenote-notebook-section-page` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-notebook-section-page copy-to-section](#groups.onenote.notebooks.sections.pagescopyToSection)|copyToSection|[Parameters](#Parametersgroups.onenote.notebooks.sections.pagescopyToSection)|Not Found|
|[az groups group-onenote-notebook-section-page onenote-patch-content](#groups.onenote.notebooks.sections.pagesonenotePatchContent)|onenotePatchContent|[Parameters](#Parametersgroups.onenote.notebooks.sections.pagesonenotePatchContent)|Not Found|
|[az groups group-onenote-notebook-section-page preview](#groups.onenote.notebooks.sections.pagespreview)|preview|[Parameters](#Parametersgroups.onenote.notebooks.sections.pagespreview)|Not Found|

### <a name="CommandsIngroups.onenote.notebooks.sections.pages.parentNotebook">Commands in `az groups group-onenote-notebook-section-page-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-notebook-section-page-parent-notebook copy-notebook](#groups.onenote.notebooks.sections.pages.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.notebooks.sections.pages.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.notebooks.sections.pages.parentSection">Commands in `az groups group-onenote-notebook-section-page-parent-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-notebook-section-page-parent-section copy-to-notebook](#groups.onenote.notebooks.sections.pages.parentSectioncopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.notebooks.sections.pages.parentSectioncopyToNotebook)|Not Found|
|[az groups group-onenote-notebook-section-page-parent-section copy-to-section-group](#groups.onenote.notebooks.sections.pages.parentSectioncopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.notebooks.sections.pages.parentSectioncopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.notebooks.sections.parentNotebook">Commands in `az groups group-onenote-notebook-section-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-notebook-section-parent-notebook copy-notebook](#groups.onenote.notebooks.sections.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.notebooks.sections.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.notebooks.sections.parentSectionGroup.parentNotebook">Commands in `az groups group-onenote-notebook-section-parent-section-group-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-notebook-section-parent-section-group-parent-notebook copy-notebook](#groups.onenote.notebooks.sections.parentSectionGroup.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.notebooks.sections.parentSectionGroup.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.notebooks.sections.parentSectionGroup.sections">Commands in `az groups group-onenote-notebook-section-parent-section-group-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-notebook-section-parent-section-group-section copy-to-notebook](#groups.onenote.notebooks.sections.parentSectionGroup.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.notebooks.sections.parentSectionGroup.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-notebook-section-parent-section-group-section copy-to-section-group](#groups.onenote.notebooks.sections.parentSectionGroup.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.notebooks.sections.parentSectionGroup.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.pages">Commands in `az groups group-onenote-page` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page copy-to-section](#groups.onenote.pagescopyToSection)|copyToSection|[Parameters](#Parametersgroups.onenote.pagescopyToSection)|Not Found|
|[az groups group-onenote-page onenote-patch-content](#groups.onenote.pagesonenotePatchContent)|onenotePatchContent|[Parameters](#Parametersgroups.onenote.pagesonenotePatchContent)|Not Found|
|[az groups group-onenote-page preview](#groups.onenote.pagespreview)|preview|[Parameters](#Parametersgroups.onenote.pagespreview)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentNotebook">Commands in `az groups group-onenote-page-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-notebook copy-notebook](#groups.onenote.pages.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.pages.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentNotebook.sections">Commands in `az groups group-onenote-page-parent-notebook-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-notebook-section copy-to-notebook](#groups.onenote.pages.parentNotebook.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-page-parent-notebook-section copy-to-section-group](#groups.onenote.pages.parentNotebook.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentNotebook.sectionGroups.parentNotebook">Commands in `az groups group-onenote-page-parent-notebook-section-group-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-notebook-section-group-parent-notebook copy-notebook](#groups.onenote.pages.parentNotebook.sectionGroups.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sectionGroups.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentNotebook.sectionGroups.sections">Commands in `az groups group-onenote-page-parent-notebook-section-group-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-notebook-section-group-section copy-to-notebook](#groups.onenote.pages.parentNotebook.sectionGroups.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sectionGroups.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-page-parent-notebook-section-group-section copy-to-section-group](#groups.onenote.pages.parentNotebook.sectionGroups.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sectionGroups.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentNotebook.sectionGroups.sections.pages">Commands in `az groups group-onenote-page-parent-notebook-section-group-section-page` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-notebook-section-group-section-page copy-to-section](#groups.onenote.pages.parentNotebook.sectionGroups.sections.pagescopyToSection)|copyToSection|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sectionGroups.sections.pagescopyToSection)|Not Found|
|[az groups group-onenote-page-parent-notebook-section-group-section-page onenote-patch-content](#groups.onenote.pages.parentNotebook.sectionGroups.sections.pagesonenotePatchContent)|onenotePatchContent|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sectionGroups.sections.pagesonenotePatchContent)|Not Found|
|[az groups group-onenote-page-parent-notebook-section-group-section-page preview](#groups.onenote.pages.parentNotebook.sectionGroups.sections.pagespreview)|preview|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sectionGroups.sections.pagespreview)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentNotebook.sectionGroups.sections.parentNotebook">Commands in `az groups group-onenote-page-parent-notebook-section-group-section-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-notebook-section-group-section-parent-notebook copy-notebook](#groups.onenote.pages.parentNotebook.sectionGroups.sections.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sectionGroups.sections.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentNotebook.sections.pages">Commands in `az groups group-onenote-page-parent-notebook-section-page` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-notebook-section-page copy-to-section](#groups.onenote.pages.parentNotebook.sections.pagescopyToSection)|copyToSection|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sections.pagescopyToSection)|Not Found|
|[az groups group-onenote-page-parent-notebook-section-page onenote-patch-content](#groups.onenote.pages.parentNotebook.sections.pagesonenotePatchContent)|onenotePatchContent|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sections.pagesonenotePatchContent)|Not Found|
|[az groups group-onenote-page-parent-notebook-section-page preview](#groups.onenote.pages.parentNotebook.sections.pagespreview)|preview|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sections.pagespreview)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentNotebook.sections.parentNotebook">Commands in `az groups group-onenote-page-parent-notebook-section-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-notebook-section-parent-notebook copy-notebook](#groups.onenote.pages.parentNotebook.sections.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sections.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentNotebook.sections.parentSectionGroup.parentNotebook">Commands in `az groups group-onenote-page-parent-notebook-section-parent-section-group-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-notebook-section-parent-section-group-parent-notebook copy-notebook](#groups.onenote.pages.parentNotebook.sections.parentSectionGroup.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sections.parentSectionGroup.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentNotebook.sections.parentSectionGroup.sections">Commands in `az groups group-onenote-page-parent-notebook-section-parent-section-group-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-notebook-section-parent-section-group-section copy-to-notebook](#groups.onenote.pages.parentNotebook.sections.parentSectionGroup.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sections.parentSectionGroup.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-page-parent-notebook-section-parent-section-group-section copy-to-section-group](#groups.onenote.pages.parentNotebook.sections.parentSectionGroup.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.pages.parentNotebook.sections.parentSectionGroup.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentSection">Commands in `az groups group-onenote-page-parent-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-section copy-to-notebook](#groups.onenote.pages.parentSectioncopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.pages.parentSectioncopyToNotebook)|Not Found|
|[az groups group-onenote-page-parent-section copy-to-section-group](#groups.onenote.pages.parentSectioncopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.pages.parentSectioncopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentSection.pages">Commands in `az groups group-onenote-page-parent-section-page` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-section-page copy-to-section](#groups.onenote.pages.parentSection.pagescopyToSection)|copyToSection|[Parameters](#Parametersgroups.onenote.pages.parentSection.pagescopyToSection)|Not Found|
|[az groups group-onenote-page-parent-section-page onenote-patch-content](#groups.onenote.pages.parentSection.pagesonenotePatchContent)|onenotePatchContent|[Parameters](#Parametersgroups.onenote.pages.parentSection.pagesonenotePatchContent)|Not Found|
|[az groups group-onenote-page-parent-section-page preview](#groups.onenote.pages.parentSection.pagespreview)|preview|[Parameters](#Parametersgroups.onenote.pages.parentSection.pagespreview)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentSection.parentNotebook">Commands in `az groups group-onenote-page-parent-section-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-section-parent-notebook copy-notebook](#groups.onenote.pages.parentSection.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.pages.parentSection.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentSection.parentNotebook.sections">Commands in `az groups group-onenote-page-parent-section-parent-notebook-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-section-parent-notebook-section copy-to-notebook](#groups.onenote.pages.parentSection.parentNotebook.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.pages.parentSection.parentNotebook.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-page-parent-section-parent-notebook-section copy-to-section-group](#groups.onenote.pages.parentSection.parentNotebook.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.pages.parentSection.parentNotebook.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentSection.parentNotebook.sectionGroups.parentNotebook">Commands in `az groups group-onenote-page-parent-section-parent-notebook-section-group-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-section-parent-notebook-section-group-parent-notebook copy-notebook](#groups.onenote.pages.parentSection.parentNotebook.sectionGroups.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.pages.parentSection.parentNotebook.sectionGroups.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentSection.parentNotebook.sectionGroups.sections">Commands in `az groups group-onenote-page-parent-section-parent-notebook-section-group-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-section-parent-notebook-section-group-section copy-to-notebook](#groups.onenote.pages.parentSection.parentNotebook.sectionGroups.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.pages.parentSection.parentNotebook.sectionGroups.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-page-parent-section-parent-notebook-section-group-section copy-to-section-group](#groups.onenote.pages.parentSection.parentNotebook.sectionGroups.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.pages.parentSection.parentNotebook.sectionGroups.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentSection.parentSectionGroup.parentNotebook">Commands in `az groups group-onenote-page-parent-section-parent-section-group-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-section-parent-section-group-parent-notebook copy-notebook](#groups.onenote.pages.parentSection.parentSectionGroup.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.pages.parentSection.parentSectionGroup.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentSection.parentSectionGroup.parentNotebook.sections">Commands in `az groups group-onenote-page-parent-section-parent-section-group-parent-notebook-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-section-parent-section-group-parent-notebook-section copy-to-notebook](#groups.onenote.pages.parentSection.parentSectionGroup.parentNotebook.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.pages.parentSection.parentSectionGroup.parentNotebook.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-page-parent-section-parent-section-group-parent-notebook-section copy-to-section-group](#groups.onenote.pages.parentSection.parentSectionGroup.parentNotebook.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.pages.parentSection.parentSectionGroup.parentNotebook.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.pages.parentSection.parentSectionGroup.sections">Commands in `az groups group-onenote-page-parent-section-parent-section-group-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-page-parent-section-parent-section-group-section copy-to-notebook](#groups.onenote.pages.parentSection.parentSectionGroup.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.pages.parentSection.parentSectionGroup.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-page-parent-section-parent-section-group-section copy-to-section-group](#groups.onenote.pages.parentSection.parentSectionGroup.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.pages.parentSection.parentSectionGroup.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.sections">Commands in `az groups group-onenote-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section copy-to-notebook](#groups.onenote.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-section copy-to-section-group](#groups.onenote.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.sectionGroups.parentNotebook">Commands in `az groups group-onenote-section-group-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-group-parent-notebook copy-notebook](#groups.onenote.sectionGroups.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.sectionGroups.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.sectionGroups.parentNotebook.sections">Commands in `az groups group-onenote-section-group-parent-notebook-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-group-parent-notebook-section copy-to-notebook](#groups.onenote.sectionGroups.parentNotebook.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.sectionGroups.parentNotebook.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-section-group-parent-notebook-section copy-to-section-group](#groups.onenote.sectionGroups.parentNotebook.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.sectionGroups.parentNotebook.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.sectionGroups.parentNotebook.sections.pages">Commands in `az groups group-onenote-section-group-parent-notebook-section-page` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-group-parent-notebook-section-page copy-to-section](#groups.onenote.sectionGroups.parentNotebook.sections.pagescopyToSection)|copyToSection|[Parameters](#Parametersgroups.onenote.sectionGroups.parentNotebook.sections.pagescopyToSection)|Not Found|
|[az groups group-onenote-section-group-parent-notebook-section-page onenote-patch-content](#groups.onenote.sectionGroups.parentNotebook.sections.pagesonenotePatchContent)|onenotePatchContent|[Parameters](#Parametersgroups.onenote.sectionGroups.parentNotebook.sections.pagesonenotePatchContent)|Not Found|
|[az groups group-onenote-section-group-parent-notebook-section-page preview](#groups.onenote.sectionGroups.parentNotebook.sections.pagespreview)|preview|[Parameters](#Parametersgroups.onenote.sectionGroups.parentNotebook.sections.pagespreview)|Not Found|

### <a name="CommandsIngroups.onenote.sectionGroups.parentNotebook.sections.pages.parentNotebook">Commands in `az groups group-onenote-section-group-parent-notebook-section-page-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-group-parent-notebook-section-page-parent-notebook copy-notebook](#groups.onenote.sectionGroups.parentNotebook.sections.pages.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.sectionGroups.parentNotebook.sections.pages.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.sectionGroups.parentNotebook.sections.pages.parentSection">Commands in `az groups group-onenote-section-group-parent-notebook-section-page-parent-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-group-parent-notebook-section-page-parent-section copy-to-notebook](#groups.onenote.sectionGroups.parentNotebook.sections.pages.parentSectioncopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.sectionGroups.parentNotebook.sections.pages.parentSectioncopyToNotebook)|Not Found|
|[az groups group-onenote-section-group-parent-notebook-section-page-parent-section copy-to-section-group](#groups.onenote.sectionGroups.parentNotebook.sections.pages.parentSectioncopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.sectionGroups.parentNotebook.sections.pages.parentSectioncopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.sectionGroups.parentNotebook.sections.parentNotebook">Commands in `az groups group-onenote-section-group-parent-notebook-section-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-group-parent-notebook-section-parent-notebook copy-notebook](#groups.onenote.sectionGroups.parentNotebook.sections.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.sectionGroups.parentNotebook.sections.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.sectionGroups.sections">Commands in `az groups group-onenote-section-group-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-group-section copy-to-notebook](#groups.onenote.sectionGroups.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.sectionGroups.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-section-group-section copy-to-section-group](#groups.onenote.sectionGroups.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.sectionGroups.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.sectionGroups.sections.pages">Commands in `az groups group-onenote-section-group-section-page` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-group-section-page copy-to-section](#groups.onenote.sectionGroups.sections.pagescopyToSection)|copyToSection|[Parameters](#Parametersgroups.onenote.sectionGroups.sections.pagescopyToSection)|Not Found|
|[az groups group-onenote-section-group-section-page onenote-patch-content](#groups.onenote.sectionGroups.sections.pagesonenotePatchContent)|onenotePatchContent|[Parameters](#Parametersgroups.onenote.sectionGroups.sections.pagesonenotePatchContent)|Not Found|
|[az groups group-onenote-section-group-section-page preview](#groups.onenote.sectionGroups.sections.pagespreview)|preview|[Parameters](#Parametersgroups.onenote.sectionGroups.sections.pagespreview)|Not Found|

### <a name="CommandsIngroups.onenote.sectionGroups.sections.pages.parentNotebook">Commands in `az groups group-onenote-section-group-section-page-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-group-section-page-parent-notebook copy-notebook](#groups.onenote.sectionGroups.sections.pages.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.sectionGroups.sections.pages.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.sectionGroups.sections.pages.parentNotebook.sections">Commands in `az groups group-onenote-section-group-section-page-parent-notebook-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-group-section-page-parent-notebook-section copy-to-notebook](#groups.onenote.sectionGroups.sections.pages.parentNotebook.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.sectionGroups.sections.pages.parentNotebook.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-section-group-section-page-parent-notebook-section copy-to-section-group](#groups.onenote.sectionGroups.sections.pages.parentNotebook.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.sectionGroups.sections.pages.parentNotebook.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.sectionGroups.sections.pages.parentSection">Commands in `az groups group-onenote-section-group-section-page-parent-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-group-section-page-parent-section copy-to-notebook](#groups.onenote.sectionGroups.sections.pages.parentSectioncopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.sectionGroups.sections.pages.parentSectioncopyToNotebook)|Not Found|
|[az groups group-onenote-section-group-section-page-parent-section copy-to-section-group](#groups.onenote.sectionGroups.sections.pages.parentSectioncopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.sectionGroups.sections.pages.parentSectioncopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.sectionGroups.sections.parentNotebook">Commands in `az groups group-onenote-section-group-section-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-group-section-parent-notebook copy-notebook](#groups.onenote.sectionGroups.sections.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.sectionGroups.sections.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.sectionGroups.sections.parentNotebook.sections">Commands in `az groups group-onenote-section-group-section-parent-notebook-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-group-section-parent-notebook-section copy-to-notebook](#groups.onenote.sectionGroups.sections.parentNotebook.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.sectionGroups.sections.parentNotebook.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-section-group-section-parent-notebook-section copy-to-section-group](#groups.onenote.sectionGroups.sections.parentNotebook.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.sectionGroups.sections.parentNotebook.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.sections.pages">Commands in `az groups group-onenote-section-page` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-page copy-to-section](#groups.onenote.sections.pagescopyToSection)|copyToSection|[Parameters](#Parametersgroups.onenote.sections.pagescopyToSection)|Not Found|
|[az groups group-onenote-section-page onenote-patch-content](#groups.onenote.sections.pagesonenotePatchContent)|onenotePatchContent|[Parameters](#Parametersgroups.onenote.sections.pagesonenotePatchContent)|Not Found|
|[az groups group-onenote-section-page preview](#groups.onenote.sections.pagespreview)|preview|[Parameters](#Parametersgroups.onenote.sections.pagespreview)|Not Found|

### <a name="CommandsIngroups.onenote.sections.pages.parentNotebook">Commands in `az groups group-onenote-section-page-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-page-parent-notebook copy-notebook](#groups.onenote.sections.pages.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.sections.pages.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.sections.pages.parentNotebook.sections">Commands in `az groups group-onenote-section-page-parent-notebook-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-page-parent-notebook-section copy-to-notebook](#groups.onenote.sections.pages.parentNotebook.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.sections.pages.parentNotebook.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-section-page-parent-notebook-section copy-to-section-group](#groups.onenote.sections.pages.parentNotebook.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.sections.pages.parentNotebook.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.sections.pages.parentNotebook.sectionGroups.parentNotebook">Commands in `az groups group-onenote-section-page-parent-notebook-section-group-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-page-parent-notebook-section-group-parent-notebook copy-notebook](#groups.onenote.sections.pages.parentNotebook.sectionGroups.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.sections.pages.parentNotebook.sectionGroups.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.sections.pages.parentNotebook.sectionGroups.sections">Commands in `az groups group-onenote-section-page-parent-notebook-section-group-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-page-parent-notebook-section-group-section copy-to-notebook](#groups.onenote.sections.pages.parentNotebook.sectionGroups.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.sections.pages.parentNotebook.sectionGroups.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-section-page-parent-notebook-section-group-section copy-to-section-group](#groups.onenote.sections.pages.parentNotebook.sectionGroups.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.sections.pages.parentNotebook.sectionGroups.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.sections.pages.parentSection">Commands in `az groups group-onenote-section-page-parent-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-page-parent-section copy-to-notebook](#groups.onenote.sections.pages.parentSectioncopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.sections.pages.parentSectioncopyToNotebook)|Not Found|
|[az groups group-onenote-section-page-parent-section copy-to-section-group](#groups.onenote.sections.pages.parentSectioncopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.sections.pages.parentSectioncopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.sections.parentNotebook">Commands in `az groups group-onenote-section-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-parent-notebook copy-notebook](#groups.onenote.sections.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.sections.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.sections.parentNotebook.sections">Commands in `az groups group-onenote-section-parent-notebook-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-parent-notebook-section copy-to-notebook](#groups.onenote.sections.parentNotebook.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.sections.parentNotebook.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-section-parent-notebook-section copy-to-section-group](#groups.onenote.sections.parentNotebook.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.sections.parentNotebook.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.sections.parentNotebook.sectionGroups.parentNotebook">Commands in `az groups group-onenote-section-parent-notebook-section-group-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-parent-notebook-section-group-parent-notebook copy-notebook](#groups.onenote.sections.parentNotebook.sectionGroups.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.sections.parentNotebook.sectionGroups.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.sections.parentNotebook.sectionGroups.sections">Commands in `az groups group-onenote-section-parent-notebook-section-group-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-parent-notebook-section-group-section copy-to-notebook](#groups.onenote.sections.parentNotebook.sectionGroups.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.sections.parentNotebook.sectionGroups.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-section-parent-notebook-section-group-section copy-to-section-group](#groups.onenote.sections.parentNotebook.sectionGroups.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.sections.parentNotebook.sectionGroups.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.sections.parentSectionGroup.parentNotebook">Commands in `az groups group-onenote-section-parent-section-group-parent-notebook` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-parent-section-group-parent-notebook copy-notebook](#groups.onenote.sections.parentSectionGroup.parentNotebookcopyNotebook)|copyNotebook|[Parameters](#Parametersgroups.onenote.sections.parentSectionGroup.parentNotebookcopyNotebook)|Not Found|

### <a name="CommandsIngroups.onenote.sections.parentSectionGroup.parentNotebook.sections">Commands in `az groups group-onenote-section-parent-section-group-parent-notebook-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-parent-section-group-parent-notebook-section copy-to-notebook](#groups.onenote.sections.parentSectionGroup.parentNotebook.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.sections.parentSectionGroup.parentNotebook.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-section-parent-section-group-parent-notebook-section copy-to-section-group](#groups.onenote.sections.parentSectionGroup.parentNotebook.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.sections.parentSectionGroup.parentNotebook.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.onenote.sections.parentSectionGroup.sections">Commands in `az groups group-onenote-section-parent-section-group-section` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-onenote-section-parent-section-group-section copy-to-notebook](#groups.onenote.sections.parentSectionGroup.sectionscopyToNotebook)|copyToNotebook|[Parameters](#Parametersgroups.onenote.sections.parentSectionGroup.sectionscopyToNotebook)|Not Found|
|[az groups group-onenote-section-parent-section-group-section copy-to-section-group](#groups.onenote.sections.parentSectionGroup.sectionscopyToSectionGroup)|copyToSectionGroup|[Parameters](#Parametersgroups.onenote.sections.parentSectionGroup.sectionscopyToSectionGroup)|Not Found|

### <a name="CommandsIngroups.threads">Commands in `az groups group-thread` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-thread create-post](#groups.threadsCreatePosts)|CreatePosts|[Parameters](#Parametersgroups.threadsCreatePosts)|Not Found|
|[az groups group-thread delete-post](#groups.threadsDeletePosts)|DeletePosts|[Parameters](#Parametersgroups.threadsDeletePosts)|Not Found|
|[az groups group-thread list-post](#groups.threadsListPosts)|ListPosts|[Parameters](#Parametersgroups.threadsListPosts)|Not Found|
|[az groups group-thread reply](#groups.threadsreply)|reply|[Parameters](#Parametersgroups.threadsreply)|Not Found|
|[az groups group-thread show-post](#groups.threadsGetPosts)|GetPosts|[Parameters](#Parametersgroups.threadsGetPosts)|Not Found|
|[az groups group-thread update-post](#groups.threadsUpdatePosts)|UpdatePosts|[Parameters](#Parametersgroups.threadsUpdatePosts)|Not Found|

### <a name="CommandsIngroups.threads.posts">Commands in `az groups group-thread-post` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-thread-post create-attachment](#groups.threads.postsCreateAttachments)|CreateAttachments|[Parameters](#Parametersgroups.threads.postsCreateAttachments)|Not Found|
|[az groups group-thread-post create-extension](#groups.threads.postsCreateExtensions)|CreateExtensions|[Parameters](#Parametersgroups.threads.postsCreateExtensions)|Not Found|
|[az groups group-thread-post create-multi-value-extended-property](#groups.threads.postsCreateMultiValueExtendedProperties)|CreateMultiValueExtendedProperties|[Parameters](#Parametersgroups.threads.postsCreateMultiValueExtendedProperties)|Not Found|
|[az groups group-thread-post create-single-value-extended-property](#groups.threads.postsCreateSingleValueExtendedProperties)|CreateSingleValueExtendedProperties|[Parameters](#Parametersgroups.threads.postsCreateSingleValueExtendedProperties)|Not Found|
|[az groups group-thread-post delete-attachment](#groups.threads.postsDeleteAttachments)|DeleteAttachments|[Parameters](#Parametersgroups.threads.postsDeleteAttachments)|Not Found|
|[az groups group-thread-post delete-extension](#groups.threads.postsDeleteExtensions)|DeleteExtensions|[Parameters](#Parametersgroups.threads.postsDeleteExtensions)|Not Found|
|[az groups group-thread-post delete-in-reply-to](#groups.threads.postsDeleteInReplyTo)|DeleteInReplyTo|[Parameters](#Parametersgroups.threads.postsDeleteInReplyTo)|Not Found|
|[az groups group-thread-post delete-multi-value-extended-property](#groups.threads.postsDeleteMultiValueExtendedProperties)|DeleteMultiValueExtendedProperties|[Parameters](#Parametersgroups.threads.postsDeleteMultiValueExtendedProperties)|Not Found|
|[az groups group-thread-post delete-single-value-extended-property](#groups.threads.postsDeleteSingleValueExtendedProperties)|DeleteSingleValueExtendedProperties|[Parameters](#Parametersgroups.threads.postsDeleteSingleValueExtendedProperties)|Not Found|
|[az groups group-thread-post forward](#groups.threads.postsforward)|forward|[Parameters](#Parametersgroups.threads.postsforward)|Not Found|
|[az groups group-thread-post list-attachment](#groups.threads.postsListAttachments)|ListAttachments|[Parameters](#Parametersgroups.threads.postsListAttachments)|Not Found|
|[az groups group-thread-post list-extension](#groups.threads.postsListExtensions)|ListExtensions|[Parameters](#Parametersgroups.threads.postsListExtensions)|Not Found|
|[az groups group-thread-post list-multi-value-extended-property](#groups.threads.postsListMultiValueExtendedProperties)|ListMultiValueExtendedProperties|[Parameters](#Parametersgroups.threads.postsListMultiValueExtendedProperties)|Not Found|
|[az groups group-thread-post list-single-value-extended-property](#groups.threads.postsListSingleValueExtendedProperties)|ListSingleValueExtendedProperties|[Parameters](#Parametersgroups.threads.postsListSingleValueExtendedProperties)|Not Found|
|[az groups group-thread-post reply](#groups.threads.postsreply)|reply|[Parameters](#Parametersgroups.threads.postsreply)|Not Found|
|[az groups group-thread-post show-attachment](#groups.threads.postsGetAttachments)|GetAttachments|[Parameters](#Parametersgroups.threads.postsGetAttachments)|Not Found|
|[az groups group-thread-post show-extension](#groups.threads.postsGetExtensions)|GetExtensions|[Parameters](#Parametersgroups.threads.postsGetExtensions)|Not Found|
|[az groups group-thread-post show-in-reply-to](#groups.threads.postsGetInReplyTo)|GetInReplyTo|[Parameters](#Parametersgroups.threads.postsGetInReplyTo)|Not Found|
|[az groups group-thread-post show-multi-value-extended-property](#groups.threads.postsGetMultiValueExtendedProperties)|GetMultiValueExtendedProperties|[Parameters](#Parametersgroups.threads.postsGetMultiValueExtendedProperties)|Not Found|
|[az groups group-thread-post show-single-value-extended-property](#groups.threads.postsGetSingleValueExtendedProperties)|GetSingleValueExtendedProperties|[Parameters](#Parametersgroups.threads.postsGetSingleValueExtendedProperties)|Not Found|
|[az groups group-thread-post update-attachment](#groups.threads.postsUpdateAttachments)|UpdateAttachments|[Parameters](#Parametersgroups.threads.postsUpdateAttachments)|Not Found|
|[az groups group-thread-post update-extension](#groups.threads.postsUpdateExtensions)|UpdateExtensions|[Parameters](#Parametersgroups.threads.postsUpdateExtensions)|Not Found|
|[az groups group-thread-post update-in-reply-to](#groups.threads.postsUpdateInReplyTo)|UpdateInReplyTo|[Parameters](#Parametersgroups.threads.postsUpdateInReplyTo)|Not Found|
|[az groups group-thread-post update-multi-value-extended-property](#groups.threads.postsUpdateMultiValueExtendedProperties)|UpdateMultiValueExtendedProperties|[Parameters](#Parametersgroups.threads.postsUpdateMultiValueExtendedProperties)|Not Found|
|[az groups group-thread-post update-single-value-extended-property](#groups.threads.postsUpdateSingleValueExtendedProperties)|UpdateSingleValueExtendedProperties|[Parameters](#Parametersgroups.threads.postsUpdateSingleValueExtendedProperties)|Not Found|

### <a name="CommandsIngroups.threads.posts.attachments">Commands in `az groups group-thread-post-attachment` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-thread-post-attachment create-upload-session](#groups.threads.posts.attachmentscreateUploadSession)|createUploadSession|[Parameters](#Parametersgroups.threads.posts.attachmentscreateUploadSession)|Not Found|

### <a name="CommandsIngroups.threads.posts.inReplyTo">Commands in `az groups group-thread-post-in-reply-to` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az groups group-thread-post-in-reply-to forward](#groups.threads.posts.inReplyToforward)|forward|[Parameters](#Parametersgroups.threads.posts.inReplyToforward)|Not Found|
|[az groups group-thread-post-in-reply-to reply](#groups.threads.posts.inReplyToreply)|reply|[Parameters](#Parametersgroups.threads.posts.inReplyToreply)|Not Found|


## COMMAND DETAILS
### group `az groups group`
#### <a name="groupsaddFavorite">Command `az groups group add-favorite`</a>


##### <a name="ParametersgroupsaddFavorite">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|

#### <a name="groupsassignLicense">Command `az groups group assign-license`</a>


##### <a name="ParametersgroupsassignLicense">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--add-licenses**|array||add_licenses|addLicenses|
|**--remove-licenses**|array||remove_licenses|removeLicenses|

#### <a name="groupscheckGrantedPermissionsForApp">Command `az groups group check-granted-permission-for-app`</a>


##### <a name="ParametersgroupscheckGrantedPermissionsForApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|

#### <a name="groupscheckMemberGroups">Command `az groups group check-member-group`</a>


##### <a name="ParametersgroupscheckMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--group-ids**|array||group_ids|groupIds|

#### <a name="groupscheckMemberObjects">Command `az groups group check-member-object`</a>


##### <a name="ParametersgroupscheckMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--ids**|array||ids|ids|

#### <a name="groupsCreateConversations">Command `az groups group create-conversation`</a>


##### <a name="ParametersgroupsCreateConversations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--has-attachments**|boolean|Indicates whether any of the posts within this Conversation has at least one attachment.|has_attachments|hasAttachments|
|**--last-delivered-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_delivered_date_time|lastDeliveredDateTime|
|**--preview**|string|A short summary from the body of the latest post in this converstaion.|preview|preview|
|**--topic**|string|The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated.|topic|topic|
|**--unique-senders**|array|All the users that sent a message to this Conversation.|unique_senders|uniqueSenders|
|**--threads**|array|A collection of all the conversation threads in the conversation. A navigation property. Read-only. Nullable.|threads|threads|

#### <a name="groupsCreateExtensions">Command `az groups group create-extension`</a>


##### <a name="ParametersgroupsCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|

#### <a name="groupsCreatePermissionGrants">Command `az groups group create-permission-grant`</a>


##### <a name="ParametersgroupsCreatePermissionGrants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--client-app-id**|string|ID of the service principal of the Azure AD app that has been granted access. Read-only.|client_app_id|clientAppId|
|**--client-id**|string|ID of the Azure AD app that has been granted access. Read-only.|client_id|clientId|
|**--permission**|string|The name of the resource-specific permission. Read-only.|permission|permission|
|**--permission-type**|string|The type of permission. Possible values are: Application, Delegated. Read-only.|permission_type|permissionType|
|**--resource-app-id**|string|ID of the Azure AD app that is hosting the resource. Read-only.|resource_app_id|resourceAppId|

#### <a name="groupsCreatePhotos">Command `az groups group create-photo`</a>


##### <a name="ParametersgroupsCreatePhotos">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--height**|integer|The height of the photo. Read-only.|height|height|
|**--width**|integer|The width of the photo. Read-only.|width|width|

#### <a name="groupsCreateRefAcceptedSenders">Command `az groups group create-ref-accepted-sender`</a>


##### <a name="ParametersgroupsCreateRefAcceptedSenders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="groupsCreateRefMembers">Command `az groups group create-ref-member`</a>


##### <a name="ParametersgroupsCreateRefMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="groupsCreateRefMemberOf">Command `az groups group create-ref-member-of`</a>


##### <a name="ParametersgroupsCreateRefMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="groupsCreateRefMembersWithLicenseErrors">Command `az groups group create-ref-member-with-license-error`</a>


##### <a name="ParametersgroupsCreateRefMembersWithLicenseErrors">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="groupsCreateRefOwners">Command `az groups group create-ref-owner`</a>


##### <a name="ParametersgroupsCreateRefOwners">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="groupsCreateRefRejectedSenders">Command `az groups group create-ref-rejected-sender`</a>


##### <a name="ParametersgroupsCreateRefRejectedSenders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="groupsCreateRefTransitiveMembers">Command `az groups group create-ref-transitive-member`</a>


##### <a name="ParametersgroupsCreateRefTransitiveMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="groupsCreateRefTransitiveMemberOf">Command `az groups group create-ref-transitive-member-of`</a>


##### <a name="ParametersgroupsCreateRefTransitiveMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="groupsCreateThreads">Command `az groups group create-thread`</a>


##### <a name="ParametersgroupsCreateThreads">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--cc-recipients**|array|The Cc: recipients for the thread.|cc_recipients|ccRecipients|
|**--has-attachments**|boolean|Indicates whether any of the posts within this thread has at least one attachment.|has_attachments|hasAttachments|
|**--is-locked**|boolean|Indicates if the thread is locked.|is_locked|isLocked|
|**--last-delivered-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_delivered_date_time|lastDeliveredDateTime|
|**--preview**|string|A short summary from the body of the latest post in this conversation.|preview|preview|
|**--topic**|string|The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated.|topic|topic|
|**--to-recipients**|array|The To: recipients for the thread.|to_recipients|toRecipients|
|**--unique-senders**|array|All the users that sent a message to this thread.|unique_senders|uniqueSenders|
|**--posts**|array|Read-only. Nullable.|posts|posts|

#### <a name="groupsDeleteConversations">Command `az groups group delete-conversation`</a>


##### <a name="ParametersgroupsDeleteConversations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupsDeleteExtensions">Command `az groups group delete-extension`</a>


##### <a name="ParametersgroupsDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupsDeletePermissionGrants">Command `az groups group delete-permission-grant`</a>


##### <a name="ParametersgroupsDeletePermissionGrants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--resource-specific-permission-grant-id**|string|key: id of resourceSpecificPermissionGrant|resource_specific_permission_grant_id|resourceSpecificPermissionGrant-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupsDeletePhotos">Command `az groups group delete-photo`</a>


##### <a name="ParametersgroupsDeletePhotos">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupsDeletePhoto">Command `az groups group delete-photo`</a>


##### <a name="ParametersgroupsDeletePhoto">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupsDeleteRefCreatedOnBehalfOf">Command `az groups group delete-ref-created-on-behalf-of`</a>


##### <a name="ParametersgroupsDeleteRefCreatedOnBehalfOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupsDeleteThreads">Command `az groups group delete-thread`</a>


##### <a name="ParametersgroupsDeleteThreads">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupsdelta">Command `az groups group delta`</a>


##### <a name="Parametersgroupsdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|

#### <a name="groupsgetAvailableExtensionProperties">Command `az groups group get-available-extension-property`</a>


##### <a name="ParametersgroupsgetAvailableExtensionProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

#### <a name="groupsgetByIds">Command `az groups group get-by-id`</a>


##### <a name="ParametersgroupsgetByIds">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

#### <a name="groupsgetMemberGroups">Command `az groups group get-member-group`</a>


##### <a name="ParametersgroupsgetMemberGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="groupsgetMemberObjects">Command `az groups group get-member-object`</a>


##### <a name="ParametersgroupsgetMemberObjects">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

#### <a name="groupsListAcceptedSenders">Command `az groups group list-accepted-sender`</a>


##### <a name="ParametersgroupsListAcceptedSenders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsListConversations">Command `az groups group list-conversation`</a>


##### <a name="ParametersgroupsListConversations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsListExtensions">Command `az groups group list-extension`</a>


##### <a name="ParametersgroupsListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsListMembers">Command `az groups group list-member`</a>


##### <a name="ParametersgroupsListMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsListMemberOf">Command `az groups group list-member-of`</a>


##### <a name="ParametersgroupsListMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsListMembersWithLicenseErrors">Command `az groups group list-member-with-license-error`</a>


##### <a name="ParametersgroupsListMembersWithLicenseErrors">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsListOwners">Command `az groups group list-owner`</a>


##### <a name="ParametersgroupsListOwners">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsListPermissionGrants">Command `az groups group list-permission-grant`</a>


##### <a name="ParametersgroupsListPermissionGrants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsListPhotos">Command `az groups group list-photo`</a>


##### <a name="ParametersgroupsListPhotos">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsListRefAcceptedSenders">Command `az groups group list-ref-accepted-sender`</a>


##### <a name="ParametersgroupsListRefAcceptedSenders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="groupsListRefMembers">Command `az groups group list-ref-member`</a>


##### <a name="ParametersgroupsListRefMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="groupsListRefMemberOf">Command `az groups group list-ref-member-of`</a>


##### <a name="ParametersgroupsListRefMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="groupsListRefMembersWithLicenseErrors">Command `az groups group list-ref-member-with-license-error`</a>


##### <a name="ParametersgroupsListRefMembersWithLicenseErrors">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="groupsListRefOwners">Command `az groups group list-ref-owner`</a>


##### <a name="ParametersgroupsListRefOwners">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="groupsListRefRejectedSenders">Command `az groups group list-ref-rejected-sender`</a>


##### <a name="ParametersgroupsListRefRejectedSenders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="groupsListRefTransitiveMembers">Command `az groups group list-ref-transitive-member`</a>


##### <a name="ParametersgroupsListRefTransitiveMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="groupsListRefTransitiveMemberOf">Command `az groups group list-ref-transitive-member-of`</a>


##### <a name="ParametersgroupsListRefTransitiveMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="groupsListRejectedSenders">Command `az groups group list-rejected-sender`</a>


##### <a name="ParametersgroupsListRejectedSenders">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsListThreads">Command `az groups group list-thread`</a>


##### <a name="ParametersgroupsListThreads">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsListTransitiveMembers">Command `az groups group list-transitive-member`</a>


##### <a name="ParametersgroupsListTransitiveMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsListTransitiveMemberOf">Command `az groups group list-transitive-member-of`</a>


##### <a name="ParametersgroupsListTransitiveMemberOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsremoveFavorite">Command `az groups group remove-favorite`</a>


##### <a name="ParametersgroupsremoveFavorite">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|

#### <a name="groupsrenew">Command `az groups group renew`</a>


##### <a name="Parametersgroupsrenew">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|

#### <a name="groupsresetUnseenCount">Command `az groups group reset-unseen-count`</a>


##### <a name="ParametersgroupsresetUnseenCount">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|

#### <a name="groupsrestore">Command `az groups group restore`</a>


##### <a name="Parametersgroupsrestore">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|

#### <a name="groupsSetPhotosContent">Command `az groups group set-photo-content`</a>


##### <a name="ParametersgroupsSetPhotosContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|
|**--data**|binary|New media content.|data|data|

#### <a name="groupsSetPhotoContent">Command `az groups group set-photo-content`</a>


##### <a name="ParametersgroupsSetPhotoContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--data**|binary|New media content.|data|data|

#### <a name="groupsSetRefCreatedOnBehalfOf">Command `az groups group set-ref-created-on-behalf-of`</a>


##### <a name="ParametersgroupsSetRefCreatedOnBehalfOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="groupsGetConversations">Command `az groups group show-conversation`</a>


##### <a name="ParametersgroupsGetConversations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsGetCreatedOnBehalfOf">Command `az groups group show-created-on-behalf-of`</a>


##### <a name="ParametersgroupsGetCreatedOnBehalfOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsGetExtensions">Command `az groups group show-extension`</a>


##### <a name="ParametersgroupsGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsGetPermissionGrants">Command `az groups group show-permission-grant`</a>


##### <a name="ParametersgroupsGetPermissionGrants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--resource-specific-permission-grant-id**|string|key: id of resourceSpecificPermissionGrant|resource_specific_permission_grant_id|resourceSpecificPermissionGrant-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsGetPhotos">Command `az groups group show-photo`</a>


##### <a name="ParametersgroupsGetPhotos">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsGetPhoto">Command `az groups group show-photo`</a>


##### <a name="ParametersgroupsGetPhoto">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsGetPhotosContent">Command `az groups group show-photo-content`</a>


##### <a name="ParametersgroupsGetPhotosContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|

#### <a name="groupsGetPhotoContent">Command `az groups group show-photo-content`</a>


##### <a name="ParametersgroupsGetPhotoContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|

#### <a name="groupsGetRefCreatedOnBehalfOf">Command `az groups group show-ref-created-on-behalf-of`</a>


##### <a name="ParametersgroupsGetRefCreatedOnBehalfOf">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|

#### <a name="groupsGetThreads">Command `az groups group show-thread`</a>


##### <a name="ParametersgroupsGetThreads">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupssubscribeByMail">Command `az groups group subscribe-by-mail`</a>


##### <a name="ParametersgroupssubscribeByMail">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|

#### <a name="groupsunsubscribeByMail">Command `az groups group unsubscribe-by-mail`</a>


##### <a name="ParametersgroupsunsubscribeByMail">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|

#### <a name="groupsUpdateConversations">Command `az groups group update-conversation`</a>


##### <a name="ParametersgroupsUpdateConversations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--id**|string|Read-only.|id|id|
|**--has-attachments**|boolean|Indicates whether any of the posts within this Conversation has at least one attachment.|has_attachments|hasAttachments|
|**--last-delivered-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_delivered_date_time|lastDeliveredDateTime|
|**--preview**|string|A short summary from the body of the latest post in this converstaion.|preview|preview|
|**--topic**|string|The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated.|topic|topic|
|**--unique-senders**|array|All the users that sent a message to this Conversation.|unique_senders|uniqueSenders|
|**--threads**|array|A collection of all the conversation threads in the conversation. A navigation property. Read-only. Nullable.|threads|threads|

#### <a name="groupsUpdateExtensions">Command `az groups group update-extension`</a>


##### <a name="ParametersgroupsUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="groupsUpdatePermissionGrants">Command `az groups group update-permission-grant`</a>


##### <a name="ParametersgroupsUpdatePermissionGrants">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--resource-specific-permission-grant-id**|string|key: id of resourceSpecificPermissionGrant|resource_specific_permission_grant_id|resourceSpecificPermissionGrant-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--client-app-id**|string|ID of the service principal of the Azure AD app that has been granted access. Read-only.|client_app_id|clientAppId|
|**--client-id**|string|ID of the Azure AD app that has been granted access. Read-only.|client_id|clientId|
|**--permission**|string|The name of the resource-specific permission. Read-only.|permission|permission|
|**--permission-type**|string|The type of permission. Possible values are: Application, Delegated. Read-only.|permission_type|permissionType|
|**--resource-app-id**|string|ID of the Azure AD app that is hosting the resource. Read-only.|resource_app_id|resourceAppId|

#### <a name="groupsUpdatePhotos">Command `az groups group update-photo`</a>


##### <a name="ParametersgroupsUpdatePhotos">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--profile-photo-id**|string|key: id of profilePhoto|profile_photo_id|profilePhoto-id|
|**--id**|string|Read-only.|id|id|
|**--height**|integer|The height of the photo. Read-only.|height|height|
|**--width**|integer|The width of the photo. Read-only.|width|width|

#### <a name="groupsUpdatePhoto">Command `az groups group update-photo`</a>


##### <a name="ParametersgroupsUpdatePhoto">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--height**|integer|The height of the photo. Read-only.|height|height|
|**--width**|integer|The width of the photo. Read-only.|width|width|

#### <a name="groupsUpdateThreads">Command `az groups group update-thread`</a>


##### <a name="ParametersgroupsUpdateThreads">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--id**|string|Read-only.|id|id|
|**--cc-recipients**|array|The Cc: recipients for the thread.|cc_recipients|ccRecipients|
|**--has-attachments**|boolean|Indicates whether any of the posts within this thread has at least one attachment.|has_attachments|hasAttachments|
|**--is-locked**|boolean|Indicates if the thread is locked.|is_locked|isLocked|
|**--last-delivered-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_delivered_date_time|lastDeliveredDateTime|
|**--preview**|string|A short summary from the body of the latest post in this conversation.|preview|preview|
|**--topic**|string|The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated.|topic|topic|
|**--to-recipients**|array|The To: recipients for the thread.|to_recipients|toRecipients|
|**--unique-senders**|array|All the users that sent a message to this thread.|unique_senders|uniqueSenders|
|**--posts**|array|Read-only. Nullable.|posts|posts|

#### <a name="groupsvalidateProperties">Command `az groups group validate-property`</a>


##### <a name="ParametersgroupsvalidateProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--display-name**|string||display_name|displayName|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-behalf-of-user-id**|uuid||on_behalf_of_user_id|onBehalfOfUserId|

### group `az groups group-calendar`
#### <a name="groups.calendarallowedCalendarSharingRoles">Command `az groups group-calendar allowed-calendar-sharing-role`</a>


##### <a name="Parametersgroups.calendarallowedCalendarSharingRoles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--user**|string|Usage: User={User}|user|User|

#### <a name="groups.calendargetSchedule">Command `az groups group-calendar get-schedule`</a>


##### <a name="Parametersgroups.calendargetSchedule">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--schedules**|array||schedules|Schedules|
|**--end-time**|object|dateTimeTimeZone|end_time|EndTime|
|**--start-time**|object|dateTimeTimeZone|start_time|StartTime|
|**--availability-view-interval**|integer||availability_view_interval|AvailabilityViewInterval|

### group `az groups group-calendar-calendar-view`
#### <a name="groups.calendar.calendarViewaccept">Command `az groups group-calendar-calendar-view accept`</a>


##### <a name="Parametersgroups.calendar.calendarViewaccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

#### <a name="groups.calendar.calendarViewcancel">Command `az groups group-calendar-calendar-view cancel`</a>


##### <a name="Parametersgroups.calendar.calendarViewcancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendar.calendarViewdecline">Command `az groups group-calendar-calendar-view decline`</a>


##### <a name="Parametersgroups.calendar.calendarViewdecline">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

#### <a name="groups.calendar.calendarViewdelta">Command `az groups group-calendar-calendar-view delta`</a>


##### <a name="Parametersgroups.calendar.calendarViewdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|

#### <a name="groups.calendar.calendarViewdismissReminder">Command `az groups group-calendar-calendar-view dismiss-reminder`</a>


##### <a name="Parametersgroups.calendar.calendarViewdismissReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|

#### <a name="groups.calendar.calendarViewforward">Command `az groups group-calendar-calendar-view forward`</a>


##### <a name="Parametersgroups.calendar.calendarViewforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendar.calendarViewsnoozeReminder">Command `az groups group-calendar-calendar-view snooze-reminder`</a>


##### <a name="Parametersgroups.calendar.calendarViewsnoozeReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

#### <a name="groups.calendar.calendarViewtentativelyAccept">Command `az groups group-calendar-calendar-view tentatively-accept`</a>


##### <a name="Parametersgroups.calendar.calendarViewtentativelyAccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

### group `az groups group-calendar-calendar-view-attachment`
#### <a name="groups.calendar.calendarView.attachmentscreateUploadSession">Command `az groups group-calendar-calendar-view-attachment create-upload-session`</a>


##### <a name="Parametersgroups.calendar.calendarView.attachmentscreateUploadSession">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### group `az groups group-calendar-calendar-view-calendar`
#### <a name="groups.calendar.calendarView.calendarallowedCalendarSharingRoles">Command `az groups group-calendar-calendar-view-calendar allowed-calendar-sharing-role`</a>


##### <a name="Parametersgroups.calendar.calendarView.calendarallowedCalendarSharingRoles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--user**|string|Usage: User={User}|user|User|

#### <a name="groups.calendar.calendarView.calendargetSchedule">Command `az groups group-calendar-calendar-view-calendar get-schedule`</a>


##### <a name="Parametersgroups.calendar.calendarView.calendargetSchedule">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--schedules**|array||schedules|Schedules|
|**--end-time**|object|dateTimeTimeZone|end_time|EndTime|
|**--start-time**|object|dateTimeTimeZone|start_time|StartTime|
|**--availability-view-interval**|integer||availability_view_interval|AvailabilityViewInterval|

### group `az groups group-calendar-calendar-view-instance`
#### <a name="groups.calendar.calendarView.instancesaccept">Command `az groups group-calendar-calendar-view-instance accept`</a>


##### <a name="Parametersgroups.calendar.calendarView.instancesaccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

#### <a name="groups.calendar.calendarView.instancescancel">Command `az groups group-calendar-calendar-view-instance cancel`</a>


##### <a name="Parametersgroups.calendar.calendarView.instancescancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendar.calendarView.instancesdecline">Command `az groups group-calendar-calendar-view-instance decline`</a>


##### <a name="Parametersgroups.calendar.calendarView.instancesdecline">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

#### <a name="groups.calendar.calendarView.instancesdelta">Command `az groups group-calendar-calendar-view-instance delta`</a>


##### <a name="Parametersgroups.calendar.calendarView.instancesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|

#### <a name="groups.calendar.calendarView.instancesdismissReminder">Command `az groups group-calendar-calendar-view-instance dismiss-reminder`</a>


##### <a name="Parametersgroups.calendar.calendarView.instancesdismissReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

#### <a name="groups.calendar.calendarView.instancesforward">Command `az groups group-calendar-calendar-view-instance forward`</a>


##### <a name="Parametersgroups.calendar.calendarView.instancesforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendar.calendarView.instancessnoozeReminder">Command `az groups group-calendar-calendar-view-instance snooze-reminder`</a>


##### <a name="Parametersgroups.calendar.calendarView.instancessnoozeReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

#### <a name="groups.calendar.calendarView.instancestentativelyAccept">Command `az groups group-calendar-calendar-view-instance tentatively-accept`</a>


##### <a name="Parametersgroups.calendar.calendarView.instancestentativelyAccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

### group `az groups group-calendar-event`
#### <a name="groups.calendar.eventsaccept">Command `az groups group-calendar-event accept`</a>


##### <a name="Parametersgroups.calendar.eventsaccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

#### <a name="groups.calendar.eventscancel">Command `az groups group-calendar-event cancel`</a>


##### <a name="Parametersgroups.calendar.eventscancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendar.eventsdecline">Command `az groups group-calendar-event decline`</a>


##### <a name="Parametersgroups.calendar.eventsdecline">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

#### <a name="groups.calendar.eventsdelta">Command `az groups group-calendar-event delta`</a>


##### <a name="Parametersgroups.calendar.eventsdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|

#### <a name="groups.calendar.eventsdismissReminder">Command `az groups group-calendar-event dismiss-reminder`</a>


##### <a name="Parametersgroups.calendar.eventsdismissReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|

#### <a name="groups.calendar.eventsforward">Command `az groups group-calendar-event forward`</a>


##### <a name="Parametersgroups.calendar.eventsforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendar.eventssnoozeReminder">Command `az groups group-calendar-event snooze-reminder`</a>


##### <a name="Parametersgroups.calendar.eventssnoozeReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

#### <a name="groups.calendar.eventstentativelyAccept">Command `az groups group-calendar-event tentatively-accept`</a>


##### <a name="Parametersgroups.calendar.eventstentativelyAccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

### group `az groups group-calendar-event-attachment`
#### <a name="groups.calendar.events.attachmentscreateUploadSession">Command `az groups group-calendar-event-attachment create-upload-session`</a>


##### <a name="Parametersgroups.calendar.events.attachmentscreateUploadSession">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### group `az groups group-calendar-event-calendar`
#### <a name="groups.calendar.events.calendarallowedCalendarSharingRoles">Command `az groups group-calendar-event-calendar allowed-calendar-sharing-role`</a>


##### <a name="Parametersgroups.calendar.events.calendarallowedCalendarSharingRoles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--user**|string|Usage: User={User}|user|User|

#### <a name="groups.calendar.events.calendargetSchedule">Command `az groups group-calendar-event-calendar get-schedule`</a>


##### <a name="Parametersgroups.calendar.events.calendargetSchedule">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--schedules**|array||schedules|Schedules|
|**--end-time**|object|dateTimeTimeZone|end_time|EndTime|
|**--start-time**|object|dateTimeTimeZone|start_time|StartTime|
|**--availability-view-interval**|integer||availability_view_interval|AvailabilityViewInterval|

### group `az groups group-calendar-event-instance`
#### <a name="groups.calendar.events.instancesaccept">Command `az groups group-calendar-event-instance accept`</a>


##### <a name="Parametersgroups.calendar.events.instancesaccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

#### <a name="groups.calendar.events.instancescancel">Command `az groups group-calendar-event-instance cancel`</a>


##### <a name="Parametersgroups.calendar.events.instancescancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendar.events.instancesdecline">Command `az groups group-calendar-event-instance decline`</a>


##### <a name="Parametersgroups.calendar.events.instancesdecline">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

#### <a name="groups.calendar.events.instancesdelta">Command `az groups group-calendar-event-instance delta`</a>


##### <a name="Parametersgroups.calendar.events.instancesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|

#### <a name="groups.calendar.events.instancesdismissReminder">Command `az groups group-calendar-event-instance dismiss-reminder`</a>


##### <a name="Parametersgroups.calendar.events.instancesdismissReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

#### <a name="groups.calendar.events.instancesforward">Command `az groups group-calendar-event-instance forward`</a>


##### <a name="Parametersgroups.calendar.events.instancesforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendar.events.instancessnoozeReminder">Command `az groups group-calendar-event-instance snooze-reminder`</a>


##### <a name="Parametersgroups.calendar.events.instancessnoozeReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

#### <a name="groups.calendar.events.instancestentativelyAccept">Command `az groups group-calendar-event-instance tentatively-accept`</a>


##### <a name="Parametersgroups.calendar.events.instancestentativelyAccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

### group `az groups group-calendar-view`
#### <a name="groups.calendarViewaccept">Command `az groups group-calendar-view accept`</a>


##### <a name="Parametersgroups.calendarViewaccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

#### <a name="groups.calendarViewcancel">Command `az groups group-calendar-view cancel`</a>


##### <a name="Parametersgroups.calendarViewcancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendarViewdecline">Command `az groups group-calendar-view decline`</a>


##### <a name="Parametersgroups.calendarViewdecline">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

#### <a name="groups.calendarViewdelta">Command `az groups group-calendar-view delta`</a>


##### <a name="Parametersgroups.calendarViewdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|

#### <a name="groups.calendarViewdismissReminder">Command `az groups group-calendar-view dismiss-reminder`</a>


##### <a name="Parametersgroups.calendarViewdismissReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|

#### <a name="groups.calendarViewforward">Command `az groups group-calendar-view forward`</a>


##### <a name="Parametersgroups.calendarViewforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendarViewsnoozeReminder">Command `az groups group-calendar-view snooze-reminder`</a>


##### <a name="Parametersgroups.calendarViewsnoozeReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

#### <a name="groups.calendarViewtentativelyAccept">Command `az groups group-calendar-view tentatively-accept`</a>


##### <a name="Parametersgroups.calendarViewtentativelyAccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

### group `az groups group-calendar-view-attachment`
#### <a name="groups.calendarView.attachmentscreateUploadSession">Command `az groups group-calendar-view-attachment create-upload-session`</a>


##### <a name="Parametersgroups.calendarView.attachmentscreateUploadSession">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### group `az groups group-calendar-view-calendar`
#### <a name="groups.calendarView.calendarallowedCalendarSharingRoles">Command `az groups group-calendar-view-calendar allowed-calendar-sharing-role`</a>


##### <a name="Parametersgroups.calendarView.calendarallowedCalendarSharingRoles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--user**|string|Usage: User={User}|user|User|

#### <a name="groups.calendarView.calendargetSchedule">Command `az groups group-calendar-view-calendar get-schedule`</a>


##### <a name="Parametersgroups.calendarView.calendargetSchedule">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--schedules**|array||schedules|Schedules|
|**--end-time**|object|dateTimeTimeZone|end_time|EndTime|
|**--start-time**|object|dateTimeTimeZone|start_time|StartTime|
|**--availability-view-interval**|integer||availability_view_interval|AvailabilityViewInterval|

### group `az groups group-calendar-view-calendar-calendar-view`
#### <a name="groups.calendarView.calendar.calendarViewaccept">Command `az groups group-calendar-view-calendar-calendar-view accept`</a>


##### <a name="Parametersgroups.calendarView.calendar.calendarViewaccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

#### <a name="groups.calendarView.calendar.calendarViewcancel">Command `az groups group-calendar-view-calendar-calendar-view cancel`</a>


##### <a name="Parametersgroups.calendarView.calendar.calendarViewcancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendarView.calendar.calendarViewdecline">Command `az groups group-calendar-view-calendar-calendar-view decline`</a>


##### <a name="Parametersgroups.calendarView.calendar.calendarViewdecline">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

#### <a name="groups.calendarView.calendar.calendarViewdelta">Command `az groups group-calendar-view-calendar-calendar-view delta`</a>


##### <a name="Parametersgroups.calendarView.calendar.calendarViewdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|

#### <a name="groups.calendarView.calendar.calendarViewdismissReminder">Command `az groups group-calendar-view-calendar-calendar-view dismiss-reminder`</a>


##### <a name="Parametersgroups.calendarView.calendar.calendarViewdismissReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

#### <a name="groups.calendarView.calendar.calendarViewforward">Command `az groups group-calendar-view-calendar-calendar-view forward`</a>


##### <a name="Parametersgroups.calendarView.calendar.calendarViewforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendarView.calendar.calendarViewsnoozeReminder">Command `az groups group-calendar-view-calendar-calendar-view snooze-reminder`</a>


##### <a name="Parametersgroups.calendarView.calendar.calendarViewsnoozeReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

#### <a name="groups.calendarView.calendar.calendarViewtentativelyAccept">Command `az groups group-calendar-view-calendar-calendar-view tentatively-accept`</a>


##### <a name="Parametersgroups.calendarView.calendar.calendarViewtentativelyAccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

### group `az groups group-calendar-view-calendar-event`
#### <a name="groups.calendarView.calendar.eventsaccept">Command `az groups group-calendar-view-calendar-event accept`</a>


##### <a name="Parametersgroups.calendarView.calendar.eventsaccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

#### <a name="groups.calendarView.calendar.eventscancel">Command `az groups group-calendar-view-calendar-event cancel`</a>


##### <a name="Parametersgroups.calendarView.calendar.eventscancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendarView.calendar.eventsdecline">Command `az groups group-calendar-view-calendar-event decline`</a>


##### <a name="Parametersgroups.calendarView.calendar.eventsdecline">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

#### <a name="groups.calendarView.calendar.eventsdelta">Command `az groups group-calendar-view-calendar-event delta`</a>


##### <a name="Parametersgroups.calendarView.calendar.eventsdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|

#### <a name="groups.calendarView.calendar.eventsdismissReminder">Command `az groups group-calendar-view-calendar-event dismiss-reminder`</a>


##### <a name="Parametersgroups.calendarView.calendar.eventsdismissReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

#### <a name="groups.calendarView.calendar.eventsforward">Command `az groups group-calendar-view-calendar-event forward`</a>


##### <a name="Parametersgroups.calendarView.calendar.eventsforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendarView.calendar.eventssnoozeReminder">Command `az groups group-calendar-view-calendar-event snooze-reminder`</a>


##### <a name="Parametersgroups.calendarView.calendar.eventssnoozeReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

#### <a name="groups.calendarView.calendar.eventstentativelyAccept">Command `az groups group-calendar-view-calendar-event tentatively-accept`</a>


##### <a name="Parametersgroups.calendarView.calendar.eventstentativelyAccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

### group `az groups group-calendar-view-instance`
#### <a name="groups.calendarView.instancesaccept">Command `az groups group-calendar-view-instance accept`</a>


##### <a name="Parametersgroups.calendarView.instancesaccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

#### <a name="groups.calendarView.instancescancel">Command `az groups group-calendar-view-instance cancel`</a>


##### <a name="Parametersgroups.calendarView.instancescancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendarView.instancesdecline">Command `az groups group-calendar-view-instance decline`</a>


##### <a name="Parametersgroups.calendarView.instancesdecline">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

#### <a name="groups.calendarView.instancesdelta">Command `az groups group-calendar-view-instance delta`</a>


##### <a name="Parametersgroups.calendarView.instancesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|

#### <a name="groups.calendarView.instancesdismissReminder">Command `az groups group-calendar-view-instance dismiss-reminder`</a>


##### <a name="Parametersgroups.calendarView.instancesdismissReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

#### <a name="groups.calendarView.instancesforward">Command `az groups group-calendar-view-instance forward`</a>


##### <a name="Parametersgroups.calendarView.instancesforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

#### <a name="groups.calendarView.instancessnoozeReminder">Command `az groups group-calendar-view-instance snooze-reminder`</a>


##### <a name="Parametersgroups.calendarView.instancessnoozeReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

#### <a name="groups.calendarView.instancestentativelyAccept">Command `az groups group-calendar-view-instance tentatively-accept`</a>


##### <a name="Parametersgroups.calendarView.instancestentativelyAccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

### group `az groups group-conversation`
#### <a name="groups.conversationsCreateThreads">Command `az groups group-conversation create-thread`</a>


##### <a name="Parametersgroups.conversationsCreateThreads">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--id**|string|Read-only.|id|id|
|**--cc-recipients**|array|The Cc: recipients for the thread.|cc_recipients|ccRecipients|
|**--has-attachments**|boolean|Indicates whether any of the posts within this thread has at least one attachment.|has_attachments|hasAttachments|
|**--is-locked**|boolean|Indicates if the thread is locked.|is_locked|isLocked|
|**--last-delivered-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_delivered_date_time|lastDeliveredDateTime|
|**--preview**|string|A short summary from the body of the latest post in this conversation.|preview|preview|
|**--topic**|string|The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated.|topic|topic|
|**--to-recipients**|array|The To: recipients for the thread.|to_recipients|toRecipients|
|**--unique-senders**|array|All the users that sent a message to this thread.|unique_senders|uniqueSenders|
|**--posts**|array|Read-only. Nullable.|posts|posts|

#### <a name="groups.conversationsDeleteThreads">Command `az groups group-conversation delete-thread`</a>


##### <a name="Parametersgroups.conversationsDeleteThreads">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.conversationsListThreads">Command `az groups group-conversation list-thread`</a>


##### <a name="Parametersgroups.conversationsListThreads">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.conversationsGetThreads">Command `az groups group-conversation show-thread`</a>


##### <a name="Parametersgroups.conversationsGetThreads">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.conversationsUpdateThreads">Command `az groups group-conversation update-thread`</a>


##### <a name="Parametersgroups.conversationsUpdateThreads">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--id**|string|Read-only.|id|id|
|**--cc-recipients**|array|The Cc: recipients for the thread.|cc_recipients|ccRecipients|
|**--has-attachments**|boolean|Indicates whether any of the posts within this thread has at least one attachment.|has_attachments|hasAttachments|
|**--is-locked**|boolean|Indicates if the thread is locked.|is_locked|isLocked|
|**--last-delivered-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_delivered_date_time|lastDeliveredDateTime|
|**--preview**|string|A short summary from the body of the latest post in this conversation.|preview|preview|
|**--topic**|string|The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated.|topic|topic|
|**--to-recipients**|array|The To: recipients for the thread.|to_recipients|toRecipients|
|**--unique-senders**|array|All the users that sent a message to this thread.|unique_senders|uniqueSenders|
|**--posts**|array|Read-only. Nullable.|posts|posts|

### group `az groups group-conversation-thread`
#### <a name="groups.conversations.threadsCreatePosts">Command `az groups group-conversation-thread create-post`</a>


##### <a name="Parametersgroups.conversations.threadsCreatePosts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_modified_date_time|lastModifiedDateTime|
|**--body**|object|itemBody|body|body|
|**--microsoft-graph-post-conversation-id**|string|Unique ID of the conversation. Read-only.|microsoft_graph_post_conversation_id|conversationId|
|**--microsoft-graph-post-conversation-thread-id-conversation-thread-id**|string|Unique ID of the conversation thread. Read-only.|microsoft_graph_post_conversation_thread_id_conversation_thread_id|conversationThreadId|
|**--has-attachments**|boolean|Indicates whether the post has at least one attachment. This is a default property.|has_attachments|hasAttachments|
|**--new-participants**|array|Conversation participants that were added to the thread as part of this post.|new_participants|newParticipants|
|**--received-date-time**|date-time|Specifies when the post was received. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|received_date_time|receivedDateTime|
|**--attachments**|array|The collection of fileAttachment, itemAttachment, and referenceAttachment attachments for the post. Read-only. Nullable.|attachments|attachments|
|**--extensions**|array|The collection of open extensions defined for the post. Read-only. Nullable.|extensions|extensions|
|**--in-reply-to**|object|post|in_reply_to|inReplyTo|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the post. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the post. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--microsoft-graph-email-address**|object|emailAddress|microsoft_graph_email_address|emailAddress|

#### <a name="groups.conversations.threadsDeletePosts">Command `az groups group-conversation-thread delete-post`</a>


##### <a name="Parametersgroups.conversations.threadsDeletePosts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.conversations.threadsListPosts">Command `az groups group-conversation-thread list-post`</a>


##### <a name="Parametersgroups.conversations.threadsListPosts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.conversations.threadsreply">Command `az groups group-conversation-thread reply`</a>


##### <a name="Parametersgroups.conversations.threadsreply">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post**|object|post|post|Post|

#### <a name="groups.conversations.threadsGetPosts">Command `az groups group-conversation-thread show-post`</a>


##### <a name="Parametersgroups.conversations.threadsGetPosts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.conversations.threadsUpdatePosts">Command `az groups group-conversation-thread update-post`</a>


##### <a name="Parametersgroups.conversations.threadsUpdatePosts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_modified_date_time|lastModifiedDateTime|
|**--body**|object|itemBody|body|body|
|**--microsoft-graph-post-conversation-id**|string|Unique ID of the conversation. Read-only.|microsoft_graph_post_conversation_id|conversationId|
|**--microsoft-graph-post-conversation-thread-id-conversation-thread-id**|string|Unique ID of the conversation thread. Read-only.|microsoft_graph_post_conversation_thread_id_conversation_thread_id|conversationThreadId|
|**--has-attachments**|boolean|Indicates whether the post has at least one attachment. This is a default property.|has_attachments|hasAttachments|
|**--new-participants**|array|Conversation participants that were added to the thread as part of this post.|new_participants|newParticipants|
|**--received-date-time**|date-time|Specifies when the post was received. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|received_date_time|receivedDateTime|
|**--attachments**|array|The collection of fileAttachment, itemAttachment, and referenceAttachment attachments for the post. Read-only. Nullable.|attachments|attachments|
|**--extensions**|array|The collection of open extensions defined for the post. Read-only. Nullable.|extensions|extensions|
|**--in-reply-to**|object|post|in_reply_to|inReplyTo|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the post. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the post. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--microsoft-graph-email-address**|object|emailAddress|microsoft_graph_email_address|emailAddress|

### group `az groups group-conversation-thread-post`
#### <a name="groups.conversations.threads.postsCreateAttachments">Command `az groups group-conversation-thread-post create-attachment`</a>


##### <a name="Parametersgroups.conversations.threads.postsCreateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The display name of the attachment. This does not need to be the actual file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="groups.conversations.threads.postsCreateExtensions">Command `az groups group-conversation-thread-post create-extension`</a>


##### <a name="Parametersgroups.conversations.threads.postsCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|

#### <a name="groups.conversations.threads.postsCreateMultiValueExtendedProperties">Command `az groups group-conversation-thread-post create-multi-value-extended-property`</a>


##### <a name="Parametersgroups.conversations.threads.postsCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.conversations.threads.postsCreateSingleValueExtendedProperties">Command `az groups group-conversation-thread-post create-single-value-extended-property`</a>


##### <a name="Parametersgroups.conversations.threads.postsCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="groups.conversations.threads.postsDeleteAttachments">Command `az groups group-conversation-thread-post delete-attachment`</a>


##### <a name="Parametersgroups.conversations.threads.postsDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.conversations.threads.postsDeleteExtensions">Command `az groups group-conversation-thread-post delete-extension`</a>


##### <a name="Parametersgroups.conversations.threads.postsDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.conversations.threads.postsDeleteInReplyTo">Command `az groups group-conversation-thread-post delete-in-reply-to`</a>


##### <a name="Parametersgroups.conversations.threads.postsDeleteInReplyTo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.conversations.threads.postsDeleteMultiValueExtendedProperties">Command `az groups group-conversation-thread-post delete-multi-value-extended-property`</a>


##### <a name="Parametersgroups.conversations.threads.postsDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.conversations.threads.postsDeleteSingleValueExtendedProperties">Command `az groups group-conversation-thread-post delete-single-value-extended-property`</a>


##### <a name="Parametersgroups.conversations.threads.postsDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.conversations.threads.postsforward">Command `az groups group-conversation-thread-post forward`</a>


##### <a name="Parametersgroups.conversations.threads.postsforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--comment**|string||comment|Comment|
|**--to-recipients**|array||to_recipients|ToRecipients|

#### <a name="groups.conversations.threads.postsListAttachments">Command `az groups group-conversation-thread-post list-attachment`</a>


##### <a name="Parametersgroups.conversations.threads.postsListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.conversations.threads.postsListExtensions">Command `az groups group-conversation-thread-post list-extension`</a>


##### <a name="Parametersgroups.conversations.threads.postsListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.conversations.threads.postsListMultiValueExtendedProperties">Command `az groups group-conversation-thread-post list-multi-value-extended-property`</a>


##### <a name="Parametersgroups.conversations.threads.postsListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.conversations.threads.postsListSingleValueExtendedProperties">Command `az groups group-conversation-thread-post list-single-value-extended-property`</a>


##### <a name="Parametersgroups.conversations.threads.postsListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.conversations.threads.postsreply">Command `az groups group-conversation-thread-post reply`</a>


##### <a name="Parametersgroups.conversations.threads.postsreply">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--post**|object|post|post|Post|

#### <a name="groups.conversations.threads.postsGetAttachments">Command `az groups group-conversation-thread-post show-attachment`</a>


##### <a name="Parametersgroups.conversations.threads.postsGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.conversations.threads.postsGetExtensions">Command `az groups group-conversation-thread-post show-extension`</a>


##### <a name="Parametersgroups.conversations.threads.postsGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.conversations.threads.postsGetInReplyTo">Command `az groups group-conversation-thread-post show-in-reply-to`</a>


##### <a name="Parametersgroups.conversations.threads.postsGetInReplyTo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.conversations.threads.postsGetMultiValueExtendedProperties">Command `az groups group-conversation-thread-post show-multi-value-extended-property`</a>


##### <a name="Parametersgroups.conversations.threads.postsGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.conversations.threads.postsGetSingleValueExtendedProperties">Command `az groups group-conversation-thread-post show-single-value-extended-property`</a>


##### <a name="Parametersgroups.conversations.threads.postsGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.conversations.threads.postsUpdateAttachments">Command `az groups group-conversation-thread-post update-attachment`</a>


##### <a name="Parametersgroups.conversations.threads.postsUpdateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The display name of the attachment. This does not need to be the actual file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="groups.conversations.threads.postsUpdateExtensions">Command `az groups group-conversation-thread-post update-extension`</a>


##### <a name="Parametersgroups.conversations.threads.postsUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="groups.conversations.threads.postsUpdateInReplyTo">Command `az groups group-conversation-thread-post update-in-reply-to`</a>


##### <a name="Parametersgroups.conversations.threads.postsUpdateInReplyTo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_modified_date_time|lastModifiedDateTime|
|**--body**|object|itemBody|body|body|
|**--microsoft-graph-post-conversation-id**|string|Unique ID of the conversation. Read-only.|microsoft_graph_post_conversation_id|conversationId|
|**--microsoft-graph-post-conversation-thread-id-conversation-thread-id**|string|Unique ID of the conversation thread. Read-only.|microsoft_graph_post_conversation_thread_id_conversation_thread_id|conversationThreadId|
|**--has-attachments**|boolean|Indicates whether the post has at least one attachment. This is a default property.|has_attachments|hasAttachments|
|**--new-participants**|array|Conversation participants that were added to the thread as part of this post.|new_participants|newParticipants|
|**--received-date-time**|date-time|Specifies when the post was received. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|received_date_time|receivedDateTime|
|**--attachments**|array|The collection of fileAttachment, itemAttachment, and referenceAttachment attachments for the post. Read-only. Nullable.|attachments|attachments|
|**--extensions**|array|The collection of open extensions defined for the post. Read-only. Nullable.|extensions|extensions|
|**--in-reply-to**|object|post|in_reply_to|inReplyTo|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the post. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the post. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--microsoft-graph-email-address**|object|emailAddress|microsoft_graph_email_address|emailAddress|

#### <a name="groups.conversations.threads.postsUpdateMultiValueExtendedProperties">Command `az groups group-conversation-thread-post update-multi-value-extended-property`</a>


##### <a name="Parametersgroups.conversations.threads.postsUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.conversations.threads.postsUpdateSingleValueExtendedProperties">Command `az groups group-conversation-thread-post update-single-value-extended-property`</a>


##### <a name="Parametersgroups.conversations.threads.postsUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az groups group-conversation-thread-post-attachment`
#### <a name="groups.conversations.threads.posts.attachmentscreateUploadSession">Command `az groups group-conversation-thread-post-attachment create-upload-session`</a>


##### <a name="Parametersgroups.conversations.threads.posts.attachmentscreateUploadSession">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### group `az groups group-conversation-thread-post-in-reply-to`
#### <a name="groups.conversations.threads.posts.inReplyToforward">Command `az groups group-conversation-thread-post-in-reply-to forward`</a>


##### <a name="Parametersgroups.conversations.threads.posts.inReplyToforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--comment**|string||comment|Comment|
|**--to-recipients**|array||to_recipients|ToRecipients|

#### <a name="groups.conversations.threads.posts.inReplyToreply">Command `az groups group-conversation-thread-post-in-reply-to reply`</a>


##### <a name="Parametersgroups.conversations.threads.posts.inReplyToreply">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-id**|string|key: id of conversation|conversation_id|conversation-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--post**|object|post|post|Post|

### group `az groups group-event`
#### <a name="groups.eventsaccept">Command `az groups group-event accept`</a>


##### <a name="Parametersgroups.eventsaccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

#### <a name="groups.eventscancel">Command `az groups group-event cancel`</a>


##### <a name="Parametersgroups.eventscancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|

#### <a name="groups.eventsdecline">Command `az groups group-event decline`</a>


##### <a name="Parametersgroups.eventsdecline">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

#### <a name="groups.eventsdelta">Command `az groups group-event delta`</a>


##### <a name="Parametersgroups.eventsdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|

#### <a name="groups.eventsdismissReminder">Command `az groups group-event dismiss-reminder`</a>


##### <a name="Parametersgroups.eventsdismissReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|

#### <a name="groups.eventsforward">Command `az groups group-event forward`</a>


##### <a name="Parametersgroups.eventsforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

#### <a name="groups.eventssnoozeReminder">Command `az groups group-event snooze-reminder`</a>


##### <a name="Parametersgroups.eventssnoozeReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

#### <a name="groups.eventstentativelyAccept">Command `az groups group-event tentatively-accept`</a>


##### <a name="Parametersgroups.eventstentativelyAccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

### group `az groups group-event-attachment`
#### <a name="groups.events.attachmentscreateUploadSession">Command `az groups group-event-attachment create-upload-session`</a>


##### <a name="Parametersgroups.events.attachmentscreateUploadSession">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### group `az groups group-event-calendar`
#### <a name="groups.events.calendarallowedCalendarSharingRoles">Command `az groups group-event-calendar allowed-calendar-sharing-role`</a>


##### <a name="Parametersgroups.events.calendarallowedCalendarSharingRoles">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--user**|string|Usage: User={User}|user|User|

#### <a name="groups.events.calendargetSchedule">Command `az groups group-event-calendar get-schedule`</a>


##### <a name="Parametersgroups.events.calendargetSchedule">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--schedules**|array||schedules|Schedules|
|**--end-time**|object|dateTimeTimeZone|end_time|EndTime|
|**--start-time**|object|dateTimeTimeZone|start_time|StartTime|
|**--availability-view-interval**|integer||availability_view_interval|AvailabilityViewInterval|

### group `az groups group-event-calendar-calendar-view`
#### <a name="groups.events.calendar.calendarViewaccept">Command `az groups group-event-calendar-calendar-view accept`</a>


##### <a name="Parametersgroups.events.calendar.calendarViewaccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

#### <a name="groups.events.calendar.calendarViewcancel">Command `az groups group-event-calendar-calendar-view cancel`</a>


##### <a name="Parametersgroups.events.calendar.calendarViewcancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

#### <a name="groups.events.calendar.calendarViewdecline">Command `az groups group-event-calendar-calendar-view decline`</a>


##### <a name="Parametersgroups.events.calendar.calendarViewdecline">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

#### <a name="groups.events.calendar.calendarViewdelta">Command `az groups group-event-calendar-calendar-view delta`</a>


##### <a name="Parametersgroups.events.calendar.calendarViewdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|

#### <a name="groups.events.calendar.calendarViewdismissReminder">Command `az groups group-event-calendar-calendar-view dismiss-reminder`</a>


##### <a name="Parametersgroups.events.calendar.calendarViewdismissReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

#### <a name="groups.events.calendar.calendarViewforward">Command `az groups group-event-calendar-calendar-view forward`</a>


##### <a name="Parametersgroups.events.calendar.calendarViewforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

#### <a name="groups.events.calendar.calendarViewsnoozeReminder">Command `az groups group-event-calendar-calendar-view snooze-reminder`</a>


##### <a name="Parametersgroups.events.calendar.calendarViewsnoozeReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

#### <a name="groups.events.calendar.calendarViewtentativelyAccept">Command `az groups group-event-calendar-calendar-view tentatively-accept`</a>


##### <a name="Parametersgroups.events.calendar.calendarViewtentativelyAccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

### group `az groups group-event-calendar-event`
#### <a name="groups.events.calendar.eventsaccept">Command `az groups group-event-calendar-event accept`</a>


##### <a name="Parametersgroups.events.calendar.eventsaccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

#### <a name="groups.events.calendar.eventscancel">Command `az groups group-event-calendar-event cancel`</a>


##### <a name="Parametersgroups.events.calendar.eventscancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

#### <a name="groups.events.calendar.eventsdecline">Command `az groups group-event-calendar-event decline`</a>


##### <a name="Parametersgroups.events.calendar.eventsdecline">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

#### <a name="groups.events.calendar.eventsdelta">Command `az groups group-event-calendar-event delta`</a>


##### <a name="Parametersgroups.events.calendar.eventsdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|

#### <a name="groups.events.calendar.eventsdismissReminder">Command `az groups group-event-calendar-event dismiss-reminder`</a>


##### <a name="Parametersgroups.events.calendar.eventsdismissReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

#### <a name="groups.events.calendar.eventsforward">Command `az groups group-event-calendar-event forward`</a>


##### <a name="Parametersgroups.events.calendar.eventsforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

#### <a name="groups.events.calendar.eventssnoozeReminder">Command `az groups group-event-calendar-event snooze-reminder`</a>


##### <a name="Parametersgroups.events.calendar.eventssnoozeReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

#### <a name="groups.events.calendar.eventstentativelyAccept">Command `az groups group-event-calendar-event tentatively-accept`</a>


##### <a name="Parametersgroups.events.calendar.eventstentativelyAccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

### group `az groups group-event-instance`
#### <a name="groups.events.instancesaccept">Command `az groups group-event-instance accept`</a>


##### <a name="Parametersgroups.events.instancesaccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

#### <a name="groups.events.instancescancel">Command `az groups group-event-instance cancel`</a>


##### <a name="Parametersgroups.events.instancescancel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|

#### <a name="groups.events.instancesdecline">Command `az groups group-event-instance decline`</a>


##### <a name="Parametersgroups.events.instancesdecline">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

#### <a name="groups.events.instancesdelta">Command `az groups group-event-instance delta`</a>


##### <a name="Parametersgroups.events.instancesdelta">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|

#### <a name="groups.events.instancesdismissReminder">Command `az groups group-event-instance dismiss-reminder`</a>


##### <a name="Parametersgroups.events.instancesdismissReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|

#### <a name="groups.events.instancesforward">Command `az groups group-event-instance forward`</a>


##### <a name="Parametersgroups.events.instancesforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|

#### <a name="groups.events.instancessnoozeReminder">Command `az groups group-event-instance snooze-reminder`</a>


##### <a name="Parametersgroups.events.instancessnoozeReminder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

#### <a name="groups.events.instancestentativelyAccept">Command `az groups group-event-instance tentatively-accept`</a>


##### <a name="Parametersgroups.events.instancestentativelyAccept">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--event-id1**|string|key: id of event|event_id1|event-id1|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|
|**--end**|object|dateTimeTimeZone|end|end|
|**--start**|object|dateTimeTimeZone|start|start|

### group `az groups group-group`
#### <a name="groups.groupCreateGroup">Command `az groups group-group create-group`</a>


##### <a name="Parametersgroups.groupCreateGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--assigned-labels**|array|The list of sensitivity label pairs (label ID, label name) associated with a Microsoft 365 group. Returned only on $select.|assigned_labels|assignedLabels|
|**--assigned-licenses**|array|The licenses that are assigned to the group. Returned only on $select. Read-only.|assigned_licenses|assignedLicenses|
|**--classification**|string|Describes a classification for the group (such as low, medium or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default.|classification|classification|
|**--created-date-time**|date-time|Timestamp of when the group was created. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only.|created_date_time|createdDateTime|
|**--description**|string|An optional description for the group. Returned by default.|description|description|
|**--display-name**|string|The display name for the group. This property is required when a group is created and cannot be cleared during updates. Returned by default. Supports $filter and $orderby.|display_name|displayName|
|**--expiration-date-time**|date-time|Timestamp of when the group is set to expire. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only.|expiration_date_time|expirationDateTime|
|**--group-types**|array|Specifies the group type and its membership.  If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static.  Returned by default. Supports $filter.|group_types|groupTypes|
|**--has-members-with-license-errors**|boolean|Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true).|has_members_with_license_errors|hasMembersWithLicenseErrors|
|**--is-assignable-to-role**|boolean|Indicates whether this group can be assigned to an Azure Active Directory role.This property can only be set while creating the group and is immutable. If set to true, the securityEnabled property must also be set to true and the group cannot be a dynamic group (that is, groupTypes cannot contain DynamicMembership).Only callers in Global Administrator and Privileged Role Administrator roles can set this property. For more, see Using a group to manage Azure AD role assignmentsReturned by default.|is_assignable_to_role|isAssignableToRole|
|**--mail**|string|The SMTP address for the group, for example, 'serviceadmins@contoso.onmicrosoft.com'. Returned by default. Read-only. Supports $filter.|mail|mail|
|**--mail-enabled**|boolean|Specifies whether the group is mail-enabled. Returned by default.|mail_enabled|mailEnabled|
|**--mail-nickname**|string|The mail alias for the group, unique in the organization. This property must be specified when a group is created. These characters cannot be used in the mailNickName: @()/[]';:.<>,SPACE. Returned by default. Supports $filter.|mail_nickname|mailNickname|
|**--membership-rule**|string|The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default.|membership_rule|membershipRule|
|**--membership-rule-processing-state**|string|Indicates whether the dynamic membership processing is on or paused. Possible values are On or Paused. Returned by default.|membership_rule_processing_state|membershipRuleProcessingState|
|**--on-premises-domain-name**|string|Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_domain_name|onPremisesDomainName|
|**--on-premises-last-sync-date-time**|date-time|Indicates the last time at which the group was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only. Supports $filter.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-net-bios-name**|string|Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_net_bios_name|onPremisesNetBiosName|
|**--on-premises-provisioning-errors**|array|Errors when using Microsoft synchronization product during provisioning. Returned by default.|on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--on-premises-sam-account-name**|string|Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_sam_account_name|onPremisesSamAccountName|
|**--on-premises-security-identifier**|string|Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Returned by default. Read-only.|on_premises_security_identifier|onPremisesSecurityIdentifier|
|**--on-premises-sync-enabled**|boolean|true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--preferred-data-location**|string|The preferred data location for the group. For more information, see  OneDrive Online Multi-Geo. Returned by default.|preferred_data_location|preferredDataLocation|
|**--preferred-language**|string|The preferred language for a Microsoft 365 group. Should follow ISO 639-1 Code; for example 'en-US'. Returned by default.|preferred_language|preferredLanguage|
|**--proxy-addresses**|array|Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required for filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter.|proxy_addresses|proxyAddresses|
|**--renewed-date-time**|date-time|Timestamp of when the group was last renewed. This cannot be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only.|renewed_date_time|renewedDateTime|
|**--security-enabled**|boolean|Specifies whether the group is a security group. Returned by default. Supports $filter.|security_enabled|securityEnabled|
|**--security-identifier**|string|Security identifier of the group, used in Windows scenarios. Returned by default.|security_identifier|securityIdentifier|
|**--theme**|string|Specifies a Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange or Red. Returned by default.|theme|theme|
|**--visibility**|string|Specifies the group join policy and group content visibility for groups. Possible values are: Private, Public, or Hiddenmembership. Hiddenmembership can be set only for Microsoft 365 groups, when the groups are created. It can't be updated later. Other values of visibility can be updated after group creation. If visibility value is not specified during group creation on Microsoft Graph, a security group is created as Private by default and Microsoft 365 group is Public. See group visibility options to learn more. Returned by default.|visibility|visibility|
|**--allow-external-senders**|boolean|Indicates if people external to the organization can send messages to the group. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).|allow_external_senders|allowExternalSenders|
|**--auto-subscribe-new-members**|boolean|Indicates if new members added to the group will be auto-subscribed to receive email notifications. You can set this property in a PATCH request for the group; do not set it in the initial POST request that creates the group. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).|auto_subscribe_new_members|autoSubscribeNewMembers|
|**--hide-from-address-lists**|boolean|true if the group is not displayed in certain parts of the Outlook user interface: in the Address Book, in address lists for selecting message recipients, and in the Browse Groups dialog for searching groups; false otherwise. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).|hide_from_address_lists|hideFromAddressLists|
|**--hide-from-outlook-clients**|boolean|true if the group is not displayed in Outlook clients, such as Outlook for Windows and Outlook on the web, false otherwise. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).|hide_from_outlook_clients|hideFromOutlookClients|
|**--is-subscribed-by-mail**|boolean|Indicates whether the signed-in user is subscribed to receive email conversations. Default value is true. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).|is_subscribed_by_mail|isSubscribedByMail|
|**--unseen-count**|integer|Count of conversations that have received new posts since the signed-in user last visited the group. This property is the same as unseenConversationsCount.Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).|unseen_count|unseenCount|
|**--is-archived**|boolean||is_archived|isArchived|
|**--app-role-assignments**|array|Represents the app roles a group has been granted for an application.|app_role_assignments|appRoleAssignments|
|**--created-on-behalf-of**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|created_on_behalf_of|createdOnBehalfOf|
|**--member-of**|array|Groups and administrative units that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--members**|array|Users, contacts, and groups that are members of this group. HTTP Methods: GET (supported for all groups), POST (supported for security groups and mail-enabled security groups), DELETE (supported only for security groups) Read-only. Nullable.|members|members|
|**--members-with-license-errors**|array|A list of group members with license errors from this group-based license assignment. Read-only.|members_with_license_errors|membersWithLicenseErrors|
|**--owners**|array|The owners of the group. The owners are a set of non-admin users who are allowed to modify this object. HTTP Methods: GET (supported for all groups), POST (supported for security groups and mail-enabled security groups), DELETE (supported only for security groups) Read-only. Nullable.|owners|owners|
|**--permission-grants**|array|The permissions that have been granted for a group to a specific application.|permission_grants|permissionGrants|
|**--settings**|array|Settings that can govern this group's behavior, like whether members can invite guest users to the group. Nullable.|settings|settings|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--transitive-members**|array||transitive_members|transitiveMembers|
|**--accepted-senders**|array|The list of users or groups that are allowed to create post's or calendar events in this group. If this list is non-empty then only users or groups listed here are allowed to post.|accepted_senders|acceptedSenders|
|**--calendar**|object|calendar|calendar|calendar|
|**--calendar-view**|array|The calendar view for the calendar. Read-only.|calendar_view|calendarView|
|**--conversations**|array|The group's conversations.|conversations|conversations|
|**--events**|array|The group's events.|events|events|
|**--photo**|object|profilePhoto|photo|photo|
|**--photos**|array|The profile photos owned by the group. Read-only. Nullable.|photos|photos|
|**--rejected-senders**|array|The list of users or groups that are not allowed to create posts or calendar events in this group. Nullable|rejected_senders|rejectedSenders|
|**--threads**|array|The group's conversation threads. Nullable.|threads|threads|
|**--drive**|object|drive|drive|drive|
|**--drives**|array|The group's drives. Read-only.|drives|drives|
|**--sites**|array|The list of SharePoint sites in this group. Access the default site with /sites/root.|sites|sites|
|**--extensions**|array|The collection of open extensions defined for the group. Read-only. Nullable.|extensions|extensions|
|**--group-lifecycle-policies**|array|The collection of lifecycle policies for this group. Read-only. Nullable.|group_lifecycle_policies|groupLifecyclePolicies|
|**--team**|object|team|team|team|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--notebooks**|array|The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.|notebooks|notebooks|
|**--operations**|array|The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.|operations|operations|
|**--pages**|array|The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|pages|pages|
|**--resources**|array|The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.|resources|resources|
|**--section-groups**|array|The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|section_groups|sectionGroups|
|**--sections**|array|The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|sections|sections|
|**--id1**|string|Read-only.|id1|id|
|**--plans**|array|Read-only. Nullable. Returns the plannerPlans owned by the group.|plans|plans|
|**--state**|string||state|state|

#### <a name="groups.groupDeleteGroup">Command `az groups group-group delete-group`</a>


##### <a name="Parametersgroups.groupDeleteGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.groupListGroup">Command `az groups group-group list-group`</a>


##### <a name="Parametersgroups.groupListGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--consistency-level**|string|Indicates the requested consistency level. Documentation URL: https://developer.microsoft.com/en-us/office/blogs/microsoft-graph-advanced-queries-for-directory-objects-are-now-generally-available/|consistency_level|ConsistencyLevel|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.groupGetGroup">Command `az groups group-group show-group`</a>


##### <a name="Parametersgroups.groupGetGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--consistency-level**|string|Indicates the requested consistency level. Documentation URL: https://developer.microsoft.com/en-us/office/blogs/microsoft-graph-advanced-queries-for-directory-objects-are-now-generally-available/|consistency_level|ConsistencyLevel|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.groupUpdateGroup">Command `az groups group-group update-group`</a>


##### <a name="Parametersgroups.groupUpdateGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--assigned-labels**|array|The list of sensitivity label pairs (label ID, label name) associated with a Microsoft 365 group. Returned only on $select.|assigned_labels|assignedLabels|
|**--assigned-licenses**|array|The licenses that are assigned to the group. Returned only on $select. Read-only.|assigned_licenses|assignedLicenses|
|**--classification**|string|Describes a classification for the group (such as low, medium or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default.|classification|classification|
|**--created-date-time**|date-time|Timestamp of when the group was created. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only.|created_date_time|createdDateTime|
|**--description**|string|An optional description for the group. Returned by default.|description|description|
|**--display-name**|string|The display name for the group. This property is required when a group is created and cannot be cleared during updates. Returned by default. Supports $filter and $orderby.|display_name|displayName|
|**--expiration-date-time**|date-time|Timestamp of when the group is set to expire. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only.|expiration_date_time|expirationDateTime|
|**--group-types**|array|Specifies the group type and its membership.  If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static.  Returned by default. Supports $filter.|group_types|groupTypes|
|**--has-members-with-license-errors**|boolean|Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true).|has_members_with_license_errors|hasMembersWithLicenseErrors|
|**--is-assignable-to-role**|boolean|Indicates whether this group can be assigned to an Azure Active Directory role.This property can only be set while creating the group and is immutable. If set to true, the securityEnabled property must also be set to true and the group cannot be a dynamic group (that is, groupTypes cannot contain DynamicMembership).Only callers in Global Administrator and Privileged Role Administrator roles can set this property. For more, see Using a group to manage Azure AD role assignmentsReturned by default.|is_assignable_to_role|isAssignableToRole|
|**--mail**|string|The SMTP address for the group, for example, 'serviceadmins@contoso.onmicrosoft.com'. Returned by default. Read-only. Supports $filter.|mail|mail|
|**--mail-enabled**|boolean|Specifies whether the group is mail-enabled. Returned by default.|mail_enabled|mailEnabled|
|**--mail-nickname**|string|The mail alias for the group, unique in the organization. This property must be specified when a group is created. These characters cannot be used in the mailNickName: @()/[]';:.<>,SPACE. Returned by default. Supports $filter.|mail_nickname|mailNickname|
|**--membership-rule**|string|The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default.|membership_rule|membershipRule|
|**--membership-rule-processing-state**|string|Indicates whether the dynamic membership processing is on or paused. Possible values are On or Paused. Returned by default.|membership_rule_processing_state|membershipRuleProcessingState|
|**--on-premises-domain-name**|string|Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_domain_name|onPremisesDomainName|
|**--on-premises-last-sync-date-time**|date-time|Indicates the last time at which the group was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only. Supports $filter.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-net-bios-name**|string|Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_net_bios_name|onPremisesNetBiosName|
|**--on-premises-provisioning-errors**|array|Errors when using Microsoft synchronization product during provisioning. Returned by default.|on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--on-premises-sam-account-name**|string|Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_sam_account_name|onPremisesSamAccountName|
|**--on-premises-security-identifier**|string|Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Returned by default. Read-only.|on_premises_security_identifier|onPremisesSecurityIdentifier|
|**--on-premises-sync-enabled**|boolean|true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--preferred-data-location**|string|The preferred data location for the group. For more information, see  OneDrive Online Multi-Geo. Returned by default.|preferred_data_location|preferredDataLocation|
|**--preferred-language**|string|The preferred language for a Microsoft 365 group. Should follow ISO 639-1 Code; for example 'en-US'. Returned by default.|preferred_language|preferredLanguage|
|**--proxy-addresses**|array|Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required for filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter.|proxy_addresses|proxyAddresses|
|**--renewed-date-time**|date-time|Timestamp of when the group was last renewed. This cannot be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only.|renewed_date_time|renewedDateTime|
|**--security-enabled**|boolean|Specifies whether the group is a security group. Returned by default. Supports $filter.|security_enabled|securityEnabled|
|**--security-identifier**|string|Security identifier of the group, used in Windows scenarios. Returned by default.|security_identifier|securityIdentifier|
|**--theme**|string|Specifies a Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange or Red. Returned by default.|theme|theme|
|**--visibility**|string|Specifies the group join policy and group content visibility for groups. Possible values are: Private, Public, or Hiddenmembership. Hiddenmembership can be set only for Microsoft 365 groups, when the groups are created. It can't be updated later. Other values of visibility can be updated after group creation. If visibility value is not specified during group creation on Microsoft Graph, a security group is created as Private by default and Microsoft 365 group is Public. See group visibility options to learn more. Returned by default.|visibility|visibility|
|**--allow-external-senders**|boolean|Indicates if people external to the organization can send messages to the group. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).|allow_external_senders|allowExternalSenders|
|**--auto-subscribe-new-members**|boolean|Indicates if new members added to the group will be auto-subscribed to receive email notifications. You can set this property in a PATCH request for the group; do not set it in the initial POST request that creates the group. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).|auto_subscribe_new_members|autoSubscribeNewMembers|
|**--hide-from-address-lists**|boolean|true if the group is not displayed in certain parts of the Outlook user interface: in the Address Book, in address lists for selecting message recipients, and in the Browse Groups dialog for searching groups; false otherwise. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).|hide_from_address_lists|hideFromAddressLists|
|**--hide-from-outlook-clients**|boolean|true if the group is not displayed in Outlook clients, such as Outlook for Windows and Outlook on the web, false otherwise. Default value is false. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).|hide_from_outlook_clients|hideFromOutlookClients|
|**--is-subscribed-by-mail**|boolean|Indicates whether the signed-in user is subscribed to receive email conversations. Default value is true. Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).|is_subscribed_by_mail|isSubscribedByMail|
|**--unseen-count**|integer|Count of conversations that have received new posts since the signed-in user last visited the group. This property is the same as unseenConversationsCount.Returned only on $select. Supported only on the Get group API (GET /groups/{ID}).|unseen_count|unseenCount|
|**--is-archived**|boolean||is_archived|isArchived|
|**--app-role-assignments**|array|Represents the app roles a group has been granted for an application.|app_role_assignments|appRoleAssignments|
|**--created-on-behalf-of**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|created_on_behalf_of|createdOnBehalfOf|
|**--member-of**|array|Groups and administrative units that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--members**|array|Users, contacts, and groups that are members of this group. HTTP Methods: GET (supported for all groups), POST (supported for security groups and mail-enabled security groups), DELETE (supported only for security groups) Read-only. Nullable.|members|members|
|**--members-with-license-errors**|array|A list of group members with license errors from this group-based license assignment. Read-only.|members_with_license_errors|membersWithLicenseErrors|
|**--owners**|array|The owners of the group. The owners are a set of non-admin users who are allowed to modify this object. HTTP Methods: GET (supported for all groups), POST (supported for security groups and mail-enabled security groups), DELETE (supported only for security groups) Read-only. Nullable.|owners|owners|
|**--permission-grants**|array|The permissions that have been granted for a group to a specific application.|permission_grants|permissionGrants|
|**--settings**|array|Settings that can govern this group's behavior, like whether members can invite guest users to the group. Nullable.|settings|settings|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--transitive-members**|array||transitive_members|transitiveMembers|
|**--accepted-senders**|array|The list of users or groups that are allowed to create post's or calendar events in this group. If this list is non-empty then only users or groups listed here are allowed to post.|accepted_senders|acceptedSenders|
|**--calendar**|object|calendar|calendar|calendar|
|**--calendar-view**|array|The calendar view for the calendar. Read-only.|calendar_view|calendarView|
|**--conversations**|array|The group's conversations.|conversations|conversations|
|**--events**|array|The group's events.|events|events|
|**--photo**|object|profilePhoto|photo|photo|
|**--photos**|array|The profile photos owned by the group. Read-only. Nullable.|photos|photos|
|**--rejected-senders**|array|The list of users or groups that are not allowed to create posts or calendar events in this group. Nullable|rejected_senders|rejectedSenders|
|**--threads**|array|The group's conversation threads. Nullable.|threads|threads|
|**--drive**|object|drive|drive|drive|
|**--drives**|array|The group's drives. Read-only.|drives|drives|
|**--sites**|array|The list of SharePoint sites in this group. Access the default site with /sites/root.|sites|sites|
|**--extensions**|array|The collection of open extensions defined for the group. Read-only. Nullable.|extensions|extensions|
|**--group-lifecycle-policies**|array|The collection of lifecycle policies for this group. Read-only. Nullable.|group_lifecycle_policies|groupLifecyclePolicies|
|**--team**|object|team|team|team|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--notebooks**|array|The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.|notebooks|notebooks|
|**--operations**|array|The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.|operations|operations|
|**--pages**|array|The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|pages|pages|
|**--resources**|array|The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.|resources|resources|
|**--section-groups**|array|The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|section_groups|sectionGroups|
|**--sections**|array|The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|sections|sections|
|**--id1**|string|Read-only.|id1|id|
|**--plans**|array|Read-only. Nullable. Returns the plannerPlans owned by the group.|plans|plans|
|**--state**|string||state|state|

### group `az groups group-lifecycle-policy`
#### <a name="groupLifecyclePoliciesaddGroup">Command `az groups group-lifecycle-policy add-group`</a>


##### <a name="ParametersgroupLifecyclePoliciesaddGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-lifecycle-policy-id**|string|key: id of groupLifecyclePolicy|group_lifecycle_policy_id|groupLifecyclePolicy-id|
|**--group-id**|string||group_id|groupId|

#### <a name="groupLifecyclePoliciesremoveGroup">Command `az groups group-lifecycle-policy remove-group`</a>


##### <a name="ParametersgroupLifecyclePoliciesremoveGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-lifecycle-policy-id**|string|key: id of groupLifecyclePolicy|group_lifecycle_policy_id|groupLifecyclePolicy-id|
|**--group-id**|string||group_id|groupId|

### group `az groups group-lifecycle-policy-group-lifecycle-policy`
#### <a name="groupLifecyclePolicies.groupLifecyclePolicyCreateGroupLifecyclePolicy">Command `az groups group-lifecycle-policy-group-lifecycle-policy create-group-lifecycle-policy`</a>


##### <a name="ParametersgroupLifecyclePolicies.groupLifecyclePolicyCreateGroupLifecyclePolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--alternate-notification-emails**|string|List of email address to send notifications for groups without owners. Multiple email address can be defined by separating email address with a semicolon.|alternate_notification_emails|alternateNotificationEmails|
|**--group-lifetime-in-days**|integer|Number of days before a group expires and needs to be renewed. Once renewed, the group expiration is extended by the number of days defined.|group_lifetime_in_days|groupLifetimeInDays|
|**--managed-group-types**|string|The group type for which the expiration policy applies. Possible values are All, Selected or None.|managed_group_types|managedGroupTypes|

#### <a name="groupLifecyclePolicies.groupLifecyclePolicyDeleteGroupLifecyclePolicy">Command `az groups group-lifecycle-policy-group-lifecycle-policy delete-group-lifecycle-policy`</a>


##### <a name="ParametersgroupLifecyclePolicies.groupLifecyclePolicyDeleteGroupLifecyclePolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-lifecycle-policy-id**|string|key: id of groupLifecyclePolicy|group_lifecycle_policy_id|groupLifecyclePolicy-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupLifecyclePolicies.groupLifecyclePolicyListGroupLifecyclePolicy">Command `az groups group-lifecycle-policy-group-lifecycle-policy list-group-lifecycle-policy`</a>


##### <a name="ParametersgroupLifecyclePolicies.groupLifecyclePolicyListGroupLifecyclePolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupLifecyclePolicies.groupLifecyclePolicyGetGroupLifecyclePolicy">Command `az groups group-lifecycle-policy-group-lifecycle-policy show-group-lifecycle-policy`</a>


##### <a name="ParametersgroupLifecyclePolicies.groupLifecyclePolicyGetGroupLifecyclePolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-lifecycle-policy-id**|string|key: id of groupLifecyclePolicy|group_lifecycle_policy_id|groupLifecyclePolicy-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupLifecyclePolicies.groupLifecyclePolicyUpdateGroupLifecyclePolicy">Command `az groups group-lifecycle-policy-group-lifecycle-policy update-group-lifecycle-policy`</a>


##### <a name="ParametersgroupLifecyclePolicies.groupLifecyclePolicyUpdateGroupLifecyclePolicy">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-lifecycle-policy-id**|string|key: id of groupLifecyclePolicy|group_lifecycle_policy_id|groupLifecyclePolicy-id|
|**--id**|string|Read-only.|id|id|
|**--alternate-notification-emails**|string|List of email address to send notifications for groups without owners. Multiple email address can be defined by separating email address with a semicolon.|alternate_notification_emails|alternateNotificationEmails|
|**--group-lifetime-in-days**|integer|Number of days before a group expires and needs to be renewed. Once renewed, the group expiration is extended by the number of days defined.|group_lifetime_in_days|groupLifetimeInDays|
|**--managed-group-types**|string|The group type for which the expiration policy applies. Possible values are All, Selected or None.|managed_group_types|managedGroupTypes|

### group `az groups group-onenote-notebook`
#### <a name="groups.onenote.notebookscopyNotebook">Command `az groups group-onenote-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.notebookscopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.notebooksgetNotebookFromWebUrl">Command `az groups group-onenote-notebook get-notebook-from-web-url`</a>


##### <a name="Parametersgroups.onenote.notebooksgetNotebookFromWebUrl">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--web-url**|string||web_url|webUrl|

#### <a name="groups.onenote.notebooksgetRecentNotebooks">Command `az groups group-onenote-notebook show-recent-notebook`</a>


##### <a name="Parametersgroups.onenote.notebooksgetRecentNotebooks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--include-personal-notebooks**|boolean|Usage: includePersonalNotebooks={includePersonalNotebooks}|include_personal_notebooks|includePersonalNotebooks|

### group `az groups group-onenote-notebook-section`
#### <a name="groups.onenote.notebooks.sectionscopyToNotebook">Command `az groups group-onenote-notebook-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.notebooks.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.notebooks.sectionscopyToSectionGroup">Command `az groups group-onenote-notebook-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.notebooks.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-notebook-section-group-parent-notebook`
#### <a name="groups.onenote.notebooks.sectionGroups.parentNotebookcopyNotebook">Command `az groups group-onenote-notebook-section-group-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.notebooks.sectionGroups.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-notebook-section-group-section`
#### <a name="groups.onenote.notebooks.sectionGroups.sectionscopyToNotebook">Command `az groups group-onenote-notebook-section-group-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.notebooks.sectionGroups.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.notebooks.sectionGroups.sectionscopyToSectionGroup">Command `az groups group-onenote-notebook-section-group-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.notebooks.sectionGroups.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-notebook-section-group-section-page`
#### <a name="groups.onenote.notebooks.sectionGroups.sections.pagescopyToSection">Command `az groups group-onenote-notebook-section-group-section-page copy-to-section`</a>


##### <a name="Parametersgroups.onenote.notebooks.sectionGroups.sections.pagescopyToSection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.notebooks.sectionGroups.sections.pagesonenotePatchContent">Command `az groups group-onenote-notebook-section-group-section-page onenote-patch-content`</a>


##### <a name="Parametersgroups.onenote.notebooks.sectionGroups.sections.pagesonenotePatchContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

#### <a name="groups.onenote.notebooks.sectionGroups.sections.pagespreview">Command `az groups group-onenote-notebook-section-group-section-page preview`</a>


##### <a name="Parametersgroups.onenote.notebooks.sectionGroups.sections.pagespreview">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|

### group `az groups group-onenote-notebook-section-group-section-page-parent-notebook`
#### <a name="groups.onenote.notebooks.sectionGroups.sections.pages.parentNotebookcopyNotebook">Command `az groups group-onenote-notebook-section-group-section-page-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.notebooks.sectionGroups.sections.pages.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-notebook-section-group-section-page-parent-section`
#### <a name="groups.onenote.notebooks.sectionGroups.sections.pages.parentSectioncopyToNotebook">Command `az groups group-onenote-notebook-section-group-section-page-parent-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.notebooks.sectionGroups.sections.pages.parentSectioncopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.notebooks.sectionGroups.sections.pages.parentSectioncopyToSectionGroup">Command `az groups group-onenote-notebook-section-group-section-page-parent-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.notebooks.sectionGroups.sections.pages.parentSectioncopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-notebook-section-group-section-parent-notebook`
#### <a name="groups.onenote.notebooks.sectionGroups.sections.parentNotebookcopyNotebook">Command `az groups group-onenote-notebook-section-group-section-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.notebooks.sectionGroups.sections.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-notebook-section-page`
#### <a name="groups.onenote.notebooks.sections.pagescopyToSection">Command `az groups group-onenote-notebook-section-page copy-to-section`</a>


##### <a name="Parametersgroups.onenote.notebooks.sections.pagescopyToSection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.notebooks.sections.pagesonenotePatchContent">Command `az groups group-onenote-notebook-section-page onenote-patch-content`</a>


##### <a name="Parametersgroups.onenote.notebooks.sections.pagesonenotePatchContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

#### <a name="groups.onenote.notebooks.sections.pagespreview">Command `az groups group-onenote-notebook-section-page preview`</a>


##### <a name="Parametersgroups.onenote.notebooks.sections.pagespreview">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|

### group `az groups group-onenote-notebook-section-page-parent-notebook`
#### <a name="groups.onenote.notebooks.sections.pages.parentNotebookcopyNotebook">Command `az groups group-onenote-notebook-section-page-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.notebooks.sections.pages.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-notebook-section-page-parent-section`
#### <a name="groups.onenote.notebooks.sections.pages.parentSectioncopyToNotebook">Command `az groups group-onenote-notebook-section-page-parent-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.notebooks.sections.pages.parentSectioncopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.notebooks.sections.pages.parentSectioncopyToSectionGroup">Command `az groups group-onenote-notebook-section-page-parent-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.notebooks.sections.pages.parentSectioncopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-notebook-section-parent-notebook`
#### <a name="groups.onenote.notebooks.sections.parentNotebookcopyNotebook">Command `az groups group-onenote-notebook-section-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.notebooks.sections.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-notebook-section-parent-section-group-parent-notebook`
#### <a name="groups.onenote.notebooks.sections.parentSectionGroup.parentNotebookcopyNotebook">Command `az groups group-onenote-notebook-section-parent-section-group-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.notebooks.sections.parentSectionGroup.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-notebook-section-parent-section-group-section`
#### <a name="groups.onenote.notebooks.sections.parentSectionGroup.sectionscopyToNotebook">Command `az groups group-onenote-notebook-section-parent-section-group-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.notebooks.sections.parentSectionGroup.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.notebooks.sections.parentSectionGroup.sectionscopyToSectionGroup">Command `az groups group-onenote-notebook-section-parent-section-group-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.notebooks.sections.parentSectionGroup.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--notebook-id**|string|key: id of notebook|notebook_id|notebook-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page`
#### <a name="groups.onenote.pagescopyToSection">Command `az groups group-onenote-page copy-to-section`</a>


##### <a name="Parametersgroups.onenote.pagescopyToSection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.pagesonenotePatchContent">Command `az groups group-onenote-page onenote-patch-content`</a>


##### <a name="Parametersgroups.onenote.pagesonenotePatchContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

#### <a name="groups.onenote.pagespreview">Command `az groups group-onenote-page preview`</a>


##### <a name="Parametersgroups.onenote.pagespreview">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|

### group `az groups group-onenote-page-parent-notebook`
#### <a name="groups.onenote.pages.parentNotebookcopyNotebook">Command `az groups group-onenote-page-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page-parent-notebook-section`
#### <a name="groups.onenote.pages.parentNotebook.sectionscopyToNotebook">Command `az groups group-onenote-page-parent-notebook-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.pages.parentNotebook.sectionscopyToSectionGroup">Command `az groups group-onenote-page-parent-notebook-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page-parent-notebook-section-group-parent-notebook`
#### <a name="groups.onenote.pages.parentNotebook.sectionGroups.parentNotebookcopyNotebook">Command `az groups group-onenote-page-parent-notebook-section-group-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sectionGroups.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page-parent-notebook-section-group-section`
#### <a name="groups.onenote.pages.parentNotebook.sectionGroups.sectionscopyToNotebook">Command `az groups group-onenote-page-parent-notebook-section-group-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sectionGroups.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.pages.parentNotebook.sectionGroups.sectionscopyToSectionGroup">Command `az groups group-onenote-page-parent-notebook-section-group-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sectionGroups.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page-parent-notebook-section-group-section-page`
#### <a name="groups.onenote.pages.parentNotebook.sectionGroups.sections.pagescopyToSection">Command `az groups group-onenote-page-parent-notebook-section-group-section-page copy-to-section`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sectionGroups.sections.pagescopyToSection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.pages.parentNotebook.sectionGroups.sections.pagesonenotePatchContent">Command `az groups group-onenote-page-parent-notebook-section-group-section-page onenote-patch-content`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sectionGroups.sections.pagesonenotePatchContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--commands**|array||commands|commands|

#### <a name="groups.onenote.pages.parentNotebook.sectionGroups.sections.pagespreview">Command `az groups group-onenote-page-parent-notebook-section-group-section-page preview`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sectionGroups.sections.pagespreview">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|

### group `az groups group-onenote-page-parent-notebook-section-group-section-parent-notebook`
#### <a name="groups.onenote.pages.parentNotebook.sectionGroups.sections.parentNotebookcopyNotebook">Command `az groups group-onenote-page-parent-notebook-section-group-section-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sectionGroups.sections.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page-parent-notebook-section-page`
#### <a name="groups.onenote.pages.parentNotebook.sections.pagescopyToSection">Command `az groups group-onenote-page-parent-notebook-section-page copy-to-section`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sections.pagescopyToSection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.pages.parentNotebook.sections.pagesonenotePatchContent">Command `az groups group-onenote-page-parent-notebook-section-page onenote-patch-content`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sections.pagesonenotePatchContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--commands**|array||commands|commands|

#### <a name="groups.onenote.pages.parentNotebook.sections.pagespreview">Command `az groups group-onenote-page-parent-notebook-section-page preview`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sections.pagespreview">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|

### group `az groups group-onenote-page-parent-notebook-section-parent-notebook`
#### <a name="groups.onenote.pages.parentNotebook.sections.parentNotebookcopyNotebook">Command `az groups group-onenote-page-parent-notebook-section-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sections.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page-parent-notebook-section-parent-section-group-parent-notebook`
#### <a name="groups.onenote.pages.parentNotebook.sections.parentSectionGroup.parentNotebookcopyNotebook">Command `az groups group-onenote-page-parent-notebook-section-parent-section-group-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sections.parentSectionGroup.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page-parent-notebook-section-parent-section-group-section`
#### <a name="groups.onenote.pages.parentNotebook.sections.parentSectionGroup.sectionscopyToNotebook">Command `az groups group-onenote-page-parent-notebook-section-parent-section-group-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sections.parentSectionGroup.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.pages.parentNotebook.sections.parentSectionGroup.sectionscopyToSectionGroup">Command `az groups group-onenote-page-parent-notebook-section-parent-section-group-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.pages.parentNotebook.sections.parentSectionGroup.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page-parent-section`
#### <a name="groups.onenote.pages.parentSectioncopyToNotebook">Command `az groups group-onenote-page-parent-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentSectioncopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.pages.parentSectioncopyToSectionGroup">Command `az groups group-onenote-page-parent-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.pages.parentSectioncopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page-parent-section-page`
#### <a name="groups.onenote.pages.parentSection.pagescopyToSection">Command `az groups group-onenote-page-parent-section-page copy-to-section`</a>


##### <a name="Parametersgroups.onenote.pages.parentSection.pagescopyToSection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.pages.parentSection.pagesonenotePatchContent">Command `az groups group-onenote-page-parent-section-page onenote-patch-content`</a>


##### <a name="Parametersgroups.onenote.pages.parentSection.pagesonenotePatchContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|
|**--commands**|array||commands|commands|

#### <a name="groups.onenote.pages.parentSection.pagespreview">Command `az groups group-onenote-page-parent-section-page preview`</a>


##### <a name="Parametersgroups.onenote.pages.parentSection.pagespreview">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-page-id1**|string|key: id of onenotePage|onenote_page_id1|onenotePage-id1|

### group `az groups group-onenote-page-parent-section-parent-notebook`
#### <a name="groups.onenote.pages.parentSection.parentNotebookcopyNotebook">Command `az groups group-onenote-page-parent-section-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentSection.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page-parent-section-parent-notebook-section`
#### <a name="groups.onenote.pages.parentSection.parentNotebook.sectionscopyToNotebook">Command `az groups group-onenote-page-parent-section-parent-notebook-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentSection.parentNotebook.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.pages.parentSection.parentNotebook.sectionscopyToSectionGroup">Command `az groups group-onenote-page-parent-section-parent-notebook-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.pages.parentSection.parentNotebook.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page-parent-section-parent-notebook-section-group-parent-notebook`
#### <a name="groups.onenote.pages.parentSection.parentNotebook.sectionGroups.parentNotebookcopyNotebook">Command `az groups group-onenote-page-parent-section-parent-notebook-section-group-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentSection.parentNotebook.sectionGroups.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page-parent-section-parent-notebook-section-group-section`
#### <a name="groups.onenote.pages.parentSection.parentNotebook.sectionGroups.sectionscopyToNotebook">Command `az groups group-onenote-page-parent-section-parent-notebook-section-group-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentSection.parentNotebook.sectionGroups.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.pages.parentSection.parentNotebook.sectionGroups.sectionscopyToSectionGroup">Command `az groups group-onenote-page-parent-section-parent-notebook-section-group-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.pages.parentSection.parentNotebook.sectionGroups.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page-parent-section-parent-section-group-parent-notebook`
#### <a name="groups.onenote.pages.parentSection.parentSectionGroup.parentNotebookcopyNotebook">Command `az groups group-onenote-page-parent-section-parent-section-group-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentSection.parentSectionGroup.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page-parent-section-parent-section-group-parent-notebook-section`
#### <a name="groups.onenote.pages.parentSection.parentSectionGroup.parentNotebook.sectionscopyToNotebook">Command `az groups group-onenote-page-parent-section-parent-section-group-parent-notebook-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentSection.parentSectionGroup.parentNotebook.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.pages.parentSection.parentSectionGroup.parentNotebook.sectionscopyToSectionGroup">Command `az groups group-onenote-page-parent-section-parent-section-group-parent-notebook-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.pages.parentSection.parentSectionGroup.parentNotebook.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-page-parent-section-parent-section-group-section`
#### <a name="groups.onenote.pages.parentSection.parentSectionGroup.sectionscopyToNotebook">Command `az groups group-onenote-page-parent-section-parent-section-group-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.pages.parentSection.parentSectionGroup.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.pages.parentSection.parentSectionGroup.sectionscopyToSectionGroup">Command `az groups group-onenote-page-parent-section-parent-section-group-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.pages.parentSection.parentSectionGroup.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section`
#### <a name="groups.onenote.sectionscopyToNotebook">Command `az groups group-onenote-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sectionscopyToSectionGroup">Command `az groups group-onenote-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-group-parent-notebook`
#### <a name="groups.onenote.sectionGroups.parentNotebookcopyNotebook">Command `az groups group-onenote-section-group-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-group-parent-notebook-section`
#### <a name="groups.onenote.sectionGroups.parentNotebook.sectionscopyToNotebook">Command `az groups group-onenote-section-group-parent-notebook-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.parentNotebook.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sectionGroups.parentNotebook.sectionscopyToSectionGroup">Command `az groups group-onenote-section-group-parent-notebook-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.parentNotebook.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-group-parent-notebook-section-page`
#### <a name="groups.onenote.sectionGroups.parentNotebook.sections.pagescopyToSection">Command `az groups group-onenote-section-group-parent-notebook-section-page copy-to-section`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.parentNotebook.sections.pagescopyToSection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sectionGroups.parentNotebook.sections.pagesonenotePatchContent">Command `az groups group-onenote-section-group-parent-notebook-section-page onenote-patch-content`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.parentNotebook.sections.pagesonenotePatchContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

#### <a name="groups.onenote.sectionGroups.parentNotebook.sections.pagespreview">Command `az groups group-onenote-section-group-parent-notebook-section-page preview`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.parentNotebook.sections.pagespreview">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|

### group `az groups group-onenote-section-group-parent-notebook-section-page-parent-notebook`
#### <a name="groups.onenote.sectionGroups.parentNotebook.sections.pages.parentNotebookcopyNotebook">Command `az groups group-onenote-section-group-parent-notebook-section-page-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.parentNotebook.sections.pages.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-group-parent-notebook-section-page-parent-section`
#### <a name="groups.onenote.sectionGroups.parentNotebook.sections.pages.parentSectioncopyToNotebook">Command `az groups group-onenote-section-group-parent-notebook-section-page-parent-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.parentNotebook.sections.pages.parentSectioncopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sectionGroups.parentNotebook.sections.pages.parentSectioncopyToSectionGroup">Command `az groups group-onenote-section-group-parent-notebook-section-page-parent-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.parentNotebook.sections.pages.parentSectioncopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-group-parent-notebook-section-parent-notebook`
#### <a name="groups.onenote.sectionGroups.parentNotebook.sections.parentNotebookcopyNotebook">Command `az groups group-onenote-section-group-parent-notebook-section-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.parentNotebook.sections.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-group-section`
#### <a name="groups.onenote.sectionGroups.sectionscopyToNotebook">Command `az groups group-onenote-section-group-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sectionGroups.sectionscopyToSectionGroup">Command `az groups group-onenote-section-group-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-group-section-page`
#### <a name="groups.onenote.sectionGroups.sections.pagescopyToSection">Command `az groups group-onenote-section-group-section-page copy-to-section`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.sections.pagescopyToSection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sectionGroups.sections.pagesonenotePatchContent">Command `az groups group-onenote-section-group-section-page onenote-patch-content`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.sections.pagesonenotePatchContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

#### <a name="groups.onenote.sectionGroups.sections.pagespreview">Command `az groups group-onenote-section-group-section-page preview`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.sections.pagespreview">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|

### group `az groups group-onenote-section-group-section-page-parent-notebook`
#### <a name="groups.onenote.sectionGroups.sections.pages.parentNotebookcopyNotebook">Command `az groups group-onenote-section-group-section-page-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.sections.pages.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-group-section-page-parent-notebook-section`
#### <a name="groups.onenote.sectionGroups.sections.pages.parentNotebook.sectionscopyToNotebook">Command `az groups group-onenote-section-group-section-page-parent-notebook-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.sections.pages.parentNotebook.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sectionGroups.sections.pages.parentNotebook.sectionscopyToSectionGroup">Command `az groups group-onenote-section-group-section-page-parent-notebook-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.sections.pages.parentNotebook.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-group-section-page-parent-section`
#### <a name="groups.onenote.sectionGroups.sections.pages.parentSectioncopyToNotebook">Command `az groups group-onenote-section-group-section-page-parent-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.sections.pages.parentSectioncopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sectionGroups.sections.pages.parentSectioncopyToSectionGroup">Command `az groups group-onenote-section-group-section-page-parent-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.sections.pages.parentSectioncopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-group-section-parent-notebook`
#### <a name="groups.onenote.sectionGroups.sections.parentNotebookcopyNotebook">Command `az groups group-onenote-section-group-section-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.sections.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-group-section-parent-notebook-section`
#### <a name="groups.onenote.sectionGroups.sections.parentNotebook.sectionscopyToNotebook">Command `az groups group-onenote-section-group-section-parent-notebook-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.sections.parentNotebook.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sectionGroups.sections.parentNotebook.sectionscopyToSectionGroup">Command `az groups group-onenote-section-group-section-parent-notebook-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.sectionGroups.sections.parentNotebook.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-page`
#### <a name="groups.onenote.sections.pagescopyToSection">Command `az groups group-onenote-section-page copy-to-section`</a>


##### <a name="Parametersgroups.onenote.sections.pagescopyToSection">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sections.pagesonenotePatchContent">Command `az groups group-onenote-section-page onenote-patch-content`</a>


##### <a name="Parametersgroups.onenote.sections.pagesonenotePatchContent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

#### <a name="groups.onenote.sections.pagespreview">Command `az groups group-onenote-section-page preview`</a>


##### <a name="Parametersgroups.onenote.sections.pagespreview">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|

### group `az groups group-onenote-section-page-parent-notebook`
#### <a name="groups.onenote.sections.pages.parentNotebookcopyNotebook">Command `az groups group-onenote-section-page-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.sections.pages.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-page-parent-notebook-section`
#### <a name="groups.onenote.sections.pages.parentNotebook.sectionscopyToNotebook">Command `az groups group-onenote-section-page-parent-notebook-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.sections.pages.parentNotebook.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sections.pages.parentNotebook.sectionscopyToSectionGroup">Command `az groups group-onenote-section-page-parent-notebook-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.sections.pages.parentNotebook.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-page-parent-notebook-section-group-parent-notebook`
#### <a name="groups.onenote.sections.pages.parentNotebook.sectionGroups.parentNotebookcopyNotebook">Command `az groups group-onenote-section-page-parent-notebook-section-group-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.sections.pages.parentNotebook.sectionGroups.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-page-parent-notebook-section-group-section`
#### <a name="groups.onenote.sections.pages.parentNotebook.sectionGroups.sectionscopyToNotebook">Command `az groups group-onenote-section-page-parent-notebook-section-group-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.sections.pages.parentNotebook.sectionGroups.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sections.pages.parentNotebook.sectionGroups.sectionscopyToSectionGroup">Command `az groups group-onenote-section-page-parent-notebook-section-group-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.sections.pages.parentNotebook.sectionGroups.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-page-parent-section`
#### <a name="groups.onenote.sections.pages.parentSectioncopyToNotebook">Command `az groups group-onenote-section-page-parent-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.sections.pages.parentSectioncopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sections.pages.parentSectioncopyToSectionGroup">Command `az groups group-onenote-section-page-parent-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.sections.pages.parentSectioncopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-parent-notebook`
#### <a name="groups.onenote.sections.parentNotebookcopyNotebook">Command `az groups group-onenote-section-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.sections.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-parent-notebook-section`
#### <a name="groups.onenote.sections.parentNotebook.sectionscopyToNotebook">Command `az groups group-onenote-section-parent-notebook-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.sections.parentNotebook.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sections.parentNotebook.sectionscopyToSectionGroup">Command `az groups group-onenote-section-parent-notebook-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.sections.parentNotebook.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-parent-notebook-section-group-parent-notebook`
#### <a name="groups.onenote.sections.parentNotebook.sectionGroups.parentNotebookcopyNotebook">Command `az groups group-onenote-section-parent-notebook-section-group-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.sections.parentNotebook.sectionGroups.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-parent-notebook-section-group-section`
#### <a name="groups.onenote.sections.parentNotebook.sectionGroups.sectionscopyToNotebook">Command `az groups group-onenote-section-parent-notebook-section-group-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.sections.parentNotebook.sectionGroups.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sections.parentNotebook.sectionGroups.sectionscopyToSectionGroup">Command `az groups group-onenote-section-parent-notebook-section-group-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.sections.parentNotebook.sectionGroups.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--section-group-id**|string|key: id of sectionGroup|section_group_id|sectionGroup-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-parent-section-group-parent-notebook`
#### <a name="groups.onenote.sections.parentSectionGroup.parentNotebookcopyNotebook">Command `az groups group-onenote-section-parent-section-group-parent-notebook copy-notebook`</a>


##### <a name="Parametersgroups.onenote.sections.parentSectionGroup.parentNotebookcopyNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-parent-section-group-parent-notebook-section`
#### <a name="groups.onenote.sections.parentSectionGroup.parentNotebook.sectionscopyToNotebook">Command `az groups group-onenote-section-parent-section-group-parent-notebook-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.sections.parentSectionGroup.parentNotebook.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sections.parentSectionGroup.parentNotebook.sectionscopyToSectionGroup">Command `az groups group-onenote-section-parent-section-group-parent-notebook-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.sections.parentSectionGroup.parentNotebook.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-onenote-section-parent-section-group-section`
#### <a name="groups.onenote.sections.parentSectionGroup.sectionscopyToNotebook">Command `az groups group-onenote-section-parent-section-group-section copy-to-notebook`</a>


##### <a name="Parametersgroups.onenote.sections.parentSectionGroup.sectionscopyToNotebook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

#### <a name="groups.onenote.sections.parentSectionGroup.sectionscopyToSectionGroup">Command `az groups group-onenote-section-parent-section-group-section copy-to-section-group`</a>


##### <a name="Parametersgroups.onenote.sections.parentSectionGroup.sectionscopyToSectionGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--string-group-id**|string||string_group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### group `az groups group-thread`
#### <a name="groups.threadsCreatePosts">Command `az groups group-thread create-post`</a>


##### <a name="Parametersgroups.threadsCreatePosts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_modified_date_time|lastModifiedDateTime|
|**--body**|object|itemBody|body|body|
|**--conversation-id**|string|Unique ID of the conversation. Read-only.|conversation_id|conversationId|
|**--microsoft-graph-post-conversation-thread-id-conversation-thread-id**|string|Unique ID of the conversation thread. Read-only.|microsoft_graph_post_conversation_thread_id_conversation_thread_id|conversationThreadId|
|**--has-attachments**|boolean|Indicates whether the post has at least one attachment. This is a default property.|has_attachments|hasAttachments|
|**--new-participants**|array|Conversation participants that were added to the thread as part of this post.|new_participants|newParticipants|
|**--received-date-time**|date-time|Specifies when the post was received. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|received_date_time|receivedDateTime|
|**--attachments**|array|The collection of fileAttachment, itemAttachment, and referenceAttachment attachments for the post. Read-only. Nullable.|attachments|attachments|
|**--extensions**|array|The collection of open extensions defined for the post. Read-only. Nullable.|extensions|extensions|
|**--in-reply-to**|object|post|in_reply_to|inReplyTo|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the post. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the post. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--microsoft-graph-email-address**|object|emailAddress|microsoft_graph_email_address|emailAddress|

#### <a name="groups.threadsDeletePosts">Command `az groups group-thread delete-post`</a>


##### <a name="Parametersgroups.threadsDeletePosts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.threadsListPosts">Command `az groups group-thread list-post`</a>


##### <a name="Parametersgroups.threadsListPosts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.threadsreply">Command `az groups group-thread reply`</a>


##### <a name="Parametersgroups.threadsreply">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post**|object|post|post|Post|

#### <a name="groups.threadsGetPosts">Command `az groups group-thread show-post`</a>


##### <a name="Parametersgroups.threadsGetPosts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.threadsUpdatePosts">Command `az groups group-thread update-post`</a>


##### <a name="Parametersgroups.threadsUpdatePosts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_modified_date_time|lastModifiedDateTime|
|**--body**|object|itemBody|body|body|
|**--conversation-id**|string|Unique ID of the conversation. Read-only.|conversation_id|conversationId|
|**--microsoft-graph-post-conversation-thread-id-conversation-thread-id**|string|Unique ID of the conversation thread. Read-only.|microsoft_graph_post_conversation_thread_id_conversation_thread_id|conversationThreadId|
|**--has-attachments**|boolean|Indicates whether the post has at least one attachment. This is a default property.|has_attachments|hasAttachments|
|**--new-participants**|array|Conversation participants that were added to the thread as part of this post.|new_participants|newParticipants|
|**--received-date-time**|date-time|Specifies when the post was received. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|received_date_time|receivedDateTime|
|**--attachments**|array|The collection of fileAttachment, itemAttachment, and referenceAttachment attachments for the post. Read-only. Nullable.|attachments|attachments|
|**--extensions**|array|The collection of open extensions defined for the post. Read-only. Nullable.|extensions|extensions|
|**--in-reply-to**|object|post|in_reply_to|inReplyTo|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the post. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the post. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--microsoft-graph-email-address**|object|emailAddress|microsoft_graph_email_address|emailAddress|

### group `az groups group-thread-post`
#### <a name="groups.threads.postsCreateAttachments">Command `az groups group-thread-post create-attachment`</a>


##### <a name="Parametersgroups.threads.postsCreateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The display name of the attachment. This does not need to be the actual file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="groups.threads.postsCreateExtensions">Command `az groups group-thread-post create-extension`</a>


##### <a name="Parametersgroups.threads.postsCreateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|

#### <a name="groups.threads.postsCreateMultiValueExtendedProperties">Command `az groups group-thread-post create-multi-value-extended-property`</a>


##### <a name="Parametersgroups.threads.postsCreateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.threads.postsCreateSingleValueExtendedProperties">Command `az groups group-thread-post create-single-value-extended-property`</a>


##### <a name="Parametersgroups.threads.postsCreateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

#### <a name="groups.threads.postsDeleteAttachments">Command `az groups group-thread-post delete-attachment`</a>


##### <a name="Parametersgroups.threads.postsDeleteAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.threads.postsDeleteExtensions">Command `az groups group-thread-post delete-extension`</a>


##### <a name="Parametersgroups.threads.postsDeleteExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.threads.postsDeleteInReplyTo">Command `az groups group-thread-post delete-in-reply-to`</a>


##### <a name="Parametersgroups.threads.postsDeleteInReplyTo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.threads.postsDeleteMultiValueExtendedProperties">Command `az groups group-thread-post delete-multi-value-extended-property`</a>


##### <a name="Parametersgroups.threads.postsDeleteMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.threads.postsDeleteSingleValueExtendedProperties">Command `az groups group-thread-post delete-single-value-extended-property`</a>


##### <a name="Parametersgroups.threads.postsDeleteSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groups.threads.postsforward">Command `az groups group-thread-post forward`</a>


##### <a name="Parametersgroups.threads.postsforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--comment**|string||comment|Comment|
|**--to-recipients**|array||to_recipients|ToRecipients|

#### <a name="groups.threads.postsListAttachments">Command `az groups group-thread-post list-attachment`</a>


##### <a name="Parametersgroups.threads.postsListAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.threads.postsListExtensions">Command `az groups group-thread-post list-extension`</a>


##### <a name="Parametersgroups.threads.postsListExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.threads.postsListMultiValueExtendedProperties">Command `az groups group-thread-post list-multi-value-extended-property`</a>


##### <a name="Parametersgroups.threads.postsListMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.threads.postsListSingleValueExtendedProperties">Command `az groups group-thread-post list-single-value-extended-property`</a>


##### <a name="Parametersgroups.threads.postsListSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.threads.postsreply">Command `az groups group-thread-post reply`</a>


##### <a name="Parametersgroups.threads.postsreply">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--post**|object|post|post|Post|

#### <a name="groups.threads.postsGetAttachments">Command `az groups group-thread-post show-attachment`</a>


##### <a name="Parametersgroups.threads.postsGetAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.threads.postsGetExtensions">Command `az groups group-thread-post show-extension`</a>


##### <a name="Parametersgroups.threads.postsGetExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.threads.postsGetInReplyTo">Command `az groups group-thread-post show-in-reply-to`</a>


##### <a name="Parametersgroups.threads.postsGetInReplyTo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.threads.postsGetMultiValueExtendedProperties">Command `az groups group-thread-post show-multi-value-extended-property`</a>


##### <a name="Parametersgroups.threads.postsGetMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.threads.postsGetSingleValueExtendedProperties">Command `az groups group-thread-post show-single-value-extended-property`</a>


##### <a name="Parametersgroups.threads.postsGetSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groups.threads.postsUpdateAttachments">Command `az groups group-thread-post update-attachment`</a>


##### <a name="Parametersgroups.threads.postsUpdateAttachments">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--attachment-id**|string|key: id of attachment|attachment_id|attachment-id|
|**--id**|string|Read-only.|id|id|
|**--content-type**|string|The MIME type.|content_type|contentType|
|**--is-inline**|boolean|true if the attachment is an inline attachment; otherwise, false.|is_inline|isInline|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The display name of the attachment. This does not need to be the actual file name.|name|name|
|**--size**|integer|The length of the attachment in bytes.|size|size|

#### <a name="groups.threads.postsUpdateExtensions">Command `az groups group-thread-post update-extension`</a>


##### <a name="Parametersgroups.threads.postsUpdateExtensions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--extension-id**|string|key: id of extension|extension_id|extension-id|
|**--id**|string|Read-only.|id|id|

#### <a name="groups.threads.postsUpdateInReplyTo">Command `az groups group-thread-post update-in-reply-to`</a>


##### <a name="Parametersgroups.threads.postsUpdateInReplyTo">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--id**|string|Read-only.|id|id|
|**--categories**|array|The categories associated with the item|categories|categories|
|**--change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|last_modified_date_time|lastModifiedDateTime|
|**--body**|object|itemBody|body|body|
|**--conversation-id**|string|Unique ID of the conversation. Read-only.|conversation_id|conversationId|
|**--microsoft-graph-post-conversation-thread-id-conversation-thread-id**|string|Unique ID of the conversation thread. Read-only.|microsoft_graph_post_conversation_thread_id_conversation_thread_id|conversationThreadId|
|**--has-attachments**|boolean|Indicates whether the post has at least one attachment. This is a default property.|has_attachments|hasAttachments|
|**--new-participants**|array|Conversation participants that were added to the thread as part of this post.|new_participants|newParticipants|
|**--received-date-time**|date-time|Specifies when the post was received. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z|received_date_time|receivedDateTime|
|**--attachments**|array|The collection of fileAttachment, itemAttachment, and referenceAttachment attachments for the post. Read-only. Nullable.|attachments|attachments|
|**--extensions**|array|The collection of open extensions defined for the post. Read-only. Nullable.|extensions|extensions|
|**--in-reply-to**|object|post|in_reply_to|inReplyTo|
|**--multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the post. Read-only. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--single-value-extended-properties**|array|The collection of single-value extended properties defined for the post. Read-only. Nullable.|single_value_extended_properties|singleValueExtendedProperties|
|**--email-address**|object|emailAddress|email_address|emailAddress|
|**--microsoft-graph-email-address**|object|emailAddress|microsoft_graph_email_address|emailAddress|

#### <a name="groups.threads.postsUpdateMultiValueExtendedProperties">Command `az groups group-thread-post update-multi-value-extended-property`</a>


##### <a name="Parametersgroups.threads.postsUpdateMultiValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--multi-value-legacy-extended-property-id**|string|key: id of multiValueLegacyExtendedProperty|multi_value_legacy_extended_property_id|multiValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|array|A collection of property values.|value|value|

#### <a name="groups.threads.postsUpdateSingleValueExtendedProperties">Command `az groups group-thread-post update-single-value-extended-property`</a>


##### <a name="Parametersgroups.threads.postsUpdateSingleValueExtendedProperties">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--single-value-legacy-extended-property-id**|string|key: id of singleValueLegacyExtendedProperty|single_value_legacy_extended_property_id|singleValueLegacyExtendedProperty-id|
|**--id**|string|Read-only.|id|id|
|**--value**|string|A property value.|value|value|

### group `az groups group-thread-post-attachment`
#### <a name="groups.threads.posts.attachmentscreateUploadSession">Command `az groups group-thread-post-attachment create-upload-session`</a>


##### <a name="Parametersgroups.threads.posts.attachmentscreateUploadSession">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### group `az groups group-thread-post-in-reply-to`
#### <a name="groups.threads.posts.inReplyToforward">Command `az groups group-thread-post-in-reply-to forward`</a>


##### <a name="Parametersgroups.threads.posts.inReplyToforward">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--comment**|string||comment|Comment|
|**--to-recipients**|array||to_recipients|ToRecipients|

#### <a name="groups.threads.posts.inReplyToreply">Command `az groups group-thread-post-in-reply-to reply`</a>


##### <a name="Parametersgroups.threads.posts.inReplyToreply">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--conversation-thread-id**|string|key: id of conversationThread|conversation_thread_id|conversationThread-id|
|**--post-id**|string|key: id of post|post_id|post-id|
|**--post**|object|post|post|Post|
