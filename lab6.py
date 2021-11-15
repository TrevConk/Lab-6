import time
from led8x8 import LED8x8

columnDataPin, rowDataPin, latchPin, clockPin = 23, 21, 24, 25

currentDisplay = LED8x8(columnDataPin, rowDataPin, latchPin, clockPin)

try:
    while True:
        for row in range(8):
            currentDisplay.display(row)
            #time.sleep(.01)
            print(row)
except Exception as e:
    print(e)