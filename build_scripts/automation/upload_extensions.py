# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=broad-except

import os
import re
import json
import tempfile
from subprocess import check_output
from util import get_ext_metadata, get_sha256sum

STORAGE_CONNECTION_STRING = os.getenv('AZURE_EXTENSION_TARGET_CONNECTION_STRING')
STORAGE_ACCOUNT_KEY = os.getenv('AZURE_EXTENSION_TARGET_STORAGE_ACCOUNT_KEY')
STORAGE_ACCOUNT = os.getenv('AZURE_EXTENSION_TARGET_STORAGE_ACCOUNT')
STORAGE_CONTAINER = os.getenv('AZURE_EXTENSION_TARGET_STORAGE_CONTAINER')
BLOB_PREFIX = os.getenv('AZURE_EXTENSION_BLOB_PREFIX')
EXTENSIONS_DIR = os.getenv('AZURE_EXTENSIONS_DIR') or 'dist/'

def _upload_wheel(ext_info, updated_indexes, ext_file, ext_name, client):
    blob_name = f'{BLOB_PREFIX}/{ext_file}' if BLOB_PREFIX else ext_file
    extension_file = os.path.abspath(os.path.join(EXTENSIONS_DIR, ext_file))
    client.create_blob_from_path(container_name=STORAGE_CONTAINER, blob_name=blob_name,
                                 file_path=os.path.abspath(os.path.join(EXTENSIONS_DIR, ext_file)))
    url = client.make_blob_url(container_name=STORAGE_CONTAINER, blob_name=blob_name)
    extensions_dir = tempfile.mkdtemp()
    ext_dir = tempfile.mkdtemp(dir=extensions_dir)

    updated_index = ext_info
    updated_index['downloadUrl'] = url
    updated_index['filename'] = ext_file
    updated_index['metadata'] = get_ext_metadata(ext_dir, extension_file, ext_name)
    updated_index['sha256Digest'] = get_sha256sum(extension_file)
    updated_indexes.append(updated_index)
    return updated_index


def _update_target_extension_index(updated_indexes, target_index_path):
    NAME_REGEX = r'^(.*?)-\d+.\d+.\d+'
    with open(target_index_path, 'r') as infile:
        curr_index = json.loads(infile.read())
    for entry in updated_indexes:
        filename = entry['filename']
        extension_name = re.findall(NAME_REGEX, filename)[0].replace('_', '-')
        if extension_name not in curr_index['extensions'].keys():
            print("Adding '{}' to index...".format(filename))
            curr_index['extensions'][extension_name] = [entry]
        else:
            print("Updating '{}' in index...".format(filename))
            curr_entry = next((ext for ext in curr_index['extensions'][extension_name] if ext['filename'] == entry['filename']), None)
            if curr_entry is not None:  # in case of overwrite
                curr_entry = entry
            else:
                curr_index['extensions'][extension_name].append(entry)

    with open(os.path.join(target_index_path), 'w') as outfile:
        outfile.write(json.dumps(curr_index, indent=4, sort_keys=True))


def main():
    import shutil
    import tempfile
    import glob
    from azure.storage.blob import BlockBlobService
    from os.path import isdir, join

    temp_dir = tempfile.mkdtemp()
    built_extensions = dict([(os.path.basename(f.split('-')[0]), os.path.basename(f)) for f in glob.glob('dist/*.whl')])
    current_extensions = dict([(os.path.basename(d), None) for d in glob.glob("msgraph-cli-extensions/beta/*") if isdir(os.path.abspath(d)) and os.path.basename(d) in built_extensions])

    os.mkdir(os.path.join(temp_dir, 'target'))
    target_index_path = os.path.join(temp_dir, 'target', 'index.json')
    client = BlockBlobService(connection_string=STORAGE_CONNECTION_STRING)
    updated_indexes = []
    print('Uploading {} extensions...\n'.format(len(built_extensions.keys())))
    # start with an empty index.json to sync all extensions
    initial_index = {"extensions": {}, "formatVersion": "1"}
    open(target_index_path, 'w').write(json.dumps(initial_index, indent=4, sort_keys=True))
    for ext_name in current_extensions:
        ext_file = built_extensions[ext_name]
        print('Uploading {}'.format(ext_file))
        ext_info = {}
        _upload_wheel(ext_info=ext_info, updated_indexes=updated_indexes, ext_file=ext_file, ext_name=ext_name, client=client)

        # for ext in current_extensions[extension_name]:
        #     print('Uploading {}'.format(ext['filename']))
        #     _sync_wheel(ext, updated_indexes, failed_urls, client, True, temp_dir)

    print("")
    _update_target_extension_index(updated_indexes, target_index_path)
    index_name = f'{BLOB_PREFIX}/index.json' if BLOB_PREFIX else 'index.json'
    client.create_blob_from_path(container_name=STORAGE_CONTAINER, blob_name=index_name,
                                 file_path=os.path.abspath(target_index_path))
    print("\nUpload finished.")
    if updated_indexes:
        print("New extensions available in:")
    for updated_index in updated_indexes:
        print(updated_index['downloadUrl'])
    shutil.rmtree(temp_dir)

    # if failed_urls:
    #     print("\nFailed to download and sync the following files. They are skipped:")
    #     for url in failed_urls:
    #         print(url)
    #     print("")
    #     raise Exception("Failed to sync some packages.")


if __name__ == '__main__':
    main()