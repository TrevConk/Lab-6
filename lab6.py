import time
from led8x8 import LED8x8

columnDataPin, rowDataPin, latchPin, clockPin = 23, 21, 24, 25

display = LED8x8(columnDataPin, rowDataPin, latchPin, clockPin)

try:
    while True:
        for row in range(8):
            display.display(row)
            time.sleep(.1)
except Exception as e:
    print(e)