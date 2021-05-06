# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az devicescloudprint_beta|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az devicescloudprint_beta` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az devicescloudprint print-print|print.print|[commands](#CommandsInprint.print)|
|az devicescloudprint print|print|[commands](#CommandsInprint)|
|az devicescloudprint print-printer|print.printers|[commands](#CommandsInprint.printers)|
|az devicescloudprint print-printer-task-trigger|print.printers.taskTriggers|[commands](#CommandsInprint.printers.taskTriggers)|
|az devicescloudprint print-printer-share|print.printerShares|[commands](#CommandsInprint.printerShares)|
|az devicescloudprint print-printer-share-printer|print.printerShares.printer|[commands](#CommandsInprint.printerShares.printer)|
|az devicescloudprint print-report|print.reports|[commands](#CommandsInprint.reports)|
|az devicescloudprint print-service|print.services|[commands](#CommandsInprint.services)|
|az devicescloudprint print-share|print.shares|[commands](#CommandsInprint.shares)|
|az devicescloudprint print-share-printer|print.shares.printer|[commands](#CommandsInprint.shares.printer)|
|az devicescloudprint print-task-definition|print.taskDefinitions|[commands](#CommandsInprint.taskDefinitions)|
|az devicescloudprint print-task-definition-task|print.taskDefinitions.tasks|[commands](#CommandsInprint.taskDefinitions.tasks)|

## COMMANDS
### <a name="CommandsInprint">Commands in `az devicescloudprint print` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescloudprint print create-connector](#printCreateConnectors)|CreateConnectors|[Parameters](#ParametersprintCreateConnectors)|Not Found|
|[az devicescloudprint print create-operation](#printCreateOperations)|CreateOperations|[Parameters](#ParametersprintCreateOperations)|Not Found|
|[az devicescloudprint print create-printer](#printCreatePrinters)|CreatePrinters|[Parameters](#ParametersprintCreatePrinters)|Not Found|
|[az devicescloudprint print create-printer-share](#printCreatePrinterShares)|CreatePrinterShares|[Parameters](#ParametersprintCreatePrinterShares)|Not Found|
|[az devicescloudprint print create-report](#printCreateReports)|CreateReports|[Parameters](#ParametersprintCreateReports)|Not Found|
|[az devicescloudprint print create-service](#printCreateServices)|CreateServices|[Parameters](#ParametersprintCreateServices)|Not Found|
|[az devicescloudprint print create-share](#printCreateShares)|CreateShares|[Parameters](#ParametersprintCreateShares)|Not Found|
|[az devicescloudprint print create-task-definition](#printCreateTaskDefinitions)|CreateTaskDefinitions|[Parameters](#ParametersprintCreateTaskDefinitions)|Not Found|
|[az devicescloudprint print delete-connector](#printDeleteConnectors)|DeleteConnectors|[Parameters](#ParametersprintDeleteConnectors)|Not Found|
|[az devicescloudprint print delete-operation](#printDeleteOperations)|DeleteOperations|[Parameters](#ParametersprintDeleteOperations)|Not Found|
|[az devicescloudprint print delete-printer](#printDeletePrinters)|DeletePrinters|[Parameters](#ParametersprintDeletePrinters)|Not Found|
|[az devicescloudprint print delete-printer-share](#printDeletePrinterShares)|DeletePrinterShares|[Parameters](#ParametersprintDeletePrinterShares)|Not Found|
|[az devicescloudprint print delete-report](#printDeleteReports)|DeleteReports|[Parameters](#ParametersprintDeleteReports)|Not Found|
|[az devicescloudprint print delete-service](#printDeleteServices)|DeleteServices|[Parameters](#ParametersprintDeleteServices)|Not Found|
|[az devicescloudprint print delete-share](#printDeleteShares)|DeleteShares|[Parameters](#ParametersprintDeleteShares)|Not Found|
|[az devicescloudprint print delete-task-definition](#printDeleteTaskDefinitions)|DeleteTaskDefinitions|[Parameters](#ParametersprintDeleteTaskDefinitions)|Not Found|
|[az devicescloudprint print list-connector](#printListConnectors)|ListConnectors|[Parameters](#ParametersprintListConnectors)|Not Found|
|[az devicescloudprint print list-operation](#printListOperations)|ListOperations|[Parameters](#ParametersprintListOperations)|Not Found|
|[az devicescloudprint print list-printer](#printListPrinters)|ListPrinters|[Parameters](#ParametersprintListPrinters)|Not Found|
|[az devicescloudprint print list-printer-share](#printListPrinterShares)|ListPrinterShares|[Parameters](#ParametersprintListPrinterShares)|Not Found|
|[az devicescloudprint print list-report](#printListReports)|ListReports|[Parameters](#ParametersprintListReports)|Not Found|
|[az devicescloudprint print list-service](#printListServices)|ListServices|[Parameters](#ParametersprintListServices)|Not Found|
|[az devicescloudprint print list-share](#printListShares)|ListShares|[Parameters](#ParametersprintListShares)|Not Found|
|[az devicescloudprint print list-task-definition](#printListTaskDefinitions)|ListTaskDefinitions|[Parameters](#ParametersprintListTaskDefinitions)|Not Found|
|[az devicescloudprint print show-connector](#printGetConnectors)|GetConnectors|[Parameters](#ParametersprintGetConnectors)|Not Found|
|[az devicescloudprint print show-operation](#printGetOperations)|GetOperations|[Parameters](#ParametersprintGetOperations)|Not Found|
|[az devicescloudprint print show-printer](#printGetPrinters)|GetPrinters|[Parameters](#ParametersprintGetPrinters)|Not Found|
|[az devicescloudprint print show-printer-share](#printGetPrinterShares)|GetPrinterShares|[Parameters](#ParametersprintGetPrinterShares)|Not Found|
|[az devicescloudprint print show-report](#printGetReports)|GetReports|[Parameters](#ParametersprintGetReports)|Not Found|
|[az devicescloudprint print show-service](#printGetServices)|GetServices|[Parameters](#ParametersprintGetServices)|Not Found|
|[az devicescloudprint print show-share](#printGetShares)|GetShares|[Parameters](#ParametersprintGetShares)|Not Found|
|[az devicescloudprint print show-task-definition](#printGetTaskDefinitions)|GetTaskDefinitions|[Parameters](#ParametersprintGetTaskDefinitions)|Not Found|
|[az devicescloudprint print update-connector](#printUpdateConnectors)|UpdateConnectors|[Parameters](#ParametersprintUpdateConnectors)|Not Found|
|[az devicescloudprint print update-operation](#printUpdateOperations)|UpdateOperations|[Parameters](#ParametersprintUpdateOperations)|Not Found|
|[az devicescloudprint print update-printer](#printUpdatePrinters)|UpdatePrinters|[Parameters](#ParametersprintUpdatePrinters)|Not Found|
|[az devicescloudprint print update-printer-share](#printUpdatePrinterShares)|UpdatePrinterShares|[Parameters](#ParametersprintUpdatePrinterShares)|Not Found|
|[az devicescloudprint print update-report](#printUpdateReports)|UpdateReports|[Parameters](#ParametersprintUpdateReports)|Not Found|
|[az devicescloudprint print update-service](#printUpdateServices)|UpdateServices|[Parameters](#ParametersprintUpdateServices)|Not Found|
|[az devicescloudprint print update-share](#printUpdateShares)|UpdateShares|[Parameters](#ParametersprintUpdateShares)|Not Found|
|[az devicescloudprint print update-task-definition](#printUpdateTaskDefinitions)|UpdateTaskDefinitions|[Parameters](#ParametersprintUpdateTaskDefinitions)|Not Found|

### <a name="CommandsInprint.print">Commands in `az devicescloudprint print-print` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescloudprint print-print show-print](#print.printGetPrint)|GetPrint|[Parameters](#Parametersprint.printGetPrint)|Not Found|
|[az devicescloudprint print-print update-print](#print.printUpdatePrint)|UpdatePrint|[Parameters](#Parametersprint.printUpdatePrint)|Not Found|

### <a name="CommandsInprint.printers">Commands in `az devicescloudprint print-printer` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescloudprint print-printer create](#print.printerscreate)|create|[Parameters](#Parametersprint.printerscreate)|Not Found|
|[az devicescloudprint print-printer create-allowed-group](#print.printersCreateAllowedGroups)|CreateAllowedGroups|[Parameters](#Parametersprint.printersCreateAllowedGroups)|Not Found|
|[az devicescloudprint print-printer create-allowed-user](#print.printersCreateAllowedUsers)|CreateAllowedUsers|[Parameters](#Parametersprint.printersCreateAllowedUsers)|Not Found|
|[az devicescloudprint print-printer create-ref-connector](#print.printersCreateRefConnectors)|CreateRefConnectors|[Parameters](#Parametersprint.printersCreateRefConnectors)|Not Found|
|[az devicescloudprint print-printer create-ref-share](#print.printersCreateRefShares)|CreateRefShares|[Parameters](#Parametersprint.printersCreateRefShares)|Not Found|
|[az devicescloudprint print-printer create-task-trigger](#print.printersCreateTaskTriggers)|CreateTaskTriggers|[Parameters](#Parametersprint.printersCreateTaskTriggers)|Not Found|
|[az devicescloudprint print-printer delete-allowed-group](#print.printersDeleteAllowedGroups)|DeleteAllowedGroups|[Parameters](#Parametersprint.printersDeleteAllowedGroups)|Not Found|
|[az devicescloudprint print-printer delete-allowed-user](#print.printersDeleteAllowedUsers)|DeleteAllowedUsers|[Parameters](#Parametersprint.printersDeleteAllowedUsers)|Not Found|
|[az devicescloudprint print-printer delete-ref-share](#print.printersDeleteRefShare)|DeleteRefShare|[Parameters](#Parametersprint.printersDeleteRefShare)|Not Found|
|[az devicescloudprint print-printer delete-task-trigger](#print.printersDeleteTaskTriggers)|DeleteTaskTriggers|[Parameters](#Parametersprint.printersDeleteTaskTriggers)|Not Found|
|[az devicescloudprint print-printer list-allowed-group](#print.printersListAllowedGroups)|ListAllowedGroups|[Parameters](#Parametersprint.printersListAllowedGroups)|Not Found|
|[az devicescloudprint print-printer list-allowed-user](#print.printersListAllowedUsers)|ListAllowedUsers|[Parameters](#Parametersprint.printersListAllowedUsers)|Not Found|
|[az devicescloudprint print-printer list-connector](#print.printersListConnectors)|ListConnectors|[Parameters](#Parametersprint.printersListConnectors)|Not Found|
|[az devicescloudprint print-printer list-ref-connector](#print.printersListRefConnectors)|ListRefConnectors|[Parameters](#Parametersprint.printersListRefConnectors)|Not Found|
|[az devicescloudprint print-printer list-ref-share](#print.printersListRefShares)|ListRefShares|[Parameters](#Parametersprint.printersListRefShares)|Not Found|
|[az devicescloudprint print-printer list-share](#print.printersListShares)|ListShares|[Parameters](#Parametersprint.printersListShares)|Not Found|
|[az devicescloudprint print-printer list-task-trigger](#print.printersListTaskTriggers)|ListTaskTriggers|[Parameters](#Parametersprint.printersListTaskTriggers)|Not Found|
|[az devicescloudprint print-printer reset-default](#print.printersresetDefaults)|resetDefaults|[Parameters](#Parametersprint.printersresetDefaults)|Not Found|
|[az devicescloudprint print-printer restore-factory-default](#print.printersrestoreFactoryDefaults)|restoreFactoryDefaults|[Parameters](#Parametersprint.printersrestoreFactoryDefaults)|Not Found|
|[az devicescloudprint print-printer set-ref-share](#print.printersSetRefShare)|SetRefShare|[Parameters](#Parametersprint.printersSetRefShare)|Not Found|
|[az devicescloudprint print-printer show-allowed-group](#print.printersGetAllowedGroups)|GetAllowedGroups|[Parameters](#Parametersprint.printersGetAllowedGroups)|Not Found|
|[az devicescloudprint print-printer show-allowed-user](#print.printersGetAllowedUsers)|GetAllowedUsers|[Parameters](#Parametersprint.printersGetAllowedUsers)|Not Found|
|[az devicescloudprint print-printer show-capability](#print.printersgetCapabilities)|getCapabilities|[Parameters](#Parametersprint.printersgetCapabilities)|Not Found|
|[az devicescloudprint print-printer show-ref-share](#print.printersGetRefShare)|GetRefShare|[Parameters](#Parametersprint.printersGetRefShare)|Not Found|
|[az devicescloudprint print-printer show-share](#print.printersGetShare)|GetShare|[Parameters](#Parametersprint.printersGetShare)|Not Found|
|[az devicescloudprint print-printer show-task-trigger](#print.printersGetTaskTriggers)|GetTaskTriggers|[Parameters](#Parametersprint.printersGetTaskTriggers)|Not Found|
|[az devicescloudprint print-printer update-allowed-group](#print.printersUpdateAllowedGroups)|UpdateAllowedGroups|[Parameters](#Parametersprint.printersUpdateAllowedGroups)|Not Found|
|[az devicescloudprint print-printer update-allowed-user](#print.printersUpdateAllowedUsers)|UpdateAllowedUsers|[Parameters](#Parametersprint.printersUpdateAllowedUsers)|Not Found|
|[az devicescloudprint print-printer update-task-trigger](#print.printersUpdateTaskTriggers)|UpdateTaskTriggers|[Parameters](#Parametersprint.printersUpdateTaskTriggers)|Not Found|

### <a name="CommandsInprint.printerShares">Commands in `az devicescloudprint print-printer-share` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescloudprint print-printer-share create-allowed-group](#print.printerSharesCreateAllowedGroups)|CreateAllowedGroups|[Parameters](#Parametersprint.printerSharesCreateAllowedGroups)|Not Found|
|[az devicescloudprint print-printer-share create-allowed-user](#print.printerSharesCreateAllowedUsers)|CreateAllowedUsers|[Parameters](#Parametersprint.printerSharesCreateAllowedUsers)|Not Found|
|[az devicescloudprint print-printer-share delete-allowed-group](#print.printerSharesDeleteAllowedGroups)|DeleteAllowedGroups|[Parameters](#Parametersprint.printerSharesDeleteAllowedGroups)|Not Found|
|[az devicescloudprint print-printer-share delete-allowed-user](#print.printerSharesDeleteAllowedUsers)|DeleteAllowedUsers|[Parameters](#Parametersprint.printerSharesDeleteAllowedUsers)|Not Found|
|[az devicescloudprint print-printer-share delete-ref-printer](#print.printerSharesDeleteRefPrinter)|DeleteRefPrinter|[Parameters](#Parametersprint.printerSharesDeleteRefPrinter)|Not Found|
|[az devicescloudprint print-printer-share list-allowed-group](#print.printerSharesListAllowedGroups)|ListAllowedGroups|[Parameters](#Parametersprint.printerSharesListAllowedGroups)|Not Found|
|[az devicescloudprint print-printer-share list-allowed-user](#print.printerSharesListAllowedUsers)|ListAllowedUsers|[Parameters](#Parametersprint.printerSharesListAllowedUsers)|Not Found|
|[az devicescloudprint print-printer-share set-ref-printer](#print.printerSharesSetRefPrinter)|SetRefPrinter|[Parameters](#Parametersprint.printerSharesSetRefPrinter)|Not Found|
|[az devicescloudprint print-printer-share show-allowed-group](#print.printerSharesGetAllowedGroups)|GetAllowedGroups|[Parameters](#Parametersprint.printerSharesGetAllowedGroups)|Not Found|
|[az devicescloudprint print-printer-share show-allowed-user](#print.printerSharesGetAllowedUsers)|GetAllowedUsers|[Parameters](#Parametersprint.printerSharesGetAllowedUsers)|Not Found|
|[az devicescloudprint print-printer-share show-printer](#print.printerSharesGetPrinter)|GetPrinter|[Parameters](#Parametersprint.printerSharesGetPrinter)|Not Found|
|[az devicescloudprint print-printer-share show-ref-printer](#print.printerSharesGetRefPrinter)|GetRefPrinter|[Parameters](#Parametersprint.printerSharesGetRefPrinter)|Not Found|
|[az devicescloudprint print-printer-share update-allowed-group](#print.printerSharesUpdateAllowedGroups)|UpdateAllowedGroups|[Parameters](#Parametersprint.printerSharesUpdateAllowedGroups)|Not Found|
|[az devicescloudprint print-printer-share update-allowed-user](#print.printerSharesUpdateAllowedUsers)|UpdateAllowedUsers|[Parameters](#Parametersprint.printerSharesUpdateAllowedUsers)|Not Found|

### <a name="CommandsInprint.printerShares.printer">Commands in `az devicescloudprint print-printer-share-printer` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescloudprint print-printer-share-printer reset-default](#print.printerShares.printerresetDefaults)|resetDefaults|[Parameters](#Parametersprint.printerShares.printerresetDefaults)|Not Found|
|[az devicescloudprint print-printer-share-printer restore-factory-default](#print.printerShares.printerrestoreFactoryDefaults)|restoreFactoryDefaults|[Parameters](#Parametersprint.printerShares.printerrestoreFactoryDefaults)|Not Found|
|[az devicescloudprint print-printer-share-printer show-capability](#print.printerShares.printergetCapabilities)|getCapabilities|[Parameters](#Parametersprint.printerShares.printergetCapabilities)|Not Found|

### <a name="CommandsInprint.printers.taskTriggers">Commands in `az devicescloudprint print-printer-task-trigger` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescloudprint print-printer-task-trigger delete-ref-definition](#print.printers.taskTriggersDeleteRefDefinition)|DeleteRefDefinition|[Parameters](#Parametersprint.printers.taskTriggersDeleteRefDefinition)|Not Found|
|[az devicescloudprint print-printer-task-trigger set-ref-definition](#print.printers.taskTriggersSetRefDefinition)|SetRefDefinition|[Parameters](#Parametersprint.printers.taskTriggersSetRefDefinition)|Not Found|
|[az devicescloudprint print-printer-task-trigger show-definition](#print.printers.taskTriggersGetDefinition)|GetDefinition|[Parameters](#Parametersprint.printers.taskTriggersGetDefinition)|Not Found|
|[az devicescloudprint print-printer-task-trigger show-ref-definition](#print.printers.taskTriggersGetRefDefinition)|GetRefDefinition|[Parameters](#Parametersprint.printers.taskTriggersGetRefDefinition)|Not Found|

### <a name="CommandsInprint.reports">Commands in `az devicescloudprint print-report` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescloudprint print-report show-group-archived-print-job](#print.reportsgetGroupArchivedPrintJobs)|getGroupArchivedPrintJobs|[Parameters](#Parametersprint.reportsgetGroupArchivedPrintJobs)|Not Found|
|[az devicescloudprint print-report show-group-print-usage-summary](#print.reportsgetGroupPrintUsageSummary)|getGroupPrintUsageSummary|[Parameters](#Parametersprint.reportsgetGroupPrintUsageSummary)|Not Found|
|[az devicescloudprint print-report show-overall-print-usage-summary](#print.reportsgetOverallPrintUsageSummary)|getOverallPrintUsageSummary|[Parameters](#Parametersprint.reportsgetOverallPrintUsageSummary)|Not Found|
|[az devicescloudprint print-report show-print-usage-summary](#print.reportsgetPrintUsageSummariesByTimeSpan)|getPrintUsageSummariesByTimeSpan|[Parameters](#Parametersprint.reportsgetPrintUsageSummariesByTimeSpan)|Not Found|
|[az devicescloudprint print-report show-print-usage-summary](#print.reportsgetPrintUsageSummariesByGroup)|getPrintUsageSummariesByGroup|[Parameters](#Parametersprint.reportsgetPrintUsageSummariesByGroup)|Not Found|
|[az devicescloudprint print-report show-print-usage-summary](#print.reportsgetPrintUsageSummariesByPrinter)|getPrintUsageSummariesByPrinter|[Parameters](#Parametersprint.reportsgetPrintUsageSummariesByPrinter)|Not Found|
|[az devicescloudprint print-report show-print-usage-summary](#print.reportsgetPrintUsageSummariesByUser)|getPrintUsageSummariesByUser|[Parameters](#Parametersprint.reportsgetPrintUsageSummariesByUser)|Not Found|
|[az devicescloudprint print-report show-printer-archived-print-job](#print.reportsgetPrinterArchivedPrintJobs)|getPrinterArchivedPrintJobs|[Parameters](#Parametersprint.reportsgetPrinterArchivedPrintJobs)|Not Found|
|[az devicescloudprint print-report show-printer-usage-summary](#print.reportsgetPrinterUsageSummary)|getPrinterUsageSummary|[Parameters](#Parametersprint.reportsgetPrinterUsageSummary)|Not Found|
|[az devicescloudprint print-report show-user-archived-print-job](#print.reportsgetUserArchivedPrintJobs)|getUserArchivedPrintJobs|[Parameters](#Parametersprint.reportsgetUserArchivedPrintJobs)|Not Found|
|[az devicescloudprint print-report show-user-print-usage-summary](#print.reportsgetUserPrintUsageSummary)|getUserPrintUsageSummary|[Parameters](#Parametersprint.reportsgetUserPrintUsageSummary)|Not Found|

### <a name="CommandsInprint.services">Commands in `az devicescloudprint print-service` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescloudprint print-service create-endpoint](#print.servicesCreateEndpoints)|CreateEndpoints|[Parameters](#Parametersprint.servicesCreateEndpoints)|Not Found|
|[az devicescloudprint print-service delete-endpoint](#print.servicesDeleteEndpoints)|DeleteEndpoints|[Parameters](#Parametersprint.servicesDeleteEndpoints)|Not Found|
|[az devicescloudprint print-service list-endpoint](#print.servicesListEndpoints)|ListEndpoints|[Parameters](#Parametersprint.servicesListEndpoints)|Not Found|
|[az devicescloudprint print-service show-endpoint](#print.servicesGetEndpoints)|GetEndpoints|[Parameters](#Parametersprint.servicesGetEndpoints)|Not Found|
|[az devicescloudprint print-service update-endpoint](#print.servicesUpdateEndpoints)|UpdateEndpoints|[Parameters](#Parametersprint.servicesUpdateEndpoints)|Not Found|

### <a name="CommandsInprint.shares">Commands in `az devicescloudprint print-share` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescloudprint print-share create-allowed-group](#print.sharesCreateAllowedGroups)|CreateAllowedGroups|[Parameters](#Parametersprint.sharesCreateAllowedGroups)|Not Found|
|[az devicescloudprint print-share create-allowed-user](#print.sharesCreateAllowedUsers)|CreateAllowedUsers|[Parameters](#Parametersprint.sharesCreateAllowedUsers)|Not Found|
|[az devicescloudprint print-share delete-allowed-group](#print.sharesDeleteAllowedGroups)|DeleteAllowedGroups|[Parameters](#Parametersprint.sharesDeleteAllowedGroups)|Not Found|
|[az devicescloudprint print-share delete-allowed-user](#print.sharesDeleteAllowedUsers)|DeleteAllowedUsers|[Parameters](#Parametersprint.sharesDeleteAllowedUsers)|Not Found|
|[az devicescloudprint print-share delete-ref-printer](#print.sharesDeleteRefPrinter)|DeleteRefPrinter|[Parameters](#Parametersprint.sharesDeleteRefPrinter)|Not Found|
|[az devicescloudprint print-share list-allowed-group](#print.sharesListAllowedGroups)|ListAllowedGroups|[Parameters](#Parametersprint.sharesListAllowedGroups)|Not Found|
|[az devicescloudprint print-share list-allowed-user](#print.sharesListAllowedUsers)|ListAllowedUsers|[Parameters](#Parametersprint.sharesListAllowedUsers)|Not Found|
|[az devicescloudprint print-share set-ref-printer](#print.sharesSetRefPrinter)|SetRefPrinter|[Parameters](#Parametersprint.sharesSetRefPrinter)|Not Found|
|[az devicescloudprint print-share show-allowed-group](#print.sharesGetAllowedGroups)|GetAllowedGroups|[Parameters](#Parametersprint.sharesGetAllowedGroups)|Not Found|
|[az devicescloudprint print-share show-allowed-user](#print.sharesGetAllowedUsers)|GetAllowedUsers|[Parameters](#Parametersprint.sharesGetAllowedUsers)|Not Found|
|[az devicescloudprint print-share show-printer](#print.sharesGetPrinter)|GetPrinter|[Parameters](#Parametersprint.sharesGetPrinter)|Not Found|
|[az devicescloudprint print-share show-ref-printer](#print.sharesGetRefPrinter)|GetRefPrinter|[Parameters](#Parametersprint.sharesGetRefPrinter)|Not Found|
|[az devicescloudprint print-share update-allowed-group](#print.sharesUpdateAllowedGroups)|UpdateAllowedGroups|[Parameters](#Parametersprint.sharesUpdateAllowedGroups)|Not Found|
|[az devicescloudprint print-share update-allowed-user](#print.sharesUpdateAllowedUsers)|UpdateAllowedUsers|[Parameters](#Parametersprint.sharesUpdateAllowedUsers)|Not Found|

### <a name="CommandsInprint.shares.printer">Commands in `az devicescloudprint print-share-printer` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescloudprint print-share-printer reset-default](#print.shares.printerresetDefaults)|resetDefaults|[Parameters](#Parametersprint.shares.printerresetDefaults)|Not Found|
|[az devicescloudprint print-share-printer restore-factory-default](#print.shares.printerrestoreFactoryDefaults)|restoreFactoryDefaults|[Parameters](#Parametersprint.shares.printerrestoreFactoryDefaults)|Not Found|
|[az devicescloudprint print-share-printer show-capability](#print.shares.printergetCapabilities)|getCapabilities|[Parameters](#Parametersprint.shares.printergetCapabilities)|Not Found|

### <a name="CommandsInprint.taskDefinitions">Commands in `az devicescloudprint print-task-definition` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescloudprint print-task-definition create-task](#print.taskDefinitionsCreateTasks)|CreateTasks|[Parameters](#Parametersprint.taskDefinitionsCreateTasks)|Not Found|
|[az devicescloudprint print-task-definition delete-task](#print.taskDefinitionsDeleteTasks)|DeleteTasks|[Parameters](#Parametersprint.taskDefinitionsDeleteTasks)|Not Found|
|[az devicescloudprint print-task-definition list-task](#print.taskDefinitionsListTasks)|ListTasks|[Parameters](#Parametersprint.taskDefinitionsListTasks)|Not Found|
|[az devicescloudprint print-task-definition show-task](#print.taskDefinitionsGetTasks)|GetTasks|[Parameters](#Parametersprint.taskDefinitionsGetTasks)|Not Found|
|[az devicescloudprint print-task-definition update-task](#print.taskDefinitionsUpdateTasks)|UpdateTasks|[Parameters](#Parametersprint.taskDefinitionsUpdateTasks)|Not Found|

### <a name="CommandsInprint.taskDefinitions.tasks">Commands in `az devicescloudprint print-task-definition-task` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az devicescloudprint print-task-definition-task delete-ref-definition](#print.taskDefinitions.tasksDeleteRefDefinition)|DeleteRefDefinition|[Parameters](#Parametersprint.taskDefinitions.tasksDeleteRefDefinition)|Not Found|
|[az devicescloudprint print-task-definition-task delete-ref-trigger](#print.taskDefinitions.tasksDeleteRefTrigger)|DeleteRefTrigger|[Parameters](#Parametersprint.taskDefinitions.tasksDeleteRefTrigger)|Not Found|
|[az devicescloudprint print-task-definition-task set-ref-definition](#print.taskDefinitions.tasksSetRefDefinition)|SetRefDefinition|[Parameters](#Parametersprint.taskDefinitions.tasksSetRefDefinition)|Not Found|
|[az devicescloudprint print-task-definition-task set-ref-trigger](#print.taskDefinitions.tasksSetRefTrigger)|SetRefTrigger|[Parameters](#Parametersprint.taskDefinitions.tasksSetRefTrigger)|Not Found|
|[az devicescloudprint print-task-definition-task show-definition](#print.taskDefinitions.tasksGetDefinition)|GetDefinition|[Parameters](#Parametersprint.taskDefinitions.tasksGetDefinition)|Not Found|
|[az devicescloudprint print-task-definition-task show-ref-definition](#print.taskDefinitions.tasksGetRefDefinition)|GetRefDefinition|[Parameters](#Parametersprint.taskDefinitions.tasksGetRefDefinition)|Not Found|
|[az devicescloudprint print-task-definition-task show-ref-trigger](#print.taskDefinitions.tasksGetRefTrigger)|GetRefTrigger|[Parameters](#Parametersprint.taskDefinitions.tasksGetRefTrigger)|Not Found|
|[az devicescloudprint print-task-definition-task show-trigger](#print.taskDefinitions.tasksGetTrigger)|GetTrigger|[Parameters](#Parametersprint.taskDefinitions.tasksGetTrigger)|Not Found|


## COMMAND DETAILS

### group `az devicescloudprint print`
#### <a name="printCreateConnectors">Command `az devicescloudprint print create-connector`</a>

##### <a name="ParametersprintCreateConnectors">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--app-version**|string||app_version|appVersion|
|**--display-name**|string||display_name|displayName|
|**--fully-qualified-domain-name**|string||fully_qualified_domain_name|fullyQualifiedDomainName|
|**--location**|object|printerLocation|location|location|
|**--name**|string||name|name|
|**--operating-system**|string||operating_system|operatingSystem|
|**--registered-date-time**|date-time||registered_date_time|registeredDateTime|
|**--last-connection-time**|date-time||last_connection_time|lastConnectionTime|

#### <a name="printCreateOperations">Command `az devicescloudprint print create-operation`</a>

##### <a name="ParametersprintCreateOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--status**|object|printOperationStatus|status|status|

#### <a name="printCreatePrinters">Command `az devicescloudprint print create-printer`</a>

##### <a name="ParametersprintCreatePrinters">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--defaults**|object|printerDefaults|defaults|defaults|
|**--display-name**|string||display_name|displayName|
|**--is-accepting-jobs**|boolean||is_accepting_jobs|isAcceptingJobs|
|**--location**|object|printerLocation|location|location|
|**--manufacturer**|string||manufacturer|manufacturer|
|**--model**|string||model|model|
|**--name**|string||name|name|
|**--status**|object|printerStatus|status|status|
|**--jobs**|array||jobs|jobs|
|**--bottom-margins**|array||bottom_margins|bottomMargins|
|**--collation**|boolean||collation|collation|
|**--color-modes**|array||color_modes|colorModes|
|**--content-types**|array||content_types|contentTypes|
|**--copies-per-job**|object|integerRange|copies_per_job|copiesPerJob|
|**--dpis**|array||dpis|dpis|
|**--duplex-modes**|array||duplex_modes|duplexModes|
|**--feed-directions**|array||feed_directions|feedDirections|
|**--feed-orientations**|array||feed_orientations|feedOrientations|
|**--finishings**|array||finishings|finishings|
|**--input-bins**|array||input_bins|inputBins|
|**--is-color-printing-supported**|boolean||is_color_printing_supported|isColorPrintingSupported|
|**--is-page-range-supported**|boolean||is_page_range_supported|isPageRangeSupported|
|**--left-margins**|array||left_margins|leftMargins|
|**--media-colors**|array||media_colors|mediaColors|
|**--media-sizes**|array||media_sizes|mediaSizes|
|**--media-types**|array||media_types|mediaTypes|
|**--multipage-layouts**|array||multipage_layouts|multipageLayouts|
|**--orientations**|array||orientations|orientations|
|**--output-bins**|array||output_bins|outputBins|
|**--pages-per-sheet**|array||pages_per_sheet|pagesPerSheet|
|**--qualities**|array||qualities|qualities|
|**--right-margins**|array||right_margins|rightMargins|
|**--scalings**|array||scalings|scalings|
|**--supported-color-configurations**|array||supported_color_configurations|supportedColorConfigurations|
|**--supported-copies-per-job**|object|integerRange|supported_copies_per_job|supportedCopiesPerJob|
|**--supported-document-mime-types**|array||supported_document_mime_types|supportedDocumentMimeTypes|
|**--supported-duplex-configurations**|array||supported_duplex_configurations|supportedDuplexConfigurations|
|**--supported-finishings**|array||supported_finishings|supportedFinishings|
|**--supported-media-colors**|array||supported_media_colors|supportedMediaColors|
|**--supported-media-sizes**|array||supported_media_sizes|supportedMediaSizes|
|**--supported-media-types**|array||supported_media_types|supportedMediaTypes|
|**--supported-orientations**|array||supported_orientations|supportedOrientations|
|**--supported-output-bins**|array||supported_output_bins|supportedOutputBins|
|**--supported-pages-per-sheet**|object|integerRange|supported_pages_per_sheet|supportedPagesPerSheet|
|**--supported-presentation-directions**|array||supported_presentation_directions|supportedPresentationDirections|
|**--supported-print-qualities**|array||supported_print_qualities|supportedPrintQualities|
|**--supports-fit-pdf-to-page**|boolean||supports_fit_pdf_to_page|supportsFitPdfToPage|
|**--top-margins**|array||top_margins|topMargins|
|**--accepting-jobs**|boolean||accepting_jobs|acceptingJobs|
|**--is-shared**|boolean||is_shared|isShared|
|**--registered-date-time**|date-time||registered_date_time|registeredDateTime|
|**--allowed-groups**|array||allowed_groups|allowedGroups|
|**--allowed-users**|array||allowed_users|allowedUsers|
|**--connectors**|array||connectors|connectors|
|**--share**|object|printerShare|share|share|
|**--shares**|array||shares|shares|
|**--task-triggers**|array||task_triggers|taskTriggers|

#### <a name="printCreatePrinterShares">Command `az devicescloudprint print create-printer-share`</a>

##### <a name="ParametersprintCreatePrinterShares">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--defaults**|object|printerDefaults|defaults|defaults|
|**--display-name**|string||display_name|displayName|
|**--is-accepting-jobs**|boolean||is_accepting_jobs|isAcceptingJobs|
|**--location**|object|printerLocation|location|location|
|**--manufacturer**|string||manufacturer|manufacturer|
|**--model**|string||model|model|
|**--name**|string||name|name|
|**--status**|object|printerStatus|status|status|
|**--jobs**|array||jobs|jobs|
|**--bottom-margins**|array||bottom_margins|bottomMargins|
|**--collation**|boolean||collation|collation|
|**--color-modes**|array||color_modes|colorModes|
|**--content-types**|array||content_types|contentTypes|
|**--copies-per-job**|object|integerRange|copies_per_job|copiesPerJob|
|**--dpis**|array||dpis|dpis|
|**--duplex-modes**|array||duplex_modes|duplexModes|
|**--feed-directions**|array||feed_directions|feedDirections|
|**--feed-orientations**|array||feed_orientations|feedOrientations|
|**--finishings**|array||finishings|finishings|
|**--input-bins**|array||input_bins|inputBins|
|**--is-color-printing-supported**|boolean||is_color_printing_supported|isColorPrintingSupported|
|**--is-page-range-supported**|boolean||is_page_range_supported|isPageRangeSupported|
|**--left-margins**|array||left_margins|leftMargins|
|**--media-colors**|array||media_colors|mediaColors|
|**--media-sizes**|array||media_sizes|mediaSizes|
|**--media-types**|array||media_types|mediaTypes|
|**--multipage-layouts**|array||multipage_layouts|multipageLayouts|
|**--orientations**|array||orientations|orientations|
|**--output-bins**|array||output_bins|outputBins|
|**--pages-per-sheet**|array||pages_per_sheet|pagesPerSheet|
|**--qualities**|array||qualities|qualities|
|**--right-margins**|array||right_margins|rightMargins|
|**--scalings**|array||scalings|scalings|
|**--supported-color-configurations**|array||supported_color_configurations|supportedColorConfigurations|
|**--supported-copies-per-job**|object|integerRange|supported_copies_per_job|supportedCopiesPerJob|
|**--supported-document-mime-types**|array||supported_document_mime_types|supportedDocumentMimeTypes|
|**--supported-duplex-configurations**|array||supported_duplex_configurations|supportedDuplexConfigurations|
|**--supported-finishings**|array||supported_finishings|supportedFinishings|
|**--supported-media-colors**|array||supported_media_colors|supportedMediaColors|
|**--supported-media-sizes**|array||supported_media_sizes|supportedMediaSizes|
|**--supported-media-types**|array||supported_media_types|supportedMediaTypes|
|**--supported-orientations**|array||supported_orientations|supportedOrientations|
|**--supported-output-bins**|array||supported_output_bins|supportedOutputBins|
|**--supported-pages-per-sheet**|object|integerRange|supported_pages_per_sheet|supportedPagesPerSheet|
|**--supported-presentation-directions**|array||supported_presentation_directions|supportedPresentationDirections|
|**--supported-print-qualities**|array||supported_print_qualities|supportedPrintQualities|
|**--supports-fit-pdf-to-page**|boolean||supports_fit_pdf_to_page|supportsFitPdfToPage|
|**--top-margins**|array||top_margins|topMargins|
|**--allow-all-users**|boolean||allow_all_users|allowAllUsers|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--allowed-groups**|array||allowed_groups|allowedGroups|
|**--allowed-users**|array||allowed_users|allowedUsers|
|**--printer**|object|printer|printer|printer|

#### <a name="printCreateReports">Command `az devicescloudprint print create-report`</a>

##### <a name="ParametersprintCreateReports">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--application-sign-in-detailed-summary**|array||application_sign_in_detailed_summary|applicationSignInDetailedSummary|
|**--credential-user-registration-details**|array||credential_user_registration_details|credentialUserRegistrationDetails|
|**--user-credential-usage-details**|array||user_credential_usage_details|userCredentialUsageDetails|
|**--daily-print-usage-summaries-by-printer**|array||daily_print_usage_summaries_by_printer|dailyPrintUsageSummariesByPrinter|
|**--daily-print-usage-summaries-by-user**|array||daily_print_usage_summaries_by_user|dailyPrintUsageSummariesByUser|
|**--monthly-print-usage-summaries-by-printer**|array||monthly_print_usage_summaries_by_printer|monthlyPrintUsageSummariesByPrinter|
|**--monthly-print-usage-summaries-by-user**|array||monthly_print_usage_summaries_by_user|monthlyPrintUsageSummariesByUser|

#### <a name="printCreateServices">Command `az devicescloudprint print create-service`</a>

##### <a name="ParametersprintCreateServices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--endpoints**|array||endpoints|endpoints|

#### <a name="printCreateShares">Command `az devicescloudprint print create-share`</a>

##### <a name="ParametersprintCreateShares">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--defaults**|object|printerDefaults|defaults|defaults|
|**--display-name**|string||display_name|displayName|
|**--is-accepting-jobs**|boolean||is_accepting_jobs|isAcceptingJobs|
|**--location**|object|printerLocation|location|location|
|**--manufacturer**|string||manufacturer|manufacturer|
|**--model**|string||model|model|
|**--name**|string||name|name|
|**--status**|object|printerStatus|status|status|
|**--jobs**|array||jobs|jobs|
|**--bottom-margins**|array||bottom_margins|bottomMargins|
|**--collation**|boolean||collation|collation|
|**--color-modes**|array||color_modes|colorModes|
|**--content-types**|array||content_types|contentTypes|
|**--copies-per-job**|object|integerRange|copies_per_job|copiesPerJob|
|**--dpis**|array||dpis|dpis|
|**--duplex-modes**|array||duplex_modes|duplexModes|
|**--feed-directions**|array||feed_directions|feedDirections|
|**--feed-orientations**|array||feed_orientations|feedOrientations|
|**--finishings**|array||finishings|finishings|
|**--input-bins**|array||input_bins|inputBins|
|**--is-color-printing-supported**|boolean||is_color_printing_supported|isColorPrintingSupported|
|**--is-page-range-supported**|boolean||is_page_range_supported|isPageRangeSupported|
|**--left-margins**|array||left_margins|leftMargins|
|**--media-colors**|array||media_colors|mediaColors|
|**--media-sizes**|array||media_sizes|mediaSizes|
|**--media-types**|array||media_types|mediaTypes|
|**--multipage-layouts**|array||multipage_layouts|multipageLayouts|
|**--orientations**|array||orientations|orientations|
|**--output-bins**|array||output_bins|outputBins|
|**--pages-per-sheet**|array||pages_per_sheet|pagesPerSheet|
|**--qualities**|array||qualities|qualities|
|**--right-margins**|array||right_margins|rightMargins|
|**--scalings**|array||scalings|scalings|
|**--supported-color-configurations**|array||supported_color_configurations|supportedColorConfigurations|
|**--supported-copies-per-job**|object|integerRange|supported_copies_per_job|supportedCopiesPerJob|
|**--supported-document-mime-types**|array||supported_document_mime_types|supportedDocumentMimeTypes|
|**--supported-duplex-configurations**|array||supported_duplex_configurations|supportedDuplexConfigurations|
|**--supported-finishings**|array||supported_finishings|supportedFinishings|
|**--supported-media-colors**|array||supported_media_colors|supportedMediaColors|
|**--supported-media-sizes**|array||supported_media_sizes|supportedMediaSizes|
|**--supported-media-types**|array||supported_media_types|supportedMediaTypes|
|**--supported-orientations**|array||supported_orientations|supportedOrientations|
|**--supported-output-bins**|array||supported_output_bins|supportedOutputBins|
|**--supported-pages-per-sheet**|object|integerRange|supported_pages_per_sheet|supportedPagesPerSheet|
|**--supported-presentation-directions**|array||supported_presentation_directions|supportedPresentationDirections|
|**--supported-print-qualities**|array||supported_print_qualities|supportedPrintQualities|
|**--supports-fit-pdf-to-page**|boolean||supports_fit_pdf_to_page|supportsFitPdfToPage|
|**--top-margins**|array||top_margins|topMargins|
|**--allow-all-users**|boolean||allow_all_users|allowAllUsers|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--allowed-groups**|array||allowed_groups|allowedGroups|
|**--allowed-users**|array||allowed_users|allowedUsers|
|**--printer**|object|printer|printer|printer|

#### <a name="printCreateTaskDefinitions">Command `az devicescloudprint print create-task-definition`</a>

##### <a name="ParametersprintCreateTaskDefinitions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-by**|object|appIdentity|created_by|createdBy|
|**--display-name**|string||display_name|displayName|
|**--tasks**|array||tasks|tasks|

#### <a name="printDeleteConnectors">Command `az devicescloudprint print delete-connector`</a>

##### <a name="ParametersprintDeleteConnectors">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-connector-id**|string|key: id of printConnector|print_connector_id|printConnector-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="printDeleteOperations">Command `az devicescloudprint print delete-operation`</a>

##### <a name="ParametersprintDeleteOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-operation-id**|string|key: id of printOperation|print_operation_id|printOperation-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="printDeletePrinters">Command `az devicescloudprint print delete-printer`</a>

##### <a name="ParametersprintDeletePrinters">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="printDeletePrinterShares">Command `az devicescloudprint print delete-printer-share`</a>

##### <a name="ParametersprintDeletePrinterShares">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="printDeleteReports">Command `az devicescloudprint print delete-report`</a>

##### <a name="ParametersprintDeleteReports">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--report-root-id**|string|key: id of reportRoot|report_root_id|reportRoot-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="printDeleteServices">Command `az devicescloudprint print delete-service`</a>

##### <a name="ParametersprintDeleteServices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="printDeleteShares">Command `az devicescloudprint print delete-share`</a>

##### <a name="ParametersprintDeleteShares">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="printDeleteTaskDefinitions">Command `az devicescloudprint print delete-task-definition`</a>

##### <a name="ParametersprintDeleteTaskDefinitions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="printListConnectors">Command `az devicescloudprint print list-connector`</a>

##### <a name="ParametersprintListConnectors">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printListOperations">Command `az devicescloudprint print list-operation`</a>

##### <a name="ParametersprintListOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printListPrinters">Command `az devicescloudprint print list-printer`</a>

##### <a name="ParametersprintListPrinters">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printListPrinterShares">Command `az devicescloudprint print list-printer-share`</a>

##### <a name="ParametersprintListPrinterShares">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printListReports">Command `az devicescloudprint print list-report`</a>

##### <a name="ParametersprintListReports">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printListServices">Command `az devicescloudprint print list-service`</a>

##### <a name="ParametersprintListServices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printListShares">Command `az devicescloudprint print list-share`</a>

##### <a name="ParametersprintListShares">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printListTaskDefinitions">Command `az devicescloudprint print list-task-definition`</a>

##### <a name="ParametersprintListTaskDefinitions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printGetConnectors">Command `az devicescloudprint print show-connector`</a>

##### <a name="ParametersprintGetConnectors">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-connector-id**|string|key: id of printConnector|print_connector_id|printConnector-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printGetOperations">Command `az devicescloudprint print show-operation`</a>

##### <a name="ParametersprintGetOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-operation-id**|string|key: id of printOperation|print_operation_id|printOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printGetPrinters">Command `az devicescloudprint print show-printer`</a>

##### <a name="ParametersprintGetPrinters">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printGetPrinterShares">Command `az devicescloudprint print show-printer-share`</a>

##### <a name="ParametersprintGetPrinterShares">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printGetReports">Command `az devicescloudprint print show-report`</a>

##### <a name="ParametersprintGetReports">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--report-root-id**|string|key: id of reportRoot|report_root_id|reportRoot-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printGetServices">Command `az devicescloudprint print show-service`</a>

##### <a name="ParametersprintGetServices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printGetShares">Command `az devicescloudprint print show-share`</a>

##### <a name="ParametersprintGetShares">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printGetTaskDefinitions">Command `az devicescloudprint print show-task-definition`</a>

##### <a name="ParametersprintGetTaskDefinitions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="printUpdateConnectors">Command `az devicescloudprint print update-connector`</a>

##### <a name="ParametersprintUpdateConnectors">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-connector-id**|string|key: id of printConnector|print_connector_id|printConnector-id|
|**--id**|string|Read-only.|id|id|
|**--app-version**|string||app_version|appVersion|
|**--display-name**|string||display_name|displayName|
|**--fully-qualified-domain-name**|string||fully_qualified_domain_name|fullyQualifiedDomainName|
|**--location**|object|printerLocation|location|location|
|**--name**|string||name|name|
|**--operating-system**|string||operating_system|operatingSystem|
|**--registered-date-time**|date-time||registered_date_time|registeredDateTime|
|**--last-connection-time**|date-time||last_connection_time|lastConnectionTime|

#### <a name="printUpdateOperations">Command `az devicescloudprint print update-operation`</a>

##### <a name="ParametersprintUpdateOperations">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-operation-id**|string|key: id of printOperation|print_operation_id|printOperation-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--status**|object|printOperationStatus|status|status|

#### <a name="printUpdatePrinters">Command `az devicescloudprint print update-printer`</a>

##### <a name="ParametersprintUpdatePrinters">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--id**|string|Read-only.|id|id|
|**--defaults**|object|printerDefaults|defaults|defaults|
|**--display-name**|string||display_name|displayName|
|**--is-accepting-jobs**|boolean||is_accepting_jobs|isAcceptingJobs|
|**--location**|object|printerLocation|location|location|
|**--manufacturer**|string||manufacturer|manufacturer|
|**--model**|string||model|model|
|**--name**|string||name|name|
|**--status**|object|printerStatus|status|status|
|**--jobs**|array||jobs|jobs|
|**--bottom-margins**|array||bottom_margins|bottomMargins|
|**--collation**|boolean||collation|collation|
|**--color-modes**|array||color_modes|colorModes|
|**--content-types**|array||content_types|contentTypes|
|**--copies-per-job**|object|integerRange|copies_per_job|copiesPerJob|
|**--dpis**|array||dpis|dpis|
|**--duplex-modes**|array||duplex_modes|duplexModes|
|**--feed-directions**|array||feed_directions|feedDirections|
|**--feed-orientations**|array||feed_orientations|feedOrientations|
|**--finishings**|array||finishings|finishings|
|**--input-bins**|array||input_bins|inputBins|
|**--is-color-printing-supported**|boolean||is_color_printing_supported|isColorPrintingSupported|
|**--is-page-range-supported**|boolean||is_page_range_supported|isPageRangeSupported|
|**--left-margins**|array||left_margins|leftMargins|
|**--media-colors**|array||media_colors|mediaColors|
|**--media-sizes**|array||media_sizes|mediaSizes|
|**--media-types**|array||media_types|mediaTypes|
|**--multipage-layouts**|array||multipage_layouts|multipageLayouts|
|**--orientations**|array||orientations|orientations|
|**--output-bins**|array||output_bins|outputBins|
|**--pages-per-sheet**|array||pages_per_sheet|pagesPerSheet|
|**--qualities**|array||qualities|qualities|
|**--right-margins**|array||right_margins|rightMargins|
|**--scalings**|array||scalings|scalings|
|**--supported-color-configurations**|array||supported_color_configurations|supportedColorConfigurations|
|**--supported-copies-per-job**|object|integerRange|supported_copies_per_job|supportedCopiesPerJob|
|**--supported-document-mime-types**|array||supported_document_mime_types|supportedDocumentMimeTypes|
|**--supported-duplex-configurations**|array||supported_duplex_configurations|supportedDuplexConfigurations|
|**--supported-finishings**|array||supported_finishings|supportedFinishings|
|**--supported-media-colors**|array||supported_media_colors|supportedMediaColors|
|**--supported-media-sizes**|array||supported_media_sizes|supportedMediaSizes|
|**--supported-media-types**|array||supported_media_types|supportedMediaTypes|
|**--supported-orientations**|array||supported_orientations|supportedOrientations|
|**--supported-output-bins**|array||supported_output_bins|supportedOutputBins|
|**--supported-pages-per-sheet**|object|integerRange|supported_pages_per_sheet|supportedPagesPerSheet|
|**--supported-presentation-directions**|array||supported_presentation_directions|supportedPresentationDirections|
|**--supported-print-qualities**|array||supported_print_qualities|supportedPrintQualities|
|**--supports-fit-pdf-to-page**|boolean||supports_fit_pdf_to_page|supportsFitPdfToPage|
|**--top-margins**|array||top_margins|topMargins|
|**--accepting-jobs**|boolean||accepting_jobs|acceptingJobs|
|**--is-shared**|boolean||is_shared|isShared|
|**--registered-date-time**|date-time||registered_date_time|registeredDateTime|
|**--allowed-groups**|array||allowed_groups|allowedGroups|
|**--allowed-users**|array||allowed_users|allowedUsers|
|**--connectors**|array||connectors|connectors|
|**--share**|object|printerShare|share|share|
|**--shares**|array||shares|shares|
|**--task-triggers**|array||task_triggers|taskTriggers|

#### <a name="printUpdatePrinterShares">Command `az devicescloudprint print update-printer-share`</a>

##### <a name="ParametersprintUpdatePrinterShares">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--id**|string|Read-only.|id|id|
|**--defaults**|object|printerDefaults|defaults|defaults|
|**--display-name**|string||display_name|displayName|
|**--is-accepting-jobs**|boolean||is_accepting_jobs|isAcceptingJobs|
|**--location**|object|printerLocation|location|location|
|**--manufacturer**|string||manufacturer|manufacturer|
|**--model**|string||model|model|
|**--name**|string||name|name|
|**--status**|object|printerStatus|status|status|
|**--jobs**|array||jobs|jobs|
|**--bottom-margins**|array||bottom_margins|bottomMargins|
|**--collation**|boolean||collation|collation|
|**--color-modes**|array||color_modes|colorModes|
|**--content-types**|array||content_types|contentTypes|
|**--copies-per-job**|object|integerRange|copies_per_job|copiesPerJob|
|**--dpis**|array||dpis|dpis|
|**--duplex-modes**|array||duplex_modes|duplexModes|
|**--feed-directions**|array||feed_directions|feedDirections|
|**--feed-orientations**|array||feed_orientations|feedOrientations|
|**--finishings**|array||finishings|finishings|
|**--input-bins**|array||input_bins|inputBins|
|**--is-color-printing-supported**|boolean||is_color_printing_supported|isColorPrintingSupported|
|**--is-page-range-supported**|boolean||is_page_range_supported|isPageRangeSupported|
|**--left-margins**|array||left_margins|leftMargins|
|**--media-colors**|array||media_colors|mediaColors|
|**--media-sizes**|array||media_sizes|mediaSizes|
|**--media-types**|array||media_types|mediaTypes|
|**--multipage-layouts**|array||multipage_layouts|multipageLayouts|
|**--orientations**|array||orientations|orientations|
|**--output-bins**|array||output_bins|outputBins|
|**--pages-per-sheet**|array||pages_per_sheet|pagesPerSheet|
|**--qualities**|array||qualities|qualities|
|**--right-margins**|array||right_margins|rightMargins|
|**--scalings**|array||scalings|scalings|
|**--supported-color-configurations**|array||supported_color_configurations|supportedColorConfigurations|
|**--supported-copies-per-job**|object|integerRange|supported_copies_per_job|supportedCopiesPerJob|
|**--supported-document-mime-types**|array||supported_document_mime_types|supportedDocumentMimeTypes|
|**--supported-duplex-configurations**|array||supported_duplex_configurations|supportedDuplexConfigurations|
|**--supported-finishings**|array||supported_finishings|supportedFinishings|
|**--supported-media-colors**|array||supported_media_colors|supportedMediaColors|
|**--supported-media-sizes**|array||supported_media_sizes|supportedMediaSizes|
|**--supported-media-types**|array||supported_media_types|supportedMediaTypes|
|**--supported-orientations**|array||supported_orientations|supportedOrientations|
|**--supported-output-bins**|array||supported_output_bins|supportedOutputBins|
|**--supported-pages-per-sheet**|object|integerRange|supported_pages_per_sheet|supportedPagesPerSheet|
|**--supported-presentation-directions**|array||supported_presentation_directions|supportedPresentationDirections|
|**--supported-print-qualities**|array||supported_print_qualities|supportedPrintQualities|
|**--supports-fit-pdf-to-page**|boolean||supports_fit_pdf_to_page|supportsFitPdfToPage|
|**--top-margins**|array||top_margins|topMargins|
|**--allow-all-users**|boolean||allow_all_users|allowAllUsers|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--allowed-groups**|array||allowed_groups|allowedGroups|
|**--allowed-users**|array||allowed_users|allowedUsers|
|**--printer**|object|printer|printer|printer|

#### <a name="printUpdateReports">Command `az devicescloudprint print update-report`</a>

##### <a name="ParametersprintUpdateReports">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--report-root-id**|string|key: id of reportRoot|report_root_id|reportRoot-id|
|**--id**|string|Read-only.|id|id|
|**--application-sign-in-detailed-summary**|array||application_sign_in_detailed_summary|applicationSignInDetailedSummary|
|**--credential-user-registration-details**|array||credential_user_registration_details|credentialUserRegistrationDetails|
|**--user-credential-usage-details**|array||user_credential_usage_details|userCredentialUsageDetails|
|**--daily-print-usage-summaries-by-printer**|array||daily_print_usage_summaries_by_printer|dailyPrintUsageSummariesByPrinter|
|**--daily-print-usage-summaries-by-user**|array||daily_print_usage_summaries_by_user|dailyPrintUsageSummariesByUser|
|**--monthly-print-usage-summaries-by-printer**|array||monthly_print_usage_summaries_by_printer|monthlyPrintUsageSummariesByPrinter|
|**--monthly-print-usage-summaries-by-user**|array||monthly_print_usage_summaries_by_user|monthlyPrintUsageSummariesByUser|

#### <a name="printUpdateServices">Command `az devicescloudprint print update-service`</a>

##### <a name="ParametersprintUpdateServices">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--id**|string|Read-only.|id|id|
|**--endpoints**|array||endpoints|endpoints|

#### <a name="printUpdateShares">Command `az devicescloudprint print update-share`</a>

##### <a name="ParametersprintUpdateShares">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--id**|string|Read-only.|id|id|
|**--defaults**|object|printerDefaults|defaults|defaults|
|**--display-name**|string||display_name|displayName|
|**--is-accepting-jobs**|boolean||is_accepting_jobs|isAcceptingJobs|
|**--location**|object|printerLocation|location|location|
|**--manufacturer**|string||manufacturer|manufacturer|
|**--model**|string||model|model|
|**--name**|string||name|name|
|**--status**|object|printerStatus|status|status|
|**--jobs**|array||jobs|jobs|
|**--bottom-margins**|array||bottom_margins|bottomMargins|
|**--collation**|boolean||collation|collation|
|**--color-modes**|array||color_modes|colorModes|
|**--content-types**|array||content_types|contentTypes|
|**--copies-per-job**|object|integerRange|copies_per_job|copiesPerJob|
|**--dpis**|array||dpis|dpis|
|**--duplex-modes**|array||duplex_modes|duplexModes|
|**--feed-directions**|array||feed_directions|feedDirections|
|**--feed-orientations**|array||feed_orientations|feedOrientations|
|**--finishings**|array||finishings|finishings|
|**--input-bins**|array||input_bins|inputBins|
|**--is-color-printing-supported**|boolean||is_color_printing_supported|isColorPrintingSupported|
|**--is-page-range-supported**|boolean||is_page_range_supported|isPageRangeSupported|
|**--left-margins**|array||left_margins|leftMargins|
|**--media-colors**|array||media_colors|mediaColors|
|**--media-sizes**|array||media_sizes|mediaSizes|
|**--media-types**|array||media_types|mediaTypes|
|**--multipage-layouts**|array||multipage_layouts|multipageLayouts|
|**--orientations**|array||orientations|orientations|
|**--output-bins**|array||output_bins|outputBins|
|**--pages-per-sheet**|array||pages_per_sheet|pagesPerSheet|
|**--qualities**|array||qualities|qualities|
|**--right-margins**|array||right_margins|rightMargins|
|**--scalings**|array||scalings|scalings|
|**--supported-color-configurations**|array||supported_color_configurations|supportedColorConfigurations|
|**--supported-copies-per-job**|object|integerRange|supported_copies_per_job|supportedCopiesPerJob|
|**--supported-document-mime-types**|array||supported_document_mime_types|supportedDocumentMimeTypes|
|**--supported-duplex-configurations**|array||supported_duplex_configurations|supportedDuplexConfigurations|
|**--supported-finishings**|array||supported_finishings|supportedFinishings|
|**--supported-media-colors**|array||supported_media_colors|supportedMediaColors|
|**--supported-media-sizes**|array||supported_media_sizes|supportedMediaSizes|
|**--supported-media-types**|array||supported_media_types|supportedMediaTypes|
|**--supported-orientations**|array||supported_orientations|supportedOrientations|
|**--supported-output-bins**|array||supported_output_bins|supportedOutputBins|
|**--supported-pages-per-sheet**|object|integerRange|supported_pages_per_sheet|supportedPagesPerSheet|
|**--supported-presentation-directions**|array||supported_presentation_directions|supportedPresentationDirections|
|**--supported-print-qualities**|array||supported_print_qualities|supportedPrintQualities|
|**--supports-fit-pdf-to-page**|boolean||supports_fit_pdf_to_page|supportsFitPdfToPage|
|**--top-margins**|array||top_margins|topMargins|
|**--allow-all-users**|boolean||allow_all_users|allowAllUsers|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--allowed-groups**|array||allowed_groups|allowedGroups|
|**--allowed-users**|array||allowed_users|allowedUsers|
|**--printer**|object|printer|printer|printer|

#### <a name="printUpdateTaskDefinitions">Command `az devicescloudprint print update-task-definition`</a>

##### <a name="ParametersprintUpdateTaskDefinitions">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--id**|string|Read-only.|id|id|
|**--created-by**|object|appIdentity|created_by|createdBy|
|**--display-name**|string||display_name|displayName|
|**--tasks**|array||tasks|tasks|

### group `az devicescloudprint print-print`
#### <a name="print.printGetPrint">Command `az devicescloudprint print-print show-print`</a>

##### <a name="Parametersprint.printGetPrint">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printUpdatePrint">Command `az devicescloudprint print-print update-print`</a>

##### <a name="Parametersprint.printUpdatePrint">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--connectors**|array||connectors|connectors|
|**--operations**|array||operations|operations|
|**--printers**|array||printers|printers|
|**--printer-shares**|array||printer_shares|printerShares|
|**--reports**|array||reports|reports|
|**--services**|array||services|services|
|**--shares**|array||shares|shares|
|**--task-definitions**|array||task_definitions|taskDefinitions|
|**--document-conversion-enabled**|boolean||document_conversion_enabled|documentConversionEnabled|

### group `az devicescloudprint print-printer`
#### <a name="print.printerscreate">Command `az devicescloudprint print-printer create`</a>

##### <a name="Parametersprint.printerscreate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--display-name**|string||display_name|displayName|
|**--manufacturer**|string||manufacturer|manufacturer|
|**--model**|string||model|model|
|**--physical-device-id**|string||physical_device_id|physicalDeviceId|
|**--has-physical-device**|boolean||has_physical_device|hasPhysicalDevice|
|**--certificate-signing-request**|object|printCertificateSigningRequest|certificate_signing_request|certificateSigningRequest|
|**--connector-id**|string||connector_id|connectorId|

#### <a name="print.printersCreateAllowedGroups">Command `az devicescloudprint print-printer create-allowed-group`</a>

##### <a name="Parametersprint.printersCreateAllowedGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

#### <a name="print.printersCreateAllowedUsers">Command `az devicescloudprint print-printer create-allowed-user`</a>

##### <a name="Parametersprint.printersCreateAllowedUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--ip-address**|string||ip_address|ipAddress|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

#### <a name="print.printersCreateRefConnectors">Command `az devicescloudprint print-printer create-ref-connector`</a>

##### <a name="Parametersprint.printersCreateRefConnectors">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="print.printersCreateRefShares">Command `az devicescloudprint print-printer create-ref-share`</a>

##### <a name="Parametersprint.printersCreateRefShares">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--body**|dictionary|New navigation property ref value|body|body|

#### <a name="print.printersCreateTaskTriggers">Command `az devicescloudprint print-printer create-task-trigger`</a>

##### <a name="Parametersprint.printersCreateTaskTriggers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--id**|string|Read-only.|id|id|
|**--event**|choice||event|event|
|**--definition**|object|printTaskDefinition|definition|definition|

#### <a name="print.printersDeleteAllowedGroups">Command `az devicescloudprint print-printer delete-allowed-group`</a>

##### <a name="Parametersprint.printersDeleteAllowedGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="print.printersDeleteAllowedUsers">Command `az devicescloudprint print-printer delete-allowed-user`</a>

##### <a name="Parametersprint.printersDeleteAllowedUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="print.printersDeleteRefShare">Command `az devicescloudprint print-printer delete-ref-share`</a>

##### <a name="Parametersprint.printersDeleteRefShare">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="print.printersDeleteTaskTriggers">Command `az devicescloudprint print-printer delete-task-trigger`</a>

##### <a name="Parametersprint.printersDeleteTaskTriggers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-task-trigger-id**|string|key: id of printTaskTrigger|print_task_trigger_id|printTaskTrigger-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="print.printersListAllowedGroups">Command `az devicescloudprint print-printer list-allowed-group`</a>

##### <a name="Parametersprint.printersListAllowedGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printersListAllowedUsers">Command `az devicescloudprint print-printer list-allowed-user`</a>

##### <a name="Parametersprint.printersListAllowedUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printersListConnectors">Command `az devicescloudprint print-printer list-connector`</a>

##### <a name="Parametersprint.printersListConnectors">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printersListRefConnectors">Command `az devicescloudprint print-printer list-ref-connector`</a>

##### <a name="Parametersprint.printersListRefConnectors">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="print.printersListRefShares">Command `az devicescloudprint print-printer list-ref-share`</a>

##### <a name="Parametersprint.printersListRefShares">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

#### <a name="print.printersListShares">Command `az devicescloudprint print-printer list-share`</a>

##### <a name="Parametersprint.printersListShares">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printersListTaskTriggers">Command `az devicescloudprint print-printer list-task-trigger`</a>

##### <a name="Parametersprint.printersListTaskTriggers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printersresetDefaults">Command `az devicescloudprint print-printer reset-default`</a>

##### <a name="Parametersprint.printersresetDefaults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|

#### <a name="print.printersrestoreFactoryDefaults">Command `az devicescloudprint print-printer restore-factory-default`</a>

##### <a name="Parametersprint.printersrestoreFactoryDefaults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|

#### <a name="print.printersSetRefShare">Command `az devicescloudprint print-printer set-ref-share`</a>

##### <a name="Parametersprint.printersSetRefShare">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="print.printersGetAllowedGroups">Command `az devicescloudprint print-printer show-allowed-group`</a>

##### <a name="Parametersprint.printersGetAllowedGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printersGetAllowedUsers">Command `az devicescloudprint print-printer show-allowed-user`</a>

##### <a name="Parametersprint.printersGetAllowedUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printersgetCapabilities">Command `az devicescloudprint print-printer show-capability`</a>

##### <a name="Parametersprint.printersgetCapabilities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|

#### <a name="print.printersGetRefShare">Command `az devicescloudprint print-printer show-ref-share`</a>

##### <a name="Parametersprint.printersGetRefShare">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|

#### <a name="print.printersGetShare">Command `az devicescloudprint print-printer show-share`</a>

##### <a name="Parametersprint.printersGetShare">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printersGetTaskTriggers">Command `az devicescloudprint print-printer show-task-trigger`</a>

##### <a name="Parametersprint.printersGetTaskTriggers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-task-trigger-id**|string|key: id of printTaskTrigger|print_task_trigger_id|printTaskTrigger-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printersUpdateAllowedGroups">Command `az devicescloudprint print-printer update-allowed-group`</a>

##### <a name="Parametersprint.printersUpdateAllowedGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

#### <a name="print.printersUpdateAllowedUsers">Command `az devicescloudprint print-printer update-allowed-user`</a>

##### <a name="Parametersprint.printersUpdateAllowedUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--ip-address**|string||ip_address|ipAddress|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

#### <a name="print.printersUpdateTaskTriggers">Command `az devicescloudprint print-printer update-task-trigger`</a>

##### <a name="Parametersprint.printersUpdateTaskTriggers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-task-trigger-id**|string|key: id of printTaskTrigger|print_task_trigger_id|printTaskTrigger-id|
|**--id**|string|Read-only.|id|id|
|**--event**|choice||event|event|
|**--definition**|object|printTaskDefinition|definition|definition|

### group `az devicescloudprint print-printer-share`
#### <a name="print.printerSharesCreateAllowedGroups">Command `az devicescloudprint print-printer-share create-allowed-group`</a>

##### <a name="Parametersprint.printerSharesCreateAllowedGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

#### <a name="print.printerSharesCreateAllowedUsers">Command `az devicescloudprint print-printer-share create-allowed-user`</a>

##### <a name="Parametersprint.printerSharesCreateAllowedUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--ip-address**|string||ip_address|ipAddress|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

#### <a name="print.printerSharesDeleteAllowedGroups">Command `az devicescloudprint print-printer-share delete-allowed-group`</a>

##### <a name="Parametersprint.printerSharesDeleteAllowedGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="print.printerSharesDeleteAllowedUsers">Command `az devicescloudprint print-printer-share delete-allowed-user`</a>

##### <a name="Parametersprint.printerSharesDeleteAllowedUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="print.printerSharesDeleteRefPrinter">Command `az devicescloudprint print-printer-share delete-ref-printer`</a>

##### <a name="Parametersprint.printerSharesDeleteRefPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="print.printerSharesListAllowedGroups">Command `az devicescloudprint print-printer-share list-allowed-group`</a>

##### <a name="Parametersprint.printerSharesListAllowedGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printerSharesListAllowedUsers">Command `az devicescloudprint print-printer-share list-allowed-user`</a>

##### <a name="Parametersprint.printerSharesListAllowedUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printerSharesSetRefPrinter">Command `az devicescloudprint print-printer-share set-ref-printer`</a>

##### <a name="Parametersprint.printerSharesSetRefPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="print.printerSharesGetAllowedGroups">Command `az devicescloudprint print-printer-share show-allowed-group`</a>

##### <a name="Parametersprint.printerSharesGetAllowedGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printerSharesGetAllowedUsers">Command `az devicescloudprint print-printer-share show-allowed-user`</a>

##### <a name="Parametersprint.printerSharesGetAllowedUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printerSharesGetPrinter">Command `az devicescloudprint print-printer-share show-printer`</a>

##### <a name="Parametersprint.printerSharesGetPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printerSharesGetRefPrinter">Command `az devicescloudprint print-printer-share show-ref-printer`</a>

##### <a name="Parametersprint.printerSharesGetRefPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

#### <a name="print.printerSharesUpdateAllowedGroups">Command `az devicescloudprint print-printer-share update-allowed-group`</a>

##### <a name="Parametersprint.printerSharesUpdateAllowedGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

#### <a name="print.printerSharesUpdateAllowedUsers">Command `az devicescloudprint print-printer-share update-allowed-user`</a>

##### <a name="Parametersprint.printerSharesUpdateAllowedUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--ip-address**|string||ip_address|ipAddress|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### group `az devicescloudprint print-printer-share-printer`
#### <a name="print.printerShares.printerresetDefaults">Command `az devicescloudprint print-printer-share-printer reset-default`</a>

##### <a name="Parametersprint.printerShares.printerresetDefaults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

#### <a name="print.printerShares.printerrestoreFactoryDefaults">Command `az devicescloudprint print-printer-share-printer restore-factory-default`</a>

##### <a name="Parametersprint.printerShares.printerrestoreFactoryDefaults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

#### <a name="print.printerShares.printergetCapabilities">Command `az devicescloudprint print-printer-share-printer show-capability`</a>

##### <a name="Parametersprint.printerShares.printergetCapabilities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

### group `az devicescloudprint print-printer-task-trigger`
#### <a name="print.printers.taskTriggersDeleteRefDefinition">Command `az devicescloudprint print-printer-task-trigger delete-ref-definition`</a>

##### <a name="Parametersprint.printers.taskTriggersDeleteRefDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-task-trigger-id**|string|key: id of printTaskTrigger|print_task_trigger_id|printTaskTrigger-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="print.printers.taskTriggersSetRefDefinition">Command `az devicescloudprint print-printer-task-trigger set-ref-definition`</a>

##### <a name="Parametersprint.printers.taskTriggersSetRefDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-task-trigger-id**|string|key: id of printTaskTrigger|print_task_trigger_id|printTaskTrigger-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="print.printers.taskTriggersGetDefinition">Command `az devicescloudprint print-printer-task-trigger show-definition`</a>

##### <a name="Parametersprint.printers.taskTriggersGetDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-task-trigger-id**|string|key: id of printTaskTrigger|print_task_trigger_id|printTaskTrigger-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.printers.taskTriggersGetRefDefinition">Command `az devicescloudprint print-printer-task-trigger show-ref-definition`</a>

##### <a name="Parametersprint.printers.taskTriggersGetRefDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-task-trigger-id**|string|key: id of printTaskTrigger|print_task_trigger_id|printTaskTrigger-id|

### group `az devicescloudprint print-report`
#### <a name="print.reportsgetGroupArchivedPrintJobs">Command `az devicescloudprint print-report show-group-archived-print-job`</a>

##### <a name="Parametersprint.reportsgetGroupArchivedPrintJobs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string||group_id|groupId|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|

#### <a name="print.reportsgetGroupPrintUsageSummary">Command `az devicescloudprint print-report show-group-print-usage-summary`</a>

##### <a name="Parametersprint.reportsgetGroupPrintUsageSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string||group_id|groupId|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|

#### <a name="print.reportsgetOverallPrintUsageSummary">Command `az devicescloudprint print-report show-overall-print-usage-summary`</a>

##### <a name="Parametersprint.reportsgetOverallPrintUsageSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|
|**--top-lists-size**|integer||top_lists_size|topListsSize|

#### <a name="print.reportsgetPrintUsageSummariesByTimeSpan">Command `az devicescloudprint print-report show-print-usage-summary`</a>

##### <a name="Parametersprint.reportsgetPrintUsageSummariesByTimeSpan">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|
|**--time-span-in-minutes**|integer||time_span_in_minutes|timeSpanInMinutes|

#### <a name="print.reportsgetPrintUsageSummariesByGroup">Command `az devicescloudprint print-report show-print-usage-summary`</a>

##### <a name="Parametersprint.reportsgetPrintUsageSummariesByGroup">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="print.reportsgetPrintUsageSummariesByPrinter">Command `az devicescloudprint print-report show-print-usage-summary`</a>

##### <a name="Parametersprint.reportsgetPrintUsageSummariesByPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="print.reportsgetPrintUsageSummariesByUser">Command `az devicescloudprint print-report show-print-usage-summary`</a>

##### <a name="Parametersprint.reportsgetPrintUsageSummariesByUser">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
#### <a name="print.reportsgetPrinterArchivedPrintJobs">Command `az devicescloudprint print-report show-printer-archived-print-job`</a>

##### <a name="Parametersprint.reportsgetPrinterArchivedPrintJobs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string||printer_id|printerId|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|

#### <a name="print.reportsgetPrinterUsageSummary">Command `az devicescloudprint print-report show-printer-usage-summary`</a>

##### <a name="Parametersprint.reportsgetPrinterUsageSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string||printer_id|printerId|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|

#### <a name="print.reportsgetUserArchivedPrintJobs">Command `az devicescloudprint print-report show-user-archived-print-job`</a>

##### <a name="Parametersprint.reportsgetUserArchivedPrintJobs">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string||user_id|userId|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|

#### <a name="print.reportsgetUserPrintUsageSummary">Command `az devicescloudprint print-report show-user-print-usage-summary`</a>

##### <a name="Parametersprint.reportsgetUserPrintUsageSummary">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string||user_id|userId|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|

### group `az devicescloudprint print-service`
#### <a name="print.servicesCreateEndpoints">Command `az devicescloudprint print-service create-endpoint`</a>

##### <a name="Parametersprint.servicesCreateEndpoints">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--uri**|string||uri|uri|

#### <a name="print.servicesDeleteEndpoints">Command `az devicescloudprint print-service delete-endpoint`</a>

##### <a name="Parametersprint.servicesDeleteEndpoints">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--print-service-endpoint-id**|string|key: id of printServiceEndpoint|print_service_endpoint_id|printServiceEndpoint-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="print.servicesListEndpoints">Command `az devicescloudprint print-service list-endpoint`</a>

##### <a name="Parametersprint.servicesListEndpoints">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.servicesGetEndpoints">Command `az devicescloudprint print-service show-endpoint`</a>

##### <a name="Parametersprint.servicesGetEndpoints">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--print-service-endpoint-id**|string|key: id of printServiceEndpoint|print_service_endpoint_id|printServiceEndpoint-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.servicesUpdateEndpoints">Command `az devicescloudprint print-service update-endpoint`</a>

##### <a name="Parametersprint.servicesUpdateEndpoints">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--print-service-endpoint-id**|string|key: id of printServiceEndpoint|print_service_endpoint_id|printServiceEndpoint-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--uri**|string||uri|uri|

### group `az devicescloudprint print-share`
#### <a name="print.sharesCreateAllowedGroups">Command `az devicescloudprint print-share create-allowed-group`</a>

##### <a name="Parametersprint.sharesCreateAllowedGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

#### <a name="print.sharesCreateAllowedUsers">Command `az devicescloudprint print-share create-allowed-user`</a>

##### <a name="Parametersprint.sharesCreateAllowedUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--ip-address**|string||ip_address|ipAddress|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

#### <a name="print.sharesDeleteAllowedGroups">Command `az devicescloudprint print-share delete-allowed-group`</a>

##### <a name="Parametersprint.sharesDeleteAllowedGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="print.sharesDeleteAllowedUsers">Command `az devicescloudprint print-share delete-allowed-user`</a>

##### <a name="Parametersprint.sharesDeleteAllowedUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="print.sharesDeleteRefPrinter">Command `az devicescloudprint print-share delete-ref-printer`</a>

##### <a name="Parametersprint.sharesDeleteRefPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="print.sharesListAllowedGroups">Command `az devicescloudprint print-share list-allowed-group`</a>

##### <a name="Parametersprint.sharesListAllowedGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.sharesListAllowedUsers">Command `az devicescloudprint print-share list-allowed-user`</a>

##### <a name="Parametersprint.sharesListAllowedUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.sharesSetRefPrinter">Command `az devicescloudprint print-share set-ref-printer`</a>

##### <a name="Parametersprint.sharesSetRefPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="print.sharesGetAllowedGroups">Command `az devicescloudprint print-share show-allowed-group`</a>

##### <a name="Parametersprint.sharesGetAllowedGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.sharesGetAllowedUsers">Command `az devicescloudprint print-share show-allowed-user`</a>

##### <a name="Parametersprint.sharesGetAllowedUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.sharesGetPrinter">Command `az devicescloudprint print-share show-printer`</a>

##### <a name="Parametersprint.sharesGetPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.sharesGetRefPrinter">Command `az devicescloudprint print-share show-ref-printer`</a>

##### <a name="Parametersprint.sharesGetRefPrinter">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

#### <a name="print.sharesUpdateAllowedGroups">Command `az devicescloudprint print-share update-allowed-group`</a>

##### <a name="Parametersprint.sharesUpdateAllowedGroups">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

#### <a name="print.sharesUpdateAllowedUsers">Command `az devicescloudprint print-share update-allowed-user`</a>

##### <a name="Parametersprint.sharesUpdateAllowedUsers">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--ip-address**|string||ip_address|ipAddress|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### group `az devicescloudprint print-share-printer`
#### <a name="print.shares.printerresetDefaults">Command `az devicescloudprint print-share-printer reset-default`</a>

##### <a name="Parametersprint.shares.printerresetDefaults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

#### <a name="print.shares.printerrestoreFactoryDefaults">Command `az devicescloudprint print-share-printer restore-factory-default`</a>

##### <a name="Parametersprint.shares.printerrestoreFactoryDefaults">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

#### <a name="print.shares.printergetCapabilities">Command `az devicescloudprint print-share-printer show-capability`</a>

##### <a name="Parametersprint.shares.printergetCapabilities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

### group `az devicescloudprint print-task-definition`
#### <a name="print.taskDefinitionsCreateTasks">Command `az devicescloudprint print-task-definition create-task`</a>

##### <a name="Parametersprint.taskDefinitionsCreateTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--id**|string|Read-only.|id|id|
|**--parent-url**|string||parent_url|parentUrl|
|**--status**|object|printTaskStatus|status|status|
|**--definition**|object|printTaskDefinition|definition|definition|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--event**|choice||event|event|
|**--microsoft-graph-print-task-definition**|object|printTaskDefinition|microsoft_graph_print_task_definition|definition|

#### <a name="print.taskDefinitionsDeleteTasks">Command `az devicescloudprint print-task-definition delete-task`</a>

##### <a name="Parametersprint.taskDefinitionsDeleteTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="print.taskDefinitionsListTasks">Command `az devicescloudprint print-task-definition list-task`</a>

##### <a name="Parametersprint.taskDefinitionsListTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.taskDefinitionsGetTasks">Command `az devicescloudprint print-task-definition show-task`</a>

##### <a name="Parametersprint.taskDefinitionsGetTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.taskDefinitionsUpdateTasks">Command `az devicescloudprint print-task-definition update-task`</a>

##### <a name="Parametersprint.taskDefinitionsUpdateTasks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--id**|string|Read-only.|id|id|
|**--parent-url**|string||parent_url|parentUrl|
|**--status**|object|printTaskStatus|status|status|
|**--definition**|object|printTaskDefinition|definition|definition|
|**--microsoft-graph-entity-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--event**|choice||event|event|
|**--microsoft-graph-print-task-definition**|object|printTaskDefinition|microsoft_graph_print_task_definition|definition|

### group `az devicescloudprint print-task-definition-task`
#### <a name="print.taskDefinitions.tasksDeleteRefDefinition">Command `az devicescloudprint print-task-definition-task delete-ref-definition`</a>

##### <a name="Parametersprint.taskDefinitions.tasksDeleteRefDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="print.taskDefinitions.tasksDeleteRefTrigger">Command `az devicescloudprint print-task-definition-task delete-ref-trigger`</a>

##### <a name="Parametersprint.taskDefinitions.tasksDeleteRefTrigger">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

#### <a name="print.taskDefinitions.tasksSetRefDefinition">Command `az devicescloudprint print-task-definition-task set-ref-definition`</a>

##### <a name="Parametersprint.taskDefinitions.tasksSetRefDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="print.taskDefinitions.tasksSetRefTrigger">Command `az devicescloudprint print-task-definition-task set-ref-trigger`</a>

##### <a name="Parametersprint.taskDefinitions.tasksSetRefTrigger">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--body**|dictionary|New navigation property ref values|body|body|

#### <a name="print.taskDefinitions.tasksGetDefinition">Command `az devicescloudprint print-task-definition-task show-definition`</a>

##### <a name="Parametersprint.taskDefinitions.tasksGetDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

#### <a name="print.taskDefinitions.tasksGetRefDefinition">Command `az devicescloudprint print-task-definition-task show-ref-definition`</a>

##### <a name="Parametersprint.taskDefinitions.tasksGetRefDefinition">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|

#### <a name="print.taskDefinitions.tasksGetRefTrigger">Command `az devicescloudprint print-task-definition-task show-ref-trigger`</a>

##### <a name="Parametersprint.taskDefinitions.tasksGetRefTrigger">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|

#### <a name="print.taskDefinitions.tasksGetTrigger">Command `az devicescloudprint print-task-definition-task show-trigger`</a>

##### <a name="Parametersprint.taskDefinitions.tasksGetTrigger">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|
