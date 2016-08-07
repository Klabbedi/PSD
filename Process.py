# coding: utf-8

import console
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as ml

# Start program
console.clear()
print('-------------------')
print('Starting program...')
file_name = 'test.npy'
print('Loading '+str(file_name)+'...')
data = np.load(file_name). # data[:, 0] is X acc, data[:, 1] is Y acc, data[:, 2] is Z acc and data[:, 3] is the time vector.

print('Plotting X acceleration...')
fig_x = plt.figure()
plt.plot(data[:, 3], data[:, 0], 'r-')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (g?)')
plt.title('X Acceleration')
plt.show()

print('Create FFT for X acceleration...')
k = np.arange(len(data))  # Create point vector
freq_two_side = k/data[-1, 3] # Create two sided freq range. data[-1,3]=total test time
freq_one_side = freq_two_side[list(range(len(data)//2))]
fftx_two_side = np.fft.fft(data[:, 0])/len(data)
fftx_one_side = fftx_two_side[list(range(len(data)//2))]
fftx_one_side_abs = abs(fftx_one_side)

print('Plot FFT for X acceleration...')
fig_fftx = plt.figure()
plt.plot(freq_one_side, fftx_one_side_abs, 'g-')
plt.xlabel('Freq (Hz)')
plt.ylabel('|Acceleration| (g?)')
plt.title('FFT X Acceleration')
plt.show()

print('Plot PSD for X')
fig_mag = plt.figure()
plt.psd(data[:, 0].flatten(), NFFT=256, Fs=len(data)/data[-1,3], window=ml.window_hanning)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power/Frequency (dB/Hz?)')
plt.title('PSD X')
plt.show()
