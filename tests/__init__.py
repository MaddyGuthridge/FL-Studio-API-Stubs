
import sys
from pathlib import Path

# Add source module to path
sys.path.insert(0, './src')

# Remove "fl_config.json" from top directory if present
fl_config = Path("fl_config.json")
if fl_config.is_file():
    fl_config.unlink()
