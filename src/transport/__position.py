"""
transport > position

Dynamic state of transport
"""
import midi


def start() -> None:
    """Start or pause playback (play/pause)

    Included since API version 1
    """


def stop() -> None:
    """Stop playback

    Included since API version 1
    """


def isPlaying() -> bool:
    """Returns `True` if playback is currently occurring.

    ## Returns:
     * `bool`: whether playback is active

    Included since API version 1
    """
    return False


def record() -> None:
    """Toggles recording

    Included since API version 1
    """


def isRecording() -> bool:
    """Returns whether recording is enabled

    ## Returns:
     * `bool`: whether recording is enabled

    Included since API version 1
    """
    return False


def getLoopMode() -> int:
    """Returns the current looping mode

    ## Returns:
     * `int`: looping mode:
          * `0`: Pattern

          * `1`: Song

    Included since API version 1
    """
    return 0


def setLoopMode() -> None:
    """Toggles the looping mode between pattern and song

    Included since API version 1
    """


def globalTransport(
    command: int,
    value: int,
    pmeflags: int = midi.PME_System,
    flags=midi.GT_All
) -> int:
    """Used as a generic way to run transport commands if a specific function
    doesn't exist for it.

    ## WARNING:
    * It is not recommended to use this function if a dedicated
      function is available for it. Its usage can make code difficult to read and
      comprehend. Almost all functionality provided by this function can be done
      more easily and cleanly by using the dedicated functions.

    * Some commands will echo keypresses (such as `FPT_F1`), meaning they
      can affect windows outside FL Studio. Make sure you test your code
      thoroughly if you decide to use this function.

    ## Args:
    * `command` (`int`): command to execute, refer to
      [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#globalTransportCommands)

    * `value` (`int`): ???

    * `pmeflags` (`int`, optional): current PME Flags. Defaults to
      `midi.PME_System`.

    * `flags` (`int`, optional): ??? Refer to
      [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#globalTransportFlags)

    ## Returns:
    * `int`: ???

    Included since API version 1
    """
    return 0
