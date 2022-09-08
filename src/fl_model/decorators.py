"""
fl_model > decorators

Contains decorators used throughout the project
"""
from functools import wraps
from fl_model import config
from fl_model.configuration.target_version import processVersion
from fl_model.exceptions import FlCallDeprecatedError


def deprecate(version: int):
    """
    Mark an API function as deprecated, meaning that it shouldn't be used in
    modern versions of the API

    ## Args:
    * `version` (`int`): the version that the function was deprecated in
    """
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if (
                processVersion(config["targetApiVersion"]) >= version
                and config["disallowDeprecated"]
            ):
                raise FlCallDeprecatedError(
                    f"Attempt to call deprecated function {func}")
            else:
                func(*args, **kwargs)
        return inner
    return decorator
