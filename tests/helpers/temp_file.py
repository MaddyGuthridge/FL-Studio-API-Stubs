"""
tests > helpers > temp_file

Code for temporarily moving files to the top directory
"""
import pathlib
from typing import Optional


class TemporaryFile:
    """
    A context manager that temporarily copies a file into the current working
    directory in order to test code that expects that file to be there.
    """
    def __init__(self, file: str, dest: Optional[str] = None) -> None:
        self.__file = pathlib.Path(file)
        if dest is None:
            dest = self.__file.name
        self.__dest = pathlib.Path.cwd().joinpath(dest)

    def __enter__(self):
        if self.__dest.exists():
            raise RuntimeError(
                f"Failed to create temporary file at '{self.__dest}'"
                f" - file already exists"
            )
        self.__dest.touch()
        self.__dest.write_text(self.__file.read_text())

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.__dest.unlink()
