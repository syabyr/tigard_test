#!/usr/bin/env python3

"""Check readline feature."""

from os.path import dirname
from sys import path
from serial import serial_for_url
from pyftdi.ftdi import Ftdi

path.append(dirname(dirname(dirname(dirname(__file__)))))

#pylint: disable-msg=wrong-import-position
from pyftdi import serialext

Ftdi.show_devices()

def main():
    """Verify readline() works with PyFTDI extension."""
    serialext.touch()
    with serial_for_url('ftdi:///1', baudrate=115200) as ser:
        ser.write(b'Hello World\r\n')
        line = ser.readline()
        print(line)
        print('testdone');

if __name__ == '__main__':
    main()
