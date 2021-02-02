# Azure CLI Module Creation Report

### devicescloudprint print create-connector

create-connector a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-connector|CreateConnectors|

#### Parameters
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
|**--device-health-last-connection-time**|date-time||last_connection_time|lastConnectionTime|

### devicescloudprint print create-operation

create-operation a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-operation|CreateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--status-description**|string||description|description|
|**--status-state**|choice||state|state|

### devicescloudprint print create-printer

create-printer a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-printer|CreatePrinters|

#### Parameters
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
|**--capabilities-bottom-margins**|array||bottom_margins|bottomMargins|
|**--capabilities-collation**|boolean||collation|collation|
|**--capabilities-color-modes**|array||color_modes|colorModes|
|**--capabilities-content-types**|array||content_types|contentTypes|
|**--capabilities-copies-per-job**|object|integerRange|copies_per_job|copiesPerJob|
|**--capabilities-dpis**|array||dpis|dpis|
|**--capabilities-duplex-modes**|array||duplex_modes|duplexModes|
|**--capabilities-feed-directions**|array||feed_directions|feedDirections|
|**--capabilities-feed-orientations**|array||feed_orientations|feedOrientations|
|**--capabilities-finishings**|array||finishings|finishings|
|**--capabilities-input-bins**|array||input_bins|inputBins|
|**--capabilities-is-color-printing-supported**|boolean||is_color_printing_supported|isColorPrintingSupported|
|**--capabilities-is-page-range-supported**|boolean||is_page_range_supported|isPageRangeSupported|
|**--capabilities-left-margins**|array||left_margins|leftMargins|
|**--capabilities-media-colors**|array||media_colors|mediaColors|
|**--capabilities-media-sizes**|array||media_sizes|mediaSizes|
|**--capabilities-media-types**|array||media_types|mediaTypes|
|**--capabilities-multipage-layouts**|array||multipage_layouts|multipageLayouts|
|**--capabilities-orientations**|array||orientations|orientations|
|**--capabilities-output-bins**|array||output_bins|outputBins|
|**--capabilities-pages-per-sheet**|array||pages_per_sheet|pagesPerSheet|
|**--capabilities-qualities**|array||qualities|qualities|
|**--capabilities-right-margins**|array||right_margins|rightMargins|
|**--capabilities-scalings**|array||scalings|scalings|
|**--capabilities-supported-color-configurations**|array||supported_color_configurations|supportedColorConfigurations|
|**--capabilities-supported-copies-per-job**|object|integerRange|supported_copies_per_job|supportedCopiesPerJob|
|**--capabilities-supported-document-mime-types**|array||supported_document_mime_types|supportedDocumentMimeTypes|
|**--capabilities-supported-duplex-configurations**|array||supported_duplex_configurations|supportedDuplexConfigurations|
|**--capabilities-supported-finishings**|array||supported_finishings|supportedFinishings|
|**--capabilities-supported-media-colors**|array||supported_media_colors|supportedMediaColors|
|**--capabilities-supported-media-sizes**|array||supported_media_sizes|supportedMediaSizes|
|**--capabilities-supported-media-types**|array||supported_media_types|supportedMediaTypes|
|**--capabilities-supported-orientations**|array||supported_orientations|supportedOrientations|
|**--capabilities-supported-output-bins**|array||supported_output_bins|supportedOutputBins|
|**--capabilities-supported-pages-per-sheet**|object|integerRange|supported_pages_per_sheet|supportedPagesPerSheet|
|**--capabilities-supported-presentation-directions**|array||supported_presentation_directions|supportedPresentationDirections|
|**--capabilities-supported-print-qualities**|array||supported_print_qualities|supportedPrintQualities|
|**--capabilities-supports-fit-pdf-to-page**|boolean||supports_fit_pdf_to_page|supportsFitPdfToPage|
|**--capabilities-top-margins**|array||top_margins|topMargins|
|**--accepting-jobs**|boolean||accepting_jobs|acceptingJobs|
|**--is-shared**|boolean||is_shared|isShared|
|**--registered-date-time**|date-time||registered_date_time|registeredDateTime|
|**--allowed-groups**|array||allowed_groups|allowedGroups|
|**--allowed-users**|array||allowed_users|allowedUsers|
|**--connectors**|array||connectors|connectors|
|**--share**|object|printerShare|share|share|
|**--shares**|array||shares|shares|
|**--task-triggers**|array||task_triggers|taskTriggers|

### devicescloudprint print create-printer-share

create-printer-share a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-printer-share|CreatePrinterShares|

