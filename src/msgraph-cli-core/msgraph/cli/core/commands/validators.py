class IterateValue(list):
    """Marker class to indicate that, when found as a value in the parsed namespace
    from argparse, the handler should be invoked once per value in the list with all
    other values in the parsed namespace frozen.

    Typical use is to allow multiple ID parameter to a show command etc.
    """
    pass  # pylint: disable=unnecessary-pass