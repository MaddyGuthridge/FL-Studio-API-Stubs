"""
fl_model > decorators

Contains decorators used throughout the project
"""
from typing import Callable, TypeVar
from typing_extensions import ParamSpec
from functools import wraps
from fl_model import getState, config
from fl_model.exceptions import (
    FlCallDeprecatedError,
    FlCallFutureError,
    FlCallKeyEchoError,
)

P = ParamSpec('P')
T = TypeVar('T')


def deprecate(version: int) -> Callable[
    [Callable[P, T]],
    Callable[P, T],
]:
    """
    Mark an API function as deprecated, meaning that it shouldn't be used in
    modern versions of the API

    ## Args:
    * `version` (`int`): the version that the function was deprecated in
    """
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs) -> T:
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


def since(version: int) -> Callable[
    [Callable[P, T]],
    Callable[P, T],
]:
    """
    Mark an API function as existing since the given version, meaning that it
    shouldn't be used in earlier versions

    ## Args:
    * `version` (`int`): API version where the function was added
    """
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs):
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


def keyEchoes() -> Callable[
    [Callable[P, T]],
    Callable[P, T],
]:
    """
    Mark an API function to indicate that it echoes a hotkey

    ## Args:
    * `version` (`int`): API version where the function was added
    """
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs):
            if (
                config["disallowKeyEchoes"]
                and getState().general.api_version < 22
            ):
                raise FlCallKeyEchoError(
                    f"Attempt to call function that echoes key-presses {func}"
                )
            else:
                return func(*args, **kwargs)
        return inner
    return decorator
