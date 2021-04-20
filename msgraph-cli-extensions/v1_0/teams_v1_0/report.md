# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az teams_v1_0|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az teams_v1_0` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az teams chatschat|chats.chat|[commands](#CommandsInchats.chat)|
|az teams chat|chats|[commands](#CommandsInchats)|
|az teams group|groups|[commands](#CommandsIngroups)|
|az teams teamsteam|teams.team|[commands](#CommandsInteams.team)|
|az teams team|teams|[commands](#CommandsInteams)|
|az teams teamschannel|teams.channels|[commands](#CommandsInteams.channels)|
|az teams teamschannelsmessage|teams.channels.messages|[commands](#CommandsInteams.channels.messages)|
|az teams teamschannelstab|teams.channels.tabs|[commands](#CommandsInteams.channels.tabs)|
|az teams teamsinstalledapp|teams.installedApps|[commands](#CommandsInteams.installedApps)|
|az teams teamsprimarychannel|teams.primaryChannel|[commands](#CommandsInteams.primaryChannel)|
|az teams teamsprimarychannelmessage|teams.primaryChannel.messages|[commands](#CommandsInteams.primaryChannel.messages)|
|az teams teamsprimarychanneltab|teams.primaryChannel.tabs|[commands](#CommandsInteams.primaryChannel.tabs)|
|az teams teamsschedule|teams.schedule|[commands](#CommandsInteams.schedule)|
|az teams teamwork|teamwork.teamwork|[commands](#CommandsInteamwork.teamwork)|
|az teams teamwork|teamwork|[commands](#CommandsInteamwork)|
|az teams user|users|[commands](#CommandsInusers)|

## COMMANDS
### <a name="CommandsInchats">Commands in `az teams chat` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams chat show-all-message](#chatsgetAllMessages)|getAllMessages|[Parameters](#ParameterschatsgetAllMessages)|Not Found|

### <a name="CommandsInchats.chat">Commands in `az teams chatschat` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams chatschat create-chat](#chats.chatCreateChat)|CreateChat|[Parameters](#Parameterschats.chatCreateChat)|Not Found|
|[az teams chatschat delete-chat](#chats.chatDeleteChat)|DeleteChat|[Parameters](#Parameterschats.chatDeleteChat)|Not Found|
|[az teams chatschat list-chat](#chats.chatListChat)|ListChat|[Parameters](#Parameterschats.chatListChat)|Not Found|
|[az teams chatschat show-chat](#chats.chatGetChat)|GetChat|[Parameters](#Parameterschats.chatGetChat)|Not Found|
|[az teams chatschat update-chat](#chats.chatUpdateChat)|UpdateChat|[Parameters](#Parameterschats.chatUpdateChat)|Not Found|

### <a name="CommandsIngroups">Commands in `az teams group` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams group delete-team](#groupsDeleteTeam)|DeleteTeam|[Parameters](#ParametersgroupsDeleteTeam)|Not Found|
|[az teams group show-team](#groupsGetTeam)|GetTeam|[Parameters](#ParametersgroupsGetTeam)|Not Found|
|[az teams group update-team](#groupsUpdateTeam)|UpdateTeam|[Parameters](#ParametersgroupsUpdateTeam)|Not Found|

### <a name="CommandsInteams">Commands in `az teams team` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams team archive](#teamsarchive)|archive|[Parameters](#Parametersteamsarchive)|Not Found|
|[az teams team clone](#teamsclone)|clone|[Parameters](#Parametersteamsclone)|Not Found|
|[az teams team create-channel](#teamsCreateChannels)|CreateChannels|[Parameters](#ParametersteamsCreateChannels)|Not Found|
|[az teams team create-installed-app](#teamsCreateInstalledApps)|CreateInstalledApps|[Parameters](#ParametersteamsCreateInstalledApps)|Not Found|
|[az teams team create-member](#teamsCreateMembers)|CreateMembers|[Parameters](#ParametersteamsCreateMembers)|Not Found|
|[az teams team create-operation](#teamsCreateOperations)|CreateOperations|[Parameters](#ParametersteamsCreateOperations)|Not Found|
|[az teams team delete-channel](#teamsDeleteChannels)|DeleteChannels|[Parameters](#ParametersteamsDeleteChannels)|Not Found|
|[az teams team delete-installed-app](#teamsDeleteInstalledApps)|DeleteInstalledApps|[Parameters](#ParametersteamsDeleteInstalledApps)|Not Found|
|[az teams team delete-member](#teamsDeleteMembers)|DeleteMembers|[Parameters](#ParametersteamsDeleteMembers)|Not Found|
|[az teams team delete-operation](#teamsDeleteOperations)|DeleteOperations|[Parameters](#ParametersteamsDeleteOperations)|Not Found|
|[az teams team delete-primary-channel](#teamsDeletePrimaryChannel)|DeletePrimaryChannel|[Parameters](#ParametersteamsDeletePrimaryChannel)|Not Found|
|[az teams team delete-ref-group](#teamsDeleteRefGroup)|DeleteRefGroup|[Parameters](#ParametersteamsDeleteRefGroup)|Not Found|
|[az teams team delete-ref-template](#teamsDeleteRefTemplate)|DeleteRefTemplate|[Parameters](#ParametersteamsDeleteRefTemplate)|Not Found|
|[az teams team delete-schedule](#teamsDeleteSchedule)|DeleteSchedule|[Parameters](#ParametersteamsDeleteSchedule)|Not Found|
|[az teams team list-channel](#teamsListChannels)|ListChannels|[Parameters](#ParametersteamsListChannels)|Not Found|
|[az teams team list-installed-app](#teamsListInstalledApps)|ListInstalledApps|[Parameters](#ParametersteamsListInstalledApps)|Not Found|
|[az teams team list-member](#teamsListMembers)|ListMembers|[Parameters](#ParametersteamsListMembers)|Not Found|
|[az teams team list-operation](#teamsListOperations)|ListOperations|[Parameters](#ParametersteamsListOperations)|Not Found|
|[az teams team set-ref-group](#teamsSetRefGroup)|SetRefGroup|[Parameters](#ParametersteamsSetRefGroup)|Not Found|
|[az teams team set-ref-template](#teamsSetRefTemplate)|SetRefTemplate|[Parameters](#ParametersteamsSetRefTemplate)|Not Found|
|[az teams team show-all-message](#teamsgetAllMessages)|getAllMessages|[Parameters](#ParametersteamsgetAllMessages)|Not Found|
|[az teams team show-channel](#teamsGetChannels)|GetChannels|[Parameters](#ParametersteamsGetChannels)|Not Found|
|[az teams team show-group](#teamsGetGroup)|GetGroup|[Parameters](#ParametersteamsGetGroup)|Not Found|
|[az teams team show-installed-app](#teamsGetInstalledApps)|GetInstalledApps|[Parameters](#ParametersteamsGetInstalledApps)|Not Found|
|[az teams team show-member](#teamsGetMembers)|GetMembers|[Parameters](#ParametersteamsGetMembers)|Not Found|
|[az teams team show-operation](#teamsGetOperations)|GetOperations|[Parameters](#ParametersteamsGetOperations)|Not Found|
|[az teams team show-primary-channel](#teamsGetPrimaryChannel)|GetPrimaryChannel|[Parameters](#ParametersteamsGetPrimaryChannel)|Not Found|
|[az teams team show-ref-group](#teamsGetRefGroup)|GetRefGroup|[Parameters](#ParametersteamsGetRefGroup)|Not Found|
|[az teams team show-ref-template](#teamsGetRefTemplate)|GetRefTemplate|[Parameters](#ParametersteamsGetRefTemplate)|Not Found|
|[az teams team show-schedule](#teamsGetSchedule)|GetSchedule|[Parameters](#ParametersteamsGetSchedule)|Not Found|
|[az teams team show-template](#teamsGetTemplate)|GetTemplate|[Parameters](#ParametersteamsGetTemplate)|Not Found|
|[az teams team unarchive](#teamsunarchive)|unarchive|[Parameters](#Parametersteamsunarchive)|Not Found|
|[az teams team update-channel](#teamsUpdateChannels)|UpdateChannels|[Parameters](#ParametersteamsUpdateChannels)|Not Found|
|[az teams team update-installed-app](#teamsUpdateInstalledApps)|UpdateInstalledApps|[Parameters](#ParametersteamsUpdateInstalledApps)|Not Found|
|[az teams team update-member](#teamsUpdateMembers)|UpdateMembers|[Parameters](#ParametersteamsUpdateMembers)|Not Found|
|[az teams team update-operation](#teamsUpdateOperations)|UpdateOperations|[Parameters](#ParametersteamsUpdateOperations)|Not Found|
|[az teams team update-primary-channel](#teamsUpdatePrimaryChannel)|UpdatePrimaryChannel|[Parameters](#ParametersteamsUpdatePrimaryChannel)|Not Found|
|[az teams team update-schedule](#teamsUpdateSchedule)|UpdateSchedule|[Parameters](#ParametersteamsUpdateSchedule)|Not Found|

### <a name="CommandsInteams.channels">Commands in `az teams teamschannel` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams teamschannel create-member](#teams.channelsCreateMembers)|CreateMembers|[Parameters](#Parametersteams.channelsCreateMembers)|Not Found|
|[az teams teamschannel create-message](#teams.channelsCreateMessages)|CreateMessages|[Parameters](#Parametersteams.channelsCreateMessages)|Not Found|
|[az teams teamschannel create-tab](#teams.channelsCreateTabs)|CreateTabs|[Parameters](#Parametersteams.channelsCreateTabs)|Not Found|
|[az teams teamschannel delete-file-folder](#teams.channelsDeleteFilesFolder)|DeleteFilesFolder|[Parameters](#Parametersteams.channelsDeleteFilesFolder)|Not Found|
|[az teams teamschannel delete-member](#teams.channelsDeleteMembers)|DeleteMembers|[Parameters](#Parametersteams.channelsDeleteMembers)|Not Found|
|[az teams teamschannel delete-message](#teams.channelsDeleteMessages)|DeleteMessages|[Parameters](#Parametersteams.channelsDeleteMessages)|Not Found|
|[az teams teamschannel delete-tab](#teams.channelsDeleteTabs)|DeleteTabs|[Parameters](#Parametersteams.channelsDeleteTabs)|Not Found|
|[az teams teamschannel list-member](#teams.channelsListMembers)|ListMembers|[Parameters](#Parametersteams.channelsListMembers)|Not Found|
|[az teams teamschannel list-message](#teams.channelsListMessages)|ListMessages|[Parameters](#Parametersteams.channelsListMessages)|Not Found|
|[az teams teamschannel list-tab](#teams.channelsListTabs)|ListTabs|[Parameters](#Parametersteams.channelsListTabs)|Not Found|
|[az teams teamschannel show-file-folder](#teams.channelsGetFilesFolder)|GetFilesFolder|[Parameters](#Parametersteams.channelsGetFilesFolder)|Not Found|
|[az teams teamschannel show-member](#teams.channelsGetMembers)|GetMembers|[Parameters](#Parametersteams.channelsGetMembers)|Not Found|
|[az teams teamschannel show-message](#teams.channelsGetMessages)|GetMessages|[Parameters](#Parametersteams.channelsGetMessages)|Not Found|
|[az teams teamschannel show-tab](#teams.channelsGetTabs)|GetTabs|[Parameters](#Parametersteams.channelsGetTabs)|Not Found|
|[az teams teamschannel update-file-folder](#teams.channelsUpdateFilesFolder)|UpdateFilesFolder|[Parameters](#Parametersteams.channelsUpdateFilesFolder)|Not Found|
|[az teams teamschannel update-member](#teams.channelsUpdateMembers)|UpdateMembers|[Parameters](#Parametersteams.channelsUpdateMembers)|Not Found|
|[az teams teamschannel update-message](#teams.channelsUpdateMessages)|UpdateMessages|[Parameters](#Parametersteams.channelsUpdateMessages)|Not Found|
|[az teams teamschannel update-tab](#teams.channelsUpdateTabs)|UpdateTabs|[Parameters](#Parametersteams.channelsUpdateTabs)|Not Found|

### <a name="CommandsInteams.channels.messages">Commands in `az teams teamschannelsmessage` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams teamschannelsmessage create-hosted-content](#teams.channels.messagesCreateHostedContents)|CreateHostedContents|[Parameters](#Parametersteams.channels.messagesCreateHostedContents)|Not Found|
|[az teams teamschannelsmessage create-reply](#teams.channels.messagesCreateReplies)|CreateReplies|[Parameters](#Parametersteams.channels.messagesCreateReplies)|Not Found|
|[az teams teamschannelsmessage delete-hosted-content](#teams.channels.messagesDeleteHostedContents)|DeleteHostedContents|[Parameters](#Parametersteams.channels.messagesDeleteHostedContents)|Not Found|
|[az teams teamschannelsmessage delete-reply](#teams.channels.messagesDeleteReplies)|DeleteReplies|[Parameters](#Parametersteams.channels.messagesDeleteReplies)|Not Found|
|[az teams teamschannelsmessage list-hosted-content](#teams.channels.messagesListHostedContents)|ListHostedContents|[Parameters](#Parametersteams.channels.messagesListHostedContents)|Not Found|
|[az teams teamschannelsmessage list-reply](#teams.channels.messagesListReplies)|ListReplies|[Parameters](#Parametersteams.channels.messagesListReplies)|Not Found|
|[az teams teamschannelsmessage show-hosted-content](#teams.channels.messagesGetHostedContents)|GetHostedContents|[Parameters](#Parametersteams.channels.messagesGetHostedContents)|Not Found|
|[az teams teamschannelsmessage show-reply](#teams.channels.messagesGetReplies)|GetReplies|[Parameters](#Parametersteams.channels.messagesGetReplies)|Not Found|
|[az teams teamschannelsmessage update-hosted-content](#teams.channels.messagesUpdateHostedContents)|UpdateHostedContents|[Parameters](#Parametersteams.channels.messagesUpdateHostedContents)|Not Found|
|[az teams teamschannelsmessage update-reply](#teams.channels.messagesUpdateReplies)|UpdateReplies|[Parameters](#Parametersteams.channels.messagesUpdateReplies)|Not Found|

### <a name="CommandsInteams.channels.tabs">Commands in `az teams teamschannelstab` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams teamschannelstab delete-ref-team-app](#teams.channels.tabsDeleteRefTeamsApp)|DeleteRefTeamsApp|[Parameters](#Parametersteams.channels.tabsDeleteRefTeamsApp)|Not Found|
|[az teams teamschannelstab set-ref-team-app](#teams.channels.tabsSetRefTeamsApp)|SetRefTeamsApp|[Parameters](#Parametersteams.channels.tabsSetRefTeamsApp)|Not Found|
|[az teams teamschannelstab show-ref-team-app](#teams.channels.tabsGetRefTeamsApp)|GetRefTeamsApp|[Parameters](#Parametersteams.channels.tabsGetRefTeamsApp)|Not Found|
|[az teams teamschannelstab show-team-app](#teams.channels.tabsGetTeamsApp)|GetTeamsApp|[Parameters](#Parametersteams.channels.tabsGetTeamsApp)|Not Found|

### <a name="CommandsInteams.installedApps">Commands in `az teams teamsinstalledapp` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams teamsinstalledapp delete-ref-team-app](#teams.installedAppsDeleteRefTeamsApp)|DeleteRefTeamsApp|[Parameters](#Parametersteams.installedAppsDeleteRefTeamsApp)|Not Found|
|[az teams teamsinstalledapp delete-ref-team-app-definition](#teams.installedAppsDeleteRefTeamsAppDefinition)|DeleteRefTeamsAppDefinition|[Parameters](#Parametersteams.installedAppsDeleteRefTeamsAppDefinition)|Not Found|
|[az teams teamsinstalledapp set-ref-team-app](#teams.installedAppsSetRefTeamsApp)|SetRefTeamsApp|[Parameters](#Parametersteams.installedAppsSetRefTeamsApp)|Not Found|
|[az teams teamsinstalledapp set-ref-team-app-definition](#teams.installedAppsSetRefTeamsAppDefinition)|SetRefTeamsAppDefinition|[Parameters](#Parametersteams.installedAppsSetRefTeamsAppDefinition)|Not Found|
|[az teams teamsinstalledapp show-ref-team-app](#teams.installedAppsGetRefTeamsApp)|GetRefTeamsApp|[Parameters](#Parametersteams.installedAppsGetRefTeamsApp)|Not Found|
|[az teams teamsinstalledapp show-ref-team-app-definition](#teams.installedAppsGetRefTeamsAppDefinition)|GetRefTeamsAppDefinition|[Parameters](#Parametersteams.installedAppsGetRefTeamsAppDefinition)|Not Found|
|[az teams teamsinstalledapp show-team-app](#teams.installedAppsGetTeamsApp)|GetTeamsApp|[Parameters](#Parametersteams.installedAppsGetTeamsApp)|Not Found|
|[az teams teamsinstalledapp show-team-app-definition](#teams.installedAppsGetTeamsAppDefinition)|GetTeamsAppDefinition|[Parameters](#Parametersteams.installedAppsGetTeamsAppDefinition)|Not Found|
|[az teams teamsinstalledapp upgrade](#teams.installedAppsupgrade)|upgrade|[Parameters](#Parametersteams.installedAppsupgrade)|Not Found|

### <a name="CommandsInteams.primaryChannel">Commands in `az teams teamsprimarychannel` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams teamsprimarychannel create-member](#teams.primaryChannelCreateMembers)|CreateMembers|[Parameters](#Parametersteams.primaryChannelCreateMembers)|Not Found|
|[az teams teamsprimarychannel create-message](#teams.primaryChannelCreateMessages)|CreateMessages|[Parameters](#Parametersteams.primaryChannelCreateMessages)|Not Found|
|[az teams teamsprimarychannel create-tab](#teams.primaryChannelCreateTabs)|CreateTabs|[Parameters](#Parametersteams.primaryChannelCreateTabs)|Not Found|
|[az teams teamsprimarychannel delete-file-folder](#teams.primaryChannelDeleteFilesFolder)|DeleteFilesFolder|[Parameters](#Parametersteams.primaryChannelDeleteFilesFolder)|Not Found|
|[az teams teamsprimarychannel delete-member](#teams.primaryChannelDeleteMembers)|DeleteMembers|[Parameters](#Parametersteams.primaryChannelDeleteMembers)|Not Found|
|[az teams teamsprimarychannel delete-message](#teams.primaryChannelDeleteMessages)|DeleteMessages|[Parameters](#Parametersteams.primaryChannelDeleteMessages)|Not Found|
|[az teams teamsprimarychannel delete-tab](#teams.primaryChannelDeleteTabs)|DeleteTabs|[Parameters](#Parametersteams.primaryChannelDeleteTabs)|Not Found|
|[az teams teamsprimarychannel list-member](#teams.primaryChannelListMembers)|ListMembers|[Parameters](#Parametersteams.primaryChannelListMembers)|Not Found|
|[az teams teamsprimarychannel list-message](#teams.primaryChannelListMessages)|ListMessages|[Parameters](#Parametersteams.primaryChannelListMessages)|Not Found|
|[az teams teamsprimarychannel list-tab](#teams.primaryChannelListTabs)|ListTabs|[Parameters](#Parametersteams.primaryChannelListTabs)|Not Found|
|[az teams teamsprimarychannel show-file-folder](#teams.primaryChannelGetFilesFolder)|GetFilesFolder|[Parameters](#Parametersteams.primaryChannelGetFilesFolder)|Not Found|
|[az teams teamsprimarychannel show-member](#teams.primaryChannelGetMembers)|GetMembers|[Parameters](#Parametersteams.primaryChannelGetMembers)|Not Found|
|[az teams teamsprimarychannel show-message](#teams.primaryChannelGetMessages)|GetMessages|[Parameters](#Parametersteams.primaryChannelGetMessages)|Not Found|
|[az teams teamsprimarychannel show-tab](#teams.primaryChannelGetTabs)|GetTabs|[Parameters](#Parametersteams.primaryChannelGetTabs)|Not Found|
|[az teams teamsprimarychannel update-file-folder](#teams.primaryChannelUpdateFilesFolder)|UpdateFilesFolder|[Parameters](#Parametersteams.primaryChannelUpdateFilesFolder)|Not Found|
|[az teams teamsprimarychannel update-member](#teams.primaryChannelUpdateMembers)|UpdateMembers|[Parameters](#Parametersteams.primaryChannelUpdateMembers)|Not Found|
|[az teams teamsprimarychannel update-message](#teams.primaryChannelUpdateMessages)|UpdateMessages|[Parameters](#Parametersteams.primaryChannelUpdateMessages)|Not Found|
|[az teams teamsprimarychannel update-tab](#teams.primaryChannelUpdateTabs)|UpdateTabs|[Parameters](#Parametersteams.primaryChannelUpdateTabs)|Not Found|

### <a name="CommandsInteams.primaryChannel.messages">Commands in `az teams teamsprimarychannelmessage` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams teamsprimarychannelmessage create-hosted-content](#teams.primaryChannel.messagesCreateHostedContents)|CreateHostedContents|[Parameters](#Parametersteams.primaryChannel.messagesCreateHostedContents)|Not Found|
|[az teams teamsprimarychannelmessage create-reply](#teams.primaryChannel.messagesCreateReplies)|CreateReplies|[Parameters](#Parametersteams.primaryChannel.messagesCreateReplies)|Not Found|
|[az teams teamsprimarychannelmessage delete-hosted-content](#teams.primaryChannel.messagesDeleteHostedContents)|DeleteHostedContents|[Parameters](#Parametersteams.primaryChannel.messagesDeleteHostedContents)|Not Found|
|[az teams teamsprimarychannelmessage delete-reply](#teams.primaryChannel.messagesDeleteReplies)|DeleteReplies|[Parameters](#Parametersteams.primaryChannel.messagesDeleteReplies)|Not Found|
|[az teams teamsprimarychannelmessage list-hosted-content](#teams.primaryChannel.messagesListHostedContents)|ListHostedContents|[Parameters](#Parametersteams.primaryChannel.messagesListHostedContents)|Not Found|
|[az teams teamsprimarychannelmessage list-reply](#teams.primaryChannel.messagesListReplies)|ListReplies|[Parameters](#Parametersteams.primaryChannel.messagesListReplies)|Not Found|
|[az teams teamsprimarychannelmessage show-hosted-content](#teams.primaryChannel.messagesGetHostedContents)|GetHostedContents|[Parameters](#Parametersteams.primaryChannel.messagesGetHostedContents)|Not Found|
|[az teams teamsprimarychannelmessage show-reply](#teams.primaryChannel.messagesGetReplies)|GetReplies|[Parameters](#Parametersteams.primaryChannel.messagesGetReplies)|Not Found|
|[az teams teamsprimarychannelmessage update-hosted-content](#teams.primaryChannel.messagesUpdateHostedContents)|UpdateHostedContents|[Parameters](#Parametersteams.primaryChannel.messagesUpdateHostedContents)|Not Found|
|[az teams teamsprimarychannelmessage update-reply](#teams.primaryChannel.messagesUpdateReplies)|UpdateReplies|[Parameters](#Parametersteams.primaryChannel.messagesUpdateReplies)|Not Found|

### <a name="CommandsInteams.primaryChannel.tabs">Commands in `az teams teamsprimarychanneltab` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams teamsprimarychanneltab delete-ref-team-app](#teams.primaryChannel.tabsDeleteRefTeamsApp)|DeleteRefTeamsApp|[Parameters](#Parametersteams.primaryChannel.tabsDeleteRefTeamsApp)|Not Found|
|[az teams teamsprimarychanneltab set-ref-team-app](#teams.primaryChannel.tabsSetRefTeamsApp)|SetRefTeamsApp|[Parameters](#Parametersteams.primaryChannel.tabsSetRefTeamsApp)|Not Found|
|[az teams teamsprimarychanneltab show-ref-team-app](#teams.primaryChannel.tabsGetRefTeamsApp)|GetRefTeamsApp|[Parameters](#Parametersteams.primaryChannel.tabsGetRefTeamsApp)|Not Found|
|[az teams teamsprimarychanneltab show-team-app](#teams.primaryChannel.tabsGetTeamsApp)|GetTeamsApp|[Parameters](#Parametersteams.primaryChannel.tabsGetTeamsApp)|Not Found|

### <a name="CommandsInteams.schedule">Commands in `az teams teamsschedule` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams teamsschedule create-offer-shift-request](#teams.scheduleCreateOfferShiftRequests)|CreateOfferShiftRequests|[Parameters](#Parametersteams.scheduleCreateOfferShiftRequests)|Not Found|
|[az teams teamsschedule create-open-shift](#teams.scheduleCreateOpenShifts)|CreateOpenShifts|[Parameters](#Parametersteams.scheduleCreateOpenShifts)|Not Found|
|[az teams teamsschedule create-open-shift-change-request](#teams.scheduleCreateOpenShiftChangeRequests)|CreateOpenShiftChangeRequests|[Parameters](#Parametersteams.scheduleCreateOpenShiftChangeRequests)|Not Found|
|[az teams teamsschedule create-scheduling-group](#teams.scheduleCreateSchedulingGroups)|CreateSchedulingGroups|[Parameters](#Parametersteams.scheduleCreateSchedulingGroups)|Not Found|
|[az teams teamsschedule create-shift](#teams.scheduleCreateShifts)|CreateShifts|[Parameters](#Parametersteams.scheduleCreateShifts)|Not Found|
|[az teams teamsschedule create-swap-shift-change-request](#teams.scheduleCreateSwapShiftsChangeRequests)|CreateSwapShiftsChangeRequests|[Parameters](#Parametersteams.scheduleCreateSwapShiftsChangeRequests)|Not Found|
|[az teams teamsschedule create-time-off](#teams.scheduleCreateTimesOff)|CreateTimesOff|[Parameters](#Parametersteams.scheduleCreateTimesOff)|Not Found|
|[az teams teamsschedule create-time-off-reason](#teams.scheduleCreateTimeOffReasons)|CreateTimeOffReasons|[Parameters](#Parametersteams.scheduleCreateTimeOffReasons)|Not Found|
|[az teams teamsschedule create-time-off-request](#teams.scheduleCreateTimeOffRequests)|CreateTimeOffRequests|[Parameters](#Parametersteams.scheduleCreateTimeOffRequests)|Not Found|
|[az teams teamsschedule delete-offer-shift-request](#teams.scheduleDeleteOfferShiftRequests)|DeleteOfferShiftRequests|[Parameters](#Parametersteams.scheduleDeleteOfferShiftRequests)|Not Found|
|[az teams teamsschedule delete-open-shift](#teams.scheduleDeleteOpenShifts)|DeleteOpenShifts|[Parameters](#Parametersteams.scheduleDeleteOpenShifts)|Not Found|
|[az teams teamsschedule delete-open-shift-change-request](#teams.scheduleDeleteOpenShiftChangeRequests)|DeleteOpenShiftChangeRequests|[Parameters](#Parametersteams.scheduleDeleteOpenShiftChangeRequests)|Not Found|
|[az teams teamsschedule delete-scheduling-group](#teams.scheduleDeleteSchedulingGroups)|DeleteSchedulingGroups|[Parameters](#Parametersteams.scheduleDeleteSchedulingGroups)|Not Found|
|[az teams teamsschedule delete-shift](#teams.scheduleDeleteShifts)|DeleteShifts|[Parameters](#Parametersteams.scheduleDeleteShifts)|Not Found|
|[az teams teamsschedule delete-swap-shift-change-request](#teams.scheduleDeleteSwapShiftsChangeRequests)|DeleteSwapShiftsChangeRequests|[Parameters](#Parametersteams.scheduleDeleteSwapShiftsChangeRequests)|Not Found|
|[az teams teamsschedule delete-time-off](#teams.scheduleDeleteTimesOff)|DeleteTimesOff|[Parameters](#Parametersteams.scheduleDeleteTimesOff)|Not Found|
|[az teams teamsschedule delete-time-off-reason](#teams.scheduleDeleteTimeOffReasons)|DeleteTimeOffReasons|[Parameters](#Parametersteams.scheduleDeleteTimeOffReasons)|Not Found|
|[az teams teamsschedule delete-time-off-request](#teams.scheduleDeleteTimeOffRequests)|DeleteTimeOffRequests|[Parameters](#Parametersteams.scheduleDeleteTimeOffRequests)|Not Found|
|[az teams teamsschedule list-offer-shift-request](#teams.scheduleListOfferShiftRequests)|ListOfferShiftRequests|[Parameters](#Parametersteams.scheduleListOfferShiftRequests)|Not Found|
|[az teams teamsschedule list-open-shift](#teams.scheduleListOpenShifts)|ListOpenShifts|[Parameters](#Parametersteams.scheduleListOpenShifts)|Not Found|
|[az teams teamsschedule list-open-shift-change-request](#teams.scheduleListOpenShiftChangeRequests)|ListOpenShiftChangeRequests|[Parameters](#Parametersteams.scheduleListOpenShiftChangeRequests)|Not Found|
|[az teams teamsschedule list-scheduling-group](#teams.scheduleListSchedulingGroups)|ListSchedulingGroups|[Parameters](#Parametersteams.scheduleListSchedulingGroups)|Not Found|
|[az teams teamsschedule list-shift](#teams.scheduleListShifts)|ListShifts|[Parameters](#Parametersteams.scheduleListShifts)|Not Found|
|[az teams teamsschedule list-swap-shift-change-request](#teams.scheduleListSwapShiftsChangeRequests)|ListSwapShiftsChangeRequests|[Parameters](#Parametersteams.scheduleListSwapShiftsChangeRequests)|Not Found|
|[az teams teamsschedule list-time-off](#teams.scheduleListTimesOff)|ListTimesOff|[Parameters](#Parametersteams.scheduleListTimesOff)|Not Found|
|[az teams teamsschedule list-time-off-reason](#teams.scheduleListTimeOffReasons)|ListTimeOffReasons|[Parameters](#Parametersteams.scheduleListTimeOffReasons)|Not Found|
|[az teams teamsschedule list-time-off-request](#teams.scheduleListTimeOffRequests)|ListTimeOffRequests|[Parameters](#Parametersteams.scheduleListTimeOffRequests)|Not Found|
|[az teams teamsschedule share](#teams.scheduleshare)|share|[Parameters](#Parametersteams.scheduleshare)|Not Found|
|[az teams teamsschedule show-offer-shift-request](#teams.scheduleGetOfferShiftRequests)|GetOfferShiftRequests|[Parameters](#Parametersteams.scheduleGetOfferShiftRequests)|Not Found|
|[az teams teamsschedule show-open-shift](#teams.scheduleGetOpenShifts)|GetOpenShifts|[Parameters](#Parametersteams.scheduleGetOpenShifts)|Not Found|
|[az teams teamsschedule show-open-shift-change-request](#teams.scheduleGetOpenShiftChangeRequests)|GetOpenShiftChangeRequests|[Parameters](#Parametersteams.scheduleGetOpenShiftChangeRequests)|Not Found|
|[az teams teamsschedule show-scheduling-group](#teams.scheduleGetSchedulingGroups)|GetSchedulingGroups|[Parameters](#Parametersteams.scheduleGetSchedulingGroups)|Not Found|
|[az teams teamsschedule show-shift](#teams.scheduleGetShifts)|GetShifts|[Parameters](#Parametersteams.scheduleGetShifts)|Not Found|
|[az teams teamsschedule show-swap-shift-change-request](#teams.scheduleGetSwapShiftsChangeRequests)|GetSwapShiftsChangeRequests|[Parameters](#Parametersteams.scheduleGetSwapShiftsChangeRequests)|Not Found|
|[az teams teamsschedule show-time-off](#teams.scheduleGetTimesOff)|GetTimesOff|[Parameters](#Parametersteams.scheduleGetTimesOff)|Not Found|
|[az teams teamsschedule show-time-off-reason](#teams.scheduleGetTimeOffReasons)|GetTimeOffReasons|[Parameters](#Parametersteams.scheduleGetTimeOffReasons)|Not Found|
|[az teams teamsschedule show-time-off-request](#teams.scheduleGetTimeOffRequests)|GetTimeOffRequests|[Parameters](#Parametersteams.scheduleGetTimeOffRequests)|Not Found|
|[az teams teamsschedule update-offer-shift-request](#teams.scheduleUpdateOfferShiftRequests)|UpdateOfferShiftRequests|[Parameters](#Parametersteams.scheduleUpdateOfferShiftRequests)|Not Found|
|[az teams teamsschedule update-open-shift](#teams.scheduleUpdateOpenShifts)|UpdateOpenShifts|[Parameters](#Parametersteams.scheduleUpdateOpenShifts)|Not Found|
|[az teams teamsschedule update-open-shift-change-request](#teams.scheduleUpdateOpenShiftChangeRequests)|UpdateOpenShiftChangeRequests|[Parameters](#Parametersteams.scheduleUpdateOpenShiftChangeRequests)|Not Found|
|[az teams teamsschedule update-scheduling-group](#teams.scheduleUpdateSchedulingGroups)|UpdateSchedulingGroups|[Parameters](#Parametersteams.scheduleUpdateSchedulingGroups)|Not Found|
|[az teams teamsschedule update-shift](#teams.scheduleUpdateShifts)|UpdateShifts|[Parameters](#Parametersteams.scheduleUpdateShifts)|Not Found|
|[az teams teamsschedule update-swap-shift-change-request](#teams.scheduleUpdateSwapShiftsChangeRequests)|UpdateSwapShiftsChangeRequests|[Parameters](#Parametersteams.scheduleUpdateSwapShiftsChangeRequests)|Not Found|
|[az teams teamsschedule update-time-off](#teams.scheduleUpdateTimesOff)|UpdateTimesOff|[Parameters](#Parametersteams.scheduleUpdateTimesOff)|Not Found|
|[az teams teamsschedule update-time-off-reason](#teams.scheduleUpdateTimeOffReasons)|UpdateTimeOffReasons|[Parameters](#Parametersteams.scheduleUpdateTimeOffReasons)|Not Found|
|[az teams teamsschedule update-time-off-request](#teams.scheduleUpdateTimeOffRequests)|UpdateTimeOffRequests|[Parameters](#Parametersteams.scheduleUpdateTimeOffRequests)|Not Found|

### <a name="CommandsInteams.team">Commands in `az teams teamsteam` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams teamsteam create-team](#teams.teamCreateTeam)|CreateTeam|[Parameters](#Parametersteams.teamCreateTeam)|Not Found|
|[az teams teamsteam delete-team](#teams.teamDeleteTeam)|DeleteTeam|[Parameters](#Parametersteams.teamDeleteTeam)|Not Found|
|[az teams teamsteam list-team](#teams.teamListTeam)|ListTeam|[Parameters](#Parametersteams.teamListTeam)|Not Found|
|[az teams teamsteam show-team](#teams.teamGetTeam)|GetTeam|[Parameters](#Parametersteams.teamGetTeam)|Not Found|
|[az teams teamsteam update-team](#teams.teamUpdateTeam)|UpdateTeam|[Parameters](#Parametersteams.teamUpdateTeam)|Not Found|

### <a name="CommandsInteamwork.teamwork">Commands in `az teams teamwork` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams teamwork show-teamwork](#teamwork.teamworkGetTeamwork)|GetTeamwork|[Parameters](#Parametersteamwork.teamworkGetTeamwork)|Not Found|
|[az teams teamwork update-teamwork](#teamwork.teamworkUpdateTeamwork)|UpdateTeamwork|[Parameters](#Parametersteamwork.teamworkUpdateTeamwork)|Not Found|

### <a name="CommandsInteamwork">Commands in `az teams teamwork` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams teamwork create-workforce-integration](#teamworkCreateWorkforceIntegrations)|CreateWorkforceIntegrations|[Parameters](#ParametersteamworkCreateWorkforceIntegrations)|Not Found|
|[az teams teamwork delete-workforce-integration](#teamworkDeleteWorkforceIntegrations)|DeleteWorkforceIntegrations|[Parameters](#ParametersteamworkDeleteWorkforceIntegrations)|Not Found|
|[az teams teamwork list-workforce-integration](#teamworkListWorkforceIntegrations)|ListWorkforceIntegrations|[Parameters](#ParametersteamworkListWorkforceIntegrations)|Not Found|
|[az teams teamwork show-workforce-integration](#teamworkGetWorkforceIntegrations)|GetWorkforceIntegrations|[Parameters](#ParametersteamworkGetWorkforceIntegrations)|Not Found|
|[az teams teamwork update-workforce-integration](#teamworkUpdateWorkforceIntegrations)|UpdateWorkforceIntegrations|[Parameters](#ParametersteamworkUpdateWorkforceIntegrations)|Not Found|

### <a name="CommandsInusers">Commands in `az teams user` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az teams user create-joined-team](#usersCreateJoinedTeams)|CreateJoinedTeams|[Parameters](#ParametersusersCreateJoinedTeams)|Not Found|
|[az teams user delete-joined-team](#usersDeleteJoinedTeams)|DeleteJoinedTeams|[Parameters](#ParametersusersDeleteJoinedTeams)|Not Found|
|[az teams user list-joined-team](#usersListJoinedTeams)|ListJoinedTeams|[Parameters](#ParametersusersListJoinedTeams)|Not Found|
|[az teams user show-joined-team](#usersGetJoinedTeams)|GetJoinedTeams|[Parameters](#ParametersusersGetJoinedTeams)|Not Found|
|[az teams user update-joined-team](#usersUpdateJoinedTeams)|UpdateJoinedTeams|[Parameters](#ParametersusersUpdateJoinedTeams)|Not Found|


## COMMAND DETAILS

### group `az teams chat`
#### <a name="chatsgetAllMessages">Command `az teams chat show-all-message`</a>

##### <a name="ParameterschatsgetAllMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
### group `az teams chatschat`
#### <a name="chats.chatCreateChat">Command `az teams chatschat create-chat`</a>

##### <a name="Parameterschats.chatCreateChat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|

#### <a name="chats.chatDeleteChat">Command `az teams chatschat delete-chat`</a>

##### <a name="Parameterschats.chatDeleteChat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="chats.chatListChat">Command `az teams chatschat list-chat`</a>

##### <a name="Parameterschats.chatListChat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chats.chatGetChat">Command `az teams chatschat show-chat`</a>

##### <a name="Parameterschats.chatGetChat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="chats.chatUpdateChat">Command `az teams chatschat update-chat`</a>

##### <a name="Parameterschats.chatUpdateChat">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--chat-id**|string|key: id of chat|chat_id|chat-id|
|**--id**|string|Read-only.|id|id|

### group `az teams group`
#### <a name="groupsDeleteTeam">Command `az teams group delete-team`</a>

##### <a name="ParametersgroupsDeleteTeam">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="groupsGetTeam">Command `az teams group show-team`</a>

##### <a name="ParametersgroupsGetTeam">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string|key: id of group|group_id|group-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="groupsUpdateTeam">Command `az teams group update-team`</a>

##### <a name="ParametersgroupsUpdateTeam">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--id1**|string|Read-only.|id1|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--assigned-labels**|array|The list of sensitivity label pairs (label ID, label name) associated with an Microsoft 365 group. Returned only on $select. Read-only.|assigned_labels|assignedLabels|
|**--assigned-licenses**|array|The licenses that are assigned to the group. Returned only on $select. Read-only.|assigned_licenses|assignedLicenses|
|**--microsoft-graph-group-classification**|string|Describes a classification for the group (such as low, medium or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default.|microsoft_graph_group_classification|classification|
|**--created-date-time**|date-time|Timestamp of when the group was created. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|created_date_time|createdDateTime|
|**--microsoft-graph-group-description**|string|An optional description for the group. Returned by default.|microsoft_graph_group_description|description|
|**--microsoft-graph-group-display-name**|string|The display name for the group. This property is required when a group is created and cannot be cleared during updates. Returned by default. Supports $filter and $orderby.|microsoft_graph_group_display_name|displayName|
|**--expiration-date-time**|date-time|Timestamp of when the group is set to expire. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|expiration_date_time|expirationDateTime|
|**--group-types**|array|Specifies the group type and its membership.  If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static.  Returned by default. Supports $filter.|group_types|groupTypes|
|**--has-members-with-license-errors**|boolean|Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an example.|has_members_with_license_errors|hasMembersWithLicenseErrors|
|**--license-processing-state**|object|licenseProcessingState|license_processing_state|licenseProcessingState|
|**--mail**|string|The SMTP address for the group, for example, 'serviceadmins@contoso.onmicrosoft.com'. Returned by default. Read-only. Supports $filter.|mail|mail|
|**--mail-enabled**|boolean|Specifies whether the group is mail-enabled. Returned by default.|mail_enabled|mailEnabled|
|**--mail-nickname**|string|The mail alias for the group, unique in the organization. This property must be specified when a group is created. Returned by default. Supports $filter.|mail_nickname|mailNickname|
|**--membership-rule**|string|The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default.|membership_rule|membershipRule|
|**--membership-rule-processing-state**|string|Indicates whether the dynamic membership processing is on or paused. Possible values are 'On' or 'Paused'. Returned by default.|membership_rule_processing_state|membershipRuleProcessingState|
|**--on-premises-domain-name**|string|Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_domain_name|onPremisesDomainName|
|**--on-premises-last-sync-date-time**|date-time|Indicates the last time at which the group was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only. Supports $filter.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-net-bios-name**|string|Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_net_bios_name|onPremisesNetBiosName|
|**--on-premises-provisioning-errors**|array|Errors when using Microsoft synchronization product during provisioning. Returned by default.|on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--on-premises-sam-account-name**|string|Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_sam_account_name|onPremisesSamAccountName|
|**--on-premises-security-identifier**|string|Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Returned by default. Read-only.|on_premises_security_identifier|onPremisesSecurityIdentifier|
|**--on-premises-sync-enabled**|boolean|true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--preferred-data-location**|string|The preferred data location for the group. For more information, see  OneDrive Online Multi-Geo. Returned by default.|preferred_data_location|preferredDataLocation|
|**--preferred-language**|string|The preferred language for an Microsoft 365 group. Should follow ISO 639-1 Code; for example 'en-US'. Returned by default.|preferred_language|preferredLanguage|
|**--proxy-addresses**|array|Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter.|proxy_addresses|proxyAddresses|
|**--renewed-date-time**|date-time|Timestamp of when the group was last renewed. This cannot be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|renewed_date_time|renewedDateTime|
|**--security-enabled**|boolean|Specifies whether the group is a security group. Returned by default. Supports $filter.|security_enabled|securityEnabled|
|**--security-identifier**|string|Security identifier of the group, used in Windows scenarios. Returned by default.|security_identifier|securityIdentifier|
|**--theme**|string|Specifies an Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange or Red. Returned by default.|theme|theme|
|**--microsoft-graph-group-visibility**|string|Specifies the visibility of a Microsoft 365 group. Possible values are: Private, Public, or Hiddenmembership; blank values are treated as public.  See group visibility options to learn more.Visibility can be set only when a group is created; it is not editable.Visibility is supported only for unified groups; it is not supported for security groups. Returned by default.|microsoft_graph_group_visibility|visibility|
|**--allow-external-senders**|boolean|Indicates if people external to the organization can send messages to the group. Default value is false. Returned only on $select.|allow_external_senders|allowExternalSenders|
|**--auto-subscribe-new-members**|boolean|Indicates if new members added to the group will be auto-subscribed to receive email notifications. You can set this property in a PATCH request for the group; do not set it in the initial POST request that creates the group. Default value is false. Returned only on $select.|auto_subscribe_new_members|autoSubscribeNewMembers|
|**--hide-from-address-lists**|boolean|True if the group is not displayed in certain parts of the Outlook UI: the Address Book, address lists for selecting message recipients, and the Browse Groups dialog for searching groups; otherwise, false. Default value is false. Returned only on $select.|hide_from_address_lists|hideFromAddressLists|
|**--hide-from-outlook-clients**|boolean|True if the group is not displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. Default value is false. Returned only on $select.|hide_from_outlook_clients|hideFromOutlookClients|
|**--is-subscribed-by-mail**|boolean|Indicates whether the signed-in user is subscribed to receive email conversations. Default value is true. Returned only on $select.|is_subscribed_by_mail|isSubscribedByMail|
|**--unseen-count**|integer|Count of conversations that have received new posts since the signed-in user last visited the group. Returned only on $select.|unseen_count|unseenCount|
|**--group-is-archived**|boolean||is_archived|isArchived|
|**--app-role-assignments**|array||app_role_assignments|appRoleAssignments|
|**--created-on-behalf-of**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|created_on_behalf_of|createdOnBehalfOf|
|**--member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--microsoft-graph-group-members**|array|Users and groups that are members of this group. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups) Nullable.|microsoft_graph_group_members|members|
|**--members-with-license-errors**|array|A list of group members with license errors from this group-based license assignment. Read-only.|members_with_license_errors|membersWithLicenseErrors|
|**--owners**|array|The owners of the group. The owners are a set of non-admin users who are allowed to modify this object. Limited to 100 owners. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups). Nullable.|owners|owners|
|**--settings**|array|Read-only. Nullable.|settings|settings|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--transitive-members**|array||transitive_members|transitiveMembers|
|**--accepted-senders**|array|The list of users or groups that are allowed to create post's or calendar events in this group. If this list is non-empty then only users or groups listed here are allowed to post.|accepted_senders|acceptedSenders|
|**--calendar**|object|calendar|calendar|calendar|
|**--calendar-view**|array|The calendar view for the calendar. Read-only.|calendar_view|calendarView|
|**--conversations**|array|The group's conversations.|conversations|conversations|
|**--events**|array|The group's calendar events.|events|events|
|**--photo**|object|profilePhoto|photo|photo|
|**--photos**|array|The profile photos owned by the group. Read-only. Nullable.|photos|photos|
|**--rejected-senders**|array|The list of users or groups that are not allowed to create posts or calendar events in this group. Nullable|rejected_senders|rejectedSenders|
|**--threads**|array|The group's conversation threads. Nullable.|threads|threads|
|**--drive**|object|drive|drive|drive|
|**--drives**|array|The group's drives. Read-only.|drives|drives|
|**--sites**|array|The list of SharePoint sites in this group. Access the default site with /sites/root.|sites|sites|
|**--extensions**|array|The collection of open extensions defined for the group. Read-only. Nullable.|extensions|extensions|
|**--group-lifecycle-policies**|array|The collection of lifecycle policies for this group. Read-only. Nullable.|group_lifecycle_policies|groupLifecyclePolicies|
|**--planner**|object|plannerGroup|planner|planner|
|**--onenote**|object|onenote|onenote|onenote|
|**--team**|object|team|team|team|
|**--id2**|string|Read-only.|id2|id|
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

### group `az teams team`
#### <a name="teamsarchive">Command `az teams team archive`</a>

##### <a name="Parametersteamsarchive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--should-set-spo-site-read-only-for-members**|boolean||should_set_spo_site_read_only_for_members|shouldSetSpoSiteReadOnlyForMembers|

#### <a name="teamsclone">Command `az teams team clone`</a>

##### <a name="Parametersteamsclone">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--display-name**|string||display_name|displayName|
|**--description**|string||description|description|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--classification**|string||classification|classification|
|**--visibility**|choice||visibility|visibility|
|**--parts-to-clone**|choice||parts_to_clone|partsToClone|

#### <a name="teamsCreateChannels">Command `az teams team create-channel`</a>

##### <a name="ParametersteamsCreateChannels">Parameters</a> 
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

#### <a name="teamsCreateInstalledApps">Command `az teams team create-installed-app`</a>

##### <a name="ParametersteamsCreateInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--teams-app-definition**|object|teamsAppDefinition|teams_app_definition|teamsAppDefinition|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

#### <a name="teamsCreateMembers">Command `az teams team create-member`</a>

##### <a name="ParametersteamsCreateMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

#### <a name="teamsCreateOperations">Command `az teams team create-operation`</a>

##### <a name="ParametersteamsCreateOperations">Parameters</a> 
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

#### <a name="teamsDeleteChannels">Command `az teams team delete-channel`</a>

##### <a name="ParametersteamsDeleteChannels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsDeleteInstalledApps">Command `az teams team delete-installed-app`</a>

##### <a name="ParametersteamsDeleteInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsDeleteMembers">Command `az teams team delete-member`</a>

##### <a name="ParametersteamsDeleteMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsDeleteOperations">Command `az teams team delete-operation`</a>

##### <a name="ParametersteamsDeleteOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-async-operation-id**|string|key: id of teamsAsyncOperation|teams_async_operation_id|teamsAsyncOperation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsDeletePrimaryChannel">Command `az teams team delete-primary-channel`</a>

##### <a name="ParametersteamsDeletePrimaryChannel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsDeleteRefGroup">Command `az teams team delete-ref-group`</a>

##### <a name="ParametersteamsDeleteRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsDeleteRefTemplate">Command `az teams team delete-ref-template`</a>

##### <a name="ParametersteamsDeleteRefTemplate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsDeleteSchedule">Command `az teams team delete-schedule`</a>

##### <a name="ParametersteamsDeleteSchedule">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamsListChannels">Command `az teams team list-channel`</a>

##### <a name="ParametersteamsListChannels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsListInstalledApps">Command `az teams team list-installed-app`</a>

##### <a name="ParametersteamsListInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsListMembers">Command `az teams team list-member`</a>

##### <a name="ParametersteamsListMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsListOperations">Command `az teams team list-operation`</a>

##### <a name="ParametersteamsListOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsSetRefGroup">Command `az teams team set-ref-group`</a>

##### <a name="ParametersteamsSetRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="teamsSetRefTemplate">Command `az teams team set-ref-template`</a>

##### <a name="ParametersteamsSetRefTemplate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="teamsgetAllMessages">Command `az teams team show-all-message`</a>

##### <a name="ParametersteamsgetAllMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="teamsGetChannels">Command `az teams team show-channel`</a>

##### <a name="ParametersteamsGetChannels">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsGetGroup">Command `az teams team show-group`</a>

##### <a name="ParametersteamsGetGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsGetInstalledApps">Command `az teams team show-installed-app`</a>

##### <a name="ParametersteamsGetInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsGetMembers">Command `az teams team show-member`</a>

##### <a name="ParametersteamsGetMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsGetOperations">Command `az teams team show-operation`</a>

##### <a name="ParametersteamsGetOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-async-operation-id**|string|key: id of teamsAsyncOperation|teams_async_operation_id|teamsAsyncOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsGetPrimaryChannel">Command `az teams team show-primary-channel`</a>

##### <a name="ParametersteamsGetPrimaryChannel">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsGetRefGroup">Command `az teams team show-ref-group`</a>

##### <a name="ParametersteamsGetRefGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|

#### <a name="teamsGetRefTemplate">Command `az teams team show-ref-template`</a>

##### <a name="ParametersteamsGetRefTemplate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|

#### <a name="teamsGetSchedule">Command `az teams team show-schedule`</a>

##### <a name="ParametersteamsGetSchedule">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsGetTemplate">Command `az teams team show-template`</a>

##### <a name="ParametersteamsGetTemplate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamsunarchive">Command `az teams team unarchive`</a>

##### <a name="Parametersteamsunarchive">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|

#### <a name="teamsUpdateChannels">Command `az teams team update-channel`</a>

##### <a name="ParametersteamsUpdateChannels">Parameters</a> 
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

#### <a name="teamsUpdateInstalledApps">Command `az teams team update-installed-app`</a>

##### <a name="ParametersteamsUpdateInstalledApps">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--id**|string|Read-only.|id|id|
|**--teams-app-definition**|object|teamsAppDefinition|teams_app_definition|teamsAppDefinition|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

#### <a name="teamsUpdateMembers">Command `az teams team update-member`</a>

##### <a name="ParametersteamsUpdateMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

#### <a name="teamsUpdateOperations">Command `az teams team update-operation`</a>

##### <a name="ParametersteamsUpdateOperations">Parameters</a> 
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

#### <a name="teamsUpdatePrimaryChannel">Command `az teams team update-primary-channel`</a>

##### <a name="ParametersteamsUpdatePrimaryChannel">Parameters</a> 
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

#### <a name="teamsUpdateSchedule">Command `az teams team update-schedule`</a>

##### <a name="ParametersteamsUpdateSchedule">Parameters</a> 
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

### group `az teams teamschannel`
#### <a name="teams.channelsCreateMembers">Command `az teams teamschannel create-member`</a>

##### <a name="Parametersteams.channelsCreateMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

#### <a name="teams.channelsCreateMessages">Command `az teams teamschannel create-message`</a>

##### <a name="Parametersteams.channelsCreateMessages">Parameters</a> 
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
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string||justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="teams.channelsCreateTabs">Command `az teams teamschannel create-tab`</a>

##### <a name="Parametersteams.channelsCreateTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|teamsTabConfiguration|configuration|configuration|
|**--display-name**|string|Name of the tab.|display_name|displayName|
|**--web-url**|string|Deep link URL of the tab instance. Read only.|web_url|webUrl|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

#### <a name="teams.channelsDeleteFilesFolder">Command `az teams teamschannel delete-file-folder`</a>

##### <a name="Parametersteams.channelsDeleteFilesFolder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.channelsDeleteMembers">Command `az teams teamschannel delete-member`</a>

##### <a name="Parametersteams.channelsDeleteMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.channelsDeleteMessages">Command `az teams teamschannel delete-message`</a>

##### <a name="Parametersteams.channelsDeleteMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.channelsDeleteTabs">Command `az teams teamschannel delete-tab`</a>

##### <a name="Parametersteams.channelsDeleteTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.channelsListMembers">Command `az teams teamschannel list-member`</a>

##### <a name="Parametersteams.channelsListMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channelsListMessages">Command `az teams teamschannel list-message`</a>

##### <a name="Parametersteams.channelsListMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channelsListTabs">Command `az teams teamschannel list-tab`</a>

##### <a name="Parametersteams.channelsListTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channelsGetFilesFolder">Command `az teams teamschannel show-file-folder`</a>

##### <a name="Parametersteams.channelsGetFilesFolder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channelsGetMembers">Command `az teams teamschannel show-member`</a>

##### <a name="Parametersteams.channelsGetMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channelsGetMessages">Command `az teams teamschannel show-message`</a>

##### <a name="Parametersteams.channelsGetMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channelsGetTabs">Command `az teams teamschannel show-tab`</a>

##### <a name="Parametersteams.channelsGetTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channelsUpdateFilesFolder">Command `az teams teamschannel update-file-folder`</a>

##### <a name="Parametersteams.channelsUpdateFilesFolder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="teams.channelsUpdateMembers">Command `az teams teamschannel update-member`</a>

##### <a name="Parametersteams.channelsUpdateMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

#### <a name="teams.channelsUpdateMessages">Command `az teams teamschannel update-message`</a>

##### <a name="Parametersteams.channelsUpdateMessages">Parameters</a> 
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
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string||justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="teams.channelsUpdateTabs">Command `az teams teamschannel update-tab`</a>

##### <a name="Parametersteams.channelsUpdateTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|teamsTabConfiguration|configuration|configuration|
|**--display-name**|string|Name of the tab.|display_name|displayName|
|**--web-url**|string|Deep link URL of the tab instance. Read only.|web_url|webUrl|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

### group `az teams teamschannelsmessage`
#### <a name="teams.channels.messagesCreateHostedContents">Command `az teams teamschannelsmessage create-hosted-content`</a>

##### <a name="Parametersteams.channels.messagesCreateHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|

#### <a name="teams.channels.messagesCreateReplies">Command `az teams teamschannelsmessage create-reply`</a>

##### <a name="Parametersteams.channels.messagesCreateReplies">Parameters</a> 
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
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string||justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="teams.channels.messagesDeleteHostedContents">Command `az teams teamschannelsmessage delete-hosted-content`</a>

##### <a name="Parametersteams.channels.messagesDeleteHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.channels.messagesDeleteReplies">Command `az teams teamschannelsmessage delete-reply`</a>

##### <a name="Parametersteams.channels.messagesDeleteReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.channels.messagesListHostedContents">Command `az teams teamschannelsmessage list-hosted-content`</a>

##### <a name="Parametersteams.channels.messagesListHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channels.messagesListReplies">Command `az teams teamschannelsmessage list-reply`</a>

##### <a name="Parametersteams.channels.messagesListReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channels.messagesGetHostedContents">Command `az teams teamschannelsmessage show-hosted-content`</a>

##### <a name="Parametersteams.channels.messagesGetHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channels.messagesGetReplies">Command `az teams teamschannelsmessage show-reply`</a>

##### <a name="Parametersteams.channels.messagesGetReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.channels.messagesUpdateHostedContents">Command `az teams teamschannelsmessage update-hosted-content`</a>

##### <a name="Parametersteams.channels.messagesUpdateHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--id**|string|Read-only.|id|id|

#### <a name="teams.channels.messagesUpdateReplies">Command `az teams teamschannelsmessage update-reply`</a>

##### <a name="Parametersteams.channels.messagesUpdateReplies">Parameters</a> 
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
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string||justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

### group `az teams teamschannelstab`
#### <a name="teams.channels.tabsDeleteRefTeamsApp">Command `az teams teamschannelstab delete-ref-team-app`</a>

##### <a name="Parametersteams.channels.tabsDeleteRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.channels.tabsSetRefTeamsApp">Command `az teams teamschannelstab set-ref-team-app`</a>

##### <a name="Parametersteams.channels.tabsSetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="teams.channels.tabsGetRefTeamsApp">Command `az teams teamschannelstab show-ref-team-app`</a>

##### <a name="Parametersteams.channels.tabsGetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|

#### <a name="teams.channels.tabsGetTeamsApp">Command `az teams teamschannelstab show-team-app`</a>

##### <a name="Parametersteams.channels.tabsGetTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--channel-id**|string|key: id of channel|channel_id|channel-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### group `az teams teamsinstalledapp`
#### <a name="teams.installedAppsDeleteRefTeamsApp">Command `az teams teamsinstalledapp delete-ref-team-app`</a>

##### <a name="Parametersteams.installedAppsDeleteRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.installedAppsDeleteRefTeamsAppDefinition">Command `az teams teamsinstalledapp delete-ref-team-app-definition`</a>

##### <a name="Parametersteams.installedAppsDeleteRefTeamsAppDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.installedAppsSetRefTeamsApp">Command `az teams teamsinstalledapp set-ref-team-app`</a>

##### <a name="Parametersteams.installedAppsSetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="teams.installedAppsSetRefTeamsAppDefinition">Command `az teams teamsinstalledapp set-ref-team-app-definition`</a>

##### <a name="Parametersteams.installedAppsSetRefTeamsAppDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="teams.installedAppsGetRefTeamsApp">Command `az teams teamsinstalledapp show-ref-team-app`</a>

##### <a name="Parametersteams.installedAppsGetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|

#### <a name="teams.installedAppsGetRefTeamsAppDefinition">Command `az teams teamsinstalledapp show-ref-team-app-definition`</a>

##### <a name="Parametersteams.installedAppsGetRefTeamsAppDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|

#### <a name="teams.installedAppsGetTeamsApp">Command `az teams teamsinstalledapp show-team-app`</a>

##### <a name="Parametersteams.installedAppsGetTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.installedAppsGetTeamsAppDefinition">Command `az teams teamsinstalledapp show-team-app-definition`</a>

##### <a name="Parametersteams.installedAppsGetTeamsAppDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.installedAppsupgrade">Command `az teams teamsinstalledapp upgrade`</a>

##### <a name="Parametersteams.installedAppsupgrade">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-app-installation-id**|string|key: id of teamsAppInstallation|teams_app_installation_id|teamsAppInstallation-id|

### group `az teams teamsprimarychannel`
#### <a name="teams.primaryChannelCreateMembers">Command `az teams teamsprimarychannel create-member`</a>

##### <a name="Parametersteams.primaryChannelCreateMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

#### <a name="teams.primaryChannelCreateMessages">Command `az teams teamsprimarychannel create-message`</a>

##### <a name="Parametersteams.primaryChannelCreateMessages">Parameters</a> 
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
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string||justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="teams.primaryChannelCreateTabs">Command `az teams teamsprimarychannel create-tab`</a>

##### <a name="Parametersteams.primaryChannelCreateTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|teamsTabConfiguration|configuration|configuration|
|**--display-name**|string|Name of the tab.|display_name|displayName|
|**--web-url**|string|Deep link URL of the tab instance. Read only.|web_url|webUrl|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

#### <a name="teams.primaryChannelDeleteFilesFolder">Command `az teams teamsprimarychannel delete-file-folder`</a>

##### <a name="Parametersteams.primaryChannelDeleteFilesFolder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.primaryChannelDeleteMembers">Command `az teams teamsprimarychannel delete-member`</a>

##### <a name="Parametersteams.primaryChannelDeleteMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.primaryChannelDeleteMessages">Command `az teams teamsprimarychannel delete-message`</a>

##### <a name="Parametersteams.primaryChannelDeleteMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.primaryChannelDeleteTabs">Command `az teams teamsprimarychannel delete-tab`</a>

##### <a name="Parametersteams.primaryChannelDeleteTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.primaryChannelListMembers">Command `az teams teamsprimarychannel list-member`</a>

##### <a name="Parametersteams.primaryChannelListMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannelListMessages">Command `az teams teamsprimarychannel list-message`</a>

##### <a name="Parametersteams.primaryChannelListMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannelListTabs">Command `az teams teamsprimarychannel list-tab`</a>

##### <a name="Parametersteams.primaryChannelListTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannelGetFilesFolder">Command `az teams teamsprimarychannel show-file-folder`</a>

##### <a name="Parametersteams.primaryChannelGetFilesFolder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannelGetMembers">Command `az teams teamsprimarychannel show-member`</a>

##### <a name="Parametersteams.primaryChannelGetMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannelGetMessages">Command `az teams teamsprimarychannel show-message`</a>

##### <a name="Parametersteams.primaryChannelGetMessages">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannelGetTabs">Command `az teams teamsprimarychannel show-tab`</a>

##### <a name="Parametersteams.primaryChannelGetTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannelUpdateFilesFolder">Command `az teams teamsprimarychannel update-file-folder`</a>

##### <a name="Parametersteams.primaryChannelUpdateFilesFolder">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="teams.primaryChannelUpdateMembers">Command `az teams teamsprimarychannel update-member`</a>

##### <a name="Parametersteams.primaryChannelUpdateMembers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--conversation-member-id**|string|key: id of conversationMember|conversation_member_id|conversationMember-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string|The display name of the user.|display_name|displayName|
|**--roles**|array|The roles for that user.|roles|roles|

#### <a name="teams.primaryChannelUpdateMessages">Command `az teams teamsprimarychannel update-message`</a>

##### <a name="Parametersteams.primaryChannelUpdateMessages">Parameters</a> 
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
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string||justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="teams.primaryChannelUpdateTabs">Command `az teams teamsprimarychannel update-tab`</a>

##### <a name="Parametersteams.primaryChannelUpdateTabs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--id**|string|Read-only.|id|id|
|**--configuration**|object|teamsTabConfiguration|configuration|configuration|
|**--display-name**|string|Name of the tab.|display_name|displayName|
|**--web-url**|string|Deep link URL of the tab instance. Read only.|web_url|webUrl|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--microsoft-graph-teams-app-display-name**|string|The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.|microsoft_graph_teams_app_display_name|displayName|
|**--distribution-method**|choice||distribution_method|distributionMethod|
|**--external-id**|string|The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.|external_id|externalId|
|**--app-definitions**|array|The details for each version of the app.|app_definitions|appDefinitions|

### group `az teams teamsprimarychannelmessage`
#### <a name="teams.primaryChannel.messagesCreateHostedContents">Command `az teams teamsprimarychannelmessage create-hosted-content`</a>

##### <a name="Parametersteams.primaryChannel.messagesCreateHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--id**|string|Read-only.|id|id|

#### <a name="teams.primaryChannel.messagesCreateReplies">Command `az teams teamsprimarychannelmessage create-reply`</a>

##### <a name="Parametersteams.primaryChannel.messagesCreateReplies">Parameters</a> 
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
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string||justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

#### <a name="teams.primaryChannel.messagesDeleteHostedContents">Command `az teams teamsprimarychannelmessage delete-hosted-content`</a>

##### <a name="Parametersteams.primaryChannel.messagesDeleteHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.primaryChannel.messagesDeleteReplies">Command `az teams teamsprimarychannelmessage delete-reply`</a>

##### <a name="Parametersteams.primaryChannel.messagesDeleteReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.primaryChannel.messagesListHostedContents">Command `az teams teamsprimarychannelmessage list-hosted-content`</a>

##### <a name="Parametersteams.primaryChannel.messagesListHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannel.messagesListReplies">Command `az teams teamsprimarychannelmessage list-reply`</a>

##### <a name="Parametersteams.primaryChannel.messagesListReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannel.messagesGetHostedContents">Command `az teams teamsprimarychannelmessage show-hosted-content`</a>

##### <a name="Parametersteams.primaryChannel.messagesGetHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannel.messagesGetReplies">Command `az teams teamsprimarychannelmessage show-reply`</a>

##### <a name="Parametersteams.primaryChannel.messagesGetReplies">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-id1**|string|key: id of chatMessage|chat_message_id1|chatMessage-id1|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.primaryChannel.messagesUpdateHostedContents">Command `az teams teamsprimarychannelmessage update-hosted-content`</a>

##### <a name="Parametersteams.primaryChannel.messagesUpdateHostedContents">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--chat-message-id**|string|key: id of chatMessage|chat_message_id|chatMessage-id|
|**--chat-message-hosted-content-id**|string|key: id of chatMessageHostedContent|chat_message_hosted_content_id|chatMessageHostedContent-id|
|**--id**|string|Read-only.|id|id|

#### <a name="teams.primaryChannel.messagesUpdateReplies">Command `az teams teamsprimarychannelmessage update-reply`</a>

##### <a name="Parametersteams.primaryChannel.messagesUpdateReplies">Parameters</a> 
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
|**--dlp-action**|choice||dlp_action|dlpAction|
|**--justification-text**|string||justification_text|justificationText|
|**--policy-tip**|object|chatMessagePolicyViolationPolicyTip|policy_tip|policyTip|
|**--user-action**|choice||user_action|userAction|
|**--verdict-details**|choice||verdict_details|verdictDetails|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|

### group `az teams teamsprimarychanneltab`
#### <a name="teams.primaryChannel.tabsDeleteRefTeamsApp">Command `az teams teamsprimarychanneltab delete-ref-team-app`</a>

##### <a name="Parametersteams.primaryChannel.tabsDeleteRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.primaryChannel.tabsSetRefTeamsApp">Command `az teams teamsprimarychanneltab set-ref-team-app`</a>

##### <a name="Parametersteams.primaryChannel.tabsSetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="teams.primaryChannel.tabsGetRefTeamsApp">Command `az teams teamsprimarychanneltab show-ref-team-app`</a>

##### <a name="Parametersteams.primaryChannel.tabsGetRefTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|

#### <a name="teams.primaryChannel.tabsGetTeamsApp">Command `az teams teamsprimarychanneltab show-team-app`</a>

##### <a name="Parametersteams.primaryChannel.tabsGetTeamsApp">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--teams-tab-id**|string|key: id of teamsTab|teams_tab_id|teamsTab-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### group `az teams teamsschedule`
#### <a name="teams.scheduleCreateOfferShiftRequests">Command `az teams teamsschedule create-offer-shift-request`</a>

##### <a name="Parametersteams.scheduleCreateOfferShiftRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
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

#### <a name="teams.scheduleCreateOpenShifts">Command `az teams teamsschedule create-open-shift`</a>

##### <a name="Parametersteams.scheduleCreateOpenShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--draft-open-shift**|object|openShiftItem|draft_open_shift|draftOpenShift|
|**--scheduling-group-id**|string|ID for the scheduling group that the open shift belongs to.|scheduling_group_id|schedulingGroupId|
|**--shared-open-shift**|object|openShiftItem|shared_open_shift|sharedOpenShift|

#### <a name="teams.scheduleCreateOpenShiftChangeRequests">Command `az teams teamsschedule create-open-shift-change-request`</a>

##### <a name="Parametersteams.scheduleCreateOpenShiftChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--open-shift-id**|string|ID for the open shift.|open_shift_id|openShiftId|

#### <a name="teams.scheduleCreateSchedulingGroups">Command `az teams teamsschedule create-scheduling-group`</a>

##### <a name="Parametersteams.scheduleCreateSchedulingGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--display-name**|string|The display name for the schedulingGroup. Required.|display_name|displayName|
|**--is-active**|boolean|Indicates whether the schedulingGroup can be used when creating new entities or updating existing ones. Required.|is_active|isActive|
|**--user-ids**|array|The list of user IDs that are a member of the schedulingGroup. Required.|user_ids|userIds|

#### <a name="teams.scheduleCreateShifts">Command `az teams teamsschedule create-shift`</a>

##### <a name="Parametersteams.scheduleCreateShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--body**|object|New navigation property|body|body|

#### <a name="teams.scheduleCreateSwapShiftsChangeRequests">Command `az teams teamsschedule create-swap-shift-change-request`</a>

##### <a name="Parametersteams.scheduleCreateSwapShiftsChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
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

#### <a name="teams.scheduleCreateTimesOff">Command `az teams teamsschedule create-time-off`</a>

##### <a name="Parametersteams.scheduleCreateTimesOff">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--draft-time-off**|object|timeOffItem|draft_time_off|draftTimeOff|
|**--shared-time-off**|object|timeOffItem|shared_time_off|sharedTimeOff|
|**--user-id**|string|ID of the user assigned to the timeOff. Required.|user_id|userId|

#### <a name="teams.scheduleCreateTimeOffReasons">Command `az teams teamsschedule create-time-off-reason`</a>

##### <a name="Parametersteams.scheduleCreateTimeOffReasons">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--display-name**|string|The name of the timeOffReason. Required.|display_name|displayName|
|**--icon-type**|choice||icon_type|iconType|
|**--is-active**|boolean|Indicates whether the timeOffReason can be used when creating new entities or updating existing ones. Required.|is_active|isActive|

#### <a name="teams.scheduleCreateTimeOffRequests">Command `az teams teamsschedule create-time-off-request`</a>

##### <a name="Parametersteams.scheduleCreateTimeOffRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
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

#### <a name="teams.scheduleDeleteOfferShiftRequests">Command `az teams teamsschedule delete-offer-shift-request`</a>

##### <a name="Parametersteams.scheduleDeleteOfferShiftRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--offer-shift-request-id**|string|key: id of offerShiftRequest|offer_shift_request_id|offerShiftRequest-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteOpenShifts">Command `az teams teamsschedule delete-open-shift`</a>

##### <a name="Parametersteams.scheduleDeleteOpenShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-id**|string|key: id of openShift|open_shift_id|openShift-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteOpenShiftChangeRequests">Command `az teams teamsschedule delete-open-shift-change-request`</a>

##### <a name="Parametersteams.scheduleDeleteOpenShiftChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-change-request-id**|string|key: id of openShiftChangeRequest|open_shift_change_request_id|openShiftChangeRequest-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteSchedulingGroups">Command `az teams teamsschedule delete-scheduling-group`</a>

##### <a name="Parametersteams.scheduleDeleteSchedulingGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--scheduling-group-id**|string|key: id of schedulingGroup|scheduling_group_id|schedulingGroup-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteShifts">Command `az teams teamsschedule delete-shift`</a>

##### <a name="Parametersteams.scheduleDeleteShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--shift-id**|string|key: id of shift|shift_id|shift-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteSwapShiftsChangeRequests">Command `az teams teamsschedule delete-swap-shift-change-request`</a>

##### <a name="Parametersteams.scheduleDeleteSwapShiftsChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--swap-shifts-change-request-id**|string|key: id of swapShiftsChangeRequest|swap_shifts_change_request_id|swapShiftsChangeRequest-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteTimesOff">Command `az teams teamsschedule delete-time-off`</a>

##### <a name="Parametersteams.scheduleDeleteTimesOff">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-id**|string|key: id of timeOff|time_off_id|timeOff-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteTimeOffReasons">Command `az teams teamsschedule delete-time-off-reason`</a>

##### <a name="Parametersteams.scheduleDeleteTimeOffReasons">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-reason-id**|string|key: id of timeOffReason|time_off_reason_id|timeOffReason-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleDeleteTimeOffRequests">Command `az teams teamsschedule delete-time-off-request`</a>

##### <a name="Parametersteams.scheduleDeleteTimeOffRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-request-id**|string|key: id of timeOffRequest|time_off_request_id|timeOffRequest-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.scheduleListOfferShiftRequests">Command `az teams teamsschedule list-offer-shift-request`</a>

##### <a name="Parametersteams.scheduleListOfferShiftRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListOpenShifts">Command `az teams teamsschedule list-open-shift`</a>

##### <a name="Parametersteams.scheduleListOpenShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListOpenShiftChangeRequests">Command `az teams teamsschedule list-open-shift-change-request`</a>

##### <a name="Parametersteams.scheduleListOpenShiftChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListSchedulingGroups">Command `az teams teamsschedule list-scheduling-group`</a>

##### <a name="Parametersteams.scheduleListSchedulingGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListShifts">Command `az teams teamsschedule list-shift`</a>

##### <a name="Parametersteams.scheduleListShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListSwapShiftsChangeRequests">Command `az teams teamsschedule list-swap-shift-change-request`</a>

##### <a name="Parametersteams.scheduleListSwapShiftsChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListTimesOff">Command `az teams teamsschedule list-time-off`</a>

##### <a name="Parametersteams.scheduleListTimesOff">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListTimeOffReasons">Command `az teams teamsschedule list-time-off-reason`</a>

##### <a name="Parametersteams.scheduleListTimeOffReasons">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleListTimeOffRequests">Command `az teams teamsschedule list-time-off-request`</a>

##### <a name="Parametersteams.scheduleListTimeOffRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleshare">Command `az teams teamsschedule share`</a>

##### <a name="Parametersteams.scheduleshare">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--notify-team**|boolean||notify_team|notifyTeam|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--end-date-time**|date-time||end_date_time|endDateTime|

#### <a name="teams.scheduleGetOfferShiftRequests">Command `az teams teamsschedule show-offer-shift-request`</a>

##### <a name="Parametersteams.scheduleGetOfferShiftRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--offer-shift-request-id**|string|key: id of offerShiftRequest|offer_shift_request_id|offerShiftRequest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetOpenShifts">Command `az teams teamsschedule show-open-shift`</a>

##### <a name="Parametersteams.scheduleGetOpenShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-id**|string|key: id of openShift|open_shift_id|openShift-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetOpenShiftChangeRequests">Command `az teams teamsschedule show-open-shift-change-request`</a>

##### <a name="Parametersteams.scheduleGetOpenShiftChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-change-request-id**|string|key: id of openShiftChangeRequest|open_shift_change_request_id|openShiftChangeRequest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetSchedulingGroups">Command `az teams teamsschedule show-scheduling-group`</a>

##### <a name="Parametersteams.scheduleGetSchedulingGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--scheduling-group-id**|string|key: id of schedulingGroup|scheduling_group_id|schedulingGroup-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetShifts">Command `az teams teamsschedule show-shift`</a>

##### <a name="Parametersteams.scheduleGetShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--shift-id**|string|key: id of shift|shift_id|shift-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetSwapShiftsChangeRequests">Command `az teams teamsschedule show-swap-shift-change-request`</a>

##### <a name="Parametersteams.scheduleGetSwapShiftsChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--swap-shifts-change-request-id**|string|key: id of swapShiftsChangeRequest|swap_shifts_change_request_id|swapShiftsChangeRequest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetTimesOff">Command `az teams teamsschedule show-time-off`</a>

##### <a name="Parametersteams.scheduleGetTimesOff">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-id**|string|key: id of timeOff|time_off_id|timeOff-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetTimeOffReasons">Command `az teams teamsschedule show-time-off-reason`</a>

##### <a name="Parametersteams.scheduleGetTimeOffReasons">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-reason-id**|string|key: id of timeOffReason|time_off_reason_id|timeOffReason-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleGetTimeOffRequests">Command `az teams teamsschedule show-time-off-request`</a>

##### <a name="Parametersteams.scheduleGetTimeOffRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-request-id**|string|key: id of timeOffRequest|time_off_request_id|timeOffRequest-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.scheduleUpdateOfferShiftRequests">Command `az teams teamsschedule update-offer-shift-request`</a>

##### <a name="Parametersteams.scheduleUpdateOfferShiftRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--offer-shift-request-id**|string|key: id of offerShiftRequest|offer_shift_request_id|offerShiftRequest-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
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

#### <a name="teams.scheduleUpdateOpenShifts">Command `az teams teamsschedule update-open-shift`</a>

##### <a name="Parametersteams.scheduleUpdateOpenShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-id**|string|key: id of openShift|open_shift_id|openShift-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--draft-open-shift**|object|openShiftItem|draft_open_shift|draftOpenShift|
|**--scheduling-group-id**|string|ID for the scheduling group that the open shift belongs to.|scheduling_group_id|schedulingGroupId|
|**--shared-open-shift**|object|openShiftItem|shared_open_shift|sharedOpenShift|

#### <a name="teams.scheduleUpdateOpenShiftChangeRequests">Command `az teams teamsschedule update-open-shift-change-request`</a>

##### <a name="Parametersteams.scheduleUpdateOpenShiftChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--open-shift-change-request-id**|string|key: id of openShiftChangeRequest|open_shift_change_request_id|openShiftChangeRequest-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--assigned-to**|choice||assigned_to|assignedTo|
|**--manager-action-date-time**|date-time||manager_action_date_time|managerActionDateTime|
|**--manager-action-message**|string||manager_action_message|managerActionMessage|
|**--manager-user-id**|string||manager_user_id|managerUserId|
|**--sender-date-time**|date-time||sender_date_time|senderDateTime|
|**--sender-message**|string||sender_message|senderMessage|
|**--sender-user-id**|string||sender_user_id|senderUserId|
|**--state**|choice||state|state|
|**--open-shift-id**|string|ID for the open shift.|open_shift_id|openShiftId|

#### <a name="teams.scheduleUpdateSchedulingGroups">Command `az teams teamsschedule update-scheduling-group`</a>

##### <a name="Parametersteams.scheduleUpdateSchedulingGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--scheduling-group-id**|string|key: id of schedulingGroup|scheduling_group_id|schedulingGroup-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--display-name**|string|The display name for the schedulingGroup. Required.|display_name|displayName|
|**--is-active**|boolean|Indicates whether the schedulingGroup can be used when creating new entities or updating existing ones. Required.|is_active|isActive|
|**--user-ids**|array|The list of user IDs that are a member of the schedulingGroup. Required.|user_ids|userIds|

#### <a name="teams.scheduleUpdateShifts">Command `az teams teamsschedule update-shift`</a>

##### <a name="Parametersteams.scheduleUpdateShifts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--shift-id**|string|key: id of shift|shift_id|shift-id|
|**--body**|object|New navigation property values|body|body|

#### <a name="teams.scheduleUpdateSwapShiftsChangeRequests">Command `az teams teamsschedule update-swap-shift-change-request`</a>

##### <a name="Parametersteams.scheduleUpdateSwapShiftsChangeRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--swap-shifts-change-request-id**|string|key: id of swapShiftsChangeRequest|swap_shifts_change_request_id|swapShiftsChangeRequest-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
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

#### <a name="teams.scheduleUpdateTimesOff">Command `az teams teamsschedule update-time-off`</a>

##### <a name="Parametersteams.scheduleUpdateTimesOff">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-id**|string|key: id of timeOff|time_off_id|timeOff-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--draft-time-off**|object|timeOffItem|draft_time_off|draftTimeOff|
|**--shared-time-off**|object|timeOffItem|shared_time_off|sharedTimeOff|
|**--user-id**|string|ID of the user assigned to the timeOff. Required.|user_id|userId|

#### <a name="teams.scheduleUpdateTimeOffReasons">Command `az teams teamsschedule update-time-off-reason`</a>

##### <a name="Parametersteams.scheduleUpdateTimeOffReasons">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-reason-id**|string|key: id of timeOffReason|time_off_reason_id|timeOffReason-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--display-name**|string|The name of the timeOffReason. Required.|display_name|displayName|
|**--icon-type**|choice||icon_type|iconType|
|**--is-active**|boolean|Indicates whether the timeOffReason can be used when creating new entities or updating existing ones. Required.|is_active|isActive|

#### <a name="teams.scheduleUpdateTimeOffRequests">Command `az teams teamsschedule update-time-off-request`</a>

##### <a name="Parametersteams.scheduleUpdateTimeOffRequests">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--time-off-request-id**|string|key: id of timeOffRequest|time_off_request_id|timeOffRequest-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
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

### group `az teams teamsteam`
#### <a name="teams.teamCreateTeam">Command `az teams teamsteam create-team`</a>

##### <a name="Parametersteams.teamCreateTeam">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--id1**|string|Read-only.|id1|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--assigned-labels**|array|The list of sensitivity label pairs (label ID, label name) associated with an Microsoft 365 group. Returned only on $select. Read-only.|assigned_labels|assignedLabels|
|**--assigned-licenses**|array|The licenses that are assigned to the group. Returned only on $select. Read-only.|assigned_licenses|assignedLicenses|
|**--microsoft-graph-group-classification**|string|Describes a classification for the group (such as low, medium or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default.|microsoft_graph_group_classification|classification|
|**--created-date-time**|date-time|Timestamp of when the group was created. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|created_date_time|createdDateTime|
|**--microsoft-graph-group-description**|string|An optional description for the group. Returned by default.|microsoft_graph_group_description|description|
|**--microsoft-graph-group-display-name**|string|The display name for the group. This property is required when a group is created and cannot be cleared during updates. Returned by default. Supports $filter and $orderby.|microsoft_graph_group_display_name|displayName|
|**--expiration-date-time**|date-time|Timestamp of when the group is set to expire. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|expiration_date_time|expirationDateTime|
|**--group-types**|array|Specifies the group type and its membership.  If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static.  Returned by default. Supports $filter.|group_types|groupTypes|
|**--has-members-with-license-errors**|boolean|Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an example.|has_members_with_license_errors|hasMembersWithLicenseErrors|
|**--license-processing-state**|object|licenseProcessingState|license_processing_state|licenseProcessingState|
|**--mail**|string|The SMTP address for the group, for example, 'serviceadmins@contoso.onmicrosoft.com'. Returned by default. Read-only. Supports $filter.|mail|mail|
|**--mail-enabled**|boolean|Specifies whether the group is mail-enabled. Returned by default.|mail_enabled|mailEnabled|
|**--mail-nickname**|string|The mail alias for the group, unique in the organization. This property must be specified when a group is created. Returned by default. Supports $filter.|mail_nickname|mailNickname|
|**--membership-rule**|string|The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default.|membership_rule|membershipRule|
|**--membership-rule-processing-state**|string|Indicates whether the dynamic membership processing is on or paused. Possible values are 'On' or 'Paused'. Returned by default.|membership_rule_processing_state|membershipRuleProcessingState|
|**--on-premises-domain-name**|string|Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_domain_name|onPremisesDomainName|
|**--on-premises-last-sync-date-time**|date-time|Indicates the last time at which the group was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only. Supports $filter.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-net-bios-name**|string|Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_net_bios_name|onPremisesNetBiosName|
|**--on-premises-provisioning-errors**|array|Errors when using Microsoft synchronization product during provisioning. Returned by default.|on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--on-premises-sam-account-name**|string|Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_sam_account_name|onPremisesSamAccountName|
|**--on-premises-security-identifier**|string|Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Returned by default. Read-only.|on_premises_security_identifier|onPremisesSecurityIdentifier|
|**--on-premises-sync-enabled**|boolean|true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--preferred-data-location**|string|The preferred data location for the group. For more information, see  OneDrive Online Multi-Geo. Returned by default.|preferred_data_location|preferredDataLocation|
|**--preferred-language**|string|The preferred language for an Microsoft 365 group. Should follow ISO 639-1 Code; for example 'en-US'. Returned by default.|preferred_language|preferredLanguage|
|**--proxy-addresses**|array|Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter.|proxy_addresses|proxyAddresses|
|**--renewed-date-time**|date-time|Timestamp of when the group was last renewed. This cannot be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|renewed_date_time|renewedDateTime|
|**--security-enabled**|boolean|Specifies whether the group is a security group. Returned by default. Supports $filter.|security_enabled|securityEnabled|
|**--security-identifier**|string|Security identifier of the group, used in Windows scenarios. Returned by default.|security_identifier|securityIdentifier|
|**--theme**|string|Specifies an Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange or Red. Returned by default.|theme|theme|
|**--microsoft-graph-group-visibility**|string|Specifies the visibility of a Microsoft 365 group. Possible values are: Private, Public, or Hiddenmembership; blank values are treated as public.  See group visibility options to learn more.Visibility can be set only when a group is created; it is not editable.Visibility is supported only for unified groups; it is not supported for security groups. Returned by default.|microsoft_graph_group_visibility|visibility|
|**--allow-external-senders**|boolean|Indicates if people external to the organization can send messages to the group. Default value is false. Returned only on $select.|allow_external_senders|allowExternalSenders|
|**--auto-subscribe-new-members**|boolean|Indicates if new members added to the group will be auto-subscribed to receive email notifications. You can set this property in a PATCH request for the group; do not set it in the initial POST request that creates the group. Default value is false. Returned only on $select.|auto_subscribe_new_members|autoSubscribeNewMembers|
|**--hide-from-address-lists**|boolean|True if the group is not displayed in certain parts of the Outlook UI: the Address Book, address lists for selecting message recipients, and the Browse Groups dialog for searching groups; otherwise, false. Default value is false. Returned only on $select.|hide_from_address_lists|hideFromAddressLists|
|**--hide-from-outlook-clients**|boolean|True if the group is not displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. Default value is false. Returned only on $select.|hide_from_outlook_clients|hideFromOutlookClients|
|**--is-subscribed-by-mail**|boolean|Indicates whether the signed-in user is subscribed to receive email conversations. Default value is true. Returned only on $select.|is_subscribed_by_mail|isSubscribedByMail|
|**--unseen-count**|integer|Count of conversations that have received new posts since the signed-in user last visited the group. Returned only on $select.|unseen_count|unseenCount|
|**--group-is-archived**|boolean||is_archived|isArchived|
|**--app-role-assignments**|array||app_role_assignments|appRoleAssignments|
|**--created-on-behalf-of**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|created_on_behalf_of|createdOnBehalfOf|
|**--member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--microsoft-graph-group-members**|array|Users and groups that are members of this group. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups) Nullable.|microsoft_graph_group_members|members|
|**--members-with-license-errors**|array|A list of group members with license errors from this group-based license assignment. Read-only.|members_with_license_errors|membersWithLicenseErrors|
|**--owners**|array|The owners of the group. The owners are a set of non-admin users who are allowed to modify this object. Limited to 100 owners. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups). Nullable.|owners|owners|
|**--settings**|array|Read-only. Nullable.|settings|settings|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--transitive-members**|array||transitive_members|transitiveMembers|
|**--accepted-senders**|array|The list of users or groups that are allowed to create post's or calendar events in this group. If this list is non-empty then only users or groups listed here are allowed to post.|accepted_senders|acceptedSenders|
|**--calendar**|object|calendar|calendar|calendar|
|**--calendar-view**|array|The calendar view for the calendar. Read-only.|calendar_view|calendarView|
|**--conversations**|array|The group's conversations.|conversations|conversations|
|**--events**|array|The group's calendar events.|events|events|
|**--photo**|object|profilePhoto|photo|photo|
|**--photos**|array|The profile photos owned by the group. Read-only. Nullable.|photos|photos|
|**--rejected-senders**|array|The list of users or groups that are not allowed to create posts or calendar events in this group. Nullable|rejected_senders|rejectedSenders|
|**--threads**|array|The group's conversation threads. Nullable.|threads|threads|
|**--drive**|object|drive|drive|drive|
|**--drives**|array|The group's drives. Read-only.|drives|drives|
|**--sites**|array|The list of SharePoint sites in this group. Access the default site with /sites/root.|sites|sites|
|**--extensions**|array|The collection of open extensions defined for the group. Read-only. Nullable.|extensions|extensions|
|**--group-lifecycle-policies**|array|The collection of lifecycle policies for this group. Read-only. Nullable.|group_lifecycle_policies|groupLifecyclePolicies|
|**--planner**|object|plannerGroup|planner|planner|
|**--onenote**|object|onenote|onenote|onenote|
|**--team**|object|team|team|team|
|**--id2**|string|Read-only.|id2|id|
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

#### <a name="teams.teamDeleteTeam">Command `az teams teamsteam delete-team`</a>

##### <a name="Parametersteams.teamDeleteTeam">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teams.teamListTeam">Command `az teams teamsteam list-team`</a>

##### <a name="Parametersteams.teamListTeam">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.teamGetTeam">Command `az teams teamsteam show-team`</a>

##### <a name="Parametersteams.teamGetTeam">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teams.teamUpdateTeam">Command `az teams teamsteam update-team`</a>

##### <a name="Parametersteams.teamUpdateTeam">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--id1**|string|Read-only.|id1|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--assigned-labels**|array|The list of sensitivity label pairs (label ID, label name) associated with an Microsoft 365 group. Returned only on $select. Read-only.|assigned_labels|assignedLabels|
|**--assigned-licenses**|array|The licenses that are assigned to the group. Returned only on $select. Read-only.|assigned_licenses|assignedLicenses|
|**--microsoft-graph-group-classification**|string|Describes a classification for the group (such as low, medium or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default.|microsoft_graph_group_classification|classification|
|**--created-date-time**|date-time|Timestamp of when the group was created. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|created_date_time|createdDateTime|
|**--microsoft-graph-group-description**|string|An optional description for the group. Returned by default.|microsoft_graph_group_description|description|
|**--microsoft-graph-group-display-name**|string|The display name for the group. This property is required when a group is created and cannot be cleared during updates. Returned by default. Supports $filter and $orderby.|microsoft_graph_group_display_name|displayName|
|**--expiration-date-time**|date-time|Timestamp of when the group is set to expire. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|expiration_date_time|expirationDateTime|
|**--group-types**|array|Specifies the group type and its membership.  If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static.  Returned by default. Supports $filter.|group_types|groupTypes|
|**--has-members-with-license-errors**|boolean|Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an example.|has_members_with_license_errors|hasMembersWithLicenseErrors|
|**--license-processing-state**|object|licenseProcessingState|license_processing_state|licenseProcessingState|
|**--mail**|string|The SMTP address for the group, for example, 'serviceadmins@contoso.onmicrosoft.com'. Returned by default. Read-only. Supports $filter.|mail|mail|
|**--mail-enabled**|boolean|Specifies whether the group is mail-enabled. Returned by default.|mail_enabled|mailEnabled|
|**--mail-nickname**|string|The mail alias for the group, unique in the organization. This property must be specified when a group is created. Returned by default. Supports $filter.|mail_nickname|mailNickname|
|**--membership-rule**|string|The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default.|membership_rule|membershipRule|
|**--membership-rule-processing-state**|string|Indicates whether the dynamic membership processing is on or paused. Possible values are 'On' or 'Paused'. Returned by default.|membership_rule_processing_state|membershipRuleProcessingState|
|**--on-premises-domain-name**|string|Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_domain_name|onPremisesDomainName|
|**--on-premises-last-sync-date-time**|date-time|Indicates the last time at which the group was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only. Supports $filter.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-net-bios-name**|string|Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_net_bios_name|onPremisesNetBiosName|
|**--on-premises-provisioning-errors**|array|Errors when using Microsoft synchronization product during provisioning. Returned by default.|on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--on-premises-sam-account-name**|string|Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_sam_account_name|onPremisesSamAccountName|
|**--on-premises-security-identifier**|string|Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Returned by default. Read-only.|on_premises_security_identifier|onPremisesSecurityIdentifier|
|**--on-premises-sync-enabled**|boolean|true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--preferred-data-location**|string|The preferred data location for the group. For more information, see  OneDrive Online Multi-Geo. Returned by default.|preferred_data_location|preferredDataLocation|
|**--preferred-language**|string|The preferred language for an Microsoft 365 group. Should follow ISO 639-1 Code; for example 'en-US'. Returned by default.|preferred_language|preferredLanguage|
|**--proxy-addresses**|array|Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter.|proxy_addresses|proxyAddresses|
|**--renewed-date-time**|date-time|Timestamp of when the group was last renewed. This cannot be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|renewed_date_time|renewedDateTime|
|**--security-enabled**|boolean|Specifies whether the group is a security group. Returned by default. Supports $filter.|security_enabled|securityEnabled|
|**--security-identifier**|string|Security identifier of the group, used in Windows scenarios. Returned by default.|security_identifier|securityIdentifier|
|**--theme**|string|Specifies an Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange or Red. Returned by default.|theme|theme|
|**--microsoft-graph-group-visibility**|string|Specifies the visibility of a Microsoft 365 group. Possible values are: Private, Public, or Hiddenmembership; blank values are treated as public.  See group visibility options to learn more.Visibility can be set only when a group is created; it is not editable.Visibility is supported only for unified groups; it is not supported for security groups. Returned by default.|microsoft_graph_group_visibility|visibility|
|**--allow-external-senders**|boolean|Indicates if people external to the organization can send messages to the group. Default value is false. Returned only on $select.|allow_external_senders|allowExternalSenders|
|**--auto-subscribe-new-members**|boolean|Indicates if new members added to the group will be auto-subscribed to receive email notifications. You can set this property in a PATCH request for the group; do not set it in the initial POST request that creates the group. Default value is false. Returned only on $select.|auto_subscribe_new_members|autoSubscribeNewMembers|
|**--hide-from-address-lists**|boolean|True if the group is not displayed in certain parts of the Outlook UI: the Address Book, address lists for selecting message recipients, and the Browse Groups dialog for searching groups; otherwise, false. Default value is false. Returned only on $select.|hide_from_address_lists|hideFromAddressLists|
|**--hide-from-outlook-clients**|boolean|True if the group is not displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. Default value is false. Returned only on $select.|hide_from_outlook_clients|hideFromOutlookClients|
|**--is-subscribed-by-mail**|boolean|Indicates whether the signed-in user is subscribed to receive email conversations. Default value is true. Returned only on $select.|is_subscribed_by_mail|isSubscribedByMail|
|**--unseen-count**|integer|Count of conversations that have received new posts since the signed-in user last visited the group. Returned only on $select.|unseen_count|unseenCount|
|**--group-is-archived**|boolean||is_archived|isArchived|
|**--app-role-assignments**|array||app_role_assignments|appRoleAssignments|
|**--created-on-behalf-of**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|created_on_behalf_of|createdOnBehalfOf|
|**--member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--microsoft-graph-group-members**|array|Users and groups that are members of this group. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups) Nullable.|microsoft_graph_group_members|members|
|**--members-with-license-errors**|array|A list of group members with license errors from this group-based license assignment. Read-only.|members_with_license_errors|membersWithLicenseErrors|
|**--owners**|array|The owners of the group. The owners are a set of non-admin users who are allowed to modify this object. Limited to 100 owners. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups). Nullable.|owners|owners|
|**--settings**|array|Read-only. Nullable.|settings|settings|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--transitive-members**|array||transitive_members|transitiveMembers|
|**--accepted-senders**|array|The list of users or groups that are allowed to create post's or calendar events in this group. If this list is non-empty then only users or groups listed here are allowed to post.|accepted_senders|acceptedSenders|
|**--calendar**|object|calendar|calendar|calendar|
|**--calendar-view**|array|The calendar view for the calendar. Read-only.|calendar_view|calendarView|
|**--conversations**|array|The group's conversations.|conversations|conversations|
|**--events**|array|The group's calendar events.|events|events|
|**--photo**|object|profilePhoto|photo|photo|
|**--photos**|array|The profile photos owned by the group. Read-only. Nullable.|photos|photos|
|**--rejected-senders**|array|The list of users or groups that are not allowed to create posts or calendar events in this group. Nullable|rejected_senders|rejectedSenders|
|**--threads**|array|The group's conversation threads. Nullable.|threads|threads|
|**--drive**|object|drive|drive|drive|
|**--drives**|array|The group's drives. Read-only.|drives|drives|
|**--sites**|array|The list of SharePoint sites in this group. Access the default site with /sites/root.|sites|sites|
|**--extensions**|array|The collection of open extensions defined for the group. Read-only. Nullable.|extensions|extensions|
|**--group-lifecycle-policies**|array|The collection of lifecycle policies for this group. Read-only. Nullable.|group_lifecycle_policies|groupLifecyclePolicies|
|**--planner**|object|plannerGroup|planner|planner|
|**--onenote**|object|onenote|onenote|onenote|
|**--team**|object|team|team|team|
|**--id2**|string|Read-only.|id2|id|
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

### group `az teams teamwork`
#### <a name="teamwork.teamworkGetTeamwork">Command `az teams teamwork show-teamwork`</a>

##### <a name="Parametersteamwork.teamworkGetTeamwork">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamwork.teamworkUpdateTeamwork">Command `az teams teamwork update-teamwork`</a>

##### <a name="Parametersteamwork.teamworkUpdateTeamwork">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--workforce-integrations**|array||workforce_integrations|workforceIntegrations|

### group `az teams teamwork`
#### <a name="teamworkCreateWorkforceIntegrations">Command `az teams teamwork create-workforce-integration`</a>

##### <a name="ParametersteamworkCreateWorkforceIntegrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--api-version**|integer|API version for the call back URL. Start with 1.|api_version|apiVersion|
|**--display-name**|string|Name of the workforce integration.|display_name|displayName|
|**--encryption**|object|workforceIntegrationEncryption|encryption|encryption|
|**--is-active**|boolean|Indicates whether this workforce integration is currently active and available.|is_active|isActive|
|**--supported-entities**|choice||supported_entities|supportedEntities|
|**--url**|string|Workforce Integration URL for callbacks from the Shifts service.|url|url|

#### <a name="teamworkDeleteWorkforceIntegrations">Command `az teams teamwork delete-workforce-integration`</a>

##### <a name="ParametersteamworkDeleteWorkforceIntegrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--workforce-integration-id**|string|key: id of workforceIntegration|workforce_integration_id|workforceIntegration-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="teamworkListWorkforceIntegrations">Command `az teams teamwork list-workforce-integration`</a>

##### <a name="ParametersteamworkListWorkforceIntegrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamworkGetWorkforceIntegrations">Command `az teams teamwork show-workforce-integration`</a>

##### <a name="ParametersteamworkGetWorkforceIntegrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--workforce-integration-id**|string|key: id of workforceIntegration|workforce_integration_id|workforceIntegration-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="teamworkUpdateWorkforceIntegrations">Command `az teams teamwork update-workforce-integration`</a>

##### <a name="ParametersteamworkUpdateWorkforceIntegrations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--workforce-integration-id**|string|key: id of workforceIntegration|workforce_integration_id|workforceIntegration-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--application**|object|identity|application|application|
|**--device**|object|identity|device|device|
|**--user**|object|identity|user|user|
|**--api-version**|integer|API version for the call back URL. Start with 1.|api_version|apiVersion|
|**--display-name**|string|Name of the workforce integration.|display_name|displayName|
|**--encryption**|object|workforceIntegrationEncryption|encryption|encryption|
|**--is-active**|boolean|Indicates whether this workforce integration is currently active and available.|is_active|isActive|
|**--supported-entities**|choice||supported_entities|supportedEntities|
|**--url**|string|Workforce Integration URL for callbacks from the Shifts service.|url|url|

### group `az teams user`
#### <a name="usersCreateJoinedTeams">Command `az teams user create-joined-team`</a>

##### <a name="ParametersusersCreateJoinedTeams">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--id1**|string|Read-only.|id1|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--assigned-labels**|array|The list of sensitivity label pairs (label ID, label name) associated with an Microsoft 365 group. Returned only on $select. Read-only.|assigned_labels|assignedLabels|
|**--assigned-licenses**|array|The licenses that are assigned to the group. Returned only on $select. Read-only.|assigned_licenses|assignedLicenses|
|**--microsoft-graph-group-classification**|string|Describes a classification for the group (such as low, medium or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default.|microsoft_graph_group_classification|classification|
|**--created-date-time**|date-time|Timestamp of when the group was created. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|created_date_time|createdDateTime|
|**--microsoft-graph-group-description**|string|An optional description for the group. Returned by default.|microsoft_graph_group_description|description|
|**--microsoft-graph-group-display-name**|string|The display name for the group. This property is required when a group is created and cannot be cleared during updates. Returned by default. Supports $filter and $orderby.|microsoft_graph_group_display_name|displayName|
|**--expiration-date-time**|date-time|Timestamp of when the group is set to expire. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|expiration_date_time|expirationDateTime|
|**--group-types**|array|Specifies the group type and its membership.  If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static.  Returned by default. Supports $filter.|group_types|groupTypes|
|**--has-members-with-license-errors**|boolean|Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an example.|has_members_with_license_errors|hasMembersWithLicenseErrors|
|**--license-processing-state**|object|licenseProcessingState|license_processing_state|licenseProcessingState|
|**--mail**|string|The SMTP address for the group, for example, 'serviceadmins@contoso.onmicrosoft.com'. Returned by default. Read-only. Supports $filter.|mail|mail|
|**--mail-enabled**|boolean|Specifies whether the group is mail-enabled. Returned by default.|mail_enabled|mailEnabled|
|**--mail-nickname**|string|The mail alias for the group, unique in the organization. This property must be specified when a group is created. Returned by default. Supports $filter.|mail_nickname|mailNickname|
|**--membership-rule**|string|The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default.|membership_rule|membershipRule|
|**--membership-rule-processing-state**|string|Indicates whether the dynamic membership processing is on or paused. Possible values are 'On' or 'Paused'. Returned by default.|membership_rule_processing_state|membershipRuleProcessingState|
|**--on-premises-domain-name**|string|Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_domain_name|onPremisesDomainName|
|**--on-premises-last-sync-date-time**|date-time|Indicates the last time at which the group was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only. Supports $filter.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-net-bios-name**|string|Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_net_bios_name|onPremisesNetBiosName|
|**--on-premises-provisioning-errors**|array|Errors when using Microsoft synchronization product during provisioning. Returned by default.|on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--on-premises-sam-account-name**|string|Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_sam_account_name|onPremisesSamAccountName|
|**--on-premises-security-identifier**|string|Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Returned by default. Read-only.|on_premises_security_identifier|onPremisesSecurityIdentifier|
|**--on-premises-sync-enabled**|boolean|true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--preferred-data-location**|string|The preferred data location for the group. For more information, see  OneDrive Online Multi-Geo. Returned by default.|preferred_data_location|preferredDataLocation|
|**--preferred-language**|string|The preferred language for an Microsoft 365 group. Should follow ISO 639-1 Code; for example 'en-US'. Returned by default.|preferred_language|preferredLanguage|
|**--proxy-addresses**|array|Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter.|proxy_addresses|proxyAddresses|
|**--renewed-date-time**|date-time|Timestamp of when the group was last renewed. This cannot be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|renewed_date_time|renewedDateTime|
|**--security-enabled**|boolean|Specifies whether the group is a security group. Returned by default. Supports $filter.|security_enabled|securityEnabled|
|**--security-identifier**|string|Security identifier of the group, used in Windows scenarios. Returned by default.|security_identifier|securityIdentifier|
|**--theme**|string|Specifies an Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange or Red. Returned by default.|theme|theme|
|**--microsoft-graph-group-visibility**|string|Specifies the visibility of a Microsoft 365 group. Possible values are: Private, Public, or Hiddenmembership; blank values are treated as public.  See group visibility options to learn more.Visibility can be set only when a group is created; it is not editable.Visibility is supported only for unified groups; it is not supported for security groups. Returned by default.|microsoft_graph_group_visibility|visibility|
|**--allow-external-senders**|boolean|Indicates if people external to the organization can send messages to the group. Default value is false. Returned only on $select.|allow_external_senders|allowExternalSenders|
|**--auto-subscribe-new-members**|boolean|Indicates if new members added to the group will be auto-subscribed to receive email notifications. You can set this property in a PATCH request for the group; do not set it in the initial POST request that creates the group. Default value is false. Returned only on $select.|auto_subscribe_new_members|autoSubscribeNewMembers|
|**--hide-from-address-lists**|boolean|True if the group is not displayed in certain parts of the Outlook UI: the Address Book, address lists for selecting message recipients, and the Browse Groups dialog for searching groups; otherwise, false. Default value is false. Returned only on $select.|hide_from_address_lists|hideFromAddressLists|
|**--hide-from-outlook-clients**|boolean|True if the group is not displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. Default value is false. Returned only on $select.|hide_from_outlook_clients|hideFromOutlookClients|
|**--is-subscribed-by-mail**|boolean|Indicates whether the signed-in user is subscribed to receive email conversations. Default value is true. Returned only on $select.|is_subscribed_by_mail|isSubscribedByMail|
|**--unseen-count**|integer|Count of conversations that have received new posts since the signed-in user last visited the group. Returned only on $select.|unseen_count|unseenCount|
|**--group-is-archived**|boolean||is_archived|isArchived|
|**--app-role-assignments**|array||app_role_assignments|appRoleAssignments|
|**--created-on-behalf-of**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|created_on_behalf_of|createdOnBehalfOf|
|**--member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--microsoft-graph-group-members**|array|Users and groups that are members of this group. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups) Nullable.|microsoft_graph_group_members|members|
|**--members-with-license-errors**|array|A list of group members with license errors from this group-based license assignment. Read-only.|members_with_license_errors|membersWithLicenseErrors|
|**--owners**|array|The owners of the group. The owners are a set of non-admin users who are allowed to modify this object. Limited to 100 owners. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups). Nullable.|owners|owners|
|**--settings**|array|Read-only. Nullable.|settings|settings|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--transitive-members**|array||transitive_members|transitiveMembers|
|**--accepted-senders**|array|The list of users or groups that are allowed to create post's or calendar events in this group. If this list is non-empty then only users or groups listed here are allowed to post.|accepted_senders|acceptedSenders|
|**--calendar**|object|calendar|calendar|calendar|
|**--calendar-view**|array|The calendar view for the calendar. Read-only.|calendar_view|calendarView|
|**--conversations**|array|The group's conversations.|conversations|conversations|
|**--events**|array|The group's calendar events.|events|events|
|**--photo**|object|profilePhoto|photo|photo|
|**--photos**|array|The profile photos owned by the group. Read-only. Nullable.|photos|photos|
|**--rejected-senders**|array|The list of users or groups that are not allowed to create posts or calendar events in this group. Nullable|rejected_senders|rejectedSenders|
|**--threads**|array|The group's conversation threads. Nullable.|threads|threads|
|**--drive**|object|drive|drive|drive|
|**--drives**|array|The group's drives. Read-only.|drives|drives|
|**--sites**|array|The list of SharePoint sites in this group. Access the default site with /sites/root.|sites|sites|
|**--extensions**|array|The collection of open extensions defined for the group. Read-only. Nullable.|extensions|extensions|
|**--group-lifecycle-policies**|array|The collection of lifecycle policies for this group. Read-only. Nullable.|group_lifecycle_policies|groupLifecyclePolicies|
|**--planner**|object|plannerGroup|planner|planner|
|**--onenote**|object|onenote|onenote|onenote|
|**--team**|object|team|team|team|
|**--id2**|string|Read-only.|id2|id|
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

#### <a name="usersDeleteJoinedTeams">Command `az teams user delete-joined-team`</a>

##### <a name="ParametersusersDeleteJoinedTeams">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="usersListJoinedTeams">Command `az teams user list-joined-team`</a>

##### <a name="ParametersusersListJoinedTeams">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersGetJoinedTeams">Command `az teams user show-joined-team`</a>

##### <a name="ParametersusersGetJoinedTeams">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--team-id**|string|key: id of team|team_id|team-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="usersUpdateJoinedTeams">Command `az teams user update-joined-team`</a>

##### <a name="ParametersusersUpdateJoinedTeams">Parameters</a> 
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
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--id1**|string|Read-only.|id1|id|
|**--deleted-date-time**|date-time||deleted_date_time|deletedDateTime|
|**--assigned-labels**|array|The list of sensitivity label pairs (label ID, label name) associated with an Microsoft 365 group. Returned only on $select. Read-only.|assigned_labels|assignedLabels|
|**--assigned-licenses**|array|The licenses that are assigned to the group. Returned only on $select. Read-only.|assigned_licenses|assignedLicenses|
|**--microsoft-graph-group-classification**|string|Describes a classification for the group (such as low, medium or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default.|microsoft_graph_group_classification|classification|
|**--created-date-time**|date-time|Timestamp of when the group was created. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|created_date_time|createdDateTime|
|**--microsoft-graph-group-description**|string|An optional description for the group. Returned by default.|microsoft_graph_group_description|description|
|**--microsoft-graph-group-display-name**|string|The display name for the group. This property is required when a group is created and cannot be cleared during updates. Returned by default. Supports $filter and $orderby.|microsoft_graph_group_display_name|displayName|
|**--expiration-date-time**|date-time|Timestamp of when the group is set to expire. The value cannot be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|expiration_date_time|expirationDateTime|
|**--group-types**|array|Specifies the group type and its membership.  If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static.  Returned by default. Supports $filter.|group_types|groupTypes|
|**--has-members-with-license-errors**|boolean|Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an example.|has_members_with_license_errors|hasMembersWithLicenseErrors|
|**--license-processing-state**|object|licenseProcessingState|license_processing_state|licenseProcessingState|
|**--mail**|string|The SMTP address for the group, for example, 'serviceadmins@contoso.onmicrosoft.com'. Returned by default. Read-only. Supports $filter.|mail|mail|
|**--mail-enabled**|boolean|Specifies whether the group is mail-enabled. Returned by default.|mail_enabled|mailEnabled|
|**--mail-nickname**|string|The mail alias for the group, unique in the organization. This property must be specified when a group is created. Returned by default. Supports $filter.|mail_nickname|mailNickname|
|**--membership-rule**|string|The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default.|membership_rule|membershipRule|
|**--membership-rule-processing-state**|string|Indicates whether the dynamic membership processing is on or paused. Possible values are 'On' or 'Paused'. Returned by default.|membership_rule_processing_state|membershipRuleProcessingState|
|**--on-premises-domain-name**|string|Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_domain_name|onPremisesDomainName|
|**--on-premises-last-sync-date-time**|date-time|Indicates the last time at which the group was synced with the on-premises directory.The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only. Supports $filter.|on_premises_last_sync_date_time|onPremisesLastSyncDateTime|
|**--on-premises-net-bios-name**|string|Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_net_bios_name|onPremisesNetBiosName|
|**--on-premises-provisioning-errors**|array|Errors when using Microsoft synchronization product during provisioning. Returned by default.|on_premises_provisioning_errors|onPremisesProvisioningErrors|
|**--on-premises-sam-account-name**|string|Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Azure Active Directory via Azure AD Connect.Returned by default. Read-only.|on_premises_sam_account_name|onPremisesSamAccountName|
|**--on-premises-security-identifier**|string|Contains the on-premises security identifier (SID) for the group that was synchronized from on-premises to the cloud. Returned by default. Read-only.|on_premises_security_identifier|onPremisesSecurityIdentifier|
|**--on-premises-sync-enabled**|boolean|true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter.|on_premises_sync_enabled|onPremisesSyncEnabled|
|**--preferred-data-location**|string|The preferred data location for the group. For more information, see  OneDrive Online Multi-Geo. Returned by default.|preferred_data_location|preferredDataLocation|
|**--preferred-language**|string|The preferred language for an Microsoft 365 group. Should follow ISO 639-1 Code; for example 'en-US'. Returned by default.|preferred_language|preferredLanguage|
|**--proxy-addresses**|array|Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter.|proxy_addresses|proxyAddresses|
|**--renewed-date-time**|date-time|Timestamp of when the group was last renewed. This cannot be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.|renewed_date_time|renewedDateTime|
|**--security-enabled**|boolean|Specifies whether the group is a security group. Returned by default. Supports $filter.|security_enabled|securityEnabled|
|**--security-identifier**|string|Security identifier of the group, used in Windows scenarios. Returned by default.|security_identifier|securityIdentifier|
|**--theme**|string|Specifies an Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange or Red. Returned by default.|theme|theme|
|**--microsoft-graph-group-visibility**|string|Specifies the visibility of a Microsoft 365 group. Possible values are: Private, Public, or Hiddenmembership; blank values are treated as public.  See group visibility options to learn more.Visibility can be set only when a group is created; it is not editable.Visibility is supported only for unified groups; it is not supported for security groups. Returned by default.|microsoft_graph_group_visibility|visibility|
|**--allow-external-senders**|boolean|Indicates if people external to the organization can send messages to the group. Default value is false. Returned only on $select.|allow_external_senders|allowExternalSenders|
|**--auto-subscribe-new-members**|boolean|Indicates if new members added to the group will be auto-subscribed to receive email notifications. You can set this property in a PATCH request for the group; do not set it in the initial POST request that creates the group. Default value is false. Returned only on $select.|auto_subscribe_new_members|autoSubscribeNewMembers|
|**--hide-from-address-lists**|boolean|True if the group is not displayed in certain parts of the Outlook UI: the Address Book, address lists for selecting message recipients, and the Browse Groups dialog for searching groups; otherwise, false. Default value is false. Returned only on $select.|hide_from_address_lists|hideFromAddressLists|
|**--hide-from-outlook-clients**|boolean|True if the group is not displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. Default value is false. Returned only on $select.|hide_from_outlook_clients|hideFromOutlookClients|
|**--is-subscribed-by-mail**|boolean|Indicates whether the signed-in user is subscribed to receive email conversations. Default value is true. Returned only on $select.|is_subscribed_by_mail|isSubscribedByMail|
|**--unseen-count**|integer|Count of conversations that have received new posts since the signed-in user last visited the group. Returned only on $select.|unseen_count|unseenCount|
|**--group-is-archived**|boolean||is_archived|isArchived|
|**--app-role-assignments**|array||app_role_assignments|appRoleAssignments|
|**--created-on-behalf-of**|object|Represents an Azure Active Directory object. The directoryObject type is the base type for many other directory entity types.|created_on_behalf_of|createdOnBehalfOf|
|**--member-of**|array|Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable.|member_of|memberOf|
|**--microsoft-graph-group-members**|array|Users and groups that are members of this group. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups) Nullable.|microsoft_graph_group_members|members|
|**--members-with-license-errors**|array|A list of group members with license errors from this group-based license assignment. Read-only.|members_with_license_errors|membersWithLicenseErrors|
|**--owners**|array|The owners of the group. The owners are a set of non-admin users who are allowed to modify this object. Limited to 100 owners. HTTP Methods: GET (supported for all groups), POST (supported for Microsoft 365 groups, security groups and mail-enabled security groups), DELETE (supported for Microsoft 365 groups and security groups). Nullable.|owners|owners|
|**--settings**|array|Read-only. Nullable.|settings|settings|
|**--transitive-member-of**|array||transitive_member_of|transitiveMemberOf|
|**--transitive-members**|array||transitive_members|transitiveMembers|
|**--accepted-senders**|array|The list of users or groups that are allowed to create post's or calendar events in this group. If this list is non-empty then only users or groups listed here are allowed to post.|accepted_senders|acceptedSenders|
|**--calendar**|object|calendar|calendar|calendar|
|**--calendar-view**|array|The calendar view for the calendar. Read-only.|calendar_view|calendarView|
|**--conversations**|array|The group's conversations.|conversations|conversations|
|**--events**|array|The group's calendar events.|events|events|
|**--photo**|object|profilePhoto|photo|photo|
|**--photos**|array|The profile photos owned by the group. Read-only. Nullable.|photos|photos|
|**--rejected-senders**|array|The list of users or groups that are not allowed to create posts or calendar events in this group. Nullable|rejected_senders|rejectedSenders|
|**--threads**|array|The group's conversation threads. Nullable.|threads|threads|
|**--drive**|object|drive|drive|drive|
|**--drives**|array|The group's drives. Read-only.|drives|drives|
|**--sites**|array|The list of SharePoint sites in this group. Access the default site with /sites/root.|sites|sites|
|**--extensions**|array|The collection of open extensions defined for the group. Read-only. Nullable.|extensions|extensions|
|**--group-lifecycle-policies**|array|The collection of lifecycle policies for this group. Read-only. Nullable.|group_lifecycle_policies|groupLifecyclePolicies|
|**--planner**|object|plannerGroup|planner|planner|
|**--onenote**|object|onenote|onenote|onenote|
|**--team**|object|team|team|team|
|**--id2**|string|Read-only.|id2|id|
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
