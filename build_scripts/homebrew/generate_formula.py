# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import jinja2
import hashlib
from enum import Enum
import requests
from poet.poet import make_graph, RESOURCE_TEMPLATE

TEMPLATE_FILE_NAME = 'formula_template.txt'
CLI_VERSION = os.environ['CLI_VERSION']
GITHUB_RELEASE_TAR = os.environ['GITHUB_RELEASE_TAR']


class BuildMethod(Enum):
    UPDATE_EXISTING = 0
    USE_TEMPLATE = 1


def main():
    generate_formula(build_method=BuildMethod.USE_TEMPLATE)


def generate_formula(build_method: BuildMethod, **_):
    content = ''
    if build_method is None or build_method == BuildMethod.UPDATE_EXISTING:
        pass
    elif build_method == BuildMethod.USE_TEMPLATE:
        content = generate_formula_with_template()
    with open('msgraph-cli.rb', mode='w') as formula:
        formula.write(content)


def generate_formula_with_template() -> str:
    """Generate a brew formula by using a template"""
    template_path = os.path.join(os.path.dirname(__file__), TEMPLATE_FILE_NAME)
    with open(template_path, mode='r') as template:
        template_content = template.read()

    template = jinja2.Template(template_content)
    content = template.render(
        resources=collect_resources(),
        github_release_tar=GITHUB_RELEASE_TAR,
        sha256=compute_sha256(GITHUB_RELEASE_TAR),
        cli_version=CLI_VERSION,
    )

    if not content.endswith('\n'):
        content += '\n'
    return content


def compute_sha256(url: str) -> str:
    sha256 = hashlib.sha256()
    resp = requests.get(url)
    resp.raise_for_status()
    sha256.update(resp.content)

    return sha256.hexdigest()


def collect_resources():   
    # nodes = make_graph('msgraph')
    nodes_render = []
    # for node_name in sorted(nodes):
    #     nodes_render.append(RESOURCE_TEMPLATE.render(resource=nodes[node_name]))
    return '\n\n'.join(nodes_render)


if __name__ == "__main__":
    main()