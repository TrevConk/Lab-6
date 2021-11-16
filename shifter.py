import RPi.GPIO as GPIO
import time


class Shifter():
    #'Shift register class'
    def __init__(self, dataColumn, dataRow, latch, clock):
        self.dataPinColumn, self.dataPinRow, self.latchPin, self.clockPin = dataColumn, dataRow, latch, clock
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.dataPinColumn, GPIO.OUT)
        GPIO.setup(self.dataPinRow, GPIO.OUT)
        GPIO.setup(self.latchPin, GPIO.OUT, initial=0)
        GPIO.setup(self.clockPin, GPIO.OUT, initial=0)

    def ping(self, pin):  # ping the clock or latch pin
        GPIO.output(pin, 1)
        time.sleep(0)
        GPIO.output(pin, 0)

    def shiftByte(self, byteValColumn, byteValRow):  # display a given byte pattern
        for i in range(8):           # 8 bits in register
            #GPIO.output(self.dataPin, ~(byteVal & (1 << i)))  # if common anode
            GPIO.output(self.dataPinColumn, byteValColumn & (1<<i))    # if common cathode
            GPIO.output(self.dataPinRow, byteValRow & (1<<i))
            self.ping(self.clockPin)
        self.ping(self.latchPin)

