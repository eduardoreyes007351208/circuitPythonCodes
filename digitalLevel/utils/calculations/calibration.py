# import libraries
import math
import time
from ..display import centerWord


def calibrate(x, y, ga, oled):
    ga = int(math.degrees(math.atan2(x, y)))
    oled.fill(1)
    oled.text("Now calibrating..", int(centerWord("Now calibrating..")), 32, 0)
    oled.show()
    time.sleep(1.5)
    oled.fill(0)
    oled.show()

    return ga
