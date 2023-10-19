import numpy as np
import matplotlib.pyplot as plt

# Generate a signal with random values between -100 and 100
signal = np.random.randint(-100, 100, size=1000)

# Scale the signal to have a maximum absolute value of 1
scaled_signal = signal / np.max(np.abs(signal))

# Normalize the signal to have a mean of 0 and a standard deviation of 1
normalized_signal = (signal - np.mean(signal)) / np.std(signal)

# Plot the original signal, the scaled signal, and the normalized signal
fig, axs = plt.subplots(3, 1, figsize=(8, 6))
axs[0].plot(signal)
axs[0].set_xlabel('Sample')
axs[0].set_ylabel('Amplitude')
axs[1].plot(scaled_signal)
axs[1].set_xlabel('Sample')
axs[1].set_ylabel('Amplitude')
axs[2].plot(normalized_signal)
axs[2].set_xlabel('Sample')
axs[2].set_ylabel('Amplitude')
plt.show()