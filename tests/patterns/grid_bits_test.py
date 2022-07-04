"""
tests > patterns > grid_bits_test

Test for grid bits, and how they relate to patterns
"""
import patterns
import channels
from fl_model.patterns import addPattern


def test_grid_bits_independent_based_on_pattern():
    addPattern()
    channels.setGridBit(0, 0, True)
    patterns.jumpToPattern(2)
    assert not channels.getGridBit(0, 0)
    patterns.jumpToPattern(2)
    assert channels.getGridBit(0, 0)
