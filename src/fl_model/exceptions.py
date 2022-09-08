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
    """
    Raised in places where an IndexError would ordinarily be raised in the API
    (eg when attempting to access a track that does not exist).
    """
    def __init__(self) -> None:
        super().__init__("Index out of range")


class FlInvalidPluginError(FlError):
    """
    Raised when a plugin is invalid (eg sampler plugin, or no plugin on mixer
    slot).
    """
    def __init__(self) -> None:
        super().__init__("Plugin is not valid")


class OperationUnsafeError(FlError):
    """
    Raised when attempting to perform an operation that is currently disabled
    in FL Studio. There are various times where most functionality is disabled.
    * FL Studio is exporting a project
    * A dialog box is open
    * A project is loading
    """
    def __init__(self) -> None:
        super().__init__("Operation unsafe at current time")


class DeviceUnassignedError(FlError):
    """
    Raised when attempting to interact with a device (eg sending a MIDI
    message) if the device isn't currently available to dispatch to (eg if
    the output port is set incorrectly or if FL Studio is currently exporting a
    project).
    """


class ConfigurationError(RuntimeError):
    """
    Failed to load configuration file for the `fl_model`.

    This exception is raised due to poor configuration of the testing system,
    and will never be raised by FL Studio.
    """
