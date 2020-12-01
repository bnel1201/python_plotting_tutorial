import numpy as np
import pandas as pd
import random
import string


def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def random_heights(n=8): return np.abs(np.random.randn(n))


def random_names(height): return [get_random_string(3) for i in range(len(height))]


def make_fake_dataframe(ngroups=6):
    means = [random_heights() for i in range(ngroups)]
    stds = [random_heights()/10 for i in range(ngroups)]
    names = random_names(means[0])

    # %%
    z = dict()
    dicts = [{f'group {i} mean': mean, f'group {i} std': std} for mean, std, i in zip(means, stds, range(len(means)))]
    [z.update(d) for d in dicts]
    return pd.DataFrame(z, index = names)