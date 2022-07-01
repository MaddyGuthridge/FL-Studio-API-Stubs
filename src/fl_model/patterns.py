
from .state import getState
from .models import PatternModel


def addPattern():
    s = getState()
    s.patterns.p.append(PatternModel(
        len(s.channels.channel_list),
        len(s.patterns.p)
    ))


def removePattern(index: int):
    # NOTE: FL Studio actually uses a remove selected patterns control
    # Handle 1-indexedness of patterns
    index -= 1
    s = getState()
    s.patterns.p.pop(index)
    if s.patterns.active_pattern >= index:
        s.patterns.active_pattern -= 1
