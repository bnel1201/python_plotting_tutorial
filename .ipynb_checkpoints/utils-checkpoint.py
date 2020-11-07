import numpy as np
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def random_heights(n=8): return np.abs(np.random.randn(n))

def random_names(height): return [get_random_string(3) for i in range(len(height))]