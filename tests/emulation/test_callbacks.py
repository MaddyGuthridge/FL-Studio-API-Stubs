"""
tests > emulation > test_callbacks

Tests for callback functions.
"""
from fl_classes import FlMidiMsg
from fl_model.emulation import DeviceModule
from . import _device


def checkOnlyCalled(counts, names: list[str]):
    for ele in dir(counts):
        val = getattr(counts, ele)
        if ele in names:
            assert val == 1
        else:
            if isinstance(val, int):
                assert val == 0


def test_init_deInit():
    """
    Can we initialise and deinitialize the device
    """
    _device.reset()
    dev = DeviceModule(_device, None)
    dev.onInit()
    dev.onDeInit()
    checkOnlyCalled(_device.counts, [
        'OnInit',
        'OnDeInit',
    ])


def test_process_note_on():
    """
    Check that note on events are sent through the correct functions
    """
    _device.reset()
    dev = DeviceModule(_device, None)
    dev.sendEvent(FlMidiMsg(0x90, 0, 0))
    checkOnlyCalled(_device.counts, [
        'OnMidiMsg',
        'OnMidiIn',
        'OnNoteOn',
    ])


def test_process_note_off():
    """
    Check that note off events are sent through the correct functions
    """
    _device.reset()
    dev = DeviceModule(_device, None)
    dev.sendEvent(FlMidiMsg(0x80, 0, 0))
    checkOnlyCalled(_device.counts, [
        'OnMidiMsg',
        'OnMidiIn',
        'OnNoteOff',
    ])


def test_process_cc():
    """
    Check that note off events are sent through the correct functions
    """
    _device.reset()
    dev = DeviceModule(_device, None)
    dev.sendEvent(FlMidiMsg(0xB0, 0, 0))
    checkOnlyCalled(_device.counts, [
        'OnMidiMsg',
        'OnMidiIn',
        'OnControlChange',
    ])


def test_process_key_pressure():
    """
    Check that note off events are sent through the correct functions
    """
    _device.reset()
    dev = DeviceModule(_device, None)
    dev.sendEvent(FlMidiMsg(0xA0, 0, 0))
    checkOnlyCalled(_device.counts, [
        'OnMidiMsg',
        'OnMidiIn',
        'OnKeyPressure',
    ])
