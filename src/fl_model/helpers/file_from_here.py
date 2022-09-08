"""
fl_model > helpers > file_from_here

Code used to get the path of a file that resides in the same folder as some
calling code
"""
import pathlib
from typing import Callable


def generate(file: str) -> Callable[[str], str]:
    """
    Generate a function that returns the full path of a file that resides in
    the same folder as the file parameter

    ## Usage:
    In each module where you wish to use this functionality, you must generate
    the function as follows:

    ```py
    from fl_model.helpers import file_from_here

    fileFromHere = file_from_here.generate(__file__)
    ```

    The generated function can then be used to determine paths of files in the
    same directory as that source file

    ```py
    path_to_my_file = fileFromHere("my_file.txt")
    # path_to_my_file == "foo/bar/my_file.txt"
    ```

    ## Args:
    * `file` (`str`): the value of __file__

    ## Returns:
    * `Callable[[str], str]`: function for finding filenames
    """
    path = pathlib.Path(file).parent

    def inner(filename: str) -> str:
        return str(path.joinpath(filename))
    return inner
