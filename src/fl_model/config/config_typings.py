"""
fl_model > config > config_typings

Contains the type definition for the configuration file to help allow for type
safety when working with it.
"""

from typing import TypedDict, Union, Literal


class FlModelConfig(TypedDict):
    """
    A type definition for the configuration file
    """
    disallowDeprecated: bool
    disallowKeyEchoes: bool
    targetApiVersion: Union[
        int,
        Union[
            Literal["latest"],
            Literal["20.9.2"],
            Literal["20.8.4"],
        ]
    ]
    unsupportedFunctionBehavior: Union[
        Literal["nothing"],
        Literal["warning"],
        Literal["error"],
    ]