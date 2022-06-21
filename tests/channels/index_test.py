
import pytest
import channels
from fl_model.channels import addSampler
from fl_model.exceptions import FlIndexError


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
