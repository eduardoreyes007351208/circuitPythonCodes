from digitalio import DigitalInOut, Pull, Direction
from adafruit_debouncer import Debouncer


# init function to create button
def makeButton(pin):
    # assign switch to board pin
    sw = DigitalInOut(pin)
    sw.direction = Direction.INPUT
    sw.pull = Pull.UP

    # add Debouncer so holding button counts as one click
    button = Debouncer(sw)

    # return button
    return button
