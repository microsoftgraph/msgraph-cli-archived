#!/usr/bin/env python

#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------

import argparse
import os
import glob
import sys
from posixpath import abspath
from subprocess import check_call

DEFAULT_DEST_FOLDER = "./dist"

class PackageInfo:
    def __init__(self, name, path) -> None:
        self.name = name
        self.path = path


def create_package(info, dest_folder=DEFAULT_DEST_FOLDER):
    absdirpath = (info.path)
    dest = os.path.abspath(dest_folder)
    check_call([sys.executable, 'setup.py', 'bdist_wheel', '-d', dest], cwd=absdirpath)
    # check_call(['python', 'setup.py', "sdist", "--format", "zip", '-d', dest], cwd=absdirpath)

def get_package_info(setup_file) -> PackageInfo:
    dir = os.path.dirname(setup_file)
    absPath = os.path.abspath(dir)
    package_name = os.path.basename(absPath)
    return PackageInfo(package_name, absPath)

def build_extension(source, name, dest_folder=DEFAULT_DEST_FOLDER):
    """
    Build a specific extension in source.
    """
    packages_info = [get_package_info(setup_file) for setup_file in (glob.glob(source + '*/{}/setup.py'.format(name)) + glob.glob(source + '{}/setup.py'.format(name)))]
    create_package(packages_info[0], dest_folder)

def build_extensions(source, dest_folder=DEFAULT_DEST_FOLDER):
    """
    Build all the extensions in source. If source is an parent directory, build all extensions in source. If
    source is an extension directory, build that extension.
    """
    packages_info = [get_package_info(setup_file) for setup_file in glob.glob(source + '*/*/setup.py')]

    for info in packages_info:
        create_package(info, dest_folder)

if __name__ == '__main__':
    """
    This file is used for Swagger CLI extension automation to build the wheel file and zip file
    """
    parser = argparse.ArgumentParser(description='Build Azure package.')
    # parser.add_argument('name', help='The package name')
    parser.add_argument('--dest', '-d', default=DEFAULT_DEST_FOLDER,
                        help='Destination folder. Relative to the package dir. [default: %(default)s]')
    parser.add_argument('--source', '-s',
                        help='Source folder. Relative to the package dir. [default: %(default)s]', required=True)
    args = parser.parse_args()
    # create_package(args.name, args.dest)
    build_extensions(args.source, args.dest)