#### Parameters
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
|**--capabilities-bottom-margins**|array||bottom_margins|bottomMargins|
|**--capabilities-collation**|boolean||collation|collation|
|**--capabilities-color-modes**|array||color_modes|colorModes|
|**--capabilities-content-types**|array||content_types|contentTypes|
|**--capabilities-copies-per-job**|object|integerRange|copies_per_job|copiesPerJob|
|**--capabilities-dpis**|array||dpis|dpis|
|**--capabilities-duplex-modes**|array||duplex_modes|duplexModes|
|**--capabilities-feed-directions**|array||feed_directions|feedDirections|
|**--capabilities-feed-orientations**|array||feed_orientations|feedOrientations|
|**--capabilities-finishings**|array||finishings|finishings|
|**--capabilities-input-bins**|array||input_bins|inputBins|
|**--capabilities-is-color-printing-supported**|boolean||is_color_printing_supported|isColorPrintingSupported|
|**--capabilities-is-page-range-supported**|boolean||is_page_range_supported|isPageRangeSupported|
|**--capabilities-left-margins**|array||left_margins|leftMargins|
|**--capabilities-media-colors**|array||media_colors|mediaColors|
|**--capabilities-media-sizes**|array||media_sizes|mediaSizes|
|**--capabilities-media-types**|array||media_types|mediaTypes|
|**--capabilities-multipage-layouts**|array||multipage_layouts|multipageLayouts|
|**--capabilities-orientations**|array||orientations|orientations|
|**--capabilities-output-bins**|array||output_bins|outputBins|
|**--capabilities-pages-per-sheet**|array||pages_per_sheet|pagesPerSheet|
|**--capabilities-qualities**|array||qualities|qualities|
|**--capabilities-right-margins**|array||right_margins|rightMargins|
|**--capabilities-scalings**|array||scalings|scalings|
|**--capabilities-supported-color-configurations**|array||supported_color_configurations|supportedColorConfigurations|
|**--capabilities-supported-copies-per-job**|object|integerRange|supported_copies_per_job|supportedCopiesPerJob|
|**--capabilities-supported-document-mime-types**|array||supported_document_mime_types|supportedDocumentMimeTypes|
|**--capabilities-supported-duplex-configurations**|array||supported_duplex_configurations|supportedDuplexConfigurations|
|**--capabilities-supported-finishings**|array||supported_finishings|supportedFinishings|
|**--capabilities-supported-media-colors**|array||supported_media_colors|supportedMediaColors|
|**--capabilities-supported-media-sizes**|array||supported_media_sizes|supportedMediaSizes|
|**--capabilities-supported-media-types**|array||supported_media_types|supportedMediaTypes|
|**--capabilities-supported-orientations**|array||supported_orientations|supportedOrientations|
|**--capabilities-supported-output-bins**|array||supported_output_bins|supportedOutputBins|
|**--capabilities-supported-pages-per-sheet**|object|integerRange|supported_pages_per_sheet|supportedPagesPerSheet|
|**--capabilities-supported-presentation-directions**|array||supported_presentation_directions|supportedPresentationDirections|
|**--capabilities-supported-print-qualities**|array||supported_print_qualities|supportedPrintQualities|
|**--capabilities-supports-fit-pdf-to-page**|boolean||supports_fit_pdf_to_page|supportsFitPdfToPage|
|**--capabilities-top-margins**|array||top_margins|topMargins|
|**--allow-all-users**|boolean||allow_all_users|allowAllUsers|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--allowed-groups**|array||allowed_groups|allowedGroups|
|**--allowed-users**|array||allowed_users|allowedUsers|
|**--printer**|object|printer|printer|printer|

### devicescloudprint print create-report

create-report a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-report|CreateReports|

#### Parameters
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

### devicescloudprint print create-service

create-service a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-service|CreateServices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--endpoints**|array||endpoints|endpoints|

### devicescloudprint print create-share

create-share a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-share|CreateShares|

#### Parameters
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
|**--capabilities-bottom-margins**|array||bottom_margins|bottomMargins|
|**--capabilities-collation**|boolean||collation|collation|
|**--capabilities-color-modes**|array||color_modes|colorModes|
|**--capabilities-content-types**|array||content_types|contentTypes|
|**--capabilities-copies-per-job**|object|integerRange|copies_per_job|copiesPerJob|
|**--capabilities-dpis**|array||dpis|dpis|
|**--capabilities-duplex-modes**|array||duplex_modes|duplexModes|
|**--capabilities-feed-directions**|array||feed_directions|feedDirections|
|**--capabilities-feed-orientations**|array||feed_orientations|feedOrientations|
|**--capabilities-finishings**|array||finishings|finishings|
|**--capabilities-input-bins**|array||input_bins|inputBins|
|**--capabilities-is-color-printing-supported**|boolean||is_color_printing_supported|isColorPrintingSupported|
|**--capabilities-is-page-range-supported**|boolean||is_page_range_supported|isPageRangeSupported|
|**--capabilities-left-margins**|array||left_margins|leftMargins|
|**--capabilities-media-colors**|array||media_colors|mediaColors|
|**--capabilities-media-sizes**|array||media_sizes|mediaSizes|
|**--capabilities-media-types**|array||media_types|mediaTypes|
|**--capabilities-multipage-layouts**|array||multipage_layouts|multipageLayouts|
|**--capabilities-orientations**|array||orientations|orientations|
|**--capabilities-output-bins**|array||output_bins|outputBins|
|**--capabilities-pages-per-sheet**|array||pages_per_sheet|pagesPerSheet|
|**--capabilities-qualities**|array||qualities|qualities|
|**--capabilities-right-margins**|array||right_margins|rightMargins|
|**--capabilities-scalings**|array||scalings|scalings|
|**--capabilities-supported-color-configurations**|array||supported_color_configurations|supportedColorConfigurations|
|**--capabilities-supported-copies-per-job**|object|integerRange|supported_copies_per_job|supportedCopiesPerJob|
|**--capabilities-supported-document-mime-types**|array||supported_document_mime_types|supportedDocumentMimeTypes|
|**--capabilities-supported-duplex-configurations**|array||supported_duplex_configurations|supportedDuplexConfigurations|
|**--capabilities-supported-finishings**|array||supported_finishings|supportedFinishings|
|**--capabilities-supported-media-colors**|array||supported_media_colors|supportedMediaColors|
|**--capabilities-supported-media-sizes**|array||supported_media_sizes|supportedMediaSizes|
|**--capabilities-supported-media-types**|array||supported_media_types|supportedMediaTypes|
|**--capabilities-supported-orientations**|array||supported_orientations|supportedOrientations|
|**--capabilities-supported-output-bins**|array||supported_output_bins|supportedOutputBins|
|**--capabilities-supported-pages-per-sheet**|object|integerRange|supported_pages_per_sheet|supportedPagesPerSheet|
|**--capabilities-supported-presentation-directions**|array||supported_presentation_directions|supportedPresentationDirections|
|**--capabilities-supported-print-qualities**|array||supported_print_qualities|supportedPrintQualities|
|**--capabilities-supports-fit-pdf-to-page**|boolean||supports_fit_pdf_to_page|supportsFitPdfToPage|
|**--capabilities-top-margins**|array||top_margins|topMargins|
|**--allow-all-users**|boolean||allow_all_users|allowAllUsers|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--allowed-groups**|array||allowed_groups|allowedGroups|
|**--allowed-users**|array||allowed_users|allowedUsers|
|**--printer**|object|printer|printer|printer|

