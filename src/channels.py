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
    
    Included since API version 1
    """

def getChannelColor(index: int) -> int:
    """Returns the colour of the channel at `index` (respecting groups)

    Note that colours can be split into or built from components using the
    functions provided in the module `utils`
    * `ColorToRGB()`
    * `RGBToColor()`

    Args:
     * `index` (`int`): index of channel

    Returns:
     * `int`: channel colour (0x--RRGGBB)
    
    Included since API version 1
    """

def setChannelColor(index: int, color: int) -> None:
    """Sets the colour of the channel at `index` (respecting groups)

    Note that colours can be split into or built from components using the
    functions provided in the module `utils`
    * `ColorToRGB()`
    * `RGBToColor()`

    Args:
     * `index` (`int`): index of channel
     * `colour` (`int`): new colour for channel (0x--RRGGBB)
    
    Included since API version 1
    """

def isChannelMuted(index: int) -> int:
    """Returns whether channel is muted (`1`) or not (`0`)

    Args:
     * `index` (`int`): index of channel

    Returns:
     * `int`: mute status
    
    Included since API version 1
    """

def muteChannel(index: int) -> None:
    """Toggles the mute state of the channel at `index`

    Args:
        `index` (`int`): index of channel
    """

def isChannelSolo(index: int) -> int:
    """Returns whether channel is solo (`1`) or not (`0`)

    Args:
     * `index` (`int`): index of channel

    Returns:
     * `int`: solo status
    
    Included since API version 1
    """

def soloChannel(index: int) -> None:
    """Toggles the solo state of the channel at `index`

    Args:
     * `index` (`int`): index of channel
    
    Included since API version 1
    """

def getChannelVolume(index: int) -> float:
    """Returns the normalised volume of the channel at `index`, where `0.0` is
    the minimum value, and `1.0` is the maximum value. Note that the default
    volume for channels is `0.78125`.

    Args:
     * `index` (`int`): index of channel

    Returns:
     * `float`: channel volume
    
    Included since API version 1
    """

def setChannelVolume(index: int, volume: float) -> None:
    """Sets the normalised volume of the channel at `index`, where `0.0` is
    the minimum value, and `1.0` is the maximum value. Note that the default
    volume for channels is `0.78125`.

    Args:
     * `index` (`int`): index of channel
     * `volume` (`float`): channel volume
    
    Included since API version 1
    """

def getChannelPan(index: int) -> float:
    """Returns the normalised pan of the channel at `index`, where `-1.0` is 
    100% left, and `1.0` is 100% right. Note that the default pan for channels 
    is `0.0` (centre).

    Args:
     * `index` (`int`): index of channel

    Returns:
     * `float`: channel pan
    
    Included since API version 1
    """

def setChannelPan(index: int, pan: float) -> None:
    """Sets the normalised pan of the channel at `index`, where `-1.0` is
    100% left, and `1.0` is 100% right. Note that the default
    pan for channels is `0.0` (centre).

    Args:
     * `index` (`int`): index of channel
     * `pan` (`float`): channel pan
    
    Included since API version 1
    """

def getChannelPitch(index: int, mode:int=0) -> 'float | int':
    """Returns the pitch of the channel at `index`. The `mode` parameter is used
    to determine the type of pitch returned.
    
    HELP WANTED: What do the `mode` parameter options mean?
    
    Args:
     * `index` (`int`): index of channel
     * `mode` (`int`, optional):
            * `1`: return value in semitones
            * `2`: return value pitch range???
    
    Returns:
     * `float`: channel pitch (when `mode` is `1`)
     * `int`: channel pitch range (when `mode` is `2`) ???
    
    Included since API version 8
    """

def setChannelPitch(index: int, value: float, mode:int=0) -> 'float | int':
    """Sets the pitch of the channel at `index` to value. The `mode` parameter is used
    to determine the type of pitch set.
    
    HELP WANTED: What do the `mode` parameter options mean?
    
    Args:
     * `index` (`int`): index of channel
     * `value` (`float`): value to set
     * `mode` (`int`, optional):
            * `1`: set value in semitones
            * `2`: set value pitch range???
    
    Included since API version 8
    """

def isChannelSelected(index: int) -> int:
    """Returns whether the channel at `index` is selected (not respecting 
    channel groups).

    Args:
     * `index` (`int`): channel index

    Returns:
     * `int`: whether the channel is selected
    
    Included since API version 1
    """

def selectChannel(index: int, value:int=-1) -> None:
    """Select the channel at `index` (respecting groups).

    Args:
     * `index` (`int`): channel index
     * `value` (`int`, optional): Whether to select or deselect the channel. 
            * `-1` (default): Toggle
            * `0` : Deselect
            * `1`: Select
    
    Included since API version 1
    """

def selectOneChannel(index: int) -> None:
    """Exclusively select the channel at `index` (deselecting any other selected
    channels).

    Args:
        `index` (`int`): channel index
    
    Included since API version 8
    """

def selectedChannel(canBeNone:int=0, offset:int=0, indexGlobal:int=0) -> int:
    """Returns the index of the first selected channel, otherwise the nth
    selected channel where n is `offset` + 1. If n is greater than the number of
    selected channels, the global index of the last selected channel will be
    returned. If `indexGlobal` is set to `1`, this will replicate the behaviour
    of `channelNumber()` by returning global indexes.
    
    NOTE: This function replaces the functionality of `channelNumber()` 
    entirely, with the added functionality of providing indexes respecting 
    groups (when `indexGlobal` is not set).
    
    If `canBeNone` is `1`, no selection will return `-1`. Otherwise, no selection
    will return `0` (representing the first channel).

    Args:
     * `canBeNone` (`int`, optional): Whether the function will return `-1` or 
       `0` when there is no selection. Defaults to `0` (returning `0`).
     * `offset` (`int`, optional): return other selected channels after offset. 
       Defaults to 0.
     * `indexGlobal` (`int`, optional): Whether to return the group index (`0`)
       or the global index (`1`).

    Returns:
     * `int`: index of first selected channel
    
    Included since API version 5
    """

def selectAll() -> None:
    """Selects all channels in the current channel group
    
    Included since API version 1
    """

def deselectAll() -> None:
    """Deselects all channels in the current channel group
    
    Included since API version 1
    """

def getChannelMidiInPort(index: int) -> int:
    """Returns the MIDI port associated with the channel at `index`.

    TODO: Write use cases

    Args:
     * `index` (`int`): channel index

    Returns:
     * `int`: MIDI port associated with channel
    
    Included since API version 1
    """

def getChannelIndex(index: int) -> int:
    """Returns the global index of a channel given the group `index`.

    Args:
     * `index` (`int`): index of channel (respecting groups)

    Returns:
     * `int`: global index of channel
    
    Included since API version 1
    """

def getTargetFxTrack(index: int) -> int:
    """Returns the mixer track that the channel at `index` is linked to.

    Args:
     * index (`int`): index of channel

    Returns:
     * `int`: index of targeted mixer track
    
    Included since API version 1
    """

def isHighlighted() -> int:
    """Returns True when a red highlight rectangle is displayed on the channel
    rack. This rectangle can be displayed using `ui.crDisplayRect()` in the UI
    module. 
    
    These hints can be used to visually indicate on the channel rack where your 
    script is mapping to.

    Returns:
        `int`: whether highlight rectangle is visible.
    """
