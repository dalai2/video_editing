from scipy.io import wavfile
import noisereduce as nr
import numpy as np
# load data
rate, data = wavfile.read("extracted_audio.wav")
orig_shape = data.shape
data = np.reshape(data, (2, -1))
# perform noise reduction
reduced_noise = nr.reduce_noise(y=data,
                                sr=rate)
wavfile.write("mywav_reduced_noise.wav", rate, reduced_noise.reshape(orig_shape))