import numpy as np 

ampFloat = np.load('./result/ampFloat.npy')
ampD1W1 = np.load('./result/ampD1W1.npy')

pianoKeyNum = 88
dataGroup = 2970     #55125/
errorD1W1 = 0
for i in range(dataGroup):
    print(i,'-',np.argmax(ampFloat[i]),np.argmax(ampD1W1[i]))
    if np.argmax(ampFloat[i]) != np.argmax(ampD1W1[i]):
        errorD1W1 += 1
    #for j in range(pianoKeyNum):
    #    print('   ',j,'-',ampFloat[i][j],ampD1W1[i][j])
print(errorD1W1)