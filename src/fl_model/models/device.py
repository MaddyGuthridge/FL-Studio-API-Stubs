
from dataclasses import dataclass


@dataclass
class DeviceModel:
    """
    Contains info on the device

    * `assigned`: whether the device is assigned

    * `port`: the device's port

    * `name`: the name of the device

    * `dispatch_targets`: list of port numbers of device numbers that we can
      dispatch to
    """
    assigned: bool
    port: int
    name: str
    dispatch_targets: list[int]


default_device = DeviceModel(
    assigned=True,
    port=0,
    name="Device",
    dispatch_targets=[]
)
