"""
tests > config > disallow_key_echo_test

Tests for giving errors when calling functions that echo hotkeys.
"""

import pytest
import ui
import transport
from typing import Callable, Sequence
from fl_model.exceptions import FlCallKeyEchoError
from tests.helpers.temp_file import TemporaryFile
from fl_model import resetState
from fl_model.helpers import file_from_here


fileFromHere = file_from_here.generate(__file__)


NO_ARGS: Sequence[Callable] = [
    ui.copy,
    ui.cut,
    ui.delete,
    ui.down,
    ui.enter,
    ui.escape,
    ui.insert,
    ui.left,
    ui.no,
    ui.paste,
    ui.right,
    ui.up,
    ui.yes,
]


ARGS: Sequence[tuple[Callable, tuple]] = [
    (transport.globalTransport, (param, 1)) for param in [
        *range(40, 44),
        *range(50, 55),
        *range(60, 72),
        *range(80, 84),
    ]
] + [(func, tuple()) for func in NO_ARGS]  # type: ignore


@pytest.mark.parametrize(
    ['func', 'params'],
    ARGS
)
def test_raises(func, params):
    with TemporaryFile(
        fileFromHere("disallow_deprecated.json"),
        "fl_config.json"
    ):
        resetState()
        with pytest.raises(FlCallKeyEchoError):
            func(*params)
