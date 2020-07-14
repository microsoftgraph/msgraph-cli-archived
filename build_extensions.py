"""
This script builds generated extensions and adds built extensions to a manifest file.
We use the manifest file to tell MainCommandsLoader what extensions to load.
"""

import os
import subprocess
import sys
from os import path
from setuptools import sandbox

path_to_extensions = path.join(os.getcwd(), 'msgraph-cli-extensions', 'src')
path_to_manifest = path.join(os.getcwd(), 'src',
                             'msgraph-cli-core', 'msgraph', 'cli', 'core', 'installed_extensions.py')


def build_extensions(extensions_directory=path_to_extensions):
    extensions = os.listdir(extensions_directory)

    manifest = open(path_to_manifest, 'w+')
    # Clear manifest's content
    manifest.truncate()
    # Change mode to append so that adding an extension's name does not overwrite other content.
    manifest.mode = 'a+'

    manifest.write('installed_extensions = [')

    for extension in extensions:
        add_extension_to_manifest(manifest, extension)
        sandbox.run_setup(path.join(path_to_extensions, extension,
                                    'setup.py'), ['clean', 'bdist_wheel'])

    manifest.write(']')
    manifest.close()


def add_extension_to_manifest(manifest, extension):
    manifest.write(f''' 'azext_{extension}','''+'\n')


build_extensions()
