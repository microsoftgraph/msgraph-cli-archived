# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msgraph.cli import read_profile, write_profile
from msgraph.cli.core.constants import DEFAULT_CLOUDS


class CloudManager:
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

        write_profile(self.profile)

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
                write_profile(self.profile)

                # No need to keep looking for the cloud
                break

        return updated

    def delete_cloud(self, name: str):
        result = []

        for cloud in self.profile['user_defined_clouds']:
            if name not in cloud.keys():
                result.append(cloud)

        self.profile['user_defined_clouds'] = result
        write_profile(self.profile)

    def set_current_cloud(self, name: str):
        self.profile['cloud'] = self.get_clouds().get(name)
        write_profile(self.profile)
