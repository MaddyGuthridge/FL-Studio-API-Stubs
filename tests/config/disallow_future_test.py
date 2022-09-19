"""
tests > config > disallow_future_test

Tests to check that it is impossible to call a function from the future
"""
import device
import channels
import pytest
from fl_model import resetState
from fl_model.helpers import file_from_here
from fl_model.exceptions import FlCallFutureError
from tests.helpers.temp_file import TemporaryFile

fileFromHere = file_from_here.generate(__file__)


def test_raises():
    """
    Do we get the expected error
    """
    with TemporaryFile(
        fileFromHere("old_target.json"),
        "fl_config.json"
    ):
        resetState()
        with pytest.raises(FlCallFutureError):
            device.getMasterSync()


def test_exact_added():
    """
    Can we still call functions that were added in this exact version
    """
    with TemporaryFile(
        fileFromHere("old_target.json"),
        "fl_config.json"
    ):
        resetState()
        channels.getActivityLevel(0)
