from knack.cli import CLIError


class CLIException(CLIError):
    """Exceptions from within msgraph-cli"""


class AuthenticationException(CLIError):
    """Exceptions from credential provider"""


class ServiceException(CLIError):
    """Response errors from Microsoft Graph service"""
