import machine
import utime
import select
import sys

led = machine.Pin(25, machine.Pin.OUT)
led.value(0)

VAL = 0.5

def usleep(time):
    utime.sleep(time)

def led_blink():
    led.value(1)
    utime.sleep(0.08)
    led.value(0)
    utime.sleep(0.1)

def loop():
    txt = input("Insert some text:")
    for char in txt:
        char_bin = bin(ord(char))[2:]
        for i in char_bin:
            if int(i) == 1:
                led.value(1)
                usleep(VAL/8)
                led.value(0)
            else:
                led.value(0)
                usleep(VAL)
                
    for i in range(10):
        led.value(1)
        usleep(VAL/20)
        led.value(0)
        usleep(VAL/20)
    

if __name__ == '__main__':
    while True: loop()
