# Make Motors Spin
# Author: Emily Ninestein

from machine import Pin, PWM
from time import sleep

# declare pins
red1 = PWM(Pin(2))
black1 = PWM(Pin(3))
red1.freq(10)
black1.freq(10)


red2 = PWM(Pin(4))
black2 = PWM(Pin(5))
red2.freq(10)
black2.freq(10)

# turn pin on with duty cycle to make spin forward
while True:
    red1.duty_u16(20000) # range from 0 to 65535
    sleep(0.0001)
    red2.duty_u16(20000) # range from 0 to 65535
    sleep(0.0001)


# make spin backwards

# make idle
























 