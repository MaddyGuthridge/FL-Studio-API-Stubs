
from dataclasses import dataclass
from fl_model.configuration.target_version import processVersion
from fl_model import config


@dataclass
class UndoItem:
    """
    An entry in the undo history

    * `name` (`str`): a descriptive name for the undo point

    * `flags` (`int`): Any combination of the following flags, combined using
      the logical or (`|`) operator:
          * `UF_None` (`0`): No flags

          * `UF_EE` (`1`): Changes in event editor

          * `UF_PR` (`2`): Changes in piano roll

          * `UF_PL` (`4`): Changes in playlist

          * `UF_KNOB` (`32`): Changes to an automated control

          * `UF_AudioRec` (`256`): Audio recording

          * `UF_AutoClip` (`512`): Automation clip

          * `UF_PRMarker` (`1024`): Piano roll (pattern) marker

          * `UF_PLMarker` (`2048`): Playlist marker

          * `UF_Plugin` (`4096`): Plugin

          * `UF_SSLooping` (`8192`): Step sequencer looping
    """
    name: str
    flags: int


@dataclass
class UndoModel:
    """
    State of undo in FL Studio

    * `items`: list of items

    * `position`: position in undo history

    * `count_len`: length of undo history as per count functions

    * `pos_len` length of undo history as per pos functions
    """
    items: list[UndoItem]
    position: int
    count_len: int
    pos_len: int


@dataclass
class GeneralModel:
    """
    General info about FL Studio

    * `api_version`: version of the FL Studio API

    * `undo`: info on the undo/redo state

    * `ppqn`: timebase of project

    * `beats`: number of beats per bar

    * `metronome`: whether the metronome is enabled

    * `pre_count`: whether pre-count is enabled

    * `changed`: whether the current project needs saving

    * `tick_num`: the number of ticks that FL Studio has run. Used by some
      functions to perform error checking
    """
    api_version: int
    undo: UndoModel
    ppqn: int
    beats: int
    metronome: bool
    pre_count: bool
    changed: bool
    tick_num: int = 0


def default_general():
    return GeneralModel(
        api_version=processVersion(config['targetApiVersion']),
        undo=UndoModel(
            items=[UndoItem("Last reset", 0)],
            position=0,
            count_len=1,
            pos_len=1,
        ),
        ppqn=96,
        beats=4,
        metronome=False,
        pre_count=False,
        changed=False
    )
