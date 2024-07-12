import numpy as np

def generate_pink_noise(size, mean=0, std=1):
    white_noise = np.random.normal(mean, std, size)
    fft = np.fft.rfft(white_noise)
    freqs = np.fft.rfftfreq(size)
    pink_filter = np.where(freqs == 0, 0, 1 / np.sqrt(np.maximum(freqs, 1e-6)))
    pink_noise = np.fft.irfft(fft * pink_filter, n=size)
    pink_noise = (pink_noise - np.mean(pink_noise)) / np.std(pink_noise) * std + mean
    return pink_noise

def generate_noisy_signal(clean_signal, noise_signal, intensity):
    noise_scaled = noise_signal[:len(clean_signal)] * intensity
    noisy_signal = clean_signal + noise_scaled
    return noisy_signal
