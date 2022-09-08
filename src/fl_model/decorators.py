"""
fl_model > decorators

Contains decorators used throughout the project
"""
from functools import wraps
from fl_model import config
from fl_model.configuration.target_version import processVersion
from fl_model.exceptions import FlCallDeprecatedError, FlCallFutureError


def prettyVersion(version) -> str:
    if isinstance(config["targetApiVersion"], str):
        return f"{version} ({config['targetApiVersion']})"
    else:
        return str(version)


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
            target = processVersion(config["targetApiVersion"])
            target_s = config["targetApiVersion"]
            if (
                target >= version
                and config["disallowDeprecatedFunctions"]
            ):
                raise FlCallDeprecatedError(
                    f"Attempt to call deprecated function {func} (target "
                    f"{prettyVersion(target_s)} >= deprecated in {version}"
                )
            else:
                func(*args, **kwargs)
        return inner
    return decorator


def since(version: int):
    """
    Mark an API function as existing since the given version, meaning that it
    shouldn't be used in earlier versions

    ## Args:
    * `version` (`int`): API version where the function was added
    """
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            target = processVersion(config["targetApiVersion"])
            target_s = config["targetApiVersion"]
            if (
                target < version
                and config["disallowFutureFunctions"]
            ):
                raise FlCallFutureError(
                    f"Attempt to call function from the future {func} (target "
                    f"{prettyVersion(target_s)} < added in {version}"
                )
            else:
                func(*args, **kwargs)
        return inner
    return decorator
