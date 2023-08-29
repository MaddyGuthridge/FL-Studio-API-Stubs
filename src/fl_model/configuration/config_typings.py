"""
fl_model > config > config_typings

Contains the type definition for the configuration file to help allow for type
safety when working with it.
"""

from typing import TypedDict, Union, Literal


ApiVersion = Union[
    int,
    # Only need to add more here for major and minor updates (not bug fixes)
    Union[
        Literal["latest"],
        Literal["21.0.3"],
        Literal["20.9.2"],
        Literal["20.8.4"],
    ]
]


class FlModelConfig(TypedDict):
    """
    A type definition for the configuration file
    """
    disallowDeprecatedFunctions: bool
    disallowFutureFunctions: bool
    disallowKeyEchoes: bool
    targetApiVersion: ApiVersion
