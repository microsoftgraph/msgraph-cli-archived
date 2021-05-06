ARG base_image=ubuntu:bionic
FROM ${base_image} AS build-env

ARG DEBIAN_FRONTEND=noninteractive

# Update APT packages
RUN apt-get update
RUN apt-get install -y libssl-dev libffi-dev python3-dev debhelper zlib1g-dev wget dh-python python3 python3-setuptools python3-pip \
        unzip libgirepository1.0-dev libcairo2-dev gir1.2-secret-1

# Download Python source code
ARG python_version="3.6.10"
ENV PYTHON_SRC_DIR=/usr/src/python
RUN mkdir -p ${PYTHON_SRC_DIR} && \
        wget -qO- https://www.python.org/ftp/python/${python_version}/Python-${python_version}.tgz \
        | tar -xz -C "${PYTHON_SRC_DIR}"

WORKDIR /msgraph-cli
RUN ${PYTHON_SRC_DIR}/*/configure --srcdir ${PYTHON_SRC_DIR}/* --prefix $(pwd)/python_env &&\
        make && \
        make install && \
        ln /msgraph-cli/python_env/bin/python3 /msgraph-cli/python_env/bin/python && \
        ln /msgraph-cli/python_env/bin/pip3 /msgraph-cli/python_env/bin/pip

ENV PATH=/msgraph-cli/python_env/bin:$PATH

RUN pip install --upgrade pip && pip install wheel pygobject

COPY . .

RUN chmod u+x ./build_scripts/debian/build.sh && \
        chmod u+x ./build_scripts/debian/prepare.sh

RUN mkdir -p ./bin/pypi && \
        BUILD_STAGINGDIRECTORY=/msgraph-cli/bin/pypi ./build_scripts/debian/build.sh && \
        if [ -d ./privates ]; then find ./privates -name '*.whl' | xargs pip install; fi && \
        find ./bin/pypi -name '*.whl' | xargs pip3 install && \
        pip install --force-reinstall urllib3==1.24.2

ARG cli_version=0.0.0-dev
ARG cli_version_revision=1

RUN mkdir -p ./debian && \
        CLI_VERSION=${cli_version} CLI_VERSION_REVISION=${cli_version_revision} ./build_scripts/debian/prepare.sh ./debian ./az.completion ./ && \
        dpkg-buildpackage -us -uc && \
        cp /msgraph-cli_${cli_version}-${cli_version_revision}_all.deb /msgraph-cli_all.deb

RUN dpkg -i /msgraph-cli_all.deb