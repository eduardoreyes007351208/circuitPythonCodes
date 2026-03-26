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

calSW = digitalio.DigitalInOut(board.D3)
calSW.direction = digitalio.Direction.INPUT
calSW.pull = digitalio.Pull.UP
calButton = Debouncer(calSW)

i2c = busio.I2C(scl=board.D5, sda=board.D4)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
accel = adafruit_adxl34x.ADXL343(i2c)

globalAngle = 0
colorFill = 0
color = 1

def centerWord1(ct):
    half = 128/2
    halfW = (len(ct)*6)/2
    return half - halfW
def centerWord2(ct):
    half = 128/2
    halfW = (len(ct)*12)/2
    return half-halfW

def updateDisplay(x, y, z, a, color, colorFill):
        
    oled.fill(colorFill)
    oled.text(f"X: {x}", int(centerWord1(f"X: {x}")), 0, color)
    oled.text(f"Y: {y}", int(centerWord1(f"Y: {y}")), 8, color)
    oled.text(f"Z: {z}", int(centerWord1(f"Z: {z}")), 16, color)
    oled.text(f"Angle:{a}", int(centerWord2(f"Angle:{a}")), 40, color, size=2)
    oled.show()

def calcAngle(x, y, z):
    global globalAngle
    angle = int(math.degrees(math.atan2(x, y)) - globalAngle)
    return angle

def calibrate(x, y):
    global globalAngle
    globalAngle = int(math.degrees(math.atan2(x, y)))
    oled.fill(1)
    oled.text("Now calibrating..", int(centerWord1("Now calibrating..")), 32, 0)
    oled.show()
    time.sleep(1.5)
    oled.fill(0)
    oled.show()
    
def updateColors(c, cf):
    global color
    global colorFill
    color = c
    colorFill = cf

powerVal = False

while True:
    
    button.update()
    calButton.update()
    
    if button.fell:
        powerVal = not powerVal
        if not powerVal:
            oled.fill(0)
            oled.show()
    if calButton.fell:
            calibrate(x, y)
    if powerVal:
    
        x, y, z = accel.acceleration
        
        
        
        angl = calcAngle(x, y, z)
        if angl == 0:
            updateColors(0, 1)
        else:
            updateColors(1, 0)
        updateDisplay(x, y, z, abs(angl), color, colorFill)
    
    time.sleep(0.05)
        
    