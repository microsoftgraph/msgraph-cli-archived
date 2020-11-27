import json
from msgraph.cli.core.constants import PROFILE_LOCATION, DEFAULT_CLOUDS
from msgraph.cli.core.exceptions import CLIException


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


def read_profile() -> dict:
    result = None

    try:
        with open(PROFILE_LOCATION, 'r') as file:
            result = file.read()
        return json.loads(result)
    except IOError as ex:
        # This error will be thrown if a user has not selected a cloud before.
        # Returning an empty dictionary so that the result can be processed by json.loads()
        return {}


def write_profile(profile: dict):
    try:
        with open(PROFILE_LOCATION, 'w') as file:
            file.write(json.dumps(profile))
    except IOError as ex:
        raise CLIException('Selected cloud was not set, CLI will use the PublicCLoud') from ex