
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

    def __eq__(self, other: object) -> bool:
        if isinstance(other, GridBits):
            return self.__bits == other.__bits
        else:
            return NotImplemented

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
    def __init__(self, num_tracks: int, pattern_num: int) -> None:
        self.track_contents = []
        self.color = DEFAULT_FL_COLOR
        self.pattern_num = pattern_num
        self.__name = ''
        self.selected = False
        for _ in range(num_tracks):
            self.track_contents.append(GridBits())

    def __eq__(self, other: object) -> bool:
        if isinstance(other, PatternModel):
            return (
                self.track_contents == other.track_contents
                and self.color == other.color
                and self.name == other.name
            )
        else:
            return NotImplemented

    def hasChanged(self) -> bool:
        """Returns whether this pattern has been modified from the default"""
        return self != PatternModel(len(self.track_contents), self.pattern_num)

    def notifyChannelCreate(self, position: int) -> None:
        self.track_contents.insert(position, GridBits())

    def notifyChannelDestroy(self, position: int) -> None:
        self.track_contents.pop(position)

    def notifyChannelSwapped(self, first: int, second: int) -> None:
        t = self.track_contents
        t[first], t[second] = t[second], t[first]

    def notifyIndexChanged(self, new_index) -> None:
        self.pattern_num = new_index

    @property
    def name(self) -> str:
        if self.__name != '':
            return self.__name
        else:
            return f'Pattern {self.pattern_num}'

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name


@dataclass
class PatternListModel:
    p: list[PatternModel]
    active_pattern: int = 1
    all_patterns_shown: bool = True


def default_pattern_list():
    return PatternListModel([PatternModel(1, i) for i in range(1000)])
