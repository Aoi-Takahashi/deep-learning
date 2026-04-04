import numpy as np


# Step関数
def step_function(x):
    return np.array(x > 0, dtype=int)


# Sigmoid関数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
