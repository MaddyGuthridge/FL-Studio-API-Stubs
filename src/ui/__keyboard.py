from fl_model.decorators import keyEchoes


@keyEchoes()
def cut() -> int:
    """Cut the selection.

    ## WARNING:
    * This function echoes the hotkey to cut, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def copy() -> int:
    """Copy the selection.

    ## WARNING:
    * This function echoes the hotkey to copy, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def paste() -> int:
    """Paste the selection.

    ## WARNING:
    * This function echoes the hotkey to paste, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def insert() -> int:
    """Press the insert key.

    ## WARNING:
    * This function echoes the insert key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def delete() -> int:
    """Press the delete key.

    ## WARNING:
    * This function echoes the delete key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def enter() -> int:
    """Press the enter key.

    ## WARNING:
    * This function echoes the enter key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def escape() -> int:
    """Press the escape key.

    ## WARNING:
    * This function echoes the escape key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def yes() -> int:
    """Press the y key.

    ## WARNING:
    * This function echoes the y key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def no() -> int:
    """Press the n key.

    ## WARNING:
    * This function echoes the n key, and thus will affect
      programs outside of FL Studio. Use with caution.

    * This function is listed in the official documentation as `not`,
      however this is incorrect, and will result in a syntax error since
      overriding core keywords (such as `if`, `def` and `not`) is not allowed.
      The function is actually named `no`, which is how this documentation
      lists it.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


@keyEchoes()
def up(value: int = 1, /) -> int:
    """Generic up control.

    ## WARNING:
    * This function echoes the up arrow key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args:
     * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns:
     * `int`: ?

    Included since API version 1, with option parameter since API version 4
    """
    return 0


@keyEchoes()
def down(value: int = 1, /) -> int:
    """Generic down control.

    ## WARNING:
    * This function echoes the down arrow key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args:
     * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns:
     * `int`: ?

    Included since API version 1, with option parameter since API version 4
    """
    return 0


@keyEchoes()
def left(value: int = 1, /) -> int:
    """Generic left control.

    ## WARNING:
    * This function echoes the left arrow key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args:
     * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns:
     * `int`: ?

    Included since API version 1, with option parameter since API version 4
    """
    return 0


@keyEchoes()
def right(value: int = 1, /) -> int:
    """Generic right control.

    ## WARNING:
    * This function echoes the right arrow key, and thus will affect
      programs outside of FL Studio. Use with caution.

    ## HELP WANTED:
    * What does the `value` variable do?

    ## Args:
     * `value` (`int`, optional): ???. Defaults to 1.

    ## Returns:
     * `int`: ?

    Included since API version 1, with option parameter since API version 4
    """
    return 0
