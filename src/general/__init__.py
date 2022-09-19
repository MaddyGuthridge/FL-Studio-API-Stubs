"""General Module (FL Studio built-in)

Handles general interactions with FL Studio
"""
__all__ = [
    'saveUndo',
    'undo',
    'undoUp',
    'undoDown',
    'undoUpDown',
    'restoreUndo',
    'restoreUndoLevel',
    'getUndoLevelHint',
    'getUndoHistoryPos',
    'getUndoHistoryCount',
    'getUndoHistoryLast',
    'setUndoHistoryPos',
    'setUndoHistoryCount',
    'setUndoHistoryLast',
    'getRecPPB',
    'getRecPPQ',
    'getUseMetronome',
    'getPrecount',
    'getChangedFlag',
    'getVersion',
    'processRECEvent',
    'dumpScoreLog',
    'clearLog',
]


from .__undo import (
    saveUndo,
    undo,
    undoUp,
    undoDown,
    undoUpDown,
    restoreUndo,
    restoreUndoLevel,
    getUndoLevelHint,
    getUndoHistoryPos,
    getUndoHistoryCount,
    getUndoHistoryLast,
    setUndoHistoryPos,
    setUndoHistoryCount,
    setUndoHistoryLast,
)
from .__fl_state import (
    getRecPPB,
    getRecPPQ,
    getUseMetronome,
    getPrecount,
    getChangedFlag,
    getVersion,
    processRECEvent,
    dumpScoreLog,
    clearLog,
)
