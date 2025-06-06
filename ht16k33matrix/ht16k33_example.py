from machine import I2C, Pin
import time

i2c = I2C(0, scl=21, sda=20, freq=400000)  # Use I2C0 on GP1 (SCL) and GP0 (SDA)
address = 0x70  # Default I2C address for HT16K33/VK16K33

# Escanear dispositivos conectados
devices = i2c.scan()

if devices:
    print("Dispositivos I2C encontrados:", devices)
else:
    print("No se detectó ningún dispositivo I2C.")

# Initialize
i2c.writeto(address, bytearray([0x21]))  # Turn on oscillator
i2c.writeto(address, bytearray([0x81]))  # Display on, no blink
i2c.writeto(address, bytearray([0xE7]))  # Brightness (0xE0 to 0xEF)

# Clear display
i2c.writeto(address, bytearray([0x00] + [0x00]*16))

# Light up a diagonal
frame = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
data = bytearray([0x00])
for val in frame:
    data.append(val)
    data.append(0x00)  # each row has 2 bytes (LSB only used here)
i2c.writeto(address, data)
