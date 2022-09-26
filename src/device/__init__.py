"""
FL Studio built-in module

Handles the way that devices connect to FL Studio's MIDI interface, and how
scripts communicate with each other.

# FL Studio's event mapping system (REC events)

FL Studio uses an advanced system mapping events from hardware controls to
software controls, which can be confusing to use without an explanation.

## Control IDs

These represent the unique identifier of a single hardware control within FL
Studio. They are formed from a port number, a MIDI channel and a CC number,
which are encoded as follows:

```py
cc + (channel << 16) + ((port + 1) << 22)
```

This encoding can be calculated using the `midi.EncodeRemoteControlID`
function.

## Event IDs

FL Studio maps events using event IDs, which represent the unique identifier of
a single software control. When automating these controls, event IDs are mapped
to control IDs. You can determine this link using the `device.findEventID`
function.

From this, several functions are available to interact with FL Studio using
event IDs.

* `device.getLinkedValue`: get the value associated with this event ID
* `device.getLinkedValueString`: get the value associated with this event ID as
  a string
* `device.getLinkedParamName`: get the name of the parameter linked with this
  event ID
* `device.getLinkedInfo`: get info about the parameter linked with this event
  ID
* `ui.openEventEditor`: open an event editor window for the control associated
  with this event ID
* `channels.getRecEventId`: return the base value for event IDs associated with
  this channel.
* `channels.incEventValue`: get an event value increased by a step
* `general.processRECEvent`: let FL Studio handle a change to the value of this
  event ID
"""

__all__ = [
    'isAssigned',
    'getPortNumber',
    'getName',
    'midiOutMsg',
    'midiOutNewMsg',
    'midiOutSysex',
    'sendMsgGeneric',
    'directFeedback',
    'repeatMidiEvent',
    'stopRepeatMidiEvent',
    'setMasterSync',
    'getMasterSync',
    'processMIDICC',
    'forwardMIDICC',
    'findEventID',
    'getLinkedValue',
    'getLinkedValueString',
    'getLinkedParamName',
    'getLinkedInfo',
    'dispatch',
    'dispatchReceiverCount',
    'dispatchGetReceiverPortNumber',
    'createRefreshThread',
    'destroyRefreshThread',
    'fullRefresh',
    'isDoubleClick',
]

from .__device import (
    isAssigned,
    getPortNumber,
    getName,
    midiOutMsg,
    midiOutNewMsg,
    midiOutSysex,
    sendMsgGeneric,
    directFeedback,
    repeatMidiEvent,
    stopRepeatMidiEvent,
    setMasterSync,
    getMasterSync,
)
from .__fl import (
    processMIDICC,
    forwardMIDICC,
    findEventID,
    getLinkedValue,
    getLinkedValueString,
    getLinkedParamName,
    getLinkedInfo,
)
from .__dispatch import (
    dispatch,
    dispatchReceiverCount,
    dispatchGetReceiverPortNumber,
)
from .__util import (
    createRefreshThread,
    destroyRefreshThread,
    fullRefresh,
    isDoubleClick,
)
