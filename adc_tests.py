from machine import ADC, Pin

sensor = ADC(26)  # Suponé que conectás un potenciómetro al GPIO 26

while True:
    lectura = sensor.read_u16()
    voltaje = lectura * (3.3 / 65535)
    print(f"\rVoltaje:", voltaje, end="")
