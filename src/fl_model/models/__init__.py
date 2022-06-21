
from dataclasses import dataclass
from .channels import ChannelsModel, default_channels
from .device import DeviceModel, default_device
from .ui import UiModel, default_ui
from .general import GeneralModel, default_general
from .transport import TransportModel, default_transport


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
    transport: TransportModel = default_transport
    ui: UiModel = default_ui


default_model = Model()
