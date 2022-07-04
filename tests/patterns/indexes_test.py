
import pytest
import channels
from fl_model.exceptions import FlIndexError
from fl_model.patterns import removePattern
import patterns


@pytest.fixture
def initialise5Patterns():
    for i in range(1, 6):
        patterns.setPatternName(i, f'My pattern {i}')


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


def test_pattern_multi_select(initialise5Patterns):
    for i in range(1, 5):
        assert not patterns.isPatternSelected(i)
        # Select it for next time
        patterns.selectPattern(i)
    # Now they should all be selected
    for i in range(1, 5):
        assert patterns.isPatternSelected(i)


def test_default_active_pattern():
    assert patterns.patternNumber() == 1


def test_selection_changes_active_pattern(initialise5Patterns):
    patterns.selectPattern(4)
    assert patterns.patternNumber() == 4


def test_deselection_changes_active_to_first_selected(initialise5Patterns):
    patterns.selectPattern(2)
    patterns.selectPattern(3)
    patterns.selectPattern(4)
    # Deselect
    patterns.selectPattern(4)
    # Active returned to first selection
    assert patterns.patternNumber() == 2


def test_last_deselection_leaves_active(initialise5Patterns):
    patterns.selectPattern(1, 0)
    patterns.selectPattern(2, 1)
    assert patterns.patternNumber() == 2
    # Deselect
    patterns.selectPattern(2, 0)
    # Pattern number remains unchanged
    assert patterns.patternNumber() == 2


def test_jump_to_pattern_selects_unselected(initialise5Patterns):
    """Calling jumpToPattern() selects that pattern alone, if it is deselected
    """
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
    patterns.selectPattern(2)
    patterns.jumpToPattern(2)
    assert patterns.patternNumber() == 2
    assert patterns.isPatternSelected(1)
    assert patterns.isPatternSelected(2)


def test_jump_to_zeroth_index():
    """Jumping to pattern 0 actually selects pattern 1"""
    patterns.jumpToPattern(0)
    # This will select the first one
    assert patterns.isPatternSelected(1)
    assert patterns.patternNumber() == 1


def test_default_pattern_count():
    assert patterns.patternCount() == 0


@pytest.mark.parametrize(
    'callback',
    [
        lambda i: patterns.setPatternName(i, 'My pattern'),
        lambda i: patterns.setPatternColor(i, 0xFFFFFF),
        # Abusing the falsiness of None to do multiple statements in a lambda
        # yuck
        lambda i: patterns.jumpToPattern(i) or channels.setGridBit(0, 0, True)  # type: ignore
    ]
)
def test_modify_pattern_increases_count(callback):
    """Test that when the given callback is used to modify a pattern, the
    pattern count increases
    """
    callback(1)
    assert patterns.patternCount() == 1
    callback(2)
    assert patterns.patternCount() == 2
    callback(3)
    assert patterns.patternCount() == 3


def test_modify_pattern_zero_ignored_count():
    """Modifying pattern zero does nothing"""
    patterns.setPatternName(0, 'Ignored pattern')
    assert patterns.patternCount() == 0


def test_select_pattern_ignored_count():
    """Selecting a pattern doesn't stop it from being ignored"""
    patterns.selectPattern(1)
    assert patterns.patternCount() == 0
    patterns.selectPattern(2)
    assert patterns.patternCount() == 0


def test_modify_out_of_order():
    """
    When we "create" a pattern out of order by modifying its properties, do
    patterns created later still turn up in the right places?
    """
    # Edit patterns in reverse: doing so "creates" each pattern
    for i in range(5, 0, -1):
        patterns.setPatternName(i, f'My pattern {i}')
    # Things should appear in the correct order (opposite to creation order)
    assert patterns.patternCount() == 5
    for i in range(1, 6):
        assert patterns.getPatternName(i) == f'My pattern {i}'
