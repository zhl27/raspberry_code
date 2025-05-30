from machine import ADC
import utime

sensor_temp = ADC(4)  # Canal ADC interno
conversion_factor = 3.3 / 65535  # Pico ADC: 16 bits (0 a 65535)

while True:
    lectura = sensor_temp.read_u16()
    voltaje = lectura * conversion_factor
    temperatura_c = 27 - (voltaje - 0.706) / 0.001721  # Fórmula oficial RP2040
    print("\rTemperatura: {:.2f} °C         ".format(temperatura_c), end="")
    utime.sleep(1)