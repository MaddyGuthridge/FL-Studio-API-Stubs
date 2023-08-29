from fl_model.decorators import since


@since(22)
def navigateBrowser(direction: int, shiftHeld: bool, /) -> str:
    """
    Navigates through the browser. `direction` can be 0 for previous
    or > 0 for next.

    Shift held will cause the browser item to expand/open  if it's a
    folder/collection ie Node Type <= -100. # similar to keyboard nav

    ## Args:
    * `direction` (`int`):
            * `40`: previous item
            * `41`: next item

    * `shiftHeld` (`bool`): whether to expand the selected item if it is a
      folder.

    ## WARNING:
    * This function's behavior changed between API version 20 and 21
    * This doesn't seem to work very reliably, at least on my machine

    ## Returns:
    * `str`: the name of the newly selected item in the browser

    Included since API Version 22
    """
    return ""


@since(22)
def navigateBrowserTabs(direction: int, /) -> str:
    """
    Navigates between browser tabs, returning the name of the newly selected
    tab.

    The direction should be one of the MIDI FPT direction constants.

    ## Args:
    * `direction` (`int`): one of:
            * `midi.FPT_Left` (`42`): change tabs left
            * `midi.FPT_Right` (`43`): change tabs right
            * any other value: navigate to first tab

    ## Returns:
    * `str`: name of the newly selected tab

    Included since API Version 22
    """
    return ""


@since(20)
def previewBrowserMenuItem():
    """
    Preview the highlighted item in the browser

    This will play a selected audio clip

    Included since API Version 20
    """


@since(20)
def selectBrowserMenuItem():
    """
    Selects the currently highlighted browser menu item, which is the
    equivalent of clicking it.

    ## WARNING:
    * This function appears to open the File menu, rather than navigating the
      browser.

    Included since API Version 20
    """


@since(20)
def getFocusedNodeCaption() -> str:
    """
    Returns the filename associated with the currently selected item in the
    browser

    ## Returns:
    * `str`: node caption

    Included since API Version 20
    """
    return ""


@since(20)
def getFocusedNodeFileType() -> int:
    """
    Returns a value based on the type of the selected file in the browser

    ## Returns:
    * `int`: One of the file type constants represented in the FL Studio
      constants.

    Refer to Image-Line's [official documentation](https://www.image-line.com/fl-studio-learning/fl-studio-beta-online-manual/html/midi_scripting.htm#BrowserFileTypes)

    Included since API Version 20
    """
    return 0


@since(20)
def isBrowserAutoHide() -> bool:
    """
    Returns whether the browser is set to auto-hide

    ## WARNING:
    * This function has no official documentation

    ## Returns:
    * `bool`: auto-hide

    Included since API Version 20
    """
    return False


@since(20)
def setBrowserAutoHide(value: int, /):
    """
    Toggle whether the browser is set to auto-hide

    ## WARNING:
    * This function has no official documentation

    ## Args:
    * `value` (`int`): whether the browser should auto-hide (`1`) or not (`0`)

    Included since API Version 20
    """
