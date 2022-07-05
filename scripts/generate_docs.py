from pathlib import Path
import os
from pdoc import pdoc, render

MODULES = [
    'arrangement',
    'channels',
    'device',
    'fl_classes',
    'fl_model',
    'general',
    'launchMapPages',
    'midi',
    'mixer',
    'patterns',
    'playlist',
    'plugins',
    'transport',
    'ui',
    'utils',
]

# Remove the old code
os.remove('./pdoc')

render.configure(
    docformat='markdown',
    footer_text='FL Studio Python API Stubs',
    show_source=False,
)

pdoc(
    *['src/' + m for m in MODULES],
    output_directory=Path('./pdoc')
)
