
from dataclasses import dataclass
from enum import Enum
from typing import Optional
from .plugin import PlugInfo


class ChannelType(Enum):
    SAMPLER = 0
    HYBRID = 1
    GENERATOR = 2
    LAYER = 3
    AUTOMATION = 4


class GridBits:
    def __init__(self) -> None:
        self.__bits: set[int] = set()

    def __setitem__(self, index: int, value: bool):
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
    plug: Optional[PlugInfo]
    name: str
    ch_type: ChannelType
    grid_bits: GridBits
    target: int = 0
    color: int = 0x5C656A
    volume: float = 0.78125
    pan: float = 0.0


@dataclass
class ChannelsModel:
    """
    Model of generator channels

    * `selections`: list of selected channels

    * `plugins`: info for each plugin
    """
    channel_list: list[ChannelPlug]
    selections: list[int]
    groups: dict[str, set[int]]
    selected_group: str


default_channels = ChannelsModel(
    selections=[0],
    channel_list=[ChannelPlug(
        plug=None,
        name='Sampler',
        ch_type=ChannelType.SAMPLER,
        grid_bits=GridBits()
    )],
    groups={},
    selected_group='',
)
