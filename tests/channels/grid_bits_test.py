import channels


def test_set_grid_bit():
    # To begin with, all channels are uninitialized
    channels.setGridBit(0, 0, True)
    assert channels.getGridBit(0, 0)
    channels.setGridBit(0, 0, False)
    assert not channels.getGridBit(0, 0)


def test_grid_bits_independent():
    """Make sure grid bits can be togged independently"""
    channels.setGridBit(0, 0, True)
    channels.setGridBit(0, 1, True)
    channels.setGridBit(0, 2, False)
    channels.setGridBit(0, 3, True)
    assert channels.getGridBit(0, 0)
    assert channels.getGridBit(0, 1)
    assert not channels.getGridBit(0, 2)
    assert channels.getGridBit(0, 3)


# TODO: Test set with loop
