"""
# Env Editor

This module provides editing tools for interacting with audio clips in the
Edison editor, using its integrated scripts functionality.

Main script files should use the `.pyscript` file extension, with additional
modules using standard `.py` files.
"""
__all__ = [
    'ScriptDialog',
    'Sample',
    'EditorSample',
    'Editor',
]

from .__script_dialog import ScriptDialog
from .__sample import Sample, EditorSample, Editor
