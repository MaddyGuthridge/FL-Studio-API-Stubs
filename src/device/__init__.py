"""
FL Studio built-in module

Handles the way that devices connect to FL Studio's MIDI interface, and how
scripts communicate with each other.
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
    'getDeviceId',
    'getLinkedChannel',
    'linkToLastTweaked',
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
    getDeviceId,
)
from .__fl import (
    processMIDICC,
    forwardMIDICC,
    findEventID,
    getLinkedValue,
    getLinkedValueString,
    getLinkedParamName,
    getLinkedInfo,
    getLinkedChannel,
    linkToLastTweaked,
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
