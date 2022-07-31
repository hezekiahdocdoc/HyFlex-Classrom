# SDR Reciever

from rtlsdr import RtlSdr
#from matplotlib 

sdr = RtlSdr()

def get_freq(samp_rate, cent_freq, freq_cor, gain):
    sdr.sample_rate = samp_rate # Hz (Note: BW = Fs/2)
    sdr.center_freq = cent_freq # Hz
    sdr.freq_correction = freq_cor
    sdr.gain = gain
    print(sdr.read_samples(512)) # Increase resolution


get_freq(2.048e6, 70e6, 60, 'auto')
