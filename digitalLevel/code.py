# import built in libraries
import time
import board
from busio import I2C

# import modules
from utils.hardware import makeButton, makeOled, makeADXL
from utils.display import updateDisplay, updateColors
from utils.calculations import calcAngle, calibrate

# init the buttons
sleepBtn = makeButton(board.D1)
calBtn = makeButton(board.D3)

# init i2c connection and oled/adxl
i2c = I2C(scl=board.D5, sda=board.D4)
oled = makeOled(i2c)
adxl = makeADXL(i2c)

# init global variables
globalAngle = 0
colorFill = 0
color = 1
powerVal = False

while True:

    # check for button update every cycle
    sleepBtn.update()
    calBtn.update()

    # flip powerVal if sleepBtn is pressed
    if sleepBtn.fell:
        powerVal = not powerVal
        if not powerVal:
            # blank screen if sleeping
            oled.fill(0)
            oled.show()

    if calBtn.fell:
        # capture global angle from calibration
        globalAngle = calibrate(x, y, globalAngle, oled)
    if powerVal:

        # get gravity acc from x, y, and z axis
        x, y, z = adxl.acceleration

        # get angle from live reading minus global for calibrated reading
        angl = calcAngle(x, y, globalAngle)

        if angl == 0:
            # inverse display color if perfect level
            color, colorFill = updateColors(0, 1)
        else:
            color, colorFill = updateColors(1, 0)
        # update oled screen every cycle
        updateDisplay(oled, x, y, z, abs(angl), color, colorFill)

    time.sleep(0.05)
