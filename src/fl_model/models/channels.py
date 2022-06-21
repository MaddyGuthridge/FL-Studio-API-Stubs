
from dataclasses import dataclass
from .plugin import PlugInfo, SAMPLER


@dataclass
class ChannelsModel:
    """
    Model of generator channels

    * `selections`: list of selected channels

    * `plugins`: info for each plugin
    """
    plugins: list[PlugInfo]
    selections: list[int] = [0]


default_channels = ChannelsModel(
    selections=[0],
    plugins=[SAMPLER]
)
