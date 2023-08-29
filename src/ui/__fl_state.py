

from fl_model.decorators import since


def isClosing() -> bool:
    """Returns `True` when FL Studio is closing

    ## Returns:
     * `bool`: is closing

    Included since API version 1
    """
    return False


def isMetronomeEnabled() -> bool:
    """Returns whether the metronome is enabled

    ## Returns:
     * `bool`: whether metronome is enabled

    Included since API version 1
    """
    return False


def isStartOnInputEnabled() -> bool:
    """Returns whether start on input is enabled

    ## Returns:
     * `bool`: whether start on input is enabled

    Included since API version 1
    """
    return False


def isPrecountEnabled() -> bool:
    """Returns whether precount is enabled

    ## Returns:
     * `bool`: whether precount is enabled

    Included since API version 1
    """
    return False


def isLoopRecEnabled() -> bool:
    """Returns whether loop recording is enabled

    ## Returns:
     * `bool`: whether loop recording is enabled

    Included since API version 1
    """
    return False


def getSnapMode() -> int:
    """Returns the current snap mode.

    Although the official documentation states that this takes an argument
    `value`, it does not. This stub reflects the actual behavior.

    ## Returns:
     * `int`: index in the snap mode list:
          * `0`: Line

          * `1`: Cell

          * `2`: Unused (separator)

          * `3`: None

          * `4`: 1/6 step

          * `5`: 1/4 step

          * `6`: 1/3 step

          * `7`: 1/2 step

          * `8`: Step

          * `9`: 1/6 beat

          * `10`: 1/4 beat

          * `11`: 1/3 beat

          * `12`: 1/2 beat

          * `13`: Beat

          * `14`: bar

    Included since API version 1
    """
    return 0


def snapMode(value: int, /) -> int:
    """
    Changes the snap mode, by shifting it by `value` in the list of modes.

    This can be used by controls such as jog wheels or arrow buttons to select
    a snapping mode. To select a value directly, use `setSnapMode`.

    ## Args:
     * `value` (`int`): increment (`1` for next, `-1` for previous)

    ## Returns:
     * `int`: ???

    Included since API version 1
    """
    return 0


@since(24)
def setSnapMode(value: int, /):
    """
    Set the snap mode using an absolute value.

    This can be used on a controller to have different buttons map to different
    modes. To increment or decrement the value, use `snapMode`.

    ## Args:
    * `value` (`int`): new mode - one of the values listed in `getSnapMode()`.
    """
    curr_mode = getSnapMode()
    if value < 2 and curr_mode > 2:
        value += 1
    if value > 2 and curr_mode < 2:
        value -= 1
    snapMode(value - curr_mode)


def snapOnOff() -> int:
    """Toggle whether snapping is enabled globally.

    ## Returns:
     * `int`: ?

    Included since API version 1
    """
    return 0


def getTimeDispMin() -> bool:
    """Returns `True` when the song position panel is displaying time, rather
    than bar and beat.

    ## Returns:
     * `bool`: whether song position is displaying time.

    Included since API version 1
    """
    return False


def setTimeDispMin() -> None:
    """Toggles whether the song position panel is displaying time or bar and
    beat.

    Included since API version 1
    """


def getHintMsg() -> str:
    """Returns the current message in FL Studio's hint panel.

    ## Returns:
     * `str`: hint

    Included since API version 1
    """
    return ""


def setHintMsg(msg: str, /) -> None:
    """Sets the current hint message in FL Studio's hint panel to `msg`.

    ## Args:
     * `msg` (`str`): new message

    ## Usage:

    As well as setting basic info, scripts can use a variety of icons before
    their hint messages, which can be accessed by embedding `^c` at the start
    of the string, where `c` is a character from the list below:

    * `b`: record

    * `c`: yellow smiling face

    * `d`: mouse right click

    * `e`: red sad face

    * `f`: orange left-facing triangle

    * `g`: fast-forward icon

    * `h`: exclamation point in a red circle

    * `i`: clock

    * `j`: rewind icon

    * `k`: link icon

    * `l`: midi keyboard

    * `m`: F1 (help) key icon

    * `n`: Image-Line icon

    * `r`: plugin icon

    * `s`: file icon

    * `t`: eye

    * `u`: tempo tap icon

    * `v`: left-facing triangle

    * `w`: right-facing triangle

    * `x`: pencil

    * `y`: slice tool

    * `z`: brush tool icon

    For example, to display a tempo tap message with a relevant icon, the
    following code could be used:

    ```py
    ui.setHintMsg("^uTap tempo")
    ```

    Note that these icon codes are not returned by `getHintMsg()`.

    Included since API version 1
    """


@since(20)
def showNotification(val: int, /):
    """
    Show a notification to the user, which is chosen from a set of notification
    strings. This notification appears in the hint panel, much like with
    `ui.setHintMsg()`, except with less customization. Currently there is no
    apparent way to link these to the Script output window.

    ## WARNING:
    * This function appears to cause FL Studio's scripting environment to crash
      when used under Wine on Linux

    ## Args:
    * `val` (`int`): Notification ID, the identifier of the notification string
      to send.
          * `0`: `"Now firmware is available for your MIDI device"`

          * `1`: `"New version of script is available"`

    Included since API Version 20
    """


def getHintValue(value: int, max: int, /) -> str:
    """Returns `value/max` as a percentage.

    Equivalent to:
    ```
    f"{value/max:.0%}"
    ```

    ## Args:
     * `value` (`int`): ???

     * `max` (`int`): ???

    ## Returns:
     * `str`: hint for `value`

    Included since API version 1
    """
    return f"{value/max:.0%}"


def getProgTitle() -> str:
    """Returns the title of the FL Studio window

    ## Returns:
     * `str`: program title

    Included since API version 1
    """
    return ""


def getVersion(mode: int = 4, /) -> 'str | int':
    """Returns the version number of FL Studio

    ## Args:
     * `mode` (`int`, optional):
          * `VER_Major` (`0`): Major version number (as `int`)
            Eg: `20`

          * `VER_Minor` (`1`): Minor version number (as `int`)
            Eg: `8`

          * `VER_Release` (`2`): Release version number (as `int`)
            Eg: `4`

          * `VER_Build` (`3`): Program build number (as `int`)
            Eg: `2553`

          * `VER_VersionAndEdition` (`4`): Program version and edition (as `str`).
            Eg: `"Producer Edition v20.8.4 [build 2553]"`

          * `VER_FillVersionAndEdition` (`5`): Full version and edition (as `str`).
            Eg: `"Producer Edition v20.8.4 [build 2553] - Signature Bundle - 64Bit"`

          * `VER_ArchAndBuild` (`6`): Architecture and build number?

    Included since API version 1, with mode parameter since API version 7
    """
    return 0


@since(28)
def getStepEditMode() -> bool:
    """
    Returns the value of the "step edit mode" within FL Studio.

    ## Returns:
    * `bool`: `True` if step editing is enabled, else `False`

    Included since API Version 28
    """
    return False


@since(28)
def setStepEditMode(newValue: bool, /):
    """
    Sets the value of the "step edit mode" within FL Studio.

    ## Args:
    * `newValue` (`bool`): `True` if step editing should be enabled, else
      `False`

    Included since API Version 28
    """
    return False
