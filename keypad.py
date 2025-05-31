from machine import Pin
import time

rows = [Pin(x, Pin.OUT) for x in (7,6,5,4)]
cols = [Pin(x, Pin.IN, Pin.PULL_UP) for x in (3,2,1,0)] 

keys = [
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*','0','#','D']
]

def scan_keypad():
    for r in range(4):
        # Set one row LOW
        rows[r].low()
        for c in range(4):
            if cols[c].value() == 0:
                return keys[r][c]
        rows[r].high()
        

if __name__ == "__main__":
    while True:
        res = scan_keypad()
        if res:
            print(f"Pressed: {res}")
        time.sleep(0.3)    

