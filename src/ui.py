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
