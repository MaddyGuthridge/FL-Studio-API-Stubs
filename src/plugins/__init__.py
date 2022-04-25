"""Plugins Module (FL Studio built-in)

Handles the way that scripts communicate with and control FL Studio plugins,
including 3rd-party VST/AU plugins. The module allows scripts to get and set
parameter values for plugins on the mixer and the channel rack.

Module added in API version 8.

## NOTES:
* `index` either refers to the index of the plugin on the channel rack, or the
  index of the mixer track containing the plugin on the mixer.

* `slotIndex` refers the the mixer slot of the plugin if it is on the mixer.
  Leave this parameter empty if the plugin is on the channel rack.
"""

import midi


def isValid(index: int, slotIndex: int = -1) -> bool:
    """Returns whether there is a valid plugin at `index`/`slotIndex`.

    ## NOTE:
    * Audio samples are not considered to be plugins in FL Studio.

    ## Args:
     * `index` (`int`): index on channel rack or mixer

     * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to -1.

    ## Returns:
     * `bool`: whether there is a valid plugin at `index`.

    Included since API version 8
    """
    return False


def getPluginName(index: int, slotIndex: int = -1, userName: int = 0) -> str:
    """Returns the name of the plugin at `index`/slotIndex`. This returns the
    original plugin name if `userName` is `False`, otherwise the name of the
    plugin as set by the user.

    ## Args:
     * `index` (`int`): index on channel rack or mixer

     * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to -1.

    ## Returns:
     * `str`: plugin name

    Included since API version 8, with `userName` parameter added in API version
    12
    """
    return ""


def getParamCount(index: int, slotIndex: int = -1) -> int:
    """Returns the number of parameters that the plugin at `index`/`slotIndex`
    has.

    ## NOTE:
    * VST plugins are listed as having `4240` parameters, but not all of
      these are necessarily used by the plugin. The first `4096` are for
      parameters, then the next `128` are used for MIDI CC sends `0` to `127`.
      The final `16` are used for aftertouch for each MIDI channel.

    ## Args:
    * `index` (`int`): index on channel rack or mixer

    * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to -1.

    ## Returns:
    * `int`: number of parameters

    Included since API version 8
    """
    return 0


def getParamName(paramIndex: int, index: int, slotIndex: int = -1) -> str:
    """Returns the name of the parameter at `paramIndex` for the plugin at
    `index`/`slotIndex`.

    ## WARNING:
    * In API versions < v20, FL Studio's Python environment will crash if an
      invalid paramIndex is provided to this function.

    ## Args:
    * `paramIndex` (`int`): index of parameter

    * `index` (`int`): index of plugin on channel rack or mixer

    * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to -1.

    ## Returns:
    * `str`: name of parameter

    Included since API version 8
    """
    return ""


def getParamValue(paramIndex: int, index: int, slotIndex: int = -1) -> float:
    """Returns the value of the parameter at `paramIndex` for the plugin at
    `index`/`slotIndex`.

    ## WARNING:
    * In API versions < v20, the return values of this function for VST plugins
      seem to be very broken, often being incorrect by orders of magnitude.

    ## Args:
     * `paramIndex` (`int`): index of parameter

     * `index` (`int`): index of plugin on channel rack or mixer

     * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to -1.

    ## Returns:
     * `float`: parameter value, between `0.0` and `1.0`

    Included since API version 8
    """
    return 0.0


def setParamValue(
    value: float,
    paramIndex: int,
    index: int,
    slotIndex: int = -1
) -> None:
    """Sets the value of the parameter at `paramIndex` for the plugin at
    `index`/`slotIndex`.

    ## Args:
     * `value` (`float`): new value of parameter (between `0.0` and `1.0`)

     * `paramIndex` (`int`): index of parameter

     * `index` (`int`): index of plugin on channel rack or mixer

     * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to -1.

    Included since API version 8
    """


def getParamValueString(
    paramIndex: int,
    index: int,
    slotIndex: int = -1,
    pickupMode: int = midi.PIM_None,
) -> str:
    """Returns a string value of the parameter at `paramIndex` for the plugin at
    `index`/`slotIndex`. This function is only supported by some FL Studio
    plugins.

    ## WARNING:
    * In API versions < v20, FL Studio's Python environment will crash if an
      invalid paramIndex is provided to this function.

    ## Args:
     * `paramIndex` (`int`): index of parameter

     * `index` (`int`): index of plugin on channel rack or mixer

     * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to -1.

    ## Returns:
     * `str`: string parameter value

    Included since API version 8
    """
    return ""


