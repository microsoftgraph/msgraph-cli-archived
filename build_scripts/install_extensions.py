"""
This script installs generated extensions.
"""
import os
import subprocess
import sys
from os import path

path_to_extensions = path.join(os.getcwd(), os.pardir, 'msgraph-cli-extensions', 'src')


def install_extension(extensions_directory=path_to_extensions):
    extensions = os.listdir(extensions_directory)
    for extension in extensions:
        try:
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install',
                path.join(path_to_extensions, extension, 'dist',
                          '{}-0.1.0-py3-none-any.whl'.format(extension))
            ])
        except Exception as error:
            print(error)


install_extension()