### devicescloudprint print create-task-definition

create-task-definition a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task-definition|CreateTaskDefinitions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--id**|string|Read-only.|id|id|
|**--created-by**|object|appIdentity|created_by|createdBy|
|**--display-name**|string||display_name|displayName|
|**--tasks**|array||tasks|tasks|

### devicescloudprint print delete

delete a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteConnectors|
|delete|DeleteOperations|
|delete|DeletePrinters|
|delete|DeletePrinterShares|
|delete|DeleteReports|
|delete|DeleteServices|
|delete|DeleteShares|
|delete|DeleteTaskDefinitions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-connector-id**|string|key: id of printConnector|print_connector_id|printConnector-id|
|**--print-operation-id**|string|key: id of printOperation|print_operation_id|printOperation-id|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--report-root-id**|string|key: id of reportRoot|report_root_id|reportRoot-id|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--if-match**|string|ETag|if_match|If-Match|

### devicescloudprint print get-connector

get-connector a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-connector|GetConnectors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-connector-id**|string|key: id of printConnector|print_connector_id|printConnector-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print get-operation

get-operation a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-operation|GetOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-operation-id**|string|key: id of printOperation|print_operation_id|printOperation-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print get-printer

get-printer a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-printer|GetPrinters|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print get-printer-share

get-printer-share a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-printer-share|GetPrinterShares|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print get-report

get-report a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-report|GetReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--report-root-id**|string|key: id of reportRoot|report_root_id|reportRoot-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print get-service

get-service a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-service|GetServices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print get-share

get-share a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share|GetShares|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print get-task-definition

get-task-definition a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task-definition|GetTaskDefinitions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print list-connector

list-connector a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-connector|ListConnectors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print list-operation

list-operation a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-operation|ListOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print list-printer

list-printer a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-printer|ListPrinters|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print list-printer-share

list-printer-share a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-printer-share|ListPrinterShares|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print list-report

list-report a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-report|ListReports|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print list-service

list-service a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-service|ListServices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print list-share

list-share a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-share|ListShares|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print list-task-definition

list-task-definition a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task-definition|ListTaskDefinitions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print update-connector

update-connector a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-connector|UpdateConnectors|

#### Parameters
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
|**--device-health-last-connection-time**|date-time||last_connection_time|lastConnectionTime|

### devicescloudprint print update-operation

update-operation a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-operation|UpdateOperations|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-operation-id**|string|key: id of printOperation|print_operation_id|printOperation-id|
|**--id**|string|Read-only.|id|id|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--status-description**|string||description|description|
|**--status-state**|choice||state|state|

### devicescloudprint print update-printer

update-printer a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-printer|UpdatePrinters|

#### Parameters
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
|**--capabilities-bottom-margins**|array||bottom_margins|bottomMargins|
|**--capabilities-collation**|boolean||collation|collation|
|**--capabilities-color-modes**|array||color_modes|colorModes|
|**--capabilities-content-types**|array||content_types|contentTypes|
|**--capabilities-copies-per-job**|object|integerRange|copies_per_job|copiesPerJob|
|**--capabilities-dpis**|array||dpis|dpis|
|**--capabilities-duplex-modes**|array||duplex_modes|duplexModes|
|**--capabilities-feed-directions**|array||feed_directions|feedDirections|
|**--capabilities-feed-orientations**|array||feed_orientations|feedOrientations|
|**--capabilities-finishings**|array||finishings|finishings|
|**--capabilities-input-bins**|array||input_bins|inputBins|
|**--capabilities-is-color-printing-supported**|boolean||is_color_printing_supported|isColorPrintingSupported|
|**--capabilities-is-page-range-supported**|boolean||is_page_range_supported|isPageRangeSupported|
|**--capabilities-left-margins**|array||left_margins|leftMargins|
|**--capabilities-media-colors**|array||media_colors|mediaColors|
|**--capabilities-media-sizes**|array||media_sizes|mediaSizes|
|**--capabilities-media-types**|array||media_types|mediaTypes|
|**--capabilities-multipage-layouts**|array||multipage_layouts|multipageLayouts|
|**--capabilities-orientations**|array||orientations|orientations|
|**--capabilities-output-bins**|array||output_bins|outputBins|
|**--capabilities-pages-per-sheet**|array||pages_per_sheet|pagesPerSheet|
|**--capabilities-qualities**|array||qualities|qualities|
|**--capabilities-right-margins**|array||right_margins|rightMargins|
|**--capabilities-scalings**|array||scalings|scalings|
|**--capabilities-supported-color-configurations**|array||supported_color_configurations|supportedColorConfigurations|
|**--capabilities-supported-copies-per-job**|object|integerRange|supported_copies_per_job|supportedCopiesPerJob|
|**--capabilities-supported-document-mime-types**|array||supported_document_mime_types|supportedDocumentMimeTypes|
|**--capabilities-supported-duplex-configurations**|array||supported_duplex_configurations|supportedDuplexConfigurations|
|**--capabilities-supported-finishings**|array||supported_finishings|supportedFinishings|
|**--capabilities-supported-media-colors**|array||supported_media_colors|supportedMediaColors|
|**--capabilities-supported-media-sizes**|array||supported_media_sizes|supportedMediaSizes|
|**--capabilities-supported-media-types**|array||supported_media_types|supportedMediaTypes|
|**--capabilities-supported-orientations**|array||supported_orientations|supportedOrientations|
|**--capabilities-supported-output-bins**|array||supported_output_bins|supportedOutputBins|
|**--capabilities-supported-pages-per-sheet**|object|integerRange|supported_pages_per_sheet|supportedPagesPerSheet|
|**--capabilities-supported-presentation-directions**|array||supported_presentation_directions|supportedPresentationDirections|
|**--capabilities-supported-print-qualities**|array||supported_print_qualities|supportedPrintQualities|
|**--capabilities-supports-fit-pdf-to-page**|boolean||supports_fit_pdf_to_page|supportsFitPdfToPage|
|**--capabilities-top-margins**|array||top_margins|topMargins|
|**--accepting-jobs**|boolean||accepting_jobs|acceptingJobs|
|**--is-shared**|boolean||is_shared|isShared|
|**--registered-date-time**|date-time||registered_date_time|registeredDateTime|
|**--allowed-groups**|array||allowed_groups|allowedGroups|
|**--allowed-users**|array||allowed_users|allowedUsers|
|**--connectors**|array||connectors|connectors|
|**--share**|object|printerShare|share|share|
|**--shares**|array||shares|shares|
|**--task-triggers**|array||task_triggers|taskTriggers|

