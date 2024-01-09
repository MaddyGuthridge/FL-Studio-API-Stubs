"""
Playlist > Performance

Functions for interacting with performance mode
"""

from fl_model.decorators import since
import midi


def getDisplayZone() -> int:
    """
    Returns the current display zone in the playlist or zero if none.

    ## HELP WANTED:
    * Explanation for what a display zone is.

    ## Returns:
    * `int`: current display zone

    Included since API version 1
    """
    return 0


def lockDisplayZone(index: int, value: int) -> None:
    """
    Lock display zone at `index`.

    ## HELP WANTED:
    * Explanation for what a display zone is.
    * Explanation for parameters.

    ## Args:
    * `index` (`int`): ???

    * `value` (`int`): ???

    Included since API version 1
    """


def liveDisplayZone(
    left: int,
    top: int,
    right: int,
    bottom: int,
    duration: int = 0,
) -> None:
    """
    Set the display zone in the playlist to the specified co-ordinates. Use the
    optional `duration` parameter to make display zone temporary.

    ## HELP WANTED:
    * Explanation for what a display zone is.
    * Explanation for parameters.

    ## Args:
     * `left` (`int`): ???

     * `top` (`int`): ???

     * `right` (`int`): ???

     * `bottom` (`int`): ???

     * `duration` (`int`, optional): ???. Defaults to `0`.

    Included since API version 1
    """


def getLiveLoopMode(index: int) -> int:
    """
    Get live loop mode

    ## HELP WANTED:
    * Explanation for parameters.

    ## Args:
    * `index` (`int`): track index???

    ## Returns:
    * `int`: live loop mode:
          * `0` (`LiveLoop_Stay`): Stay

          * `1` (`LiveLoop_OneShot`): One shot

          * `2` (`LiveLoop_MarchWrap`): March and wrap

          * `3` (`LiveLoop_MarchStay`): March and stay

          * `4` (`LiveLoop_MarchStop`): March and stop

          * `5` (`LiveLoop_Random`): Random

          * `6` (`LiveLoop_ExRandom`): Random, avoiding previous clip?

    Included since API version 1
    """
    return 0


def getLiveTriggerMode(index: int) -> int:
    """
    Get live trigger mode

    ## HELP WANTED:
    * What does this do?

    ## Args:
    * `index` (`int`): track index???

    ## Returns:
    * `int`: live trigger mode:
          * `0` (`LiveTrig_Retrigger`): Retrigger

          * `1` (`LiveTrig_Hold`): Hold and stop

          * `2` (`LiveTrig_HMotion`): Hold and motion

          * `3` (`LiveTrig_Latch`): Latch

    Included since API version 1
    """
    return 0


def getLivePosSnap(index: int) -> int:
    """
    Get live position snap

    ## HELP WANTED:
    * What does this do?

    ## Args:
    * `index` (`int`): track index???

    ## Returns:
    * `int`: live position snap:
          * `0` (`LiveSnap_Off`): No snap

          * `1` (`LiveSnap_Fourth`): 1/4 beat

          * `2` (`LiveSnap_Half`): 1/2 beat

          * `3` (`LiveSnap_One`): 1 beat

          * `4` (`LiveSnap_Two`): 2 beats

          * `5` (`LiveSnap_Four`): 4 beats

          * `6` (`LiveSnap_Auto`): Auto

    Included since API version 1
    """
    return 0


def getLiveTrigSnap(index: int) -> int:
    """
    Get live trigger snap

    ## HELP WANTED:
    * What does this do?

    ## Args:
    * `index` (`int`): track index???

    ## Returns:
    * `int`: live position snap:
          * `0` (`LiveSnap_Off`): No snap

          * `1` (`LiveSnap_Fourth`): 1/4 beat

          * `2` (`LiveSnap_Half`): 1/2 beat

          * `3` (`LiveSnap_One`): 1 beat

          * `4` (`LiveSnap_Two`): 2 beats

          * `5` (`LiveSnap_Four`): 4 beats

          * `6` (`LiveSnap_Auto`): Auto

    Included since API version 1
    """
    return 0


