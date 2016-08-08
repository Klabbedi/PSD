# PSD

Plotting [Power Spectral Density](http://matplotlib.org/1.2.1/api/pyplot_api.html?highlight=psd#matplotlib.pyplot.psd) in [Pythonista for iOS](http://omz-software.com/pythonista/).

I wanted to see if I could find out the centrifugation speed of my old washing machine using some vibration analysis in Numpy using fft etc. So I wrote a little script that captured accelerometer data at 80Hz for one minute and then placed my iPad on top of the machine during centrifugation. I stored the data in an array in an .npy file. My graphs looked ok, I think, with a dominant peak at about 12Hz(12*60=720rpm...this probably explains why my clothes are so wet coming out from the machine.

For more details see: https://forum.omz-software.com/topic/3393/why-do-i-get-diffrent-graphs-running-this-code-with-python-2-7-or-3-5
