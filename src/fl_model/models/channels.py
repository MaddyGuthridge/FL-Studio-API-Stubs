
from dataclasses import dataclass
from .plugin import PlugInfo


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
    plug: PlugInfo
    name: str
    grid_bits: GridBits
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
    plugins: list[ChannelPlug]
    selections: list[int]


default_channels = ChannelsModel(
    selections=[0],
    plugins=[ChannelPlug(
        PlugInfo(is_valid=False, plug_name='Sampler'),
        name='Sampler',
        grid_bits=GridBits()
    )]
)
