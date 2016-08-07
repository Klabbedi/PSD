# coding: utf-8

import console
import motion
import time
import numpy as np

# Start program
console.clear()
print('-------------------')
print('Starting program...')
test_time = 10.0  # Capture time in seconds
print('Capture time: '+str(test_time))
test_freq = 90.0  # Sample rate in Hz. Max 100.0?
print('Sample rate: '+str(test_freq)+'Hz')
pause_time = 3.0  # Pause time before data capture
print('Pause time: '+str(pause_time))
file_name = 'test.npy'
num_points = test_time * test_freq  # Number of points in anlysis

print('Creating numpy array of zeros...')
data = np.zeros((num_points, 3))  # Create Numpy array of zeros

print('Create time vector...')
time_vector = np.linspace(0.0, test_time, num=num_points).reshape((num_points,1))

print('Pause before start...')
time.sleep(pause_time)  # Insert pause before capture starts

print('Starting data capture...')
n = 0
motion.start_updates()
while n < num_points:
	data[n] = motion.get_user_acceleration()
	n = n + 1
	time.sleep(1.0/test_freq)
motion.stop_updates()

print('Adding time vector to array...')
data = np.concatenate((data, time_vector), axis=1)

print('Saving '+str(num_points)+' points to '+str(file_name))
np.save(file_name, data)
print('-------------------')
