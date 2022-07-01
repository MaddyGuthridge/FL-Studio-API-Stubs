
from dataclasses import dataclass
from fl_model.exceptions import FlIndexError
from ..consts import DEFAULT_FL_COLOR


class GridBits:
    """
    Represents the grid bits for a single channel, allowing the bits to be
    toggled or set for each index.
    """
    def __init__(self) -> None:
        self.__bits: set[int] = set()

    def __setitem__(self, index: int, value: bool):
        if index < 0:
            raise FlIndexError()
        if value:
            self.__bits.add(index)
        else:
            self.__bits.discard(index)

    def __getitem__(self, index: int) -> bool:
        return index in self.__bits

    def toggle(self, index: int):
        self[index] = not self[index]


class PatternModel:
    name: str
    color: int
    selected: bool
    track_contents: list[GridBits]

    def __init__(self, num_tracks: int, pattern_num: int) -> None:
        self.track_contents = []
        self.color = DEFAULT_FL_COLOR
        self.name = f'Pattern {pattern_num}'
        self.selected = False
        for _ in range(num_tracks):
            self.track_contents.append(GridBits())

    def notifyChannelCreate(self, position: int) -> None:
        self.track_contents.insert(position, GridBits())

    def notifyChannelDestroy(self, position: int) -> None:
        self.track_contents.pop(position)

    def notifyChannelSwapped(self, first: int, second: int) -> None:
        t = self.track_contents
        t[first], t[second] = t[second], t[first]


@dataclass
class PatternListModel:
    p: list[PatternModel]
    active_pattern: int = 1


default_pattern_list = PatternListModel([PatternModel(1, 1)])
