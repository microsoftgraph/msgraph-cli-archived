# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import jinja2
import hashlib
import requests
from poet.poet import make_graph, RESOURCE_TEMPLATE

TEMPLATE_FILE_NAME = 'formula_template.txt'
CLI_VERSION = os.environ['CLI_VERSION']
GITHUB_RELEASE_TAR = os.environ['GITHUB_RELEASE_TAR']


def main():
    generate_formula(build_method='use_template')


def generate_formula(build_method: str, **_):
    content = ''
    if build_method is None or build_method == 'update_existing':
        # content = update_formula()
        pass
    elif build_method == 'use_template':
        content = generate_formula_with_template()
    with open('msgraph-cli.rb', mode='w') as fq:
        fq.write(content)


def generate_formula_with_template() -> str:
    """Generate a brew formula by using a template"""
    template_path = os.path.join(os.path.dirname(__file__), TEMPLATE_FILE_NAME)
    with open(template_path, mode='r') as fq:
        template_content = fq.read()

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
    nodes = make_graph('msgraph')
    nodes_render = []
    for node_name in sorted(nodes):
        nodes_render.append(RESOURCE_TEMPLATE.render(resource=nodes[node_name]))
    return '\n\n'.join(nodes_render)


if __name__ == "__main__":
    main()