"""
general > __undo

Functions for managing undo and redo
"""
from fl_model.decorators import deprecate
from fl_model.models.general import UndoItem
from fl_model import getState


def saveUndo(undoName: str, flags: int, update: bool = True, /) -> None:
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
    undo = getState().general.undo
    # Slice out any later elements
    if undo.position != 0:
        undo.items = undo.items[undo.position:]
        undo.pos_len = undo.count_len = len(undo.items)
    undo.items.insert(0, UndoItem(undoName, flags))
    undo.count_len += 1
    undo.pos_len += 1


def undo() -> int:
    """Perform an undo toggle, much like pressing Ctrl+Z. If the position in the
    undo history is at the most recent, it will undo, otherwise, it will redo.

    ## Returns:
     * `int`: ???

    Included since API version 1
    """
    if getState().general.undo.position == 0:
        undoUp()
    else:
        undoDown()
    return 0


def undoUp() -> int:
    """
    Move up in the undo history. This is much like undo in most programs.

    Note that in FL Studio 21, the ordering of the undo history was changed,
    so visually this actually moves down.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    undoUpDown(-1)
    return 0


def undoDown() -> int:
    """
    Move down in the undo history. This is much like redo in most programs.

    Note that in FL Studio 21, the ordering of the undo history was changed,
    so visually this actually moves up.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    undoUpDown(1)
    return 0


def undoUpDown(value: int, /) -> int:
    """Move in the undo history by delta `value`

    ## Args:
     * `value` (`int`): amount to undo or redo (positive is redo, negative is
        undo)

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    undo = getState().general.undo
    undo.position = max(0, min(len(undo.items) - 1, undo.position - value))
    return 0


@deprecate(1)
def restoreUndo() -> int:
    """
    Undo-redo toggle. This behaves in the same way as `undo()`.

    ## Returns:
     * `int`: ?

    Included since API version 1

    Deprecated since API version 1
    """
    return undo()


@deprecate(1)
def restoreUndoLevel(level: int, /) -> int:
    """
    Undo-redo toggle. This behaves in the same way as `undo()`.

    ## Args:
     * `level` (`int`): this parameter is ignored.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return undo()


def getUndoLevelHint() -> str:
    """Returns a fraction-like string that shows the position in the undo
    history as well as the total length of it.

    ## Returns:
     * `str`: fraction-like string:
          * numerator: position in history (`1` is most recent)

          * denominator: number of elements in history

    Included since API version 1
    """
    return f"{getUndoHistoryLast() + 1}/{getUndoHistoryCount()}"


def getUndoHistoryPos() -> int:
    """Returns the length of the undo history

    ## HELP WANTED:
    * This seems to behave the same as `getUndoHistoryCount()`. What's the
      difference?

    ## Returns:
     * `int`: number of elements in undo history

    Included since API version 1
    """
    return getState().general.undo.pos_len


def getUndoHistoryCount() -> int:
    """
    Returns the total number of items that have ever been added to the undo
    history including items that have been trimmed by `setUndoHistoryPos()`,
    but not items that have been trimmed by `setUndoHistoryCount()`.

    ## Returns:
     * `int`: number of elements in undo history

    Included since API version 1
    """
    return getState().general.undo.count_len


def getUndoHistoryLast() -> int:
    """Returns the current position in the undo history. The most recent
    position is `0`, with earlier points in the history having higher indexes.

    ## Returns:
     * `int`: position in undo history

    Included since API version 1
    """
    return getState().general.undo.position


def setUndoHistoryPos(index: int, /) -> None:
    """
    Removes recent elements from the undo history, leaving only the earliest
    `n = index` elements in the history.

    This will affect the length of the undo history as per
    `getUndoHistoryPos()`, but not affect it as per `getUndoHistoryCount()`

    This will not actually undo the actions, just remove them from the undo
    history. It could be useful for grouping multiple undo items into one.

    ## Known issues:
    * The browser will not refresh when this action

    ## Args:
     * `index` (`int`): number of elements to leave at the start of the history

    Included since API version 1
    """
    undo = getState().general.undo
    index = min(max(index, 0), len(undo.items))
    undo.pos_len = index
    undo.items = undo.items[-index:]


def setUndoHistoryCount(value: int, /) -> None:
    """
    Removes old elements from the undo history, leaving only the latest
    `n = index` elements.

    This will affect the length of the undo history as per
    `getUndoHistoryCount()`, but not affect it as per `getUndoHistoryPos()`

    ## Known issues:
    * The browser will not refresh when this action

    ## Args:
     * `value` (`int`): number of elements to leave at the end of the history

    Included since API version 1
    """
    undo = getState().general.undo
    value = min(max(value, 0), len(undo.items))
    undo.count_len = value
    undo.items = undo.items[:value]


def setUndoHistoryLast(index: int, /) -> None:
    """Sets the position in the undo history, where `index = 0` is the most
    recent element and earlier points have higher indexes.

    ## Args:
     * `index` (`int`): new position in undo history

    Included since API version 1
    """
    undo = getState().general.undo
    index = min(max(index, 0), len(undo.items))
    undo.position = index
