"""
ui > keyboard

Functions for emulating key-presses.
"""
from fl_model.decorators import keyEchoes


@keyEchoes()
def cut() -> int:
    """
    Cut the selection.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


@keyEchoes()
def copy() -> int:
    """
    Copy the selection.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


@keyEchoes()
def paste() -> int:
    """
    Paste the selection.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


@keyEchoes()
def insert() -> int:
    """
    Press the insert key.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


@keyEchoes()
def delete() -> int:
    """
    Press the delete key.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


@keyEchoes()
def enter() -> int:
    """
    Press the enter key.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


@keyEchoes()
def escape() -> int:
    """
    Press the escape key.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


@keyEchoes()
def yes() -> int:
    """
    Press the y key.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


@keyEchoes()
def no() -> int:
    """
    Press the n key.

    ## Returns

    * `int`: ?

    Included since API version 1.
    """
    return 0


@keyEchoes()
def up(value: int = 1) -> int:
    """
    Press the up arrow key.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args

    * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns

    * `int`: ?

    Included since API version 1, with option parameter since API version 4.
    """
    return 0


@keyEchoes()
def down(value: int = 1) -> int:
    """
    Press the down arrow key.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args

    * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns

    * `int`: ?

    Included since API version 1, with option parameter since API version 4
    """
    return 0


@keyEchoes()
def left(value: int = 1) -> int:
    """
    Press the left arrow key.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args

    * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns

    * `int`: ?

    Included since API version 1, with option parameter since API version 4
    """
    return 0


@keyEchoes()
def right(value: int = 1) -> int:
    """
    Press the right arrow key.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args

    * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns

    * `int`: ?

    Included since API version 1, with option parameter since API version 4
    """
    return 0
