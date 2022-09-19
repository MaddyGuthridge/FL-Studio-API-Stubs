"""
fl_model > emulation

Contains code which allows for devices to be registered, with a system for
sending events to them.

## Note:
Testing with multiple devices at once is not supported yet, but it is a planned
feature, which will be added to this module.
"""
from fl_classes import FlMidiMsg
from types import ModuleType
from typing import Callable, Optional


# The order in which events should be handled
EVENT_HANDLE_ORDER: list[tuple[str, Callable[[FlMidiMsg], bool]]] = [
    ('OnMidiIn', lambda _: True),
    ('OnMidiMsg', lambda e: e.status != 0xF0),
    ('OnSysEx', lambda e: e.status == 0xF0),
    ('OnNoteOn', lambda e: e.status >> 4 == 0x9),
    ('OnNoteOff', lambda e: e.status >> 4 == 0x8),
    ('OnControlChange', lambda e: e.status >> 4 == 0xB),
    ('OnProgramChange', lambda e: e.status >> 4 == 0xC),
    ('OnPitchBend', lambda e: e.status >> 4 == 0xE),
    ('OnKeyPressure', lambda e: e.status >> 4 == 0xA),
    ('OnChannelPressure', lambda e: e.status >> 4 == 0xD),
]


class DeviceModule:
    """
    A class representing a module registered with FL Studio.

    It allows you to interact with the script and have the rest of the model
    behave correctly.
    """
    def __init__(
        self,
        module: ModuleType,
        midi_out_callback: Optional[Callable[[FlMidiMsg], None]]
    ) -> None:
        """
        Create a DeviceModule object, which can be used to emulate an instance
        of a device

        You can then use this object to emulate sending MIDI messages to the
        device in order to test the device.

        ## Args:
        * `module` (`ModuleType`): module used to represent device

        * `midi_out_callback` (`Callable[[FlMidiMsg], None]`): function which
          will be called when the devices sends a MIDI message back to the
          controller
        """
        self.__mod = module
        self.__midi_out_callback = midi_out_callback
        # Use a queue so that devices can respond directly without causing a
        # recursion error
        self.__message_queue: list[FlMidiMsg] = []

    def __callIfPresent(self, name: str, args: tuple):
        """
        Calls a callback function named `name` in the device's module if it is
        present. Otherwise, does nothing
        """
        if hasattr(self.__mod, name):
            getattr(self.__mod, name)(*args)

    def onInit(self):
        """
        Tell the script to initialize
        """
        self.__callIfPresent('OnInit', tuple())

    def onDeInit(self):
        """
        Tell the script to deinitialize
        """
        self.__callIfPresent('OnDeInit', tuple())

    def sendEvent(self, msg: FlMidiMsg):
        """
        Adds a MIDI message to the queue of MIDI messages to send to the
        device.

        If calling this from the midi_out_callback, care should be taken to
        ensure that an infinite loop isn't created - if both the script and the
        hardware respond to every event then this function will never end.
        """
        # If there's nothing in the queue, add this, process all events (others
        # could be added later)
        if len(self.__message_queue) == 0:
            self.__message_queue.append(msg)
            while len(self.__message_queue) != 0:
                self.__processEvent(self.__message_queue[0])
                self.__message_queue.pop(0)
        # Otherwise, just add it to the queue and it'll get processed later
        else:
            self.__message_queue.append(msg)

    def __processEvent(self, msg: FlMidiMsg):
        """
        Process an event, sending it to any given functions that it matches
        until it is handled
        """
        # Check each potential callback function
        for name, check in EVENT_HANDLE_ORDER:
            # If it can handle this event
            if check(msg):
                # Call it
                self.__callIfPresent(name, (msg,))
                # If it handled the event, our work is done
                if msg.handled:
                    return

    def onMidiOutMsg(self, msg: FlMidiMsg):
        """
        Call the OnIdle function if it is present
        """
        self.__callIfPresent('OnMidiOutMsg', (msg,))

    def onIdle(self):
        """
        Call the OnIdle function if it is present
        """
        self.__callIfPresent('OnIdle', tuple())

    def onProjectLoad(self, status: int):
        """
        Tell the script that a project has loaded
        """
        self.__callIfPresent('OnProjectLoad', (status,))

    def onRefresh(self, flags: int):
        """
        Tell the script to refresh
        """
        self.__callIfPresent('OnRefresh', (flags,))

    def onDoFullRefresh(self):
        """
        Tell the script to refresh completely
        """
        self.__callIfPresent('OnDoFullRefresh', tuple())

    def onUpdateBeatIndicator(self, value: int):
        """
        Tell the script that we changed beat
        """
        self.__callIfPresent('OnUpdateBeatIndicator', (value,))

    def onDisplayZone(self):
        """
        Tell the script that the playlist zone changed
        """
        self.__callIfPresent('OnDisplayZone', tuple())

    def onUpdateLiveMode(self, lastTrack: int):
        """
        Tell the script that something has changed about live mode
        """
        self.__callIfPresent('OnUpdateLiveMode', (lastTrack,))

    def onDirtyMixerTrack(self, index: int):
        """
        Tell the script that a mixer track has changed.
        """
        self.__callIfPresent('OnDirtyMixerTrack', (index,))

    def onDirtyChannel(self, index: int):
        """
        Tell the script that a channel has changed.
        """
        self.__callIfPresent('OnDirtyChannel', (index,))

    def onFirstConnect(self):
        """
        Tell the script that it has just connected to FL Studio
        """
        self.__callIfPresent('OnFirstConnect', tuple())

    def onUpdateMeters(self):
        """
        Tell the script that it should update mixer track meters
        """
        self.__callIfPresent('OnUpdateMeters', tuple())

    def onWaitingForInput(self):
        """
        Tell the script that FL Studio is waiting for MIDI input
        """
        self.__callIfPresent('OnWaitingForInput', tuple())

    def onSendTempMsg(self, message: str, duration: int):
        """
        Tell the script that it should temporarily display a message on its
        screen
        """
        self.__callIfPresent('OnSendTempMsg', (message, duration))
