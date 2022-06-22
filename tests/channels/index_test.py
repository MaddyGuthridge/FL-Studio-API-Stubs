
import pytest
import channels
from fl_model.channels import (
    addSampler,
    removeChannel,
    getChannelsInGroup,
    addToGroup,
    removeChannelFromAnyGroup,
    removeChannelFromGroup,
    globalIndexToGroupIndex,
)
from fl_model.exceptions import FlIndexError


@pytest.fixture
def no_channels():
    removeChannel(0)


@pytest.mark.parametrize(
    ['func', 'args'],
    [
        # Getters
        (channels.getChannelColor, tuple()),
        (channels.getChannelIndex, tuple()),
        (channels.getActivityLevel, tuple()),
        (channels.getChannelMidiInPort, tuple()),
        (channels.getChannelName, tuple()),
        (channels.getChannelPan, tuple()),
        (channels.getChannelPitch, tuple()),
        (channels.getChannelType, tuple()),
        (channels.getChannelVolume, tuple()),
        (channels.getTargetFxTrack, tuple()),
        (channels.focusEditor, tuple()),
        (channels.getCurrentStepParam, (0, 0)),
        (channels.getGridBit, (0,)),
        (channels.getGridBitWithLoop, (0,)),
        (channels.getRecEventId, tuple()),
        (channels.getStepParam, (0, 0, 0, 0)),
        (channels.isChannelMuted, tuple()),
        (channels.isChannelSolo, tuple()),
        (channels.isChannelSelected, tuple()),
        (channels.midiNoteOn, (64, 127)),
        (channels.quickQuantize, tuple()),
        (channels.showCSForm, tuple()),
        # Setters
        (channels.setChannelColor, (0xFFFFFF,)),
        (channels.setChannelName, ('Channel',)),
        (channels.setChannelPan, (0.5,)),
        (channels.setChannelPitch, (1.0,)),
        (channels.setChannelVolume, (0.5,)),
        (channels.setGridBit, (0, True)),
        (channels.muteChannel, tuple()),
        (channels.soloChannel, tuple()),
        (channels.selectChannel, tuple()),
        (channels.selectOneChannel, tuple()),
    ]
)
def test_access_invalid_index(func, args):
    """Are we unable to access out-of-bounds indexes"""
    with pytest.raises(FlIndexError):
        func(1, *args)
    with pytest.raises(FlIndexError):
        func(-1, *args)
    # Add an extra channel
    addSampler('Sampler #2')
    func(1, *args)  # No error
    with pytest.raises(FlIndexError):
        func(2, *args)


def test_get_channel_groups_all(no_channels):
    """Are all channels included in the list of unsorted channels"""
    for i in range(10):
        addSampler(f'Sampler {i+1}')

    assert getChannelsInGroup('') == [i for i in range(10)]


def test_split_groups(no_channels):
    """Can channels be split into groups during creation"""
    for i in range(10):
        if i % 2:
            addSampler(f'Sampler {i+1}', group='Test')
        else:
            addSampler(f'Sampler {i+1}')

    assert getChannelsInGroup('Test') == [i for i in range(10) if i % 2]
    assert getChannelsInGroup('') == [i for i in range(10) if not i % 2]


def test_add_to_group(no_channels):
    """Can we add channels to groups manually"""
    for i in range(10):
        addSampler(f'Sampler {i+1}')

    # Group first 10 channels
    addToGroup('Hello', set(range(5, 10)))

    assert getChannelsInGroup('Hello') == list(range(5, 10))
    assert getChannelsInGroup('') == list(range(5))


def test_add_to_group_bad_channel_index():
    """
    Do we get an FlIndexError when we try to add a chanel to an invalid group?
    """
    with pytest.raises(FlIndexError):
        addToGroup('Test', {1})


def test_remove_from_group(no_channels):
    """Can we remove a channel from a group"""
    for i in range(10):
        if i % 2:
            addSampler(f'Sampler {i+1}', group='Test')
        else:
            addSampler(f'Sampler {i+1}')

    # Remove channel one from group
    removeChannelFromGroup(1, 'Test')

    assert getChannelsInGroup('Test') == [i for i in range(3, 10) if i % 2]
    # It should now be in the ungrouped category
    assert getChannelsInGroup('') == \
        [i for i in range(10) if i == 1 or (i % 2 == 0)]
