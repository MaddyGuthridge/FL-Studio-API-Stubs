
import pytest
from fl_model.exceptions import FlIndexError
from fl_model.patterns import addPattern, removePattern
import patterns


def test_default_pattern_count():
    assert patterns.patternCount() == 1


def test_add_pattern():
    addPattern()
    assert patterns.patternCount() == 2
    removePattern(1)
    assert patterns.patternCount() == 1


@pytest.mark.parametrize(
    ('func', 'params'),
    [
        (patterns.burnLoop, tuple()),
        (patterns.ensureValidNoteRecord, tuple()),
        (patterns.getPatternColor, tuple()),
        (patterns.getPatternLength, tuple()),
        (patterns.getPatternName, tuple()),
        (patterns.selectPattern, tuple()),
        (patterns.setPatternColor, (0,)),
        (patterns.setPatternName, ('Pat',)),
        (patterns.isPatternSelected, tuple()),
        (patterns.jumpToPattern, tuple()),
    ]
)
def test_invalid_indexes(func, params):
    """Anything outside the range 0 <= i <= 999 is invalid"""
    with pytest.raises(FlIndexError):
        func(-1, *params)
    with pytest.raises(FlIndexError):
        func(1000, *params)


@pytest.mark.parametrize(
    ('func', 'params'),
    [
        (patterns.burnLoop, tuple()),
        (patterns.ensureValidNoteRecord, tuple()),
        (patterns.getPatternColor, tuple()),
        (patterns.getPatternLength, tuple()),
        (patterns.getPatternName, tuple()),
        (patterns.selectPattern, tuple()),
        (patterns.setPatternColor, (0,)),
        (patterns.setPatternName, ('Pat',)),
        (patterns.isPatternSelected, tuple()),
        (patterns.jumpToPattern, tuple()),
    ]
)
def test_valid_indexes(func, params):
    """Anything inside the range 0 <= i <= 999 is valid"""
    func(0, *params)
    func(999, *params)


def test_selection_default():
    """By default no pattern is selected"""
    assert not patterns.isPatternSelected(1)


def test_toggle_pattern_selection():
    patterns.selectPattern(1)
    assert patterns.isPatternSelected(1)
    patterns.selectPattern(1)
    assert not patterns.isPatternSelected(1)


def test_select_pattern():
    patterns.selectPattern(1, 1)
    assert patterns.isPatternSelected(1)
    patterns.selectPattern(1, 1)
    assert patterns.isPatternSelected(1)


def test_deselect_pattern():
    patterns.selectPattern(1, 0)
    assert not patterns.isPatternSelected(1)
    patterns.selectPattern(1, 0)
    assert not patterns.isPatternSelected(1)


def test_pattern_multi_select():
    addPattern()
    addPattern()
    addPattern()
    for i in range(1, 5):
        assert not patterns.isPatternSelected(i)
        # Select it for next time
        patterns.selectPattern(i)
    # Now they should all be selected
    for i in range(1, 5):
        assert patterns.isPatternSelected(i)


def test_default_active_pattern():
    assert patterns.patternNumber() == 1


def test_selection_changes_active_pattern():
    addPattern()
    addPattern()
    addPattern()
    patterns.selectPattern(4)
    assert patterns.patternNumber() == 4


def test_deselection_changes_active_to_first_selected():
    addPattern()
    addPattern()
    addPattern()
    patterns.selectPattern(2)
    patterns.selectPattern(3)
    patterns.selectPattern(4)
    # Deselect
    patterns.selectPattern(4)
    # Active returned to first selection
    assert patterns.patternNumber() == 2


def test_last_deselection_leaves_active():
    addPattern()
    addPattern()
    addPattern()
    patterns.selectPattern(1, 0)
    patterns.selectPattern(2, 1)
    assert patterns.patternNumber() == 2
    # Deselect
    patterns.selectPattern(2, 0)
    # Pattern number remains unchanged
    assert patterns.patternNumber() == 2


def test_jump_to_pattern_selects_unselected():
    """Calling jumpToPattern() selects that pattern alone, if it is deselected
    """
    addPattern()
    addPattern()
    addPattern()
    patterns.jumpToPattern(2)
    assert patterns.patternNumber() == 2
    assert not patterns.isPatternSelected(1)
    assert patterns.isPatternSelected(2)


def test_jump_to_pattern_select_begin():
    """Calling jumpToPattern() leaves selection if the pattern is already
    selected
    """
    patterns.jumpToPattern(1)
    assert patterns.isPatternSelected(1)


def test_jump_to_pattern_not_select_selected():
    """Calling jumpToPattern() leaves selection if the pattern is already
    selected
    """
    addPattern()
    addPattern()
    addPattern()
    patterns.selectPattern(2)
    patterns.jumpToPattern(2)
    assert patterns.patternNumber() == 2
    assert patterns.isPatternSelected(1)
    assert patterns.isPatternSelected(2)


def test_jump_to_zeroth_index():
    """Jumping to pattern 0 actually selects pattern 1"""
    patterns.selectPattern(0)
    # This will select the first one
    assert patterns.isPatternSelected(1)
    assert patterns.patternNumber() == 1
