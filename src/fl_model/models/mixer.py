
from dataclasses import dataclass
from .plugin import PlugInfo


@dataclass
class MixerPlug:
    """
    Mixer plugin info

    * `plug`: plugin

    * `level`: send level
    """
    plug: PlugInfo
    level: float


@dataclass
class SendInfo:
    """
    Info on sends for a mixer track

    * `to` the index of the track that we're targeting

    * `amount` the amount that is being sent (between 0 and 1)
    """
    to: int
    amount: float


@dataclass
class MixerTrack:
    """
    Info on a mixer track

    * `selected`: whether the track is selected

    * `plugins`: the list of plugins on the track

    * `volume`: volume fader

    * `pan`: pan dial

    * `sends`: list of sends

    * `muted`: whether the track is muted
    """
    selected: bool
    plugins: list[PlugInfo]
    volume: float
    pan: float
    sends: list[SendInfo]
    muted: bool


@dataclass
class MixerModel:
    """
    Model of mixer

    * `tracks`: list of track info
    """
    tracks: list[MixerTrack]


default_mixer = MixerModel(
    tracks=[
        MixerTrack(  # Master
            selected=True,
            plugins=[],
            volume=1.0,
            pan=0.0,
            sends=[],
            muted=False,
        )
    ] + [
        MixerTrack(  # Main tracks
            selected=False,
            plugins=[],
            volume=1.0,
            pan=0.0,
            sends=[SendInfo(to=0, amount=1.0)],
            muted=False,
        )
    ] * 125
)
