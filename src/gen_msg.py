"""
Generates message signals to use for testing and simulations.
"""

import numpy as np

# Generates a random binary message signal of a given size.
# Inputting a seed is optional.
def gen_random_msg(size, seed=None):
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(0, 2, size=size)

