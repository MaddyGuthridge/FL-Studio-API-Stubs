"""
fl_model > config

Contains code for parsing and validating `fl_config.json` files.
"""
from .load_data import getConfig

__all__ = [
    "config",
    "updateConfig",
]

config = getConfig()


def updateConfig() -> None:
    """
    Update a configuration by replacing its values with the latest
    configuration.
    """
    # type ignored due to https://github.com/python/mypy/issues/6462
    config.update(getConfig())  # type: ignore
