
import sys
import pytest
from fl_model import resetState


@pytest.fixture(autouse=True)
def resetFl():
    sys.stderr.write("fixture\n")
    return resetState()
