## CLI

These settings apply only when `--az` is specified on the command line.

``` yaml $(az)
az:
  extensions: msgraphusersuser
  package-name: azure-mgmt-msgraphusersuser
  namespace: azure.mgmt.msgraphusersuser
  client-subscription-bound: false
  client-base-url-bound: false
az-output-folder: $(azure-cli-extension-folder)/src/msgraphusersuser
python-sdk-output-folder: "$(az-output-folder)/azext_msgraphusersuser/vendored_sdks/msgraphusersuser"
```