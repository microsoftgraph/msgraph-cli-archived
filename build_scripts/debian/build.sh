#!/usr/bin/env bash

set -ev

echo "Starting at `pwd`"

: "${BUILD_STAGINGDIRECTORY:?BUILD_STAGINGDIRECTORY environment variable not set}"
: "${BUILD_SOURCESDIRECTORY:=`cd $(dirname $0); cd ../../; pwd`}"

cd $BUILD_SOURCESDIRECTORY

echo "Search setup files from `pwd`."
python --version

pip install -U pip setuptools wheel
pip list

pushd "build_scripts"
    python install_extensions.py
popd

python setup.py bdist_wheel -d $BUILD_STAGINGDIRECTORY
python setup.py sdist  -d $BUILD_STAGINGDIRECTORY