### devicescloudprint print update-printer-share

update-printer-share a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-printer-share|UpdatePrinterShares|

#### Parameters
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
|**--capabilities-bottom-margins**|array||bottom_margins|bottomMargins|
|**--capabilities-collation**|boolean||collation|collation|
|**--capabilities-color-modes**|array||color_modes|colorModes|
|**--capabilities-content-types**|array||content_types|contentTypes|
|**--capabilities-copies-per-job**|object|integerRange|copies_per_job|copiesPerJob|
|**--capabilities-dpis**|array||dpis|dpis|
|**--capabilities-duplex-modes**|array||duplex_modes|duplexModes|
|**--capabilities-feed-directions**|array||feed_directions|feedDirections|
|**--capabilities-feed-orientations**|array||feed_orientations|feedOrientations|
|**--capabilities-finishings**|array||finishings|finishings|
|**--capabilities-input-bins**|array||input_bins|inputBins|
|**--capabilities-is-color-printing-supported**|boolean||is_color_printing_supported|isColorPrintingSupported|
|**--capabilities-is-page-range-supported**|boolean||is_page_range_supported|isPageRangeSupported|
|**--capabilities-left-margins**|array||left_margins|leftMargins|
|**--capabilities-media-colors**|array||media_colors|mediaColors|
|**--capabilities-media-sizes**|array||media_sizes|mediaSizes|
|**--capabilities-media-types**|array||media_types|mediaTypes|
|**--capabilities-multipage-layouts**|array||multipage_layouts|multipageLayouts|
|**--capabilities-orientations**|array||orientations|orientations|
|**--capabilities-output-bins**|array||output_bins|outputBins|
|**--capabilities-pages-per-sheet**|array||pages_per_sheet|pagesPerSheet|
|**--capabilities-qualities**|array||qualities|qualities|
|**--capabilities-right-margins**|array||right_margins|rightMargins|
|**--capabilities-scalings**|array||scalings|scalings|
|**--capabilities-supported-color-configurations**|array||supported_color_configurations|supportedColorConfigurations|
|**--capabilities-supported-copies-per-job**|object|integerRange|supported_copies_per_job|supportedCopiesPerJob|
|**--capabilities-supported-document-mime-types**|array||supported_document_mime_types|supportedDocumentMimeTypes|
|**--capabilities-supported-duplex-configurations**|array||supported_duplex_configurations|supportedDuplexConfigurations|
|**--capabilities-supported-finishings**|array||supported_finishings|supportedFinishings|
|**--capabilities-supported-media-colors**|array||supported_media_colors|supportedMediaColors|
|**--capabilities-supported-media-sizes**|array||supported_media_sizes|supportedMediaSizes|
|**--capabilities-supported-media-types**|array||supported_media_types|supportedMediaTypes|
|**--capabilities-supported-orientations**|array||supported_orientations|supportedOrientations|
|**--capabilities-supported-output-bins**|array||supported_output_bins|supportedOutputBins|
|**--capabilities-supported-pages-per-sheet**|object|integerRange|supported_pages_per_sheet|supportedPagesPerSheet|
|**--capabilities-supported-presentation-directions**|array||supported_presentation_directions|supportedPresentationDirections|
|**--capabilities-supported-print-qualities**|array||supported_print_qualities|supportedPrintQualities|
|**--capabilities-supports-fit-pdf-to-page**|boolean||supports_fit_pdf_to_page|supportsFitPdfToPage|
|**--capabilities-top-margins**|array||top_margins|topMargins|
|**--allow-all-users**|boolean||allow_all_users|allowAllUsers|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--allowed-groups**|array||allowed_groups|allowedGroups|
|**--allowed-users**|array||allowed_users|allowedUsers|
|**--printer**|object|printer|printer|printer|

### devicescloudprint print update-report

update-report a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-report|UpdateReports|

#### Parameters
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

### devicescloudprint print update-service

update-service a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-service|UpdateServices|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--id**|string|Read-only.|id|id|
|**--endpoints**|array||endpoints|endpoints|

### devicescloudprint print update-share

update-share a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-share|UpdateShares|