def getLiveStatus(index: int, mode: int = midi.LB_Status_Default) -> int:
    """
    Returns the live status for track at `index`

    ## HELP WANTED:
    * What does this do?

    ## Args:
     * `index` (`int`): track index

     * `mode` (`int`, optional): live status mode. Defaults to 'LB_Status_Default'.

    ## Returns:
     * `int`: live status of track:
            Refer to [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#getLiveStatusMode)

    Included since API version 1
    """
    return 0


def getLiveBlockStatus(
    index: int,
    blockNum: int,
    mode: int = midi.LB_Status_Default,
) -> int:
    """
    Returns the live block status for track at `index` and for block `blockNum`

    ## HELP WANTED:
    * What does this do?

    ## Args:
    * `index` (`int`): track index

    * `blockNum` (`int`): block number

    * `mode` (`int`, optional): live status mode. Defaults to 'LB_Status_Default'.

    ## Returns:
    * `int`: live status of track:
       Refer to [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#getLiveStatusMode).

    Included since API version 1
    """
    return 0


def getLiveBlockColor(index: int, blockNum: int) -> int:
    """
    Returns the color of block on track `index` at position `blockNum`

    ## HELP WANTED:
    * What does this do?

    Note that colors can be split into or built from components using the
    functions provided in the `utils` module

    * `ColorToRGB()`

    * `RGBToColor()`

    ## Args:
    * `index` (`int`): track index

    * `blockNum` (`int`): block number

    ## Returns:
    * `int`: block color (`0x--BBGGRR`)

    Included since API version 1
    """
    return 0


def triggerLiveClip(
    index: int,
    subNum: int,
    flags: int,
    velocity: int = -1,
) -> None:
    """
    Triggers live clip for track at `index` and for block `subNum`

    ## HELP WANTED:
    * What does this do?

    ## Args:
    * `index` (`int`): track index

    * `subNum` (`int`): block number (usually `blockNum`)

    * `flags` (`int`): live clip trigger flags. Refer to
      [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#triggerLiveClipFlags).

    * `velocity` (`int`, optional): velocity for triggering clip. Defaults to `-1`.

    Included since API version 1
    """


def refreshLiveClip(index: int, value: int) -> None:
    """
    Triggers live clip for track at `index` and for block `subNum`

    ## HELP WANTED:
    * What does this do?

    ## Args:
    * `index` (`int`): track index

    * `value` (`int`): ???

    Included since API version 1
    """


def incLivePosSnap(index: int, value: int) -> None:
    """
    Increase live position snap for track at `index`

    ## HELP WANTED:
    * What does this do?

    ## Args:
    * `index` (`int`): track index

    * `value` (`int`): ???

    Included since API version 1
    """


def incLiveTrigSnap(index: int, value: int) -> None:
    """
    Increase live trigger snap for track at `index`

    ## HELP WANTED:
    * What does this do?

    ## Args:
    * `index` (`int`): track index

    * `value` (`int`): ???

    Included since API version 1
    """


def incLiveLoopMode(index: int, value: int) -> None:
    """
    Increase live loop mode for track at `index`

    ## HELP WANTED:
    * What does this do?

    ## Args:
    * `index` (`int`): track index

    * `value` (`int`): ???

    Included since API version 1
    """


def incLiveTrigMode(index: int, value: int) -> None:
    """
    Increase live trigger mode for track at `index`

    ## HELP WANTED:
    * What does this do?

    ## Args:
    * `index` (`int`): track index

    * `value` (`int`): ???

    Included since API version 1
    """


def getVisTimeBar() -> int:
    """
    Returns the time bar

    ## HELP WANTED:
    * Explanation. I could only get this function to return `0`.

    ## Returns:
    * `int`: time bar

    Included since API version 1
    """
    return 0


def getVisTimeTick() -> int:
    """
    Returns the time tick

    ## HELP WANTED:
    * Explanation. I could only get this function to return `0`.

    ## Returns:
    * `int`: time tick

    Included since API version 1
    """
    return 0


def getVisTimeStep() -> int:
    """
    Returns the time bar

    ## HELP WANTED:
    * Explanation. I could only get this function to return `0`.

    ## Returns:
    * `int`: time step

    Included since API version 1
    """
    return 0


@since(21)
def getPerformanceModeState() -> bool:
    """
    Returns whether FL Studio's performance mode is enabled

    ## Returns:
    * `bool`: whether performance mode is enabled

    Included since API Version 21
    """
    return False
