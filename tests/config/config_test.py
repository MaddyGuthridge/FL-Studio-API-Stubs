"""
tests > config > config_test.py

Tests for the configuration
"""
from fl_model.config import getConfig
from fl_model.helpers import file_from_here
from tests.helpers.temp_file import TemporaryFile

fileFromHere = file_from_here.generate(__file__)


def test_defaults():
    """
    Can we access the default settings?
    """
    config = getConfig()
    assert not config['disallowDeprecated']


def test_empty_config_leaves_defaults():
    """
    When we load an empty config, does it keep the default settings?
    """
    with TemporaryFile(fileFromHere("empty_config.json"), "fl_config.json"):
        config = getConfig()
        assert not config['disallowDeprecated']


def test_override_properties():
    """
    When we load a configuration, does it override the correct properties
    """
    with TemporaryFile(
        fileFromHere("disallow_deprecated.json"),
        "fl_config.json"
    ):
        config = getConfig()
        assert config['disallowDeprecated']
