"""
channels > properties

Function definitions for managing channel properties.
"""
import midi
import utils
from typing import overload, Literal
from fl_model import getState
from fl_model.decorators import deprecate, since
from fl_model.consts import oo
from fl_model.channels import (
    getChannelsInGroup,
    groupIndexToGlobalIndex,
    checkGroupIndex,
    getGroupedChannelReference,
)
from fl_model.util import clamp


@since(5)
def selectedChannel(
    canBeNone: bool = False,
    offset: int = 0,
    indexGlobal: bool = False,
) -> int:
    """
    Returns the index of the first selected channel, otherwise the nth selected
    channel where n is `offset` + 1. If n is greater than the number of
    selected channels, the global index of the last selected channel will be
    returned. If `indexGlobal` is set to `1`, this will replicate the behavior
    of [channelNumber()](https://miguelguthridge.github.io/FL-Studio-API-Stubs/channels/#channels.channelNumber)
    by returning global indexes.

    ## Note

    * This function replaces the functionality of `channelNumber()`
      entirely, with the added functionality of providing indexes respecting
      groups (when `indexGlobal` is not set).

    ## Args

    * `canBeNone` (`bool`, optional): Whether the function will return `-1` or
      `0` when there is no selection. Defaults to `False` (returning `0`).

    * `offset` (`int`, optional): return other selected channels after offset.
      Defaults to 0.

    * `indexGlobal` (`bool`, optional): Whether to return the group index
      (`False`) or the global index (`True`).

    ## Returns

    * `int`: index of first selected channel.

    Included since API version 5
    """
    if indexGlobal:
        return channelNumber(canBeNone, offset)
    found = 0
    for i, i_global in enumerate(getChannelsInGroup()):
        ch = getState().channels.channel_list[i_global]
        if ch.selected:
            if found == offset:
                return i
            found += 1

    if canBeNone:
        return -1
    else:
        return 0


def channelNumber(canBeNone: bool = False, offset: int = 0) -> int:
    """
    Returns the global index of the first selected channel, otherwise the nth
    selected channel where n is `offset` + 1. If n is greater than the number
    of selected channels, the global index of the last selected channel will be
    returned.

    If `canBeNone` is `1`, no selection will return `-1`. Otherwise, no
    selection will return `0` (representing the first channel).

    ## Args

    * `canBeNone` (`bool`, optional): Whether the function will return `-1` or
      `0` when there is no selection. Defaults to `False` (returning `0`).

    * `offset` (`int`, optional): return other selected channels after offset.
      Defaults to 0.

    ## Returns

    * `int`: global index of first selected channel.

    Included since API version 1.
    """
    found = 0
    for i in getChannelsInGroup():
        if getState().channels.channel_list[i].selected:
            if found == offset:
                return i
            found += 1
    if canBeNone:
        return -1
    else:
        return 0


def channelCount(mode: bool = False) -> int:
    """
    Returns the number of channels on the channel rack. Respect for groups is
    controlled by the `mode` flag.

    ## Args

    * `mode` (`bool`, optional): Whether the number of channels should be
      global. Defaults to `False` (groups respected).

    ## Returns

    * `int`: number of channels.

    Included since API version 1. (updated with optional parameter in API
    version 3).
    """
    if mode:
        return len(getState().channels.channel_list)
    else:
        return len(getChannelsInGroup())


def getChannelName(index: int, useGlobalIndex: bool = False) -> str:
    """
    Returns the name of the channel at `index`.

    ## Args

    * `index` (`int`): index of channel.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when getting the channel name.

    ## Returns:
     * `str`: channel name.

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    return getGroupedChannelReference(index).name


def setChannelName(
    index: int,
    name: str,
    useGlobalIndex: bool = False,
) -> None:
    """
    Sets the name of the channel at `index`.

    If a channel's name is set to "", its name will be set to the default name
    of the plugin or sample.

    ## Args

    * `index` (`int`): index of channel.

    * `name` (`str`): new name for channel.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when setting the channel name.

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    getGroupedChannelReference(index).name = name


