
from fl_model.consts import oo
import channels


def test_name():
    name = "My channel"
    channels.setChannelName(0, name)
    assert channels.getChannelName(0) == name


def test_color():
    c = 0xFFFFFF
    channels.setChannelColor(0, c)
    assert channels.getChannelColor(0) == c


def test_color_default():
    c = 0x5C656A
    assert channels.getChannelColor(0) == c


def test_volume_default():
    """Default volume"""
    assert channels.getChannelVolume(0) == 0.78125


def test_volume():
    v = 0.5
    channels.setChannelVolume(0, v)
    assert channels.getChannelVolume(0) == v


def test_volume_out_of_range():
    """Out of range volumes are clamped"""
    channels.setChannelVolume(0, 1.5)
    assert channels.getChannelVolume(0) == 1.0
    channels.setChannelVolume(0, -0.1)
    assert channels.getChannelVolume(0) == 0.0


def test_panning_default():
    """Default panning"""
    assert channels.getChannelPan(0) == 0.0


def test_panning():
    v = 0.5
    channels.setChannelPan(0, v)
    assert channels.getChannelPan(0) == v
    v = -0.5
    channels.setChannelPan(0, v)
    assert channels.getChannelPan(0) == v


def test_panning_out_of_range():
    """Out of range pans are clamped"""
    channels.setChannelPan(0, 1.5)
    assert channels.getChannelPan(0) == 1.0
    channels.setChannelPan(0, -1.5)
    assert channels.getChannelPan(0) == -1.0


def test_volume_db_default():
    """The default volume for channels is -5.2 dB"""
    assert channels.getChannelVolume(0, True) == -5.2


def test_volume_db_mute():
    """When muted, the volume of a channel is -oo"""
    channels.setChannelVolume(0, 0.0)
    assert channels.getChannelVolume(0, True) == -oo


def test_volume_db_max():
    """When maxed, the volume of a channel is 0 db"""
    channels.setChannelVolume(0, 1.0)
    assert channels.getChannelVolume(0, True) == 0
