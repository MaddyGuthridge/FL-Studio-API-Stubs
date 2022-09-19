"""
tests > config > disallow_deprecated_test

Tests that we get errors when we try to call deprecated functions
"""
import general
import channels
import device
import pytest
from fl_model import resetState
from fl_model.helpers import file_from_here
from fl_model.exceptions import FlCallDeprecatedError
from tests.helpers.temp_file import TemporaryFile

fileFromHere = file_from_here.generate(__file__)


@pytest.mark.parametrize(
    ['func', 'params'],
    [
        (channels.processRECEvent, (0, 0, 0)),
        (device.sendMsgGeneric, (0, "msg", "last_msg")),
        (general.restoreUndo, tuple()),
        (general.restoreUndoLevel, (0,)),
    ]
)
def test_disallow_deprecated_raises(func, params):
    """
    Do we get an error when calling a deprecated function if the setting to
    disallow it is enabled?
    """
    with TemporaryFile(
        fileFromHere("disallow_deprecated.json"),
        "fl_config.json"
    ):
        resetState()
        with pytest.raises(FlCallDeprecatedError):
            func(*params)


def test_old_target_does_not_raise():
    """
    When targeting an old version of the API do we not get warnings when
    calling deprecated functions?
    """
    with TemporaryFile(
        fileFromHere("disallow_deprecated_old_target.json"),
        "fl_config.json"
    ):
        resetState()
        device.sendMsgGeneric(0, "msg", "last_msg")


def test_old_target_raises_for_even_older_deprecations():
    """
    When targeting an old version of the API do we get warnings when calling
    functions that were deprecated even then?
    """
    with TemporaryFile(
        fileFromHere("disallow_deprecated_old_target.json"),
        "fl_config.json"
    ):
        resetState()
        with pytest.raises(FlCallDeprecatedError):
            channels.processRECEvent(0, 0, 0)
