# import libraries
import math


def calcAngle(x, y, ga):
    global globalAngle
    angle = int(math.degrees(math.atan2(x, y)) - ga)
    return angle
