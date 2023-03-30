"""Channels Module (FL Studio built-in)

Allows you to control and interact with the FL Studio Channel Rack, and with
instrument channels.

## NOTE:
* In this documentation, an index respects channel groups, whereas a
  global index does not.

* Channels are zero-indexed.
"""
from .__properties import (
    channelNumber,
    channelCount,
    getChannelName,
    setChannelName,
    getChannelColor,
    setChannelColor,
    isChannelMuted,
    muteChannel,
    isChannelSolo,
    soloChannel,
    getChannelVolume,
    setChannelVolume,
    getChannelPan,
    setChannelPan,
    getChannelPitch,
    setChannelPitch,
    getChannelType,
    isChannelSelected,
    selectChannel,
    selectOneChannel,
    selectedChannel,
    selectAll,
    deselectAll,
    getChannelMidiInPort,
    getChannelIndex,
    getTargetFxTrack,
    setTargetFxTrack,
    processRECEvent,
    incEventValue,
    getRecEventId,
)
from .__sequencer import (
    getGridBit,
    getGridBitWithLoop,
    setGridBit,
    isGridBitAssigned,
    getStepParam,
    getCurrentStepParam,
    setStepParameterByIndex,
    updateGraphEditor,
)
from .__ui import (
    isHighlighted,
    showGraphEditor,
    isGraphEditorVisible,
    showEditor,
    focusEditor,
    showCSForm,
    getActivityLevel,
)
from .__notes import (
    midiNoteOn,
    quickQuantize,
)


__all__ = (
    'channelNumber',
    'channelCount',
    'getChannelName',
    'setChannelName',
    'getChannelColor',
    'setChannelColor',
    'isChannelMuted',
    'muteChannel',
    'isChannelSolo',
    'soloChannel',
    'getChannelVolume',
    'setChannelVolume',
    'getChannelPan',
    'setChannelPan',
    'getChannelPitch',
    'setChannelPitch',
    'getChannelType',
    'isChannelSelected',
    'selectChannel',
    'selectOneChannel',
    'selectedChannel',
    'selectAll',
    'deselectAll',
    'getChannelMidiInPort',
    'getChannelIndex',
    'getTargetFxTrack',
    'setTargetFxTrack',
    'processRECEvent',
    'incEventValue',
    'getRecEventId',
    'getGridBit',
    'getGridBitWithLoop',
    'setGridBit',
    'isGridBitAssigned',
    'getStepParam',
    'getCurrentStepParam',
    'setStepParameterByIndex',
    'updateGraphEditor',
    'isHighlighted',
    'showGraphEditor',
    'isGraphEditorVisible',
    'showEditor',
    'focusEditor',
    'showCSForm',
    'getActivityLevel',
    'midiNoteOn',
    'quickQuantize',
)
