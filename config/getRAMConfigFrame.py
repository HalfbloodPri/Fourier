import numpy as np
import time

class neuron():
    def __init__(self):
        self.tick = '0000'
        self.potential = '0000000000000000000'
        self.weight0 = '000000001'
        self.weight1 = '000000001'
        self.weight2 = '000000001'
        self.weight3 = '000000001'
        self.weightDetStoch = '0'
        self.leakWeight = '0000000000'
        self.leakDetStoch = '0'
        self.leakReversalFlag = '0'
        self.thresholdPos = '000000000000000001'
        self.thresholdNeg = '111111111111111111'
        self.thresholdMaskCtrl = '00000'
        self.thresholdNegMode = '1'
        self.resetWeight = '0000000000000000000'
        self.resetMode = '00'

#生成64bit的配置帧
frameAppended = '0000000000000000000'
frameTitle = '000100'
chipAndCoreAddr = ['00000000000000000000','00000000000000100000']
with open('./config/axonType64bit.txt','w') as randomSeedConfigFile:
    for addr in chipAndCoreAddr:
        coreYAddr = addr[15:20]
        for j in range(int(2048/64)):
            for i in range(4):
                data = 0
                randomSeedConfigFile.write(frameAppended + coreYAddr + frameTitle + addr + '{:0>14b}'.format(data)+'\n')
            data = 0
            randomSeedConfigFile.write(frameAppended + coreYAddr + frameTitle + addr + '{:0>8b}'.format(data)+'000000\n')