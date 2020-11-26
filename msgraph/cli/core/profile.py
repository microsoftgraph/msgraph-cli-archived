import json
from msgraph.cli.core.constants import PROFILE_LOCATION
from msgraph.cli.core.exceptions import CLIException


class CloudManager:
    def __init__(self):
        self.profile = read_profile()

    def create_cloud(self, cloud_name, cloud_endpoints):
        entry = {cloud_name: cloud_endpoints}

        try:
            user_defined_clouds = self.profile['user_defined_clouds']
            user_defined_clouds.append(entry)
        except KeyError:
            self.profile['user_defined_clouds'] = [entry]

        write_profile(json.dumps(self.profile))

    def get_current_cloud(self):
        return self.profile.get('cloud', None)

    def update_cloud(self):

        pass

    def delete_cloud(self):
        pass


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


def write_profile(profile: str):
    try:
        with open(PROFILE_LOCATION, 'w') as file:
            file.write(profile)
    except IOError as ex:
        raise CLIException('Selected cloud was not set, CLI will use the PublicCLoud') from ex