import numpy as np
import librosa
def calculate_mfcc(signal, sr, win_len, hop_len, n_mfcc=20, pre_em=False):
    if pre_em:
        pre_emphasis = 0.97
        signal = np.append(signal[0], signal[1:] - pre_emphasis * signal[:-1])
    mel_spec = librosa.feature.melspectrogram(y=signal, sr=sr, n_fft=win_len, hop_length=hop_len,\
                                             window='hamming')
    mfcc = librosa.feature.mfcc(S=librosa.power_to_db(mel_spec), sr=sr, n_mfcc=n_mfcc)
    return mfcc