#### Parameters
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
|**--capabilities-bottom-margins**|array||bottom_margins|bottomMargins|
|**--capabilities-collation**|boolean||collation|collation|
|**--capabilities-color-modes**|array||color_modes|colorModes|
|**--capabilities-content-types**|array||content_types|contentTypes|
|**--capabilities-copies-per-job**|object|integerRange|copies_per_job|copiesPerJob|
|**--capabilities-dpis**|array||dpis|dpis|
|**--capabilities-duplex-modes**|array||duplex_modes|duplexModes|
|**--capabilities-feed-directions**|array||feed_directions|feedDirections|
|**--capabilities-feed-orientations**|array||feed_orientations|feedOrientations|
|**--capabilities-finishings**|array||finishings|finishings|
|**--capabilities-input-bins**|array||input_bins|inputBins|
|**--capabilities-is-color-printing-supported**|boolean||is_color_printing_supported|isColorPrintingSupported|
|**--capabilities-is-page-range-supported**|boolean||is_page_range_supported|isPageRangeSupported|
|**--capabilities-left-margins**|array||left_margins|leftMargins|
|**--capabilities-media-colors**|array||media_colors|mediaColors|
|**--capabilities-media-sizes**|array||media_sizes|mediaSizes|
|**--capabilities-media-types**|array||media_types|mediaTypes|
|**--capabilities-multipage-layouts**|array||multipage_layouts|multipageLayouts|
|**--capabilities-orientations**|array||orientations|orientations|
|**--capabilities-output-bins**|array||output_bins|outputBins|
|**--capabilities-pages-per-sheet**|array||pages_per_sheet|pagesPerSheet|
|**--capabilities-qualities**|array||qualities|qualities|
|**--capabilities-right-margins**|array||right_margins|rightMargins|
|**--capabilities-scalings**|array||scalings|scalings|
|**--capabilities-supported-color-configurations**|array||supported_color_configurations|supportedColorConfigurations|
|**--capabilities-supported-copies-per-job**|object|integerRange|supported_copies_per_job|supportedCopiesPerJob|
|**--capabilities-supported-document-mime-types**|array||supported_document_mime_types|supportedDocumentMimeTypes|
|**--capabilities-supported-duplex-configurations**|array||supported_duplex_configurations|supportedDuplexConfigurations|
|**--capabilities-supported-finishings**|array||supported_finishings|supportedFinishings|
|**--capabilities-supported-media-colors**|array||supported_media_colors|supportedMediaColors|
|**--capabilities-supported-media-sizes**|array||supported_media_sizes|supportedMediaSizes|
|**--capabilities-supported-media-types**|array||supported_media_types|supportedMediaTypes|
|**--capabilities-supported-orientations**|array||supported_orientations|supportedOrientations|
|**--capabilities-supported-output-bins**|array||supported_output_bins|supportedOutputBins|
|**--capabilities-supported-pages-per-sheet**|object|integerRange|supported_pages_per_sheet|supportedPagesPerSheet|
|**--capabilities-supported-presentation-directions**|array||supported_presentation_directions|supportedPresentationDirections|
|**--capabilities-supported-print-qualities**|array||supported_print_qualities|supportedPrintQualities|
|**--capabilities-supports-fit-pdf-to-page**|boolean||supports_fit_pdf_to_page|supportsFitPdfToPage|
|**--capabilities-top-margins**|array||top_margins|topMargins|
|**--allow-all-users**|boolean||allow_all_users|allowAllUsers|
|**--created-date-time**|date-time||created_date_time|createdDateTime|
|**--allowed-groups**|array||allowed_groups|allowedGroups|
|**--allowed-users**|array||allowed_users|allowedUsers|
|**--printer**|object|printer|printer|printer|

### devicescloudprint print update-task-definition

update-task-definition a devicescloudprint print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print|print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task-definition|UpdateTaskDefinitions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--id**|string|Read-only.|id|id|
|**--created-by**|object|appIdentity|created_by|createdBy|
|**--display-name**|string||display_name|displayName|
|**--tasks**|array||tasks|tasks|

### devicescloudprint print-print get-print

get-print a devicescloudprint print-print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-print|print.print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-print|GetPrint|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-print update-print

update-print a devicescloudprint print-print.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-print|print.print|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-print|UpdatePrint|

#### Parameters
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
|**--settings-document-conversion-enabled**|boolean||document_conversion_enabled|documentConversionEnabled|

### devicescloudprint print-printer create

create a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create|create|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--display-name**|string||display_name|displayName|
|**--manufacturer**|string||manufacturer|manufacturer|
|**--model**|string||model|model|
|**--physical-device-id**|string||physical_device_id|physicalDeviceId|
|**--has-physical-device**|boolean||has_physical_device|hasPhysicalDevice|
|**--certificate-signing-request**|object|printCertificateSigningRequest|certificate_signing_request|certificateSigningRequest|
|**--connector-id**|string||connector_id|connectorId|

### devicescloudprint print-printer create-allowed-group

create-allowed-group a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-allowed-group|CreateAllowedGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### devicescloudprint print-printer create-allowed-user

create-allowed-user a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-allowed-user|CreateAllowedUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--ip-address**|string||ip_address|ipAddress|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### devicescloudprint print-printer create-ref-connector

create-ref-connector a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-connector|CreateRefConnectors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### devicescloudprint print-printer create-ref-share

create-ref-share a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-ref-share|CreateRefShares|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--body**|dictionary|New navigation property ref value|body|body|

### devicescloudprint print-printer create-task-trigger

create-task-trigger a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task-trigger|CreateTaskTriggers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--id**|string|Read-only.|id|id|
|**--event**|choice||event|event|
|**--definition**|object|printTaskDefinition|definition|definition|

