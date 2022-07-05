"""
fl_model > exceptions

Contains definitions for exceptions produced by the API. Note that in all
cases, FL Studio actually raises a TypeError. These exceptions are mainly used
for unit tests for the API stubs. They should not be used within runtime code.
"""


class FlError(TypeError):
    """
    Errors raised by the mock API, useful for unit tests
    """


class FlIndexError(FlError):
    """IndexError but within FL Studio"""
    def __init__(self) -> None:
        super().__init__("Index out of range")


class FlInvalidPluginError(FlError):
    """
    Called when a plugin is invalid (eg sampler plugin, or no plugin on mixer
    slot)
    """
    def __init__(self) -> None:
        super().__init__("Plugin is not valid")


class OperationUnsafeError(FlError):
    """
    Operation in FL Studio is unsafe
    """
    def __init__(self) -> None:
        super().__init__("Operation unsafe at current time")
