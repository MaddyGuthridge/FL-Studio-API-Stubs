"""Arrangement Module (FL Studio built-in)

Allows you to control and interact with FL Studio Arrangements, including
markers, selections and timestamps.
"""


def jumpToMarker(index: int, select: bool, /) -> None:
    """
    Jumps to the marker at the given delta index.

    For example, to jump to the previous marker, use an index of `-1`.

    ## Args:
    * index (`int`): relative marker index

    * select (`bool`): whether to select the marker

    Included since API version 1
    """


def getMarkerName(index: int, /) -> str:
    """Returns the name of the marker at `index`

    Note that this uses an absolute index, not a relative index.

    ## Args:
    * index (`int`): marker index

    ## Returns:
    * `str`: name of the marker

    Included since API version 1
    """
    return ""


def addAutoTimeMarker(time: int, name: str, /) -> None:
    """Add an automatic time marker at `time`.

    ## Args:
    * `time` (`int`): time (TODO: What are the units?)

    * `name` (`str`): name of new marker

    Included since API version 1
    """


def liveSelection(time: int, stop: int, /) -> None:
    """Set a live selection point at `time`.

    Set `stop` to True, to use end point of the selection (instead of start).

    ## HELP WANTED:
    * A better explanation would be good

    ## Args:
    * `time` (`int`): ???

    * `stop` (`int`): ???

    Included since API version 1
    """


def liveSelectionStart() -> int:
    """Returns the start time of the current live selection

    ## Returns:
    * `int`: start of selection time

    Included since API version 1
    """
    return 0


def currentTime(snap: int, /) -> int:
    """Returns the current time in the current arrangement, in terms of ticks.
    Note that by default, most projects have a PPQ of 96. Use
    [`general.getRecPPQ()`][general.getRecPPQ] to get the PPQ of the project.

    ## Args:
    * `snap` (`int`): whether to get time snapped to grid

    ## Returns:
    * `int`: current time

    Included since API version 1
    """
    return 0


def currentTimeHint(
    mode: int,
    time: int,
    setRecPPB: int = 0,
    isLength: int = 0,
    /,
) -> str:
    """Returns a hint string for the given time, formatted as: Bar:Beat?:Tick

    ## Args:
    * `mode` (`int`): pattern mode (`0`) or song mode (`1`)

    * `time` (`int`): time in ticks

    * `setRecPPB` (`int`, optional): ???. Defaults to ?

    * `isLength` (`int`, optional): ???. Defaults to 0

    ## Returns:
    * `str`: current time as string hint

    Included since API version 1
    """
    return ""


def selectionStart() -> int:
    """Returns the returns the start time of the current selection.

    ## Returns:
    * `int`: start time

    Included since API version 1
    """
    return 0


def selectionEnd() -> int:
    """Returns the returns the end time of the current selection.

    ## Returns:
    * `int`: end time

    Included since API version 1
    """
    return 0
