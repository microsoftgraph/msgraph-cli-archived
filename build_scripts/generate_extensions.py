import os
import sys
from os import path
import subprocess


def generate_extension_from_open_api_description(version='v1_0'):
    open_api_descriptions = get_open_api_descriptions(version)

    for item in open_api_descriptions:
        file_name, file_path = item
        file_name = remove_file_extension_and_group(file_name)

        # Config files are used to modify generated extensions
        generate_az_config_for(file_name, version)
        generate_cli_config_for(file_name)
        generate_python_config_for(file_name)

        subprocess.run([
            'autorest',
            '--version=3.0.6370',
            '--clear-output-folder',
            '--az',
            f'''--input-file={file_path}''',
            f'''--azure-cli-extension-folder=../msgraph-cli-extensions/{version}''',
            r'''--use=https://github.com/Azure/autorest.az/releases/download/1.7.3-b.20210624.2/autorest-az-1.7.3.tgz''',
        ],
                       shell=True)


def get_open_api_descriptions(version: str):
    result = []

    open_api_dir = path.join(os.getcwd(), os.pardir, 'open-api-docs', version)
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
    # enable flattening
    cli-flatten-set-enabled: true
    # flatten payloads
    cli-flatten-payload: true
    # max properties allowed for flattening. Don't flatten if properties exceed set count.
    # Using 256 so that most of the payloads get flattened, payloads with more than 256 properties
    # won't be flattened
    cli-flatten-payload-max-prop: 256
    # max depth of flatten
    cli-flatten-payload-max-level: 1
    cli-flatten-payload-max-complexity: 0.5
    cli-flatten-payload-max-array-object-prop-count: 8
```
    """
    write_to('readme.cli.md', config)


def generate_az_config_for(file_name, version):
    parsed_file_name = file_name

    # For filenames that are plural we get their singular form by removing the s.
    # Command group use the singular form of the filename, ie if filename is applications
    # the command group will be mg applications application
    if file_name[-1] == 's':
        parsed_file_name = file_name[:-1]

    config = f"""
# CLI

These settings apply only when `--az` is specified on the command line.

``` yaml $(az)
az:
  extensions: {file_name}_{version}
  package-name: azure-mgmt-{file_name}
  namespace: azure.mgmt.{file_name}
  client-subscription-bound: false
  client-base-url-bound: false

az-output-folder: $(azure-cli-extension-folder)/{file_name}_{version}
python-sdk-output-folder: "$(az-output-folder)/azext_{file_name}_{version}/vendored_sdks/{file_name}"

directive:
    - where:
          group: {file_name}_beta
      set:
          group: {file_name}-beta
    - where:
          group: {file_name}_{version}
      set:
          group: {file_name}
    - where:
          group: {parsed_file_name}-{parsed_file_name}
      set:
          group: {parsed_file_name}
    - where:
          command: {file_name} {parsed_file_name} create-{parsed_file_name}
      set:
          command: {file_name} {parsed_file_name} create
    - where:
          command: {file_name} {parsed_file_name} get-{parsed_file_name}
      set:
          command: {file_name} {parsed_file_name} get
    - where:
          command: {file_name} {parsed_file_name} list-{parsed_file_name}
      set:
          command: {file_name} {parsed_file_name} list
    - where:
          command: {file_name} {parsed_file_name} update-{parsed_file_name}
      set:
          command: {file_name} {parsed_file_name} update

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
  payload-flattening-threshold: 2
  namespace: azure.mgmt.{file_name}
  package-name: azure-mgmt-{file_name}
  package-version: 0.1.0
  clear-output-folder: true
```
``` yaml $(python) && $(python-mode) == 'update'
python:
  no-namespace-folders: true
  output-folder: $(python-sdks-folder)/{file_name}/azure-mgmt-{file_name}/azure/mgmt/{file_name}
```
``` yaml $(python) && $(python-mode) == 'create'
python:
  basic-setup-py: true
  output-folder: $(python-sdks-folder)/msgraph/extensions/{file_name}/azure-mgmt-{file_name}
```
  """
    write_to('readme.python.md', config)


def write_to(file, config):
    with open(file, 'w') as f:
        f.write(config)


# generate_extension_from_open_api_description(version='v1_0')
generate_extension_from_open_api_description(version='beta')