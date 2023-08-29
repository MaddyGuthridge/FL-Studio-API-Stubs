"""
Mixer > Properties

Properties of the mixer and other aspects of FL Studio as a whole
"""
from typing import Optional
import midi
from fl_model.decorators import since


def getTrackInfo(mode: int, /) -> int:
    """Returns the index of a special mixer track depending on `mode`.

    This function can serve to help potentially future-proof scripts by
    ensuring that they continue to use the correct indexes for mixer tracks

    ## Args:
     * `mode` (`int`): Determined the type of information provided:
          * `TN_Master` (`0`): Index of master track

          * `TN_FirstIns` (`1`): Index of first insert track

          * `TN_LastIns` (`2`): Index of last insert track

          * `TN_Sel` (`3`): Index of the "current" track (the one with the
            large peak meter docked to the left).

    ## Returns:
     * `int`: requested track index

    Included since API version 1
    """
    return 0


def trackCount() -> int:
    """Returns the number of tracks available on the mixer.
    Tracks range = `0 - (trackCount()-1)`. Includes master and "current track"
    tracks.

    ## Returns:
     * `int`: number of tracks

    Included since API version 1
    """
    return 0


def getSongStepPos() -> int:
    """Returns the current position in the song, measured in steps.

    ## Returns:
     * `int`: song position

    Included since API version 1
    """
    return 0


def getCurrentTempo(asInt: int = 0, /) -> 'int | float':
    """Returns the current tempo of the song

    ## Args:
     * `asInt` (`int`, optional): whether to return the tempo as an `int` (`1`)
       or not (`0`). Defaults to `0`.

    ## Returns:
     * `int` or `float`: Current tempo

    Included since API version 1
    """
    return 0


def getRecPPS() -> int:
    """Returns the recording PPS

    ## HELP WANTED:
    * What is PPS? I can only get this to return 24. Perhaps this is the bit
      depth of the incoming audio?

    ## Returns:
     * `int`: recording PPS

    Included since API version 1
    """
    return 0


def getSongTickPos(mode: int = midi.ST_Int, /) -> 'int | float':
    """Returns the current position in the song, measured in ticks.

    ## Returns:
     * `int` or `float`: song position in ticks

    Included since API version 1
    """
    return 0


@since(9)
def getLastPeakVol(section: int, /) -> float:
    """Returns last peak volume.

    ## Args:
     * `section` (`int`): audio channel
          * `0`: left channel

          * `1`: right channel

    ## Returns:
     * `float`: last peak volume (`0.0` for silence, `1.0` for 0 dB, `>1.0` for
       clipping)

    Included since API version 9
    """
    return 0.0


@since(25)
def focusEditor(index: int, plugIndex: int, /):
    """
    Focus the editor the effect plugin at the given location

    ## Args:
    * `index` (`int`): track index of plugin

    * `plugIndex` (`int`): mixer slot index of plugin

    Included since API Version 25
    """


@since(25)
def getActiveEffectIndex() -> Optional[tuple[int, int]]:
    """
    Returns the index of the active effects plugin, or None if there isn't one.

    ## Returns:
    * `tuple[int, int]`: (index, plugIndex), or None

    Included since API Version 25
    """
    return None