def getColor(
    index: int,
    slotIndex: int = -1,
    flag: int = midi.GC_BackgroundColor
) -> int:
    """Returns various plugin colour parameter values for the plugin at
    `index`/`slotIndex`.

    ## Args:
     * `index` (`int`): index of plugin on channel rack or mixer

     * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to -1.

     * `flag` (`int`, optional): colour type to return:
          * `GC_BackgroundColor` (`0`, default): The darkest background colour
          of the plugin.

          * `GC_Semitone` (`1`): Retrieves semitone colour (in FPC, returns
            colour of drum pads).

    ## Returns:
     * `int`: colour (`0x--BBGGRR`)

    Included since API version 12
    """
    return 0


def getName(
    index: int,
    slotIndex: int = -1,
    flag: int = midi.FPN_Param,
    paramIndex: int = 0
) -> str:
    """Returns various names for parts of plugins for the plugin at
    `index`/`slotIndex`.

    ## HELP WANTED:
    * Explanation of `flag` values from `3` onwards, excluding `6`.
    * Fixing the markdown formatting here: I can't get it to behave in VS Code.

    ## Args:
     * `index` (`int`): index of plugin on channel rack or mixer

     * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to -1.

     * `flag` (`int`, optional): name type to return. Names marked with a *
       require the `paramIndex` parameter in order to work correctly.
          * `FPN_Param` (`0`, default) * : Name of plugin parameter.
              * Eg: `"Expression"`

          * `FPN_ParamValue` (`1`) * : Text value of plugin parameter.
              * Eg: `"62%"`

          * `FPN_Semitone` (`2`) * : Name of note as defined by plugin.
              * `paramIndex` should be the note number (eg `60` for middle C)

              * If note names aren't defined by the plugin, an empty string is given.

              * Eg: `"Kick"`

          * `FPN_Patch` (`3`): Name of the patch defined by plugin?

          * `FPN_VoiceLevel` (`4`) * : Name of per-voice parameter defined by plugin

          * `FPN_VoiceLevelHint` (`5`) * : Hint for per-voice parameter defined by plugin

          * `FPN_Preset` (`6`) * : For plugins that support internal presets, the name of the preset at `paramIndex`.
              * Eg: `"Dystopian lead"`

          * `FPN_OutCtrl` (`7`): For plugins that output controllers, the name of the output controller?

          * `FPN_VoiceColor` (`8`): Name of per-voice colour
              * `paramIndex` as MIDI channel?

          * `FPN_VoiceColor` (`9`): For plugins that output voices, the name of output voice
              * `paramIndex` as voice number?

     * `paramIndex` (`int`, optional): index required by requested flag (if
       necessary)

    ## Returns:
     * `str`: name of requested parameter

    Included since API version 13
    """
    return ""


def getPadInfo(
    chanIndex: int,
    slotIndex: int = -1,
    paramOption: int = 0,
    paramIndex: int = -1
) -> int:
    """
    Returns info about drum pads

    Currently only supported by FPC

    ## WARNING:
    * None of the parameters can be given as keyword arguments

    * The official documentation lists this as returning a string, but it
      actually returns an int.

    ## Args:
    * `chanIndex` (`int`): channel of plugin to check

    * `slotIndex` (`int`, optional): slot of mixer track plugin. Defaults to -1.

    * `paramOption` (`int`, optional): type of query:
          * `0`: number of pads (note: given number is one greater than there
            actually are, ie. FPC has 32 pads but 33 is returned)

          * `1`: semitone number of pad (use `paramIndex`)

          * `2`: color of pad as 0xBBGGRR (use `paramIndex`)

    * `paramIndex` (`int`, optional): drum pad number (0-indexed)

    ## Returns:
    * `int`: number of parameters, or

    * `int`: note number of pad, or

    * `int`: color of pad

    Included since API Version 19
    """
    return 0


def getPresetCount(index: int, slotIndex: int = -1) -> int:
    """Returns the number of presets available for the selected plugin.

    ## Args:
     * `index` (`int`): index of plugin on channel rack or mixer.

     * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to -1.

    Included since API version 15
    """
    return 0


def nextPreset(index: int, slotIndex: int = -1) -> None:
    """Navigate to the next preset for plugin at `index`/`slotIndex`.

    ## Args:
     * `index` (`int`): index of plugin on channel rack or mixer
     * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to -1.

    Included since API version 10
    """


def prevPreset(index: int, slotIndex: int = -1) -> None:
    """Navigate to the previous preset for plugin at `index`/`slotIndex`.

    ## Args:
     * `index` (`int`): index of plugin on channel rack or mixer

     * `slotIndex` (`int`, optional): mixer slot if on mixer. Defaults to -1.

    Included since API version 10
    """
