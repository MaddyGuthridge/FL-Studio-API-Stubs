"""
fl_model > config

Contains code for parsing and validating `fl_config.json` files.
"""
from .load_data import getConfig

__all__ = [
    "config",
]

config = getConfig()
