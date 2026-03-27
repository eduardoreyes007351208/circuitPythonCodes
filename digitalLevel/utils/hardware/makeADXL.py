# import libraries
from adafruit_adxl34x import ADXL343


# init makeADXL function
def makeADXL(i2c):
    adxl = ADXL343(i2c=i2c)

    return adxl
