# Validate the login experience - TODO: validate from MSI

# 1. Login without scopes before installing wheels

.\mg login

# Result:

<#
WARNING: No module named 'azext_identitydirmgt_v1_0'
usage: mg login [-h] [--verbose] [--debug] [--only-show-errors] [--output {json,jsonc,yaml,yamlc,table,tsv,none}] [--query JMESPATH] --scopes SCOPES [--client-id CLIENT_ID]
                [--tenant-id TENANT_ID]
mg login: error: the following arguments are required: --scopes
#>

# 2. Login with scopes before installing wheels

.\mg login --scopes user.read

# Results:

<#
WARNING: No module named 'azext_identitydirmgt_v1_0'
Logged in successfully
#>

# 3. Incremental login with new scope after installing wheels against tenant where user consent is disabled

.\mg login --scopes mail.read

# Results:

<#
ERROR: Authentication failed: ['access_denied']
#>

# TODO: Consider handling with a user friendly message to indicate that either: 1) the scope is not applicable to delegate auth, 
# 2) they may need to acquire admin consent to use the scope. This brings up another set of questions around how is the app
# registered and what is the auth story.