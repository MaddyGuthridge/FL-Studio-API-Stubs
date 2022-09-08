
from dataclasses import dataclass
from .channels import ChannelsModel, ChannelPlug, default_channels
from .device import DeviceModel, default_device
from .ui import UiModel, default_ui
from .general import GeneralModel, default_general
from .mixer import MixerModel, MixerPlug, default_mixer
from .plugin import PlugInfo, PluginParam
from .transport import TransportModel, default_transport
from .pattern import PatternListModel, PatternModel, default_pattern_list

__all__ = [
    'ChannelsModel',
    'ChannelPlug',
    'DeviceModel',
    'UiModel',
    'GeneralModel',
    'PlugInfo',
    'PluginParam',
    'TransportModel',
    'MixerModel',
    'MixerPlug',
    'PatternModel',
    'PatternListModel',
]


@dataclass
class Model:
    """
    Overall model of FL Studio

    * `channels`

    * `device`

    * `general`

    * `transport`

    * `ui`
    """
    channels: ChannelsModel
    device: DeviceModel
    general: GeneralModel
    mixer: MixerModel
    transport: TransportModel
    ui: UiModel
    patterns: PatternListModel


def default_model():
    return Model(
        channels=default_channels(),
        device=default_device(),
        general=default_general(),
        mixer=default_mixer(),
        transport=default_transport(),
        ui=default_ui(),
        patterns=default_pattern_list(),
    )
