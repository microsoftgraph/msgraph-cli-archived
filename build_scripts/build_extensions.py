"""
This script builds generated extensions and adds built extensions to a manifest file.
We use the manifest file to tell MainCommandsLoader what extensions to load.
"""

import os
from os import path
from setuptools import sandbox

path_to_extensions = path.join(os.getcwd(), os.pardir, 'msgraph-cli-extensions', 'src')


def build_extensions(extensions_directory=path_to_extensions):
    extensions = os.listdir(extensions_directory)

    for extension in extensions:
        sandbox.run_setup(path.join(path_to_extensions, extension,
                                    'setup.py'), ['clean', 'bdist_wheel'])


def add_extension_to_manifest(manifest, extension):
    manifest.write(f''' 'azext_{extension}','''+'\n')


build_extensions()
