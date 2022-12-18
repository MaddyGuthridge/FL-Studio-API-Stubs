# Home

## Fl Studio API Documentation

This is user-written documentation for FL Studio's Python API. It contains information on how to use the API to interact with FL Studio. As well as this, it is also available as an installable package, which allows you to write code for FL Studio with the help of smart suggestions and inline documentation. Both the online documentation and the installable package use the same definitions, meaning that they share the same detailed and helpful information.

If you wish to help contribute to this documentation, you can do so by creating a pull request to [the original repository](https://github.com/MiguelGuthridge/FL-Studio-API-Stubs).

This fork of the FL Studio API Documentation is maintained separately and provides the same information as the original, but using MkDocs instead of pdoc, you can contribute to this fork specifically by creating a pull request to [this repository](https://github.com/abbydiode/fl-studio-api-docs).

## List of modules

* `arrangement`: functions for interacting with individual arrangements,
  including markers and playlist selections.
* `channels`: functions for interacting with the channel rack and its channels.
* `device`: functions for interacting with the device hardware, as well as
  tools for managing rec events.
* `enveditor`: a module for interacting with edison, only available through its
  scripting interface.
* `fl_classes`: a non-built-in module that provides definitions for classes
  used by FL Studio. It cannot be imported during runtime.
* `fl_model`: a non-built-in module that provides an emulation of FL Studio
  which useful for testing scripts without needing to open FL Studio.
* `general`: miscellaneous functions for interacting with FL Studio.
* `launchMapPages`: functions for implementing page displays on some MIDI
  controllers.
* `midi`: a module containing constants used by the rest of the API.
* `mixer`: functions for interacting with the mixer and its tracks.
* `patterns`: functions for interacting with patterns.
* `playlist`: functions for interacting with the playlist.
* `plugins`: functions for interacting with plugins on the channel rack and
  mixer.
* `transport`: functions for interacting with FL Studio's playback and
  recording systems.
* `ui`: functions for interacting with FL Studio's user interface.
* `utils`: utility functions and classes. Note that a lot of code in this
  module is buggy and should be avoided.
