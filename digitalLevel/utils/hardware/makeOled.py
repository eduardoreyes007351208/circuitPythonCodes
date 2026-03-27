# import libraries
from adafruit_ssd1306 import SSD1306_I2C


# init makeOled funtion
def makeOled(i2c):
    oled = SSD1306_I2C(128, 64, i2c)

    return oled
