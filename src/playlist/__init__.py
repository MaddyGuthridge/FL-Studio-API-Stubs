"""Playlist Module (FL Studio built-in)

Allows you to control and interact with the FL Studio Playlist.

## NOTES:
* Playlist tracks are 1-indexed.
* For information on performance mode, see the
[performance mode tutorial](/tutorials/performance_mode).
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
    refreshLiveClips,
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
    "refreshLiveClips",
    "incLivePosSnap",
    "incLiveTrigSnap",
    "incLiveLoopMode",
    "incLiveTrigMode",
    "getVisTimeBar",
    "getVisTimeTick",
    "getVisTimeStep",
    "getPerformanceModeState",
]
