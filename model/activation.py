import numpy as np


# Step関数
def step_function(x):
    return np.array(x > 0, dtype=int)
