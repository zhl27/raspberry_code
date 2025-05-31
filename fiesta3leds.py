from machine import Pin
import utime
from temp_interna import print_temp_interna

led1 =Pin(28,Pin.OUT)
led2 =Pin(27,Pin.OUT)
led3 =Pin(26,Pin.OUT)
 
delay = .5

def on_for(leds, time):
    utime.sleep(time/2)
    for led in leds:
        led.value(1)
    utime.sleep(time)
    for led in leds:
        led.value(0)

while True:
    for _ in range(3):
        on_for({led1}, .1)
        on_for({led2}, .08)
        on_for({led3}, .08)
        on_for({led2}, .08)
    for _ in range(3):
        on_for({led1, led2, led3}, .8)
    
    print_temp_interna()
    
        
