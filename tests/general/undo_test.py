"""
tests > general > undo

Tests to ensure that undo behaves correctly
"""
import general


# helper for checking how FL actually behaves
def do(): print(f"{general.getUndoHistoryCount()=}, {general.getUndoHistoryPos()=}, {general.getUndoHistoryLast()=}")  # noqa: E704


def makeUndoHistory(amount: int):
    for _ in range(amount):
        general.saveUndo('a', 1)


def test_default_undo_len():
    """
    By default, the number of items in the undo history is 1
    """
    assert general.getUndoHistoryPos() == 1


def test_default_undo_pos():
    """
    By default, we're on the most recent item
    """
    assert general.getUndoHistoryLast() == 0


def test_add_undo_item():
    """
    Can we add an item to the undo history?
    """
    makeUndoHistory(1)
    assert general.getUndoHistoryPos() == 2


def test_add_undo_item_keeps_undo_position():
    """
    When we add an undo history item, do we stay pointed at the most recent
    one?
    """
    makeUndoHistory(1)
    assert general.getUndoHistoryLast() == 0


def test_undo():
    """
    Can we undo things?
    """
    makeUndoHistory(1)
    general.undo()
    assert general.getUndoHistoryLast() == 1


def test_undo_redo():
    """
    Can we redo things using the undo toggle?
    """
    makeUndoHistory(1)
    general.undo()
    general.undo()
    assert general.getUndoHistoryLast() == 0


def test_redo():
    """
    Can we redo things using the undo down function?
    """
    makeUndoHistory(1)
    general.undo()
    general.undoDown()
    assert general.getUndoHistoryLast() == 0


def test_undo_up():
    """
    Can we undo things using the undo up function?
    """
    makeUndoHistory(1)
    general.undoUp()
    assert general.getUndoHistoryLast() == 1


def test_undo_multi():
    """
    Can we undo multiple things using the undo up function?
    """
    makeUndoHistory(2)
    general.undoUp()
    general.undoUp()
    assert general.getUndoHistoryLast() == 2


def test_undo_toggle_multi():
    """
    If we undo multiple things, does the undo toggle keep redoing until we
    reach the most recent item, and then will it undo?
    """
    makeUndoHistory(3)
    general.undoUp()
    general.undoUp()
    general.undoUp()
    assert general.getUndoHistoryLast() == 3
    general.undo()
    general.undo()
    general.undo()
    assert general.getUndoHistoryLast() == 0
    general.undo()
    assert general.getUndoHistoryLast() == 1


def test_add_undo_removes_future_history():
    """
    If we add an entry in the undo history, does it remove all things we've
    undone previously?
    """
    makeUndoHistory(3)
    general.undoUp()
    general.undoUp()
    general.saveUndo('another item', 1)
    assert general.getUndoHistoryCount() == 3


def test_undo_nothing_there():
    """
    Does nothing happen when we undo if there is nothing to undo
    """
    general.undo()
    assert general.getUndoHistoryLast() == 0


def test_undo_up_nothing_there():
    """
    Does nothing happen when we undo up if there's nothing to undo?
    """
    makeUndoHistory(1)
    general.undoUp()
    assert general.getUndoHistoryLast() == 1
    # End of history
    general.undoUp()
    assert general.getUndoHistoryLast() == 1


def test_undo_down_nothing_there():
    """
    Does nothing happen when we undo down if there's nothing to redo?
    """
    general.undoDown()
    assert general.getUndoHistoryLast() == 0


def test_undo_up_down():
    """
    Can we use undoUpDown to jump around in the undo history?
    """
    makeUndoHistory(3)
    general.undoUpDown(-2)
    assert general.getUndoHistoryLast() == 2


def test_undo_up_down_bad_indexes():
    """
    When we use undoUpDown to jump past the end or before the start of the
    """
    makeUndoHistory(1)
    # Past the end
    general.undoUpDown(-2)
    assert general.getUndoHistoryLast() == 1
    # Before the start
    general.undoUpDown(2)
    assert general.getUndoHistoryLast() == 0


def test_restore_undo():
    """
    Restore undo should be the same as undo
    """
    makeUndoHistory(1)
    general.restoreUndo()
    assert general.getUndoHistoryLast() == 1


def test_restore_undo_level():
    """
    Restore undo level should be the same as undo
    """
    makeUndoHistory(1)
    general.restoreUndoLevel(0)
    assert general.getUndoHistoryLast() == 1


def test_undo_level_hint_default():
    """
    Are we given a correct string for getUndoLevelHint?
    """
    assert general.getUndoLevelHint() == "1/1"


def test_undo_level_hint_more_history():
    """
    Are we given a correct string for getUndoLevelHint when we add to the undo
    history?
    """
    makeUndoHistory(4)
    assert general.getUndoLevelHint() == "1/5"


def test_undo_level_hint_has_undone():
    """
    Are we given a correct string for getUndoLevelHint when we undo something?
    """
    makeUndoHistory(2)
    general.undoUp()
    assert general.getUndoLevelHint() == "2/3"
    general.undoUp()
    assert general.getUndoLevelHint() == "3/3"


def test_get_undo_history_count():
    """
    Check that getUndoHistoryCount returns the number of items in the undo
    history.
    """
    makeUndoHistory(2)
    assert general.getUndoHistoryCount() == 3


def test_get_undo_history_last():
    """
    Check that getUndoHistoryLast returns the current place in the undo history
    """
    assert general.getUndoHistoryLast() == 0
    makeUndoHistory(2)
    general.undoUpDown(-2)
    assert general.getUndoHistoryLast() == 2


def test_set_undo_history_pos():
    """
    Can we use setUndoHistoryPos() to remove recent elements from the undo
    history

    1 2 3  => 2 3
      ^         ^
    """
    makeUndoHistory(2)
    general.undo()
    general.setUndoHistoryPos(2)
    assert general.getUndoHistoryPos() == 2
    # We're still second in the queue
    assert general.getUndoHistoryLast() == 1


def test_set_undo_history_pos_can_delete_last_reset():
    """
    Make sure that setUndoHistoryPos() can delete the final element in the
    undo history
    """
    general.setUndoHistoryPos(0)
    assert general.getUndoHistoryPos() == 0


def test_set_undo_history_pos_doesnt_affect_count():
    """
    setUndoHistoryPos should not affect the length of the history from
    getUndoHistoryCount
    """
    makeUndoHistory(2)
    general.setUndoHistoryPos(2)
    assert general.getUndoHistoryCount() == 3


def test_set_undo_history_count():
    """
    Can we use setUndoHistoryCount() to remove old elements from the undo
    history?

    1 2 3  => 1 2
      ^         ^
    """
    makeUndoHistory(2)
    general.undo()
    general.setUndoHistoryCount(2)
    assert general.getUndoHistoryCount() == 2
    # We're still second in the queue
    assert general.getUndoHistoryLast() == 1


def test_set_undo_history_count_can_delete_last_reset():
    """
    Make sure that setUndoHistoryPos() can delete the final element in the
    undo history
    """
    general.setUndoHistoryCount(0)
    assert general.getUndoHistoryCount() == 0


def test_set_undo_history_count_doesnt_affect_pos():
    """
    setUndoHistoryPos should not affect the length of the history from
    getUndoHistoryCount
    """
    makeUndoHistory(2)
    general.setUndoHistoryCount(2)
    assert general.getUndoHistoryPos() == 3
