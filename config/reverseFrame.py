def transfer(frameData):
	#转成按字节倒序（即高位字节在最后，低位字节在最前）的64比特的帧数据
	return frameData[56:64]+frameData[48:56]+frameData[40:48]+frameData[32:40]+\
        frameData[24:32]+frameData[16:24]+frameData[8:16]+frameData[0:8]+'\n'

#读入40比特的帧数据
with open('./config/fourierConfigFrame.txt','r') as net64b:
	frames = net64b.readlines()
	framesTrans = [transfer(f) for f in frames]

#写入64比特的帧数据,networkName64b.txt or networkName64b_rever.txt 
with open('./config/fourierConfigFrameReverse.txt','w') as net64bReverse:
	temp=[net64bReverse.write(f) for f in framesTrans]