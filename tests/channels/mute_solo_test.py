"""
tests > channels > mute_solo_test

Test mute and solo functionality on channel rack
"""
import channels
from fl_model.channels import addSampler, removeChannel


def test_mute_channel_toggle():
    channels.muteChannel(0)
    assert channels.isChannelMuted(0)
    channels.muteChannel(0)
    assert not channels.isChannelMuted(0)


def test_single_channel_is_solo():
    assert channels.isChannelSolo(0)


def test_solo_mutes_others():
    removeChannel(0)
    for _ in range(10):
        addSampler('Sampler')
    channels.soloChannel(0)
    assert channels.isChannelSolo(0)
    for _ in range(1, 10):
        assert channels.isChannelMuted(0)
