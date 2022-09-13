"""
device > __fl

Communication with FL Studio
"""
from fl_model import since
from fl_classes import FlMidiMsg


def processMIDICC(eventData: FlMidiMsg) -> None:
    """Lets FL Studio process a MIDI CC message.

    ## Args:
    * `eventData` (`eventData`): FL MIDI Event to process.

    Included since API version 1
    """


@since(7)
def forwardMIDICC(message: int, mode: int = 1) -> None:
    """Forwards a MIDI CC message to the currently focused plugin.

    ## Args:
    * `message` (`int`): MIDI message to forward

    * `mode` (`int`, optional): Where to send the message:
          * `0`: Send the message to all plugins

          * `1` (default): ???

          * `2`: Send the message to the selected channels

    Included since API version 7
    """


def findEventID(controlId: int, flags: int = 0) -> int:
    """Returns eventID for controlId.

    ## HELP WANTED:
    * What does this do?

    ## Args:
     * `controlId` (`int`): ???

     * `flags` (`int`, optional): ???. Defaults to 0.

    ## Returns:
     * `int`: event ID

    Included since API version 1
    """
    return 0


def getLinkedValue(eventID: int) -> float:
    """Returns normalized value of the REC event at `eventID`. Returns `-1`
    if "there is no linked control".

    ```
    >>> channel_rec_id = channels.getRecEventId(0)
    >>> device.getLinkedValue(channel_rec_id + midi.REC_Chan_Vol)
    0.78125
    >>> device.getLinkedValue(channel_rec_id + midi.REC_Chan_Pan)
    0.5
    ```

    ## Args:
     * `eventID` (`int`): eventID

    ## Returns:
     * `float`: Current value of the controller parameter between [0.0, 1.0]

    Included since API version 1
    """
    return 0.0


@since(10)
def getLinkedValueString(eventID: int) -> str:
    """Returns text value of the REC event at `eventID`

    The text representation is formatted appropriately based on the
    REC parameter.

    ```
    >>> channel_rec_id = channels.getRecEventId(0)
    >>> device.getLinkedValueString(channel_rec_id + midi.REC_Chan_Vol)
    '-5.2 dB'
    >>> device.getLinkedValueString(channel_rec_id + midi.REC_Chan_Pan)
    'Centered'
    ```

    ## Args:
     * `eventID` (`int`): eventID

    ## Returns:
     * `str`: Parameter value string

    Included since API version 10
    """
    return ""


@since(10)
def getLinkedParamName(eventID: int) -> str:
    """Returns the parameter name of the REC event at `eventID`.

    ```
    >>> channel_rec_id = channels.getRecEventId(0)
    >>> device.getLinkedParamName(channel_rec_id + midi.REC_Chan_Vol)
    'Channel volume'
    >>> device.getLinkedParamName(channel_rec_id + midi.REC_Chan_Pan)
    'Channel panning'
    ```

    ## Args:
     * `eventID` (`int`): eventID

    ## Returns:
     * `str`: Parameter name

    Included since API version 10
    """
    return ""


def getLinkedInfo(eventID: int) -> int:
    """Returns information about a linked control via `eventID`.

    ## Args:
     * `eventID` (`int`): eventID

    ## Returns:
     * `int`: linked control info:
          * `-1`: no linked control

          * `Event_CantInterpolate` (`1`): ???

          * `Event_Float` (`2`): ???

          * `Event_Centered` (`4`): ???

    Included since API version 1
    """
    return 0
