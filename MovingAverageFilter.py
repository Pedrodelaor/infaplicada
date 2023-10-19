import numpy as np
import matplotlib.pyplot as plt

# Generate a noisy signal
fs = 1000
t = np.arange(fs) / fs
signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.random.randn(fs)

# Apply a moving average filter with a window length of 10 samples
window_length = 10
filtered_signal = np.convolve(signal, np.ones(window_length) / window_length, mode='same')

# Plot the original signal and the filtered signal
fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(t, signal)
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Amplitude')
axs[1].plot(t, filtered_signal)
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Amplitude')
plt.show()
##################################################
