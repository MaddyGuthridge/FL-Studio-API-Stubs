"""
fl_context

NOTE: This module is not included in FL Studio's runtime, and should not be
imported from within your main script. It is intended to be used within a
testing framework in order to help validate the behaviour of MIDI scripts.

Currently, this module is terribly designed, and is very bare-bones. If there
is enough interest, I will redesign it to improve its usability.

# Values

Set the state's values either using an `FlContext` context manager, or the
`setValue()` function.

* `api_version` (`int`): The version of the API

* `device_assigned` (`bool`): Whether the device is assigned or not

* `device_port` (`int`): The port of the device

* `device_name` (`str`): The name of the device

* `dispatch_targets` (`list[int]`): A list of the ports of potential targets
  used by `device.dispatch()`
"""

from typing import Any


default_values = {
    "api_version": 20,

    "device_assigned": True,
    "device_port": 1,
    "device_name": "Device",
    # List of ports that we can dispatch to
    "dispatch_targets": [],
}

values = default_values.copy()

def resetState():
    """
    Reset the state to its default values
    """
    global values
    values = default_values.copy()

def setState(new_state: dict):
    """
    Replace the state with a new one
    """
    global values
    values = new_state

def getState() -> dict:
    """
    Get the current state of the state
    """
    return values

def getValue(key: str) -> Any:
    """
    Get the value of a key in the state.

    Used within the stubs to get return values
    """
    return values[key]

def setValue(key: str, value: Any) -> None:
    """
    Set the value of a key in the state.

    Can be used within test files to control the stub return
    values.
    """
    values[key] = value

class FlContext:
    """
    A context manager used to temporarily set the testing context.

    To use this, provide a dictionary of values, which will be used by the
    state until the context manager closes.
    """
    def __init__(self, state_mods: dict) -> None:
        self._old_state = getState()
        self._mods = state_mods

    def __enter__(self):
        for k in self._old_state:
            if k not in self._mods:
                self._mods[k] = self._old_state[k]
        setState(self._mods)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        setState(self._old_state)
