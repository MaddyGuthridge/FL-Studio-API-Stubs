"""Channels Module (FL Studio built-in)

Allows you to control and interact with the FL Studio Channel Rack, and with
instrument channels.

NOTES:
 * In this documentation, an index respects channel groups, whereas a 
   global index does not.
 * Channels are zero-indexed.
"""

def channelNumber(canBeNone:int=0, offset:int=0) -> int:
    """Returns the global index of the first selected channel, otherwise the nth
    selected channel where n is `offset` + 1. If n is greater than the number of
    selected channels, the global index of the last selected channel will be
    returned.
    
    If `canBeNone` is `1`, no selection will return `-1`. Otherwise, no selection
    will return `0` (representing the first channel).

    Args:
     * `canBeNone` (`int`, optional): Whether the function will return `-1` or `0`
       when there is no selection. Defaults to `0` (returning `0`).
     * `offset` (`int`, optional): return other selected channels after offset. Defaults to 0.

    Returns:
     * `int`: global index of first selected channel
    
    Included since API version 1
    """

def channelCount(mode:int=0) -> int:
    """Returns the number of channels on the channel rack. Respect for groups is
    controlled by the `mode` flag.

    Args:
     * `mode` (`int`, optional): Whether the number of channels respects groups. 
       Defaults to 0.

    Returns:
     * `int`: number of channels
    
    Included since API version 1. (updated with optional parameter in API 
    version 3).
    """

def getChannelName(index: int) -> str:
    """Returns the name of the channel at `index` (respecting groups)

    Args:
     * `index` (`int`): index of channel

    Returns:
     * `str`: channel name
    
    Included since API version 1
    """

def setChannelName(index: int, name: str) -> None:
    """Sets the name of the channel at `index` (respecting groups)

    If a channel's name is set to "", its name will be set to the default name
    of the plugin or sample.

    Args:
     * `index` (`int`): index of channel
     * `name` (`str`): new name for channel
    """
