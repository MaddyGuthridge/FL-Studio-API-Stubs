"""Device Module (FL Studio built-in)

Handles the way that devices connect to FL Studio's MIDI interface, and how
scripts communicate with each other.
"""

def isAssigned() -> bool:
    """Returns `True` if an output interface is linked to the script, meaning
    that the script can send MIDI messages to that device.

    Returns:
     * `bool`: whether the device is assigned
    """

def getPortNumber() -> int:
    """Returns the port number for the input device that the script is attached
    to. If the device requires two-way communication, the output port (where 
    functions like `midiOutMsg()` send their data to) should be set to the value
    of the input port, which is returned by this function.

    Returns:
     * `int`: port number of the input device
    """

def getName() -> str:
    """Returns the name of the device.

    Returns:
     * `str`: device name
    """

def midiOutMsg(message: int, channel:int=None, data1:int=None, data2:int=None)\
    -> None:
    """Sends a MIDI message to the linked output device.
    
    This can be done either through a single combined message, or in its 
    distinct components.

    Args:
     * `message` (`int`): 
            * the MIDI message to send (if sending a complete message):
                * Lowest byte: `status`
                * Middle byte: `data 1`
                * Upper byte: `data 2`
            * OR the message type (if sending a partial MIDI message, 
              eg `0xB` for a CC message)
     * `channel` (`int`, optional): the channel to send the message to (if 
       sending a partial MIDI message)
     * `data1` (`int`, optional): the note data value for the message (if
       sending a partial MIDI message)
     * `data2` (`int`, optional): the velocity data value for the message (if
       sending a partial MIDI message)
    """

def midiOutNewMsg(slotIndex: int, message: int) -> None:
    """Sends a MIDI message to the linked output device, but only if the message
    being sent has changed compared to the last message sent with the same 
    `slotIndex`.

    Args:
     * `slotIndex` (`int`): index for MIDI message comparison
     * `message` (`int`): message to potentially send
    """

def midiOutSysex(message: str) -> None:
    """Send a SysEx message to the (linked) output device.

    Args:
     * `message` (`str`): SysEx message to send
    """

def sendMsgGeneric(id: int, message: str, lastMsg: str, offset:int=0) -> str:
    """Send a text string as a SysEx message to the linked output device.
    
    WARNING: This function is depreciated

    Args:
     * `id` (`int`): the first 6 bytes of the message (the end value `0xF7` is 
       added automatically)
     * `message` (`str`): the text to send
     * `lastMsg` (`str`): the string returned by the previous call to this
       function.
     * `offset` (`int`, optional): ???. Defaults to 0.

    Returns:
     * `str`: value to use in the next call of this function
    """

def processMIDICC(eventData) -> None:
    """Lets FL Studio process a MIDI CC message.

    Args:
        eventData (`eventData`): FL MIDI Event to process.
    """

def forwardMIDICC(message: int, mode:int=1) -> None:
    """Forwards a MIDI CC message to the currently focused plugin.

    Args:
        message (`int`): MIDI message to forward
        mode (`int`, optional): Where to send the message:
            * `0`: Send the message to all plugins
            * `1` (default): ???
            * `2`: Send the message to the selected channels
    """
