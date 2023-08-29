from fl_model.decorators import since


def launchAudioEditor(
    reuse: int,
    filename: str,
    index: int,
    preset: str,
    presetGUID: str,
    /,
) -> int:
    """Launches an audio editor for track at `index` and returns the state of
    the editor. Set `reuse` to true (`1`) to reuse an already loaded audio
    editor.

    ## HELP WANTED:
    * How do I get this to work? I can only get it to open an empty window.

    ## Args:
     * `reuse` (`int`): whether to reuse an already open audio editor

     * `filename` (`str`): filename to open?

     * `index` (`int`): mixer track index to open on

     * `preset` (`str`): ???

     * `presetGUID` (`str`): ???

    ## Returns:
     * `int`: ???

    Included since API version 1
    """
    return 0


@since(9)
def openEventEditor(
    eventId: int,
    mode: int,
    newWindow: int = 0,
    /,
) -> int:
    """Launches an event editor for `eventId`.

    ## HELP WANTED:
    * Yuck REC events please help me.

    ## Args:
     * `eventId` (`int`): ???

     * `mode` (`int`): Refer to [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm#openEventEditorMode)

     * `newWindow` (`int`, optional): whether to open in a new window. Defaults
       to 0.

    ## Returns:
     * `int`: ???

    Included since API version 9
    """
    return 0
