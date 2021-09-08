"""User Interface Module (FL Studio built-in)

Allows you to control and interact with FL Studio's UI.

HELP WANTED:
 * What do the return values mean?
"""

def jog(value: int) -> int:
    """Jog control. Used to map a jog wheel to selections.

    Args:
     * `value` (`int`): delta value (increment), for example
            * `1`: next
            * `-1`: previous
        
    Returns:
     * `int`: ?
    """

def jog2(value: int) -> int:
    """Alternate jog control. Used to map a jog wheel to relocate.

    Args:
     * `value` (`int`): delta value (increment), for example
            * `1`: next
            * `-1`: previous
        
    Returns:
     * `int`: ?
    """

def strip(value: int) -> int:
    """Used by touch-sensitive strip controls.
    
    HELP WANTED: What does this apply to?

    Args:
     * `value` (`int`): ???

    Returns:
     * `int`: ?
    """

def stripJog(value: int) -> int:
    """Touch-sensitive strip in jog mode.

    Args:
     * `value` (`int`): delta value (increment)

    Returns:
     * `int`: ?
    """

def stripHold(value: int) -> int:
    """Touch-sensitive strip in hold mode

    Args:
     * `value` (`int`):
            * `0`: release
            * `1`: 1-finger centred mode
            * `2`: 2-fingers centred mode
            * `-1`: 1-finger jog mode
            * `-2`: 2-finger jog mode

    Returns:
     * `int`: ?
    """

def previous() -> int:
    """Select to previous control:
     * in mixer: select previous track
     * in channel rack: select previous channel
     * in browser: scroll to previous item
     * in plugin: switch to previous preset

    Returns:
     * `int`: ?
    """

def previous() -> int:
    """Select to previous control:
     * in mixer: select previous track
     * in channel rack: select previous channel
     * in browser: scroll to previous item
     * in plugin: switch to previous preset

    Returns:
     * `int`: ?
    """

def next() -> int:
    """Select to next control:
     * in mixer: select next track
     * in channel rack: select next channel
     * in browser: scroll to next item
     * in plugin: switch to next preset

    Returns:
     * `int`: ?
    """

def moveJog(value: int) -> int:
    """Used to relocate items with a jog control.
    
    HELP WANTED: How does this differ from `jog2()`?

    Args:
     * `value` (`int`): delta value (increment)

    Returns:
     * `int`: ?
    """

def up(value:int=1) -> int:
    """Generic up control.

    Args:
     * `value` (`int`, optional): ???. Defaults to 1.

    Returns:
     * `int`: ?
    """

def down(value:int=1) -> int:
    """Generic down control.

    Args:
     * `value` (`int`, optional): ???. Defaults to 1.

    Returns:
     * `int`: ?
    """

def left(value:int=1) -> int:
    """Generic left control.

    Args:
     * `value` (`int`, optional): ???. Defaults to 1.

    Returns:
     * `int`: ?
    """

def right(value:int=1) -> int:
    """Generic right control.

    Args:
     * `value` (`int`, optional): ???. Defaults to 1.

    Returns:
     * `int`: ?
    """

def horZoom(value: int) -> int:
    """Zoom horizontally by `value`.

    Args:
     * `value` (`int`): amount to zoom by. Negative zooms out, positive zooms in.
        Larger magnitudes zoom more, but the scale doesn't seem consistent.

    Returns:
     * `int`: ?
    """

def verZoom(value: int) -> int:
    """Zoom vertically by `value`.

    Args:
     * `value` (`int`): amount to zoom by. Negative zooms out, positive zooms in.
        Larger magnitudes zoom more, but the scale doesn't seem consistent.

    Returns:
     * `int`: ?
    """

def snapOnOff() -> int:
    """Toggle whether snapping is enabled globally.

    Returns:
     * `int`: ?
    """

def cut() -> int:
    """Cut the selection.
    
    WARNING: This function echos the hotkey to cut, and thus will affect
    programs outside of FL Studio. Use with caution.

    Returns:
     * `int`: ?
    """

def copy() -> int:
    """Copy the selection.
    
    WARNING: This function echos the hotkey to copy, and thus will affect
    programs outside of FL Studio. Use with caution.

    Returns:
     * `int`: ?
    """

def paste() -> int:
    """Paste the selection.
    
    WARNING: This function echos the hotkey to paste, and thus will affect
    programs outside of FL Studio. Use with caution.

    Returns:
     * `int`: ?
    """

def insert() -> int:
    """Press the insert key.
    
    WARNING: This function echos the insert key, and thus will affect
    programs outside of FL Studio. Use with caution.

    Returns:
     * `int`: ?
    """

