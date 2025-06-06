from machine import Pin
import time
from temp_interna import print_temp_interna

G_TIME = .05

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

def on(led):
    led.value(1)

def off(led):
    led.value(0)

def all_off(leds_list: list):
    for led in leds:
        off(led)

def all_on(leds_list: list):
    for led in leds_list:
        on(led)

def leds_simultaneous_blink_dance(leds_list):
    all_off(leds_list)
    time.sleep(G_TIME)
    all_on(leds_list)
    time.sleep(G_TIME)
    all_off(leds)

def leds_alternate_dance(leds_list):
    all_off(leds_list)
    length = len(leds_list)
    all_on(leds_list[0:length:2])
    time.sleep(G_TIME)
    all_off(leds)
    all_on(leds_list[1:length:2])
    time.sleep(G_TIME)
    all_off(leds_list)

def leds_sequence_dance(leds_list):
    all_off(leds_list)
    for led in leds:
        on(led)
        time.sleep(G_TIME)
    all_off(leds_list)

def leds_sequence_blink_dance(leds_list):
    all_off(leds_list)
    for led in leds:
        on(led)
        time.sleep(G_TIME)
        off(led)
        time.sleep(G_TIME)
    all_off(leds_list)
        
def leds_ping_pong_dance(leds_list):
    all_off(leds_list)
    for led in leds:
        on(led)
        time.sleep(G_TIME)
        off(led)
        time.sleep(G_TIME/2)
    for led in leds[::-1]:
        on(led)
        time.sleep(G_TIME)
        off(led)
        time.sleep(G_TIME/2)

def leds_display_int_as_binary(leds_list, integer):
    all_off(leds_list)
    int_bin = bin(int(integer))[2:]
    for index, bit in enumerate(reversed(int_bin)):
        #print(index, bit)
        leds_list[index].value(int(bit))

def test_leds(leds_list):
    all_off(leds_list)
    print("Testing leds...")
    for _ in range(3): leds_simultaneous_blink_dance(leds)
    for _ in range(3): leds_alternate_dance(leds)
    for _ in range(3): leds_sequence_dance(leds)
    for _ in range(3): leds_sequence_blink_dance(leds)
    for _ in range(3): leds_ping_pong_dance(leds)
    for num in range(255):
        leds_display_int_as_binary(leds_list, num)
        time.sleep(G_TIME/2)
    for _ in range(3): leds_simultaneous_blink_dance(leds)
    
    all_off(leds_list)


if __name__ == "__main__":
    while True:
        test_leds(leds)