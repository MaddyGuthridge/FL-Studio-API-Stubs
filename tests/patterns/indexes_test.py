
import pytest
import channels
from fl_model import getState
from fl_model.consts import PATTERN_COUNT
from fl_model.exceptions import FlIndexError
from fl_model.patterns import removePattern, isPatternVisible
import patterns


@pytest.fixture
def initialise5Patterns():
    for i in range(1, 6):
        patterns.setPatternName(i, f'My pattern {i}')


def test_access_hidden_index():
    """Can we access pattern index 0?"""
    assert patterns.getPatternName(0) == 'Pattern 0'


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
        func(PATTERN_COUNT, *params)


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
    """Are indexes inside the range 0 <= i <= 999 valid?"""
    func(0, *params)
    func(PATTERN_COUNT - 1, *params)


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


def test_jump_to_pattern():
    """When we jump to a pattern, does it become the active pattern?
    """
    patterns.jumpToPattern(5)
    assert patterns.patternNumber() == 5


def test_jump_to_pattern_selects_unselected(initialise5Patterns):
    """Does calling jumpToPattern() selects that pattern alone if it is
    deselected?
    """
    patterns.jumpToPattern(2)
    assert patterns.patternNumber() == 2
    assert not patterns.isPatternSelected(1)
    assert patterns.isPatternSelected(2)


def test_jump_to_pattern_select_begin():
    """Does calling jumpToPattern() leave the selection if the pattern is
    already selected
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
    """Does modifying pattern zero do nothing?
    """
    patterns.setPatternName(0, 'Ignored pattern')
    assert patterns.patternCount() == 0


def test_select_pattern_ignored_count():
    """Does a pattern keep being ignored when it is selected?
    """
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


def test_remove_pattern_reset():
    """Does removing a pattern reset its properties?
    """
    patterns.setPatternColor(1, 0xFFFFFF)
    patterns.setPatternName(1, 'Custom name')
    channels.setGridBit(0, 0, True)
    removePattern(1)
    assert patterns.getPatternColor(1) != 0xFFFFFF
    assert patterns.getPatternName(1) == 'Pattern 1'
    assert not channels.getGridBit(0, 0)


def test_remove_pattern_shift_later():
    """Does removing a pattern reduce the indexes of previous patterns?
    """
    patterns.setPatternName(2, "My pattern 2")
    removePattern(1)
    assert patterns.getPatternName(1) == "My pattern 2"


def test_remove_pattern_wrap_around():
    """Do properties set to pattern 0 get copied to pattern 999 when a pattern
    is removed?
    """
    patterns.setPatternName(0, "How is this allowed?")
    removePattern(1)
    assert patterns.getPatternName(PATTERN_COUNT - 1) == "How is this allowed?"


def test_pattern_visible_jump_to():
    """Does a pattern become visible when we jump to it?
    """
    patterns.jumpToPattern(10)
    assert isPatternVisible(10)


def test_pattern_visible_modify():
    """Does a pattern become visible when we modify it?
    """
    patterns.setPatternName(10, "Now you see me")
    assert isPatternVisible(10)


def test_pattern_zero_invisible():
    """Is it impossible to make pattern zero visible?
    """
    patterns.setPatternName(0, "Now you don't")
    assert not isPatternVisible(0)


def select_all_patterns(initialise5Patterns):
    """Can we select all patterns?
    """
    patterns.selectAll()
    for i in range(1, 6):
        assert patterns.isPatternSelected(i)
    # Are invisible patterns ignored
    assert not patterns.isPatternSelected(0)
    for i in range(6, PATTERN_COUNT):
        assert not patterns.isPatternSelected(i)


def deselect_all_patterns(initialise5Patterns):
    """Can we deselect all patterns?
    """
    for i in range(1, 6):
        patterns.selectPattern(i)
    patterns.deselectAll()
    for i in range(1, 6):
        assert not patterns.isPatternSelected(i)


def select_all_patterns_view_empty():
    """Are empty patterns selected when shown if we select all?
    """
    getState().patterns.all_patterns_shown = True
    patterns.selectAll()
    for i in range(1, PATTERN_COUNT):
        assert patterns.isPatternSelected(i)
    # Is pattern 0 ignored?
    assert not patterns.isPatternSelected(0)
