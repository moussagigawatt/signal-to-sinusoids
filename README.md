# signal-to-sinusoids
The signal to sinusoids decomposer is a python module that helps the spectral analysis of 1D discrete signal.
Decomposition functions (Based on TFD)

### $$s(t) = \sum_{k=0}^n A(f_k)\sin(2 \pi f_kt + \phi(f_k))$$
# Features:

  - Extracting amplitude, spectrum and phases $${(f_k, A(f_k), \phi(f_k)),\ k \in(0:n)}$$
  - Sinusoid matrix {time representation sinusoids composing the input signal}

### Envirement

Signal to sinusoids decomposer uses python numpy module to work properly.

### I/O files

Signal to sinusoids decomposer is currently uses a set of editable in/out-puts file paths. Instructions on how to use them in your own application are linked below.
  #### 1. input.csv
CSV file composed of two columns that contain sampling time; the signal in that particular instant. (separation = ',')
 - Example:
 
| Time |Values |
| ------ | ------ |
| $$t_0$$ |$$s(t_0)$$|
|$$t_1$$|$$s(t_1)$$|
...|... 
| $$t_n$$ |$$s(t_n)$$|

   #### 2. polarSpectrum.csv
CSV file composed of three columns that contain frequencies spectrum; the amplitude; and initial phase of the sinusoid. (separation = ',')
 - Example:
 
|Frequencies |Amplitudes | Phases |
| ------ | ------ | ------ |
| $$f_0$$| $$A(f_0)$$ | $$\phi(t_0)$$|
| $$f_1$$|$$A(f_1)$$| $$\phi(t_1)$$|
...|...|... 
| $$f_n$$ |$$A(f_n)$$| $$\phi(t_n)$$|

   #### 3. wavesMatrix.csv
CSV file composed of N columns that contain sampling time; and sinusoids composing the initial signal build from amplitudes, frequencies and phases in polarSpectrum.csv file. (separation = ',')
 - Example:
 
|Time|$$H_0$$|$$H_1$$|...|$$H_n$$|
|------|------|------|------|------|
| $$t_0$$ | $$A(f_0).sin(2.\pi.f_0.t_0 + \phi(f_0))$$| $$A(f_1).sin(2.\pi.f_1.t_0 + \phi(f_1))$$| ...|$$A(f_n).sin(2.\pi.f_n.t_0 + \phi(f_n))$$
| $$t_1$$|$$A(f_0).sin(2.\pi.f_0.t_1 + \phi(f_0))$$| $$A(f_1).sin(2.\pi.f_1.t_1 + \phi(f_1))$$|...| $$A(f_n).sin(2.\pi.f_n.t_1 + \phi(f_n))$$
...|...|... |...|... 
| $$t_n$$ |$$A(f_0).sin(2.\pi.f_0.t_n + \phi(f_0))$$| $$A(f_1).sin(2.\pi.f_1.t_n + \phi(f_1))$$| ...|$$A(f_n).sin(2.\pi.f_n.t_n + \phi(f_n)))$$|

### Todos

 - Building command line input interface
 - Integrating JSON as input/output supported format
 - Buildig web API serving decomposing random discrete signals 

License
----

MIT

**Free Software, provided by $$Ker(\Gamma)$$**
