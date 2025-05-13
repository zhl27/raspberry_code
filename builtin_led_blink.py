import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.value(1)  # Turn LED on
    utime.sleep(0.8)  # Wait 1 second
    led.value(0)  # Turn LED off
    utime.sleep(1)  # Wait 1 second
