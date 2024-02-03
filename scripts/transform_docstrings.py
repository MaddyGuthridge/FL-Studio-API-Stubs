"""
# Scripts / transform docstrings

Transform docstrings to make them render more nicely inline, and online.
"""
from transdoc import transform
from pathlib import Path
from shutil import rmtree, copyfile
import os


INPUT_DIR = Path("src")
OUTPUT_DIR = Path("transdoc_build")


# Rule definitions
###############################################################################


BASE_URL = "https://miguelguthridge.github.io/FL-Studio-API-Stubs"

FL_MANUAL_URL = "https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html"

NOTE_MAPPINGS = {
    "colors": """Note that colors can be split into or built from components using the
    functions provided in the [utils](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/) module.

    * [ColorToRGB()](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/#utils.ColorToRGB)

    * [RGBToColor()](https://miguelguthridge.github.io/FL-Studio-API-Stubs/utils/#utils.RGBToColor)""",

    "playlist_indexes": "Note that playlist track indexes start at 1.",
}


def docs_url_fn(function: str) -> str:
    """
    Return a markdown URL for a function within the API documentation, given
    its name.
    """
    module, fn = function.rsplit(".", 1)
    return f"[{module}.{fn}()]({BASE_URL}/{module}/#{module}.{fn})"

    # Or for the online site:
    # return f"[`{function}()`][{function}]"


def docs_url_page(text: str, location: str) -> str:
    """
    Return a markdown URL for a page in the API documentation.
    """
    return f"[{text}]({BASE_URL}/{location})"


def fl_manual_anchor(anchor: str, text: str = "FL Studio manual") -> str:
    """
    Return a markdown URL for a location anchored within the MIDI scripting
    page of FL Studio's manual.
    """
    return f"[{text}]({FL_MANUAL_URL}/midi_scripting.htm#{anchor})"


def fl_manual_page(location: str, text: str = "FL Studio manual") -> str:
    """
    Return a markdown URL for a page within FL Studio's manual.
    """
    return f"[{text}]({FL_MANUAL_URL}/{location})"


def note(name: str) -> str:
    """
    Insert a note given its name.
    """
    return NOTE_MAPPINGS[name]


TRANSDOC_RULES = [
    docs_url_fn,
    docs_url_page,
    fl_manual_anchor,
    fl_manual_page,
    note,
]


# The actual script
###############################################################################


def transform_modules():
    """
    Go through all code in the src/ directory and transform it
    """

    try:
        rmtree(OUTPUT_DIR)
    except Exception as e:
        print(e)

    for dirpath, _, filenames in os.walk(INPUT_DIR):
        # Create directory
        out_dir = OUTPUT_DIR.joinpath(Path(dirpath).relative_to(INPUT_DIR))
        out_dir.mkdir()
        for file in filenames:
            # If it's not a Python file, just copy it
            out_file = out_dir.joinpath(file)
            in_file = Path(dirpath).joinpath(file)

            if not in_file.suffix == ".py":
                copyfile(in_file, out_file)
            else:
                txt = in_file.read_text()
                out_file.write_text(transform(txt, TRANSDOC_RULES))


if __name__ == '__main__':
    transform_modules()
