"""
tests > emulation > _device

A virtual device used to test that our callbacks are working
"""
from dataclasses import dataclass


@dataclass
class Counts:
    OnInit: int = 0
    OnDeInit: int = 0
    OnMidiIn: int = 0
    OnMidiMsg: int = 0
    OnSysex: int = 0
    OnNoteOn: int = 0
    OnNoteOff: int = 0
    OnControlChange: int = 0
    OnProgramChange: int = 0
    OnPitchBend: int = 0
    OnKeyPressure: int = 0
    OnChannelPressure: int = 0
    OnMidiOutMsg: int = 0
    OnIdle: int = 0
    OnProjectLoad: int = 0
    OnRefresh: int = 0
    OnDoFullRefresh: int = 0
    OnUpdateBeatIndicator: int = 0
    OnDisplayZone: int = 0
    OnUpdateLiveMode: int = 0
    OnDirtyMixerTrack: int = 0
    OnDirtyChannel: int = 0
    OnFirstConnect: int = 0
    OnUpdateMeters: int = 0
    OnWaitingForInput: int = 0
    OnSendTempMsg: int = 0


counts = Counts()


def generate():
    callbacks = [
        'OnInit',
        'OnDeInit',
        'OnMidiIn',
        'OnMidiMsg',
        'OnSysex',
        'OnNoteOn',
        'OnNoteOff',
        'OnControlChange',
        'OnProgramChange',
        'OnPitchBend',
        'OnKeyPressure',
        'OnChannelPressure',
        'OnMidiOutMsg',
        'OnIdle',
        'OnProjectLoad',
        'OnRefresh',
        'OnDoFullRefresh',
        'OnUpdateBeatIndicator',
        'OnDisplayZone',
        'OnUpdateLiveMode',
        'OnDirtyMixerTrack',
        'OnDirtyChannel',
        'OnFirstConnect',
        'OnUpdateMeters',
        'OnWaitingForInput',
        'OnSendTempMsg',
    ]

    # Generate all the callback functions
    for c in callbacks:
        def create(name):
            def func(*_):
                count = getattr(counts, name)
                setattr(counts, name, count + 1)
            return func
        # Add this function to the global namespace
        globals()[c] = create(c)


def reset():
    global counts
    counts = Counts()


generate()
