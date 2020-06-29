#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function
from codecs import open
from setuptools import setup

cmdclass = {}

VERSION = "1.0.0"
# If we have source, validate that our version numbers match
# This should prevent uploading releases with mismatched versions.
try:
    with open('msgraph/cli/core/__init__.py', 'r', encoding='utf-8') as f:
        content = f.read()
except OSError:
    pass
else:
    import re
    import sys

    m = re.search(r'__version__\s*=\s*[\'"](.+?)[\'"]', content)
    if not m:
        print('Could not find __version__ in msgraph/cli/core/__init__.py')
        sys.exit(1)
    if m.group(1) != VERSION:
        print('Expected __version__ = "{}"; found "{}"'.format(VERSION, m.group(1)))
        sys.exit(1)

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = [
    'adal~=1.2',
    'argcomplete~=1.8',
    'azure-cli-telemetry',
    'azure-identity',
    'colorama>=0.3.9',
    'humanfriendly>=4.7,<9.0',
    'jmespath',
    'knack==0.7.0rc4',
    'msal~=1.0.0',
    'msal-extensions~=0.1.3',
    'msrest>=0.4.4',
    'msrestazure>=0.6.3',
    'paramiko>=2.0.8,<3.0.0',
    'PyJWT',
    'pyopenssl>=17.1.0',  # https://github.com/pyca/pyopenssl/pull/612
    'requests~=2.20',
    'six~=1.12',
    'pkginfo>=1.5.0.1',
    'azure-mgmt-resource==9.0.0',
    'azure-mgmt-core==1.0.0'
]

TESTS_REQUIRE = [
    'mock'
]

with open('README.md', 'r', encoding='utf-8') as f:
    README = f.read()
with open('HISTORY.md', 'r', encoding='utf-8') as f:
    HISTORY = f.read()

setup(
    name='msgraph-cli-core',
    version=VERSION,
    description='Microsoft Azure Command-Line Tools Core Module',
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    author='Microsoft Corporation',
    author_email='graphtooling@microsoft.com',
    url='https://github.com/microsoftgraph/msgraph-cli',
    zip_safe=False,
    classifiers=CLASSIFIERS,
    packages=[
        'msgraph',
        'msgraph.cli',
        'msgraph.cli.core',
        'msgraph.cli.core.commands',
    ],
    install_requires=DEPENDENCIES,
    extras_require={
        ":python_version<'3.4'": ['enum34'],
        ":python_version<'2.7.9'": ['pyopenssl', 'ndg-httpsclient', 'pyasn1'],
        ':python_version<"3.0"': ['futures'],
        "test": TESTS_REQUIRE,
    },
    tests_require=TESTS_REQUIRE,
    cmdclass=cmdclass
)
