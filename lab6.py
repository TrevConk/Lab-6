import time
from led8x8 import LED8x8

columnDataPin, rowDataPin, latchPin, clockPin = 23, 21, 24, 25

currentDisplay = LED8x8(columnDataPin, rowDataPin, latchPin, clockPin)

try:
    while True:
        for row in range(8):
            currentDisplay.display(row)
            print(row)
            time.sleep(.4)
except Exception as e:
    print(e)