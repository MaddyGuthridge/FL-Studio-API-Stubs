
import sys
import pytest

# Add source module to path
sys.path.insert(0, './src')

from fl_model import resetState

# Reset FL Studio between tests
@pytest.fixture(autouse=True, scope="session")
def resetFl():
    resetState()
