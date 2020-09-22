#!/usr/bin/env bash
#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------

if [[ ! $CLI_VERSION ]]; then
    echo "Please set the CLI_VERSION environment variable, e.g. 1.0.0"
    exit 1
fi

python_version="3.6.10"

python_download_url="https://www.python.org/ftp/python/${python_version}/Python-${python_version}.tgz"

artifacts_dir="artifacts"
temp_scratch_dir="$artifacts_dir/cli_scratch"
build_dir="$artifacts_dir/cli"
python_dir="$artifacts_dir/Python36"
output_dir="out/"
repo_root="../../"

mkdir $artifacts_dir

echo "Cleaning previous build artifacts"
if [[ -d $output_dir ]]; then
    rm -rf $output_dir
fi
mkdir $output_dir

echo "Cleaning build directory"
if [[ -d $build_dir ]]; then 
    rm -rf $build_dir
fi
mkdir $build_dir

echo "Cleaning scratch directory"
if [[ -d $temp_scratch_dir ]]; then
    rm -rf $temp_scratch_dir
fi
mkdir $temp_scratch_dir


if [[ -d ${repo_root}/privates ]]; then 
    cp ${repo_root}/privates $temp_scratch_dir
fi

if [[ -d $python_dir ]]; then
    echo "Using existing Python at $python_dir"
else
    echo "Dowloading python"
    mkdir -p ${python_dir} && \
            wget -qO- https://www.python.org/ftp/python/${python_version}/Python-${python_version}.tgz \
            | tar -xz -C "${python_dir}"
    
    pushd "${python_dir}/Python-3.6.10"
    ./configure  --prefix $(pwd)/python_env &&\
            make && \
            make install
    popd
fi


#TODO: Use absolute path
python="${python_dir}/Python-3.6.10/python_env/bin/python3.6"
pip="${python_dir}/Python-3.6.10/python_env/bin/pip3"

$pip list

pushd "../"
"debian/${python}" install_extensions.py
popd

pushd "../../"
"build_scripts/debian/${python}" setup.py bdist_wheel 
"build_scripts/debian/${python}" setup.py sdist 
popd

$pip install --force-reinstall urllib3==1.24.2 distutils

cli_version=0.0.0-dev
cli_version_revision=1

rm -rf ./debian

export PYBUILD_SYSTEM=distutils

mkdir -p ./debian && \
        CLI_VERSION=${cli_version} CLI_VERSION_REVISION=${cli_version_revision} ./prepare.sh ./debian ../../az.completion ../../ && \
        dpkg-buildpackage -us -uc -rsudo && \
        cp /msgraph-cli_${cli_version}-${cli_version_revision}_all.deb /msgraph-cli_all.deb
