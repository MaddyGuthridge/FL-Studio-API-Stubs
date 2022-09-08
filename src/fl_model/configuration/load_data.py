"""
fl_model > config > load_data

Responsible for loading and validating data in the FL Studio configuration.
"""
import json
import jsonschema
from fl_model.exceptions import FlConfigurationError
from fl_model.helpers import file_from_here
from .config_typings import FlModelConfig

fileFromHere = file_from_here.generate(__file__)


def loadConfig():
    """
    Load the configuration file and return the JSON object
    """
    return json.load(open("fl_config.json"))


def loadSchema():
    """
    Load the JSON schema used to validate the configuration
    """
    return json.load(open(fileFromHere("schema.json")))


def loadDefaultConfig():
    """
    Load the default configuration file
    """
    return json.load(open(fileFromHere("default.json")))


def getConfig() -> FlModelConfig:
    """
    Load the configuration if it is set, otherwise load the default
    configuration. The configuration is then validated using the schema.
    """
    try:
        config = loadConfig()
    except OSError:
        config = {}
    default_config = loadDefaultConfig()
    schema = loadSchema()
    # Validate the config
    try:
        jsonschema.validate(config, schema)
    except jsonschema.ValidationError as e:
        raise FlConfigurationError(
            "Failed to validate FL Studio API Stubs configuration"
        ) from e
    return default_config | config
