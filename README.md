# FL Studio Python API Stubs

This project contains function definitions to provide intellisense while
working on scripts for FL Studio's Python API, as well as a partially-complete
model of FL Studio, which allows for scripts to be tested outside of FL Studio.

## Online Reference

The documentation is also available as an
[online reference](https://miguelguthridge.github.io/FL-Studio-API-Stubs) if
Image-Line's own documentation isn't up to scratch.

## Installation

To avoid module conflicts with other Python projects, it is recommended that
you install this script in a virtual environment by following
[these instructions](https://docs.python.org/3/library/venv.html) in the
official Python documentation.

After activating the environment in your editor, you can install the stub
modules by running the command `pip install FL-Studio-API-Stubs` on Windows or
`pip3 install FL-Studio-API-Stubs` on MacOS or Linux.

[Video reference for installation instructions](https://youtu.be/6_KdXJIfeoI)

## Testing using the FL Studio API Stubs

This code provides a model of FL Studio which can be used to test basic
functionality of projects using the API. The [fl_model](./src/fl_model/) module can be used for
controlling the state of the model. Refer to its documentation for usage
instructions.

## The Small Print

A couple of notes regarding this repo.

### This Documentation isn't Complete

Although the stubs are mostly complete, there are a few functions where I don't
fully understand how they work. These functions have a `HELP WANTED:` label in
their documentation. If you happen to know how to use one, I'd love it if you
helped out by improving the documentation! I may also have incorrect
definitions for some functions. Please
[create an issue](https://github.com/MiguelGuthridge/FL-Studio-API-Stubs/issues/new)
if you find anything incorrect.

### Differences to the Official Implementation

A small number of tweaks have been made to these stubs in order to ease code
writing. These shouldn't have any functional impact on the behavior of the API
compared to the implied behavior from the stubs, but should help clarify some
properties of certain functions.

* Functions where parameters or returns are boolean by nature are listed as
  using a `bool` type, even though the implementation uses the integers `0` and
  `1`. This change should help to describe the context in which the functions
  should be called when writing scripts, which in a language like Python is far
  more important than the actual implementation of the functions.

## Development

Dependencies for this project are managed using
[Poetry](https://python-poetry.org/). You'll need to
[install Poetry](https://python-poetry.org/docs/#installation) to develop it.

To install the required dependencies, run `poetry install`.
