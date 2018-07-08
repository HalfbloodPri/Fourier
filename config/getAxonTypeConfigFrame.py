import numpy as np
import time

#生成64bit的配置帧
frameAppended = '0000000000000000000'
frameTitle = '000100'
chipAndCoreAddr = ['00000000000000000000']
axonType = '0'*(2048-441*4) + '01'*441 + '00'*441
with open('./config/axonType64bit.txt','w') as axonTypeConfigFile:
    for addr in chipAndCoreAddr:
        coreYAddr = addr[15:20]
        for j in range(int(2048/64)):
            partOfAxonType = axonType[(64*j):(64*(j+1))]
            for i in range(4):
                axonTypeConfigFile.write(frameAppended + coreYAddr + frameTitle + addr + partOfAxonType[(14*i):(14*(i+1))]+'\n')
            axonTypeConfigFile.write(frameAppended + coreYAddr + frameTitle + addr + partOfAxonType[(14*4):64]+'000000\n')