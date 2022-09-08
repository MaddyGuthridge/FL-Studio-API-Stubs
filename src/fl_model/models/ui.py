
from enum import Enum
from dataclasses import dataclass


class WindowIndex(Enum):
    """
    Window selection

    * MIXER (0)

    * CHANNEL_RACK (1)

    * PLAYLIST (2)

    * PIANO_ROLL (3)

    * BROWSER (4)

    """
    MIXER = 0
    CHANNEL_RACK = 1
    PLAYLIST = 2
    PIANO_ROLL = 3
    BROWSER = 4


class ActivitySelection(Enum):
    """
    Activity selection. Can be

    * WINDOW (1),

    * GENERATOR (2), or

    * EFFECT (3)
    """
    WINDOW = 1
    GENERATOR = 2
    EFFECT = 3


@dataclass
class UiModel:
    """
    Model for UI

    # Properties

    * `active_window`: active FL window ID

    * `active_generator`: index on channel rack of active generator plugin

    * `active_effect`: index in mixer of active effect plugin

    * `selection`: determines what is selected (FL Window, generator plugin, or
      effect plugin)
    """
    active_window: WindowIndex
    active_generator: int
    active_effect: tuple[int, int]
    selection: ActivitySelection


def default_ui():
    return UiModel(
        active_window=WindowIndex.MIXER,
        active_generator=0,
        active_effect=(0, 0),
        selection=ActivitySelection.WINDOW
    )
