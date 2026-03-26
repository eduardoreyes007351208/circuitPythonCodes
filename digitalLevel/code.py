import time
import math
import board
import digitalio
import busio
import adafruit_ssd1306
import adafruit_adxl34x
from adafruit_debouncer import Debouncer

sw = digitalio.DigitalInOut(board.D1)
sw.direction = digitalio.Direction.INPUT
sw.pull = digitalio.Pull.UP
button = Debouncer(sw)

i2c = busio.I2C(scl=board.D5, sda=board.D4)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
accel = adafruit_adxl34x.ADXL343(i2c)

def centerWord1(ct):
    half = 128/2
    halfW = (len(ct)*6)/2
    return half - halfW
def centerWord2(ct):
    half = 128/2
    halfW = (len(ct)*12)/2
    return half-halfW

def updateDisplay(x, y, z, a):
    oled.fill(0)
    oled.text(f"X: {x}", int(centerWord1(f"X: {x}")), 0, 1)
    oled.text(f"Y: {y}", int(centerWord1(f"Y: {y}")), 8, 1)
    oled.text(f"Z: {z}", int(centerWord1(f"Z: {z}")), 16, 1)
    oled.text(f"Angle:{a}", int(centerWord2(f"Angle:{a}°")), 40, 1, size=2)
    oled.show()

def calcAngle(x, y, z):
    angle = int(math.degrees(math.atan2(x, y)))
    return angle

powerVal = False

while True:
    
    button.update()
    
    if button.fell:
        powerVal = not powerVal
        if not powerVal:
            oled.fill(0)
            oled.show()
    
    if powerVal:
    
        x, y, z = accel.acceleration
    
        angl = calcAngle(x, y, z)
        updateDisplay(x, y, z, abs(angl))
    
    time.sleep(0.05)
        
    