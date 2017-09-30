pypicoboard
===========
Python library for using the Scratch PicoBoard.  Scratch has built in support
for the PicoBoard.  More information about the PicoBoard may be found here:

    https://wiki.scratch.mit.edu/wiki/PicoBoard

Project page:

    https://github.com/drewarnett/pypicoboard

To install:

    pip install https://github.com/drewarnett/pypicoboard/archive/master.zip

Or, just grab the picoboard.py file.

Note:  this library is Python2 and Python3 compatible.

Prerequisites:

* pyserial

Example use:

    >>> from picoboard import PicoBoard
    >>> pb = PicoBoard('/dev/ttyUSB0')    # or 'COM1' or '/dev/ttyS0', etc.
    >>> readings = pb.read()
    >>> print(readings["button"])

The dictionary returned by read():

    key (channel name) - value
    A - resistance sensor A
    B - resistance sensor B
    C - resistance sensor C
    D - resistance sensor D
    button - button sensor
    light - light sensor
    slider - slider sensor
    sound - sound sensor
