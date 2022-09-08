"""
fl_model > config > load_data

Responsible for loading and validating data in the FL Studio configuration.
"""

import json
import jsonschema
import pathlib
from .config_typings import FlModelConfig


def loadConfig():
    """
    Load the configuration file and return the JSON object
    """
    return json.load(open("fl_config.json"))


def loadSchema():
    """
    Load the JSON schema used to validate the configuration
    """
    schema_file = str(pathlib.Path(__file__)
                             .parent
                             .joinpath("config_schema.json"))
    return json.load(open(schema_file))


def loadDefaultConfig():
    """
    Load the default configuration file
    """
    config_file = str(pathlib.Path(__file__)
                             .parent
                             .joinpath("config_default.json"))
    return json.load(open(config_file))


def getConfig() -> FlModelConfig:
    """
    Load the configuration if it is set, otherwise load the default
    configuration. The configuration is then validated using the schema.
    """
    try:
        config = loadConfig()
    except OSError:
        config = loadDefaultConfig()
    schema = loadSchema()
    # Validate the config
    try:
        jsonschema.validate(config, schema)
    except jsonschema.ValidationError as e:
        raise RuntimeError(
            "Failed to validate FL Studio API Stubs configuration"
        ) from e
    return config
