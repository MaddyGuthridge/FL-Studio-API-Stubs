"""
tests > device > sync

Tests for master sync
"""
from device import getMasterSync, setMasterSync


def test_disabled_by_default():
    assert not getMasterSync()


def test_set_master_sync():
    setMasterSync(True)
    assert getMasterSync()
    setMasterSync(False)
    assert not getMasterSync()
