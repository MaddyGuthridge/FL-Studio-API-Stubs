
from typing import Optional

from .consts import VST_FINAL_PARAM_NAMES
from .state import getState
from .models import PlugInfo, PluginParam
from .models.channels import ChannelPlug, ChannelType, GridBits


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
