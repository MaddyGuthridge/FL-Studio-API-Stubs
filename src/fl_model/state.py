
from copy import deepcopy
from typing import Optional
from .models import Model, default_model
from .configuration import updateConfig


state: Model = default_model()


def getState() -> Model:
    """
    Returns a reference to the current state of the FL Studio model

    This state can be modified as required, and changes will be reflected in
    the current state

    ## Returns:
    * `Model`: FL state

    ## Example Usage
    """
    return state


def setState(new_state: Model) -> None:
    """
    Sets the current state of the FL Studio model

    The `new_state` is copied before setting it, so that the original state
    won't be modified by future changes

    ## Args:
    * `new_state` (`Model`): state to set to
    """
    global state
    state = deepcopy(new_state)


def resetState() -> None:
    """
    Resets the state of the FL Studio model to the default
    """
    updateConfig()
    setState(default_model())


class FlContext:
    """
    A context manager that can be used to temporarily modify the FL Studio
    model's state. When the context is entered, a reference to the state is
    given, so that modifications to the state can be made easily. At the end of
    the context, the state is reset to what it was when the state was created.

    ## Example Usage

    ```py
    # Create a copy of the state
    with FlContext() as fl:
        # Set the state, so that playback is happening
        fl.transport.playing = True
        assert transport.isPlaying()
    # When the context closes, the state is reset
    assert not transport.isPlaying()
    ```
    """
    def __init__(self) -> None:
        self.__old_state: Optional[Model] = None

    def __enter__(self):
        self.__old_state = deepcopy(getState())
        return getState()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        assert self.__old_state is not None
        setState(self.__old_state)
