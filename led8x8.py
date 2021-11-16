from typing import Pattern
from shifter import Shifter
import time


class LED8x8:

    columnDataPin, rowDataPin, latchPin, clockPin = 23, 21, 24, 25
    pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]
    rowsern = [0b10000000, 0b01000000, 0b00100000, 0b00010000, 0b00001000, 0b00000100, 0b00000010, 0b00000001]

    def __init__(self, columnData, latch, clock):
        self.shifterColumn = Shifter(columnData, latch, clock)
        
    def display(self, row):
        for n in range(len(LED8x8.pattern)):
            self.shifterColumn.shiftByte(LED8x8.pattern[row])
            self.shifterColumn.shiftByte(1 << (n))
            self.shifterColumn.latch()
        #self.shifterRow.shiftByte(0b10000000)
        #self.shifterColumn.shiftByte(0b00111100)
        print(LED8x8.pattern[row])
    


theDisplay = LED8x8()

while True:
  theDisplay.display()
  time.sleep(.001)