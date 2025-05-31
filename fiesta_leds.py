from machine import Pin
import utime
from temp_interna import print_temp_interna

led1 = Pin(28,Pin.OUT)
led2 = Pin(27,Pin.OUT)
led3 = Pin(26,Pin.OUT)
led4 = Pin(22,Pin.OUT)
led5 = Pin(21,Pin.OUT)
led6 = Pin(20,Pin.OUT)

def on_for(leds, time):
    utime.sleep(time/2)
    for led in leds:
        led.value(1)
    utime.sleep(time)
    for led in leds:
        led.value(0)

def traverse():
    on_for({led1}, .1)
    on_for({led2}, .08)
    on_for({led3}, .08)
    on_for({led4}, .08)
    on_for({led5}, .08)
    on_for({led6}, .08)

def ping_pong():
    on_for({led1}, .1)
    on_for({led2}, .08)
    on_for({led3}, .08)
    on_for({led4}, .08)
    on_for({led5}, .08)
    on_for({led6}, .1)
    on_for({led5}, .08)
    on_for({led4}, .08)
    on_for({led3}, .08)
    on_for({led2}, .08) 

def on_all():
    on_for({led1, led2, led3, led4, led5, led6}, .8)

def led_dance():
    while True:
        for _ in range(3):
            traverse()
        for _ in range(3):
            on_all()
        for _ in range(3):
            ping_pong()
        for _ in range(3):
            on_all()
        
        print_temp_interna()

if __name__ == "__main__":
    led_dance()