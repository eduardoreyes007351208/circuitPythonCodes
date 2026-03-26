import time
import board
import digitalio
import busio
import neopixel
from adafruit_debouncer import Debouncer
import adafruit_ssd1306

button = digitalio.DigitalInOut(board.D1)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
sw = Debouncer(button)

power = digitalio.DigitalInOut(board.NEOPIXEL_POWER)
power.direction = digitalio.Direction.OUTPUT
power.value = True  # turn on power to
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

i2c = busio.I2C(scl=board.D5, sda=board.D4)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

def centerWord1(ct):
    half = 128/2
    halfW = (len(ct)*6)/2
    return half - halfW
def centerWord2(ct):
    half = 128/2
    halfW = (len(ct)*12)/2
    return half-halfW

def updateDisplay(ct):
    oled.fill(0)
    oled.text("The LED is currently", int(centerWord1("The LED is currently")), 0, 1)
    oled.text(ct, int(centerWord2(ct)), 8, 1, size=2)
    oled.text("Press the button to", int(centerWord1("Press the button to")), 26, 1)
    oled.text("change the color", int(centerWord1("change the color")), 34, 1)
    oled.show()

updateDisplay("Red")
val = True

while True:
    sw.update()
    
    color = (255, 0, 0) if val else (0, 255, 0)
    

    pixel[0] = color

    if sw.fell:
        val = not val 
        if val:
            updateDisplay("Red")
        else:
            updateDisplay("Green")
        
        
