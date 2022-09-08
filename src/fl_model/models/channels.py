
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Union
from .plugin import PlugInfo
from .. import consts


class ChannelType(Enum):
    """
    Represents the type of a channel

    * `SAMPLER`

    * `HYBRID`: sampler fed by generator

    * `GENERATOR`

    * `LAYER`

    * `AUTOMATION`: automation clip
    """
    SAMPLER = 0
    HYBRID = 1
    GENERATOR = 2
    LAYER = 3
    AUTOMATION = 4


@dataclass
class ChannelPlug:
    """
    Represents a plugin on the channel rack

    * `plug`: plugin if applicable

    * `name`: channel name

    * `ch_type`: type of channel

    * `grid_bits`: grid bits for this channel (will move to patterns module)

    * `target`: target mixer track

    * `group`: group that the channel belongs to

    * `selected`: whether the channel is selected

    * `color`

    * `volume`

    * `pan`

    * `muted`
    """
    plug: Optional[PlugInfo]
    name: str
    ch_type: ChannelType
    target: int = 0
    group: str = ''
    selected: bool = False
    color: int = consts.DEFAULT_FL_COLOR
    volume: float = consts.DEFAULT_CHANNEL_VOLUME
    pan: float = 0.0
    muted: bool = False


@dataclass
class ChannelsModel:
    """
    Model of generator channels

    * `channel_list`: list of channels

    * `selected_group`: name of currently selected group (`''` if viewing
      unsorted, `None` if viewing all)
    """
    channel_list: list[ChannelPlug]
    selected_group: Union[str, 'ellipsis']  # noqa: F821


def default_channels():
    return ChannelsModel(
        channel_list=[ChannelPlug(
            plug=None,
            name='Sampler',
            group='',
            ch_type=ChannelType.SAMPLER,
        )],
        selected_group=...,
    )
