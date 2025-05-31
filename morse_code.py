from machine import Pin
import utime

led = Pin(25, Pin.OUT)

def morse_dot():
    led.on()
    utime.sleep(0.2)
    led.off()
    utime.sleep(0.2)

def morse_dash():
    led.on()
    utime.sleep(0.6)
    led.off()
    utime.sleep(0.2)

def morse_letter_pause():
    utime.sleep(0.6)

# Ejemplo: S = •••, O = –––
def sos():
    for _ in range(3): morse_dot()
    morse_letter_pause()
    for _ in range(3): morse_dash()
    morse_letter_pause()
    for _ in range(3): morse_dot()

sos()
