"""
This script builds generated extensions.
"""
import os
import subprocess
import sys
from os import path
from setuptools import sandbox

path_to_extensions = path.join(os.getcwd(), 'msgraph-cli-extensions', 'src')


def build_extension(extensions_directory=path_to_extensions):
    extensions = os.listdir(extensions_directory)

    file_to_write = open(path.join(os.getcwd(), 'src',
                                   'msgraph-cli-core', 'msgraph', 'cli', 'core', 'installed_extensions.py'), 'w+')
    file_to_write.truncate()

    file_to_write.write('installed_extensions = [')
    file_to_write.close()

    for extension in extensions:
        create_extensions_manifest(extension)
        sandbox.run_setup(path.join(path_to_extensions, extension,
                                    'setup.py'), ['clean', 'bdist_wheel'])

    file_to_write = open(path.join(os.getcwd(), 'src',
                                   'msgraph-cli-core', 'msgraph', 'cli', 'core', 'installed_extensions.py'), 'a+')
    file_to_write.write(']')
    file_to_write.close()


def create_extensions_manifest(extension):
    with open(path.join(os.getcwd(), 'src', 'msgraph-cli-core', 'msgraph', 'cli', 'core', 'installed_extensions.py'), 'a+') as file:
        file.write(f''' 'azext_{extension}','''+'\n')


build_extension()
