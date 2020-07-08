"""
This script installs generated extensions.
"""
import os
import subprocess
import sys
from os import path
from setuptools import sandbox

path_to_extensions = path.join(os.getcwd(), 'msgraph-cli-extensions', 'src')


def install_extension(extensions_directory=path_to_extensions):
    extensions = os.listdir(extensions_directory)
    for extension in extensions:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", path.join(path_to_extensions, extension, 'dist', '{}-0.1.0-py3-none-any.whl'.format(extension))])


install_extension()
