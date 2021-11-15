from typing import Pattern
from shifter import Shifter
import time


class LED8x8:

    pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]
    rows = [0b1000000, 0b01000000, 0b00100000, 0b00010000, 0b00001000, 0b00000100, 0b00000010, 0b00000001]

    def __init__(self, columnData, rowData, latch, clock):
        self.shifterColumn = Shifter(columnData, latch, clock)
        self.shifterRow = Shifter(rowData, latch, clock)
        
    def display(self, row):
        self.shifterColumn.shiftByte(LED8x8.rows[row])
        self.shifterColumn.shiftByte(LED8x8.pattern[row])
        print(pattern[row])


