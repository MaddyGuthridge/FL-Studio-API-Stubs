"""
fl_model > util

Contains utility functions used by the rest of the script
"""


def clamp(value: float, min: float = 0, max: float = 1) -> float:
    """
    Clamps the given value to be within the range required
    """
    if value < min:
        return min
    elif value > max:
        return max
    else:
        return value
