from pin_hcsr04 import HCSR04
import time

measure = HCSR04(trigger = 'X8', echo = 'X7')

while True:
    print("%.1f cm" % (measure.distance_mm() / 10))
    time.sleep(1)
