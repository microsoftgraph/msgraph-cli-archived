import json
from msgraph.cli.core.constants import PROFILE_LOCATION
from msgraph.cli.core.exceptions import CLIException


def read_profile() -> dict:
    result = None

    try:
        with open(PROFILE_LOCATION, 'r') as file:
            result = file.read()
        return json.loads(result)
    except IOError as ex:
        return {}


def write_profile(profile: str):
    try:
        with open(PROFILE_LOCATION, 'w') as file:
            file.write(profile)
    except IOError as ex:
        raise CLIException('Selected cloud was not set, CLI will use the PublicCLoud') from ex