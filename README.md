pypicoboard
===========
A library for using the PicoBoard in Python instead of Scratch.

Python2 and Python3 compatible.

Reference:  https://wiki.scratch.mit.edu/wiki/PicoBoard

github.com/drewarnett/pypicoboard

Install:

    pip install zip-url-found-on-github-pypicoboard-project-page

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
