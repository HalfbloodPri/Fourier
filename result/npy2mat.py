import scipy.io as scio
import numpy as np 
#import h5py

amp = np.load('./para/imaginaryWInt.npy')
scio.savemat('./para/imaginaryWInt.mat',{'imaginaryWInt':amp})