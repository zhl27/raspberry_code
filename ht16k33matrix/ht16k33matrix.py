# Archivo: ht16k33matrix.py
class Matrix8x8:
    def __init__(self, i2c, address=0x70):
        self.i2c = i2c
        self.address = address
        self.buffer = bytearray(16)
        self.i2c.writeto(self.address, b'\x21')  # Activar oscilador
        self.i2c.writeto(self.address, b'\x81')  # Encender pantalla, sin parpadeo
        self.i2c.writeto(self.address, b'\xE7')  # Brillo máximo (0xE0-0xEF)

    def fill(self, val):
        for i in range(0, 16, 2):
            self.buffer[i] = 0xFF if val else 0x00
            self.buffer[i+1] = 0x00

    def show(self):
        self.i2c.writeto_mem(self.address, 0x00, self.buffer)
