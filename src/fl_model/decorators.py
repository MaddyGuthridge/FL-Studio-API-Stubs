"""
fl_model > decorators

Contains decorators used throughout the project
"""
from functools import wraps
from fl_model import getState, config
from fl_model.exceptions import (
    FlCallDeprecatedError,
    FlCallFutureError,
    FlCallKeyEchoError,
)


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
            target = getState().general.api_version
            if (
                target >= version
                and config["disallowDeprecatedFunctions"]
            ):
                raise FlCallDeprecatedError(
                    f"Attempt to call deprecated function {func} (target "
                    f"{target} >= deprecated in {version}"
                )
            else:
                return func(*args, **kwargs)
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
            target = getState().general.api_version
            if (
                target < version
                and config["disallowFutureFunctions"]
            ):
                raise FlCallFutureError(
                    f"Attempt to call function from the future {func} (target "
                    f"{target} < added in {version}"
                )
            else:
                return func(*args, **kwargs)
        return inner
    return decorator


def keyEchoes():
    """
    Mark an API function to indicate that it echoes a hotkey

    ## Args:
    * `version` (`int`): API version where the function was added
    """
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if config["disallowKeyEchoes"]:
                raise FlCallKeyEchoError(
                    f"Attempt to call function that echoes key-presses {func}"
                )
            else:
                return func(*args, **kwargs)
        return inner
    return decorator
