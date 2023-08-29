"""
channels > sequencer

Function definitions for interacting with the step sequencer
"""
from fl_model.patterns import getPatternReference
from fl_model.channels import checkGroupIndex


def getGridBit(index: int, position: int, /) -> bool:
    """Returns whether the grid bit on channel at `index` in `position` is set.

    ## Args:
     * `index` (`int`): channel index

     * `position` (`int`): index of grid bit (horizontal axis)

    ## Returns:
     * `bool`: whether grid bit is set

    Included since API version 1
    """
    checkGroupIndex(index)
    return getPatternReference().track_contents[index][position]


def getGridBitWithLoop(index: int, position: int, /) -> bool:
    """Get value of grid bit on channel `index` in `position` accounting for
    loops.

    ## NOTE:
    * Official documentations say this returns None, but it doesn't. This
      documentation reflects the actual behavior.

    ## Args:
     * `index` (`int`): channel index`

     * `position` (`int`): position on grid (x axis)

    ## Returns:
     * `bool`: whether grid bit is set

    Included since API version 1
    """
    checkGroupIndex(index)
    return False


def setGridBit(index: int, position: int, value: bool, /) -> None:
    """Sets the value of the grid bit on channel at `index` in `position`.

    ## Args:
     * `index` (`int`): channel index

     * `position` (`int`): index of grid bit (horizontal axis)

     * `value` (`bool`): whether grid bit is set (`True`) or not (`False`)

    Included since API version 1
    """
    checkGroupIndex(index)
    getPatternReference().track_contents[index][position] = value


def isGridBitAssigned(*args) -> bool:
    """
    TODO
    ???
    """
    return False


def getStepParam(
    step: int,
    param: int,
    offset: int,
    startPos: int,
    padsStride: int = 16,
    /,
) -> int:
    """
    Get the values of properties associated with a step in the step sequencer.
    This provides an interface to access the graph editor.

    ## Args:
    * `step` (`int`): step (grid bit index) to get parameter for

    * `param` (`int`): one of the parameter types (see below)

    * `offset` (`int`): ???

    * `startPos` (`int`): ????

    * `padsStride` (`int`, optional): ?????. Defaults to 16.

    ## Returns:
    * `int`: value for step parameter

    ## See also:
    * [`getCurrentStepParam()`][channels.getCurrentStepParam]
    * [`setStepParameterByIndex()`][channels.setStepParameterByIndex]

    ## Step parameter types:
    * `0`: Note pitch (MIDI note number, default 60 for middle C)
    * `1`: Velocity (0 - 127, default 100)
    * `2`: Release velocity (0 - 127, default 64)
    * `3`: Fine pitch (in cents: 0 - 240, with default 120 for no tuning)
    * `4`: Panning (0 - 127, with default 64 for centred)
    * `5`: Mod X (0-127, with default 64 for midpoint)
    * `6`: Mod Y (0-127, with default 64 for midpoint)
    * `7`: Number of ticks to offset the note by (0 - PPQN / 4; , with default
      0 for no shifting)

    Included since API version 1
    """
    return 0


def getCurrentStepParam(index: int, step: int, param: int, /) -> int:
    """Get current step parameter for channel at `index` and for step at `step`.

    ## HELP WANTED:
    * What does this do?

    ## NOTE:
    * Official documentation says this returns None, but it actually seems to
      return an int.

    ## Args:
    * `index` (`int`): channel index

    * `step` (`int`): step (grid bit index) to get parameter for

    * `param` (`int`): step parameter (refer to [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#stepParams)
      although it looks kinda dodgy for some values)

    ## Returns:
    * `int`: value for step parameter

    ## Step parameter types:
    * `0`: Note pitch (MIDI note number, default 60 for middle C)
    * `1`: Velocity (0 - 127, default 100)
    * `2`: Release velocity (0 - 127, default 64)
    * `3`: Fine pitch (in cents: 0 - 240, with default 120 for no tuning)
    * `4`: Panning (0 - 127, with default 64 for centred)
    * `5`: Mod X (0-127, with default 64 for midpoint)
    * `6`: Mod Y (0-127, with default 64 for midpoint)
    * `7`: Number of ticks to offset the note by (0 - PPQN / 4; , with default
      0 for no shifting)

    Included since API version 1
    """
    checkGroupIndex(index)
    return 0


def setStepParameterByIndex(
    index: int,
    patNum: int,
    step: int,
    param: int,
    value: int,
    globalIndex: bool = True,
    /,
) -> None:
    """
    Set the value of a step parameter at the given location.

    ## Args:
    * `index` (`int`): channel index

    * `patNum` (`int`): pattern number to set step parameter on (1-indexed)

    * `step` (`int`): step index

    * `param` (`int`): step parameter to set (see below)

    * `value` (`int`): value to set parameter to

    * `globalIndex` (`bool`, optional): whether to use a global index for the
      channel. Defaults to `True`.

    Included since API Version 1
    """


def updateGraphEditor() -> None:
    """
    ???

    ## WARNING:
    * This function has no official documentation

    Included since API Version 20?
    """
