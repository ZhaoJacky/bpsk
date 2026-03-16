"""
Functions that modulate message signals.
"""
import numpy as np

def symbol_map(msg):
    # Maps 0 to -1 and 1 to 1.
    return 2 * msg - 1

# Modulates a given message using BPSK using a specified sampling frequency,
# carrier frequency, and cycles per symbol.
def bpsk_modulate(msg, cycles, fs, fc):

    # Maps the message bits to -1 or 1.
    symbol_mapped = symbol_map(msg)

    # Creates a time vector per symbol based on the cycles, carrier frequency,
    # and sampling frequency.
    time_per_symbol = cycles / fc
    t = np.linspace(0, time_per_symbol, int(time_per_symbol * fs), endpoint=False)

    modulated_signal = np.array([])
    
    # Creates a modulated signal using a cosine at the carrier frequency based 
    # on the symbols.
    for symbol in symbol_mapped:
        chunk = symbol * np.cos(2 * np.pi * fc * t)
        modulated_signal = np.concatenate([modulated_signal, chunk])
    
    return modulated_signal
