
from dataclasses import dataclass
from typing import Optional


@dataclass
class Param:
    """
    Parameter of a plugin

    * `name`: name of parameter

    * `value`: value of parameter
    """
    name: str
    value: float


@dataclass
class PlugInfo:
    """
    Info on a plugin

    * `is_valid`: whether the plugin is valid, in that its properties can be
      accessed. Examples of invalid plugins are th channel rack sampler, and an
      empty plugin on the mixer

    * `name`: name of plugin instance (can be renamed by user)

    * `plug_name`: name of the plugin (immutable)

    * `params`: list of plugin parameters
    """
    is_valid: bool
    plug_name: str
    params: Optional[list[Param]] = None
