import numpy as np
import time

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