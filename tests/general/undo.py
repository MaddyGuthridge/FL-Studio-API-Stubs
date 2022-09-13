"""
tests > general > undo

Tests to ensure that undo behaves correctly
"""
import general


def makeUndoHistory(amount: int):
    for _ in range(amount):
        general.saveUndo('a', 0)


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
    Can we undo things?
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
    reach the most recent item?
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
    general.saveUndo('another item', 0)
    assert general.getUndoHistoryLast() == 3
