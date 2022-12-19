
from dataclasses import dataclass


@dataclass
class PositionModel:
    bar: int = 0
    step: int = 0
    tick: int = 0
    time: float = 0.0


@dataclass
class MarkerModel:
    name: str
    position: PositionModel


@dataclass
class TransportModel:
    """
    General info about FL Studio
    """
    playing: bool
    recording: bool
    position: PositionModel
    length: PositionModel
    markers: list[MarkerModel]


def default_transport():
    return TransportModel(
        playing=False,
        recording=False,
        position=PositionModel(),
        length=PositionModel(),
        markers=[]
    )
