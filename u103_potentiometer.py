from machine import ADC, Pin
import time

class Potentiometer_U103:
    def __init__(self, adc, base_voltage):
        self.pot = adc
        self.base_voltage = base_voltage

    def read(self):
        val = self.pot.read_u16()  # Devuelve un valor entre 0 y 65535
        voltage = val * self.base_voltage / 65535  # Convierte a voltaje real (0V–3.3V)
        time.sleep(0.2)
        return (val, voltage)
    

if __name__ == "__main__":
    pot = Potentiometer_U103(ADC(26), 3.3)     # GP26 = ADC0
    while True:
        val, voltage = pot.read()
        print(f"\rRaw: {val}  |  Voltage: {voltage:.2f} V", end="           ")    