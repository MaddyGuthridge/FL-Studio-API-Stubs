
from typing import Optional, Union

from . import consts
from .exceptions import FlIndexError
from .state import getState
from .models import PlugInfo, PluginParam
from .models.channels import (
    ChannelPlug,
    ChannelType,
    default_channels,
)


def addChannel(
    plug: Optional[PlugInfo],
    name: str,
    ch_type: ChannelType,
    index: int = -1,
    target: int = 0,
    group: str = '',
    color: int = consts.DEFAULT_FL_COLOR,
    volume: float = consts.DEFAULT_CHANNEL_VOLUME,
    pan: float = 0.0,
) -> None:
    """
    Add a channel to the channel rack

    ## Args:
    * `plug` (`Optional[PlugInfo]`): plugin info of plugin to add

    * `name` (`str`): name of channel

    * `ch_type` (`ChannelType`): type of channel

    * `index` (`int`, optional): index to insert to. Defaults to end.

    * `target` (`int`, optional): target mixer track. Defaults to `0`.

    * `color` (`int`, optional): color. Defaults to `0x5C656A`.

    * `volume` (`float`, optional): volume. Defaults to `0.78125`.

    * `pan` (`float`, optional): pan. Defaults to `0.0`.
    """
    fl = getState()
    channels = fl.channels.channel_list
    # Insert to end if index == -1
    if index == -1:
        index = len(channels)
    channels.insert(index, ChannelPlug(
        plug,
        name,
        ch_type,
        target,
        group,
        False,
        color,
        volume,
        pan,
    ))
    # Update every pattern
    for pattern in getState().patterns.p:
        pattern.notifyChannelCreate(index)


def removeChannel(index: int) -> None:
    """
    Remove a channel from the channel rack

    ## Args:
    * `index` (`int`): index of channel to remove
    """
    fl = getState()
    fl.channels.channel_list.pop(index)
    # Update every pattern
    for pattern in getState().patterns.p:
        pattern.notifyChannelDestroy(index)


def resetChannels() -> None:
    """
    Reset channels to their default state
    """
    fl = getState()
    fl.channels = default_channels()


def addSampler(
    name: str,
    **kwargs
) -> None:
    """
    Add a sampler to the channel rack

    ## Args:
    * `name` (`string`): name of channel

    * `**kwargs`: other args (refer to optional args for `addChannel()`)
    """
    addChannel(None, name, ChannelType.SAMPLER, **kwargs)


def addFlPlugin(
    name: str,
    plug_name: str,
    params: list[str],
    **kwargs
) -> None:
    """
    Add an FL plugin to the channel rack

    ## Args:
    * `name` (`str`): name of channel

    * `plug_name` (`str`): name of plugin

    * `params` (`list[str]`): list of parameter names (initialized to zero)

    * `**kwargs`: other args (refer to optional args for `addChannel()`)
    """
    param_list = [PluginParam(p) for p in params]
    plug = PlugInfo(plug_name, param_list)
    addChannel(plug, name, ChannelType.GENERATOR, **kwargs)


def addVstPlugin(
    name: str,
    plug_name: str,
    params: list[str],
    **kwargs
) -> None:
    """
    Add a VST plugin to the channel rack

    ## Args:
    * `name` (`str`): name of channel

    * `plug_name` (`str`): name of plugin

    * `params` (`list[str]`): list of parameter names (initialized to zero)

    * `**kwargs`: other args (refer to optional args for `addChannel()`)
    """
    # Generate parameter list
    param_list: list[PluginParam] = []
    for i in range(consts.VST_PARAM_COUNT):
        if i < len(params):
            param_list.append(PluginParam(params[i]))
        elif i in consts.VST_FINAL_PARAM_NAMES:
            param_list.append(PluginParam(consts.VST_FINAL_PARAM_NAMES[i]))
        else:
            param_list.append(PluginParam(''))
    plug = PlugInfo(plug_name, param_list)
    addChannel(plug, name, ChannelType.GENERATOR, **kwargs)


def addToGroup(
    name: str,
    plugs: set[int],
) -> None:
    """
    Add a set of plugins, specified by their global indexes, to a group

    If a group with the given name can't be found, a new one is created

    ## Args:
    * `name` (`str`): nme of group

    * `plugs` (`set[int]`): set of channels to add

    ## Raises:
    * `ValueError`: name of group can't be empty
    """
    channels = getState().channels.channel_list
    for p in plugs:
        try:
            channels[p].group = name
        except IndexError as e:
            raise FlIndexError() from e


def removeChannelFromGroup(idx: int, group: str) -> bool:
    """
    Remove a channel from the group if present. Delete the group if empty.

    ## Args:
    * `idx` (`int`): global index of channel

    * `group` (`str`): group name

    ## Returns:
    * `bool`: whether the channel was removed
    """
    channels = getState().channels.channel_list
    if channels[idx].group == group:
        channels[idx].group = ''
        return True
    return False


def removeChannelFromAnyGroup(idx: int):
    """
    Removes a channel from its group

    ## Args:
    * `plug` (`int`): global index of channel
    """
    channels = getState().channels.channel_list
    channels[idx].group = ''


def getChannelsInGroup(
    group: 'str | ellipsis | None' = None  # noqa: F821
) -> list[int]:
    """
    Return a list of the indexes of channels in a group

    ## Args:
    * `group` (`str | ellipsis | None`)
          * `str`: name of group

          * `''`: unsorted group

          * `...`: all group

          * `None`: current group

    ## Returns:
    * `list[int]`: list of global channel indexes
    """
    if group is None:
        group = getState().channels.selected_group
    if group is ...:
        return list(range(len(getState().channels.channel_list)))
    group_indexes: list[int] = []
    for i, c in enumerate(getState().channels.channel_list):
        if c.group == group:
            group_indexes.append(i)
    return group_indexes


def globalIndexToGroupIndex(idx: int, group: Optional[str] = None) -> int:
    """
    Convert a global channel index to a grouped channel index

    Group argument can be used to validate that the channel is a member of that
    particular group.

    ## Args:
    * `idx` (`int`): global index

    * `group` (`str`, optional): group. Defaults to `None`, for any group.

    ## Raises:
    * `ValueError`: channel not a member of that group

    ## Returns:
    * `int`: group index
    """
    channels = getState().channels.channel_list
    if group is None:
        group = channels[idx].group
    group_idx = 0
    for i, c in enumerate(channels):
        if i == idx:
            if c.group != group:
                raise ValueError("Channel not a member of that group")
            return group_idx
        if c.group == group:
            group_idx += 1
    raise FlIndexError()


def groupIndexToGlobalIndex(
    idx: int,
    group: Union[str, None, 'ellipsis'] = None  # noqa: F821
) -> int:
    """
    Convert a grouped channel index to a global channel index

    Group argument can be used to specify a group to search in.

    ## Args:
    * `idx` (`int`): grouped channel index

    * `group` (`Optional[str]`, optional): group to search in. Defaults to
      `None` for currently selected group.

    ## Returns:
    * `int`: global index
    """
    fl = getState()
    # If it's None
    if group is None:
        group = fl.channels.selected_group
    # If we're viewing the "all" group (...), no change is required
    if group is Ellipsis:
        return idx
    # Now group is guaranteed to be a str, regardless of what mypy thinks
    return getChannelsInGroup(group)[idx]


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
