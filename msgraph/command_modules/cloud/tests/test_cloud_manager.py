import unittest

from pathlib import Path
from os import path, remove

from msgraph.command_modules.cloud._cloud_manager import CloudManager
from msgraph.cli.core.profile import ProfileProvider
from msgraph.cli.core.constants import DEFAULT_CLOUDS, DEFAULT_PROFILE
from msgraph.cli.core.exceptions import CLIError

TEST_PROFILE_LOCATION = 'test-profile.json'
TEST_CLOUD = {
    'graph_endpoint': 'https://graph.microsoft.com',
    'azure_ad_endpoint': 'https://microsoftonline.com'
}


class TestCloudManager(unittest.TestCase):
    def setUp(self):
        self.profile_provider = ProfileProvider(TEST_PROFILE_LOCATION)
        self.profile_provider.write_profile(DEFAULT_PROFILE, error_msg='Could not create profile')
        self.cloud_manager = CloudManager(self.profile_provider)

    def tearDown(self):
        remove(TEST_PROFILE_LOCATION)

    def test_get_clouds_returns_default_clouds_by_default(self):
        clouds = self.cloud_manager.get_clouds()
        self.assertEqual(DEFAULT_CLOUDS, clouds)

    def test_can_create_user_defined_cloud(self):
        self.cloud_manager.create_cloud('TEST_CLOUD', TEST_CLOUD)

        new_cloud_name = list(self.cloud_manager.get_clouds().keys())[-1]

        self.assertEqual('TEST_CLOUD', new_cloud_name)

    def test_can_set_current_cloud(self):
        self.cloud_manager.set_current_cloud('PUBLIC')

        current_cloud = self.profile_provider.read_profile()['cloud']
        self.assertEqual('PUBLIC', current_cloud['name'])

    def test_can_update_cloud(self):
        self.cloud_manager.create_cloud('TEST_CLOUD', TEST_CLOUD)
        self.cloud_manager.update_cloud('TEST_CLOUD', {'name': 'TESTED_CLOUD'})

        updated_cloud_name = list(self.cloud_manager.get_clouds().keys())[-1]
        self.assertEqual('TESTED_CLOUD', updated_cloud_name)

    def test_can_delete_cloud(self):
        self.cloud_manager.create_cloud('TEST_CLOUD', TEST_CLOUD)
        self.cloud_manager.delete_cloud('TEST_CLOUD')
        user_defined_clouds = self.profile_provider.read_profile().get('user_defined_clouds')
        self.assertEqual(len(user_defined_clouds), 0)

    def test_throws_an_error_when_deleting_a_default_cloud(self):
        with self.assertRaises(Exception):
            try:
                self.cloud_manager.delete_cloud('PUBLIC')
            except Exception as error:
                self.assertEqual(error, 'The cloud "PUBLIC" is not a user defined cloud')
