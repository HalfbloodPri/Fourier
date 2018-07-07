import numpy as np

dataNum = 441
pianoKeyNum = 88
kValue = np.load('./para/f.npy')
realW = np.zeros((pianoKeyNum,dataNum))
imaginaryW = np.zeros((pianoKeyNum,dataNum))

for kNo in range(pianoKeyNum):
    for n in range(dataNum):
        realW[kNo][n] = np.cos(n*kValue[kNo]*2*np.pi/dataNum)
        imaginaryW[kNo][n] = -np.sin(n*kValue[kNo]*2*np.pi/dataNum)

np.save('./para/realW.npy',realW)
np.save('./para/imaginaryW.npy',imaginaryW)