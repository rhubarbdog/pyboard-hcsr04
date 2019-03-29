# HCSR04 distance measurement
# Author  - Phil Hall
#         - https://github.com/rhubarbdog
# License - MIT 2019 see file LICENSE in this repository

import machine
import time

class HCSR04():
    def __init__(self, trigger, echo):
        self.trig = machine.Pin(trigger, machine.Pin.OUT)
        self.echo = machine.Pin(echo, machine.Pin.IN, machine.Pin.PULL_DOWN)
        self.trig.value(0)
        
    def distance_mm(self):
        times_up = time.ticks_add(time.ticks_us(), 10)
        self.trig.value(1)
        while time.ticks_diff(times_up, time.ticks_us()) > 0:
            pass
        self.trig.value(0)

        pulse = machine.time_pulse_us(self.echo, 1, 2000000)
        if pulse > 0:
            pulse = (pulse * 340) / 2000
            
        return pulse
        
