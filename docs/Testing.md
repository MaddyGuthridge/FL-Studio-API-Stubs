
# Testing using the FL MIDI Stubs

The stubs provide an extremely minimal testing framework, which can be used to
develop basic unit tests for scripts intended to run within the FL Studio
Python environment.

Note that this functionality is bare-bones and terribly designed, and is thus
subject to change without much notice.

## Managing Contexts

Within the `fl_context` module, this API has an extremely simple context
manager that can be used to determine the return values of certain function
calls. Refer to the module's documentation for a reference on how to manage
this context.
