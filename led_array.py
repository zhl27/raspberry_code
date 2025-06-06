from machine import Pin
import time

class LedArray:
    
    GLOBAL_DEFAULT_WAIT_TIME = 0.5
    
    def __init__(self, ordered_list_of_leds, wait_time=None):
        if wait_time is None:
            print(f"{__class__.__name__}: wait_time is None, defaulting to {LedArray.GLOBAL_DEFAULT_WAIT_TIME}")
            self.wait_time = LedArray.GLOBAL_DEFAULT_WAIT_TIME
        else:
            self.wait_time = wait_time
        self.leds_list = ordered_list_of_leds
        self.len = len(self.leds_list)

    def __getitem__(self, key):
        #print(f"Recibido: {key} ({type(key)})")
        return LedArray(list(self.leds_list[key]), self.wait_time)

    def __len__(self):
        return self.len
    
    def __str__(self):
        return f"LedArray({str(self.leds_list)})"
    
    def on(self, led_index):
        self.leds_list[led_index].value(1)
    def off(self, led_index):
        self.leds_list[led_index].value(0)

    def all_on(self):
        for led in self.leds_list:
            led.value(1)
#         for index in range(self.len):
#             self.on(index)
    def all_off(self):
        for led in self.leds_list:
            led.value(0)
#         for index in range(self.len):
#             self.on(index)

    def simultaneous_blink_dance(self):
        self.all_off()
        time.sleep(self.wait_time)
        self.all_on()
        time.sleep(self.wait_time)
        self.all_off()

    def alternate_dance(self):
        self.all_off()
        self[0:self.len:2].all_on()
        time.sleep(self.wait_time)
        self.all_off()
        self[1:self.len:2].all_on()
        time.sleep(self.wait_time)
        self.all_off()

    def sequence_dance(self):
        self.all_off()
        for index in range(self.len):
            self.on(index)
            time.sleep(self.wait_time)
        self.all_off()

    def sequence_blink_dance(self):
        self.all_off()
        for index in range(self.len):
            self.on(index)
            time.sleep(self.wait_time)
            self.off(index)
            time.sleep(self.wait_time)
        self.all_off()

    def ping_pong_dance(self):
        self.all_off()
        for index in range(self.len):
            self.on(index)
            time.sleep(self.wait_time)
            self.off(index)
            time.sleep(self.wait_time/2)
        for index in range(0,self.len,-1):
            self.on(index)
            time.sleep(self.wait_time)
            self.off(index)
            time.sleep(self.wait_time/2)

    def display_int_as_binary(self, integer):
        self.all_off()
        int_bin = bin(int(integer))[2:]
        for index, bit in enumerate(reversed(int_bin)):
            #print(index, bit)
            self.leds_list[index].value(int(bit))

    def test_leds(self):
        self.all_off()
        print("Testing leds...")
        for _ in range(3): self.simultaneous_blink_dance()
        for _ in range(3): self.alternate_dance()
        for _ in range(3): self.sequence_dance()
        for _ in range(3): self.sequence_blink_dance()
        for _ in range(3): self.ping_pong_dance()
        for number in range(16):
            self.display_int_as_binary(number)
            time.sleep(self.wait_time)
        for _ in range(3): self.simultaneous_blink_dance()
        self.all_off()

if __name__ == "__main__":
    
    led_arr = LedArray([
        Pin(28,Pin.OUT),
        Pin(27,Pin.OUT),
        Pin(22,Pin.OUT),
        Pin(19,Pin.OUT),
        Pin(18,Pin.OUT),
    ])
    
    print(led_arr)
    
    led_arr.test_leds()
    
    