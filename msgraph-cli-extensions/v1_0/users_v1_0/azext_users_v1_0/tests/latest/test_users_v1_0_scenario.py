# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from .. import try_manual, raise_if, calc_coverage


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test):
    pass


@try_manual
def cleanup(test):
    pass


@try_manual
def call_scenario(test):
    setup(test)
    cleanup(test)


@try_manual
class UsersScenarioTest(ScenarioTest):

    def test_users_v1_0(self):

        call_scenario(self)
        calc_coverage(__file__)
        raise_if()
