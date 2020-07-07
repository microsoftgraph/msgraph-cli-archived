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
    for extension in extensions:
        sandbox.run_setup(path.join(path_to_extensions, extension,
                                    'setup.py'), ['clean', 'bdist_wheel'])


build_extension()
