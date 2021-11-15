import time
from led8x8 import LED8x8

columnDataPin, rowDataPin, latchPin, clockPin = 23, 21, 24, 25

currentDisplay = LED8x8(columnDataPin, rowDataPin, latchPin, clockPin)

try:
    while True:
        for row in range(7):
            currentDisplay.display(row)
            print(row)
except Exception as e:
    print(e)