### devicescloudprint print-printer delete

delete a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAllowedGroups|
|delete|DeleteAllowedUsers|
|delete|DeleteTaskTriggers|
|delete|DeleteRefShare|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--print-task-trigger-id**|string|key: id of printTaskTrigger|print_task_trigger_id|printTaskTrigger-id|
|**--if-match**|string|ETag|if_match|If-Match|

### devicescloudprint print-printer get-allowed-group

get-allowed-group a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-allowed-group|GetAllowedGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-printer get-allowed-user

get-allowed-user a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-allowed-user|GetAllowedUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-printer get-capability

get-capability a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-capability|getCapabilities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|

### devicescloudprint print-printer get-ref-share

get-ref-share a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-share|GetRefShare|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|

### devicescloudprint print-printer get-share

get-share a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-share|GetShare|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-printer get-task-trigger

get-task-trigger a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task-trigger|GetTaskTriggers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-task-trigger-id**|string|key: id of printTaskTrigger|print_task_trigger_id|printTaskTrigger-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-printer list-allowed-group

list-allowed-group a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-allowed-group|ListAllowedGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-printer list-allowed-user

list-allowed-user a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-allowed-user|ListAllowedUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-printer list-connector

list-connector a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-connector|ListConnectors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-printer list-ref-connector

list-ref-connector a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-connector|ListRefConnectors|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### devicescloudprint print-printer list-ref-share

list-ref-share a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-ref-share|ListRefShares|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|

### devicescloudprint print-printer list-share

list-share a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-share|ListShares|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-printer list-task-trigger

list-task-trigger a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task-trigger|ListTaskTriggers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-printer reset-default

reset-default a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reset-default|resetDefaults|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|

### devicescloudprint print-printer restore-factory-default

restore-factory-default a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore-factory-default|restoreFactoryDefaults|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|

### devicescloudprint print-printer set-ref-share

set-ref-share a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-share|SetRefShare|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### devicescloudprint print-printer update-allowed-group

update-allowed-group a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-allowed-group|UpdateAllowedGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### devicescloudprint print-printer update-allowed-user

update-allowed-user a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-allowed-user|UpdateAllowedUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--ip-address**|string||ip_address|ipAddress|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### devicescloudprint print-printer update-task-trigger

update-task-trigger a devicescloudprint print-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer|print.printers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task-trigger|UpdateTaskTriggers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-task-trigger-id**|string|key: id of printTaskTrigger|print_task_trigger_id|printTaskTrigger-id|
|**--id**|string|Read-only.|id|id|
|**--event**|choice||event|event|
|**--definition**|object|printTaskDefinition|definition|definition|

### devicescloudprint print-printer-share create-allowed-group

create-allowed-group a devicescloudprint print-printer-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-share|print.printerShares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-allowed-group|CreateAllowedGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### devicescloudprint print-printer-share create-allowed-user

create-allowed-user a devicescloudprint print-printer-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-share|print.printerShares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-allowed-user|CreateAllowedUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--ip-address**|string||ip_address|ipAddress|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### devicescloudprint print-printer-share delete

delete a devicescloudprint print-printer-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-share|print.printerShares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAllowedGroups|
|delete|DeleteAllowedUsers|
|delete|DeleteRefPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--if-match**|string|ETag|if_match|If-Match|

### devicescloudprint print-printer-share get-allowed-group

get-allowed-group a devicescloudprint print-printer-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-share|print.printerShares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-allowed-group|GetAllowedGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-printer-share get-allowed-user

get-allowed-user a devicescloudprint print-printer-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-share|print.printerShares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-allowed-user|GetAllowedUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-printer-share get-printer

get-printer a devicescloudprint print-printer-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-share|print.printerShares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-printer|GetPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-printer-share get-ref-printer

get-ref-printer a devicescloudprint print-printer-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-share|print.printerShares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-printer|GetRefPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

### devicescloudprint print-printer-share list-allowed-group

list-allowed-group a devicescloudprint print-printer-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-share|print.printerShares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-allowed-group|ListAllowedGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-printer-share list-allowed-user

list-allowed-user a devicescloudprint print-printer-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-share|print.printerShares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-allowed-user|ListAllowedUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-printer-share set-ref-printer

set-ref-printer a devicescloudprint print-printer-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-share|print.printerShares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-printer|SetRefPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### devicescloudprint print-printer-share update-allowed-group

update-allowed-group a devicescloudprint print-printer-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-share|print.printerShares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-allowed-group|UpdateAllowedGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### devicescloudprint print-printer-share update-allowed-user

update-allowed-user a devicescloudprint print-printer-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-share|print.printerShares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-allowed-user|UpdateAllowedUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--ip-address**|string||ip_address|ipAddress|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### devicescloudprint print-printer-share-printer get-capability

get-capability a devicescloudprint print-printer-share-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-share-printer|print.printerShares.printer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-capability|getCapabilities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

### devicescloudprint print-printer-share-printer reset-default

reset-default a devicescloudprint print-printer-share-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-share-printer|print.printerShares.printer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reset-default|resetDefaults|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

### devicescloudprint print-printer-share-printer restore-factory-default

restore-factory-default a devicescloudprint print-printer-share-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-share-printer|print.printerShares.printer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore-factory-default|restoreFactoryDefaults|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

### devicescloudprint print-printer-task-trigger delete

delete a devicescloudprint print-printer-task-trigger.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-task-trigger|print.printers.taskTriggers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRefDefinition|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-task-trigger-id**|string|key: id of printTaskTrigger|print_task_trigger_id|printTaskTrigger-id|
|**--if-match**|string|ETag|if_match|If-Match|

