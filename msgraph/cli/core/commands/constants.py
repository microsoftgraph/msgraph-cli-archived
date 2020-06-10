CLI_COMMON_KWARGS = ['min_api', 'max_api', 'resource_type', 'operation_group',
                     'custom_command_type', 'command_type', 'is_preview', 'preview_info',
                     'is_experimental', 'experimental_info', 'local_context_attribute']


CLI_COMMAND_KWARGS = ['transform', 'table_transformer', 'confirmation', 'exception_handler',
                      'client_factory', 'operations_tmpl', 'no_wait_param', 'supports_no_wait', 'validator',
                      'client_arg_name', 'doc_string_source', 'deprecate_info',
                      'supports_local_cache', 'model_path'] + CLI_COMMON_KWARGS