def delete() -> int:
    """Press the delete key.
    
    WARNING: This function echos the delete key, and thus will affect
    programs outside of FL Studio. Use with caution.

    Returns:
     * `int`: ?
    """

def enter() -> int:
    """Press the enter key.
    
    WARNING: This function echos the enter key, and thus will affect
    programs outside of FL Studio. Use with caution.

    Returns:
     * `int`: ?
    """

def escape() -> int:
    """Press the escape key.
    
    WARNING: This function echos the escape key, and thus will affect
    programs outside of FL Studio. Use with caution.

    Returns:
     * `int`: ?
    """

def yes() -> int:
    """Press the y key.
    
    WARNING: This function echos the y key, and thus will affect
    programs outside of FL Studio. Use with caution.

    Returns:
     * `int`: ?
    """

def no() -> int:
    """Press the n key.
    
    WARNING: This function echos the n key, and thus will affect
    programs outside of FL Studio. Use with caution.

    NOTE: This function is listed in the official documentation as `not`, 
    however this is incorrect, and will result in a syntax error since
    overriding core keywords (such as `if`, `def` and `not`) is not allowed. The
    function is actually named `no`, which is how this documentation lists it.

    Returns:
     * `int`: ?
    """

def getHintMsg() -> str:
    """Returns the current message in FL Studio's hint panel.

    Returns:
     * `str`: hint
    """

def setHintMessage(msg: str) -> None:
    """Sets the current hint message in FL Studio's hint panel to `msg`.

    Args:
     * `msg` (`str`): new message
    """

def getHintValue(value: int, max: int) -> str:
    """Returns hint for `value`.
    
    HELP WANTED: What does this do?

    Args:
     * `value` (`int`): ???
     * `max` (`int`): ???

    Returns:
     * `str`: hint for `value`
    """

def getTimeDispMin() -> bool:
    """Returns `True` when the song position panel is displaying time, rather
    than bar and beat.

    Returns:
     * `bool`: whether song position is displaying time.
    """

def setTimeDispMin() -> None:
    """Toggles whether the song position panel is displaying time or bar and 
    beat.
    """

def getVisible(index: int) -> bool:
    """Returns whether an FL Studio window is visible.

    Args:
     * `index` (`int`): window index:
            * `widMixer` (`0`): Mixer
            * `widChannelRack` (`1`): Channel Rack
            * `widPlaylist` (`2`): Playlist
            * `widPianoRoll` (`3`): Piano Roll
            * `widBrowser` (`4`): Browser

    Returns:
     * `bool`: whether it is visible
    """

def showWindow(index: int) -> None:
    """Shows an FL Studio window specified by `index`.

    Args:
     * `index` (`int`): window index:
            * `widMixer` (`0`): Mixer
            * `widChannelRack` (`1`): Channel Rack
            * `widPlaylist` (`2`): Playlist
            * `widPianoRoll` (`3`): Piano Roll
            * `widBrowser` (`4`): Browser
    """

def hideWindow(index: int) -> None:
    """Hides an FL Studio window specified by `index`.

    Args:
     * `index` (`int`): window index:
            * `widMixer` (`0`): Mixer
            * `widChannelRack` (`1`): Channel Rack
            * `widPlaylist` (`2`): Playlist
            * `widPianoRoll` (`3`): Piano Roll
            * `widBrowser` (`4`): Browser
    """

def getFocused(index: int) -> bool:
    """Returns whether an FL Studio window is focused (meaning it is the
    currently selected Window in FL Studio). 
    
    NOTE: this doesn't necessarily mean that it is the currently selected window
    in the host operating system, so functions that rely on keypress emulation 
    (such as `ui.copy()`) may not work as intended, even if this returns `True`.
    
    Args:
     * `index` (`int`): window index:
            * `widMixer` (`0`): Mixer
            * `widChannelRack` (`1`): Channel Rack
            * `widPlaylist` (`2`): Playlist
            * `widPianoRoll` (`3`): Piano Roll
            * `widBrowser` (`4`): Browser
            * `widPlugin` (`5`): Plugin Window (note that this constant is only
              usable in this particular function).

    Returns:
     * `bool`: whether it is visible
    """

def setFocused(index: int) -> Note:
    """Sets which FL Studio window should be focused (meaning it is the
    currently selected Window in FL Studio). 
    
    NOTE: this doesn't necessarily mean that it will be the currently selected 
    window in the host operating system, so functions that rely on keypress 
    emulation (such as `ui.copy()`) may not work as intended, even after calling
    this function.
    
    Args:
     * `index` (`int`): window index:
            * `widMixer` (`0`): Mixer
            * `widChannelRack` (`1`): Channel Rack
            * `widPlaylist` (`2`): Playlist
            * `widPianoRoll` (`3`): Piano Roll
            * `widBrowser` (`4`): Browser
    """
