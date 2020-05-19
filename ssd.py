import numpy as np

def polar_spect(w): # polar spectrum => Mag, Phase
 
 return(np.concatenate(((np.sqrt(2)*np.absolute(w)/w.shape[-1]).reshape(w.shape[-1],1), (np.angle(w) + np.pi/4).reshape(w.shape[-1],1)), axis = 1))

def improt_data(path, type = 'csv'): # importing data ( path => str)
 
 if(type == 'csv'):
  
  try:
   q = np.loadtxt(path, delimiter = ';') # reading input
  except:
   q = np.loadtxt(path, delimiter = ',') # reading input
  t = q[:, 0] # time vector

  Ts = np.amin(np.diff(t)) # signal sampling period 

  f_t = q[:, 1] # signal magnitude in the time domain

 return({ 'time' : t, 'magnitude' : f_t, 'sampling' : Ts }) 

def export_data(m, path = "output.csv", type = 'csv'): # exporting data ( m => numpy matrix )

 if(type == 'csv'): # data export csv

  np.savetxt(path, m, delimiter = ';')
 
 return(1)

def tfd ( signal ): # discrete fourier transform ( signal => { 'time' : t, 'magnitude' : f_t, 'sampling' : Ts } )

 return({ 'frequency' : np.fft.fftfreq(signal['time'].shape[-1], signal['sampling']), 'transform' : np.fft.fft(signal['magnitude']) }) 
 
def symmetric_polar_spect(fft_input):# symmetric polar spectrum ( fft_input => { 'frequency' : fftfreq, 'transform' : fft } )

 freq = fft_input['frequency']

 v = polar_spect(fft_input['transform'])
 
 export_data(v, path = "rid.csv")

 return( np.concatenate(((freq.reshape(freq.shape[-1],1))[np.flip(np.argsort(v[:,0].T))],v[np.flip(np.argsort(v[:,0].T)),:]), axis = 1) )
 
def compact_polar_spect(polar_spect): # compact polar spectrum ( polar_spect => np.ndarray[ col1 = freq, col2 = Mag, col3 = phase ] )

 n = np.matrix(np.array([polar_spect[0,0], polar_spect[0,1], polar_spect[0,2]]))

 freq = polar_spect[:,0]

 for i, h in enumerate(freq):
 
  itemindex = np.where(freq == -h)

  if(len(itemindex[0])) and (itemindex[0][0] > i):

   if(freq[itemindex[0][0]] > freq[i]):
    
	j = itemindex[0][0]
   
   else:
    
	j = i
   
   n = np.vstack((n, np.array([freq[j],  (np.sqrt(2)*polar_spect[j,1]), polar_spect[j,2] + np.pi/4])))
  
  if(len(itemindex[0]) == 0):
   
   if(freq[i]<0):
    
	n = np.vstack((n, np.array([-freq[i], polar_spect[i,1], -polar_spect[i,2] - np.pi])))
 
 return(n) #( n => np.ndarray[ col1 = freq, col2 = Mag, col3 = phase ] )


def full_series(bh, time_): # transform polar spectrum into discrete time sinusoid signal ( bh => np.ndarray[ col1 = freq, col2 = Mag, col3 = phase ] , time_ = np.array) 

 O = np.zeros((time_.shape[-1], bh.shape[0]))
 
 for i, h in enumerate(bh):
  
  x = np.array(h)
  
  h = np.reshape(x, 3)
  
  O[:,i] = h[1]*np.sin(2*np.pi*h[0]*time_ + h[2])
 
 return(O) # O => ( np.ndarray[ col1 = A_1.sin(2.pi.f_1.time_ + phi_1), col2 = A_2.sin(2.pi.f_2.time_ + phi_2), ...,coln = A_n.sin(2.pi.f_n.time_ + phi_n) ] )


def main():
   
  inputfile = 'input.csv' # input's file path
   
  outputploarspet = 'polarSpectrum.csv' # polar spectrum, output file
   
  outputwave = 'wavesMatrix.csv' # matrix of output composed signal in the discrete time domain, output file
  
  x = improt_data(inputfile)

  X = tfd ( x )

  W = compact_polar_spect(symmetric_polar_spect( X ))

  export_data(W, path = outputploarspet)

  Y = full_series(W, x['time'])

  export_data(np.concatenate((x['time'].reshape(x['time'].shape[-1],1),Y), axis = 1), path = outputwave, type = 'csv')


if __name__ == "__main__":

   main()
