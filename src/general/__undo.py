"""
general > __undo

Functions for managing undo and redo
"""


def saveUndo(undoName: str, flags: int, update: int = 1) -> None:
    """Save an undo point into FL Studio's history.

    ## Args:
     * `undoName` (`str`): a descriptive name for the undo point

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

          * `UF_Reset` (`65536`): Reset undo history

     * `update` (`int`, optional): ???. Defaults to 1.

    Included since API version 1
    """


def undo() -> int:
    """Perform an undo toggle, much like pressing Ctrl+Z. If the position in the
    undo history is at the most recent, it will undo, otherwise, it will redo.

    ## Returns:
     * `int`: ???

    Included since API version 1
    """
    return 0


def undoUp() -> int:
    """Move up in the undo history. This is much like undo in most programs

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def undoDown() -> int:
    """Move down in the undo history. This is much like redo in most programs

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def undoUpDown(value: int) -> int:
    """Move in the undo history by delta `value`

    ## Args:
     * `value` (`int`): amount to undo or redo (positive is redo, negative is
        undo)

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def restoreUndo() -> int:
    """???

    This seems to behave in the same way as `undo()`.

    ## HELP WANTED:
    * What does this do?

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def restoreUndoLevel(level: int) -> int:
    """???

    This seems to behave in the same way as `undo()`.

    ## HELP WANTED:
    * What does this do? What is the parameter for?

    ## Args:
     * `level` (`int`): ???

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def getUndoLevelHint() -> str:
    """Returns a fraction-like string that shows the position in the undo
    history as well as the total length of it.

    ## Returns:
     * `str`: fraction-like string:
          * numerator: position in history (`1` is most recent)

          * denominator: number of elements in history

    Included since API version 1
    """
    return ""


def getUndoHistoryPos() -> int:
    """Returns the length of the undo history

    ## HELP WANTED:
    * This seems to behave the same as `getUndoHistoryCount()`. What's the
      difference?

    ## Returns:
     * `int`: number of elements in undo history

    Included since API version 1
    """
    return 0


def getUndoHistoryCount() -> int:
    """Returns the length of the undo history

    ## Returns:
     * `int`: number of elements in undo history

    Included since API version 1
    """
    return 0


def getUndoHistoryLast() -> int:
    """Returns the current position in the undo history. The most recent
    position is `0`, with earlier points in the history having higher indexes.

    ## Returns:
     * `int`: position in undo history

    Included since API version 1
    """
    return 0


def setUndoHistoryPos(index: int) -> None:
    """Removes recent elements from the undo history, leaving only the first
    `index` elements

    ## Args:
     * `index` (`int`): number of elements to leave at the start of the history

    Included since API version 1
    """


def setUndoHistoryCount(value: int) -> None:
    """Removes old elements from the undo history, leaving only the last
    `index` elements

    ## Args:
     * `value` (`int`): number of elements to leave at the end of the history

    Included since API version 1
    """


def setUndoHistoryLast(index: int) -> None:
    """Sets the position in the undo history, where `index = 0` is the most
    recent element and earlier points have higher indexes.

    ## Args:
     * `index` (`int`): new position in undo history

    Included since API version 1
    """