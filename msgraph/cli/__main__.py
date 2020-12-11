# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import sys
from os import path

from msgraph.cli.core import get_default_cli
from msgraph.cli.core.constants import DEFAULT_CLOUDS, PROFILE_LOCATION
from msgraph.cli.core.profile import write_profile

mg_cli = get_default_cli()


# Check if a profile exists, if not create one
def create_profile_if_none_exists():
    has_profile = path.exists(PROFILE_LOCATION)

    if not has_profile:
        profile = {'cloud': DEFAULT_CLOUDS['PUBLIC'], 'version': 'v1.0', 'user_defined_clouds': []}
        write_profile(profile, error_msg='An error occured while creating your profile')


def cli_main(cli, args):
    create_profile_if_none_exists()
    return cli.invoke(args)


exit_code = cli_main(mg_cli, sys.argv[1:])
sys.exit(exit_code)
