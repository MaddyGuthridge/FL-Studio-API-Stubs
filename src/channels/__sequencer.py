"""
channels > sequencer

Function definitions for interacting with the step sequencer
"""
from fl_model.patterns import getPatternReference
from .__helpers import checkGroupIndex


def getGridBit(index: int, position: int) -> bool:
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


def getGridBitWithLoop(index: int, position: int) -> bool:
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


def setGridBit(index: int, position: int, value: bool) -> None:
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


def getStepParam(step: int, param: int, offset: int, startPos: int,
                 padsStride: int = 16) -> int:
    """Get step parameter for `step`.

    ## HELP WANTED:
    * What does this do?

    ## Args:
     * `step` (`int`): ?

     * `param` (`int`): ?? at least there's the [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#stepParams)
       (actually, tbh the docs on this looks kinda dodgy for some values)

     * `offset` (`int`): ???

     * `startPos` (`int`): ????

     * `padsStride` (`int`, optional): ?????. Defaults to 16.

    ## Returns:
     * `int`: ??????

    Included since API version 1
    """
    return 0


def getCurrentStepParam(index: int, step: int, param: int) -> int:
    """Get current step parameter for channel at `index` and for step at `step`.

    ## HELP WANTED:
    * What does this do?

    ## NOTE:
    * Official documentation says this returns None, but it actually seems to
      return an int.

    ## Args:
     * `index` (`int`): channel index

     * `step` (`int`): ???

     * `param` (`int`): step parameter (refer to [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#stepParams)
       although it looks kinda dodgy for some values)

    Included since API version 1
    """
    checkGroupIndex(index)
    return 0


def setStepParameterByIndex(*args) -> None:
    """
    ???

    ## WARNING:
    * This function has no official documentation

    Included since API Version 20?
    """


def updateGraphEditor() -> None:
    """
    ???

    ## WARNING:
    * This function has no official documentation

    Included since API Version 20?
    """
