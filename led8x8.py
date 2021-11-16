from typing import Pattern
from shifter import Shifter
import time


class LED8x8:

    columnDataPin, rowDataPin, latchPin, clockPin = 23, 21, 24, 25
    pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]
    rowsern = [0b10000000, 0b01000000, 0b00100000, 0b00010000, 0b00001000, 0b00000100, 0b00000010, 0b00000001]

    def __init__(self, columnDataPin, rowDataPin, latchPin, clockPin):
        self.shifter = Shifter(columnDataPin, rowDataPin, latchPin, clockPin)
        
    def display(self, num):
        self.shifter.shiftByte(LED8x8.pattern[num],LED8x8.rowsern[num])
    


theDisplay = LED8x8(LED8x8.columnDataPin, LED8x8.rowDataPin, LED8x8.latchPin, LED8x8.clockPin)

while True:
  for n in range(8):
      theDisplay.display(n)
      time.sleep(.001)