import sys
from pathlib import Path
import shutil
from pdoc import pdoc, render  # type: ignore
from pdoc.web import DocServer, open_browser

# Add source module to path
sys.path.insert(0, './src')
import general  # noqa: E402

modules = [
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
try:
    shutil.rmtree('./pdoc')
except FileNotFoundError:
    pass

render.configure(
    docformat='markdown',
    footer_text=f'FL Studio Python API Stubs (v{general.getVersion()})',
    show_source=False,
    template_directory=Path('./resources/pdoc_templates'),
)

modules = ['src/' + m for m in modules]

# Generate the docs
if len(sys.argv) == 1:
    print('Generating...')
    pdoc(
        *modules,
        output_directory=Path('./pdoc')
    )
    print('Done!')

# Start a web server
elif sys.argv[1] == 'server':
    server = DocServer(('localhost', 8080), modules)
    with server:
        url = f'http://localhost:{server.server_port}'
        print(f'pdoc server ready at {url}')
        open_browser(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print('\nGoodbye!')
            server.server_close()

# Invalid args
else:
    print(
        f'Error: unrecognized argument {sys.argv[1]} (available: `server`)',
        file=sys.stderr
    )
