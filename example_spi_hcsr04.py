from spi_hcsr04 import HCSR04
import time

sonar=HCSR04()
while True:
    print('%.1f cm' % (sonar.distance_mm()/10))
    time.sleep(1)
