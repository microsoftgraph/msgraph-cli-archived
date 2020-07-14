from __future__ import print_function
from codecs import open
from setuptools import setup, find_packages
import sys
import os


VERSION = "1.0.0"
# If we have source, validate that our version numbers match
# This should prevent uploading releases with mismatched versions
try:
    with open('msgraph/cli/__init__.py', 'r', encoding='utf-8') as f:
        content = f.read()
except OSError:
    pass
else:
    import re

    m = re.search(r'__version__\s*=\s*[\'"](.+?)[\'"]', content)
    if not m:
        print('Could not find __version__ in msgraph/cli/__init__.py')
        sys.exit(1)
    if m.group(1) != VERSION:
        print('Expected __version__ = "{}"; found "{}"'.format(VERSION, m.group(1)))
        sys.exit(1)

cmdclass = {}

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
    'antlr4-python3-runtime~=4.7.2',
    'colorama~=0.4.1',
    'cryptography>=2.3.1,<3.0.0',
    'fabric~=2.4',
    'jsmin~=2.2.2',
    'knack==0.7.1',
    'mock~=4.0',
    'paramiko>=2.0.8,<3.0.0',
    'pyOpenSSL>=17.1.0',
    'pytz==2019.1',
    'requests~=2.22',
    'scp~=0.13.2',
    'six~=1.12',
    'sshtunnel~=0.1.4',
    'urllib3[secure]~=1.18',
    'vsts-cd-manager~=1.0.0,>=1.0.2',
    'websocket-client~=0.56.0',
    'xmltodict~=0.12',
    'javaproperties==0.5.1',
    'jsondiff==1.2.0'
]

with open('README.md', 'r', encoding='utf-8') as f:
    README = f.read()
with open('HISTORY.md', 'r', encoding='utf-8') as f:
    HISTORY = f.read()

setup(
    name='msgraph-cli',
    version=VERSION,
    description='Microsoft Graph Command-Line Tools',
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    author='Microsoft Corporation',
    url='https://github.com/microsoftgraph/msgraph-cli',
    zip_safe=False,
    classifiers=CLASSIFIERS,
    scripts=[
        'mg.bat',
    ],
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=DEPENDENCIES,
    cmdclass=cmdclass
)
