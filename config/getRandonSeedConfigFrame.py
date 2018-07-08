import numpy as np
import time

#生成64bit的配置帧
frameAppended = '0000000000000000000'
frameTitle = '000000'
chipAndCoreAddr = ['00000000000000000000']
with open('./config/randomSeed64bit.txt','w') as randomSeedConfigFile:
    for addr in chipAndCoreAddr:
        coreYAddr = addr[15:20]
        for i in range(4):
            data = np.random.randint(0,(1<<14)-1)
            randomSeedConfigFile.write(frameAppended + coreYAddr + frameTitle + addr + '{:0>14b}'.format(data)+'\n')
            time.sleep(0.001)
        data = np.random.randint(0,(1<<8)-1)
        randomSeedConfigFile.write(frameAppended + coreYAddr + frameTitle + addr + '{:0>8b}'.format(data)+'000000\n')