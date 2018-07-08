frameTitle = '010000'
chipAndCoreAddr = '00000000000000000000'

with open('./config/fourierFullInputFrame.txt','w') as inputFile:
    inputFile.write('begin\n')
    for axonAddr in range(441*2):
        inputFile.write(frameTitle+chipAndCoreAddr+'{:0>10b}'.format(axonAddr)+'0000\n')
    inputFile.write('inputFrameEnd\n')
    inputFile.write('0110000000000000000000000000000000000000\n')
    inputFile.write('startFrameEnd')