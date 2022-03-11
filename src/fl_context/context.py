"""
fl_context > context

Underlying implementation of the FL Context of the stubs
"""

from typing import Any


default_values = {
    "api_version": 19,
    
    "device_assigned": True,
    "device_port": 1,
    "device_name": "Device",
}

values = default_values.copy()

def resetState():
    """
    Reset the context to the default state
    """
    global values
    values = default_values.copy()

def setState(new_state: dict):
    """
    Set the context to a new state
    """
    global values
    values = new_state

def getState() -> dict:
    """
    Get the current state of the context
    """
    return values

def getValue(key: str) -> Any:
    """
    Get the value of a key in the context.

    Used within the stubs to get return values
    """
    return values[key]

def setValue(key: str, value: Any) -> None:
    """
    Set the value of a key in the context.
    
    Can be used within test files to control the stub return
    values.
    """
    values[key] = value

class FlContext:
    """
    A context manager used to temporarily set the context
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
