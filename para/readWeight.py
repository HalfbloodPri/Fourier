import numpy as np 

realWInt = np.load('./para/realWInt.npy')
imaginaryWInt = np.load('./para/imaginaryWInt.npy')

for i in range(88):
    print('#',i)
    print(realWInt[i])
    print(imaginaryWInt[i])