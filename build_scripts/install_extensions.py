"""
This script installs generated extensions.
"""
import os
import subprocess
import sys
from os import path

path_to_extensions = path.join(os.getcwd(), os.pardir, 'msgraph-cli-extensions', 'src')
path_to_manifest = path.join(os.getcwd(), os.pardir, 'msgraph', 'cli', 'core',
                             'installed_extensions.py')


def install_extension(extensions_directory=path_to_extensions):
    extensions = os.listdir(extensions_directory)

    manifest = open(path_to_manifest, 'w+')
    # Clear manifest's content
    manifest.truncate()
    # Change mode to append so that adding an extension's name does not overwrite other content.
    manifest.mode = 'a+'

    manifest.write('installed_extensions = [')

    extensions = os.listdir(extensions_directory)
    for extension in extensions:
        add_extension_to_manifest(manifest, extension)

        try:
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install',
                path.join(path_to_extensions, extension, '.')
            ])
        except Exception as error:
            print(error)

    manifest.write(']')
    manifest.close()


def add_extension_to_manifest(manifest, extension):
    manifest.write(f''' 'azext_{extension}',''' + '\n')


install_extension()
