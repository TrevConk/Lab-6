from led8x8 import LED8x8
import multiprocessing
import numpy as np
import time

#pattern = [0,0,0,0,0,0,0,0]
pattern = multiprocessing.Array('i',8)
myValue = multiprocessing.Value('i')
pattern[0] = 127
pattern[1] = 255
pattern[2] = 255
pattern[3] = 255
pattern[4] = 255
pattern[5] = 255
pattern[6] = 255
pattern[7] = 255


def array2pattern(array):
    returnValues = [0,0,0,0,0,0,0,0]
    for row in range(8):
        currentVals = [1,1,1,1,1,1,1,1]
        for col in range(8):
            if row == array[0] and col == array[1]:
                currentVals[col] = 0
        #print(int("".join(str(x) for x in currentVals), 2))
        returnValues[row] = int("".join(str(x) for x in currentVals), 2)
    return returnValues

def pattern2array(array):
    #print('in pattern2array')
    for row in range(8):
        currentRow = '{0:08b}'.format(array[row])
        if '0' in currentRow:
            col = currentRow.find('0')
            return [row,col]



def randomWalk(pattern, myValue):
  while True:
    array = [0,0,0,0,0,0,0,0]
    array = pattern
    condensedArray = pattern2array(array)
    print(condensedArray)
    for i in range(2):
        if condensedArray[i] == 0:
            condensedArray[i] = condensedArray[i] + np.random.randint(0, 2)
        elif condensedArray[i] == 7:
            condensedArray[i] = condensedArray[i] + np.random.randint(-1, 1)
        else:
            condensedArray[i] = condensedArray[i] + np.random.randint(-1, 2)
    print(condensedArray)
    for i in range(8):
        pattern[i] = array2pattern(condensedArray)[i]
    print(pattern[:])
    time.sleep(.1)

#try:
#    while True:
#        pattern = randomWalk(pattern)
#        print(pattern)
#        time.sleep(1)

#except Exception as e:
#    print(e)
try:
    p = multiprocessing.Process(target=randomWalk, args=(pattern, myValue))
    p.start()
    theDisplay = LED8x8(LED8x8.columnDataPin, LED8x8.rowDataPin, LED8x8.latchPin, LED8x8.clockPin)

    while True:
        for n in range(8):
            theDisplay.display(n,pattern[n])
            time.sleep(.001)

except Exception as e:
    print(e)
    p.terminate()