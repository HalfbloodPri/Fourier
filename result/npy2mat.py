import scipy.io as scio
import numpy as np 
#import h5py

amp = np.load('./result/ampFloat.npy')
scio.savemat('./result/ampFloat.mat',{'ampFloat':amp})