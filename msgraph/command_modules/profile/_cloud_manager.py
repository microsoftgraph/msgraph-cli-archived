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

    def update_cloud(self):

        pass

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
