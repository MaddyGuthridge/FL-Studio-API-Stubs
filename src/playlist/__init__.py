"""Playlist Module (FL Studio built-in)

Allows you to control and interact with the FL Studio Playlist.

## NOTES:
* Playlist tracks are 1-indexed.

## KNOWN ISSUES:
* For all API versions below 20, the accessible range is 0-499 rather than
  1-500.

## HELP WANTED:
* Explanations for display zone functions

* Explanations for live performance related functions
"""

from .__tracks import (
    trackCount,
    getTrackName,
    setTrackName,
    getTrackColor,
    setTrackColor,
    isTrackMuted,
    muteTrack,
    isTrackMuteLock,
    muteTrackLock,
    isTrackSolo,
    soloTrack,
    isTrackSelected,
    selectTrack,
    selectAll,
    deselectAll,
    getTrackActivityLevel,
    getTrackActivityLevelVis,
)

from .__performance import (
    getDisplayZone,
    lockDisplayZone,
    liveDisplayZone,
    getLiveLoopMode,
    getLiveTriggerMode,
    getLivePosSnap,
    getLiveTrigSnap,
    getLiveStatus,
    getLiveBlockStatus,
    getLiveBlockColor,
    triggerLiveClip,
    refreshLiveClip,
    incLivePosSnap,
    incLiveTrigSnap,
    incLiveLoopMode,
    incLiveTrigMode,
    getVisTimeBar,
    getVisTimeTick,
    getVisTimeStep,
    getPerformanceModeState,
)


__all__ = [
    "trackCount",
    "getTrackName",
    "setTrackName",
    "getTrackColor",
    "setTrackColor",
    "isTrackMuted",
    "muteTrack",
    "isTrackMuteLock",
    "muteTrackLock",
    "isTrackSolo",
    "soloTrack",
    "isTrackSelected",
    "selectTrack",
    "selectAll",
    "deselectAll",
    "getTrackActivityLevel",
    "getTrackActivityLevelVis",
    "getDisplayZone",
    "lockDisplayZone",
    "liveDisplayZone",
    "getLiveLoopMode",
    "getLiveTriggerMode",
    "getLivePosSnap",
    "getLiveTrigSnap",
    "getLiveStatus",
    "getLiveBlockStatus",
    "getLiveBlockColor",
    "triggerLiveClip",
    "refreshLiveClip",
    "incLivePosSnap",
    "incLiveTrigSnap",
    "incLiveLoopMode",
    "incLiveTrigMode",
    "getVisTimeBar",
    "getVisTimeTick",
    "getVisTimeStep",
    "getPerformanceModeState",
]
