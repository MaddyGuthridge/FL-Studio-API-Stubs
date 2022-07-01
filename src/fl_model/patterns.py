
from .state import getState
from .models import PatternModel


def addPattern():
    s = getState()
    s.patterns.p.append(PatternModel(
        len(s.channels.channel_list),
        len(s.patterns.p)
    ))


def removePattern(index: int):
    # Handle 1-indexedness of patterns
    index -= 1
    s = getState()
    s.patterns.p.pop(index)
