import time
from led8x8 import LED8x8

columnDataPin, rowDataPin, latchPin, clockPin = 22, 23, 24, 25

display = LED8x8(columnDataPin, rowDataPin, latchPin, clockPin)

while True:
    for row in 8:
        display.display(row)
        time.sleep(.1)