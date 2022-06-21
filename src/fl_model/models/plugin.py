
from dataclasses import dataclass
from typing import Optional


@dataclass
class PluginParam:
    """
    Parameter of a plugin

    * `name`: name of parameter

    * `value`: value of parameter
    """
    name: str
    value: float = 0.0


@dataclass
class PlugInfo:
    """
    Info on a plugin

    * `name`: name of plugin instance (can be renamed by user)

    * `plug_name`: name of the plugin (immutable)

    * `params`: list of plugin parameters
    """
    plug_name: str
    params: Optional[list[PluginParam]] = None
