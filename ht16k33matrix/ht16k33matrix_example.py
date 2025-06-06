from machine import I2C, Pin
import time
from ht16k33matrix import Matrix8x8

# Crear I2C en GP20 (SDA) y GP21 (SCL)
i2c = I2C(0, scl=21, sda=20, freq=400000)

# Escanear dispositivos conectados
devices = i2c.scan()

if devices:
    print("Dispositivos I2C encontrados:", devices)
else:
    print("No se detectó ningún dispositivo I2C.")
    
matrix = Matrix8x8(i2c)

for _ in range(10):
    matrix.fill(1)
    matrix.show()
    time.sleep(0.05)
    matrix.fill(0)
    matrix.show()
    time.sleep(0.05)