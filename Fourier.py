import numpy as np

dataNum = 441
pianoKeyNum = 88
dataGroup = 2970

##准备输入值和权值
realW = np.load('./para/realW.npy')     #pianoKeyNum*dataNum
imaginaryW = np.load('./para/imaginaryW.npy')    #pianoKeyNum*dataNum
inputData = np.load('./para/1309770.npy')
inputDataNor = None

#对输入值进行归一化
def inputNormalization():
    global inputData
    inputData = np.where(abs(inputData)<=0.001,0,inputData)
    for i in range(dataGroup):
        maxValue = max(abs(inputData[(i*dataNum):((i+1)*dataNum)].max()),abs(inputData[(i*dataNum):((i+1)*dataNum)].min()))
        if maxValue != 0:
            inputData[(i*dataNum):((i+1)*dataNum)] = inputData[(i*dataNum):((i+1)*dataNum)]/maxValue
#对输入值进行定点化
def inputInt():
    global inputDataNor
    inputDataNor = np.where(inputData<=-0.5, -1, np.where(inputData<0.5,0,inputData))
    inputDataNor = np.where(inputDataNor>=0.5, 1, inputDataNor)
#对权值进行定点化
def weightInt():
    global realW
    maxValue = realW.max()
    minValue = realW.min()
    realW = np.round((1*(realW-minValue)/(maxValue-minValue)))
    global imaginaryW
    maxValue = imaginaryW.max()
    minValue = imaginaryW.min()
    imaginaryW = np.round((1*(imaginaryW-minValue)/(maxValue-minValue)))

##先对输入进行归一化
inputNormalization()
inputInt()
weightInt()
amplitude = np.zeros((dataGroup,pianoKeyNum))
for i in range(dataGroup):
    ##计算实部幅值和虚部幅值
    realAmplitude = np.dot(realW,inputDataNor[(i*dataNum):((i+1)*dataNum)])
    imaginaryAmplitude = np.dot(imaginaryW,inputDataNor[(i*dataNum):((i+1)*dataNum)])
    ##计算最终幅值
    amplitude[i] = realAmplitude*realAmplitude + imaginaryAmplitude*imaginaryAmplitude
    #print(i)
    #print(amplitude[i])
    #print(np.argmax(amplitude[i]))
np.save('./result/ampD1W1.npy',amplitude)