### devicescloudprint print-printer-task-trigger get-definition

get-definition a devicescloudprint print-printer-task-trigger.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-task-trigger|print.printers.taskTriggers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-definition|GetDefinition|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-task-trigger-id**|string|key: id of printTaskTrigger|print_task_trigger_id|printTaskTrigger-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-printer-task-trigger get-ref-definition

get-ref-definition a devicescloudprint print-printer-task-trigger.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-task-trigger|print.printers.taskTriggers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-definition|GetRefDefinition|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-task-trigger-id**|string|key: id of printTaskTrigger|print_task_trigger_id|printTaskTrigger-id|

### devicescloudprint print-printer-task-trigger set-ref-definition

set-ref-definition a devicescloudprint print-printer-task-trigger.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-printer-task-trigger|print.printers.taskTriggers|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-definition|SetRefDefinition|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string|key: id of printer|printer_id|printer-id|
|**--print-task-trigger-id**|string|key: id of printTaskTrigger|print_task_trigger_id|printTaskTrigger-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### devicescloudprint print-report get-group-archived-print-job

get-group-archived-print-job a devicescloudprint print-report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-report|print.reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-group-archived-print-job|getGroupArchivedPrintJobs|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string||group_id|groupId|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|

### devicescloudprint print-report get-group-print-usage-summary

get-group-print-usage-summary a devicescloudprint print-report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-report|print.reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-group-print-usage-summary|getGroupPrintUsageSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--group-id**|string||group_id|groupId|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|

### devicescloudprint print-report get-overall-print-usage-summary

get-overall-print-usage-summary a devicescloudprint print-report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-report|print.reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-overall-print-usage-summary|getOverallPrintUsageSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|
|**--top-lists-size**|integer||top_lists_size|topListsSize|

### devicescloudprint print-report get-print-usage-summary-by-group

get-print-usage-summary-by-group a devicescloudprint print-report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-report|print.reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-print-usage-summary-by-group|getPrintUsageSummariesByGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|

### devicescloudprint print-report get-print-usage-summary-by-printer

get-print-usage-summary-by-printer a devicescloudprint print-report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-report|print.reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-print-usage-summary-by-printer|getPrintUsageSummariesByPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|

### devicescloudprint print-report get-print-usage-summary-by-time-span

get-print-usage-summary-by-time-span a devicescloudprint print-report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-report|print.reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-print-usage-summary-by-time-span|getPrintUsageSummariesByTimeSpan|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|
|**--time-span-in-minutes**|integer||time_span_in_minutes|timeSpanInMinutes|

### devicescloudprint print-report get-print-usage-summary-by-user

get-print-usage-summary-by-user a devicescloudprint print-report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-report|print.reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-print-usage-summary-by-user|getPrintUsageSummariesByUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|

### devicescloudprint print-report get-printer-archived-print-job

get-printer-archived-print-job a devicescloudprint print-report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-report|print.reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-printer-archived-print-job|getPrinterArchivedPrintJobs|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string||printer_id|printerId|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|

### devicescloudprint print-report get-printer-usage-summary

get-printer-usage-summary a devicescloudprint print-report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-report|print.reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-printer-usage-summary|getPrinterUsageSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-id**|string||printer_id|printerId|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|

### devicescloudprint print-report get-user-archived-print-job

get-user-archived-print-job a devicescloudprint print-report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-report|print.reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-archived-print-job|getUserArchivedPrintJobs|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string||user_id|userId|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|

### devicescloudprint print-report get-user-print-usage-summary

get-user-print-usage-summary a devicescloudprint print-report.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-report|print.reports|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-user-print-usage-summary|getUserPrintUsageSummary|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string||user_id|userId|
|**--period-start**|date-time||period_start|periodStart|
|**--period-end**|date-time||period_end|periodEnd|

### devicescloudprint print-service create-endpoint

create-endpoint a devicescloudprint print-service.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-service|print.services|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-endpoint|CreateEndpoints|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--uri**|string||uri|uri|

### devicescloudprint print-service delete

delete a devicescloudprint print-service.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-service|print.services|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteEndpoints|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--print-service-endpoint-id**|string|key: id of printServiceEndpoint|print_service_endpoint_id|printServiceEndpoint-id|
|**--if-match**|string|ETag|if_match|If-Match|

### devicescloudprint print-service get-endpoint

get-endpoint a devicescloudprint print-service.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-service|print.services|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-endpoint|GetEndpoints|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--print-service-endpoint-id**|string|key: id of printServiceEndpoint|print_service_endpoint_id|printServiceEndpoint-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-service list-endpoint

list-endpoint a devicescloudprint print-service.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-service|print.services|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-endpoint|ListEndpoints|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-service update-endpoint

update-endpoint a devicescloudprint print-service.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-service|print.services|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-endpoint|UpdateEndpoints|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-service-id**|string|key: id of printService|print_service_id|printService-id|
|**--print-service-endpoint-id**|string|key: id of printServiceEndpoint|print_service_endpoint_id|printServiceEndpoint-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--uri**|string||uri|uri|

### devicescloudprint print-share create-allowed-group

create-allowed-group a devicescloudprint print-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-share|print.shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-allowed-group|CreateAllowedGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### devicescloudprint print-share create-allowed-user

create-allowed-user a devicescloudprint print-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-share|print.shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-allowed-user|CreateAllowedUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--ip-address**|string||ip_address|ipAddress|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### devicescloudprint print-share delete

delete a devicescloudprint print-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-share|print.shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteAllowedGroups|
|delete|DeleteAllowedUsers|
|delete|DeleteRefPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--if-match**|string|ETag|if_match|If-Match|

### devicescloudprint print-share get-allowed-group

