<h1>Distance measuring with HCSR04</h1>
</br>
</br>
Files <code>pin_hcrs04.py</code> and <code>spi_hcrs04.py</code> both contain
the single class <code>HCSR04</code>.  This has one method <code>.distance_mm()
</code>. <code>pin_hcrs04.py</code> can use any 2 pins where as <code>
spi_hcrs04.py</code> can only use pin X7 echo and X8 trigger in position 1 and
pin Y7 echo and Y8 trigger in position 2.
</br>
</br>
The HCSR04 is a 5 volt device you need to use a logic level shifter. Or you can
trigger the device with 3.3v and using a voltage divider on the echo circuit.
see http://www.raspberrypi-spy.co.uk/2012/12/ultrasonic-distance-measurement-using-python-part-1/