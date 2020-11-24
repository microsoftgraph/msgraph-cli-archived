import os
from os import path
import subprocess


def generate_extension_from_open_api_description():
    open_api_descriptions = get_open_api_descriptions()

    for item in open_api_descriptions:
        file_name, file_path = item
        file_name = remove_file_extension_and_group(file_name)

        # Config files are used to modify generated extensions
        generate_az_config_for(file_name)
        generate_cli_config_for(file_name)
        generate_python_config_for(file_name)

        subprocess.run([
            'autorest',
            '--az',
            '--v3',
            f'''--input-file:{file_path}''',
            r'''--azure-cli-extension-folder=../msgraph-cli-extensions''',
            r'''--use=@autorest/python@5.1.0-preview.4''',
            r'''--use=@autorest/modelerfour@4.15.421''',
            r'''--use=@autorest/az@1.5.1''',
        ],
                       shell=True)


def get_open_api_descriptions():
    result = []

    open_api_dir = path.join(os.getcwd(), os.pardir, 'open-api-docs', 'v1.0')
    open_api_files = os.listdir(open_api_dir)

    for file in open_api_files:
        file_and_path = (file, path.join(open_api_dir, file))
        result.append(file_and_path)

    return result


def remove_file_extension_and_group(file_name):
    return file_name.replace('.', '')[:-3].lower()


def generate_cli_config_for(file_name):
    config = f"""
# CLI

These settings don't need to apply `--cli` on the command line.

``` yaml $(cli)
cli:
  cli-name: {file_name}
  flatten:
    cli-flatten-set-enabled: true
    cli-flatten-payload: true
    cli-flatten-payload-max-prop: 100
```
    """
    write_to('readme.cli.md', config)


def generate_az_config_for(file_name):
    config = f"""
# CLI

These settings apply only when `--az` is specified on the command line.

``` yaml $(az)
az:
  extensions: {file_name}
  package-name: azure-mgmt-{file_name}
  namespace: azure.mgmt.{file_name}
  client-subscription-bound: false
  client-base-url-bound: false

az-output-folder: $(azure-cli-extension-folder)/src/{file_name}
python-sdk-output-folder: "$(az-output-folder)/azext_{file_name}/vendored_sdks/{file_name}"
cli-core-lib: msgraph.cli.core

directive:
    - where:
          group: ^{file_name}(.*)
      set:
          group: {file_name}

modelerfour:
    lenient-model-deduplication: true
    group-parameters: true
    flatten-models: true
    flatten-payloads: true
```
  """
    write_to('readme.az.md', config)


def generate_python_config_for(file_name):
    config = f"""
# Python

These settings apply only when `--python` is specified on the command line.
Please also specify `--python-sdks-folder=<path to the root directory of your azure-sdk-for-python clone>`.
Use `--python-mode=update` if you already have a setup.py and just want to update the code itself.

``` yaml $(python)
python:
  azure-arm: true
  license-header: MICROSOFT_MIT_NO_VERSION
  payload-flattening-threshold: 1
  namespace: azure.mgmt.{file_name}
  package-name: azure-mgmt-{file_name}
  package-version: 0.1.0
  clear-output-folder: true
```
``` yaml $(python) && $(python-mode) == 'update'
python:
  no-namespace-folders: true
  payload-flattening-threshold: 1
  output-folder: $(python-sdks-folder)/{file_name}/azure-mgmt-{file_name}/azure/mgmt/{file_name}
```
``` yaml $(python) && $(python-mode) == 'create'
python:
  basic-setup-py: true
  payload-flattening-threshold: 1
  output-folder: $(python-sdks-folder)/msgraph/extensions/{file_name}/azure-mgmt-{file_name}
```
  """
    write_to('readme.python.md', config)


def write_to(file, config):
    with open(file, 'w') as f:
        f.write(config)


generate_extension_from_open_api_description()