get-allowed-group a devicescloudprint print-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-share|print.shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-allowed-group|GetAllowedGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-share get-allowed-user

get-allowed-user a devicescloudprint print-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-share|print.shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-allowed-user|GetAllowedUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-share get-printer

get-printer a devicescloudprint print-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-share|print.shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-printer|GetPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-share get-ref-printer

get-ref-printer a devicescloudprint print-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-share|print.shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-printer|GetRefPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

### devicescloudprint print-share list-allowed-group

list-allowed-group a devicescloudprint print-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-share|print.shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-allowed-group|ListAllowedGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-share list-allowed-user

list-allowed-user a devicescloudprint print-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-share|print.shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-allowed-user|ListAllowedUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-share set-ref-printer

set-ref-printer a devicescloudprint print-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-share|print.shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-printer|SetRefPrinter|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### devicescloudprint print-share update-allowed-group

update-allowed-group a devicescloudprint print-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-share|print.shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-allowed-group|UpdateAllowedGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-identity-id**|string|key: id of printIdentity|print_identity_id|printIdentity-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|

### devicescloudprint print-share update-allowed-user

update-allowed-user a devicescloudprint print-share.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-share|print.shares|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-allowed-user|UpdateAllowedUsers|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|
|**--print-user-identity-id**|string|key: id of printUserIdentity|print_user_identity_id|printUserIdentity-id|
|**--id**|string|Read-only.|id|id|
|**--display-name**|string||display_name|displayName|
|**--ip-address**|string||ip_address|ipAddress|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### devicescloudprint print-share-printer get-capability

get-capability a devicescloudprint print-share-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-share-printer|print.shares.printer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-capability|getCapabilities|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

### devicescloudprint print-share-printer reset-default

reset-default a devicescloudprint print-share-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-share-printer|print.shares.printer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reset-default|resetDefaults|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

### devicescloudprint print-share-printer restore-factory-default

restore-factory-default a devicescloudprint print-share-printer.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-share-printer|print.shares.printer|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore-factory-default|restoreFactoryDefaults|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--printer-share-id**|string|key: id of printerShare|printer_share_id|printerShare-id|

### devicescloudprint print-task-definition create-task

create-task a devicescloudprint print-task-definition.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-task-definition|print.taskDefinitions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-task|CreateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--id**|string|Read-only.|id|id|
|**--parent-url**|string||parent_url|parentUrl|
|**--status**|object|printTaskStatus|status|status|
|**--definition**|object|printTaskDefinition|definition|definition|
|**--trigger-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--trigger-event**|choice||event|event|
|**--trigger-definition**|object|printTaskDefinition|microsoft_graph_print_task_definition|definition|

### devicescloudprint print-task-definition delete

delete a devicescloudprint print-task-definition.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-task-definition|print.taskDefinitions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### devicescloudprint print-task-definition get-task

get-task a devicescloudprint print-task-definition.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-task-definition|print.taskDefinitions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-task|GetTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-task-definition list-task

list-task a devicescloudprint print-task-definition.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-task-definition|print.taskDefinitions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|list-task|ListTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--orderby**|array|Order items by property values|orderby|$orderby|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-task-definition update-task

update-task a devicescloudprint print-task-definition.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-task-definition|print.taskDefinitions|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-task|UpdateTasks|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--id**|string|Read-only.|id|id|
|**--parent-url**|string||parent_url|parentUrl|
|**--status**|object|printTaskStatus|status|status|
|**--definition**|object|printTaskDefinition|definition|definition|
|**--trigger-id**|string|Read-only.|microsoft_graph_entity_id|id|
|**--trigger-event**|choice||event|event|
|**--trigger-definition**|object|printTaskDefinition|microsoft_graph_print_task_definition|definition|

### devicescloudprint print-task-definition-task delete

delete a devicescloudprint print-task-definition-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-task-definition-task|print.taskDefinitions.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete|DeleteRefDefinition|
|delete|DeleteRefTrigger|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--if-match**|string|ETag|if_match|If-Match|

### devicescloudprint print-task-definition-task get-definition

get-definition a devicescloudprint print-task-definition-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-task-definition-task|print.taskDefinitions.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-definition|GetDefinition|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-task-definition-task get-ref-definition

get-ref-definition a devicescloudprint print-task-definition-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-task-definition-task|print.taskDefinitions.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-definition|GetRefDefinition|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|

### devicescloudprint print-task-definition-task get-ref-trigger

get-ref-trigger a devicescloudprint print-task-definition-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-task-definition-task|print.taskDefinitions.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-ref-trigger|GetRefTrigger|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|

### devicescloudprint print-task-definition-task get-trigger

get-trigger a devicescloudprint print-task-definition-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-task-definition-task|print.taskDefinitions.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-trigger|GetTrigger|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--select**|array|Select properties to be returned|select|$select|
|**--expand**|array|Expand related entities|expand|$expand|

### devicescloudprint print-task-definition-task set-ref-definition

set-ref-definition a devicescloudprint print-task-definition-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-task-definition-task|print.taskDefinitions.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-definition|SetRefDefinition|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--body**|dictionary|New navigation property ref values|body|body|

### devicescloudprint print-task-definition-task set-ref-trigger

set-ref-trigger a devicescloudprint print-task-definition-task.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|devicescloudprint print-task-definition-task|print.taskDefinitions.tasks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|set-ref-trigger|SetRefTrigger|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--print-task-definition-id**|string|key: id of printTaskDefinition|print_task_definition_id|printTaskDefinition-id|
|**--print-task-id**|string|key: id of printTask|print_task_id|printTask-id|
|**--body**|dictionary|New navigation property ref values|body|body|
