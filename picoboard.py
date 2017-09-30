"""pypicoboard

Python library for using the Scratch PicoBoard.  Scratch has built in support
for the PicoBoard.  more information about the PicoBoard may be found here:

    https://wiki.scratch.mit.edu/wiki/PicoBoard

Project page:

    https://github.com/drewarnett/pypicoboard

Note:  this library Python2 and Python3 compatible.

Prerequisites:

* pyserial
"""

from __future__ import print_function

import struct

import serial


_SCRATCH_DATA_REQUEST = 1

_CHANNEL_NUMBERS_PER_NAME = {
    "D":  0,
    "C":  1,
    "B":  2,
    "button":  3,
    "A":  4,
    "light":  5,
    "sound":  6,
    "slider":  7
}

_CHANNEL_NAMES_PER_CHANNEL = {
    value: key for key, value in _CHANNEL_NUMBERS_PER_NAME.items()}

CHANNEL_NAMES = tuple(sorted(_CHANNEL_NUMBERS_PER_NAME.keys()))


class PicoBoard(object):
    """PicoBoard interface object

    Example use:

    >>> from picoboard import PicoBoard
    >>> pb = PicoBoard('/dev/ttyUSB0')    # or 'COM1' or '/dev/ttyS0', etc.
    >>> readings = pb.read()
    >>> print(readings["button"])
    """

    def __init__(self, serial_port):
        """connect to PicoBoard using given serial port

        UNIX example:  /dev/ttyUSB0

        MS Windows example:  COM1
        """

        self._interface = serial.Serial(serial_port, 38400, timeout=0.1)

    def read(self):
        """reads the PicoBoard sensors once and returns a readings dictionary

        key:  channel name
            A - resistance sensor A
            B - resistance sensor B
            C - resistance sensor C
            D - resistance sensor D
            button - button sensor
            light - light sensor
            slider - slider sensor
            sound - sound sensor

        value:  value from PicoBoard sensor
        """

        def readchannel():
            """read and parse once channel worth of response data"""

            data = self._interface.read(2)
            upper_byte, lower_byte = struct.unpack('>BB', data)
            assert (upper_byte >> 7) & 1 == 1
            assert (lower_byte >> 7) & 1 == 0
            channel = (upper_byte >> 3) & 0xf
            value = ((upper_byte & 0x7) << 7) | ((lower_byte & 0x7f) << 0)
            return (channel, value)

        self._interface.flushInput()
        self._interface.write(struct.pack('B', _SCRATCH_DATA_REQUEST))

        assert readchannel() == (15, 4)

        rval = dict()

        for i in range(8):
            channel, value = readchannel()
            rval[_CHANNEL_NAMES_PER_CHANNEL[channel]] = value
        return rval

# vim:  ts=4 sw=4 expandtab
