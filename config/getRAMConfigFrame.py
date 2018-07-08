import numpy as np
import time

class neuron():
    def __init__(self):
        self.tick = '0000'
        self.potential = '0000000000000000000'
        self.weight0 = '00000000001'
        self.weight1 = '11111111111'
        self.weight2 = '00000000000'
        self.weight3 = '00000000000'
        self.weightDetStoch = '0'
        self.leakWeight = '0000000000000000000'
        self.leakDetStoch = '0'
        self.leakReversalFlag = '0'
        self.thresholdPos = '000000000000000001'
        self.thresholdNeg = '000000000000000000'
        self.thresholdMaskCtrl = '00000'
        self.thresholdNegMode = '1'
        self.resetWeight = '0000000000000000000'
        self.resetMode = '01'
    
    def setWeight(self,w0,w1,w2,w3):
        self.weight0 = w0
        self.weight1 = w1
        self.weight2 = w2
        self.weight3 = w3

    def setThresholdPos(self,thresholdPos):
        self.thresholdPos = thresholdPos

#生成64bit的配置帧
frameAppended = '0000000000000000000'
frameTitle = '001000'
chipAndCoreAddr = '00000000000000000000'
realW = np.load('./para/realW.npy')     #pianoKeyNum*dataNum
imaginaryW = np.load('./para/imaginaryW.npy')    #pianoKeyNum*dataNum
with open('./config/RAM64bit.txt','w') as RAMConfigFile:
    coreYAddr = chipAndCoreAddr[15:20]
    aimChipAndCoreAddr = '00001000000000000000'
    neuron0 = neuron()
    #实部正常计算的neuron的配置，0~87;
    for neuronAddr in range(88):
        configData = ''
        wij = '0'*(1024-441*2)
        connection = ''
        for i in range(441):
            if realW[neuronAddr][440-i] == 0:
                connection += '0'
            else:
                connection += '1'
        wij += connection + connection
        configData += wij + '000000000' + neuron0.tick + '{:0>10b}'.format(neuronAddr) + aimChipAndCoreAddr +\
                    neuron0.resetMode + neuron0.resetWeight + '0' + neuron0.thresholdMaskCtrl +\
                    neuron0.thresholdNegMode + neuron0.thresholdNeg + neuron0.thresholdPos +\
                    neuron0.leakReversalFlag + neuron0.leakDetStoch + neuron0.leakWeight + \
                    neuron0.weightDetStoch + neuron0.weight3 + neuron0.weight2 + neuron0.weight1 +\
                    neuron0.weight0 + neuron0.potential
        for i in range (int(1216/4)):
            RAMConfigFile.write(frameAppended + coreYAddr + frameTitle + chipAndCoreAddr + \
                            '{:0>10b}'.format(neuronAddr) + configData[(4*i):(4*(i+1))] + '\n')
    #虚部正常计算的neuron的配置，88~(88*2-1);
    for neuronAddr in range(88,88*2):
        configData = ''
        wij = '0'*(1024-441*2)
        connection = ''
        for i in range(441):
            if imaginaryW[neuronAddr-88][440-i] == 0:
                connection += '0'
            else:
                connection += '1'
        wij += connection + connection
        configData += wij + '000000000' + neuron0.tick + '{:0>10b}'.format(neuronAddr) + aimChipAndCoreAddr +\
                    neuron0.resetMode + neuron0.resetWeight + '0' + neuron0.thresholdMaskCtrl +\
                    neuron0.thresholdNegMode + neuron0.thresholdNeg + neuron0.thresholdPos +\
                    neuron0.leakReversalFlag + neuron0.leakDetStoch + neuron0.leakWeight + \
                    neuron0.weightDetStoch + neuron0.weight3 + neuron0.weight2 + neuron0.weight1 +\
                    neuron0.weight0 + neuron0.potential
        for i in range (int(1216/4)):
            RAMConfigFile.write(frameAppended + coreYAddr + frameTitle + chipAndCoreAddr + \
                            '{:0>10b}'.format(neuronAddr) + configData[(4*i):(4*(i+1))] + '\n')

    neuron0.setWeight('11111111111','00000000001','00000000000','00000000000')
    #实部互补计算的neuron的配置，88*2~(88*3-1);
    for neuronAddr in range(88*2,88*3):
        configData = ''
        wij = '0'*(1024-441*2)
        connection = ''
        for i in range(441):
            if realW[neuronAddr-88*2][440-i] == 0:
                connection += '0'
            else:
                connection += '1'
        wij += connection + connection
        configData += wij + '000000000' + neuron0.tick + '{:0>10b}'.format(neuronAddr) + aimChipAndCoreAddr +\
                    neuron0.resetMode + neuron0.resetWeight + '0' + neuron0.thresholdMaskCtrl +\
                    neuron0.thresholdNegMode + neuron0.thresholdNeg + neuron0.thresholdPos +\
                    neuron0.leakReversalFlag + neuron0.leakDetStoch + neuron0.leakWeight + \
                    neuron0.weightDetStoch + neuron0.weight3 + neuron0.weight2 + neuron0.weight1 +\
                    neuron0.weight0 + neuron0.potential
        for i in range (int(1216/4)):
            RAMConfigFile.write(frameAppended + coreYAddr + frameTitle + chipAndCoreAddr + \
                            '{:0>10b}'.format(neuronAddr) + configData[(4*i):(4*(i+1))] + '\n')
    #虚部互补计算的neuron的配置，88*3~(88*4-1);
    for neuronAddr in range(88*3,88*4):
        configData = ''
        wij = '0'*(1024-441*2)
        connection = ''
        for i in range(441):
            if imaginaryW[neuronAddr-88*3][440-i] == 0:
                connection += '0'
            else:
                connection += '1'
        wij += connection + connection
        configData += wij + '000000000' + neuron0.tick + '{:0>10b}'.format(neuronAddr) + aimChipAndCoreAddr +\
                    neuron0.resetMode + neuron0.resetWeight + '0' + neuron0.thresholdMaskCtrl +\
                    neuron0.thresholdNegMode + neuron0.thresholdNeg + neuron0.thresholdPos +\
                    neuron0.leakReversalFlag + neuron0.leakDetStoch + neuron0.leakWeight + \
                    neuron0.weightDetStoch + neuron0.weight3 + neuron0.weight2 + neuron0.weight1 +\
                    neuron0.weight0 + neuron0.potential
        for i in range (int(1216/4)):
            RAMConfigFile.write(frameAppended + coreYAddr + frameTitle + chipAndCoreAddr + \
                            '{:0>10b}'.format(neuronAddr) + configData[(4*i):(4*(i+1))] + '\n')
    #其他无关neuron的配置，88*4~1023；
    for neuronAddr in range(88*4,1024):
        configData = ''
        wij = '0'*1024
        configData += wij + '000000000' + neuron0.tick + '{:0>10b}'.format(neuronAddr) + aimChipAndCoreAddr +\
                    neuron0.resetMode + neuron0.resetWeight + '0' + neuron0.thresholdMaskCtrl +\
                    neuron0.thresholdNegMode + neuron0.thresholdNeg + neuron0.thresholdPos +\
                    neuron0.leakReversalFlag + neuron0.leakDetStoch + neuron0.leakWeight + \
                    neuron0.weightDetStoch + neuron0.weight3 + neuron0.weight2 + neuron0.weight1 +\
                    neuron0.weight0 + neuron0.potential
        for i in range (int(1216/4)):
            RAMConfigFile.write(frameAppended + coreYAddr + frameTitle + chipAndCoreAddr + \
                            '{:0>10b}'.format(neuronAddr) + configData[(4*i):(4*(i+1))] + '\n')