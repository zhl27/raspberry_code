from machine import Pin, ADC
import time
#from temp_interna import print_temp_interna
from led_array import LedArray
from u103_potentiometer import Potentiometer_U103


pot = Potentiometer_U103(ADC(0))     # GP26 = ADC0

led_arr = LedArray([
    Pin(28,Pin.OUT),
    Pin(27,Pin.OUT),
    Pin(22,Pin.OUT),
    Pin(19,Pin.OUT),
    Pin(18,Pin.OUT),
], logging=True, wait_time=0.01)

def main():
    led_arr.test_leds()
    
    val_min_refresh = 0.05*Potentiometer_U103.READ_MAX_VAL
    
    prev_frac = 0 
    while True:
        val = pot.read()
        #time.sleep(0.2)
        frac = round(val/Potentiometer_U103.READ_MAX_VAL, 1)
        if abs(prev_frac - frac) < val_min_refresh:
            led_arr.display_fraction_as_levels(frac)
            print(f"Raw: {val}. frac=round({val}/{Potentiometer_U103.READ_MAX_VAL},2)={frac}")
            prev_frac = frac


if __name__ == "__main__":
    main()
    
    
    
    
    