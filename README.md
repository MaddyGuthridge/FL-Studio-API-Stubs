# FL Studio MIDI Python API

This project contains simple stub functions to provide intellisense while
working on scripts for FL Studio's MIDI Python API.

Currently, it only provides function definitions and docstrings, but these
functions don't do anything. It is NOT a complete testing framework, and it
cannot guarantee your script will work correctly. However, it may help you to
resolve issues with incorrect function calls when interacting with the API.

# Important Note

Although the stubs are mostly complete, there are a few functions where I don't
fully understand how they work. These functions have a `HELP WANTED:` label in
their documentation. If you happen to know how to use one, I'd love it if you 
helped out by improving the documentation!

# Online Reference

The documentation is also available as an [online reference](https://miguelguthridge.github.io/FL-Midi-Stub/pdoc/src/index.html)
if Image-Line's own documentation isn't up to scratch.

# Differences to Official Implementation

A small number of tweaks have been made to these stubs in order to ease code 
writing. These shouldn't have any functional impact on the behaviour of the API
compared to the implied behaviour from the stubs, but should help clarify some
properties of certain functions.

 * Functions whose returns are boolean by nature are listed as returning a 
 `bool` type, even though the implementation returns the integers `0` and `1`.
 This change should help to describe the context in which the functions should 
 be called when writing scripts, which in a language like Python is far more 
 important than the actual implementation of the functions.

# Installation

To avoid module conflicts with other Python projects, it is recommended that 
you install this script in a virtual environment by following 
[these instructions](https://docs.python.org/3/library/venv.html) in the 
official Python documentation.

After activating the environment in your editor, you can install the stub 
modules by running the command `pip install FL-Studio-API-Stubs` on Windows or
`pip3 install FL-Studio-API-Stubs` on MacOS or Linux.
