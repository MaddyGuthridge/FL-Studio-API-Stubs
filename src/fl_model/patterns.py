
from copy import deepcopy
from typing import Optional
from .consts import PATTERN_COUNT
from .state import getState
from .models import PatternModel


def removePattern(index: int) -> None:
    """Remove the pattern at index"""
    s = getState()
    s.patterns.p.pop(index)
    if s.patterns.active_pattern >= index:
        s.patterns.active_pattern -= 1
    # Add the final pattern back
    new_pat = deepcopy(s.patterns.p[0])
    s.patterns.p.append(new_pat)
    # Notify remaining patterns that their index has changed
    for i in range(index, PATTERN_COUNT):
        s.patterns.p[i].notifyIndexChanged(i)


def isPatternVisible(index: int) -> bool:
    """Returns whether the pattern is visible within FL Studio's UI"""
    # Pattern zero is never visible
    if index == 0:
        return False
    pat = getPatternReference(index)
    s = getState()
    return (
        s.patterns.all_patterns_shown
        or s.patterns.active_pattern == index
        or pat.hasChanged()
    )


def getPatternReference(index: Optional[int] = None) -> PatternModel:
    """
    Returns a reference to the pattern at index.

    ## Args:
    * `index` (`Optional[int]`, optional): pattern index. Defaults to `None`,
      for current pattern.

    ## Returns:
    * `PatternModel`: pattern
    """
    if index is None:
        index = getState().patterns.active_pattern
    return getState().patterns.p[index]
