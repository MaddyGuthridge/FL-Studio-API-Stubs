"""
fl_context

NOTE: This module is not included in FL Studio's runtime, and should not be
imported from within your main script. It is intended to be used within a
testing framework in order to help validate the behaviour of MIDI scripts.

Refer to the `fl_context.context` module for help with using the stub code's
state manager tools.
"""

__all__ = [
    'getValue',
    'resetState',
    'FlContext',
]

from .context import (
    getValue,
    resetState,
    FlContext
)
