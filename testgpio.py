from pyftdi.ftdi import Ftdi
from pyftdi.gpio import (GpioAsyncController,
                         GpioSyncController,
                         GpioMpsseController)

gpio1 = GpioAsyncController()
gpio2 = GpioAsyncController()
gpio1.configure('ftdi:///1', direction=0x95)
gpio2.configure('ftdi:///2', direction=0xbb)
# later, reconfigure BD2 as input and BD7 as output
# gpio.set_direction(0x84, 0x80)

pins1 = gpio1.read()
pins1 &= ~gpio1.direction
pins2 = gpio2.read()
pins2 &= ~gpio2.direction

print("pins1:",hex(pins1));
print("pins2:",hex(pins2));

gpio1.close();
gpio2.close();
