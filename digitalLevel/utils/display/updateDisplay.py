from .centerWord import centerWord
from .centerWordBig import centerWordBig


def updateDisplay(oled, x, y, z, a, color, colorFill):

    oled.fill(colorFill)
    oled.text(f"X: {x}", int(centerWord(f"X: {x}")), 0, color)
    oled.text(f"Y: {y}", int(centerWord(f"Y: {y}")), 8, color)
    oled.text(f"Z: {z}", int(centerWord(f"Z: {z}")), 16, color)
    oled.text(f"Angle:{a}", int(centerWordBig(f"Angle:{a}")), 40, color, size=2)
    oled.show()
