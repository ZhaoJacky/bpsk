"""
Main module to show one use case for the program.
"""

import gen_msg
import modulator
import matplotlib.pyplot as plt
import numpy as np

def main():

    # Generate a random message signal.
    msg = gen_msg.gen_random_msg(20, seed=42)
    modulated_signal = modulator.bpsk_modulate(msg, 5, fs=1000, fc=100)
    t = np.linspace(0, len(msg) * (5/100), len(modulated_signal), endpoint=False)

    # Plot the modulated signal.
    plt.plot(t, modulated_signal)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("BPSK Modulated Signal")
    plt.show()

if __name__ == "__main__":
    main()