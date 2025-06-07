from machine import Pin, PWM
import time
import math

MIN_VEL = 0
MAX_VEL = 65535

# Define motor control pins
INA = PWM(15)  # Motor forward pin
INB = PWM(14)  # Motor backward pin

# Set PWM frequency
INA.freq(1000)
INB.freq(1000)



def motor_forward(frac_speed):
    """Rotate motor clockwise at specified speed (0-65535)."""
    speed = math.floor(MAX_VEL * frac_speed)
    INA.duty_u16(speed)
    INB.duty_u16(0)

def motor_backward(frac_speed):
    """Rotate motor counterclockwise at specified speed (0-65535)."""
    speed = math.floor(MAX_VEL * frac_speed)
    INA.duty_u16(0)
    INB.duty_u16(speed)

def motor_stop():
    """Stop motor rotation."""
    INA.duty_u16(0)
    INB.duty_u16(0)

while True:
    motor_forward(1)  # Run motor forward at medium speed
    time.sleep(2)
    motor_stop()
    time.sleep(2)
    #time.sleep(1)
    
    #motor_backward(30000)  # Run motor backward at medium speed
    #time.sleep(3)
    #motor_stop()
    #time.sleep(1)