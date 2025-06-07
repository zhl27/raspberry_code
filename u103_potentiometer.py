import time

class Potentiometer_U103:
    READ_MAX_VAL = 65535
    
    def __init__(self, adc, base_voltage=None):
        self.pot = adc
        self.base_voltage = base_voltage
    
    def read(self):
        time.sleep(0.2)
        val = self.pot.read_u16()  # Devuelve un valor entre 0 y 65535
        if self.base_voltage is None:
            return val
        voltage = val * self.base_voltage / Potentiometer_U103.READ_MAX_VAL  # Convierte a voltaje real (0V–3.3V)
        return (val, voltage)
    
    

if __name__ == "__main__":
    from machine import ADC, Pin
    pot = Potentiometer_U103(ADC(Pin(26)), 3.3)     # GP26 = ADC0
    print(pot)
    while True:
        val, voltage = pot.read()
        print(f"\rRaw: {val}  |  Voltage: {voltage:.2f} V", end="           ")
        
        