import numpy
import time

timeBegin = time.time()
timeRuning = time.time()

#读入按字节倒序的64比特的帧数据，并转成bytes类型数据，存入.npy文件中
with open('./config/fourierConfigFrameReverse.txt','r') as net64b:
	frames = net64b.read().splitlines()
	framesNum = len(frames)
	tempData = numpy.zeros(framesNum).astype('uint64')
	for i,f in enumerate(frames):
		tempData[i] = int(f,2)
		if i%10000 == 0:
			print(i,'----',time.time()-timeRuning)
			timeRuning = time.time()

timeRuning = time.time()
tempData.dtype = 'uint8'
frameBytes = bytes(tempData)
print('Transform ----',time.time()-timeRuning)

numpy.save('./config/fourierConfig.npy',numpy.array(frameBytes))
timeEnd = time.time()
print(timeEnd-timeBegin)