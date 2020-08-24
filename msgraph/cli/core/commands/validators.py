class IterateValue(list):
    """Marker class to indicate that, when found as a value in the parsed namespace
    from argparse, the handler should be invoked once per value in the list with all
    other values in the parsed namespace frozen.

    Typical use is to allow multiple ID parameter to a show command etc.
    """
    pass  # pylint: disable=unnecessary-pass


def validate_file_or_dict(string):
    import os
    string = os.path.expanduser(string)
    if os.path.exists(string):
        from msgraph.cli.core.util import get_file_json
        return get_file_json(string)

    from msgraph.cli.core.util import shell_safe_json_parse
    return shell_safe_json_parse(string)


def validate_parameter_set(namespace,
                           required,
                           forbidden,
                           dest_to_options=None,
                           description=None):
    """ validates that a given namespace contains the specified required parameters and does not contain any of
        the provided forbidden parameters (unless the value came from a default). """

    missing_required = [x for x in required if not getattr(namespace, x)]
    included_forbidden = [
        x for x in forbidden if getattr(namespace, x)
        and not hasattr(getattr(namespace, x), 'is_default')
    ]
    if missing_required or included_forbidden:
        from knack.util import CLIError

        def _dest_to_option(dest):
            try:
                return dest_to_options[dest]
            except (KeyError, TypeError):
                # assume the default dest to option
                return '--{}'.format(dest).replace('_', '-')

        error = 'invalid usage{}{}'.format(' for ' if description else ':',
                                           description)
        if missing_required:
            missing_string = ', '.join(
                _dest_to_option(x) for x in missing_required)
            error = '{}\n\tmissing: {}'.format(error, missing_string)
        if included_forbidden:
            forbidden_string = ', '.join(
                _dest_to_option(x) for x in included_forbidden)
            error = '{}\n\tnot applicable: {}'.format(error, forbidden_string)
        raise CLIError(error)
