"""
channels > notes

Function definitions for managing notes on channels
"""
from fl_model.decorators import since
from fl_model.channels import checkGlobalIndex, checkGroupIndex


def midiNoteOn(
    indexGlobal: int,
    note: int,
    velocity: int,
    channel: int = -1,
    /,
) -> None:
    """Set a MIDI Note for the channel at `indexGlobal` (not respecting groups)

    This can be used to create extra notes (eg mapping one note to a chord).

    ## WARNING:
    * Specifying a `channel` doesn't appear to do anything

    ## Args:
    * `indexGlobal` (`int`): channel index (not respecting groups)

    * `note` (`int`): note number (0-127)

    * `velocity` (`int`): note velocity (1-127, 0 is note off)

    * `channel` (`int`, optional): MIDI channel to use. Defaults to -1.

    Included since API version 1
    """
    checkGlobalIndex(indexGlobal)
    # TODO: Maintain list of note ons for each channel


@since(9)
def quickQuantize(index: int, startOnly: int = 1, /) -> None:
    """
    Perform a quick quantize operation on the channel at index

    ## NOTE:
    * The API documentation lists this as returning a float, however it
      actually returns None, which is what is documented here.

    ## Args:
    * `index` (`int`): channel index, respecting groups

    * `startOnly` (`int`, optional): ???. Defaults to `1`.

    Included since API Version 9
    """
    checkGroupIndex(index)
