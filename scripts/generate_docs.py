from pathlib import Path
import shutil
from pdoc import pdoc, render  # type: ignore

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
shutil.rmtree('./pdoc')

render.configure(
    docformat='markdown',
    footer_text='FL Studio Python API Stubs',
    show_source=False,
)

print("Generating...")
pdoc(
    *['src/' + m for m in MODULES],
    output_directory=Path('./pdoc')
)
print("Done!")
