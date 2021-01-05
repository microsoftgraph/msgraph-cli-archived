"""
This script installs generated extensions.
"""
import os
import subprocess
import sys
from os import path


def install_extension(version='v1.0'):
    extensions_directory = path.join(os.getcwd(), os.pardir, 'msgraph-cli-extensions', f'{version}')
    path_to_manifest = path.join(os.getcwd(), os.pardir, 'msgraph', 'cli', 'core',
                                 f'{version}_installed_extensions.py')

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
                path.join(extensions_directory, extension, '.')
            ])
        except Exception as error:
            print(error)

    manifest.write(']')
    manifest.close()


def add_extension_to_manifest(manifest, extension):
    manifest.write(f''' 'azext_{extension}',''' + '\n')


install_extension(version='v1_0')
install_extension(version='beta')
