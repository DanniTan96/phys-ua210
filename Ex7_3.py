import numpy as np 
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

psig = np.loadtxt('piano.txt')
tsig = np.loadtxt('trumpet.txt')
N = 10000
freq = fftfreq(100000, 1/44100)
t = np.linspace(0, 2.268, 100000)

ckp = fft(psig)
ckp_amp = np.sqrt(np.real(ckp)**2 + np.imag(ckp)**2)
plt.figure(1)
plt.plot(freq[0:N], ckp_amp[0:N], '-b', label='Piano FFT')
plt.xlabel('Frequency (Hz)')
plt.ylabel(r'$c_k$')
plt.legend(loc='best')
plt.savefig('Ex7_3_Piano_FFT.png')

ckt = fft(tsig)
ckt_amp = np.sqrt(np.real(ckt)**2 + np.imag(ckt)**2)
plt.figure(2)
plt.plot(freq[0:N], ckt_amp[0:N], '-k', label='Trumpet FFT')
plt.xlabel('Frequency(Hz)')
plt.ylabel(r'$c_k$')
plt.legend(loc='best')
plt.savefig('Ex7_3_Trumpet_FFT.png')

plt.figure(3, figsize=(8., 5.))
plt.plot(t, psig, '-b', label='Piano Waveform')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (Signal Units)')
plt.legend(loc='best')
plt.savefig('Ex7_3_Piano_Signal.png')

plt.figure(4, figsize=(8., 5.))
plt.plot(t, tsig, '-k', label='Trumpet Waveform')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (Signal Units)')
plt.legend(loc='best')
plt.savefig('Ex7_3_Trumpet_Signal.png')



