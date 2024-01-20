"""
# Scripts / Check stubs against FL Studio

Check to ensure that the stub code completely covers all functions in FL
Studio's library.
"""
import importlib
import inspect
from typing import Optional
import flapi
from jestspectation import Equals


MODULES = [
    "arrangement",
    "channels",
    "device",
    "general",
    "launchMapPages",
    # "midi",
    "mixer",
    "patterns",
    "playlist",
    "plugins",
    "screen",
    "transport",
    "ui",
    # "utils",
]


LibraryItems = dict[str, list[str]]


def filter_module_items(items: list[str]) -> list[str]:
    """
    Filter items such that we only include the relevant ones
    """
    return list(filter(
        lambda name: not name.startswith('_'),
        items,
    ))


def generate_from_stubs(modules: list[str]) -> 'LibraryItems':
    """
    Generate collection of all items in the stub code
    """
    items = {}
    for mod in modules:
        items[mod] = filter_module_items(dir(importlib.import_module(mod)))

    return items


def generate_from_fl_studio(modules: list[str]) -> LibraryItems:
    """
    Generate collection of all items in FL Studio
    """

    # Connect to FL Studio
    if not flapi.enable():
        if not flapi.init():
            print("Couldn't connect to FL Studio")
            exit(1)

    flapi.fl_exec("import importlib")
    flapi.fl_exec(inspect.getsource(filter_module_items))
    flapi.fl_exec(inspect.getsource(generate_from_stubs))

    return flapi.fl_eval(f"generate_from_stubs({modules})")

    items = {}
    for mod in modules:
        # flapi.fl_exec(f"import {mod}")
        items[mod] = filter_module_items(flapi.fl_eval(f"dir({mod})"))

    return items


def diff(stubs: LibraryItems, fl: LibraryItems) -> Optional[str]:
    eq = Equals(fl)
    if eq == stubs:
        return None
    else:
        return "\n".join(eq.get_diff(stubs, False))


def main():
    stubs = generate_from_stubs(MODULES)
    fl = generate_from_fl_studio(MODULES)
    if (difference := diff(stubs, fl)) is not None:
        print("Stub code not same as FL Studio libraries")
        print(difference)
        exit(1)
    else:
        print("Stub code matches FL Studio libraries")


if __name__ == '__main__':
    main()
