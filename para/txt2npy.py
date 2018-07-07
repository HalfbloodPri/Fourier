import numpy as np

with open('./para/1309770.txt',"r") as inputFile:
    inputData = inputFile.read().splitlines()

length = len(inputData)
inputDataNpy = np.zeros(length)
for i in range(length):
    inputDataNpy[i] = float(inputData[i])
np.save('./para/1309770.npy',inputDataNpy)


'''
with open('./para/f.txt',"r") as fFile:
    fValue = fFile.read().splitlines()

fValueNpy = np.zeros(len(fValue))
for i in range(len(fValue)):
    fValueNpy[i] = float(fValue[i])
np.save('./para/f.npy',fValueNpy)
print(fValueNpy)
'''