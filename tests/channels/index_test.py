
import pytest
import channels
from fl_model import getState
from fl_model.channels import (
    addSampler,
    groupIndexToGlobalIndex,
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
    """
    Remove first channel
    """
    removeChannel(0)


@pytest.fixture
def ten_channels(no_channels):
    """
    Ten channels
    """
    for i in range(10):
        addSampler(f'Sampler {i+1}')


@pytest.fixture
def ten_grouped_channels(no_channels):
    """
    Ten channels which have been organized into groups

    * `0`: ungrouped

    * `1`: in group 'Test'

    * `2`: ungrouped

    * etc
    """
    for i in range(10):
        if i % 2:
            addSampler(f'Sampler {i+1}', group='Test')
        else:
            addSampler(f'Sampler {i+1}')


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


def test_get_channel_groups_unsorted(ten_channels):
    """Are all channels included in the list of unsorted channels"""
    assert getChannelsInGroup('') == [i for i in range(10)]


def test_get_channel_groups_all(ten_grouped_channels):
    """Are all channels included in the list of all channels"""
    assert getChannelsInGroup(...) == [i for i in range(10)]


def test_split_groups(ten_grouped_channels):
    """Can channels be split into groups during creation"""
    assert getChannelsInGroup('Test') == [i for i in range(10) if i % 2]
    assert getChannelsInGroup('') == [i for i in range(10) if not i % 2]


def test_add_to_group(ten_channels):
    """Can we add channels to groups manually"""
    # Group channels 5-10
    addToGroup('Hello', set(range(5, 10)))

    assert getChannelsInGroup('Hello') == list(range(5, 10))
    assert getChannelsInGroup('') == list(range(5))


def test_add_to_group_bad_channel_index():
    """
    Do we get an FlIndexError when we try to add a chanel to an invalid group
    """
    with pytest.raises(FlIndexError):
        addToGroup('Test', {1})


def test_remove_from_group(ten_grouped_channels):
    """Can we remove a channel from a group"""
    # Remove channel one from group
    assert removeChannelFromGroup(1, 'Test')

    assert getChannelsInGroup('Test') == [i for i in range(3, 10) if i % 2]
    # It should now be in the ungrouped category
    assert getChannelsInGroup('') == \
        [i for i in range(10) if i == 1 or (i % 2 == 0)]


def test_remove_from_wrong_group():
    """
    Do we get False returned when we remove a channel from the wrong group
    """
    assert not removeChannelFromGroup(0, 'Not a group')


def test_remove_from_unsorted_group():
    """
    Does nothing happen when we remove a channel from the '' unsorted group
    """
    assert removeChannelFromGroup(0, '')
    assert getChannelsInGroup('') == [0]


def test_remove_from_any_group(ten_grouped_channels):
    """Can we remove a channel from any group"""
    # Remove channel one from group
    removeChannelFromAnyGroup(1)

    assert getChannelsInGroup('Test') == [i for i in range(3, 10) if i % 2]
    # It should now be in the ungrouped category
    assert getChannelsInGroup('') == \
        [i for i in range(10) if i == 1 or (i % 2 == 0)]


def test_index_to_grouped_index_ungrouped(ten_channels):
    """
    Do we get the right indexes when we get group indexes for channels when
    there are no groups
    """
    for i in range(10):
        assert globalIndexToGroupIndex(i) == i


def test_index_to_grouped_index_grouped(ten_grouped_channels):
    """
    Do we get the right indexes when we get group indexes for channels when
    the are grouped
    """
    for i in range(10):
        assert globalIndexToGroupIndex(i) == i // 2


def test_index_to_grouped_index_wrong_group(ten_grouped_channels):
    """
    Do we get a ValueError when we ask for the group index of a track not in
    that group
    """
    with pytest.raises(ValueError):
        globalIndexToGroupIndex(0, 'Test')
    with pytest.raises(ValueError):
        globalIndexToGroupIndex(1, '')


def test_index_to_global_index_no_groups(ten_channels):
    """
    Do we get the right indexes when we get global indexes for channels when
    there are no groups
    """
    for i in range(10):
        assert groupIndexToGlobalIndex(i) == i


def test_channel_number_allow_no_select():
    """Do we get -1 for the channel number if there is no selection?
    """
    channels.selectChannel(0, False)
    assert channels.channelNumber(True) == -1


def test_channel_number_disallow_no_select():
    """Do we get 0 for channel number if there is no selection and we didn't
    allow none?
    """
    channels.selectChannel(0, False)
    assert channels.channelNumber() == 0


def test_channel_number_offset(ten_channels):
    """Can we get the correct offset indexes for channelNumber?"""
    for i in range(10):
        channels.selectChannel(i, True)
    for i in range(10):
        assert channels.channelNumber(False, i) == i


def test_selected_channel_global_allow_no_select():
    """Do we get -1 for the channel number if there is no selection?
    """
    channels.selectChannel(0, False)
    assert channels.selectedChannel(True, 0, True) == -1


def test_selected_channel_global_disallow_no_select():
    """Do we get 0 for channel number if there is no selection and we didn't
    allow none?
    """
    channels.selectChannel(0, False)
    assert channels.selectedChannel(False, 0, True) == 0


def test_selected_channel_global_offset(ten_channels):
    """Can we get the correct offset indexes for channelNumber?"""
    for i in range(10):
        channels.selectChannel(i, True)
    for i in range(10):
        assert channels.selectedChannel(False, i, True) == i


def test_selected_channel_group_allow_no_select():
    """Do we get -1 for the channel number if there is no selection?
    """
    channels.selectChannel(0, False)
    assert channels.selectedChannel(True) == -1


def test_selected_channel_group_disallow_no_select():
    """Do we get 0 for channel number if there is no selection and we didn't
    allow none?
    """
    channels.selectChannel(0, False)
    assert channels.selectedChannel() == 0


def test_selected_channel_group_offset(ten_grouped_channels):
    """Can we get the correct offset indexes for channelNumber?"""
    for i in range(5):
        channels.selectChannel(i, True)
    for i in range(5):
        assert channels.selectedChannel(False, i) == i


def test_channel_count_global(ten_grouped_channels):
    assert channels.channelCount(True) == 10


def test_channel_count_grouped(ten_grouped_channels):
    # Only view the unsorted channels
    getState().channels.selected_group = ''
    assert channels.channelCount() == 5

# TODO: Index errors for group conversion, all group, selected group,
