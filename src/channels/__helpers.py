"""
channels > helpers

Helper functions for working with channels
"""
from fl_model.exceptions import FlIndexError
from fl_model.channels import getChannelsInGroup, ChannelPlug
from fl_model import getState


def checkGroupIndex(index: int) -> None:
    """
    Ensures that the index lies within the allowed range for group indexes

    ## Args:
    * `index` (`int`): index to check
    """
    if not 0 <= index < len(getChannelsInGroup()):
        raise FlIndexError()


def checkGlobalIndex(index: int) -> None:
    """
    Ensures that the index lies within the allowed range for global indexes

    ## Args:
    * `index` (`int`): index to check
    """
    if not 0 <= index < len(getState().channels.channel_list):
        raise FlIndexError


def getGroupedChannelReference(index: int) -> ChannelPlug:
    """
    Returns a reference to a channel given its group index

    ## Args:
    * `index` (`int`): group index

    ## Returns:
    * `ChannelPlug`: channel
    """
    return getState().channels.channel_list[getChannelsInGroup()[index]]


def clamp(value: float, min: float = 0, max: float = 1) -> float:
    """
    Clamps the given value to be within the range required
    """
    if value < min:
        return min
    elif value > max:
        return max
    else:
        return value
