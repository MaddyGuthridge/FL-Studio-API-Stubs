
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
    # Only index 1 exists
    with pytest.raises(FlIndexError):
        func(0, *params)
    with pytest.raises(FlIndexError):
        func(2, *params)


def test_selection_default():
    # By default no pattern is selected
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
    for i in range(1, 4):
        assert not patterns.isPatternSelected(i)
        # Select it for next time
        patterns.selectPattern(i)
    # Now they should all be selected
    for i in range(1, 4):
        assert patterns.isPatternSelected(i)

