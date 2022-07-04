"""
patterns > helpers

Helper functions for dealing with patterns
"""
from fl_model.consts import PATTERN_COUNT
from fl_model.exceptions import FlIndexError


def checkIndex(index: int):
    """
    Raise an FlIndexError for invalid indexes
    """
    if not 0 <= index < PATTERN_COUNT:
        raise FlIndexError()
