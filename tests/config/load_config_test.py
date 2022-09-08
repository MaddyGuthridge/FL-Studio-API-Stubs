"""
tests > config > load_config_test.py

Tests to ensure that the configuration system is working correctly
"""
import pytest
from fl_model.exceptions import FlConfigurationError
from fl_model.config.load_data import getConfig
from fl_model.helpers import file_from_here
from tests.helpers.temp_file import TemporaryFile

fileFromHere = file_from_here.generate(__file__)


def test_load_default_config():
    """
    Can we load the default configuration file?
    """
    # No config file
    getConfig()


def test_load_valid_empty():
    """
    Are we able to load an empty configuration?
    """
    with TemporaryFile(fileFromHere('empty_config.json'), "fl_config.json"):
        getConfig()


def test_load_invalid_bad_property():
    """
    Are we unable to load the configuration if it contains incorrect
    properties?
    """
    with TemporaryFile(fileFromHere('invalid_bad_property.json'), "fl_config.json"):
        with pytest.raises(FlConfigurationError):
            getConfig()


def test_load_invalid_bad_type():
    """
    Are we unable to load the configuration if it contains incorrect
    types?
    """
    with TemporaryFile(fileFromHere('invalid_bad_type.json'), "fl_config.json"):
        with pytest.raises(FlConfigurationError):
            getConfig()
