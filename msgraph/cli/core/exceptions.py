from knack.cli import CLIError


class CLIException(CLIError):
    """Exceptions from within msgraph-cli"""


class AuthenticationException(CLIError):
    """Exceptions from credential provider handled in msgraph-cli"""


class ServiceException(Exception):
    """Response errors from Microsoft Graph service"""
