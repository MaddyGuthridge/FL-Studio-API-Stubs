
from copy import deepcopy
from typing import Optional

from .consts import VST_FINAL_PARAM_NAMES
from .state import getState
from .models import PlugInfo, PluginParam
from .models.channels import (
    ChannelPlug,
    ChannelType,
    GridBits,
    default_channels,
)


def addChannel(
    plug: Optional[PlugInfo],
    name: str,
    ch_type: ChannelType,
    index: int = -1,
    target: int = 0,
    color: int = 0x5C656A,
    volume: float = 0.78125,
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
        GridBits(),
        target,
        color,
        volume,
        pan,
    ))
    # Update groups
    for g in fl.channels.groups.values():
        for i, j in enumerate(g):
            if j >= index:
                g[i] = j + 1


def removeChannel(index: int) -> None:
    """
    Remove a channel from the channel rack

    ## Args:
    * `index` (`int`): index of channel to remove
    """
    fl = getState()
    for g in fl.channels.groups.values():
        for i, j in enumerate(g):
            if j == index:
                g.remove(j)
            elif j > index:
                g[i] = j - 1
    fl.channels.channel_list.pop(index)


def resetChannels() -> None:
    """
    Reset channels to their default state
    """
    fl = getState()
    fl.channels = deepcopy(default_channels)


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
    for i in range(4240):
        if i < len(params):
            param_list.append(PluginParam(params[i]))
        elif 4096 <= i:
            param_list.append(PluginParam(VST_FINAL_PARAM_NAMES[i]))
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
    if name == '':
        raise ValueError("Name can't be empty")
    fl = getState()
    # Get the group we want to modify
    group = fl.channels.groups.get(name, [])

    # Remove each plugin from any groups it is already in
    for p in plugs:
        removeChannelFromAnyGroup(p)
        group.append(p)

    # Store the group back into the dictionary
    group.sort()
    fl.channels.groups[name] = group


def removeChannelFromGroup(idx: int, group: str) -> bool:
    """
    Remove a channel from the group if present. Delete the group if empty.

    ## Args:
    * `idx` (`int`): global index of channel

    * `group` (`str`): group name

    ## Returns:
    * `bool`: whether the channel was removed
    """
    fl = getState()
    try:
        fl.channels.groups[group].remove(idx)
        if not len(fl.channels.groups[group]):
            fl.channels.groups.pop(group)
    except ValueError:
        return False
    return True


def removeChannelFromAnyGroup(idx: int):
    """
    Removes a channel from its group

    ## Args:
    * `plug` (`int`): global index of channel
    """
    fl = getState()
    for g in fl.channels.groups.values():
        if idx in g:
            g.remove(idx)
            # Assumes it's only in one group, which should be the case if the
            # correct functions are used
            return