def getChannelColor(index: int, useGlobalIndex: bool = False) -> int:
    """
    Returns the color of the channel at `index`.

    Note that colors can be split into or built from components using the
    functions provided in the module [utils](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/).

    * [ColorToRGB()](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/#utils.ColorToRGB)

    * [RGBToColor()](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/#utils.RGBToColor)

    ## Args

    * `index` (`int`): index of channel.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when getting the channel color.

    ## Returns:
     * `int`: channel color (0x--BBGGRR).

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    return getGroupedChannelReference(index).color


def setChannelColor(
    index: int,
    color: int,
    useGlobalIndex: bool = False,
) -> None:
    """
    Sets the color of the channel at `index`.

    Note that colors can be split into or built from components using the
    functions provided in the module [utils](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/).

    * [ColorToRGB()](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/#utils.ColorToRGB)

    * [RGBToColor()](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/#utils.RGBToColor)

    ## Args

    * `index` (`int`): index of channel.

    * `color` (`int`): new color for channel (0x--BBGGRR).

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when setting the channel color.

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    getGroupedChannelReference(index).color = color


def isChannelMuted(index: int, useGlobalIndex: bool = False) -> bool:
    """
    Returns whether channel is muted (`True`) or not (`False`).

    ## Args

    * `index` (`int`): index of channel.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when getting the channel's mute status.

    ## Returns

    * `bool`: mute status.

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    return getGroupedChannelReference(index).muted


def muteChannel(
    index: int,
    value: int = -1,
    useGlobalIndex: bool = False,
) -> None:
    """
    Toggles the mute state of the channel at `index`.

    ## Args

    * `index` (`int`): index of channel.

    * `value` (`int`, optional): new value for mute state.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when muting channel.

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    getGroupedChannelReference(index).muted = not isChannelMuted(index)


def isChannelSolo(index: int, useGlobalIndex: bool = False) -> bool:
    """
    Returns whether channel is solo (`True`) or not (`False`).

    ## Args

    * `index` (`int`): index of channel.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when getting channel solo status.

    ## Returns

    * `bool`: solo status.

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    # Calculate number of enabled channels
    enabled = sum(map(lambda c: not c.muted, getState().channels.channel_list))
    # Channel is the only one enabled
    return enabled == 1 and not isChannelMuted(index)


def soloChannel(index: int, useGlobalIndex: bool = False) -> None:
    """
    Toggles the solo state of the channel at `index`.

    ## Args

    * `index` (`int`): index of channel.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when soloing channel.

    Included since API version 1

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    index_global = getChannelIndex(index)
    for i, c in enumerate(getState().channels.channel_list):
        if index_global == i:
            c.muted = False
        else:
            c.muted = True


def getChannelVolume(
    index: int,
    mode: bool = False,
    useGlobalIndex: bool = False,
) -> float:
    """
    Returns the normalized volume of the channel at `index`, where `0.0` is the
    minimum value, and `1.0` is the maximum value. Note that the default volume
    for channels is `0.78125`. By setting the `mode` flag to `True`, the volume
    is returned in decibels.

    ## Args

    * `index` (`int`): index of channel.

    * `mode` (`int`, optional): whether to return as a float between 0 and 1
      (`False`) or a value in dB (`True`). Defaults to `False`.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when getting channel volume.

    ## Returns

    * `float`: channel volume.

    Included since API version 1

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    index_global = getChannelIndex(index)
    volume = getState().channels.channel_list[index_global].volume
    if mode:
        if volume == 0.0:
            return -oo
        return utils.VolTodB(volume)
    else:
        return volume


def setChannelVolume(
    index: int,
    volume: float,
    pickupMode: int = midi.PIM_None,
    useGlobalIndex: bool = False,
) -> None:
    """
    Sets the normalized volume of the channel at `index`, where `0.0` is the
    minimum value, and `1.0` is the maximum value. Note that the default volume
    for channels is `0.78125`. Use the pickup mode flag to set pickup options.

    ## Args

    * `index` (`int`): index of channel.

    * `volume` (`float`): channel volume.

    * `pickupMode` (`int`, optional): define the pickup behavior. Refer to
      the [manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#pickupModes).

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when setting channel volume.

    Included since API version 1

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    index_global = getChannelIndex(index)
    getState().channels.channel_list[index_global].volume = clamp(volume)


def getChannelPan(index: int, useGlobalIndex: bool = False) -> float:
    """
    Returns the normalized pan of the channel at `index`, where `-1.0` is 100%
    left, and `1.0` is 100% right. Note that the default pan for channels is
    `0.0` (centered).

    ## Args

    * `index` (`int`): index of channel.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when getting channel pan.

    ## Returns

    * `float`: channel pan.

    Included since API version 1

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    index_global = getChannelIndex(index)
    return getState().channels.channel_list[index_global].pan


def setChannelPan(
    index: int,
    pan: float,
    pickupMode: int = midi.PIM_None,
    useGlobalIndex: bool = False,
) -> None:
    """
    Sets the normalized pan of the channel at `index`, where `-1.0` is 100%
    left, and `1.0` is 100% right. Note that the default pan for channels is
    `0.0` (centered). Use the pickup mode flag to set pickup options.

    ## Args

    * `index` (`int`): index of channel.

    * `pan` (`float`): channel pan.

    * `pickupMode` (`int`, optional): define the pickup behavior. Refer to
      the [manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#pickupModes).

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when setting channel pan.

    Included since API version 1

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    index_global = getChannelIndex(index)
    getState().channels.channel_list[index_global].pan = clamp(pan, min=-1)


@overload
def getChannelPitch(
    index: int,
    mode: Literal[1, 2],
    useGlobalIndex: bool = False,
) -> int:
    ...


@overload
def getChannelPitch(
    index: int,
    mode: Literal[0] = 0,
    useGlobalIndex: bool = False,
) -> float:
    ...


@since(8)
def getChannelPitch(
    index: int,
    mode: int = 0,
    useGlobalIndex: bool = False,
) -> 'float | int':
    """
    Returns the current pitch bend (or range) of the channel at `index`. The
    `mode` parameter is used to determine the type of pitch returned.

    ## Args

    * `index` (`int`): index of channel.

    * `mode` (`int`, optional):
          * `0` (default): return the current pitch bend as a factor of the current
              range (usually `-1.0` to `1.0`). Larger values might be reached if the
              pitch is automated with events, for example.

          * `1`: return the current pitch offset in cents.
              * BUG: Official API docs incorrectly state "semitones".

          * `2`: return the current pitch range in semitones.
              * BUG: This is not guaranteed to be correct.
                For more information, see `setChannelPitch` on
                modifying the pitch range of a channel.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when getting channel pitch.

    ## Returns

    * `float`: channel pitch (when `mode` is `0`).

    * `int`: channel pitch range (when `mode` is `1` or 2).

    Included since API version 8.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    return 0.0


@since(8)
def setChannelPitch(
    index: int,
    value: float,
    mode: int = 0,
    pickupMode: int = midi.PIM_None,
    useGlobalIndex: bool = False,
) -> None:
    """
    Sets the pitch of the channel at `index` to value. The `mode` parameter is
    used to determine the type of pitch set. Use the pickup mode flag to set
    pickup options. The final pitch will be clamped to the current pitch range.

    ## Args

    * `index` (`int`): index of channel.

    * `value` (`float`): value to set.

    * `mode` (`int`, optional):
          * `0` (default): set pitch as a factor of the current pitch bend range (between [-1.0, 1.0]).

          * `1`: set pitch in cents.

          * `2`: **UTTERLY BROKEN.** Set the pitch range in semitones.

            BUG: This only affects the range reported by `getChannelPitch`.
            This will desynchronize the reported range from what is visible in the UI.

    * `pickupMode` (`int`, optional): define the pickup behavior. Refer to
      the [manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#pickupModes).

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when setting channel pitch.

    Included since API version 8.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)


@since(19)
def getChannelType(index: int, useGlobalIndex: bool = False) -> int:
    """
    Returns the type of instrument loaded into the channel rack at `index`.

    ## Args

    * `index` (`int`): index of channel.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when querying channel type.

    ## Returns

    * `int`: type of channel:
          * `GT_Sampler` (`0`): internal sampler.

          * `GT_Hybrid` (`1`): generator plugin feeding internal sampler.

          * `GT_GenPlug` (`2`): generator plugin.

          * `GT_Layer` (`3`): layer (refer to the [FL Studio Manual](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/chansettings_layer.htm)).

          * `GT_AutoClip` (`4`): automation clip.

    Included since API Version 19.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    index_global = getChannelIndex(index)
    return getState().channels.channel_list[index_global].ch_type.value


def isChannelSelected(index: int, useGlobalIndex: bool = False) -> bool:
    """
    Returns whether the channel at `index` is selected.

    ## Args

    * `index` (`int`): channel index.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index.

    ## Returns

    * `bool`: whether the channel is selected.

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    index_global = getChannelIndex(index)
    return getState().channels.channel_list[index_global].selected


@since(8)
def selectOneChannel(index: int, useGlobalIndex: bool = False) -> None:
    """
    Exclusively select the channel at `index` (deselecting any other selected
    channels).

    Using global indexes to select a channel outside of the current group
    deselects all channels.

    ## Args

    * `index` (`int`): channel index.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when selecting channels.

    Included since API version 8.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    deselectAll()
    index_global = getChannelIndex(index)
    getState().channels.channel_list[index_global].selected = True


def selectChannel(
    index: int,
    value: int = -1,
    useGlobalIndex: bool = False,
) -> None:
    """
    Select the channel at `index` (respecting groups).

    Using global indexes to select a channel outside of the current group has
    no effect.

    ## Args

    * `index` (`int`): channel index.

    * `value` (`int`, optional): Whether to select or deselect the channel.
          * `-1` (default): Toggle

          * `0` : Deselect

          * `1`: Select

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when selecting channels.

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    if value == -1:
        bool_val = not isChannelSelected(index)
    else:
        bool_val = bool(value)
    index_global = getChannelIndex(index)
    getState().channels.channel_list[index_global].selected = bool_val


def selectAll() -> None:
    """
    Selects all channels in the current channel group.

    Included since API version 1.
    """


def deselectAll() -> None:
    """
    Deselects all channels in the current channel group.

    Included since API version 1.
    """


def getChannelMidiInPort(index: int, useGlobalIndex: bool = False) -> int:
    """
    Returns the MIDI-in port associated with the channel at `index`.

    Channel MIDI-in ports can be used to send data directly to channels.
    Although channels are unassigned by default, a user can configure plugins
    to receive MIDI on a certain channel which can unlock many useful
    plugin-specific features.

    Note that triggering notes using `channels.midiNoteOn` means that this
    functionality may be lost, so developers should take care to ensure that
    `getChannelMidiInPort` is checked to ensure that scripts don't
    inadvertently override this behavior.

    ## Args

    * `index` (`int`): channel index.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index when querying channel MIDI-in port.

    ## Returns

    * `int`: MIDI port associated with channel.

    * `-3`: Channel receiving notes from touch keyboard.

    * `-2`: Channel not assigned to a MIDI port.

    * `-1`: Channel receiving notes from typing keyboard.

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    return 0


def getChannelIndex(index: int) -> int:
    """
    Returns the global index of a channel given the group `index`.

    ## Args

    * `index` (`int`): index of channel (respecting groups).

    ## Returns

    * `int`: global index of channel.

    Included since API version 1.
    """
    checkGroupIndex(index)
    return groupIndexToGlobalIndex(index)


def getTargetFxTrack(index: int, useGlobalIndex: bool = False) -> int:
    """
    Returns the mixer track that the channel at `index` is linked to.

    ## Args

    * `index` (`int`): index of channel.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index.

    ## Returns

    * `int`: index of targeted mixer track.

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    return 0


def setTargetFxTrack(
    channelIndex: int,
    mixerIndex: int,
    useGlobalIndex: bool = False,
) -> None:
    """
    Sets the mixer track that the channel at `index` is linked to.

    ## Args

    * `channelIndex` (`int`): index of channel to link from.

    * `mixerIndex` (`int`): index of mixer track to link to.

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index.

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(channelIndex)


def getRecEventId(index: int, useGlobalIndex: bool = False) -> int:
    """
    Return the starting point of REC event IDs for the channel at `index`.

    See the [event mapping tutorial](https://miguelguthridge.github.io/FL-Studio-API-Stubs/tutorials/event_mapping/)
    for more information on REC events.

    ## Args

    * `index` (`int`): channel index

    * `useGlobalIndex` (`bool`, optional): whether to use the global channel
      index.

    ## Returns

    * `int`: REC event ID offset for accessing `midi.REC_Chan_*` parameters

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    checkGroupIndex(index)
    return 0


def incEventValue(eventId: int, step: int, res: float = 1 / 24) -> int:
    """
    Get event value increased by step.

    This can be used to map encoder-style controls to events, by allowing them
    to adjust a parameter using a delta value.

    Use result as new value in [general.processRECEvent()](https://miguelguthridge.github.io/FL-Studio-API-Stubs/general/#general.processRECEvent).

    ## Example usage

    ```py
    # Increases the volume of channel 0 by a small delta of 1
    delta = 1
    # Calculate the event ID for the volume of channel 0
    event_id = midi.REC_Chan_Vol + channels.getRecEventId(0)
    # Get the value adjusted by the delta
    new_value = channels.incEventValue(event_id, delta)
    # Process the new value
    general.processRECEvent(event_id, new_value, midi.REC_UpdateValue | midi.REC_UpdateControl)
    ```

    ## Args

    * `eventId` (`int`): event ID (see the [event mapping tutorial](https://miguelguthridge.github.io/FL-Studio-API-Stubs/tutorials/event_mapping/)).

    * `step` (`int`): delta value for the event.

    * `res` (`float`, optional): increment resolution, used as a multiplier to
      ensure that encoders are responsive. Defaults to `1/24`.

    ## Returns

    * `int`: incremented event value, for use in `general.processRECEvent()`.

    Included since API version 1.

    ## API Changes

    * v33: add `useGlobalIndex` flag.
    """
    return 0


@deprecate(7)
def processRECEvent(eventId: int, value: int, flags: int, /) -> int:
    """
    Processes a recording event.

    ## WARNING

    * This function is deprecated here, and moved to `general.processRECEvent`
      as of API version 7.

    Included since API version 1.

    Deprecated since API version 7.
    """
    return 0
