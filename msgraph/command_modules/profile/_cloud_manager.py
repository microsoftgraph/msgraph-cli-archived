# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msgraph.cli import read_profile, write_profile
from msgraph.cli.core.constants import DEFAULT_CLOUDS
from msgraph.cli.core.exceptions import CLIError


class CloudManager:
    '''This class adds support for managing MicrosoftGraph and user defined clouds
    List of supported Microsoft Graph clouds: https://docs.microsoft.com/en-us/graph/deployments
    '''
    def __init__(self):
        self.profile = read_profile()

    def get_clouds(self) -> dict:
        user_defined_clouds = self.profile.get('user_defined_clouds', {})
        supported_clouds = DEFAULT_CLOUDS

        for cloud in user_defined_clouds:
            supported_clouds.update(cloud)
        return supported_clouds

    def create_cloud(self, cloud_name, cloud_endpoints):
        entry = {cloud_name: cloud_endpoints}

        try:
            user_defined_clouds = self.profile['user_defined_clouds']
            user_defined_clouds.append(entry)
        except KeyError:
            self.profile['user_defined_clouds'] = [entry]

        write_profile(self.profile, 'An error occured while creating the cloud.')

    def get_current_cloud(self) -> dict:
        return self.profile.get('cloud', None)

    def update_cloud(self, cloud_name: str, props: dict):
        updated = False
        user_defined_clouds = self.profile.get('user_defined_clouds')

        # Search for the cloud to update in user defined clouds
        for index, cloud in enumerate(user_defined_clouds):
            found = cloud.get(cloud_name, None)

            if found:
                cloud_to_update = cloud[cloud_name]
                cloud_to_update.update(props)

                # Remove the old cloud and replace it with the updated cloud
                user_defined_clouds.pop(index)
                user_defined_clouds.insert(index, {cloud_to_update['name']: cloud_to_update})

                updated = True
                self.profile['user_defined_clouds'] = user_defined_clouds
                write_profile(
                    self.profile,
                    error_msg=f'An error occured while updating  the "{cloud_name}" cloud')

                # No need to keep looking for the cloud
                break

        return updated

    def delete_cloud(self, name: str):
        result = []
        current_cloud = self.profile.get('cloud', None)

        # throw an error if a user attempts to delete a user defined cloud
        if current_cloud and name == current_cloud['name']:
            raise CLIError(f'''The cloud "{name}" could not be deleted because it is a current cloud

To see the current cloud run mg cloud show-current
To change to a different cloud run mg cloud select
''')

        # throw an error if the cloud is not a user defined cloud
        if name not in self.profile['user_defined_clouds']:
            raise CLIError(f'The cloud "{name}" is not a user defined cloud')

        for cloud in self.profile['user_defined_clouds']:
            if name not in cloud.keys():
                result.append(cloud)

        self.profile['user_defined_clouds'] = result
        write_profile(self.profile, error_msg=f'An error occured while deleting the "{name}" cloud')

    def set_current_cloud(self, name: str):
        self.profile['cloud'] = self.get_clouds().get(name)
        write_profile(
            self.profile,
            error_msg=
            'An error occured while setting the selected cloud, the CLI will use the PUBLIC cloud')
