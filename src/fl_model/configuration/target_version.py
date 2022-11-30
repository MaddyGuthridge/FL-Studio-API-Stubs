"""
fl_model > config > target_version

Contains code used for processing info about target versions
"""
from .config_typings import ApiVersion
from fl_model import consts


def processVersion(version: ApiVersion) -> int:
    """
    Process the configuration's version number setting

    This is used to replace the string constants with proper values

    ## Args:
    * `version` (`ApiVersion`): version number or string

    ## Returns:
    * `int`: version number
    """
    if isinstance(version, int):
        return version

    mappings = {
        "latest": consts.LATEST_API_VERSION,
        "21.0.0": 22,
        "20.9.2": 20,
        "20.8.4": 15,
    }
    return mappings[version]
