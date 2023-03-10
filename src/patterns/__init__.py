"""Patterns Module (FL Studio built-in)

Allows you to control and interact with FL Studio Patterns.

## NOTES:

* Patterns are 1-indexed, with a range from `1` - `999`, meaning that the
  1000th pattern cannot be created

    * HELP WANTED: What happens when you create that many patterns
"""
from .__properties import (
    patternNumber,
    patternCount,
    patternMax,
    getPatternName,
    setPatternName,
    getPatternColor,
    setPatternColor,
    getPatternLength,
    jumpToPattern,
    findFirstNextEmptyPat,
    isPatternSelected,
    selectPattern,
    selectAll,
    deselectAll,
    burnLoop,
    isPatternDefault,
    clonePattern,
)
from .__performance import (
    getBlockSetStatus,
    ensureValidNoteRecord,
)
from .__groups import (
    getActivePatternGroup,
    getPatternGroupCount,
    getPatternGroupName,
    getPatternsInGroup,
)


__all__ = (
    'patternNumber',
    'patternCount',
    'patternMax',
    'getPatternName',
    'setPatternName',
    'getPatternColor',
    'setPatternColor',
    'getPatternLength',
    'jumpToPattern',
    'findFirstNextEmptyPat',
    'isPatternSelected',
    'selectPattern',
    'selectAll',
    'deselectAll',
    'burnLoop',
    'isPatternDefault',
    'getBlockSetStatus',
    'ensureValidNoteRecord',
    'clonePattern',
    'getActivePatternGroup',
    'getPatternGroupCount',
    'getPatternGroupName',
    'getPatternsInGroup',
)
