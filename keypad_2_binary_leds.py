from machine import Pin
import time

import keypad
from temp_interna import print_temp_interna
from led_party import on, off, all_off, all_on, leds_simultaneous_blink_dance, leds_alternate_dance, leds_sequence_dance, leds_sequence_blink_dance, leds_ping_pong_dance, leds_display_int_as_binary, test_leds

leds = [
    Pin(18,Pin.OUT),
    Pin(19,Pin.OUT),
    Pin(20,Pin.OUT),
    Pin(21,Pin.OUT),
    Pin(22,Pin.OUT),
    Pin(26,Pin.OUT),
    Pin(27,Pin.OUT),
    Pin(28,Pin.OUT),
]

if __name__ == "__main__":
    all_off(leds)
    
    test_leds(leds)
    
    print(f"Ready for input. Enter a number on the keypad. Press '#' to confirm")

    number_buffer = []
    while True:
        res = keypad.scan_keypad()
        if (res != None):
            if res.isdigit():
                print(f"Pressed: {res}")
                number_buffer += res
            elif res == '#':
                if not number_buffer:
                    print("Enter valid number. Try again.")
                    continue
                number = int("".join(number_buffer))
                            
                if number > 255:
                    print("Enter a number between 0 and 255. Try again.")
                    continue

                print(f"Number confirmed: {number}")
                leds_display_int_as_binary(leds, number)
                number_buffer.clear()
            
        time.sleep(0.3)







