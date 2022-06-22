
from dataclasses import dataclass
from .channels import ChannelsModel, ChannelPlug, default_channels
from .device import DeviceModel, default_device
from .ui import UiModel, default_ui
from .general import GeneralModel, default_general
from .mixer import MixerModel, MixerPlug, default_mixer
from .plugin import PlugInfo, PluginParam
from .transport import TransportModel, default_transport

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
    channels: ChannelsModel = default_channels
    device: DeviceModel = default_device
    general: GeneralModel = default_general
    mixer: MixerModel = default_mixer
    transport: TransportModel = default_transport
    ui: UiModel = default_ui


default_model = Model()
