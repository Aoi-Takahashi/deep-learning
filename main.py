import numpy as np
from matplotlib import pyplot as plt

from model.activation import step_function


def main():
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)  # y軸の範囲を指定
    plt.savefig("figure/Step関数.png")


if __name__ == "__main__":
    main()
