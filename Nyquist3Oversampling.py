import numpy as np
import matplotlib.pyplot as plt

# Define the signal
fs = 1000
t = np.linspace(0, 1, fs)
signal = np.sin(2 * np.pi * 100 * t) + 0.5 * np.sin(2 * np.pi * 200 * t)

# Compute the Fourier Transform of the original signal
freqs = np.fft.rfftfreq(len(signal), d=1/fs)
fft_original = np.abs(np.fft.rfft(signal))

# Oversample the signal
fs_new = 2000
t_new = np.linspace(0, 1, fs_new)
signal_new = np.interp(t_new, t, signal)

# Compute the Fourier Transform of the oversampled signal
freqs_new = np.fft.rfftfreq(len(signal_new), d=1/fs_new)
fft_new = np.abs(np.fft.rfft(signal_new))

# Plot the original signal and its Fourier Transform, and the oversampled signal and its Fourier Transform
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].plot(t, signal)
axs[0, 0].set_xlabel('Time (s)')
axs[0, 0].set_ylabel('Amplitude')
axs[1, 0].plot(freqs, fft_original)
axs[1, 0].set_xlabel('Frequency (Hz)')
axs[1, 0].set_ylabel('Magnitude')
axs[0, 1].plot(t_new, signal_new)
axs[0, 1].set_xlabel('Time (s)')
axs[0, 1].set_ylabel('Amplitude')
axs[1, 1].plot(freqs_new, fft_new)
axs[1, 1].set_xlabel('Frequency (Hz)')
axs[1, 1].set_ylabel('Magnitude')
plt.show()

#This code generates a signal consisting of two sine waves with frequencies of 100 Hz and 200 Hz, respectively, and samples it at a rate of 1000 Hz. The Fourier Transform of the original signal is then computed and plotted.

#The signal is then oversampled by a factor of 2, i.e., the sampling rate is doubled to 2000 Hz, using the interp function. The Fourier Transform of the oversampled signal is then computed and plotted.

