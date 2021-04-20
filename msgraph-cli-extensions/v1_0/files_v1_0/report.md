# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az files_v1_0|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az files_v1_0` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az files drivesdrive|drives.drive|[commands](#CommandsIndrives.drive)|
|az files drive|drives|[commands](#CommandsIndrives)|
|az files driveslist|drives.list|[commands](#CommandsIndrives.list)|
|az files driveslistcontenttype|drives.list.contentTypes|[commands](#CommandsIndrives.list.contentTypes)|
|az files driveslistitem|drives.list.items|[commands](#CommandsIndrives.list.items)|
|az files driveslistitemsversion|drives.list.items.versions|[commands](#CommandsIndrives.list.items.versions)|
|az files group|groups|[commands](#CommandsIngroups)|
|az files sharesshareddriveitem|shares.sharedDriveItem|[commands](#CommandsInshares.sharedDriveItem)|
|az files share|shares|[commands](#CommandsInshares)|
|az files shareslist|shares.list|[commands](#CommandsInshares.list)|
|az files shareslistcontenttype|shares.list.contentTypes|[commands](#CommandsInshares.list.contentTypes)|
|az files shareslistitem|shares.list.items|[commands](#CommandsInshares.list.items)|
|az files shareslistitemsversion|shares.list.items.versions|[commands](#CommandsInshares.list.items.versions)|
|az files shareslistitem|shares.listItem|[commands](#CommandsInshares.listItem)|
|az files shareslistitemversion|shares.listItem.versions|[commands](#CommandsInshares.listItem.versions)|
|az files sharespermission|shares.permission|[commands](#CommandsInshares.permission)|
|az files user|users|[commands](#CommandsInusers)|

## COMMANDS
### <a name="CommandsIndrives">Commands in `az files drive` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files drive create-following](#drivesCreateFollowing)|CreateFollowing|[Parameters](#ParametersdrivesCreateFollowing)|Not Found|
|[az files drive create-item](#drivesCreateItems)|CreateItems|[Parameters](#ParametersdrivesCreateItems)|Not Found|
|[az files drive create-special](#drivesCreateSpecial)|CreateSpecial|[Parameters](#ParametersdrivesCreateSpecial)|Not Found|
|[az files drive delete-following](#drivesDeleteFollowing)|DeleteFollowing|[Parameters](#ParametersdrivesDeleteFollowing)|Not Found|
|[az files drive delete-item](#drivesDeleteItems)|DeleteItems|[Parameters](#ParametersdrivesDeleteItems)|Not Found|
|[az files drive delete-list](#drivesDeleteList)|DeleteList|[Parameters](#ParametersdrivesDeleteList)|Not Found|
|[az files drive delete-root](#drivesDeleteRoot)|DeleteRoot|[Parameters](#ParametersdrivesDeleteRoot)|Not Found|
|[az files drive delete-special](#drivesDeleteSpecial)|DeleteSpecial|[Parameters](#ParametersdrivesDeleteSpecial)|Not Found|
|[az files drive list-following](#drivesListFollowing)|ListFollowing|[Parameters](#ParametersdrivesListFollowing)|Not Found|
|[az files drive list-item](#drivesListItems)|ListItems|[Parameters](#ParametersdrivesListItems)|Not Found|
|[az files drive list-special](#drivesListSpecial)|ListSpecial|[Parameters](#ParametersdrivesListSpecial)|Not Found|
|[az files drive recent](#drivesrecent)|recent|[Parameters](#Parametersdrivesrecent)|Not Found|
|[az files drive search](#drivessearch)|search|[Parameters](#Parametersdrivessearch)|Not Found|
|[az files drive shared-with-me](#drivessharedWithMe)|sharedWithMe|[Parameters](#ParametersdrivessharedWithMe)|Not Found|
|[az files drive show-following](#drivesGetFollowing)|GetFollowing|[Parameters](#ParametersdrivesGetFollowing)|Not Found|
|[az files drive show-item](#drivesGetItems)|GetItems|[Parameters](#ParametersdrivesGetItems)|Not Found|
|[az files drive show-list](#drivesGetList)|GetList|[Parameters](#ParametersdrivesGetList)|Not Found|
|[az files drive show-root](#drivesGetRoot)|GetRoot|[Parameters](#ParametersdrivesGetRoot)|Not Found|
|[az files drive show-special](#drivesGetSpecial)|GetSpecial|[Parameters](#ParametersdrivesGetSpecial)|Not Found|
|[az files drive update-following](#drivesUpdateFollowing)|UpdateFollowing|[Parameters](#ParametersdrivesUpdateFollowing)|Not Found|
|[az files drive update-item](#drivesUpdateItems)|UpdateItems|[Parameters](#ParametersdrivesUpdateItems)|Not Found|
|[az files drive update-list](#drivesUpdateList)|UpdateList|[Parameters](#ParametersdrivesUpdateList)|Not Found|
|[az files drive update-root](#drivesUpdateRoot)|UpdateRoot|[Parameters](#ParametersdrivesUpdateRoot)|Not Found|
|[az files drive update-special](#drivesUpdateSpecial)|UpdateSpecial|[Parameters](#ParametersdrivesUpdateSpecial)|Not Found|

### <a name="CommandsIndrives.drive">Commands in `az files drivesdrive` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files drivesdrive create-drive](#drives.driveCreateDrive)|CreateDrive|[Parameters](#Parametersdrives.driveCreateDrive)|Not Found|
|[az files drivesdrive delete-drive](#drives.driveDeleteDrive)|DeleteDrive|[Parameters](#Parametersdrives.driveDeleteDrive)|Not Found|
|[az files drivesdrive list-drive](#drives.driveListDrive)|ListDrive|[Parameters](#Parametersdrives.driveListDrive)|Not Found|
|[az files drivesdrive show-drive](#drives.driveGetDrive)|GetDrive|[Parameters](#Parametersdrives.driveGetDrive)|Not Found|
|[az files drivesdrive update-drive](#drives.driveUpdateDrive)|UpdateDrive|[Parameters](#Parametersdrives.driveUpdateDrive)|Not Found|

### <a name="CommandsIndrives.list">Commands in `az files driveslist` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files driveslist create-column](#drives.listCreateColumns)|CreateColumns|[Parameters](#Parametersdrives.listCreateColumns)|Not Found|
|[az files driveslist create-content-type](#drives.listCreateContentTypes)|CreateContentTypes|[Parameters](#Parametersdrives.listCreateContentTypes)|Not Found|
|[az files driveslist create-item](#drives.listCreateItems)|CreateItems|[Parameters](#Parametersdrives.listCreateItems)|Not Found|
|[az files driveslist create-subscription](#drives.listCreateSubscriptions)|CreateSubscriptions|[Parameters](#Parametersdrives.listCreateSubscriptions)|Not Found|
|[az files driveslist delete-column](#drives.listDeleteColumns)|DeleteColumns|[Parameters](#Parametersdrives.listDeleteColumns)|Not Found|
|[az files driveslist delete-content-type](#drives.listDeleteContentTypes)|DeleteContentTypes|[Parameters](#Parametersdrives.listDeleteContentTypes)|Not Found|
|[az files driveslist delete-drive](#drives.listDeleteDrive)|DeleteDrive|[Parameters](#Parametersdrives.listDeleteDrive)|Not Found|
|[az files driveslist delete-item](#drives.listDeleteItems)|DeleteItems|[Parameters](#Parametersdrives.listDeleteItems)|Not Found|
|[az files driveslist delete-subscription](#drives.listDeleteSubscriptions)|DeleteSubscriptions|[Parameters](#Parametersdrives.listDeleteSubscriptions)|Not Found|
|[az files driveslist list-column](#drives.listListColumns)|ListColumns|[Parameters](#Parametersdrives.listListColumns)|Not Found|
|[az files driveslist list-content-type](#drives.listListContentTypes)|ListContentTypes|[Parameters](#Parametersdrives.listListContentTypes)|Not Found|
|[az files driveslist list-item](#drives.listListItems)|ListItems|[Parameters](#Parametersdrives.listListItems)|Not Found|
|[az files driveslist list-subscription](#drives.listListSubscriptions)|ListSubscriptions|[Parameters](#Parametersdrives.listListSubscriptions)|Not Found|
|[az files driveslist show-column](#drives.listGetColumns)|GetColumns|[Parameters](#Parametersdrives.listGetColumns)|Not Found|
|[az files driveslist show-content-type](#drives.listGetContentTypes)|GetContentTypes|[Parameters](#Parametersdrives.listGetContentTypes)|Not Found|
|[az files driveslist show-drive](#drives.listGetDrive)|GetDrive|[Parameters](#Parametersdrives.listGetDrive)|Not Found|
|[az files driveslist show-item](#drives.listGetItems)|GetItems|[Parameters](#Parametersdrives.listGetItems)|Not Found|
|[az files driveslist show-subscription](#drives.listGetSubscriptions)|GetSubscriptions|[Parameters](#Parametersdrives.listGetSubscriptions)|Not Found|
|[az files driveslist update-column](#drives.listUpdateColumns)|UpdateColumns|[Parameters](#Parametersdrives.listUpdateColumns)|Not Found|
|[az files driveslist update-content-type](#drives.listUpdateContentTypes)|UpdateContentTypes|[Parameters](#Parametersdrives.listUpdateContentTypes)|Not Found|
|[az files driveslist update-drive](#drives.listUpdateDrive)|UpdateDrive|[Parameters](#Parametersdrives.listUpdateDrive)|Not Found|
|[az files driveslist update-item](#drives.listUpdateItems)|UpdateItems|[Parameters](#Parametersdrives.listUpdateItems)|Not Found|
|[az files driveslist update-subscription](#drives.listUpdateSubscriptions)|UpdateSubscriptions|[Parameters](#Parametersdrives.listUpdateSubscriptions)|Not Found|

### <a name="CommandsIndrives.list.contentTypes">Commands in `az files driveslistcontenttype` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files driveslistcontenttype create-column-link](#drives.list.contentTypesCreateColumnLinks)|CreateColumnLinks|[Parameters](#Parametersdrives.list.contentTypesCreateColumnLinks)|Not Found|
|[az files driveslistcontenttype delete-column-link](#drives.list.contentTypesDeleteColumnLinks)|DeleteColumnLinks|[Parameters](#Parametersdrives.list.contentTypesDeleteColumnLinks)|Not Found|
|[az files driveslistcontenttype list-column-link](#drives.list.contentTypesListColumnLinks)|ListColumnLinks|[Parameters](#Parametersdrives.list.contentTypesListColumnLinks)|Not Found|
|[az files driveslistcontenttype show-column-link](#drives.list.contentTypesGetColumnLinks)|GetColumnLinks|[Parameters](#Parametersdrives.list.contentTypesGetColumnLinks)|Not Found|
|[az files driveslistcontenttype update-column-link](#drives.list.contentTypesUpdateColumnLinks)|UpdateColumnLinks|[Parameters](#Parametersdrives.list.contentTypesUpdateColumnLinks)|Not Found|

### <a name="CommandsIndrives.list.items">Commands in `az files driveslistitem` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files driveslistitem create-version](#drives.list.itemsCreateVersions)|CreateVersions|[Parameters](#Parametersdrives.list.itemsCreateVersions)|Not Found|
|[az files driveslistitem delete-drive-item](#drives.list.itemsDeleteDriveItem)|DeleteDriveItem|[Parameters](#Parametersdrives.list.itemsDeleteDriveItem)|Not Found|
|[az files driveslistitem delete-field](#drives.list.itemsDeleteFields)|DeleteFields|[Parameters](#Parametersdrives.list.itemsDeleteFields)|Not Found|
|[az files driveslistitem delete-ref-analytic](#drives.list.itemsDeleteRefAnalytics)|DeleteRefAnalytics|[Parameters](#Parametersdrives.list.itemsDeleteRefAnalytics)|Not Found|
|[az files driveslistitem delete-version](#drives.list.itemsDeleteVersions)|DeleteVersions|[Parameters](#Parametersdrives.list.itemsDeleteVersions)|Not Found|
|[az files driveslistitem list-version](#drives.list.itemsListVersions)|ListVersions|[Parameters](#Parametersdrives.list.itemsListVersions)|Not Found|
|[az files driveslistitem set-ref-analytic](#drives.list.itemsSetRefAnalytics)|SetRefAnalytics|[Parameters](#Parametersdrives.list.itemsSetRefAnalytics)|Not Found|
|[az files driveslistitem show-activity](#drives.list.itemsgetActivitiesByInterval-53ee)|getActivitiesByInterval-53ee|[Parameters](#Parametersdrives.list.itemsgetActivitiesByInterval-53ee)|Not Found|
|[az files driveslistitem show-activity](#drives.list.itemsgetActivitiesByInterval-96b0)|getActivitiesByInterval-96b0|[Parameters](#Parametersdrives.list.itemsgetActivitiesByInterval-96b0)|Not Found|
|[az files driveslistitem show-analytic](#drives.list.itemsGetAnalytics)|GetAnalytics|[Parameters](#Parametersdrives.list.itemsGetAnalytics)|Not Found|
|[az files driveslistitem show-drive-item](#drives.list.itemsGetDriveItem)|GetDriveItem|[Parameters](#Parametersdrives.list.itemsGetDriveItem)|Not Found|
|[az files driveslistitem show-field](#drives.list.itemsGetFields)|GetFields|[Parameters](#Parametersdrives.list.itemsGetFields)|Not Found|
|[az files driveslistitem show-ref-analytic](#drives.list.itemsGetRefAnalytics)|GetRefAnalytics|[Parameters](#Parametersdrives.list.itemsGetRefAnalytics)|Not Found|
|[az files driveslistitem show-version](#drives.list.itemsGetVersions)|GetVersions|[Parameters](#Parametersdrives.list.itemsGetVersions)|Not Found|
|[az files driveslistitem update-drive-item](#drives.list.itemsUpdateDriveItem)|UpdateDriveItem|[Parameters](#Parametersdrives.list.itemsUpdateDriveItem)|Not Found|
|[az files driveslistitem update-field](#drives.list.itemsUpdateFields)|UpdateFields|[Parameters](#Parametersdrives.list.itemsUpdateFields)|Not Found|
|[az files driveslistitem update-version](#drives.list.itemsUpdateVersions)|UpdateVersions|[Parameters](#Parametersdrives.list.itemsUpdateVersions)|Not Found|

### <a name="CommandsIndrives.list.items.versions">Commands in `az files driveslistitemsversion` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files driveslistitemsversion delete-field](#drives.list.items.versionsDeleteFields)|DeleteFields|[Parameters](#Parametersdrives.list.items.versionsDeleteFields)|Not Found|
|[az files driveslistitemsversion restore-version](#drives.list.items.versionsrestoreVersion)|restoreVersion|[Parameters](#Parametersdrives.list.items.versionsrestoreVersion)|Not Found|
|[az files driveslistitemsversion show-field](#drives.list.items.versionsGetFields)|GetFields|[Parameters](#Parametersdrives.list.items.versionsGetFields)|Not Found|
|[az files driveslistitemsversion update-field](#drives.list.items.versionsUpdateFields)|UpdateFields|[Parameters](#Parametersdrives.list.items.versionsUpdateFields)|Not Found|

### <a name="CommandsIngroups">Commands in `az files group` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files group create-drive](#groupsCreateDrives)|CreateDrives|[Parameters](#ParametersgroupsCreateDrives)|Not Found|
|[az files group delete-drive](#groupsDeleteDrives)|DeleteDrives|[Parameters](#ParametersgroupsDeleteDrives)|Not Found|
|[az files group delete-drive](#groupsDeleteDrive)|DeleteDrive|[Parameters](#ParametersgroupsDeleteDrive)|Not Found|
|[az files group list-drive](#groupsListDrives)|ListDrives|[Parameters](#ParametersgroupsListDrives)|Not Found|
|[az files group show-drive](#groupsGetDrives)|GetDrives|[Parameters](#ParametersgroupsGetDrives)|Not Found|
|[az files group show-drive](#groupsGetDrive)|GetDrive|[Parameters](#ParametersgroupsGetDrive)|Not Found|
|[az files group update-drive](#groupsUpdateDrives)|UpdateDrives|[Parameters](#ParametersgroupsUpdateDrives)|Not Found|
|[az files group update-drive](#groupsUpdateDrive)|UpdateDrive|[Parameters](#ParametersgroupsUpdateDrive)|Not Found|

### <a name="CommandsInshares">Commands in `az files share` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files share create-item](#sharesCreateItems)|CreateItems|[Parameters](#ParameterssharesCreateItems)|Not Found|
|[az files share delete-drive-item](#sharesDeleteDriveItem)|DeleteDriveItem|[Parameters](#ParameterssharesDeleteDriveItem)|Not Found|
|[az files share delete-item](#sharesDeleteItems)|DeleteItems|[Parameters](#ParameterssharesDeleteItems)|Not Found|
|[az files share delete-list](#sharesDeleteList)|DeleteList|[Parameters](#ParameterssharesDeleteList)|Not Found|
|[az files share delete-list-item](#sharesDeleteListItem)|DeleteListItem|[Parameters](#ParameterssharesDeleteListItem)|Not Found|
|[az files share delete-permission](#sharesDeletePermission)|DeletePermission|[Parameters](#ParameterssharesDeletePermission)|Not Found|
|[az files share delete-root](#sharesDeleteRoot)|DeleteRoot|[Parameters](#ParameterssharesDeleteRoot)|Not Found|
|[az files share delete-site](#sharesDeleteSite)|DeleteSite|[Parameters](#ParameterssharesDeleteSite)|Not Found|
|[az files share list-item](#sharesListItems)|ListItems|[Parameters](#ParameterssharesListItems)|Not Found|
|[az files share show-drive-item](#sharesGetDriveItem)|GetDriveItem|[Parameters](#ParameterssharesGetDriveItem)|Not Found|
|[az files share show-item](#sharesGetItems)|GetItems|[Parameters](#ParameterssharesGetItems)|Not Found|
|[az files share show-list](#sharesGetList)|GetList|[Parameters](#ParameterssharesGetList)|Not Found|
|[az files share show-list-item](#sharesGetListItem)|GetListItem|[Parameters](#ParameterssharesGetListItem)|Not Found|
|[az files share show-permission](#sharesGetPermission)|GetPermission|[Parameters](#ParameterssharesGetPermission)|Not Found|
|[az files share show-root](#sharesGetRoot)|GetRoot|[Parameters](#ParameterssharesGetRoot)|Not Found|
|[az files share show-site](#sharesGetSite)|GetSite|[Parameters](#ParameterssharesGetSite)|Not Found|
|[az files share update-drive-item](#sharesUpdateDriveItem)|UpdateDriveItem|[Parameters](#ParameterssharesUpdateDriveItem)|Not Found|
|[az files share update-item](#sharesUpdateItems)|UpdateItems|[Parameters](#ParameterssharesUpdateItems)|Not Found|
|[az files share update-list](#sharesUpdateList)|UpdateList|[Parameters](#ParameterssharesUpdateList)|Not Found|
|[az files share update-list-item](#sharesUpdateListItem)|UpdateListItem|[Parameters](#ParameterssharesUpdateListItem)|Not Found|
|[az files share update-permission](#sharesUpdatePermission)|UpdatePermission|[Parameters](#ParameterssharesUpdatePermission)|Not Found|
|[az files share update-root](#sharesUpdateRoot)|UpdateRoot|[Parameters](#ParameterssharesUpdateRoot)|Not Found|
|[az files share update-site](#sharesUpdateSite)|UpdateSite|[Parameters](#ParameterssharesUpdateSite)|Not Found|

### <a name="CommandsInshares.list">Commands in `az files shareslist` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files shareslist create-column](#shares.listCreateColumns)|CreateColumns|[Parameters](#Parametersshares.listCreateColumns)|Not Found|
|[az files shareslist create-content-type](#shares.listCreateContentTypes)|CreateContentTypes|[Parameters](#Parametersshares.listCreateContentTypes)|Not Found|
|[az files shareslist create-item](#shares.listCreateItems)|CreateItems|[Parameters](#Parametersshares.listCreateItems)|Not Found|
|[az files shareslist create-subscription](#shares.listCreateSubscriptions)|CreateSubscriptions|[Parameters](#Parametersshares.listCreateSubscriptions)|Not Found|
|[az files shareslist delete-column](#shares.listDeleteColumns)|DeleteColumns|[Parameters](#Parametersshares.listDeleteColumns)|Not Found|
|[az files shareslist delete-content-type](#shares.listDeleteContentTypes)|DeleteContentTypes|[Parameters](#Parametersshares.listDeleteContentTypes)|Not Found|
|[az files shareslist delete-drive](#shares.listDeleteDrive)|DeleteDrive|[Parameters](#Parametersshares.listDeleteDrive)|Not Found|
|[az files shareslist delete-item](#shares.listDeleteItems)|DeleteItems|[Parameters](#Parametersshares.listDeleteItems)|Not Found|
|[az files shareslist delete-subscription](#shares.listDeleteSubscriptions)|DeleteSubscriptions|[Parameters](#Parametersshares.listDeleteSubscriptions)|Not Found|
|[az files shareslist list-column](#shares.listListColumns)|ListColumns|[Parameters](#Parametersshares.listListColumns)|Not Found|
|[az files shareslist list-content-type](#shares.listListContentTypes)|ListContentTypes|[Parameters](#Parametersshares.listListContentTypes)|Not Found|
|[az files shareslist list-item](#shares.listListItems)|ListItems|[Parameters](#Parametersshares.listListItems)|Not Found|
|[az files shareslist list-subscription](#shares.listListSubscriptions)|ListSubscriptions|[Parameters](#Parametersshares.listListSubscriptions)|Not Found|
|[az files shareslist show-column](#shares.listGetColumns)|GetColumns|[Parameters](#Parametersshares.listGetColumns)|Not Found|
|[az files shareslist show-content-type](#shares.listGetContentTypes)|GetContentTypes|[Parameters](#Parametersshares.listGetContentTypes)|Not Found|
|[az files shareslist show-drive](#shares.listGetDrive)|GetDrive|[Parameters](#Parametersshares.listGetDrive)|Not Found|
|[az files shareslist show-item](#shares.listGetItems)|GetItems|[Parameters](#Parametersshares.listGetItems)|Not Found|
|[az files shareslist show-subscription](#shares.listGetSubscriptions)|GetSubscriptions|[Parameters](#Parametersshares.listGetSubscriptions)|Not Found|
|[az files shareslist update-column](#shares.listUpdateColumns)|UpdateColumns|[Parameters](#Parametersshares.listUpdateColumns)|Not Found|
|[az files shareslist update-content-type](#shares.listUpdateContentTypes)|UpdateContentTypes|[Parameters](#Parametersshares.listUpdateContentTypes)|Not Found|
|[az files shareslist update-drive](#shares.listUpdateDrive)|UpdateDrive|[Parameters](#Parametersshares.listUpdateDrive)|Not Found|
|[az files shareslist update-item](#shares.listUpdateItems)|UpdateItems|[Parameters](#Parametersshares.listUpdateItems)|Not Found|
|[az files shareslist update-subscription](#shares.listUpdateSubscriptions)|UpdateSubscriptions|[Parameters](#Parametersshares.listUpdateSubscriptions)|Not Found|

### <a name="CommandsInshares.list.contentTypes">Commands in `az files shareslistcontenttype` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files shareslistcontenttype create-column-link](#shares.list.contentTypesCreateColumnLinks)|CreateColumnLinks|[Parameters](#Parametersshares.list.contentTypesCreateColumnLinks)|Not Found|
|[az files shareslistcontenttype delete-column-link](#shares.list.contentTypesDeleteColumnLinks)|DeleteColumnLinks|[Parameters](#Parametersshares.list.contentTypesDeleteColumnLinks)|Not Found|
|[az files shareslistcontenttype list-column-link](#shares.list.contentTypesListColumnLinks)|ListColumnLinks|[Parameters](#Parametersshares.list.contentTypesListColumnLinks)|Not Found|
|[az files shareslistcontenttype show-column-link](#shares.list.contentTypesGetColumnLinks)|GetColumnLinks|[Parameters](#Parametersshares.list.contentTypesGetColumnLinks)|Not Found|
|[az files shareslistcontenttype update-column-link](#shares.list.contentTypesUpdateColumnLinks)|UpdateColumnLinks|[Parameters](#Parametersshares.list.contentTypesUpdateColumnLinks)|Not Found|

### <a name="CommandsInshares.list.items">Commands in `az files shareslistitem` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files shareslistitem create-version](#shares.list.itemsCreateVersions)|CreateVersions|[Parameters](#Parametersshares.list.itemsCreateVersions)|Not Found|
|[az files shareslistitem delete-drive-item](#shares.list.itemsDeleteDriveItem)|DeleteDriveItem|[Parameters](#Parametersshares.list.itemsDeleteDriveItem)|Not Found|
|[az files shareslistitem delete-field](#shares.list.itemsDeleteFields)|DeleteFields|[Parameters](#Parametersshares.list.itemsDeleteFields)|Not Found|
|[az files shareslistitem delete-ref-analytic](#shares.list.itemsDeleteRefAnalytics)|DeleteRefAnalytics|[Parameters](#Parametersshares.list.itemsDeleteRefAnalytics)|Not Found|
|[az files shareslistitem delete-version](#shares.list.itemsDeleteVersions)|DeleteVersions|[Parameters](#Parametersshares.list.itemsDeleteVersions)|Not Found|
|[az files shareslistitem list-version](#shares.list.itemsListVersions)|ListVersions|[Parameters](#Parametersshares.list.itemsListVersions)|Not Found|
|[az files shareslistitem set-ref-analytic](#shares.list.itemsSetRefAnalytics)|SetRefAnalytics|[Parameters](#Parametersshares.list.itemsSetRefAnalytics)|Not Found|
|[az files shareslistitem show-activity](#shares.list.itemsgetActivitiesByInterval-53ee)|getActivitiesByInterval-53ee|[Parameters](#Parametersshares.list.itemsgetActivitiesByInterval-53ee)|Not Found|
|[az files shareslistitem show-activity](#shares.list.itemsgetActivitiesByInterval-96b0)|getActivitiesByInterval-96b0|[Parameters](#Parametersshares.list.itemsgetActivitiesByInterval-96b0)|Not Found|
|[az files shareslistitem show-analytic](#shares.list.itemsGetAnalytics)|GetAnalytics|[Parameters](#Parametersshares.list.itemsGetAnalytics)|Not Found|
|[az files shareslistitem show-drive-item](#shares.list.itemsGetDriveItem)|GetDriveItem|[Parameters](#Parametersshares.list.itemsGetDriveItem)|Not Found|
|[az files shareslistitem show-field](#shares.list.itemsGetFields)|GetFields|[Parameters](#Parametersshares.list.itemsGetFields)|Not Found|
|[az files shareslistitem show-ref-analytic](#shares.list.itemsGetRefAnalytics)|GetRefAnalytics|[Parameters](#Parametersshares.list.itemsGetRefAnalytics)|Not Found|
|[az files shareslistitem show-version](#shares.list.itemsGetVersions)|GetVersions|[Parameters](#Parametersshares.list.itemsGetVersions)|Not Found|
|[az files shareslistitem update-drive-item](#shares.list.itemsUpdateDriveItem)|UpdateDriveItem|[Parameters](#Parametersshares.list.itemsUpdateDriveItem)|Not Found|
|[az files shareslistitem update-field](#shares.list.itemsUpdateFields)|UpdateFields|[Parameters](#Parametersshares.list.itemsUpdateFields)|Not Found|
|[az files shareslistitem update-version](#shares.list.itemsUpdateVersions)|UpdateVersions|[Parameters](#Parametersshares.list.itemsUpdateVersions)|Not Found|

### <a name="CommandsInshares.listItem">Commands in `az files shareslistitem` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files shareslistitem create-version](#shares.listItemCreateVersions)|CreateVersions|[Parameters](#Parametersshares.listItemCreateVersions)|Not Found|
|[az files shareslistitem delete-drive-item](#shares.listItemDeleteDriveItem)|DeleteDriveItem|[Parameters](#Parametersshares.listItemDeleteDriveItem)|Not Found|
|[az files shareslistitem delete-field](#shares.listItemDeleteFields)|DeleteFields|[Parameters](#Parametersshares.listItemDeleteFields)|Not Found|
|[az files shareslistitem delete-ref-analytic](#shares.listItemDeleteRefAnalytics)|DeleteRefAnalytics|[Parameters](#Parametersshares.listItemDeleteRefAnalytics)|Not Found|
|[az files shareslistitem delete-version](#shares.listItemDeleteVersions)|DeleteVersions|[Parameters](#Parametersshares.listItemDeleteVersions)|Not Found|
|[az files shareslistitem list-version](#shares.listItemListVersions)|ListVersions|[Parameters](#Parametersshares.listItemListVersions)|Not Found|
|[az files shareslistitem set-ref-analytic](#shares.listItemSetRefAnalytics)|SetRefAnalytics|[Parameters](#Parametersshares.listItemSetRefAnalytics)|Not Found|
|[az files shareslistitem show-activity](#shares.listItemgetActivitiesByInterval-53ee)|getActivitiesByInterval-53ee|[Parameters](#Parametersshares.listItemgetActivitiesByInterval-53ee)|Not Found|
|[az files shareslistitem show-activity](#shares.listItemgetActivitiesByInterval-96b0)|getActivitiesByInterval-96b0|[Parameters](#Parametersshares.listItemgetActivitiesByInterval-96b0)|Not Found|
|[az files shareslistitem show-analytic](#shares.listItemGetAnalytics)|GetAnalytics|[Parameters](#Parametersshares.listItemGetAnalytics)|Not Found|
|[az files shareslistitem show-drive-item](#shares.listItemGetDriveItem)|GetDriveItem|[Parameters](#Parametersshares.listItemGetDriveItem)|Not Found|
|[az files shareslistitem show-field](#shares.listItemGetFields)|GetFields|[Parameters](#Parametersshares.listItemGetFields)|Not Found|
|[az files shareslistitem show-ref-analytic](#shares.listItemGetRefAnalytics)|GetRefAnalytics|[Parameters](#Parametersshares.listItemGetRefAnalytics)|Not Found|
|[az files shareslistitem show-version](#shares.listItemGetVersions)|GetVersions|[Parameters](#Parametersshares.listItemGetVersions)|Not Found|
|[az files shareslistitem update-drive-item](#shares.listItemUpdateDriveItem)|UpdateDriveItem|[Parameters](#Parametersshares.listItemUpdateDriveItem)|Not Found|
|[az files shareslistitem update-field](#shares.listItemUpdateFields)|UpdateFields|[Parameters](#Parametersshares.listItemUpdateFields)|Not Found|
|[az files shareslistitem update-version](#shares.listItemUpdateVersions)|UpdateVersions|[Parameters](#Parametersshares.listItemUpdateVersions)|Not Found|

### <a name="CommandsInshares.list.items.versions">Commands in `az files shareslistitemsversion` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files shareslistitemsversion delete-field](#shares.list.items.versionsDeleteFields)|DeleteFields|[Parameters](#Parametersshares.list.items.versionsDeleteFields)|Not Found|
|[az files shareslistitemsversion restore-version](#shares.list.items.versionsrestoreVersion)|restoreVersion|[Parameters](#Parametersshares.list.items.versionsrestoreVersion)|Not Found|
|[az files shareslistitemsversion show-field](#shares.list.items.versionsGetFields)|GetFields|[Parameters](#Parametersshares.list.items.versionsGetFields)|Not Found|
|[az files shareslistitemsversion update-field](#shares.list.items.versionsUpdateFields)|UpdateFields|[Parameters](#Parametersshares.list.items.versionsUpdateFields)|Not Found|

### <a name="CommandsInshares.listItem.versions">Commands in `az files shareslistitemversion` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files shareslistitemversion delete-field](#shares.listItem.versionsDeleteFields)|DeleteFields|[Parameters](#Parametersshares.listItem.versionsDeleteFields)|Not Found|
|[az files shareslistitemversion restore-version](#shares.listItem.versionsrestoreVersion)|restoreVersion|[Parameters](#Parametersshares.listItem.versionsrestoreVersion)|Not Found|
|[az files shareslistitemversion show-field](#shares.listItem.versionsGetFields)|GetFields|[Parameters](#Parametersshares.listItem.versionsGetFields)|Not Found|
|[az files shareslistitemversion update-field](#shares.listItem.versionsUpdateFields)|UpdateFields|[Parameters](#Parametersshares.listItem.versionsUpdateFields)|Not Found|

### <a name="CommandsInshares.permission">Commands in `az files sharespermission` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files sharespermission grant](#shares.permissiongrant)|grant|[Parameters](#Parametersshares.permissiongrant)|Not Found|

### <a name="CommandsInshares.sharedDriveItem">Commands in `az files sharesshareddriveitem` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files sharesshareddriveitem create-shared-drive-item](#shares.sharedDriveItemCreateSharedDriveItem)|CreateSharedDriveItem|[Parameters](#Parametersshares.sharedDriveItemCreateSharedDriveItem)|Not Found|
|[az files sharesshareddriveitem delete-shared-drive-item](#shares.sharedDriveItemDeleteSharedDriveItem)|DeleteSharedDriveItem|[Parameters](#Parametersshares.sharedDriveItemDeleteSharedDriveItem)|Not Found|
|[az files sharesshareddriveitem list-shared-drive-item](#shares.sharedDriveItemListSharedDriveItem)|ListSharedDriveItem|[Parameters](#Parametersshares.sharedDriveItemListSharedDriveItem)|Not Found|
|[az files sharesshareddriveitem show-shared-drive-item](#shares.sharedDriveItemGetSharedDriveItem)|GetSharedDriveItem|[Parameters](#Parametersshares.sharedDriveItemGetSharedDriveItem)|Not Found|
|[az files sharesshareddriveitem update-shared-drive-item](#shares.sharedDriveItemUpdateSharedDriveItem)|UpdateSharedDriveItem|[Parameters](#Parametersshares.sharedDriveItemUpdateSharedDriveItem)|Not Found|

### <a name="CommandsInusers">Commands in `az files user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az files user create-drive](#usersCreateDrives)|CreateDrives|[Parameters](#ParametersusersCreateDrives)|Not Found|
|[az files user delete-drive](#usersDeleteDrives)|DeleteDrives|[Parameters](#ParametersusersDeleteDrives)|Not Found|
|[az files user delete-drive](#usersDeleteDrive)|DeleteDrive|[Parameters](#ParametersusersDeleteDrive)|Not Found|
|[az files user list-drive](#usersListDrives)|ListDrives|[Parameters](#ParametersusersListDrives)|Not Found|
|[az files user show-drive](#usersGetDrives)|GetDrives|[Parameters](#ParametersusersGetDrives)|Not Found|
|[az files user show-drive](#usersGetDrive)|GetDrive|[Parameters](#ParametersusersGetDrive)|Not Found|
|[az files user update-drive](#usersUpdateDrives)|UpdateDrives|[Parameters](#ParametersusersUpdateDrives)|Not Found|
|[az files user update-drive](#usersUpdateDrive)|UpdateDrive|[Parameters](#ParametersusersUpdateDrive)|Not Found|


## COMMAND DETAILS

### group `az files drive`
#### <a name="drivesCreateFollowing">Command `az files drive create-following`</a>

##### <a name="ParametersdrivesCreateFollowing">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--body**|object|New navigation property|body|body|

#### <a name="drivesCreateItems">Command `az files drive create-item`</a>

##### <a name="ParametersdrivesCreateItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--body**|object|New navigation property|body|body|

#### <a name="drivesCreateSpecial">Command `az files drive create-special`</a>

##### <a name="ParametersdrivesCreateSpecial">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--body**|object|New navigation property|body|body|

#### <a name="drivesDeleteFollowing">Command `az files drive delete-following`</a>

##### <a name="ParametersdrivesDeleteFollowing">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drivesDeleteItems">Command `az files drive delete-item`</a>

##### <a name="ParametersdrivesDeleteItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drivesDeleteList">Command `az files drive delete-list`</a>

##### <a name="ParametersdrivesDeleteList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drivesDeleteRoot">Command `az files drive delete-root`</a>

##### <a name="ParametersdrivesDeleteRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drivesDeleteSpecial">Command `az files drive delete-special`</a>

##### <a name="ParametersdrivesDeleteSpecial">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drivesListFollowing">Command `az files drive list-following`</a>

##### <a name="ParametersdrivesListFollowing">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drivesListItems">Command `az files drive list-item`</a>

##### <a name="ParametersdrivesListItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drivesListSpecial">Command `az files drive list-special`</a>

##### <a name="ParametersdrivesListSpecial">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drivesrecent">Command `az files drive recent`</a>

##### <a name="Parametersdrivesrecent">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|

#### <a name="drivessearch">Command `az files drive search`</a>

##### <a name="Parametersdrivessearch">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--q**|string||q|q|

#### <a name="drivessharedWithMe">Command `az files drive shared-with-me`</a>

##### <a name="ParametersdrivessharedWithMe">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|

#### <a name="drivesGetFollowing">Command `az files drive show-following`</a>

##### <a name="ParametersdrivesGetFollowing">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drivesGetItems">Command `az files drive show-item`</a>

##### <a name="ParametersdrivesGetItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drivesGetList">Command `az files drive show-list`</a>

##### <a name="ParametersdrivesGetList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drivesGetRoot">Command `az files drive show-root`</a>

##### <a name="ParametersdrivesGetRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drivesGetSpecial">Command `az files drive show-special`</a>

##### <a name="ParametersdrivesGetSpecial">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drivesUpdateFollowing">Command `az files drive update-following`</a>

##### <a name="ParametersdrivesUpdateFollowing">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="drivesUpdateItems">Command `az files drive update-item`</a>

##### <a name="ParametersdrivesUpdateItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="drivesUpdateList">Command `az files drive update-list`</a>

##### <a name="ParametersdrivesUpdateList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--microsoft-graph-item-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string|The displayable title of the list.|display_name|displayName|
|**--list**|object|listInfo|list|list|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--system**|dictionary|systemFacet|system|system|
|**--columns**|array|The collection of field definitions for this list.|columns|columns|
|**--content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--items**|array|All items contained in the list.|items|items|
|**--subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|

#### <a name="drivesUpdateRoot">Command `az files drive update-root`</a>

##### <a name="ParametersdrivesUpdateRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="drivesUpdateSpecial">Command `az files drive update-special`</a>

##### <a name="ParametersdrivesUpdateSpecial">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--body**|object|New navigation property values|body|body|

### group `az files drivesdrive`
#### <a name="drives.driveCreateDrive">Command `az files drivesdrive create-drive`</a>

##### <a name="Parametersdrives.driveCreateDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--microsoft-graph-drive-type**|string|Describes the type of drive represented by this resource. OneDrive personal drives will return personal. OneDrive for Business will return business. SharePoint document libraries will return documentLibrary. Read-only.|microsoft_graph_drive_type|driveType|
|**--share-point-ids**|object|sharepointIds|share_point_ids|sharePointIds|
|**--system**|dictionary|systemFacet|system|system|
|**--following**|array|The list of items the user is following. Only in OneDrive for Business.|following|following|
|**--items**|array|All items contained in the drive. Read-only. Nullable.|items|items|
|**--root**|object|driveItem|root|root|
|**--special**|array|Collection of common folders available in OneDrive. Read-only. Nullable.|special|special|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-base-item-created-date-time-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--microsoft-graph-base-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--microsoft-graph-base-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--microsoft-graph-base-item-last-modified-date-time-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-base-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--microsoft-graph-base-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--microsoft-graph-user-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--microsoft-graph-user-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--microsoft-graph-item-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--microsoft-graph-item-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--id1**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--name1**|string|The name of the item being referenced. Read-only.|name1|name|
|**--microsoft-graph-item-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--microsoft-graph-item-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--microsoft-graph-item-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--display-name**|string|The displayable title of the list.|display_name|displayName|
|**--list**|object|listInfo|list|list|
|**--sharepoint-ids1**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--microsoft-graph-system-facet-system**|dictionary|systemFacet|microsoft_graph_system_facet_system|system|
|**--columns**|array|The collection of field definitions for this list.|columns|columns|
|**--content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--microsoft-graph-list-items**|array|All items contained in the list.|microsoft_graph_list_items|items|
|**--subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|
|**--deleted**|integer|Total space consumed by files in the recycle bin, in bytes. Read-only.|deleted|deleted|
|**--remaining**|integer|Total space remaining before reaching the quota limit, in bytes. Read-only.|remaining|remaining|
|**--state**|string|Enumeration value that indicates the state of the storage space. Read-only.|state|state|
|**--storage-plan-information**|object|storagePlanInformation|storage_plan_information|storagePlanInformation|
|**--total**|integer|Total allowed storage space, in bytes. Read-only.|total|total|
|**--used**|integer|Total space used, in bytes. Read-only.|used|used|
|**--application3**|object|identity|application3|application|
|**--device3**|object|identity|device3|device|
|**--user3**|object|identity|user3|user|

#### <a name="drives.driveDeleteDrive">Command `az files drivesdrive delete-drive`</a>

##### <a name="Parametersdrives.driveDeleteDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drives.driveListDrive">Command `az files drivesdrive list-drive`</a>

##### <a name="Parametersdrives.driveListDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.driveGetDrive">Command `az files drivesdrive show-drive`</a>

##### <a name="Parametersdrives.driveGetDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.driveUpdateDrive">Command `az files drivesdrive update-drive`</a>

##### <a name="Parametersdrives.driveUpdateDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--microsoft-graph-item-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--microsoft-graph-drive-type**|string|Describes the type of drive represented by this resource. OneDrive personal drives will return personal. OneDrive for Business will return business. SharePoint document libraries will return documentLibrary. Read-only.|microsoft_graph_drive_type|driveType|
|**--share-point-ids**|object|sharepointIds|share_point_ids|sharePointIds|
|**--system**|dictionary|systemFacet|system|system|
|**--following**|array|The list of items the user is following. Only in OneDrive for Business.|following|following|
|**--items**|array|All items contained in the drive. Read-only. Nullable.|items|items|
|**--root**|object|driveItem|root|root|
|**--special**|array|Collection of common folders available in OneDrive. Read-only. Nullable.|special|special|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-base-item-created-date-time-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--microsoft-graph-base-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--microsoft-graph-base-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--microsoft-graph-base-item-last-modified-date-time-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-base-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--microsoft-graph-base-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--microsoft-graph-user-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--microsoft-graph-user-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--drive-id1**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id1|driveId|
|**--microsoft-graph-item-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--id1**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--name1**|string|The name of the item being referenced. Read-only.|name1|name|
|**--microsoft-graph-item-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--microsoft-graph-item-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--microsoft-graph-item-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--display-name**|string|The displayable title of the list.|display_name|displayName|
|**--list**|object|listInfo|list|list|
|**--sharepoint-ids1**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--microsoft-graph-system-facet-system**|dictionary|systemFacet|microsoft_graph_system_facet_system|system|
|**--columns**|array|The collection of field definitions for this list.|columns|columns|
|**--content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--microsoft-graph-list-items**|array|All items contained in the list.|microsoft_graph_list_items|items|
|**--subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|
|**--deleted**|integer|Total space consumed by files in the recycle bin, in bytes. Read-only.|deleted|deleted|
|**--remaining**|integer|Total space remaining before reaching the quota limit, in bytes. Read-only.|remaining|remaining|
|**--state**|string|Enumeration value that indicates the state of the storage space. Read-only.|state|state|
|**--storage-plan-information**|object|storagePlanInformation|storage_plan_information|storagePlanInformation|
|**--total**|integer|Total allowed storage space, in bytes. Read-only.|total|total|
|**--used**|integer|Total space used, in bytes. Read-only.|used|used|
|**--application3**|object|identity|application3|application|
|**--device3**|object|identity|device3|device|
|**--user3**|object|identity|user3|user|

### group `az files driveslist`
#### <a name="drives.listCreateColumns">Command `az files driveslist create-column`</a>

##### <a name="Parametersdrives.listCreateColumns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--id**|string|Read-only.|id|id|
|**--boolean**|dictionary|booleanColumn|boolean|boolean|
|**--calculated**|object|calculatedColumn|calculated|calculated|
|**--choice**|object|choiceColumn|choice|choice|
|**--column-group**|string|For site columns, the name of the group this column belongs to. Helps organize related columns.|column_group|columnGroup|
|**--date-time**|object|dateTimeColumn|date_time|dateTime|
|**--default-value**|object|defaultColumnValue|default_value|defaultValue|
|**--description**|string|The user-facing description of the column.|description|description|
|**--display-name**|string|The user-facing name of the column.|display_name|displayName|
|**--enforce-unique-values**|boolean|If true, no two list items may have the same value for this column.|enforce_unique_values|enforceUniqueValues|
|**--geolocation**|dictionary|geolocationColumn|geolocation|geolocation|
|**--hidden**|boolean|Specifies whether the column is displayed in the user interface.|hidden|hidden|
|**--indexed**|boolean|Specifies whether the column values can used for sorting and searching.|indexed|indexed|
|**--lookup**|object|lookupColumn|lookup|lookup|
|**--name**|string|The API-facing name of the column as it appears in the [fields][] on a [listItem][]. For the user-facing name, see displayName.|name|name|
|**--number**|object|numberColumn|number|number|
|**--person-or-group**|object|personOrGroupColumn|person_or_group|personOrGroup|
|**--read-only**|boolean|Specifies whether the column values can be modified.|read_only|readOnly|
|**--required**|boolean|Specifies whether the column value is not optional.|required|required|
|**--text**|object|textColumn|text|text|
|**--locale**|string|Specifies the locale from which to infer the currency symbol.|locale|locale|

#### <a name="drives.listCreateContentTypes">Command `az files driveslist create-content-type`</a>

##### <a name="Parametersdrives.listCreateContentTypes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string|The descriptive text for the item.|description|description|
|**--group**|string|The name of the group this content type belongs to. Helps organize related content types.|group|group|
|**--hidden**|boolean|Indicates whether the content type is hidden in the list's 'New' menu.|hidden|hidden|
|**--name**|string|The name of the content type.|name|name|
|**--order**|object|contentTypeOrder|order|order|
|**--parent-id**|string|The unique identifier of the content type.|parent_id|parentId|
|**--read-only**|boolean|If true, the content type cannot be modified unless this value is first set to false.|read_only|readOnly|
|**--sealed**|boolean|If true, the content type cannot be modified by users or through push-down operations. Only site collection administrators can seal or unseal content types.|sealed|sealed|
|**--column-links**|array|The collection of columns that are required by this content type|column_links|columnLinks|
|**--microsoft-graph-item-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|

#### <a name="drives.listCreateItems">Command `az files driveslist create-item`</a>

##### <a name="Parametersdrives.listCreateItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--microsoft-graph-item-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--content-type**|object|contentTypeInfo|content_type|contentType|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|

#### <a name="drives.listCreateSubscriptions">Command `az files driveslist create-subscription`</a>

##### <a name="Parametersdrives.listCreateSubscriptions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--id**|string|Read-only.|id|id|
|**--application-id**|string|Identifier of the application used to create the subscription. Read-only.|application_id|applicationId|
|**--change-type**|string|Required. Indicates the type of change in the subscribed resource that will raise a change notification. The supported values are: created, updated, deleted. Multiple values can be combined using a comma-separated list.Note: Drive root item and list change notifications support only the updated changeType. User and group change notifications support updated and deleted changeType.|change_type|changeType|
|**--client-state**|string|Optional. Specifies the value of the clientState property sent by the service in each change notification. The maximum length is 128 characters. The client can check that the change notification came from the service by comparing the value of the clientState property sent with the subscription with the value of the clientState property received with each change notification.|client_state|clientState|
|**--creator-id**|string|Identifier of the user or service principal that created the subscription. If the app used delegated permissions to create the subscription, this field contains the id of the signed-in user the app called on behalf of. If the app used application permissions, this field contains the id of the service principal corresponding to the app. Read-only.|creator_id|creatorId|
|**--encryption-certificate**|string|A base64-encoded representation of a certificate with a public key used to encrypt resource data in change notifications. Optional. Required when includeResourceData is true.|encryption_certificate|encryptionCertificate|
|**--encryption-certificate-id**|string|A custom app-provided identifier to help identify the certificate needed to decrypt resource data. Optional.|encryption_certificate_id|encryptionCertificateId|
|**--expiration-date-time**|date-time|Required. Specifies the date and time when the webhook subscription expires. The time is in UTC, and can be an amount of time from subscription creation that varies for the resource subscribed to.  See the table below for maximum supported subscription length of time.|expiration_date_time|expirationDateTime|
|**--include-resource-data**|boolean|When set to true, change notifications include resource data (such as content of a chat message). Optional.|include_resource_data|includeResourceData|
|**--latest-supported-tls-version**|string||latest_supported_tls_version|latestSupportedTlsVersion|
|**--lifecycle-notification-url**|string||lifecycle_notification_url|lifecycleNotificationUrl|
|**--notification-url**|string|Required. The URL of the endpoint that will receive the change notifications. This URL must make use of the HTTPS protocol.|notification_url|notificationUrl|
|**--resource**|string|Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.|resource|resource|

#### <a name="drives.listDeleteColumns">Command `az files driveslist delete-column`</a>

##### <a name="Parametersdrives.listDeleteColumns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--column-definition-id**|string|key: id of columnDefinition|column_definition_id|columnDefinition-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drives.listDeleteContentTypes">Command `az files driveslist delete-content-type`</a>

##### <a name="Parametersdrives.listDeleteContentTypes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drives.listDeleteDrive">Command `az files driveslist delete-drive`</a>

##### <a name="Parametersdrives.listDeleteDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drives.listDeleteItems">Command `az files driveslist delete-item`</a>

##### <a name="Parametersdrives.listDeleteItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drives.listDeleteSubscriptions">Command `az files driveslist delete-subscription`</a>

##### <a name="Parametersdrives.listDeleteSubscriptions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--subscription-id**|string|key: id of subscription|subscription_id|subscription-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drives.listListColumns">Command `az files driveslist list-column`</a>

##### <a name="Parametersdrives.listListColumns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.listListContentTypes">Command `az files driveslist list-content-type`</a>

##### <a name="Parametersdrives.listListContentTypes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.listListItems">Command `az files driveslist list-item`</a>

##### <a name="Parametersdrives.listListItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.listListSubscriptions">Command `az files driveslist list-subscription`</a>

##### <a name="Parametersdrives.listListSubscriptions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.listGetColumns">Command `az files driveslist show-column`</a>

##### <a name="Parametersdrives.listGetColumns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--column-definition-id**|string|key: id of columnDefinition|column_definition_id|columnDefinition-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.listGetContentTypes">Command `az files driveslist show-content-type`</a>

##### <a name="Parametersdrives.listGetContentTypes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.listGetDrive">Command `az files driveslist show-drive`</a>

##### <a name="Parametersdrives.listGetDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.listGetItems">Command `az files driveslist show-item`</a>

##### <a name="Parametersdrives.listGetItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.listGetSubscriptions">Command `az files driveslist show-subscription`</a>

##### <a name="Parametersdrives.listGetSubscriptions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--subscription-id**|string|key: id of subscription|subscription_id|subscription-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.listUpdateColumns">Command `az files driveslist update-column`</a>

##### <a name="Parametersdrives.listUpdateColumns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--column-definition-id**|string|key: id of columnDefinition|column_definition_id|columnDefinition-id|
|**--id**|string|Read-only.|id|id|
|**--boolean**|dictionary|booleanColumn|boolean|boolean|
|**--calculated**|object|calculatedColumn|calculated|calculated|
|**--choice**|object|choiceColumn|choice|choice|
|**--column-group**|string|For site columns, the name of the group this column belongs to. Helps organize related columns.|column_group|columnGroup|
|**--date-time**|object|dateTimeColumn|date_time|dateTime|
|**--default-value**|object|defaultColumnValue|default_value|defaultValue|
|**--description**|string|The user-facing description of the column.|description|description|
|**--display-name**|string|The user-facing name of the column.|display_name|displayName|
|**--enforce-unique-values**|boolean|If true, no two list items may have the same value for this column.|enforce_unique_values|enforceUniqueValues|
|**--geolocation**|dictionary|geolocationColumn|geolocation|geolocation|
|**--hidden**|boolean|Specifies whether the column is displayed in the user interface.|hidden|hidden|
|**--indexed**|boolean|Specifies whether the column values can used for sorting and searching.|indexed|indexed|
|**--lookup**|object|lookupColumn|lookup|lookup|
|**--name**|string|The API-facing name of the column as it appears in the [fields][] on a [listItem][]. For the user-facing name, see displayName.|name|name|
|**--number**|object|numberColumn|number|number|
|**--person-or-group**|object|personOrGroupColumn|person_or_group|personOrGroup|
|**--read-only**|boolean|Specifies whether the column values can be modified.|read_only|readOnly|
|**--required**|boolean|Specifies whether the column value is not optional.|required|required|
|**--text**|object|textColumn|text|text|
|**--locale**|string|Specifies the locale from which to infer the currency symbol.|locale|locale|

#### <a name="drives.listUpdateContentTypes">Command `az files driveslist update-content-type`</a>

##### <a name="Parametersdrives.listUpdateContentTypes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string|The descriptive text for the item.|description|description|
|**--group**|string|The name of the group this content type belongs to. Helps organize related content types.|group|group|
|**--hidden**|boolean|Indicates whether the content type is hidden in the list's 'New' menu.|hidden|hidden|
|**--name**|string|The name of the content type.|name|name|
|**--order**|object|contentTypeOrder|order|order|
|**--parent-id**|string|The unique identifier of the content type.|parent_id|parentId|
|**--read-only**|boolean|If true, the content type cannot be modified unless this value is first set to false.|read_only|readOnly|
|**--sealed**|boolean|If true, the content type cannot be modified by users or through push-down operations. Only site collection administrators can seal or unseal content types.|sealed|sealed|
|**--column-links**|array|The collection of columns that are required by this content type|column_links|columnLinks|
|**--microsoft-graph-item-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|

#### <a name="drives.listUpdateDrive">Command `az files driveslist update-drive`</a>

##### <a name="Parametersdrives.listUpdateDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--microsoft-graph-item-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--microsoft-graph-drive-type**|string|Describes the type of drive represented by this resource. OneDrive personal drives will return personal. OneDrive for Business will return business. SharePoint document libraries will return documentLibrary. Read-only.|microsoft_graph_drive_type|driveType|
|**--share-point-ids**|object|sharepointIds|share_point_ids|sharePointIds|
|**--system**|dictionary|systemFacet|system|system|
|**--following**|array|The list of items the user is following. Only in OneDrive for Business.|following|following|
|**--items**|array|All items contained in the drive. Read-only. Nullable.|items|items|
|**--root**|object|driveItem|root|root|
|**--special**|array|Collection of common folders available in OneDrive. Read-only. Nullable.|special|special|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-base-item-created-date-time-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--microsoft-graph-base-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--microsoft-graph-base-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--microsoft-graph-base-item-last-modified-date-time-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-base-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--microsoft-graph-base-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--microsoft-graph-user-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--microsoft-graph-user-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--drive-id1**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id1|driveId|
|**--microsoft-graph-item-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--id1**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--name1**|string|The name of the item being referenced. Read-only.|name1|name|
|**--microsoft-graph-item-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--microsoft-graph-item-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--microsoft-graph-item-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--display-name**|string|The displayable title of the list.|display_name|displayName|
|**--list**|object|listInfo|list|list|
|**--sharepoint-ids1**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--microsoft-graph-system-facet-system**|dictionary|systemFacet|microsoft_graph_system_facet_system|system|
|**--columns**|array|The collection of field definitions for this list.|columns|columns|
|**--content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--microsoft-graph-list-items**|array|All items contained in the list.|microsoft_graph_list_items|items|
|**--subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|
|**--deleted**|integer|Total space consumed by files in the recycle bin, in bytes. Read-only.|deleted|deleted|
|**--remaining**|integer|Total space remaining before reaching the quota limit, in bytes. Read-only.|remaining|remaining|
|**--state**|string|Enumeration value that indicates the state of the storage space. Read-only.|state|state|
|**--storage-plan-information**|object|storagePlanInformation|storage_plan_information|storagePlanInformation|
|**--total**|integer|Total allowed storage space, in bytes. Read-only.|total|total|
|**--used**|integer|Total space used, in bytes. Read-only.|used|used|
|**--application3**|object|identity|application3|application|
|**--device3**|object|identity|device3|device|
|**--user3**|object|identity|user3|user|

#### <a name="drives.listUpdateItems">Command `az files driveslist update-item`</a>

##### <a name="Parametersdrives.listUpdateItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--microsoft-graph-item-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--content-type**|object|contentTypeInfo|content_type|contentType|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|

#### <a name="drives.listUpdateSubscriptions">Command `az files driveslist update-subscription`</a>

##### <a name="Parametersdrives.listUpdateSubscriptions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--subscription-id**|string|key: id of subscription|subscription_id|subscription-id|
|**--id**|string|Read-only.|id|id|
|**--application-id**|string|Identifier of the application used to create the subscription. Read-only.|application_id|applicationId|
|**--change-type**|string|Required. Indicates the type of change in the subscribed resource that will raise a change notification. The supported values are: created, updated, deleted. Multiple values can be combined using a comma-separated list.Note: Drive root item and list change notifications support only the updated changeType. User and group change notifications support updated and deleted changeType.|change_type|changeType|
|**--client-state**|string|Optional. Specifies the value of the clientState property sent by the service in each change notification. The maximum length is 128 characters. The client can check that the change notification came from the service by comparing the value of the clientState property sent with the subscription with the value of the clientState property received with each change notification.|client_state|clientState|
|**--creator-id**|string|Identifier of the user or service principal that created the subscription. If the app used delegated permissions to create the subscription, this field contains the id of the signed-in user the app called on behalf of. If the app used application permissions, this field contains the id of the service principal corresponding to the app. Read-only.|creator_id|creatorId|
|**--encryption-certificate**|string|A base64-encoded representation of a certificate with a public key used to encrypt resource data in change notifications. Optional. Required when includeResourceData is true.|encryption_certificate|encryptionCertificate|
|**--encryption-certificate-id**|string|A custom app-provided identifier to help identify the certificate needed to decrypt resource data. Optional.|encryption_certificate_id|encryptionCertificateId|
|**--expiration-date-time**|date-time|Required. Specifies the date and time when the webhook subscription expires. The time is in UTC, and can be an amount of time from subscription creation that varies for the resource subscribed to.  See the table below for maximum supported subscription length of time.|expiration_date_time|expirationDateTime|
|**--include-resource-data**|boolean|When set to true, change notifications include resource data (such as content of a chat message). Optional.|include_resource_data|includeResourceData|
|**--latest-supported-tls-version**|string||latest_supported_tls_version|latestSupportedTlsVersion|
|**--lifecycle-notification-url**|string||lifecycle_notification_url|lifecycleNotificationUrl|
|**--notification-url**|string|Required. The URL of the endpoint that will receive the change notifications. This URL must make use of the HTTPS protocol.|notification_url|notificationUrl|
|**--resource**|string|Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.|resource|resource|

### group `az files driveslistcontenttype`
#### <a name="drives.list.contentTypesCreateColumnLinks">Command `az files driveslistcontenttype create-column-link`</a>

##### <a name="Parametersdrives.list.contentTypesCreateColumnLinks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|The name of the column  in this content type.|name|name|

#### <a name="drives.list.contentTypesDeleteColumnLinks">Command `az files driveslistcontenttype delete-column-link`</a>

##### <a name="Parametersdrives.list.contentTypesDeleteColumnLinks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: id of columnLink|column_link_id|columnLink-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drives.list.contentTypesListColumnLinks">Command `az files driveslistcontenttype list-column-link`</a>

##### <a name="Parametersdrives.list.contentTypesListColumnLinks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.list.contentTypesGetColumnLinks">Command `az files driveslistcontenttype show-column-link`</a>

##### <a name="Parametersdrives.list.contentTypesGetColumnLinks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: id of columnLink|column_link_id|columnLink-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.list.contentTypesUpdateColumnLinks">Command `az files driveslistcontenttype update-column-link`</a>

##### <a name="Parametersdrives.list.contentTypesUpdateColumnLinks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: id of columnLink|column_link_id|columnLink-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|The name of the column  in this content type.|name|name|

### group `az files driveslistitem`
#### <a name="drives.list.itemsCreateVersions">Command `az files driveslistitem create-version`</a>

##### <a name="Parametersdrives.list.itemsCreateVersions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|

#### <a name="drives.list.itemsDeleteDriveItem">Command `az files driveslistitem delete-drive-item`</a>

##### <a name="Parametersdrives.list.itemsDeleteDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drives.list.itemsDeleteFields">Command `az files driveslistitem delete-field`</a>

##### <a name="Parametersdrives.list.itemsDeleteFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drives.list.itemsDeleteRefAnalytics">Command `az files driveslistitem delete-ref-analytic`</a>

##### <a name="Parametersdrives.list.itemsDeleteRefAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drives.list.itemsDeleteVersions">Command `az files driveslistitem delete-version`</a>

##### <a name="Parametersdrives.list.itemsDeleteVersions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drives.list.itemsListVersions">Command `az files driveslistitem list-version`</a>

##### <a name="Parametersdrives.list.itemsListVersions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.list.itemsSetRefAnalytics">Command `az files driveslistitem set-ref-analytic`</a>

##### <a name="Parametersdrives.list.itemsSetRefAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="drives.list.itemsgetActivitiesByInterval-53ee">Command `az files driveslistitem show-activity`</a>

##### <a name="Parametersdrives.list.itemsgetActivitiesByInterval-53ee">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--start-date-time**|string||start_date_time|startDateTime|
|**--end-date-time**|string||end_date_time|endDateTime|
|**--interval**|string||interval|interval|

#### <a name="drives.list.itemsgetActivitiesByInterval-96b0">Command `az files driveslistitem show-activity`</a>

##### <a name="Parametersdrives.list.itemsgetActivitiesByInterval-96b0">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="drives.list.itemsGetAnalytics">Command `az files driveslistitem show-analytic`</a>

##### <a name="Parametersdrives.list.itemsGetAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.list.itemsGetDriveItem">Command `az files driveslistitem show-drive-item`</a>

##### <a name="Parametersdrives.list.itemsGetDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.list.itemsGetFields">Command `az files driveslistitem show-field`</a>

##### <a name="Parametersdrives.list.itemsGetFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.list.itemsGetRefAnalytics">Command `az files driveslistitem show-ref-analytic`</a>

##### <a name="Parametersdrives.list.itemsGetRefAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|

#### <a name="drives.list.itemsGetVersions">Command `az files driveslistitem show-version`</a>

##### <a name="Parametersdrives.list.itemsGetVersions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.list.itemsUpdateDriveItem">Command `az files driveslistitem update-drive-item`</a>

##### <a name="Parametersdrives.list.itemsUpdateDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="drives.list.itemsUpdateFields">Command `az files driveslistitem update-field`</a>

##### <a name="Parametersdrives.list.itemsUpdateFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--id**|string|Read-only.|id|id|

#### <a name="drives.list.itemsUpdateVersions">Command `az files driveslistitem update-version`</a>

##### <a name="Parametersdrives.list.itemsUpdateVersions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|

### group `az files driveslistitemsversion`
#### <a name="drives.list.items.versionsDeleteFields">Command `az files driveslistitemsversion delete-field`</a>

##### <a name="Parametersdrives.list.items.versionsDeleteFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="drives.list.items.versionsrestoreVersion">Command `az files driveslistitemsversion restore-version`</a>

##### <a name="Parametersdrives.list.items.versionsrestoreVersion">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|

#### <a name="drives.list.items.versionsGetFields">Command `az files driveslistitemsversion show-field`</a>

##### <a name="Parametersdrives.list.items.versionsGetFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="drives.list.items.versionsUpdateFields">Command `az files driveslistitemsversion update-field`</a>

##### <a name="Parametersdrives.list.items.versionsUpdateFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|

### group `az files group`
#### <a name="groupsCreateDrives">Command `az files group create-drive`</a>

##### <a name="ParametersgroupsCreateDrives">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--microsoft-graph-drive-type**|string|Describes the type of drive represented by this resource. OneDrive personal drives will return personal. OneDrive for Business will return business. SharePoint document libraries will return documentLibrary. Read-only.|microsoft_graph_drive_type|driveType|
|**--share-point-ids**|object|sharepointIds|share_point_ids|sharePointIds|
|**--system**|dictionary|systemFacet|system|system|
|**--following**|array|The list of items the user is following. Only in OneDrive for Business.|following|following|
|**--items**|array|All items contained in the drive. Read-only. Nullable.|items|items|
|**--root**|object|driveItem|root|root|
|**--special**|array|Collection of common folders available in OneDrive. Read-only. Nullable.|special|special|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-base-item-created-date-time-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--microsoft-graph-base-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--microsoft-graph-base-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--microsoft-graph-base-item-last-modified-date-time-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-base-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--microsoft-graph-base-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--microsoft-graph-user-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--microsoft-graph-user-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--microsoft-graph-item-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--microsoft-graph-item-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--id1**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--name1**|string|The name of the item being referenced. Read-only.|name1|name|
|**--microsoft-graph-item-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--microsoft-graph-item-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--microsoft-graph-item-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--display-name**|string|The displayable title of the list.|display_name|displayName|
|**--list**|object|listInfo|list|list|
|**--sharepoint-ids1**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--microsoft-graph-system-facet-system**|dictionary|systemFacet|microsoft_graph_system_facet_system|system|
|**--columns**|array|The collection of field definitions for this list.|columns|columns|
|**--content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--microsoft-graph-list-items**|array|All items contained in the list.|microsoft_graph_list_items|items|
|**--subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|
|**--deleted**|integer|Total space consumed by files in the recycle bin, in bytes. Read-only.|deleted|deleted|
|**--remaining**|integer|Total space remaining before reaching the quota limit, in bytes. Read-only.|remaining|remaining|
|**--state**|string|Enumeration value that indicates the state of the storage space. Read-only.|state|state|
|**--storage-plan-information**|object|storagePlanInformation|storage_plan_information|storagePlanInformation|
|**--total**|integer|Total allowed storage space, in bytes. Read-only.|total|total|
|**--used**|integer|Total space used, in bytes. Read-only.|used|used|
|**--application3**|object|identity|application3|application|
|**--device3**|object|identity|device3|device|
|**--user3**|object|identity|user3|user|

#### <a name="groupsDeleteDrives">Command `az files group delete-drive`</a>

##### <a name="ParametersgroupsDeleteDrives">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupsDeleteDrive">Command `az files group delete-drive`</a>

##### <a name="ParametersgroupsDeleteDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="groupsListDrives">Command `az files group list-drive`</a>

##### <a name="ParametersgroupsListDrives">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsGetDrives">Command `az files group show-drive`</a>

##### <a name="ParametersgroupsGetDrives">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsGetDrive">Command `az files group show-drive`</a>

##### <a name="ParametersgroupsGetDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="groupsUpdateDrives">Command `az files group update-drive`</a>

##### <a name="ParametersgroupsUpdateDrives">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--microsoft-graph-item-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--microsoft-graph-drive-type**|string|Describes the type of drive represented by this resource. OneDrive personal drives will return personal. OneDrive for Business will return business. SharePoint document libraries will return documentLibrary. Read-only.|microsoft_graph_drive_type|driveType|
|**--share-point-ids**|object|sharepointIds|share_point_ids|sharePointIds|
|**--system**|dictionary|systemFacet|system|system|
|**--following**|array|The list of items the user is following. Only in OneDrive for Business.|following|following|
|**--items**|array|All items contained in the drive. Read-only. Nullable.|items|items|
|**--root**|object|driveItem|root|root|
|**--special**|array|Collection of common folders available in OneDrive. Read-only. Nullable.|special|special|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-base-item-created-date-time-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--microsoft-graph-base-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--microsoft-graph-base-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--microsoft-graph-base-item-last-modified-date-time-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-base-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--microsoft-graph-base-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--microsoft-graph-user-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--microsoft-graph-user-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--drive-id1**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id1|driveId|
|**--microsoft-graph-item-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--id1**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--name1**|string|The name of the item being referenced. Read-only.|name1|name|
|**--microsoft-graph-item-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--microsoft-graph-item-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--microsoft-graph-item-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--display-name**|string|The displayable title of the list.|display_name|displayName|
|**--list**|object|listInfo|list|list|
|**--sharepoint-ids1**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--microsoft-graph-system-facet-system**|dictionary|systemFacet|microsoft_graph_system_facet_system|system|
|**--columns**|array|The collection of field definitions for this list.|columns|columns|
|**--content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--microsoft-graph-list-items**|array|All items contained in the list.|microsoft_graph_list_items|items|
|**--subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|
|**--deleted**|integer|Total space consumed by files in the recycle bin, in bytes. Read-only.|deleted|deleted|
|**--remaining**|integer|Total space remaining before reaching the quota limit, in bytes. Read-only.|remaining|remaining|
|**--state**|string|Enumeration value that indicates the state of the storage space. Read-only.|state|state|
|**--storage-plan-information**|object|storagePlanInformation|storage_plan_information|storagePlanInformation|
|**--total**|integer|Total allowed storage space, in bytes. Read-only.|total|total|
|**--used**|integer|Total space used, in bytes. Read-only.|used|used|
|**--application3**|object|identity|application3|application|
|**--device3**|object|identity|device3|device|
|**--user3**|object|identity|user3|user|

#### <a name="groupsUpdateDrive">Command `az files group update-drive`</a>

##### <a name="ParametersgroupsUpdateDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|

### group `az files share`
#### <a name="sharesCreateItems">Command `az files share create-item`</a>

##### <a name="ParameterssharesCreateItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--body**|object|New navigation property|body|body|

#### <a name="sharesDeleteDriveItem">Command `az files share delete-drive-item`</a>

##### <a name="ParameterssharesDeleteDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="sharesDeleteItems">Command `az files share delete-item`</a>

##### <a name="ParameterssharesDeleteItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="sharesDeleteList">Command `az files share delete-list`</a>

##### <a name="ParameterssharesDeleteList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="sharesDeleteListItem">Command `az files share delete-list-item`</a>

##### <a name="ParameterssharesDeleteListItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="sharesDeletePermission">Command `az files share delete-permission`</a>

##### <a name="ParameterssharesDeletePermission">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="sharesDeleteRoot">Command `az files share delete-root`</a>

##### <a name="ParameterssharesDeleteRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="sharesDeleteSite">Command `az files share delete-site`</a>

##### <a name="ParameterssharesDeleteSite">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="sharesListItems">Command `az files share list-item`</a>

##### <a name="ParameterssharesListItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="sharesGetDriveItem">Command `az files share show-drive-item`</a>

##### <a name="ParameterssharesGetDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="sharesGetItems">Command `az files share show-item`</a>

##### <a name="ParameterssharesGetItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="sharesGetList">Command `az files share show-list`</a>

##### <a name="ParameterssharesGetList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="sharesGetListItem">Command `az files share show-list-item`</a>

##### <a name="ParameterssharesGetListItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="sharesGetPermission">Command `az files share show-permission`</a>

##### <a name="ParameterssharesGetPermission">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="sharesGetRoot">Command `az files share show-root`</a>

##### <a name="ParameterssharesGetRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="sharesGetSite">Command `az files share show-site`</a>

##### <a name="ParameterssharesGetSite">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="sharesUpdateDriveItem">Command `az files share update-drive-item`</a>

##### <a name="ParameterssharesUpdateDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="sharesUpdateItems">Command `az files share update-item`</a>

##### <a name="ParameterssharesUpdateItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--drive-item-id**|string|key: id of driveItem|drive_item_id|driveItem-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="sharesUpdateList">Command `az files share update-list`</a>

##### <a name="ParameterssharesUpdateList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string|The displayable title of the list.|display_name|displayName|
|**--list**|object|listInfo|list|list|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--system**|dictionary|systemFacet|system|system|
|**--columns**|array|The collection of field definitions for this list.|columns|columns|
|**--content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--items**|array|All items contained in the list.|items|items|
|**--subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|

#### <a name="sharesUpdateListItem">Command `az files share update-list-item`</a>

##### <a name="ParameterssharesUpdateListItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--content-type**|object|contentTypeInfo|content_type|contentType|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|

#### <a name="sharesUpdatePermission">Command `az files share update-permission`</a>

##### <a name="ParameterssharesUpdatePermission">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="sharesUpdateRoot">Command `az files share update-root`</a>

##### <a name="ParameterssharesUpdateRoot">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="sharesUpdateSite">Command `az files share update-site`</a>

##### <a name="ParameterssharesUpdateSite">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--display-name**|string|The full title for the site. Read-only.|display_name|displayName|
|**--root**|dictionary|root|root|root|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--columns**|array|The collection of column definitions reusable across lists under this site.|columns|columns|
|**--content-types**|array|The collection of content types defined for this site.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--drives**|array|The collection of drives (document libraries) under this site.|drives|drives|
|**--items**|array|Used to address any item contained in this site. This collection cannot be enumerated.|items|items|
|**--lists**|array|The collection of lists under this site.|lists|lists|
|**--sites**|array|The collection of the sub-sites under this site.|sites|sites|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--notebooks**|array|The collection of OneNote notebooks that are owned by the user or group. Read-only. Nullable.|notebooks|notebooks|
|**--operations**|array|The status of OneNote operations. Getting an operations collection is not supported, but you can get the status of long-running operations if the Operation-Location header is returned in the response. Read-only. Nullable.|operations|operations|
|**--pages**|array|The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|pages|pages|
|**--resources**|array|The image and other file resources in OneNote pages. Getting a resources collection is not supported, but you can get the binary content of a specific resource. Read-only. Nullable.|resources|resources|
|**--section-groups**|array|The section groups in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|section_groups|sectionGroups|
|**--sections**|array|The sections in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.|sections|sections|
|**--data-location-code**|string|The geographic region code for where this site collection resides. Read-only.|data_location_code|dataLocationCode|
|**--hostname**|string|The hostname for the site collection. Read-only.|hostname|hostname|
|**--microsoft-graph-root**|dictionary|root|microsoft_graph_root|root|
|**--code**|string||code|code|
|**--details**|array||details|details|
|**--inner-error**|object|publicInnerError|inner_error|innerError|
|**--message**|string||message|message|
|**--target**|string||target|target|

### group `az files shareslist`
#### <a name="shares.listCreateColumns">Command `az files shareslist create-column`</a>

##### <a name="Parametersshares.listCreateColumns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--boolean**|dictionary|booleanColumn|boolean|boolean|
|**--calculated**|object|calculatedColumn|calculated|calculated|
|**--choice**|object|choiceColumn|choice|choice|
|**--column-group**|string|For site columns, the name of the group this column belongs to. Helps organize related columns.|column_group|columnGroup|
|**--date-time**|object|dateTimeColumn|date_time|dateTime|
|**--default-value**|object|defaultColumnValue|default_value|defaultValue|
|**--description**|string|The user-facing description of the column.|description|description|
|**--display-name**|string|The user-facing name of the column.|display_name|displayName|
|**--enforce-unique-values**|boolean|If true, no two list items may have the same value for this column.|enforce_unique_values|enforceUniqueValues|
|**--geolocation**|dictionary|geolocationColumn|geolocation|geolocation|
|**--hidden**|boolean|Specifies whether the column is displayed in the user interface.|hidden|hidden|
|**--indexed**|boolean|Specifies whether the column values can used for sorting and searching.|indexed|indexed|
|**--lookup**|object|lookupColumn|lookup|lookup|
|**--name**|string|The API-facing name of the column as it appears in the [fields][] on a [listItem][]. For the user-facing name, see displayName.|name|name|
|**--number**|object|numberColumn|number|number|
|**--person-or-group**|object|personOrGroupColumn|person_or_group|personOrGroup|
|**--read-only**|boolean|Specifies whether the column values can be modified.|read_only|readOnly|
|**--required**|boolean|Specifies whether the column value is not optional.|required|required|
|**--text**|object|textColumn|text|text|
|**--locale**|string|Specifies the locale from which to infer the currency symbol.|locale|locale|

#### <a name="shares.listCreateContentTypes">Command `az files shareslist create-content-type`</a>

##### <a name="Parametersshares.listCreateContentTypes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string|The descriptive text for the item.|description|description|
|**--group**|string|The name of the group this content type belongs to. Helps organize related content types.|group|group|
|**--hidden**|boolean|Indicates whether the content type is hidden in the list's 'New' menu.|hidden|hidden|
|**--name**|string|The name of the content type.|name|name|
|**--order**|object|contentTypeOrder|order|order|
|**--parent-id**|string|The unique identifier of the content type.|parent_id|parentId|
|**--read-only**|boolean|If true, the content type cannot be modified unless this value is first set to false.|read_only|readOnly|
|**--sealed**|boolean|If true, the content type cannot be modified by users or through push-down operations. Only site collection administrators can seal or unseal content types.|sealed|sealed|
|**--column-links**|array|The collection of columns that are required by this content type|column_links|columnLinks|
|**--drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|

#### <a name="shares.listCreateItems">Command `az files shareslist create-item`</a>

##### <a name="Parametersshares.listCreateItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--content-type**|object|contentTypeInfo|content_type|contentType|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|

#### <a name="shares.listCreateSubscriptions">Command `az files shareslist create-subscription`</a>

##### <a name="Parametersshares.listCreateSubscriptions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--application-id**|string|Identifier of the application used to create the subscription. Read-only.|application_id|applicationId|
|**--change-type**|string|Required. Indicates the type of change in the subscribed resource that will raise a change notification. The supported values are: created, updated, deleted. Multiple values can be combined using a comma-separated list.Note: Drive root item and list change notifications support only the updated changeType. User and group change notifications support updated and deleted changeType.|change_type|changeType|
|**--client-state**|string|Optional. Specifies the value of the clientState property sent by the service in each change notification. The maximum length is 128 characters. The client can check that the change notification came from the service by comparing the value of the clientState property sent with the subscription with the value of the clientState property received with each change notification.|client_state|clientState|
|**--creator-id**|string|Identifier of the user or service principal that created the subscription. If the app used delegated permissions to create the subscription, this field contains the id of the signed-in user the app called on behalf of. If the app used application permissions, this field contains the id of the service principal corresponding to the app. Read-only.|creator_id|creatorId|
|**--encryption-certificate**|string|A base64-encoded representation of a certificate with a public key used to encrypt resource data in change notifications. Optional. Required when includeResourceData is true.|encryption_certificate|encryptionCertificate|
|**--encryption-certificate-id**|string|A custom app-provided identifier to help identify the certificate needed to decrypt resource data. Optional.|encryption_certificate_id|encryptionCertificateId|
|**--expiration-date-time**|date-time|Required. Specifies the date and time when the webhook subscription expires. The time is in UTC, and can be an amount of time from subscription creation that varies for the resource subscribed to.  See the table below for maximum supported subscription length of time.|expiration_date_time|expirationDateTime|
|**--include-resource-data**|boolean|When set to true, change notifications include resource data (such as content of a chat message). Optional.|include_resource_data|includeResourceData|
|**--latest-supported-tls-version**|string||latest_supported_tls_version|latestSupportedTlsVersion|
|**--lifecycle-notification-url**|string||lifecycle_notification_url|lifecycleNotificationUrl|
|**--notification-url**|string|Required. The URL of the endpoint that will receive the change notifications. This URL must make use of the HTTPS protocol.|notification_url|notificationUrl|
|**--resource**|string|Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.|resource|resource|

#### <a name="shares.listDeleteColumns">Command `az files shareslist delete-column`</a>

##### <a name="Parametersshares.listDeleteColumns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--column-definition-id**|string|key: id of columnDefinition|column_definition_id|columnDefinition-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.listDeleteContentTypes">Command `az files shareslist delete-content-type`</a>

##### <a name="Parametersshares.listDeleteContentTypes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.listDeleteDrive">Command `az files shareslist delete-drive`</a>

##### <a name="Parametersshares.listDeleteDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.listDeleteItems">Command `az files shareslist delete-item`</a>

##### <a name="Parametersshares.listDeleteItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.listDeleteSubscriptions">Command `az files shareslist delete-subscription`</a>

##### <a name="Parametersshares.listDeleteSubscriptions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--subscription-id**|string|key: id of subscription|subscription_id|subscription-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.listListColumns">Command `az files shareslist list-column`</a>

##### <a name="Parametersshares.listListColumns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.listListContentTypes">Command `az files shareslist list-content-type`</a>

##### <a name="Parametersshares.listListContentTypes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.listListItems">Command `az files shareslist list-item`</a>

##### <a name="Parametersshares.listListItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.listListSubscriptions">Command `az files shareslist list-subscription`</a>

##### <a name="Parametersshares.listListSubscriptions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.listGetColumns">Command `az files shareslist show-column`</a>

##### <a name="Parametersshares.listGetColumns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--column-definition-id**|string|key: id of columnDefinition|column_definition_id|columnDefinition-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.listGetContentTypes">Command `az files shareslist show-content-type`</a>

##### <a name="Parametersshares.listGetContentTypes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.listGetDrive">Command `az files shareslist show-drive`</a>

##### <a name="Parametersshares.listGetDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.listGetItems">Command `az files shareslist show-item`</a>

##### <a name="Parametersshares.listGetItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.listGetSubscriptions">Command `az files shareslist show-subscription`</a>

##### <a name="Parametersshares.listGetSubscriptions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--subscription-id**|string|key: id of subscription|subscription_id|subscription-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.listUpdateColumns">Command `az files shareslist update-column`</a>

##### <a name="Parametersshares.listUpdateColumns">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--column-definition-id**|string|key: id of columnDefinition|column_definition_id|columnDefinition-id|
|**--id**|string|Read-only.|id|id|
|**--boolean**|dictionary|booleanColumn|boolean|boolean|
|**--calculated**|object|calculatedColumn|calculated|calculated|
|**--choice**|object|choiceColumn|choice|choice|
|**--column-group**|string|For site columns, the name of the group this column belongs to. Helps organize related columns.|column_group|columnGroup|
|**--date-time**|object|dateTimeColumn|date_time|dateTime|
|**--default-value**|object|defaultColumnValue|default_value|defaultValue|
|**--description**|string|The user-facing description of the column.|description|description|
|**--display-name**|string|The user-facing name of the column.|display_name|displayName|
|**--enforce-unique-values**|boolean|If true, no two list items may have the same value for this column.|enforce_unique_values|enforceUniqueValues|
|**--geolocation**|dictionary|geolocationColumn|geolocation|geolocation|
|**--hidden**|boolean|Specifies whether the column is displayed in the user interface.|hidden|hidden|
|**--indexed**|boolean|Specifies whether the column values can used for sorting and searching.|indexed|indexed|
|**--lookup**|object|lookupColumn|lookup|lookup|
|**--name**|string|The API-facing name of the column as it appears in the [fields][] on a [listItem][]. For the user-facing name, see displayName.|name|name|
|**--number**|object|numberColumn|number|number|
|**--person-or-group**|object|personOrGroupColumn|person_or_group|personOrGroup|
|**--read-only**|boolean|Specifies whether the column values can be modified.|read_only|readOnly|
|**--required**|boolean|Specifies whether the column value is not optional.|required|required|
|**--text**|object|textColumn|text|text|
|**--locale**|string|Specifies the locale from which to infer the currency symbol.|locale|locale|

#### <a name="shares.listUpdateContentTypes">Command `az files shareslist update-content-type`</a>

##### <a name="Parametersshares.listUpdateContentTypes">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--id**|string|Read-only.|id|id|
|**--description**|string|The descriptive text for the item.|description|description|
|**--group**|string|The name of the group this content type belongs to. Helps organize related content types.|group|group|
|**--hidden**|boolean|Indicates whether the content type is hidden in the list's 'New' menu.|hidden|hidden|
|**--name**|string|The name of the content type.|name|name|
|**--order**|object|contentTypeOrder|order|order|
|**--parent-id**|string|The unique identifier of the content type.|parent_id|parentId|
|**--read-only**|boolean|If true, the content type cannot be modified unless this value is first set to false.|read_only|readOnly|
|**--sealed**|boolean|If true, the content type cannot be modified by users or through push-down operations. Only site collection administrators can seal or unseal content types.|sealed|sealed|
|**--column-links**|array|The collection of columns that are required by this content type|column_links|columnLinks|
|**--drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|

#### <a name="shares.listUpdateDrive">Command `az files shareslist update-drive`</a>

##### <a name="Parametersshares.listUpdateDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--microsoft-graph-drive-type**|string|Describes the type of drive represented by this resource. OneDrive personal drives will return personal. OneDrive for Business will return business. SharePoint document libraries will return documentLibrary. Read-only.|microsoft_graph_drive_type|driveType|
|**--share-point-ids**|object|sharepointIds|share_point_ids|sharePointIds|
|**--system**|dictionary|systemFacet|system|system|
|**--following**|array|The list of items the user is following. Only in OneDrive for Business.|following|following|
|**--items**|array|All items contained in the drive. Read-only. Nullable.|items|items|
|**--root**|object|driveItem|root|root|
|**--special**|array|Collection of common folders available in OneDrive. Read-only. Nullable.|special|special|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-base-item-created-date-time-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--microsoft-graph-base-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--microsoft-graph-base-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--microsoft-graph-base-item-last-modified-date-time-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-base-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--microsoft-graph-base-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--microsoft-graph-user-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--microsoft-graph-user-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--microsoft-graph-item-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--microsoft-graph-item-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--id1**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--name1**|string|The name of the item being referenced. Read-only.|name1|name|
|**--microsoft-graph-item-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--microsoft-graph-item-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--microsoft-graph-item-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--display-name**|string|The displayable title of the list.|display_name|displayName|
|**--list**|object|listInfo|list|list|
|**--sharepoint-ids1**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--microsoft-graph-system-facet-system**|dictionary|systemFacet|microsoft_graph_system_facet_system|system|
|**--columns**|array|The collection of field definitions for this list.|columns|columns|
|**--content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--microsoft-graph-list-items**|array|All items contained in the list.|microsoft_graph_list_items|items|
|**--subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|
|**--deleted**|integer|Total space consumed by files in the recycle bin, in bytes. Read-only.|deleted|deleted|
|**--remaining**|integer|Total space remaining before reaching the quota limit, in bytes. Read-only.|remaining|remaining|
|**--state**|string|Enumeration value that indicates the state of the storage space. Read-only.|state|state|
|**--storage-plan-information**|object|storagePlanInformation|storage_plan_information|storagePlanInformation|
|**--total**|integer|Total allowed storage space, in bytes. Read-only.|total|total|
|**--used**|integer|Total space used, in bytes. Read-only.|used|used|
|**--application3**|object|identity|application3|application|
|**--device3**|object|identity|device3|device|
|**--user3**|object|identity|user3|user|

#### <a name="shares.listUpdateItems">Command `az files shareslist update-item`</a>

##### <a name="Parametersshares.listUpdateItems">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--content-type**|object|contentTypeInfo|content_type|contentType|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--analytics**|object|itemAnalytics|analytics|analytics|
|**--drive-item**|object|driveItem|drive_item|driveItem|
|**--versions**|array|The list of previous versions of the list item.|versions|versions|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|

#### <a name="shares.listUpdateSubscriptions">Command `az files shareslist update-subscription`</a>

##### <a name="Parametersshares.listUpdateSubscriptions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--subscription-id**|string|key: id of subscription|subscription_id|subscription-id|
|**--id**|string|Read-only.|id|id|
|**--application-id**|string|Identifier of the application used to create the subscription. Read-only.|application_id|applicationId|
|**--change-type**|string|Required. Indicates the type of change in the subscribed resource that will raise a change notification. The supported values are: created, updated, deleted. Multiple values can be combined using a comma-separated list.Note: Drive root item and list change notifications support only the updated changeType. User and group change notifications support updated and deleted changeType.|change_type|changeType|
|**--client-state**|string|Optional. Specifies the value of the clientState property sent by the service in each change notification. The maximum length is 128 characters. The client can check that the change notification came from the service by comparing the value of the clientState property sent with the subscription with the value of the clientState property received with each change notification.|client_state|clientState|
|**--creator-id**|string|Identifier of the user or service principal that created the subscription. If the app used delegated permissions to create the subscription, this field contains the id of the signed-in user the app called on behalf of. If the app used application permissions, this field contains the id of the service principal corresponding to the app. Read-only.|creator_id|creatorId|
|**--encryption-certificate**|string|A base64-encoded representation of a certificate with a public key used to encrypt resource data in change notifications. Optional. Required when includeResourceData is true.|encryption_certificate|encryptionCertificate|
|**--encryption-certificate-id**|string|A custom app-provided identifier to help identify the certificate needed to decrypt resource data. Optional.|encryption_certificate_id|encryptionCertificateId|
|**--expiration-date-time**|date-time|Required. Specifies the date and time when the webhook subscription expires. The time is in UTC, and can be an amount of time from subscription creation that varies for the resource subscribed to.  See the table below for maximum supported subscription length of time.|expiration_date_time|expirationDateTime|
|**--include-resource-data**|boolean|When set to true, change notifications include resource data (such as content of a chat message). Optional.|include_resource_data|includeResourceData|
|**--latest-supported-tls-version**|string||latest_supported_tls_version|latestSupportedTlsVersion|
|**--lifecycle-notification-url**|string||lifecycle_notification_url|lifecycleNotificationUrl|
|**--notification-url**|string|Required. The URL of the endpoint that will receive the change notifications. This URL must make use of the HTTPS protocol.|notification_url|notificationUrl|
|**--resource**|string|Required. Specifies the resource that will be monitored for changes. Do not include the base URL (https://graph.microsoft.com/v1.0/). See the possible resource path values for each supported resource.|resource|resource|

### group `az files shareslistcontenttype`
#### <a name="shares.list.contentTypesCreateColumnLinks">Command `az files shareslistcontenttype create-column-link`</a>

##### <a name="Parametersshares.list.contentTypesCreateColumnLinks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|The name of the column  in this content type.|name|name|

#### <a name="shares.list.contentTypesDeleteColumnLinks">Command `az files shareslistcontenttype delete-column-link`</a>

##### <a name="Parametersshares.list.contentTypesDeleteColumnLinks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: id of columnLink|column_link_id|columnLink-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.list.contentTypesListColumnLinks">Command `az files shareslistcontenttype list-column-link`</a>

##### <a name="Parametersshares.list.contentTypesListColumnLinks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.list.contentTypesGetColumnLinks">Command `az files shareslistcontenttype show-column-link`</a>

##### <a name="Parametersshares.list.contentTypesGetColumnLinks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: id of columnLink|column_link_id|columnLink-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.list.contentTypesUpdateColumnLinks">Command `az files shareslistcontenttype update-column-link`</a>

##### <a name="Parametersshares.list.contentTypesUpdateColumnLinks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--content-type-id**|string|key: id of contentType|content_type_id|contentType-id|
|**--column-link-id**|string|key: id of columnLink|column_link_id|columnLink-id|
|**--id**|string|Read-only.|id|id|
|**--name**|string|The name of the column  in this content type.|name|name|

### group `az files shareslistitem`
#### <a name="shares.list.itemsCreateVersions">Command `az files shareslistitem create-version`</a>

##### <a name="Parametersshares.list.itemsCreateVersions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|

#### <a name="shares.list.itemsDeleteDriveItem">Command `az files shareslistitem delete-drive-item`</a>

##### <a name="Parametersshares.list.itemsDeleteDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.list.itemsDeleteFields">Command `az files shareslistitem delete-field`</a>

##### <a name="Parametersshares.list.itemsDeleteFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.list.itemsDeleteRefAnalytics">Command `az files shareslistitem delete-ref-analytic`</a>

##### <a name="Parametersshares.list.itemsDeleteRefAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.list.itemsDeleteVersions">Command `az files shareslistitem delete-version`</a>

##### <a name="Parametersshares.list.itemsDeleteVersions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.list.itemsListVersions">Command `az files shareslistitem list-version`</a>

##### <a name="Parametersshares.list.itemsListVersions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.list.itemsSetRefAnalytics">Command `az files shareslistitem set-ref-analytic`</a>

##### <a name="Parametersshares.list.itemsSetRefAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="shares.list.itemsgetActivitiesByInterval-53ee">Command `az files shareslistitem show-activity`</a>

##### <a name="Parametersshares.list.itemsgetActivitiesByInterval-53ee">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--start-date-time**|string||start_date_time|startDateTime|
|**--end-date-time**|string||end_date_time|endDateTime|
|**--interval**|string||interval|interval|

#### <a name="shares.list.itemsgetActivitiesByInterval-96b0">Command `az files shareslistitem show-activity`</a>

##### <a name="Parametersshares.list.itemsgetActivitiesByInterval-96b0">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="shares.list.itemsGetAnalytics">Command `az files shareslistitem show-analytic`</a>

##### <a name="Parametersshares.list.itemsGetAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.list.itemsGetDriveItem">Command `az files shareslistitem show-drive-item`</a>

##### <a name="Parametersshares.list.itemsGetDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.list.itemsGetFields">Command `az files shareslistitem show-field`</a>

##### <a name="Parametersshares.list.itemsGetFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.list.itemsGetRefAnalytics">Command `az files shareslistitem show-ref-analytic`</a>

##### <a name="Parametersshares.list.itemsGetRefAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|

#### <a name="shares.list.itemsGetVersions">Command `az files shareslistitem show-version`</a>

##### <a name="Parametersshares.list.itemsGetVersions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.list.itemsUpdateDriveItem">Command `az files shareslistitem update-drive-item`</a>

##### <a name="Parametersshares.list.itemsUpdateDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="shares.list.itemsUpdateFields">Command `az files shareslistitem update-field`</a>

##### <a name="Parametersshares.list.itemsUpdateFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--id**|string|Read-only.|id|id|

#### <a name="shares.list.itemsUpdateVersions">Command `az files shareslistitem update-version`</a>

##### <a name="Parametersshares.list.itemsUpdateVersions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|

### group `az files shareslistitem`
#### <a name="shares.listItemCreateVersions">Command `az files shareslistitem create-version`</a>

##### <a name="Parametersshares.listItemCreateVersions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|

#### <a name="shares.listItemDeleteDriveItem">Command `az files shareslistitem delete-drive-item`</a>

##### <a name="Parametersshares.listItemDeleteDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.listItemDeleteFields">Command `az files shareslistitem delete-field`</a>

##### <a name="Parametersshares.listItemDeleteFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.listItemDeleteRefAnalytics">Command `az files shareslistitem delete-ref-analytic`</a>

##### <a name="Parametersshares.listItemDeleteRefAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.listItemDeleteVersions">Command `az files shareslistitem delete-version`</a>

##### <a name="Parametersshares.listItemDeleteVersions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.listItemListVersions">Command `az files shareslistitem list-version`</a>

##### <a name="Parametersshares.listItemListVersions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.listItemSetRefAnalytics">Command `az files shareslistitem set-ref-analytic`</a>

##### <a name="Parametersshares.listItemSetRefAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="shares.listItemgetActivitiesByInterval-53ee">Command `az files shareslistitem show-activity`</a>

##### <a name="Parametersshares.listItemgetActivitiesByInterval-53ee">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--start-date-time**|string||start_date_time|startDateTime|
|**--end-date-time**|string||end_date_time|endDateTime|
|**--interval**|string||interval|interval|

#### <a name="shares.listItemgetActivitiesByInterval-96b0">Command `az files shareslistitem show-activity`</a>

##### <a name="Parametersshares.listItemgetActivitiesByInterval-96b0">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="shares.listItemGetAnalytics">Command `az files shareslistitem show-analytic`</a>

##### <a name="Parametersshares.listItemGetAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.listItemGetDriveItem">Command `az files shareslistitem show-drive-item`</a>

##### <a name="Parametersshares.listItemGetDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.listItemGetFields">Command `az files shareslistitem show-field`</a>

##### <a name="Parametersshares.listItemGetFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.listItemGetRefAnalytics">Command `az files shareslistitem show-ref-analytic`</a>

##### <a name="Parametersshares.listItemGetRefAnalytics">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|

#### <a name="shares.listItemGetVersions">Command `az files shareslistitem show-version`</a>

##### <a name="Parametersshares.listItemGetVersions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.listItemUpdateDriveItem">Command `az files shareslistitem update-drive-item`</a>

##### <a name="Parametersshares.listItemUpdateDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="shares.listItemUpdateFields">Command `az files shareslistitem update-field`</a>

##### <a name="Parametersshares.listItemUpdateFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--id**|string|Read-only.|id|id|

#### <a name="shares.listItemUpdateVersions">Command `az files shareslistitem update-version`</a>

##### <a name="Parametersshares.listItemUpdateVersions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|
|**--last-modified-date-time**|date-time|Date and time the version was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--publication**|object|publicationFacet|publication|publication|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|

### group `az files shareslistitemsversion`
#### <a name="shares.list.items.versionsDeleteFields">Command `az files shareslistitemsversion delete-field`</a>

##### <a name="Parametersshares.list.items.versionsDeleteFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.list.items.versionsrestoreVersion">Command `az files shareslistitemsversion restore-version`</a>

##### <a name="Parametersshares.list.items.versionsrestoreVersion">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|

#### <a name="shares.list.items.versionsGetFields">Command `az files shareslistitemsversion show-field`</a>

##### <a name="Parametersshares.list.items.versionsGetFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.list.items.versionsUpdateFields">Command `az files shareslistitemsversion update-field`</a>

##### <a name="Parametersshares.list.items.versionsUpdateFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-id**|string|key: id of listItem|list_item_id|listItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|

### group `az files shareslistitemversion`
#### <a name="shares.listItem.versionsDeleteFields">Command `az files shareslistitemversion delete-field`</a>

##### <a name="Parametersshares.listItem.versionsDeleteFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.listItem.versionsrestoreVersion">Command `az files shareslistitemversion restore-version`</a>

##### <a name="Parametersshares.listItem.versionsrestoreVersion">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|

#### <a name="shares.listItem.versionsGetFields">Command `az files shareslistitemversion show-field`</a>

##### <a name="Parametersshares.listItem.versionsGetFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.listItem.versionsUpdateFields">Command `az files shareslistitemversion update-field`</a>

##### <a name="Parametersshares.listItem.versionsUpdateFields">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--list-item-version-id**|string|key: id of listItemVersion|list_item_version_id|listItemVersion-id|
|**--id**|string|Read-only.|id|id|

### group `az files sharespermission`
#### <a name="shares.permissiongrant">Command `az files sharespermission grant`</a>

##### <a name="Parametersshares.permissiongrant">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--roles**|array||roles|roles|
|**--recipients**|array||recipients|recipients|

### group `az files sharesshareddriveitem`
#### <a name="shares.sharedDriveItemCreateSharedDriveItem">Command `az files sharesshareddriveitem create-shared-drive-item`</a>

##### <a name="Parametersshares.sharedDriveItemCreateSharedDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--body**|object|New entity|body|body|

#### <a name="shares.sharedDriveItemDeleteSharedDriveItem">Command `az files sharesshareddriveitem delete-shared-drive-item`</a>

##### <a name="Parametersshares.sharedDriveItemDeleteSharedDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="shares.sharedDriveItemListSharedDriveItem">Command `az files sharesshareddriveitem list-shared-drive-item`</a>

##### <a name="Parametersshares.sharedDriveItemListSharedDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.sharedDriveItemGetSharedDriveItem">Command `az files sharesshareddriveitem show-shared-drive-item`</a>

##### <a name="Parametersshares.sharedDriveItemGetSharedDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="shares.sharedDriveItemUpdateSharedDriveItem">Command `az files sharesshareddriveitem update-shared-drive-item`</a>

##### <a name="Parametersshares.sharedDriveItemUpdateSharedDriveItem">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--shared-drive-item-id**|string|key: id of sharedDriveItem|shared_drive_item_id|sharedDriveItem-id|
|**--body**|object|New property values|body|body|

### group `az files user`
#### <a name="usersCreateDrives">Command `az files user create-drive`</a>

##### <a name="ParametersusersCreateDrives">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--microsoft-graph-drive-type**|string|Describes the type of drive represented by this resource. OneDrive personal drives will return personal. OneDrive for Business will return business. SharePoint document libraries will return documentLibrary. Read-only.|microsoft_graph_drive_type|driveType|
|**--share-point-ids**|object|sharepointIds|share_point_ids|sharePointIds|
|**--system**|dictionary|systemFacet|system|system|
|**--following**|array|The list of items the user is following. Only in OneDrive for Business.|following|following|
|**--items**|array|All items contained in the drive. Read-only. Nullable.|items|items|
|**--root**|object|driveItem|root|root|
|**--special**|array|Collection of common folders available in OneDrive. Read-only. Nullable.|special|special|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-base-item-created-date-time-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--microsoft-graph-base-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--microsoft-graph-base-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--microsoft-graph-base-item-last-modified-date-time-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-base-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--microsoft-graph-base-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--microsoft-graph-user-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--microsoft-graph-user-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--microsoft-graph-item-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--microsoft-graph-item-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--id1**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--name1**|string|The name of the item being referenced. Read-only.|name1|name|
|**--microsoft-graph-item-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--microsoft-graph-item-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--microsoft-graph-item-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--display-name**|string|The displayable title of the list.|display_name|displayName|
|**--list**|object|listInfo|list|list|
|**--sharepoint-ids1**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--microsoft-graph-system-facet-system**|dictionary|systemFacet|microsoft_graph_system_facet_system|system|
|**--columns**|array|The collection of field definitions for this list.|columns|columns|
|**--content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--microsoft-graph-list-items**|array|All items contained in the list.|microsoft_graph_list_items|items|
|**--subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|
|**--deleted**|integer|Total space consumed by files in the recycle bin, in bytes. Read-only.|deleted|deleted|
|**--remaining**|integer|Total space remaining before reaching the quota limit, in bytes. Read-only.|remaining|remaining|
|**--state**|string|Enumeration value that indicates the state of the storage space. Read-only.|state|state|
|**--storage-plan-information**|object|storagePlanInformation|storage_plan_information|storagePlanInformation|
|**--total**|integer|Total allowed storage space, in bytes. Read-only.|total|total|
|**--used**|integer|Total space used, in bytes. Read-only.|used|used|
|**--application3**|object|identity|application3|application|
|**--device3**|object|identity|device3|device|
|**--user3**|object|identity|user3|user|

#### <a name="usersDeleteDrives">Command `az files user delete-drive`</a>

##### <a name="ParametersusersDeleteDrives">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersDeleteDrive">Command `az files user delete-drive`</a>

##### <a name="ParametersusersDeleteDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="usersListDrives">Command `az files user list-drive`</a>

##### <a name="ParametersusersListDrives">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetDrives">Command `az files user show-drive`</a>

##### <a name="ParametersusersGetDrives">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetDrive">Command `az files user show-drive`</a>

##### <a name="ParametersusersGetDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="usersUpdateDrives">Command `az files user update-drive`</a>

##### <a name="ParametersusersUpdateDrives">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--drive-id**|string|key: id of drive|drive_id|drive-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|Date and time of item creation. Read-only.|created_date_time|createdDateTime|
|**--description**|string|Provides a user-visible description of the item. Optional.|description|description|
|**--e-tag**|string|ETag for the item. Read-only.|e_tag|eTag|
|**--last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|last_modified_date_time|lastModifiedDateTime|
|**--name**|string|The name of the item. Read-write.|name|name|
|**--web-url**|string|URL that displays the resource in the browser. Read-only.|web_url|webUrl|
|**--created-by-user**|object|Represents an Azure Active Directory user object.|created_by_user|createdByUser|
|**--last-modified-by-user**|object|Represents an Azure Active Directory user object.|last_modified_by_user|lastModifiedByUser|
|**--microsoft-graph-item-reference-drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|microsoft_graph_item_reference_drive_id|driveId|
|**--drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|drive_type|driveType|
|**--microsoft-graph-item-reference-id**|string|Unique identifier of the item in the drive. Read-only.|microsoft_graph_item_reference_id|id|
|**--microsoft-graph-item-reference-name**|string|The name of the item being referenced. Read-only.|microsoft_graph_item_reference_name|name|
|**--path**|string|Path that can be used to navigate to the item. Read-only.|path|path|
|**--share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|share_id|shareId|
|**--sharepoint-ids**|object|sharepointIds|sharepoint_ids|sharepointIds|
|**--site-id**|string||site_id|siteId|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--microsoft-graph-identity-application**|object|identity|microsoft_graph_identity_application|application|
|**--microsoft-graph-identity-device**|object|identity|microsoft_graph_identity_device|device|
|**--microsoft-graph-identity-user**|object|identity|microsoft_graph_identity_user|user|
|**--microsoft-graph-drive-type**|string|Describes the type of drive represented by this resource. OneDrive personal drives will return personal. OneDrive for Business will return business. SharePoint document libraries will return documentLibrary. Read-only.|microsoft_graph_drive_type|driveType|
|**--share-point-ids**|object|sharepointIds|share_point_ids|sharePointIds|
|**--system**|dictionary|systemFacet|system|system|
|**--following**|array|The list of items the user is following. Only in OneDrive for Business.|following|following|
|**--items**|array|All items contained in the drive. Read-only. Nullable.|items|items|
|**--root**|object|driveItem|root|root|
|**--special**|array|Collection of common folders available in OneDrive. Read-only. Nullable.|special|special|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-base-item-created-date-time-created-date-time**|date-time|Date and time of item creation. Read-only.|microsoft_graph_base_item_created_date_time_created_date_time|createdDateTime|
|**--microsoft-graph-base-item-description**|string|Provides a user-visible description of the item. Optional.|microsoft_graph_base_item_description|description|
|**--microsoft-graph-base-item-e-tag**|string|ETag for the item. Read-only.|microsoft_graph_base_item_e_tag|eTag|
|**--microsoft-graph-base-item-last-modified-date-time-last-modified-date-time**|date-time|Date and time the item was last modified. Read-only.|microsoft_graph_base_item_last_modified_date_time_last_modified_date_time|lastModifiedDateTime|
|**--microsoft-graph-base-item-name**|string|The name of the item. Read-write.|microsoft_graph_base_item_name|name|
|**--microsoft-graph-base-item-web-url**|string|URL that displays the resource in the browser. Read-only.|microsoft_graph_base_item_web_url|webUrl|
|**--microsoft-graph-user-created-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_created_by_user|createdByUser|
|**--microsoft-graph-user-last-modified-by-user**|object|Represents an Azure Active Directory user object.|microsoft_graph_user_last_modified_by_user|lastModifiedByUser|
|**--drive-id1**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id1|driveId|
|**--microsoft-graph-item-reference-drive-type**|string|Identifies the type of drive. See [drive][] resource for values.|microsoft_graph_item_reference_drive_type|driveType|
|**--id1**|string|Unique identifier of the item in the drive. Read-only.|id1|id|
|**--name1**|string|The name of the item being referenced. Read-only.|name1|name|
|**--microsoft-graph-item-reference-path**|string|Path that can be used to navigate to the item. Read-only.|microsoft_graph_item_reference_path|path|
|**--microsoft-graph-item-reference-share-id**|string|A unique identifier for a shared resource that can be accessed via the [Shares][] API.|microsoft_graph_item_reference_share_id|shareId|
|**--microsoft-graph-sharepoint-ids**|object|sharepointIds|microsoft_graph_sharepoint_ids|sharepointIds|
|**--microsoft-graph-item-reference-site-id**|string||microsoft_graph_item_reference_site_id|siteId|
|**--application1**|object|identity|application1|application|
|**--device1**|object|identity|device1|device|
|**--user1**|object|identity|user1|user|
|**--application2**|object|identity|application2|application|
|**--device2**|object|identity|device2|device|
|**--user2**|object|identity|user2|user|
|**--display-name**|string|The displayable title of the list.|display_name|displayName|
|**--list**|object|listInfo|list|list|
|**--sharepoint-ids1**|object|sharepointIds|sharepoint_ids1|sharepointIds|
|**--microsoft-graph-system-facet-system**|dictionary|systemFacet|microsoft_graph_system_facet_system|system|
|**--columns**|array|The collection of field definitions for this list.|columns|columns|
|**--content-types**|array|The collection of content types present in this list.|content_types|contentTypes|
|**--drive**|object|drive|drive|drive|
|**--microsoft-graph-list-items**|array|All items contained in the list.|microsoft_graph_list_items|items|
|**--subscriptions**|array|The set of subscriptions on the list.|subscriptions|subscriptions|
|**--deleted**|integer|Total space consumed by files in the recycle bin, in bytes. Read-only.|deleted|deleted|
|**--remaining**|integer|Total space remaining before reaching the quota limit, in bytes. Read-only.|remaining|remaining|
|**--state**|string|Enumeration value that indicates the state of the storage space. Read-only.|state|state|
|**--storage-plan-information**|object|storagePlanInformation|storage_plan_information|storagePlanInformation|
|**--total**|integer|Total allowed storage space, in bytes. Read-only.|total|total|
|**--used**|integer|Total space used, in bytes. Read-only.|used|used|
|**--application3**|object|identity|application3|application|
|**--device3**|object|identity|device3|device|
|**--user3**|object|identity|user3|user|

#### <a name="usersUpdateDrive">Command `az files user update-drive`</a>

##### <a name="ParametersusersUpdateDrive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--drive-id**|string|Unique identifier of the drive instance that contains the item. Read-only.|drive_id|driveId|
