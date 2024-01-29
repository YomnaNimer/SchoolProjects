import matplotlib.pyplot as plt
from matplotlib import image as imagelib
import numpy as np
       # symbol duration
FileName = 'Ibraham-Lin.jpg'

try:
    img = (1 - (np.mean(imagelib.imread(FileName),axis=2)/256))**2
except:
    img = 1 - imagelib.imread(FileName)/256
    
L = np.shape(img)[0]
W = np.shape(img)[1]
N = W*16 #number of samples in each line.

t = np.linspace(0,W,N,endpoint=False)

N_lines = 1000 #change this
frequency = 0.25  #Change this
0
signal = np.cos(t*frequency)*0.3 + (1+(np.cos(t*frequency)>0).astype(int))/2

plt.figure(figsize=(10,12))
for k in range(0,L,int(L/N_lines)):
    A = (2*np.mean(img[k:k+int(L/N_lines),:],axis=0) + np.max(img[k:k+int(L/N_lines),:],axis=0))/3
    Line =  np.repeat(A,16) * signal  #np.real(mod(t,A,B))
    plt.plot(t,Line-1.3*k/int(L/N_lines),'k',linewidth=1+3*np.mean(np.abs(Line)**2))
plt.axis('off')
plt.savefig(FileName[:-4]+'Edited.jpg', bbox_inches='tight')