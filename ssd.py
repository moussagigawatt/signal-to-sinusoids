import numpy as np

def polar_spect(w):
 return(np.concatenate(((np.sqrt(2)*np.absolute(w)/w.shape[-1]).reshape(w.shape[-1],1), (np.angle(w) + np.pi/4).reshape(w.shape[-1],1)), axis = 1))


q = np.loadtxt("input.csv", delimiter = ',')

t = q[:, 0]
Ts = np.amin(np.diff(t))
f_t = q[:, 1]

sp = np.fft.fft(f_t)
freq = np.fft.fftfreq(t.shape[-1],Ts)

v = polar_spect(sp)

bh = np.concatenate((freq.reshape(freq.shape[-1],1),v), axis = 1)

np.savetxt("polarSpectrum.csv", bh, delimiter = ',')

O = bh[:,1]*np.sin(np.matmul(2*np.pi*bh[:,0].reshape(bh[:,0].shape[-1],1),t.reshape(t.shape[-1],1).T)+ bh[:,2])

np.savetxt("sinusMatrix.csv", np.concatenate((t.reshape(t.shape[-1],1),O), axis = 1), delimiter = ',')