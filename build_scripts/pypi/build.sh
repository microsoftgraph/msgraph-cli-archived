#!/usr/bin/env bash

set -ev

echo "Starting at `pwd`"

: "${BUILD_STAGINGDIRECTORY:?BUILD_STAGINGDIRECTORY environment variable not set}"
: "${BUILD_SOURCESDIRECTORY:=`cd $(dirname $0); cd ../../; pwd`}"

cd $BUILD_SOURCESDIRECTORY

echo "Search setup files from `pwd`."
python3 --version

pip3 install -U pip setuptools wheel
pip3 list

python3 setup.py bdist_wheel -d $BUILD_STAGINGDIRECTORY
python3 setup.py sdist  -d $BUILD_STAGINGDIRECTORY
