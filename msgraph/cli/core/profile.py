import json
from msgraph.cli.core.exceptions import CLIException


class ProfileProvider:
    def __init__(profile_location: string):
        self.profile_location = profile_location

    def read_profile(self) -> dict:
        result = None

        try:
            with open(self.profile_location, 'r') as file:
                result = file.read()
            return json.loads(result)
        except IOError as ex:
            # This error will be thrown if a user has not selected a cloud before.
            # Returning an empty dictionary so that the result can be processed by json.loads()
            return {}

    def write_profile(self, profile: dict, error_msg: str):
        try:
            with open(self.profile_location, 'w') as file:
                file.write(json.dumps(profile))
        except IOError as ex:
            raise CLIException(error_msg) from ex
