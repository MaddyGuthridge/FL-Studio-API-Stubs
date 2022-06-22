
from dataclasses import dataclass
from enum import Enum
from typing import Optional
from .plugin import PlugInfo
from ..exceptions import FlIndexError


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


class GridBits:
    """
    Represents the grid bits for a single channel, allowing the bits to be
    toggled or set for each index.
    """
    def __init__(self) -> None:
        self.__bits: set[int] = set()

    def __setitem__(self, index: int, value: bool):
        if index < 0:
            raise FlIndexError()
        if value:
            self.__bits.add(index)
        else:
            self.__bits.discard(index)

    def __getitem__(self, index: int) -> bool:
        return index in self.__bits

    def toggle(self, index: int):
        self[index] = not self[index]


@dataclass
class ChannelPlug:
    """
    Represents a plugin on the channel rack

    * `plug`: plugin if applicable

    * `name`: channel name

    * `group`: group that the channel belongs to

    * `ch_type`: type of channel

    * `grid_bits`

    * `group`

    * `target`: target mixer track

    * `color`

    * `volume`

    * `pan`
    """
    plug: Optional[PlugInfo]
    name: str
    ch_type: ChannelType
    grid_bits: GridBits
    target: int = 0
    group: str = ''
    selected: bool = False
    color: int = 0x5C656A
    volume: float = 0.78125
    pan: float = 0.0


@dataclass
class ChannelsModel:
    """
    Model of generator channels

    * `selections`: list of selected channels

    * `plugins`: info for each plugin

    * `groups`: dictionary of groups

    * `selected_group`: name of currently selected group
    """
    channel_list: list[ChannelPlug]
    selected_group: str


default_channels = ChannelsModel(
    channel_list=[ChannelPlug(
        plug=None,
        name='Sampler',
        group='',
        ch_type=ChannelType.SAMPLER,
        grid_bits=GridBits()
    )],
    selected_group='',
)
