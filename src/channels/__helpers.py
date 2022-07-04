"""
channels > helpers

Helper functions for working with channels
"""
from fl_model.exceptions import FlIndexError
from fl_model.channels import getChannelsInGroup
from fl_model import getState


def checkGroupIndex(index: int) -> None:
    """
    Ensures that the index lies within the allowed range for groups

    ## Args:
    * `index` (`int`): index to check
    """
    if not 0 <= index < len(getChannelsInGroup()):
        raise FlIndexError()


def checkGlobalIndex(index: int) -> None:
    if not 0 <= index < len(getState().channels.channel_list):
        raise FlIndexError
