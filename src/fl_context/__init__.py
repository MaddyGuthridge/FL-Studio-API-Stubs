"""
fl_context

The FL Context module isn't a module that is actually used by FL Studio, but
instead can be used with unit tests for scripts using the stubs. It lets
some return values for scripts be managed.

This shouldn't be imported from your main script, but only from the test files.
"""

from .context import (
    getValue,
    resetState,
    FlContext
)
